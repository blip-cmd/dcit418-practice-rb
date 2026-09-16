from pathlib import Path
import re, unicodedata, difflib

ROOT=Path(__file__).parents[1]
def n(s):
    s=unicodedata.normalize('NFKD',s).encode('ascii','ignore').decode().lower()
    return re.sub(r'[^a-z0-9]+','',s)
def headings(p):
    return [m.group(2).strip() for m in re.finditer(r'^### (\d+)\.\s+(.*)$',p.read_text(errors='ignore'),re.M)]
def numbered(p):
    t=p.read_text(errors='ignore')
    return [m.group(1).replace('\n',' ').strip() for m in re.finditer(r'(?ms)^\d+\.\s+(.*?)(?=\n(?:A\.|Correct Answer:|The correct answer))',t)]
def loose(p):
    t=p.read_text(errors='ignore').replace('\r','')
    out=[]
    for line in t.splitlines():
        if re.match(r'^\s*(?:[-*]\s*)?A[.)]\s+',line):
            q=' '.join(out[-1].split()) if out else ''
            if q and len(q)>12: out[-1]=q
        elif line.strip():
            if out and out[-1].startswith('__Q__'): out[-1] += ' '+line.strip()
            else: out.append('__Q__ '+line.strip())
    return [x[6:].strip() for x in out if x.startswith('__Q__')]
def best(qs, bank):
    return [(q,max((difflib.SequenceMatcher(None,n(q),n(b)).ratio() for b in bank),default=0)) for q in qs]
quiz= sum((headings(p) for p in [ROOT/'data_files/quiz_bank/quiz_clean.md']),[])
ia=headings(ROOT/'data_files/ia_bank/ia_clean.md')
emma=[]
for p in [ROOT/'data_files/received qus/Emma/chatgpt.md',ROOT/'data_files/received qus/Emma/gemini.md']:
    qs=loose(p); emma += [(p.name,q) for q in qs]
report=['# Received-question audit','', 'Generated from the current banks and received files. Similarity is triage evidence, not proof of academic equivalence.','']
for name,bank in [('Quiz bank',quiz),('IA bank',ia)]:
    report += [f'## Emma against {name}','', '| File | Questions detected | >=0.72 similar | <0.72 similar |','|---|---:|---:|---:|']
    for p in sorted({x[0] for x in emma}):
        qs=[q for fn,q in emma if fn==p]; scores=[s for _,s in best(qs,bank)]
        report.append(f'| {p} | {len(qs)} | {sum(s>=.72 for s in scores)} | {sum(s<.72 for s in scores)} |')
    report.append('')
report += ['## Interpretation','', '- Emma chatgpt.md is an ECC/groups/discrete-log cluster and should be treated as IA-candidate material pending source confirmation.', '- Emma gemini.md begins with TLS/IPsec and continues through cryptography topics; topic continuity alone does not identify Quiz versus IA.', '- The exact break must be reviewed at the first low-overlap run boundary; no automatic bank append is made from an uncertain label.']
(ROOT/'RECEIVED_AUDIT.md').write_text('\n'.join(report)+'\n',encoding='utf8')
print('\n'.join(report))
