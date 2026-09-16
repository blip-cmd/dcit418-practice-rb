#!/usr/bin/env python3
"""
Parse and convert Christian's Quiz 1-5 exports to parser format.

Reads:
  - data_files/received qus/Chris/Quiz 1.md (8 questions, ChatGPT transcript
    style; one question's answer is unrecoverable from the source and is
    dropped rather than guessed)
  - data_files/received qus/Chris/Quiz 2.md (7 questions, same style)
  - data_files/received qus/Chris/Quiz 3.md (8 questions, same style; 4 lack
    a source explanation and get one written here)
  - data_files/received qus/Chris/quiz_4.md (noisy PDF-export style with
    duplicated intro content; parsed with an anchor-based extractor that
    walks backward from each answer line to find its stem and options)

Quiz 1-3 are small enough (23 usable questions total) that they were
transcribed by hand from the source after an automated parser proved
unreliable on their inconsistent formatting, then verified against the
raw file.

quiz_5.md is a garbled multilingual voice-transcript artifact (fragments
like "What's the answer?" and stray French/Japanese text) where the real
question text was never captured, only pieces of an AI's spoken-back
explanation. It is excluded entirely rather than have its questions
reconstructed from a guess.

Outputs:
  - data_files/quiz_bank/chris_quiz_clean.md (parser format, batch
    "chris_quiz"; kept separate from the "chris" IA-review batch so quiz
    and IA content are never mixed)
"""
import re
from pathlib import Path

# --- Quiz 1 (8 source questions, 1 dropped: its answer line does not match
# any of its own options and cannot be resolved from the source) ---------
QUIZ1 = [
    {
        "body": "Which element of the security policy framework requires approval from upper management and applies to the entire organization?",
        "options": [("A", "Policy"), ("B", "Standard"), ("C", "Guideline"), ("D", "Procedure")],
        "answer": "A",
        "explanation": "Policies are high-level statements that require senior/upper management approval and apply broadly across the entire organization, setting overall direction and intent. Standards, guidelines, and procedures typically flow from policies and can be approved/managed at lower levels since they support implementation rather than set organizational-wide mandate.",
    },
    {
        "body": "An information system is a safeguard or countermeasure an organization implements to help reduce risk.",
        "options": [("A", "True"), ("B", "False")],
        "answer": "B",
        "explanation": "This describes a control (safeguard/countermeasure to reduce risk), not an information system. An information system is the combination of hardware, software, data, and people used to collect, process, store, and distribute information, typically the asset being protected, not the safeguard itself.",
    },
    {
        "body": "The Local Area Network (LAN)-to-Wide Area Network (WAN) Domain is where the IT infrastructure links to a WAN and the Internet.",
        "options": [("A", "True"), ("B", "False")],
        "answer": "A",
        "explanation": "The LAN-to-WAN Domain is exactly the boundary where an organization's internal network connects out to a wide area network and the public internet.",
    },
    {
        "body": "Cryptography is the practice of making data unreadable.",
        "options": [("A", "True"), ("B", "False")],
        "answer": "A",
        "explanation": "Cryptography transforms plaintext into ciphertext that is unreadable without the correct key, which is the core purpose the statement describes.",
    },
    {
        "body": "Availability is the tenet of information security that deals with uptime and downtime.",
        "options": [("A", "True"), ("B", "False")],
        "answer": "A",
        "explanation": "Availability, one leg of the CIA triad, means authorized users can access information and systems when needed, which is exactly a matter of uptime versus downtime.",
    },
    {
        "body": "The Sarbanes-Oxley Act (SOX) requires all types of financial institutions to protect customers' private financial information.",
        "options": [("A", "True"), ("B", "False")],
        "answer": "B",
        "explanation": "This describes the Gramm-Leach-Bliley Act (GLBA), not SOX. SOX applies to publicly traded companies and focuses on the accuracy and reliability of financial reporting and corporate governance controls, it isn't specifically about protecting customers' private financial information at financial institutions.",
    },
    {
        "body": "A router is a security appliance that is used to filter Internet Protocol (IP) packets and block unwanted packets.",
        "options": [("A", "True"), ("B", "False")],
        "answer": "B",
        "explanation": "A router's primary function is to forward and route traffic between networks based on IP addresses, it is a networking device, not a security appliance. While routers can use access control lists to filter some traffic, that description more accurately fits a firewall, whose primary purpose is filtering and blocking unwanted packets for security.",
    },
]

# --- Quiz 2 (7 questions, all answerable) --------------------------------
QUIZ2 = [
    {
        "body": "Vendors or service providers that have remote access to an Internet of Things (IoT) device may be able to pull information or data from your device without your permission.",
        "options": [("A", "True"), ("B", "False")],
        "answer": "A",
        "explanation": "Vendors with remote access to an IoT device can typically pull data/telemetry from it as part of normal operation (diagnostics, updates, usage analytics), often under terms buried in a EULA or privacy policy the user never fully reads or meaningfully consents to. So functionally, data can be collected without the user's informed permission, even if it's technically authorized in some fine print.",
    },
    {
        "body": "Which of the following is an example of a business-to-consumer (B2C) application of the Internet of Things (IoT)?",
        "options": [("A", "Video conferencing"), ("B", "Infrastructure monitoring"), ("C", "Health monitoring"), ("D", "Traffic monitoring")],
        "answer": "C",
        "explanation": "Health monitoring (like wearable fitness trackers, smartwatches, or remote patient monitoring devices) is a direct B2C application, businesses provide these IoT devices/services directly to individual consumers. Infrastructure and traffic monitoring are typically government/enterprise applications, and video conferencing isn't inherently an IoT application.",
    },
    {
        "body": "Application service providers (ASPs) are software companies that build applications hosted in the cloud and on the Internet.",
        "options": [("A", "True"), ("B", "False")],
        "answer": "A",
        "explanation": "Application Service Providers develop, host, and deliver software applications to customers over the Internet/cloud rather than requiring users to install and run the software locally, customers access the application remotely, typically via a web browser.",
    },
    {
        "body": "The ownership of Internet of Things (IoT) data, as well as the metadata of that data, is sometimes in question.",
        "options": [("A", "True"), ("B", "False")],
        "answer": "A",
        "explanation": "Data ownership in IoT is often ambiguous, it's frequently unclear whether the device manufacturer, the service provider, or the end user actually owns the data (and associated metadata) generated by the device, and terms of service agreements don't always clarify this in a way that's favorable or transparent to the consumer.",
    },
    {
        "body": "Internet of Things (IoT) upgrades can be difficult to distribute and deploy, leaving gaps in the remediation of IoT devices or endpoints.",
        "options": [("A", "True"), ("B", "False")],
        "answer": "A",
        "explanation": "IoT upgrades and patches can be difficult to distribute and deploy due to device diversity, limited connectivity, vendor support lifecycles, resource-constrained hardware, and devices deployed in hard-to-reach locations, which often leaves security gaps where vulnerabilities remain unremediated for extended periods.",
    },
    {
        "body": "Which organization pursues standards for Internet of Things (IoT) devices and is widely recognized as the authority for creating standards on the Internet?",
        "options": [("A", "Internet Society"), ("B", "Internet Engineering Task Force (IETF)"), ("C", "Internet Association"), ("D", "Internet Authority")],
        "answer": "B",
        "explanation": "The IETF is widely recognized as the leading authority for developing and maintaining Internet standards, including protocols relevant to IoT. The Internet Society is IETF's parent organization but isn't itself the standards-writing body, and the other two options aren't legitimate standards organizations.",
    },
    {
        "body": "Vehicles that have Wi-Fi access and onboard computers require software patches and upgrades from the manufacturer.",
        "options": [("A", "True"), ("B", "False")],
        "answer": "A",
        "explanation": "Modern vehicles with Wi-Fi connectivity and onboard computers run software just like any connected device, and manufacturers need to issue patches and upgrades to fix bugs, address security vulnerabilities, and add functionality, much like smartphones or computers receive over-the-air updates.",
    },
]

# --- Quiz 3 (8 questions, 4 lack a source explanation and get one here) --
QUIZ3 = [
    {
        "body": "Sharing in the data lifecycle means:",
        "options": [("A", "Never share"), ("B", "Sell without consent"), ("C", "Enable reuse"), ("D", "Share only with competitors")],
        "answer": "C",
        "explanation": "In the data lifecycle, the sharing stage refers to making data available for others to access, use, or build on, enabling reuse (internally across teams, or externally with partners or the public), typically under defined permissions or licenses. It's not about selling data, restricting it entirely, or limiting it to competitors.",
    },
    {
        "body": "A benefit of conducting a Data Protection Impact Assessment (DPIA) is:",
        "options": [("A", "Builds public trust"), ("B", "Increases data breaches"), ("C", "Ignores privacy risks"), ("D", "Reduces compliance")],
        "answer": "A",
        "explanation": "A DPIA identifies and mitigates privacy risks before a system or process launches, and demonstrating that care publicly signals accountability to users and regulators, which is what builds trust. The other options describe outcomes a DPIA is specifically meant to prevent, not produce.",
    },
    {
        "body": "A DPIA should be reviewed:",
        "options": [("A", "When processing changes or regularly"), ("B", "Only once"), ("C", "Every ten years"), ("D", "Never again")],
        "answer": "A",
        "explanation": "A DPIA isn't a one-and-done exercise, it should be revisited whenever there's a significant change to the processing activity (new data types, new purposes, new systems) or on a regular schedule, since risks can evolve over time. Treating it as a single, permanent assessment defeats its purpose of ongoing risk management.",
    },
    {
        "body": "Data localization drives investment in:",
        "options": [("A", "Offshore storage"), ("B", "Local data centers"), ("C", "Manual record keeping"), ("D", "Foreign data centers")],
        "answer": "B",
        "explanation": "Data localization laws require certain data to be stored and processed within a country's own borders, so complying with them directly drives investment in local data center infrastructure rather than offshore or foreign facilities.",
    },
    {
        "body": "A Data Protection Impact Assessment (DPIA) is:",
        "options": [("A", "A process to identify privacy risks before launch"), ("B", "Used only after a breach"), ("C", "Optional under all laws"), ("D", "Only for government agencies")],
        "answer": "A",
        "explanation": "A DPIA is a proactive process conducted before deployment to identify and mitigate privacy risks, not something used reactively after a breach, and it's legally mandatory (not optional) under laws like Ghana's Act 843 and Nigeria's NDPA, applying broadly rather than only to government agencies.",
    },
    {
        "body": "Many African countries lack:",
        "options": [("A", "Internet access completely"), ("B", "Interest in technology"), ("C", "Skilled data-hosting professionals"), ("D", "Basic electricity")],
        "answer": "C",
        "explanation": "A recognized barrier to building local data-hosting capacity across much of Africa is a shortage of professionals skilled in data center operations and hosting infrastructure, not a lack of internet access, interest in technology, or electricity in absolute terms.",
    },
    {
        "body": "Strict localization rules across Africa can:",
        "options": [("A", "Remove competition"), ("B", "Create one digital market"), ("C", "Split Africa's digital market"), ("D", "Reduce compliance costs")],
        "answer": "C",
        "explanation": "If different African countries impose strict, inconsistent localization requirements, it creates barriers between national markets rather than unifying them, working against efforts like AfCFTA's Digital Trade Protocol to build an integrated continental digital economy.",
    },
    {
        "body": "The opposite of Privacy by Design is:",
        "options": [("A", "Continuous privacy"), ("B", "Proactive privacy"), ("C", "Privacy added at the end"), ("D", "Built-in privacy")],
        "answer": "C",
        "explanation": "Privacy by Design means privacy protections are built into a system from the start; its opposite is bolting privacy measures on only after the system is already built, as an afterthought rather than a foundational requirement.",
    },
]


# quiz_4.md ends with a run of questions the source never explained at all
# (the transcript shifts to "fast answers, no fluff" mode); these fill the gap.
QUIZ4_EXPLANATIONS = {
    "A key advantage of the Feistel structure is that:": "A Feistel cipher's decryption process is structurally identical to encryption, just run with the round subkeys in reverse order, so the same hardware or software implementation can perform both operations, with no need for a separate inverse cipher.",
    "AES was originally designed and submitted to NIST under the name ____": "Rijndael, designed by Joan Daemen and Vincent Rijmen, was the algorithm NIST selected through its open competition and standardized as AES.",
    "Fermat's Little Theorem and Euler's Theorem are foundational to the correctness of the ____ public-key algorithm.": "RSA's decryption correctness proof relies on Fermat's Little Theorem for a prime modulus, generalized by Euler's Theorem to RSA's composite modulus n = p times q.",
    "A cipher in which plaintext bits or letters are rearranged without changing their values is called a ____ cipher.": "A transposition (or permutation) cipher only reorders the positions of plaintext symbols; it never substitutes one symbol for another, which is what distinguishes it from a substitution cipher.",
    "Which mode of block cipher operation encrypts blocks independently without chaining, so identical plaintext blocks produce identical ciphertext blocks?": "ECB (Electronic Codebook) encrypts each block independently under the same key with no dependency on previous blocks or an IV, so identical plaintext blocks always produce identical ciphertext blocks, which is exactly the pattern-leakage weakness that makes it unsafe for most data.",
}


def strip_noise(text: str) -> str:
    lines = text.split("\n")
    out = []
    for line in lines:
        s = line.strip()
        core = re.sub(r"^[>\-*]\s*", "", s)
        if core == "PDF" or re.match(r"^PDF\+\s*\d+$", core):
            continue
        if s.startswith("Blank ") and "fill in the blank" in s.lower():
            continue
        if s.lower().startswith("what follows is a fill in the blank"):
            continue
        if s in ("# Maybe Quiz 4", "Reset Selection"):
            continue
        if s.lower().startswith("please provide fast answers") or s.lower().startswith("understood. send your questions"):
            continue
        out.append(line)
    return "\n".join(out)


def is_noise_or_blank(s: str) -> bool:
    return s == "" or s.startswith("#") or s.startswith(">") or s.startswith("-")


def find_stem_backward(lines, start_idx, needs_options):
    i = start_idx - 1
    options = []
    if needs_options:
        opt_lines = []
        while i >= 0:
            s = lines[i].strip()
            if re.match(r"^[A-D]\.\s+", s):
                opt_lines.append(s)
                i -= 1
                continue
            if s == "":
                i -= 1
                continue
            break
        opt_lines.reverse()
        for ol in opt_lines:
            m = re.match(r"^([A-D])\.\s+(.+)$", ol)
            if m:
                options.append((m.group(1), m.group(2)))
        if len(options) < 2:
            return None, [], i
    while i >= 0 and lines[i].strip() == "":
        i -= 1
    if i < 0:
        return None, options, i
    s = lines[i].strip()
    if is_noise_or_blank(s) or re.match(r"^\*\*", s):
        return None, options, i
    stem_lines = [s]
    j = i - 1
    while j >= 0 and lines[j].strip() != "":
        prev = lines[j].strip()
        if is_noise_or_blank(prev) or re.match(r"^[A-D]\.\s+", prev) or re.match(r"^\*\*", prev):
            break
        stem_lines.append(prev)
        j -= 1
    stem_lines.reverse()
    stem = " ".join(stem_lines)
    stem_start = i - len(stem_lines) + 1
    return stem, options, stem_start


def clean_explanation(block_lines):
    text_lines = []
    for line in block_lines:
        s = line.strip()
        if s == "":
            continue
        s = re.sub(r"^#+\s*", "", s)
        s = re.sub(r"^[-*]\s*", "", s)
        s = re.sub(r"^>\s*", "", s)
        text_lines.append(s)
    joined = " ".join(text_lines)
    return re.sub(r"\s*—\s*", ", ", joined)


def parse_quiz4() -> list[dict]:
    path = Path("data_files/received qus/Chris/quiz_4.md")
    raw = strip_noise(path.read_text(encoding="utf-8"))
    lines = raw.split("\n")

    anchors = []
    for idx, line in enumerate(lines):
        s = line.strip()
        m = re.match(r"^(?:The correct answer is\s*)?\*\*([A-D])\.\s*(.+?)\*\*\.?$", s)
        if m:
            anchors.append((idx, "mcq", m.group(1), m.group(2)))
            continue
        m2 = re.match(r"^\*\*(.+?)\*\*(?:\s*[_(].*)?$", s)
        if m2 and len(s) < 120:
            anchors.append((idx, "fill", None, m2.group(1)))

    parsed = []
    for idx, kind, letter, ans_text in anchors:
        stem, options, stem_start = find_stem_backward(lines, idx, kind == "mcq")
        if stem is None:
            continue
        if kind == "fill" and "____" not in stem:
            continue
        parsed.append({
            "kind": kind, "body": stem, "options": options,
            "answer": letter, "answer_text": ans_text,
            "anchor_idx": idx, "stem_start": stem_start,
        })

    for k, q in enumerate(parsed):
        end = parsed[k + 1]["stem_start"] if k + 1 < len(parsed) else len(lines)
        block = lines[q["anchor_idx"] + 1:end]
        q["explanation"] = clean_explanation(block)

    return parsed


def generate_clean_md() -> str:
    lines = [
        "# DCIT418: Christian's Quiz 1-3 and Quiz 4 (Parser Format)",
        "",
        "Christian's Quiz 1-3 (IT security policy/7 domains and IoT topics) and Quiz 4",
        "(cryptography and block cipher topics), formatted for parse_security_bank.py.",
        "Quiz 1-3 were transcribed by hand after an automated parser proved unreliable",
        "on their inconsistent formatting; Quiz 4 was extracted with an anchor-based",
        "parser. Quiz 5 is excluded entirely: it is a garbled multilingual voice",
        "transcript in which the real question text was never captured.",
        "",
    ]
    n = 0
    for q in QUIZ1 + QUIZ2 + QUIZ3:
        n += 1
        lines.append(f"### {n}. {q['body']}")
        lines.append("")
        for letter, text in q["options"]:
            lines.append(f"- {letter}. {text}")
        lines.append("")
        ans_text = dict(q["options"])[q["answer"]]
        lines.append(f"**Correct Answer:** **{q['answer']}. {ans_text}**")
        lines.append("")
        lines.append(f"**Intuition:** {q['explanation']}")
        lines.append("")
        lines.append("---")
        lines.append("")

    for q in parse_quiz4():
        n += 1
        lines.append(f"### {n}. {q['body']}")
        lines.append("")
        if q["kind"] == "mcq":
            for letter, text in q["options"]:
                lines.append(f"- {letter}. {text}")
            lines.append("")
            lines.append(f"**Correct Answer:** **{q['answer']}. {q['answer_text']}**")
        else:
            lines.append(f"**Correct Answer:** **{q['answer_text']}**")
        lines.append("")
        expl = q["explanation"] or QUIZ4_EXPLANATIONS.get(q["body"], "See answer key for detailed reasoning.")
        lines.append(f"**Intuition:** {expl}")
        lines.append("")
        lines.append("---")
        lines.append("")

    return "\n".join(lines)


if __name__ == "__main__":
    content = generate_clean_md()
    out_path = Path("data_files/quiz_bank/chris_quiz_clean.md")
    out_path.write_text(content, encoding="utf-8")
    count = content.count("\n### ")
    print(f"Wrote {count} questions to {out_path}")
