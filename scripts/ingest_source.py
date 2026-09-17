#!/usr/bin/env python3
"""
Reusable ingestion pipeline for a new question source: extract, deduplicate
against the current bank, and append the unique survivors directly into
ia_clean.md or quiz_clean.md.

This exists because three earlier one-off scripts (convert_chris_ia.py,
convert_desmond_ia.py, the quiz_4.md half of convert_chris_quiz.py) each
reimplemented the same "N. question / A-D options / Answer: X" extraction
and the same "find unique survivors, append to a *_clean.md file" logic.
Future sources in this shape should use this module instead of copying that
logic again.

Two building blocks:
  extract_numbered_qa(text)   Parse "N. question / A-D options / Answer: X"
                               text (the shape produced by most PDF-to-text
                               extractions of exam-review question banks)
                               into a list of {body, options, answer_letter,
                               answer_text, explanation} dicts. Handles
                               multi-line wrapped questions, options and
                               answers; both MCQ and fill-in questions;
                               MCQ answers may repeat the option text
                               ("Answer: C. text") or a bare answer letter.
  dedupe_against_bank(qs)     Split a list of such dicts into (unique, dup)
                               against the current questions.json, using the
                               exact same normalized-body-prefix key the main
                               parser's own deduplicate() function uses, so
                               "unique" here means the same thing it means
                               everywhere else in this pipeline.

Command-line usage:
    python scripts/ingest_source.py \\
        --source "data_files/received qus/SK_ia.pdf" \\
        --target ia_bank --batch sk_ia --section "SK's Exam Review" \\
        --explanations-json explanations.json

--target is "ia_bank" (appends to data_files/ia_bank/ia_clean.md) or
"quiz_bank" (appends to data_files/quiz_bank/quiz_clean.md). PDFs are
converted to text automatically if PyMuPDF (import name "fitz") is
importable; otherwise pass a pre-extracted .txt/.md file as --source.

Any unique question with no source explanation is left with a
"NEEDS_EXPLANATION" placeholder and printed to stderr rather than silently
skipped, so genuine analysis gets written before publishing, the same
standard every other source in this bank was held to. Re-run with
--explanations-json pointing at a {body_prefix: explanation} file to fill
those in without re-touching everything else.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from scripts.parse_security_bank import normalize_text, classify_part, PART_TITLES

NEEDS_EXPLANATION = "NEEDS_EXPLANATION"


def _read_source_text(source: Path) -> str:
    if source.suffix.lower() == ".pdf":
        try:
            import fitz  # PyMuPDF
        except ImportError as exc:
            raise SystemExit(
                "PyMuPDF (pip install pymupdf) is required to read a PDF source, "
                "or pre-extract the text yourself and pass a .txt/.md --source."
            ) from exc
        doc = fitz.open(str(source))
        return "\n".join(page.get_text() for page in doc)
    return source.read_text(encoding="utf-8")


def extract_numbered_qa(text: str) -> list[dict]:
    """Parse the common 'N. question / A-D options / Answer: X' shape.

    Each question starts at a line matching ^\\d+\\. and continues (possibly
    across several wrapped lines) until an option line (^[A-D]\\.) or an
    'Answer:' line is seen. Options accumulate the same way. The answer line
    may give a bare letter, a letter plus repeated option text, or (for a
    fill-in with no options) the answer text directly; it may also wrap onto
    following lines until the next question number or a blank-then-heading
    boundary. Any explanation text between the answer and the next question
    number is captured as-is.
    """
    lines = [l.rstrip() for l in text.split("\n")]
    n = len(lines)
    i = 0
    questions: list[dict] = []

    q_start = re.compile(r"^(\d+)\.\s*(.*)$")
    opt_line = re.compile(r"^([A-D])\.\s+(.+)$")
    ans_line = re.compile(r"^Answer:\s*(.*)$", re.IGNORECASE)

    while i < n:
        s = lines[i].strip()
        if not s:
            i += 1
            continue
        m = q_start.match(s)
        if not m:
            i += 1
            continue

        body_lines = [m.group(2).strip()]
        i += 1
        while i < n and lines[i].strip() and not opt_line.match(lines[i].strip()) and not ans_line.match(lines[i].strip()):
            body_lines.append(lines[i].strip())
            i += 1
        body = " ".join(l for l in body_lines if l)

        # Options and their wrapped continuation lines are interleaved: an
        # option's text can wrap onto an unlettered line before the *next*
        # lettered option appears, so this must stay one loop rather than a
        # "collect options" pass followed by a separate "collect wraps" pass,
        # or a wrap in the middle of the list stops option collection early
        # and strands the remaining options unread.
        options: list[tuple[str, str]] = []
        while i < n:
            s2 = lines[i].strip()
            if ans_line.match(s2):
                break
            om = opt_line.match(s2)
            if om:
                options.append((om.group(1), om.group(2)))
                i += 1
                continue
            if not s2:
                i += 1
                continue
            if options:
                letter, prev_text = options[-1]
                options[-1] = (letter, prev_text + " " + s2)
                i += 1
                continue
            # no options yet and not an Answer line: stray body-wrap text
            body += " " + s2
            i += 1

        while i < n and not lines[i].strip():
            i += 1
        if i >= n:
            questions.append({"body": body, "options": options, "answer_letter": None, "answer_text": "", "explanation": ""})
            break
        am = ans_line.match(lines[i].strip())
        if not am:
            # malformed: no recognizable answer, record as unanswered rather
            # than misattributing a later line
            questions.append({"body": body, "options": options, "answer_letter": None, "answer_text": "", "explanation": ""})
            continue
        answer_lines = [am.group(1).strip()]
        i += 1
        while i < n and lines[i].strip() and not q_start.match(lines[i].strip()):
            nxt = lines[i].strip()
            options_here = opt_line.match(nxt)
            if options_here:
                break
            answer_lines.append(nxt)
            i += 1
        answer_raw = " ".join(a for a in answer_lines if a)

        letter = None
        answer_text = answer_raw
        opt_map = dict(options)
        lm = re.match(r"^([A-D])\.\s*(.*)$", answer_raw)
        if lm and lm.group(1) in opt_map:
            letter = lm.group(1)
            answer_text = opt_map[letter]
        elif len(answer_raw) == 1 and answer_raw.upper() in opt_map:
            letter = answer_raw.upper()
            answer_text = opt_map[letter]

        # anything after the answer, up to the next question number, is an
        # explanation if this source provides one (most don't)
        expl_lines = []
        while i < n and lines[i].strip() and not q_start.match(lines[i].strip()):
            expl_lines.append(lines[i].strip())
            i += 1
        explanation = " ".join(expl_lines)

        questions.append({
            "body": body,
            "options": options,
            "answer_letter": letter,
            "answer_text": answer_text,
            "explanation": explanation,
        })

    return questions


def dedupe_against_bank(questions: list[dict], bank_path: Path = Path("questions.json")) -> tuple[list[dict], list[dict]]:
    """Split questions into (unique, duplicate) against the current bank,
    using the same normalized-body-prefix key parse_security_bank.deduplicate
    uses, and also drops duplicates within the source itself."""
    existing = json.loads(bank_path.read_text(encoding="utf-8"))
    existing_keys = {normalize_text(q["bodyMarkdown"])[:80] for q in existing}

    unique: list[dict] = []
    dup: list[dict] = []
    seen_here: set[str] = set()
    for q in questions:
        key = normalize_text(q["body"])[:80]
        if key in existing_keys or key in seen_here:
            dup.append(q)
            continue
        seen_here.add(key)
        unique.append(q)
    return unique, dup


def render_clean_block(q: dict, num: int) -> str:
    lines = [f"### {num}. {q['body']}"]
    if q["options"]:
        for letter, text in q["options"]:
            lines.append(f"- {letter}. {text}")
        lines.append("")
    lines.append("<details>")
    lines.append("<summary>Reveal Answer</summary>")
    lines.append("")
    if q["answer_letter"]:
        lines.append(f"**Correct Answer:** **{q['answer_letter']}. {q['answer_text']}**")
    else:
        lines.append(f"**Correct Answer:** **{q['answer_text']}**")
    lines.append("")
    lines.append(f"*Intuition:* {q['explanation'] or NEEDS_EXPLANATION}")
    lines.append("</details>")
    lines.append("")
    lines.append("---")
    lines.append("")
    return "\n".join(lines)


def append_to_bank(questions: list[dict], target_path: Path, section_title: str) -> None:
    text = target_path.read_text(encoding="utf-8")
    nums = [int(m.group(1)) for m in re.finditer(r"^### (\d+)\.", text, re.MULTILINE)]
    start = max(nums) + 1 if nums else 1
    blocks = [f"## {section_title}", ""]
    for i, q in enumerate(questions):
        blocks.append(render_clean_block(q, start + i))
    new_text = text.rstrip("\n") + "\n\n---\n\n" + "\n".join(blocks)
    target_path.write_text(new_text, encoding="utf-8")


def apply_explanations(questions: list[dict], explanations_path: Path | None) -> int:
    if not explanations_path or not explanations_path.exists():
        return 0
    overrides = json.loads(explanations_path.read_text(encoding="utf-8"))
    filled = 0
    for q in questions:
        if q["explanation"]:
            continue
        key = normalize_text(q["body"])[:80]
        if key in overrides:
            q["explanation"] = overrides[key]
            filled += 1
    return filled


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--source", required=True, type=Path)
    parser.add_argument("--target", required=True, choices=["ia_bank", "quiz_bank"])
    parser.add_argument("--batch", required=True, help="Label used only in the printed report")
    parser.add_argument("--section", required=True, help="## heading for the appended block")
    parser.add_argument("--explanations-json", type=Path, default=None)
    parser.add_argument("--dry-run", action="store_true", help="Report only; do not write the target file")
    args = parser.parse_args()

    text = _read_source_text(args.source)
    parsed = extract_numbered_qa(text)
    print(f"Extracted {len(parsed)} questions from {args.source}")

    unanswered = [q for q in parsed if q["answer_letter"] is None and not q["answer_text"]]
    if unanswered:
        print(f"WARNING: {len(unanswered)} question(s) have no resolvable answer and will be dropped:", file=sys.stderr)
        for q in unanswered:
            print(f"  - {q['body'][:70]}", file=sys.stderr)
    answered = [q for q in parsed if q["answer_letter"] is not None or q["answer_text"]]

    unique, dup = dedupe_against_bank(answered)
    print(f"{len(unique)} unique, {len(dup)} duplicate of the existing bank or of each other")

    filled = apply_explanations(unique, args.explanations_json)
    if filled:
        print(f"Filled {filled} explanation(s) from {args.explanations_json}")

    missing = [q for q in unique if not q["explanation"]]
    if missing:
        print(f"\n{len(missing)} unique question(s) still need a real explanation before this is publish-ready:", file=sys.stderr)
        for q in missing:
            print(f"  - {q['body'][:90]}", file=sys.stderr)
        print(
            "\nWrite a {normalized-80-char-body-prefix: explanation} JSON file and re-run with "
            "--explanations-json, or edit the appended blocks directly afterward.",
            file=sys.stderr,
        )

    if args.dry_run:
        print("\n--dry-run: nothing written.")
        return

    target_file = {
        "ia_bank": Path("data_files/ia_bank/ia_clean.md"),
        "quiz_bank": Path("data_files/quiz_bank/quiz_clean.md"),
    }[args.target]
    append_to_bank(unique, target_file, args.section)
    print(f"\nAppended {len(unique)} questions to {target_file}")
    print("Next: npm run build:bank, then run the test suite.")


if __name__ == "__main__":
    main()
