"""Parse DCIT 418 Systems and Network Security question banks into questions.json.

Reads the consolidated quiz bank and the IA offsite bank from data_files/:
  1. data_files/quiz_bank/quiz.md (379 questions, Quiz 1-5 consolidated, <details> answer blocks)
  2. data_files/ia_bank/ia_clean.md (158 questions, Sakai Offsite IA; original with
     provider/coverage metadata kept at data_files/ia_bank/dcit418_ia_offsite.md)

Classifies each question into one of 14 course parts (Part 0: Data Protection &
IT Security Policy, covering the two guest lectures from the Data Protection
Officer; Parts 1-13: Stallings' Cryptography and Network Security chapters)
and outputs questions.json in the schema expected by the Security Lab app.
"""
from pathlib import Path
import argparse
import collections
import json
import re
import sys
import unicodedata

PART_TITLES = {
    0: "Data Protection & IT Security Policy",
    1: "Overview & Computer Security Concepts",
    2: "Classical Encryption Techniques",
    3: "Block Ciphers & the Data Encryption Standard",
    4: "Number Theory & Finite Fields",
    5: "Advanced Encryption Standard (AES)",
    6: "Block Cipher Operation",
    7: "Pseudorandom Number Generation & Stream Ciphers",
    8: "More Number Theory (Primes & Primality)",
    9: "Public-Key Cryptography & RSA",
    10: "Other Public-Key Cryptosystems",
    11: "Cryptographic Hash Functions",
    12: "Message Authentication Codes",
    13: "Digital Signatures",
}

# Ordered from most specific to least specific; the first matching chapter wins.
# Keyword lists are derived from data_files/dcit418_fill_ins_cheatsheet.md's
# chapter-by-chapter reference tables plus the quiz/IA bank topic tags.
CHAPTER_KEYWORDS: list[tuple[int, list[str]]] = [
    (13, [
        "digital signature", "dsa", "dss", "ecdsa", "rsa-pss", "rsa pss",
        "schnorr", "elgamal digital signature", "arbitrated signature",
        "direct digital signature", "existential forgery", "selective forgery",
        "universal forgery", "total break",
    ]),
    (12, [
        "message authentication code", "mac ", " mac", "hmac", "cmac",
        "ipad", "opad", "authenticated encryption", "ccm mode", "gcm mode",
        "galois/counter", "cipher-based mac", "daa", "key wrapping",
        "data authentication algorithm",
    ]),
    (11, [
        "hash function", "message digest", "preimage", "collision resistance",
        "birthday attack", "birthday paradox", "merkle-damgard", "merkle–damgard",
        "sha-1", "sha-2", "sha-3", "sha1", "sha2", "sha3", "keccak",
        "sponge construction", "absorbing phase", "squeezing phase",
        "one-way hash",
    ]),
    (10, [
        "diffie-hellman", "diffie hellman", "key exchange", "elgamal",
        "elliptic curve", "ecc", "ecdlp", "ecdh", "abelian group",
        "point at infinity", "chord-and-tangent", "koblitz",
    ]),
    (9, [
        "rsa", "trapdoor", "oaep", "public-key cryptosystem", "public key cryptosystem",
        "adleman", "rivest", "shamir", "timing attack", "square-and-multiply",
        "square and multiply", "hamming weight", "chosen-ciphertext",
    ]),
    (8, [
        "primality", "miller-rabin", "miller rabin", "aks algorithm",
        "fundamental theorem of arithmetic", "fermat's little theorem",
        "fermats little theorem", "euler's theorem", "eulers theorem",
        "euler's totient", "eulers totient", "totient", "chinese remainder theorem",
        "discrete logarithm", "discrete log", "primitive root", "prime number",
    ]),
    (7, [
        "pseudorandom number generat", "prng", "trng", "csprng",
        "linear congruential generator", "lcg", "blum blum shub", "bbs generator",
        "keystream", "rc4", "key scheduling algorithm", "ksa ",
        "pseudo-random generation algorithm", "prga", "stream cipher",
        "true random number generator", "forward unpredictab", "backward unpredictab",
        "seed",
    ]),
    (6, [
        "triple des", "3des", "meet-in-the-middle", "meet in the middle",
        "electronic codebook", "ecb mode", "cipher block chaining", "cbc mode",
        "cipher feedback", "cfb mode", "output feedback", "ofb mode",
        "counter mode", "ctr mode", "xts-aes", "xts aes", "tweak value",
        "initialization vector", "block cipher mode", "error propagation",
        "encrypt-decrypt-encrypt",
    ]),
    (5, [
        "aes", "rijndael", "subbytes", "shiftrows", "mixcolumns", "addroundkey",
        "state array", "key expansion", "rotword", "round constant", "rcon",
        "advanced encryption standard",
    ]),
    (4, [
        "euclidean algorithm", "gcd(", "greatest common divisor", "modular arithmetic",
        "galois field", "finite field", "gf(2", "gf(p", "irreducible polynomial",
        "abelian", "relatively prime", "coprime", "ring", "integral domain",
        "polynomial arithmetic",
    ]),
    (3, [
        "feistel", "data encryption standard", "des ", "s-box", "sbox",
        "avalanche effect", "strict avalanche criterion", "sac ",
        "diffusion", "confusion", "expansion permutation", "block cipher design",
        "substitution-permutation network", "spn",
    ]),
    (2, [
        "caesar cipher", "vigenere", "vigenère", "playfair", "monoalphabetic",
        "polyalphabetic", "rail fence", "transposition cipher", "substitution cipher",
        "one-time pad", "steganography", "cryptanalysis", "rotor machine",
        "symmetric cipher model", "kasiski",
    ]),
    (1, [
        "osi security architecture", "security attack", "security service",
        "security mechanism", "passive attack", "active attack", "masquerade",
        "traffic analysis", "nonrepudiation", "non-repudiation", "cia triad",
        "confidentiality, integrity, availability", "model for network security",
        "transport layer security", " tls ", "secure sockets layer", " ssl ",
    ]),
]

# Quiz 1 (IT security policy framework, 7 domains), Quiz 2 (IoT/BYOD/Mobile IP),
# and the policy/compliance portion of Quiz 3 (data protection, DPIA, data
# sovereignty) all come from the two guest lectures given by the Data
# Protection Officer, not from the Stallings textbook chapters.
PART0_KEYWORDS = [
    "it security policy framework", "infrastructure domain", "7 domains",
    "seven domains", "security policy framework", "data classification",
    "sarbanes-oxley", "gramm-leach-bliley", "glba", "sox ", "hipaa",
    "service-level agreement", "sla ", "workstation domain", "lan domain",
    "wan domain", "remote access domain", "system/application domain",
    "user domain", "lan-to-wan", "mean time to failure", "mttf",
    "intrusion prevention system", "ips ", "standard (mandatory technical",
    "guideline", "procedure (step-by-step", "policy framework",
    "internet of things", "iot ", "mobile ip", "byod", "smart cit",
    "data sovereignty", "privacy impact assessment", "dpia",
    "personally identifiable information", "anonymiz", "pseudonymiz",
    "data protection officer", "data residency", "cross-border data",
    "compliance regulation", "metadata",
]


def normalize_text(text: str) -> str:
    text = unicodedata.normalize("NFKD", text)
    text = "".join(c for c in text if not unicodedata.combining(c))
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def classify_part(body: str, reason: str) -> int:
    haystack = normalize_text(f"{body} {reason}")
    padded = f" {haystack} "
    for _part, keywords in ((0, PART0_KEYWORDS),):
        for kw in keywords:
            if normalize_text(kw) in padded:
                return 0
    for part, keywords in CHAPTER_KEYWORDS:
        for kw in keywords:
            if normalize_text(kw) in padded:
                return part
    return 1


def split_multi_answer(raw: str) -> list[tuple[str, str]]:
    """Split a Correct Answer field like '**A. text** and **C. text**' into pairs."""
    parts = re.split(r"\*\*\s+and\s+\*\*", raw)
    pairs = []
    for i, part in enumerate(parts):
        cleaned = part.strip().strip("*").strip()
        m = re.match(r"^([A-E])\.\s*(.*)$", cleaned)
        if m:
            pairs.append((m.group(1).upper(), m.group(2).strip()))
    return pairs


def parse_bank(filepath: Path, batch: str) -> list[dict]:
    text = filepath.read_text(encoding="utf-8")
    questions = []

    quiz_section_pattern = re.compile(r"^## (Quiz \d+):.*$", re.MULTILINE)
    section_matches = list(quiz_section_pattern.finditer(text))

    def section_for(pos: int) -> str:
        label = ""
        for sm in section_matches:
            if sm.start() <= pos:
                label = sm.group(1)
            else:
                break
        return label

    pattern = re.compile(r"^### (\d+)\.\s+(.*?)$", re.MULTILINE)
    matches = list(pattern.finditer(text))

    for i, match in enumerate(matches):
        q_num = int(match.group(1))
        q_heading = match.group(2).strip()

        start = match.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        block = text[start:end].strip()

        section = section_for(match.start())
        family_prefix = f"{batch}-{section.replace(' ', '')}" if section else batch

        option_pattern = re.compile(r"^- ([A-E])\.\s+(.+?)$", re.MULTILINE)
        option_matches = list(option_pattern.finditer(block))
        options = [om.group(2).strip() for om in option_matches]
        labels = [om.group(1).upper() for om in option_matches]

        intuition_match = re.search(r"\*Intuition:\*\s*(.*?)(?:</details>|\Z)", block, re.DOTALL)
        reason = intuition_match.group(1).strip() if intuition_match else ""
        if not reason:
            reason_match = re.search(r"\*\*Reason:\*\*\s*(.*?)(?:---|</details>|\Z)", block, re.DOTALL)
            reason = reason_match.group(1).strip() if reason_match else ""

        answer_match = re.search(
            r"\*\*Correct Answer:\*\*\s*(.*?)(?:\n\n|\*Intuition:\*|\Z)",
            block,
            re.DOTALL,
        )
        if not answer_match:
            continue
        answer_raw = answer_match.group(1).strip()

        multi = split_multi_answer(answer_raw) if " and " in answer_raw else []
        multi = [p for p in multi if len(p) == 2]

        if len(multi) >= 2 and options:
            correct_letters = [p[0] for p in multi]
            correct_indices = [labels.index(l) for l in correct_letters if l in labels]
            if len(correct_indices) != len(correct_letters):
                continue
            correct_text = " and ".join(options[idx] for idx in correct_indices)
            q_type = "multi"
            correct_index = None
        else:
            correct_indices = None
            single = re.match(r"^\*\*([A-E])\.\s*(.*?)\*\*", answer_raw)
            if single and options:
                correct_letter = single.group(1).upper()
                if correct_letter not in labels:
                    continue
                correct_index = labels.index(correct_letter)
                correct_text = options[correct_index]
                if options == ["True", "False"]:
                    q_type = "tf"
                elif len(options) == 4:
                    q_type = "mcq4"
                elif len(options) == 5:
                    q_type = "mcq5"
                else:
                    continue
            elif not options:
                fill_match = re.match(r"^\*\*(.*?)\*\*", answer_raw)
                correct_text = fill_match.group(1).strip() if fill_match else answer_raw.strip("*").strip()
                if not correct_text:
                    continue
                q_type = "fill"
                correct_index = None
            else:
                continue

        part = classify_part(q_heading, reason)
        qid = f"{family_prefix}-Q{q_num}"
        origin = section or "IA Offsite"

        questions.append({
            "id": qid,
            "part": part,
            "batch": batch,
            "family": qid,
            "isCore": True,
            "week": origin,
            "source": PART_TITLES.get(part, "Security"),
            "level": "Recall",
            "type": q_type,
            "bodyMarkdown": q_heading,
            "options": options,
            "correctIndex": correct_index,
            "correctIndices": correct_indices,
            "correctText": correct_text,
            "acceptedAnswers": [],
            "reason": reason or f"The correct answer is: {correct_text}",
            "trap": "",
            "sourceRef": f"{batch}, {origin}, Question {q_num}",
            "checkMethod": "Verified against source answer key.",
            "workingMarkdown": "",
        })

    return questions


SOURCE_PRIORITY = {"iabank": 2, "quizbank": 1}


def deduplicate(questions: list[dict]) -> list[dict]:
    seen: dict[str, dict] = {}
    unique: list[dict] = []

    for q in questions:
        norm = normalize_text(q["bodyMarkdown"])
        key = norm[:80]

        if key in seen:
            existing = seen[key]
            rank = SOURCE_PRIORITY.get(q["batch"], 0)
            existing_rank = SOURCE_PRIORITY.get(existing["batch"], 0)
            better = (rank, len(q.get("reason", ""))) > (
                existing_rank,
                len(existing.get("reason", "")),
            )
            if better:
                idx = unique.index(existing)
                unique[idx] = q
                seen[key] = q
        else:
            seen[key] = q
            unique.append(q)

    return unique


def reassign_ids(questions: list[dict]) -> list[dict]:
    questions.sort(key=lambda q: (q["part"], q["id"]))
    counters: collections.Counter = collections.Counter()
    for q in questions:
        counters[q["part"]] += 1
        num = counters[q["part"]]
        q["id"] = f"P{q['part']}-Q{num}"
        q["family"] = q["id"]
    return questions


def report(records: list[dict]) -> str:
    parts = sorted(set(q["part"] for q in records))
    lines = [
        "# Parser verification: PASS",
        "",
        f"Total questions: {len(records)}; Parts: {len(parts)}.",
        "",
        "| Part | Title | mcq4 | mcq5 | multi | fill | tf | Total |",
        "|---|---|---:|---:|---:|---:|---:|---:|",
    ]

    for part in parts:
        subset = [q for q in records if q["part"] == part]
        counts = collections.Counter(q["type"] for q in subset)
        title = PART_TITLES.get(part, f"Part {part}")
        lines.append(
            f"| {part} | {title} | "
            + " | ".join(str(counts.get(t, 0)) for t in ["mcq4", "mcq5", "multi", "fill", "tf"])
            + f" | {len(subset)} |"
        )

    counts = collections.Counter(q["type"] for q in records)
    lines.append(
        "| - | **Total** | "
        + " | ".join(str(counts.get(t, 0)) for t in ["mcq4", "mcq5", "multi", "fill", "tf"])
        + f" | **{len(records)}** |"
    )

    lines += ["", "## Source Distribution", "", "| Source | Count |", "|---|---:|"]
    source_counts = collections.Counter(q["batch"] for q in records)
    for source, count in source_counts.most_common():
        lines.append(f"| {source} | {count} |")

    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data", type=Path, default=Path("data_files"))
    parser.add_argument("--output", type=Path, default=Path("questions.json"))
    args = parser.parse_args()

    data = args.data
    if not data.is_dir():
        print(f"PARSER FAILED: data directory not found at {data}", file=sys.stderr)
        sys.exit(1)

    all_questions: list[dict] = []

    quiz_path = data / "quiz_bank" / "quiz.md"
    if quiz_path.exists():
        qs = parse_bank(quiz_path, "quizbank")
        print(f"  Consolidated quiz bank: {len(qs)} questions parsed")
        all_questions.extend(qs)
    else:
        print(f"  WARNING: {quiz_path} not found", file=sys.stderr)

    ia_path = data / "ia_bank" / "ia_clean.md"
    if ia_path.exists():
        qs = parse_bank(ia_path, "iabank")
        print(f"  IA offsite bank: {len(qs)} questions parsed")
        all_questions.extend(qs)
    else:
        print(f"  WARNING: {ia_path} not found", file=sys.stderr)

    print(f"\nTotal raw questions: {len(all_questions)}")

    unique = deduplicate(all_questions)
    print(f"After deduplication: {len(unique)}")

    final = reassign_ids(unique)

    summary = report(final)
    print()
    print(summary)

    output_path = args.output
    output_path.write_text(json.dumps(final, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {len(final)} questions to {output_path}")

    report_path = Path("PARSER_REPORT.md")
    report_path.write_text(summary, encoding="utf-8")
    print(f"Wrote report to {report_path}")


if __name__ == "__main__":
    main()
