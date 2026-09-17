---
name: writing-standards
description: Use when writing or editing any prose in this DCIT 418 practice app repo, question explanations, README/docs, UI copy, commit messages, code comments. Covers the no-em-dash rule and the explanation-quality bar for question banks. Trigger whenever producing written content for this repo, not just when asked about style directly.
---

# Writing standards for this repo

## No em dashes, anywhere

Never use an em dash (—) in anything written for this repo: prose, UI copy, code comments, generated documentation, commit messages, question explanations. When a sentence would naturally reach for one, rewrite it with a comma, a period, a colon, parentheses, or two separate sentences instead.

This applies retroactively too: if a task requires touching a file that already contains a pre-existing em dash in its own boilerplate (a heading, an intro line you're editing anyway), fix it while you're there. It does not mean bulk-rewriting large bodies of pre-existing verbatim question content (source exam questions, student-contributed explanations already in the bank) purely to hunt down em dashes, that's a separate, much larger task and out of scope unless asked for directly. The line: fix it in anything you are actively authoring or already touching for another reason; don't go looking for it in untouched historical content.

Before finishing any writing task in this repo, grep the files you touched for "—" as a final check.

## Every question needs a real, specific explanation

A question's "Intuition" or "Reason" field must explain *why* the correct answer is correct, in terms specific to that question, not a generic sentence that could apply to any question in the set. This repo has caught and fixed exactly that failure mode twice: a fallback string ("See answer key for detailed reasoning.") used when a source genuinely provided no explanation, and a literal identical placeholder ("Fill-in precision is critical on Sakai exams.") repeated across all 100 questions in one source file. Both were bugs, not acceptable shortcuts.

When a source provides no explanation of its own, write one. Aim for one to three sentences: state the mechanism or definition that makes the answer correct, and where useful, briefly note what makes a specific wrong option tempting or wrong. Match the depth and tone already present in `data_files/ia_bank/ia_clean.md` and `data_files/quiz_bank/quiz_clean.md`, technically precise, no padding, no restating the question back as the explanation.

Before considering a batch of new questions done, grep the relevant `*_clean.md` file (or the built `questions.json`, filtered to that batch) for repeated substrings across many `reason` fields, that's the signature of a generic placeholder that needs replacing.
