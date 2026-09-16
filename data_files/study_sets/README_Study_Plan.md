# DCIT418 — Revision Pack
## How to use these files

## TODO: Update study sets for the new exam format

- [ ] Update the study sets, especially the SET3 and SET9 exam papers, their answer keys, and this study plan, to match the new format: **50 multiple-choice questions (MCQs), 10 fill-in questions, and 2 practical questions**. Include applied security scenarios such as how ATMs store and verify passwords/PINs. Reconcile the existing section instructions and question counts with this format.
- [ ] `data_files/study_sets/SET5_clean.md`: all 100 fill-in questions share the same generic placeholder reason, "Fill-in precision is critical on Sakai exams.", instead of a real, question-specific explanation. Write actual reasons for each, matching the quality bar used for the other clean.md sources (chris_clean.md, desmond_clean.md, chris_quiz_clean.md).

The existing papers below still use the previous format until this task is completed.

**Exam format:** 60 minutes on Sakai. MCQs, fill-ins, essay. Chapters 1–13. No calculation questions, though simple worked examples remain because they build understanding one could be asked to explain in words.

---

## What is in the pack

All nine sets now cover Chapters 1–13 and match the Sakai format. Chapter 11–13 material sits in clearly marked sections at the end of each set.

**Depth sets — build and test understanding**
| File | What it is |
|---|---|
| SET1 | Knowledge, factual recall and vocabulary. 130 marks. |
| SET2 | Reasoning and application. Section A trimmed to eight simple worked examples; the weight now sits in 16 reasoning scenarios. |
| SET2B | The "why" paper. 52 design-rationale questions. The hardest set here, and the one that moves a B to an A. |

**Format sets — match the exam shape**
| File | What it is |
|---|---|
| SET4 | MCQ drill. 100 questions. |
| SET5 | Fill-in-the-blanks. 100 blanks. |
| SET6 | Essay bank. 24 prompts with skeletons. |
| SET7 | Confusion pairs. The distinctions MCQ distractors are built from. |
| SET8 | Tools and labs. Light, 20 minutes, insurance only. |

**Full papers — sit under timed conditions**
| File | What it is |
|---|---|
| SET3 | Sakai-format paper: 30 MCQ, 25 fill-in, 2 essays chosen from 6. |
| SET9 | Second Sakai-format paper: 30 MCQ, 25 fill-in, 3 essays chosen from 7. |

Sets 3 and 9 are different papers. Sit one, mark it, patch the gaps, then sit the other a day later.

---

## On the calculations

The exam has none, so Set 2's calculation section is down to eight short items and Set 3's have gone entirely. The ones kept are there because working a Vigenère or an RSA key generation by hand is what makes you able to *explain* them in words, which is what the essay section will actually ask for. Four minutes each, no more. Do not grind them.

---

## Sequence

**First:** Chapters 11, 12 and 13 have not been taught yet. Every set now contains questions on them. Do not attempt those sections cold — study the blocks, then sit the papers.

Once Ch 11–13 are covered:

1. **SET7** first. Thirty minutes. It sharpens the distinctions everything else depends on.
2. **SET4**, then **SET5**. Format-matched recall drills, carrying most of the marks on a Sakai paper.
3. **SET1** if recall is still shaky after those. It is broader and slower.
4. **SET6**, skeletons from memory only. Then write three prompts out in full at exam speed.
5. **SET2** and **SET2B** for the reasoning depth that essays reward.
6. **SET8** if time allows. Twenty minutes, no more.
7. **SET3**, timed. Mark, patch, then **SET9** a day later, timed.

---

## Marking rules

Mark strictly. A near-miss on a technical term is a lost mark on Sakai, and generous self-marking is the most common way revision produces false confidence.

Tally every error **by chapter**, not by question number. The chapter with the most errors gets the next revision hour. Do not revise chapters you already score well on — it feels productive and buys nothing.

---

## Your four repeat errors

These four were wrong more than once across the three study days. They are flagged in every answer key.

1. The six X.800 services — **Availability** is the one that keeps going missing.
2. The AES modulus — **x⁸ + x⁴ + x³ + x + 1**. Note the x⁴ term, not x², and the trailing 1.
3. **ShiftRows**, not "ShiftCols". And AddRoundKey belongs in the list of four.
4. RSA encrypts and decrypts **mod n**, never mod φ(n). φ(n) appears only in key generation.

If any of these is wrong again, stop reading explanations and write them out by hand until they are automatic. Repeated exposure has not worked; production practice will.

---

## Two things to do off-screen

**Confirm the chapter range.** The course outline states twice that the course is based on Chapters 1–8, and the weekly reading column ends at Chapter 8. You have been told in class it extends to 13. Get that confirmed by a coursemate or the lecturer, because Chapters 11–13 are three extra topics to carry.

**Write the four repeat errors on a single card** and keep it where you will see it. Not in a file, not in this chat. On paper.
