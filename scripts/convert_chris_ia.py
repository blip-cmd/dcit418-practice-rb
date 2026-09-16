#!/usr/bin/env python3
"""
Parse and convert Chris's 100-question IA exam review to parser format.

Reads:
  - data_files/received qus/Chris/IA.md (100 well-formatted Q&A with explanations)

Outputs:
  - data_files/ia_bank/chris_clean.md (parser format)
  - Provides structure for merging into ia_offsite.md

The questions are already well-organized MCQ + fill-in format with detailed explanations.
This script converts them to parser-compatible markdown.
"""
import re
from pathlib import Path


def parse_chris_ia() -> list[dict]:
    """Parse Chris's IA.md into structured questions."""
    ia_path = Path("data_files/received qus/Chris/IA.md")
    text = ia_path.read_text(encoding="utf-8")
    
    questions = []
    current_q = None
    current_heading = None
    current_options = []
    current_answer = None
    current_explanation = None
    in_options = False
    
    lines = text.split("\n")
    i = 0
    
    while i < len(lines):
        line = lines[i].strip()
        
        # Match question heading: "1. Some text" or "53. Some text" etc
        q_match = re.match(r"^(\d+)\.\s+(.+)$", line)
        if q_match and not line.startswith("Correct Answer"):
            # Save previous question if any
            if current_q is not None:
                questions.append({
                    "num": current_q,
                    "heading": current_heading,
                    "options": current_options,
                    "answer": current_answer,
                    "explanation": current_explanation,
                })
            
            current_q = int(q_match.group(1))
            current_heading = q_match.group(2).strip()
            current_options = []
            current_answer = None
            current_explanation = None
            in_options = False
            i += 1
            continue
        
        # Match options: "A. text", "B. text", etc.
        opt_match = re.match(r"^([A-E])\.\s+(.+)$", line)
        if opt_match and current_q is not None:
            current_options.append((opt_match.group(1), opt_match.group(2)))
            in_options = True
            i += 1
            continue
        
        # Match "Correct Answer: ..." or "Correct Answer:** C. text **"
        ans_match = re.match(r"^Correct Answer:\s*(.+)$", line)
        if ans_match and current_q is not None:
            current_answer = ans_match.group(1).strip()
            in_options = False
            i += 1
            continue
        
        # Match "Explanation: ..." 
        exp_match = re.match(r"^Explanation:\s*(.+)$", line)
        if exp_match and current_q is not None:
            # Collect multi-line explanation
            explanation_lines = [exp_match.group(1)]
            i += 1
            while i < len(lines):
                next_line = lines[i].strip()
                # Stop if we hit bullet points, "Page X", question number, or "Correct Answer"
                if (next_line.startswith("•") or 
                    next_line.startswith("Page ") or 
                    re.match(r"^\d+\.", next_line) or
                    next_line.startswith("Correct Answer")):
                    break
                if next_line:
                    explanation_lines.append(next_line)
                i += 1
            current_explanation = " ".join(explanation_lines)
            continue
        
        i += 1
    
    # Don't forget last question
    if current_q is not None:
        questions.append({
            "num": current_q,
            "heading": current_heading,
            "options": current_options,
            "answer": current_answer,
            "explanation": current_explanation,
        })
    
    return questions


def generate_chris_clean(questions: list[dict]) -> str:
    """Generate parser-format markdown for Chris's IA questions."""
    output = []
    output.append("# DCIT418: Christian's Exam Review (Parser Format)")
    output.append("")
    output.append("100 high-quality exam review questions from Christian's comprehensive study bank,")
    output.append("formatted for parse_security_bank.py. These questions emphasize synthesis and reasoning.")
    output.append("")
    
    for q in questions:
        q_num = q["num"]
        heading = q["heading"]
        options = q["options"]
        answer_raw = q["answer"]
        explanation = q["explanation"]
        
        output.append(f"### {q_num}. {heading}")
        output.append("")
        
        # Add options if MCQ
        if options:
            for letter, opt_text in options:
                output.append(f"- {letter}. {opt_text}")
            output.append("")
        
        # Parse answer
        if answer_raw:
            # Handle "C. text" format
            ans_mcq_match = re.match(r"^\*\*([A-E])\.\s*(.+?)\*\*$", answer_raw)
            if ans_mcq_match:
                ans_letter = ans_mcq_match.group(1)
                ans_text = ans_mcq_match.group(2).strip()
                output.append(f"**Correct Answer:** **{ans_letter}. {ans_text}**")
            else:
                # Handle fill-in format
                ans_clean = answer_raw.strip("*").strip()
                output.append(f"**Correct Answer:** **{ans_clean}**")
            
            output.append("")
        
        if explanation:
            output.append(f"**Intuition:** {explanation}")
        else:
            output.append("**Intuition:** See answer key for detailed reasoning.")
        
        output.append("")
        output.append("---")
        output.append("")
    
    return "\n".join(output)


if __name__ == "__main__":
    print("Parsing Chris's Exam Review (100 questions)...")
    questions = parse_chris_ia()
    print(f"✓ Parsed {len(questions)} questions")
    
    chris_clean_content = generate_chris_clean(questions)
    chris_clean_path = Path("data_files/ia_bank/chris_clean.md")
    chris_clean_path.write_text(chris_clean_content, encoding="utf-8")
    print(f"✓ Wrote {len(questions)} questions to {chris_clean_path}")
    
    print("\nNext steps:")
    print("1. Update parse_security_bank.py to ingest chris_clean.md")
    print("2. Run 'npm run build:bank' to regenerate questions.json")
    print("3. Update README with new question count")
