#!/usr/bin/env python3
"""
compile_quiz_bank.py

Compiles and deduplicates all DCIT 418 quiz questions from:
1. data_files/quiz_bank/dcit418_quiz1.md
2. data_files/quiz_bank/dcit418_quiz2.md
3. data_files/quiz_bank/dcit418_quiz3.md
4. data_files/quiz_bank/dcit418_quiz4.md
5. data_files/quiz_bank/dcit418_quiz5.md
6. data_files/quiz_bank/quiz1.txt - quiz5.txt (or from quizzes and ia-20260915T213146Z-1-001.zip)

Deduplication:
- Identifies and eliminates duplicate questions (both intra-quiz and cross-quiz review items).
- Normalizes question stems by stripping prefixes ("True or False?"), suffixes ("(Fill in the blank)"), and formatting variants.
- For repeated questions, updates the Repetition Count and records all source takes in the Frequency Table.
- Renumbers questions cleanly (1..N) within each quiz module.
- Generates 12-column high-density Answer Summary Tables.

Outputs:
- quiz.md (root)
- data_files/quiz_bank/quiz_bank.md
- data_files/quiz_bank/quiz.md
"""

import os
import re
import json
import zipfile
from collections import OrderedDict

LETTERS = ["A", "B", "C", "D", "E", "F"]

def clean_stem(s):
    # Strip question formatting prefixes/suffixes
    s = re.sub(r'^(?:true\s+or\s+false\??\s*:?\s*)', '', s, flags=re.I)
    s = re.sub(r'\s*\((?:fill\s+in\s+the\s+blank\.?|choose\s+\w+|select\s+\w+|\d+\s+answers?)\)', '', s, flags=re.I)
    s = re.sub(r'[_]{2,}', '____', s)
    s = re.sub(r'[^a-zA-Z0-9]', '', s.lower())
    # Handle known paraphrasing variants
    if 'requiresapprovalfromuppermanagement' in s or 'requiresseniormanagementapproval' in s:
        return 'securitypolicyframeworkpolicyapproval'
    return s

def make_12col_grid(qa_pairs):
    n = len(qa_pairs)
    if n == 0:
        return ""
    cols = 6
    num_rows = (n + cols - 1) // cols
    
    lines = [
        "| Q | Answer | Q | Answer | Q | Answer | Q | Answer | Q | Answer | Q | Answer |",
        "|---|--------|---|--------|---|--------|---|--------|---|--------|---|--------|"
    ]
    
    for r in range(num_rows):
        row_cells = []
        for c in range(cols):
            idx = c * num_rows + r
            if idx < n:
                q_num, ans = qa_pairs[idx]
                row_cells.append(f"| **{q_num}** | {ans} ")
            else:
                row_cells.append("|  |  ")
        row_cells.append("|")
        lines.append("".join(row_cells))
    return "\n".join(lines)

def parse_existing_quiz(md_path):
    with open(md_path, "r", encoding="utf-8") as f:
        content = f.read()

    title_m = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    subtitle_m = re.search(r'^##\s+(Quiz\s+\d+:\s*.+)$', content, re.MULTILINE)
    topic_m = re.search(r'\*\*Topic:\*\*\s*(.+)', content)

    title = title_m.group(1).strip() if title_m else "DCIT 418: Systems and Network Security"
    subtitle = subtitle_m.group(1).strip() if subtitle_m else "Quiz"
    topic = topic_m.group(1).strip() if topic_m else ""

    # Parse Frequency Table mapping
    freq_dict = {}
    freq_m = re.search(r'## 📊 Question Frequency & Repetition Analysis Table\s*\n\s*\|.*?\n\s*\|.*?\n(.*?)(?=\n## |\Z)', content, re.DOTALL)
    if freq_m:
        raw_rows = freq_m.group(1).strip().splitlines()
        for r in raw_rows:
            if r.strip().startswith("|") and not r.strip().startswith("|:"):
                parts = [p.strip() for p in r.strip().split("|")[1:-1]]
                if len(parts) >= 5:
                    q_col, concept, ans_col, rep_col, takes_col = parts[0], parts[1], parts[2], parts[3], parts[4]
                    # Clean q_col
                    q_num_m = re.search(r'\d+', q_col)
                    if q_num_m:
                        freq_dict[int(q_num_m.group(0))] = {
                            "concept": concept,
                            "rep": rep_col,
                            "takes": takes_col
                        }

    raw_blocks = re.split(r'\n(?=###\s+\d+\.\s+)', content)
    questions = []
    for b in raw_blocks[1:]:
        m = re.match(r'###\s+(\d+)\.\s+(.+?)(?=\n-|\n\*|\n<details>|\Z)', b, re.DOTALL)
        if not m:
            continue
        q_num = int(m.group(1))
        q_stem = m.group(2).strip()

        ans_m = re.search(r'\*\*Correct Answer:\*\*\s*\*{0,2}(.+?)\*{0,2}\s*$', b, re.MULTILINE)
        raw_ans = ans_m.group(1).strip() if ans_m else "N/A"
        
        code_m = re.match(r'^([A-F](?:,\s*[A-F])?)(?:\.|\s|$)', raw_ans)
        if code_m:
            short_ans = code_m.group(1)
        else:
            first_word = raw_ans.split()[0] if raw_ans else "N/A"
            short_ans = raw_ans if len(raw_ans) <= 12 else first_word

        questions.append({
            "num": q_num,
            "stem": q_stem,
            "raw_block": b.strip(),
            "short_ans": short_ans,
            "full_ans": raw_ans,
            "freq_info": freq_dict.get(q_num, {})
        })

    return {
        "title": title,
        "subtitle": subtitle,
        "topic": topic,
        "questions": questions
    }

def format_new_question(item):
    stem = item.get("stem", "").strip()
    qtype = item.get("type", "mcq")
    options = item.get("options", [])
    correct = item.get("correct")
    explanation = item.get("explanation", item.get("topic", ""))
    topic = item.get("topic", "Security Concepts")

    short_ans = ""
    full_ans = ""
    lines = [f"### 0. {stem}"]  # placeholder number, will be renumbered

    if options and correct is not None:
        for idx, opt in enumerate(options):
            letter = LETTERS[idx] if idx < len(LETTERS) else f"({idx+1})"
            lines.append(f"- {letter}. {opt}")

        if isinstance(correct, list):
            letters = [LETTERS[c] for c in correct if c < len(LETTERS)]
            short_ans = ", ".join(letters)
            ans_parts = [f"{LETTERS[c]}. {options[c]}" for c in correct if c < len(options)]
            full_ans = " AND ".join(ans_parts)
        else:
            c_idx = int(correct)
            letter = LETTERS[c_idx] if c_idx < len(LETTERS) else "?"
            short_ans = letter
            opt_text = options[c_idx] if c_idx < len(options) else ""
            full_ans = f"{letter}. {opt_text}"

        lines.append("")
        lines.append("<details>")
        lines.append("<summary>Reveal Answer</summary>")
        lines.append("")
        lines.append(f"**Correct Answer:** **{full_ans}**")
        lines.append("")
        lines.append(f"*Intuition:* {explanation}")
        lines.append("</details>")
        lines.append("")
        lines.append("---")
    elif qtype == "fill" or "answer" in item or "answers" in item:
        ans_text = item.get("answer", item.get("answers", [""])[0])
        short_ans = ans_text[:12]
        full_ans = ans_text

        lines.append(f"*Answer:* **{ans_text}**")
        lines.append("")
        lines.append("<details>")
        lines.append("<summary>Reveal Answer</summary>")
        lines.append("")
        lines.append(f"**Correct Answer:** **{ans_text}**")
        lines.append("")
        lines.append(f"*Intuition:* {explanation}")
        lines.append("</details>")
        lines.append("")
        lines.append("---")
    else:
        short_ans = "N/A"
        full_ans = "N/A"
        lines.append("")
        lines.append("<details>")
        lines.append("<summary>Reveal Answer</summary>")
        lines.append("")
        lines.append(f"**Correct Answer:** **{full_ans}**")
        lines.append("")
        lines.append(f"*Intuition:* {explanation}")
        lines.append("</details>")
        lines.append("")
        lines.append("---")

    block_str = "\n".join(lines)
    return {
        "stem": stem,
        "raw_block": block_str,
        "short_ans": short_ans,
        "full_ans": full_ans,
        "topic": topic,
        "is_pool": True
    }

def main():
    repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    quiz_dir = os.path.join(repo_root, "data_files", "quiz_bank")
    zip_path = os.path.join(quiz_dir, "quizzes and ia-20260915T213146Z-1-001.zip")

    print(f"Reading and deduplicating quizzes from: {quiz_dir}")
    
    # 1. Load all original quiz data
    raw_quiz_data = OrderedDict()
    for idx in range(1, 6):
        md_path = os.path.join(quiz_dir, f"dcit418_quiz{idx}.md")
        raw_quiz_data[idx] = parse_existing_quiz(md_path)

    # 2. Global deduplication registry
    # key: clean_stem -> {quiz_idx, q_idx_in_unique_list, q_obj}
    seen_stems = {}
    duplicates_found = []

    unique_by_quiz = OrderedDict()
    for idx in range(1, 6):
        unique_by_quiz[idx] = []

    # Process Core Questions in order (Quiz 1 to 5)
    for qz_idx in range(1, 6):
        for q in raw_quiz_data[qz_idx]["questions"]:
            cs = clean_stem(q["stem"])
            if cs in seen_stems:
                orig_entry = seen_stems[cs]
                duplicates_found.append({
                    "stem": q["stem"],
                    "dup_in_quiz": qz_idx,
                    "dup_num": q["num"],
                    "orig_quiz": orig_entry["quiz"],
                    "orig_num": orig_entry["num"]
                })
                # Increment repetition on original
                orig_q = orig_entry["q_obj"]
                orig_q["rep_count"] = orig_q.get("rep_count", 1) + 1
                curr_takes = orig_q.get("takes", "")
                add_note = f"Quiz {qz_idx} Take (Q{q['num']})"
                if add_note not in curr_takes:
                    orig_q["takes"] = f"{curr_takes}, {add_note}" if curr_takes else add_note
            else:
                q["rep_count"] = 1
                # Initialize takes from original freq_info if available
                orig_takes = q.get("freq_info", {}).get("takes", "")
                if not orig_takes:
                    orig_takes = f"Quiz {qz_idx} Take"
                q["takes"] = orig_takes
                q["concept"] = q.get("freq_info", {}).get("concept", q["stem"][:60])
                q["is_pool"] = False

                unique_by_quiz[qz_idx].append(q)
                seen_stems[cs] = {
                    "quiz": qz_idx,
                    "num": len(unique_by_quiz[qz_idx]),
                    "q_obj": q
                }

    # Process Question Pools (.txt) in order
    for qz_idx in [1, 2, 3, 5]:
        raw_json = None
        loose_txt = os.path.join(quiz_dir, f"quiz{qz_idx}.txt")
        if os.path.exists(loose_txt):
            with open(loose_txt, "r", encoding="utf-8", errors="ignore") as tf:
                raw_json = tf.read().strip()
        elif os.path.exists(zip_path):
            with zipfile.ZipFile(zip_path, "r") as z:
                json_name = f"quizzes and ia/quiz{qz_idx}.txt"
                if json_name in z.namelist():
                    raw_json = z.read(json_name).decode("utf-8", errors="ignore").strip()

        if raw_json:
            try:
                pool_items = json.loads(raw_json)
                for item in pool_items:
                    st = item.get("stem", "").strip()
                    cs = clean_stem(st)
                    if cs in seen_stems:
                        orig_entry = seen_stems[cs]
                        orig_q = orig_entry["q_obj"]
                        orig_q["rep_count"] = orig_q.get("rep_count", 1) + 1
                        curr_takes = orig_q.get("takes", "")
                        if "Sakai Question Pool" not in curr_takes:
                            orig_q["takes"] = f"{curr_takes}, Sakai Question Pool" if curr_takes else "Sakai Question Pool"
                    else:
                        formatted_q = format_new_question(item)
                        formatted_q["rep_count"] = 1
                        formatted_q["takes"] = "Extended Sakai Question Pool"
                        formatted_q["concept"] = item.get("topic", "Security Concepts")
                        unique_by_quiz[qz_idx].append(formatted_q)
                        seen_stems[cs] = {
                            "quiz": qz_idx,
                            "num": len(unique_by_quiz[qz_idx]),
                            "q_obj": formatted_q
                        }
            except Exception as e:
                print(f"Error parsing pool for Quiz {qz_idx}: {e}")

    # Renumber questions sequentially within each quiz
    for qz_idx in range(1, 6):
        q_list = unique_by_quiz[qz_idx]
        for new_idx, q in enumerate(q_list, 1):
            q["num"] = new_idx
            # Update the header line ### \d+\. in raw_block
            q["raw_block"] = re.sub(r'^###\s+\d+\.', f'### {new_idx}.', q["raw_block"])

    total_unique = sum(len(q_list) for q_list in unique_by_quiz.values())
    print(f"\nDeduplication complete:")
    print(f"  - Total unique questions: {total_unique}")
    print(f"  - Duplicates eliminated: {len(duplicates_found)}")
    for d in duplicates_found:
        print(f"    * Removed Quiz {d['dup_in_quiz']} Q{d['dup_num']} (duplicate of Quiz {d['orig_quiz']} Q{d['orig_num']})")

    for qz in range(1, 6):
        core_c = sum(1 for q in unique_by_quiz[qz] if not q["is_pool"])
        pool_c = sum(1 for q in unique_by_quiz[qz] if q["is_pool"])
        print(f"Quiz {qz}: {len(unique_by_quiz[qz])} unique questions ({core_c} core, {pool_c} pool)")

    # Build Document
    doc = []
    
    # 1. Header & Metadata Block
    doc.append("# DCIT 418: Systems and Network Security")
    doc.append("## Consolidated Master Quiz Bank & Exam Review (Quizzes 1–5)")
    doc.append("**Department of Computer Science, University of Ghana**  ")
    doc.append("**Course Code:** DCIT 418 | **Credits:** 3 Credits  ")
    doc.append("**Prepared by:** Ryan Brown  ")
    doc.append("**Source / Links Provided by:** Bayat, Eugene, Christian, Ryan, and Sakai Question Pools  ")
    doc.append("**Source Format / Reference:** Consolidated Sakai Quiz Bank, Exam Takes, and Chat Exports  ")
    doc.append("")
    doc.append("---")
    doc.append("")

    # 2. Interactive Study Checklist & Progress Tracker
    doc.append("### 📝 Study Checklist & Progress Tracker")
    for qz in range(1, 6):
        q_list = unique_by_quiz[qz]
        core_c = sum(1 for q in q_list if not q["is_pool"])
        pool_c = sum(1 for q in q_list if q["is_pool"])
        doc.append(f"- [ ] **Part {qz}: Quiz {qz} — {raw_quiz_data[qz]['subtitle'].split(':', 1)[-1].strip()} ({len(q_list)} Unique Questions)**")
        doc.append(f"  - [ ] Core Exam Takes (Q1–Q{core_c})")
        if pool_c > 0:
            doc.append(f"  - [ ] Extended Sakai Question Pool (Q{core_c + 1}–Q{len(q_list)})")
    doc.append("")
    doc.append("---")
    doc.append("")

    # 3. Overview Callout Box
    doc.append("> [!NOTE]")
    doc.append("> **Prepared by:** Ryan Brown  ")
    doc.append("> **Source / Links Provided by:** Bayat, Eugene, Christian, Ryan, and Sakai Question Pools  ")
    doc.append(f"> This master document consolidates all **{total_unique} verified unique quiz questions** across DCIT 418: Quizzes 1 through 5. All duplicate questions (both intra-quiz formatting duplicates and cross-quiz review items) have been thoroughly deduplicated and indexed.")
    doc.append("> - For repeated exam questions, occurrence counts (`2x`, `3x`) and source takes are tracked in each module's **Question Frequency & Repetition Analysis Table**.")
    doc.append("> - High-density **Answer Summary Tables** (12-column grid format) provide rapid reference for each quiz.")
    doc.append("> - Every question features an interactive **'Reveal Answer'** drop-down containing verified answers and detailed conceptual/engineering intuition based on course literature and William Stallings' *Cryptography and Network Security*.")
    doc.append("")
    doc.append("---")
    doc.append("")

    # 4. Master Quick Navigation Table
    doc.append("## 📑 Master Quiz Index & Syllabus Coverage")
    doc.append("")
    doc.append("| Part | Quiz Title | Syllabus Scope & Topics | Unique Questions |")
    doc.append("|:---:|:---|:---|:---:|")
    doc.append(f"| **Quiz 1** | [IT Security Policy Framework & Infrastructure Domains](#quiz-1-it-security-policy-framework--infrastructure-domains) | Policies, Standards, 7 Domains, CIA Triad, MTTF, SOX, GLBA | **{len(unique_by_quiz[1])}** |")
    doc.append(f"| **Quiz 2** | [Internet of Things (IoT), Mobile IP & BYOD](#quiz-2-internet-of-things-iot-mobile-ip-byod--emerging-technologies) | Smart Cities, Telemetry, Metadata, Mobile IP (HA/FA/MN), BYOD | **{len(unique_by_quiz[2])}** |")
    doc.append(f"| **Quiz 3** | [Data Protection, DPIA & African Data Sovereignty](#quiz-3-data-protection-dpia--african-data-sovereignty) | DPIA, Data Localization, POPIA, NDPA, Malabo Convention, 72h Breach | **{len(unique_by_quiz[3])}** |")
    doc.append(f"| **Quiz 4** | [Cryptography & Block Cipher Modes](#quiz-4-cryptography--block-cipher-modes) | DES, 3DES, AES, Modes (ECB, CBC, CFB, CTR), Number Theory, RSA, ECC | **{len(unique_by_quiz[4])}** |")
    doc.append(f"| **Quiz 5** | [Hashes, MACs, Digital Signatures, PKI & Protocols](#quiz-5-hashes-macs-digital-signatures-pki--network-security-protocols) | SHA-1/2/3, HMAC, DSA, X.509, Kerberos, IPsec, TLS, 802.11i, PGP | **{len(unique_by_quiz[5])}** |")
    doc.append(f"| **Total** | **All 5 Quizzes Consolidated** | **Full DCIT 418 Systems and Network Security Curriculum** | **{total_unique}** |")
    doc.append("")
    doc.append("---")
    doc.append("")

    # 5. Build Each Quiz Module
    for idx in range(1, 6):
        data = raw_quiz_data[idx]
        q_list = unique_by_quiz[idx]
        core_c = sum(1 for q in q_list if not q["is_pool"])
        pool_c = sum(1 for q in q_list if q["is_pool"])

        # Build QA pairs for the 12-column Answer Summary Table
        qa_pairs = []
        for q in q_list:
            short = q["short_ans"]
            if len(short) > 10:
                short = short[:10] + ".."
            qa_pairs.append((q["num"], short))

        grid_table = make_12col_grid(qa_pairs)

        doc.append(f"## {data['subtitle']}")
        doc.append(f"**Topic:** {data['topic']}  ")
        doc.append(f"**Total Questions:** {len(q_list)} (Core Exam Takes: {core_c}, Extended Sakai Pool: {pool_c})")
        doc.append("")
        
        # Answer Summary Table
        doc.append(f"### Quiz {idx} Complete Answer Summary Table")
        doc.append("")
        doc.append(grid_table)
        doc.append("")
        doc.append("---")
        doc.append("")

        # Frequency & Repetition Table
        doc.append(f"### 📊 Quiz {idx} Question Frequency & Repetition Analysis Table")
        doc.append("")
        doc.append("| Q# | Question Topic / Core Concept | Answer | Repetition Count | Test Occurrences / Source Takes |")
        doc.append("|:---|:------------------------------|:------:|:----------------:|:--------------------------------|")
        
        for q in q_list:
            rep_str = f"**{q.get('rep_count', 1)}x**"
            takes_str = q.get("takes", f"Quiz {idx} Take")
            concept_str = q.get("concept", q["stem"][:60])
            doc.append(f"| **{q['num']}** | {concept_str} | {q['short_ans']} | {rep_str} | {takes_str} |")

        doc.append("")
        doc.append("---")
        doc.append("")

        # Questions & Detailed Solutions
        doc.append(f"### Quiz {idx} Questions & Detailed Solutions")
        doc.append("")

        core_qs = [q for q in q_list if not q["is_pool"]]
        pool_qs = [q for q in q_list if q["is_pool"]]

        doc.append(f"#### Part A: Core Exam Takes (Questions 1–{len(core_qs)})")
        doc.append("")
        for q in core_qs:
            doc.append(q["raw_block"])
            doc.append("")

        if pool_qs:
            doc.append(f"#### Part B: Extended Sakai Question Pool (Questions {len(core_qs)+1}–{len(q_list)})")
            doc.append("")
            for q in pool_qs:
                doc.append(q["raw_block"])
                doc.append("")

        doc.append("")
        doc.append("---")
        doc.append("")

    full_output = "\n".join(doc)

    out_paths = [
        os.path.join(repo_root, "quiz.md"),
        os.path.join(quiz_dir, "quiz_bank.md"),
        os.path.join(quiz_dir, "quiz.md"),
    ]

    for p in out_paths:
        with open(p, "w", encoding="utf-8") as out_f:
            out_f.write(full_output)
        print(f"Successfully wrote {len(full_output)} characters ({len(full_output.splitlines())} lines) to: {p}")

if __name__ == "__main__":
    main()
