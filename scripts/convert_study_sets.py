#!/usr/bin/env python3
"""
Convert DCIT418 Study Sets (SET4 MCQ Drill, SET5 Fill-ins) to parser format.

Reads:
  - data_files/study_sets/SET4_MCQ_Drill_QUESTIONS.md
  - data_files/study_sets/SET4_MCQ_Drill_ANSWER_KEY.md
  - data_files/study_sets/SET5_FillIns_QUESTIONS.md
  - data_files/study_sets/SET5_FillIns_ANSWER_KEY.md

Outputs:
  - data_files/study_sets/SET4_clean.md (parser format)
  - data_files/study_sets/SET5_clean.md (parser format)

These clean files are then ingested by parse_security_bank.py.
"""
import re
from pathlib import Path
from typing import Optional


def extract_set4_answers() -> dict:
    """Parse SET4 answer key table into {q_num: (answer_letter, note)}."""
    answers_file = Path("data_files/study_sets/SET4_MCQ_Drill_ANSWER_KEY.md")
    text = answers_file.read_text(encoding="utf-8")
    
    answers = {}
    # Parse markdown table rows: "| 1 | c | Note text |"
    pattern = r"\|\s*(\d+)\s*\|\s*([a-e])\s*\|\s*(.*?)\s*\|"
    for match in re.finditer(pattern, text):
        q_num = int(match.group(1))
        ans_letter = match.group(2).upper()
        note = match.group(3).strip()
        answers[q_num] = (ans_letter, note)
    
    return answers


def extract_set5_answers() -> dict:
    """Parse SET5 answer key into {q_num: answer_text}."""
    answers_file = Path("data_files/study_sets/SET5_FillIns_ANSWER_KEY.md")
    text = answers_file.read_text(encoding="utf-8")
    
    answers = {}
    # Look for patterns like "1. Confidentiality; Integrity; Availability"
    # These appear after chapter headings
    lines = text.split("\n")
    for line in lines:
        # Match "1. " at line start (after stripping leading #'s and newlines)
        m = re.match(r"^(\d+)\.\s+(.+)$", line.strip())
        if m:
            q_num = int(m.group(1))
            answer_text = m.group(2).strip()
            answers[q_num] = answer_text
    
    return answers


def parse_set4_questions() -> dict:
    """Parse SET4 questions into {q_num: (heading, options)}."""
    questions_file = Path("data_files/study_sets/SET4_MCQ_Drill_QUESTIONS.md")
    text = questions_file.read_text(encoding="utf-8")
    
    questions = {}
    # Match "**1.** Heading text" followed by options
    q_pattern = r"^\*\*(\d+)\.\*\*\s+(.+?)$"
    option_pattern = r"^-\s+\*\*([A-E])\.\*\*\s+(.+?)$"
    
    lines = text.split("\n")
    current_q = None
    current_heading = None
    current_options = []
    
    for line in lines:
        # Try to match a question heading
        q_match = re.match(q_pattern, line)
        if q_match:
            # Save previous question if any
            if current_q is not None:
                questions[current_q] = (current_heading, current_options)
            
            current_q = int(q_match.group(1))
            current_heading = q_match.group(2).strip()
            current_options = []
            continue
        
        # Try to match an option
        opt_match = re.match(option_pattern, line)
        if opt_match and current_q is not None:
            letter = opt_match.group(1)
            text_opt = opt_match.group(2).strip()
            current_options.append((letter, text_opt))
    
    # Don't forget last question
    if current_q is not None:
        questions[current_q] = (current_heading, current_options)
    
    return questions


def parse_set5_questions() -> dict:
    """Parse SET5 fill-in questions into {q_num: heading}."""
    questions_file = Path("data_files/study_sets/SET5_FillIns_QUESTIONS.md")
    text = questions_file.read_text(encoding="utf-8")
    
    questions = {}
    # Match "1. The three components of..."
    pattern = r"^(\d+)\.\s+(.+?)$"
    
    for line in text.split("\n"):
        m = re.match(pattern, line.strip())
        if m:
            q_num = int(m.group(1))
            heading = m.group(2).strip()
            questions[q_num] = heading
    
    return questions


def generate_set4_clean(questions: dict, answers: dict) -> str:
    """Generate parser-format markdown for SET4."""
    output = []
    output.append("# DCIT418 — SET 4: MCQ Drill (Parser Format)")
    output.append("")
    output.append("100 questions from the SET4 MCQ practice examination, formatted for parse_security_bank.py.")
    output.append("")
    
    for q_num in sorted(questions.keys()):
        heading, options = questions[q_num]
        ans_letter, note = answers.get(q_num, ("?", ""))
        
        # Convert answer letter to index (A=0, B=1, etc.)
        correct_index = ord(ans_letter) - ord("A") if ans_letter != "?" else 0
        
        output.append(f"### {q_num}. {heading}")
        output.append("")
        
        for letter, opt_text in options:
            output.append(f"- {letter}. {opt_text}")
        output.append("")
        
        output.append(f"**Correct Answer:** **{ans_letter}. {options[correct_index][1] if correct_index < len(options) else ''}**")
        output.append("")
        
        if note:
            output.append(f"**Reason:** {note}")
        else:
            output.append("**Reason:** (See answer key for context.)")
        output.append("")
        output.append("---")
        output.append("")
    
    return "\n".join(output)


def generate_set5_clean(questions: dict, answers: dict) -> str:
    """Generate parser-format markdown for SET5."""
    output = []
    output.append("# DCIT418 — SET 5: Fill-in-the-Blanks (Parser Format)")
    output.append("")
    output.append("100 fill-in questions from SET5, formatted for parse_security_bank.py.")
    output.append("")
    
    for q_num in sorted(questions.keys()):
        heading = questions[q_num]
        answer_text = answers.get(q_num, "(See answer key)")
        
        output.append(f"### {q_num}. {heading}")
        output.append("")
        output.append(f"**Correct Answer:** **{answer_text}**")
        output.append("")
        output.append("**Reason:** Fill-in precision is critical on Sakai exams.")
        output.append("")
        output.append("---")
        output.append("")
    
    return "\n".join(output)


if __name__ == "__main__":
    print("Converting SET4 MCQ Drill...")
    set4_q = parse_set4_questions()
    set4_ans = extract_set4_answers()
    set4_clean_content = generate_set4_clean(set4_q, set4_ans)
    
    set4_clean_path = Path("data_files/study_sets/SET4_clean.md")
    set4_clean_path.write_text(set4_clean_content, encoding="utf-8")
    print(f"✓ Wrote {len(set4_q)} SET4 questions to {set4_clean_path}")
    
    print("Converting SET5 Fill-ins...")
    set5_q = parse_set5_questions()
    set5_ans = extract_set5_answers()
    set5_clean_content = generate_set5_clean(set5_q, set5_ans)
    
    set5_clean_path = Path("data_files/study_sets/SET5_clean.md")
    set5_clean_path.write_text(set5_clean_content, encoding="utf-8")
    print(f"✓ Wrote {len(set5_q)} SET5 questions to {set5_clean_path}")
    
    print(f"\nTotal new questions: {len(set4_q) + len(set5_q)}")
    print("Next: Update parse_security_bank.py to ingest SET4_clean.md and SET5_clean.md")
