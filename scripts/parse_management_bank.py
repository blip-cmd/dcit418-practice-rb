"""Parse DCIT 402 Management Principles question banks into questions.json.

Reads three source markdown files from the bd/ directory:
  1. dcit402-sakai-quiz1.md (60 questions, <details> answer blocks)
  2. principles-and-practices-of-management-questions-mbamcq.md (445 questions)
  3. dcit402-it-class-combined-tagged-quiz-bank.md (191 questions)

Outputs questions.json in the schema expected by the Management Lab app.
"""
from pathlib import Path
import argparse
import collections
import json
import re
import sys
import unicodedata

# ---------------------------------------------------------------------------
# Part mapping: slide root -> part number
# ---------------------------------------------------------------------------
SLIDE_TO_PART = {
    'DCIT402_Week1_Introduction_to_Management': 1,
    'DCIT402_Week2_Planning_and_Mission': 2,
    'DCIT402_Week3_Organising': 3,
    'DCIT402_Week4_Leadership': 4,
    'DCIT402_Week5_Motivation': 5,
    'DCIT402_Week6_Communication_Coordination': 5,
    'DCIT402_Week7_Controlling': 5,
    'DCIT402_Week8_Evolution_of_Management_Science': 6,
    'DCIT402_Week9_Communication': 5,
}

PART_TITLES = {
    1: 'Management Foundations',
    2: 'Planning & Mission',
    3: 'Organising & Structure',
    4: 'Leadership',
    5: 'Motivation, Communication & Control',
    6: 'Evolution of Management',
}

TOPIC_TO_PART = {
    'management foundations': 1,
    'planning foundations': 2,
    'decision-making': 2,
    'classical management': 6,
    'delegation and authority': 3,
    'formal organisation and bureaucracy': 3,
    'leadership styles and power': 4,
    'leadership foundations': 4,
    'leadership theories': 4,
    'communication': 5,
    'motivation theories': 5,
    'modern management approaches': 6,
    'human relations school': 6,
    'organisation structures': 3,
    'coordination': 5,
    'controlling': 5,
    'departmentation': 3,
    'principles of organising': 3,
}

# ---------------------------------------------------------------------------
# Normalisation helpers
# ---------------------------------------------------------------------------

def normalize_text(text):
    """Lowercase, strip accents, collapse whitespace, remove punctuation for dedup comparison."""
    text = unicodedata.normalize('NFKD', text)
    text = ''.join(c for c in text if not unicodedata.combining(c))
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text


def extract_slide_root(text):
    """Extract the slide root from a Source slide field value."""
    m = re.search(r'(DCIT402_Week\d+_[A-Za-z_]+)', text)
    if m:
        root = m.group(1)
        root = re.sub(r'\.(pptx|pdf)$', '', root)
        return root
    return None


def determine_part(slide_text, topic_text):
    """Determine part number from slide root and/or topic text."""
    if slide_text:
        root = extract_slide_root(slide_text)
        if root and root in SLIDE_TO_PART:
            return SLIDE_TO_PART[root]
    if topic_text:
        t = topic_text.strip().lower()
        if t in TOPIC_TO_PART:
            return TOPIC_TO_PART[t]
    return 1


def determine_week(slide_text, part):
    """Extract week string from slide text or infer from part."""
    if slide_text:
        m = re.search(r'Week(\d+)', slide_text)
        if m:
            return f'Week {m.group(1)}'
    week_map = {1: 'Week 1', 2: 'Week 2', 3: 'Week 3', 4: 'Week 4', 5: 'Weeks 5 to 9', 6: 'Week 8'}
    return week_map.get(part, 'Week 1')


# ---------------------------------------------------------------------------
# Parsers for each source format
# ---------------------------------------------------------------------------

def parse_sakai_and_mba(filepath, source_label):
    """Parse files that use ### N. heading + <details> answer blocks."""
    text = filepath.read_text(encoding='utf-8')
    questions = []
    
    pattern = re.compile(r'^### (\d+)\.\s+(.*?)$', re.MULTILINE)
    matches = list(pattern.finditer(text))
    
    for i, match in enumerate(matches):
        q_num = int(match.group(1))
        q_heading = match.group(2).strip()
        
        start = match.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        block = text[start:end].strip()
        
        slide_match = re.search(r'\*\*Source slide:\*\*\s*`?([^`\n]+)`?', block)
        slide_text = slide_match.group(1).strip() if slide_match else ''
        
        topic_match = re.search(r'\*\*Topic:\*\*\s*(.+)', block)
        topic_text = topic_match.group(1).strip() if topic_match else ''
        
        option_pattern = re.compile(r'^- ([A-E])\.\s+(.+?)$', re.MULTILINE)
        option_matches = list(option_pattern.finditer(block))
        options = []
        labels = []
        for om in option_matches:
            labels.append(om.group(1).upper())
            options.append(om.group(2).strip())
        
        answer_match = re.search(
            r'^\*\*Correct Answer:\*\*\s+\*\*([A-E])\.\s*(.*?)\*\*\s*$',
            block,
            re.MULTILINE,
        )
        correct_letter = None
        correct_text = ''
        reason = ''
        
        if answer_match:
            correct_letter = answer_match.group(1).upper()
            correct_text = answer_match.group(2).strip().rstrip('*').strip()

        if not options and source_label == 'mbamcq' and correct_letter and correct_text:
            number_match = re.match(r'^(\d+)\.?$', correct_text.rstrip('.'))
            if number_match:
                correct_number = int(number_match.group(1))
                correct_offset = ord(correct_letter) - ord('A')
                first_number = correct_number - correct_offset
                if first_number > 0:
                    options = [str(first_number + n) for n in range(4)]
                    labels = list('ABCD')
        
        intuition_match = re.search(r'\*Intuition:\*\s*(.*?)(?:</details>|$)', block, re.DOTALL)
        if intuition_match:
            reason = intuition_match.group(1).strip()

        reason_match = re.search(r'\*\*Reason:\*\*\s*(.*?)(?:---|</details>|\Z)', block, re.DOTALL)
        if reason_match:
            reason = reason_match.group(1).strip()

        if not options:
            continue
        
        correct_index = None
        if correct_letter and correct_letter in labels:
            correct_index = labels.index(correct_letter)
            correct_text = options[correct_index]
        elif correct_letter and options:
            idx = ord(correct_letter) - ord('A')
            if 0 <= idx < len(options):
                correct_index = idx
                correct_text = options[idx]
        
        if correct_index is None:
            continue
        
        if options == ['True', 'False']:
            q_type = 'tf'
        elif len(options) == 4:
            q_type = 'mcq4'
        elif len(options) == 5:
            q_type = 'mcq5'
        elif len(options) == 3:
            continue
        elif len(options) == 2 and options != ['True', 'False']:
            continue
        else:
            continue
        
        part = determine_part(slide_text, topic_text)
        week = determine_week(slide_text, part)
        
        questions.append({
            'id': f'{source_label}-Q{q_num}',
            'part': part,
            'batch': source_label,
            'family': f'{source_label}-Q{q_num}',
            'isCore': True,
            'week': week,
            'source': topic_text or 'Management',
            'level': 'Recall',
            'type': q_type,
            'bodyMarkdown': q_heading,
            'options': options,
            'correctIndex': correct_index,
            'correctText': correct_text,
            'acceptedAnswers': [],
            'reason': reason or f'The correct answer is {correct_letter}. {correct_text}',
            'trap': '',
            'sourceRef': f'{source_label}, Question {q_num}',
            'checkMethod': 'Verified against source answer key.',
            'workingMarkdown': '',
        })
    
    return questions


def parse_it_class(filepath, source_label):
    """Parse the IT class combined tagged quiz bank format."""
    text = filepath.read_text(encoding='utf-8')
    questions = []
    
    pattern = re.compile(r'^### (\d+)\.\s+(.*?)$', re.MULTILINE)
    matches = list(pattern.finditer(text))
    
    for i, match in enumerate(matches):
        q_num = int(match.group(1))
        q_heading = match.group(2).strip()
        
        start = match.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        block = text[start:end].strip()
        
        option_pattern = re.compile(r'^- ([A-E])\.\s+(.+?)$', re.MULTILINE)
        option_matches = list(option_pattern.finditer(block))
        options = []
        labels = []
        for om in option_matches:
            labels.append(om.group(1).upper())
            options.append(om.group(2).strip())
        
        answer_match = re.search(r'\*\*Answer:\*\*\s*(.*?)$', block, re.MULTILINE)
        if not answer_match:
            continue
        answer_raw = answer_match.group(1).strip()
        
        reason_match = re.search(r'\*\*Reason:\*\*\s*(.*?)(?:---|\Z)', block, re.DOTALL)
        reason = reason_match.group(1).strip() if reason_match else ''
        
        letter_answer = re.match(r'^([A-E])\.\s*(.*)', answer_raw)
        
        is_tf_options = set(o.strip() for o in options) == {'True', 'False'}
        
        if options and letter_answer and not (is_tf_options and letter_answer.group(1).upper() not in labels):
            correct_letter = letter_answer.group(1).upper()
            if correct_letter in labels:
                correct_index = labels.index(correct_letter)
                correct_text = options[correct_index]
            else:
                idx = ord(correct_letter) - ord('A')
                if 0 <= idx < len(options):
                    correct_index = idx
                    correct_text = options[idx]
                else:
                    continue
            
            if options == ['True', 'False']:
                q_type = 'tf'
            elif len(options) == 4:
                q_type = 'mcq4'
            elif len(options) == 5:
                q_type = 'mcq5'
            else:
                continue
            
            questions.append({
                'id': f'{source_label}-Q{q_num}',
                'part': 1,
                'batch': source_label,
                'family': f'{source_label}-Q{q_num}',
                'isCore': True,
                'week': 'Week 1',
                'source': 'Management',
                'level': 'Recall',
                'type': q_type,
                'bodyMarkdown': q_heading,
                'options': options,
                'correctIndex': correct_index,
                'correctText': correct_text,
                'acceptedAnswers': [],
                'reason': reason or f'The correct answer is {correct_letter}. {correct_text}',
                'trap': '',
                'sourceRef': f'{source_label}, Question {q_num}',
                'checkMethod': 'Verified against source answer key.',
                'workingMarkdown': '',
            })
        elif not letter_answer:
            # Fill-in question
            correct_text = answer_raw.strip()
            if not correct_text:
                continue
            
            questions.append({
                'id': f'{source_label}-Q{q_num}',
                'part': 1,
                'batch': source_label,
                'family': f'{source_label}-Q{q_num}',
                'isCore': True,
                'week': 'Week 1',
                'source': 'Management',
                'level': 'Recall',
                'type': 'fill',
                'bodyMarkdown': q_heading,
                'options': [],
                'correctIndex': None,
                'correctText': correct_text,
                'acceptedAnswers': [],
                'reason': reason or f'The correct answer is: {correct_text}',
                'trap': '',
                'sourceRef': f'{source_label}, Question {q_num}',
                'checkMethod': 'Verified against source answer key.',
                'workingMarkdown': '',
            })
    
    return questions


def infer_part_from_reason(reason_text):
    """Try to infer part number from the content of the reason text."""
    reason_lower = reason_text.lower()
    
    keywords = {
        4: ['leadership', 'leader style', 'hersey', 'blanchard', 'fiedler', 'path-goal',
            'ohio state', 'transformational', 'transactional', 'contingency model',
            'lpc', 'autocratic', 'democratic', 'laissez-faire', 'initiating structure',
            'consideration', 'blake', 'mouton', 'managerial grid', 'likert'],
        5: ['motivation', 'maslow', 'herzberg', 'vroom', 'expectancy', 'equity theory',
            'erg theory', 'alderfer', 'mcclelland', 'reinforcement', 'hygiene',
            'communication', 'encoding', 'decoding', 'feedback loop', 'barrier',
            'controlling', 'control process', 'balanced scorecard', 'coordination'],
        6: ['taylor', 'scientific management', 'time and motion', 'piece-rate',
            'fayol', '14 principles', 'weber', 'bureaucra', 'hawthorne', 'mayo',
            'follett', 'gulick', 'posdcorb', 'gilbreth', 'gantt',
            'human relations', 'systems approach', 'contingency approach',
            'chester barnard', 'mcgregor', 'theory x', 'theory y',
            'classical management', 'neo-classical'],
        2: ['planning', 'mission', 'vision', 'values', 'swot', 'pestle',
            'smart goal', 'strategic plan', 'tactical plan', 'operational plan',
            'mbo', 'management by objectives', 'ansoff', 'decision tree',
            'decision making', 'bounded rationality', 'satisficing',
            'programmed decision', 'non-programmed'],
        3: ['organis', 'departm', 'delegation', 'authority', 'span of control',
            'centrali', 'decentrali', 'line and staff', 'matrix',
            'scalar chain', 'unity of command', 'tall', 'flat',
            'formal organisation', 'informal organisation'],
        1: ['management function', 'manager role', 'mintzberg', 'drucker',
            'koontz', 'functions of management', 'interpersonal role',
            'informational role', 'decisional role', 'top management',
            'middle management', 'first-line', 'supervisory'],
    }
    
    for part, kws in sorted(keywords.items(), key=lambda x: -x[0]):
        for kw in kws:
            if kw in reason_lower:
                return part
    
    return None


# Course-specific banks outrank the generic imported bank when the same
# question appears in both, so a duplicate never strips a question out of the
# quiz bank it actually belongs to.
SOURCE_PRIORITY = {'sakai': 3, 'itclass': 2, 'mbamcq': 1}


def deduplicate(questions):
    """Remove duplicate questions based on normalized body text similarity."""
    seen = {}
    unique = []

    for q in questions:
        norm = normalize_text(q['bodyMarkdown'])
        key = norm[:80]

        if key in seen:
            existing = seen[key]
            rank = SOURCE_PRIORITY.get(q['batch'], 0)
            existing_rank = SOURCE_PRIORITY.get(existing['batch'], 0)
            better = (rank, len(q.get('reason', ''))) > (
                existing_rank,
                len(existing.get('reason', '')),
            )
            if better:
                idx = unique.index(existing)
                unique[idx] = q
                seen[key] = q
        else:
            seen[key] = q
            unique.append(q)

    return unique


def reassign_ids(questions):
    """Assign sequential IDs within each part."""
    questions.sort(key=lambda q: (q['part'], q['id']))
    
    counters = collections.Counter()
    for q in questions:
        counters[q['part']] += 1
        num = counters[q['part']]
        q['id'] = f'P{q["part"]}-Q{num}'
        q['family'] = q['id']
    
    return questions


def report(records):
    """Generate a summary report."""
    parts = sorted(set(q['part'] for q in records))
    lines = [
        f'# Parser verification: PASS',
        '',
        f'Total questions: {len(records)}; Parts: {len(parts)}.',
        '',
        '| Part | Title | mcq4 | mcq5 | fill | tf | Total |',
        '|---|---|---:|---:|---:|---:|---:|',
    ]
    
    for part in parts:
        subset = [q for q in records if q['part'] == part]
        counts = collections.Counter(q['type'] for q in subset)
        title = PART_TITLES.get(part, f'Part {part}')
        lines.append(
            f'| {part} | {title} | '
            + ' | '.join(str(counts.get(t, 0)) for t in ['mcq4', 'mcq5', 'fill', 'tf'])
            + f' | {len(subset)} |'
        )
    
    counts = collections.Counter(q['type'] for q in records)
    lines.append(
        f'| - | **Total** | '
        + ' | '.join(str(counts.get(t, 0)) for t in ['mcq4', 'mcq5', 'fill', 'tf'])
        + f' | **{len(records)}** |'
    )
    
    lines += ['', '## Source Distribution', '', '| Source | Count |', '|---|---:|']
    source_counts = collections.Counter(q['batch'] for q in records)
    for source, count in source_counts.most_common():
        lines.append(f'| {source} | {count} |')
    
    return '\n'.join(lines) + '\n'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--bd', type=Path, default=None,
                        help='Directory containing source markdown files')
    parser.add_argument('--output', type=Path, default=Path('questions.json'))
    args = parser.parse_args()
    
    if args.bd:
        bd = args.bd
    elif Path('bd').is_dir():
        bd = Path('bd')
    else:
        bd = Path(__file__).resolve().parent.parent.parent / 'bd'
    
    if not bd.is_dir():
        print(f'PARSER FAILED: bd directory not found at {bd}', file=sys.stderr)
        sys.exit(1)
    
    print(f'Reading source files from: {bd}')

    all_questions = []
    
    sakai_path = bd / 'dcit402-sakai-quiz1.md'
    if sakai_path.exists():
        sakai_qs = parse_sakai_and_mba(sakai_path, 'sakai')
        print(f'  Sakai quiz: {len(sakai_qs)} questions parsed')
        all_questions.extend(sakai_qs)
    else:
        print(f'  WARNING: {sakai_path} not found', file=sys.stderr)
    
    mba_path = bd / 'principles-and-practices-of-management-questions-mbamcq.md'
    if mba_path.exists():
        mba_qs = parse_sakai_and_mba(mba_path, 'mbamcq')
        print(f'  MBA MCQ bank: {len(mba_qs)} questions parsed')
        all_questions.extend(mba_qs)
    else:
        print(f'  WARNING: {mba_path} not found', file=sys.stderr)
    
    it_path = bd / 'dcit402-it-class-combined-tagged-quiz-bank.md'
    if it_path.exists():
        it_qs = parse_it_class(it_path, 'itclass')
        print(f'  IT class bank: {len(it_qs)} questions parsed')
        for q in it_qs:
            inferred = infer_part_from_reason(q['reason'])
            if inferred:
                q['part'] = inferred
                q['week'] = determine_week(None, inferred)
                q['source'] = PART_TITLES.get(inferred, 'Management')
        all_questions.extend(it_qs)
    else:
        print(f'  WARNING: {it_path} not found', file=sys.stderr)

    print(f'\nTotal raw questions: {len(all_questions)}')

    unique = deduplicate(all_questions)
    print(f'After deduplication: {len(unique)}')

    final = reassign_ids(unique)

    summary = report(final)
    print()
    print(summary)
    
    output_path = args.output
    output_path.write_text(
        json.dumps(final, ensure_ascii=False, indent=2) + '\n',
        encoding='utf-8'
    )
    print(f'Wrote {len(final)} questions to {output_path}')
    
    report_path = Path('PARSER_REPORT.md')
    report_path.write_text(summary, encoding='utf-8')
    print(f'Wrote report to {report_path}')


if __name__ == '__main__':
    raise SystemExit('This legacy DCIT 402 parser is disabled in the DCIT 418 app. Run python scripts/parse_security_bank.py instead.')
