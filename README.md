# Security Lab · DCIT 418

Browser exam practice for **Systems and Network Security**, built with React, TypeScript and Vite. Progress stays in your browser; there is no backend or account.

See [the comprehensive feature list](docs/feature_list.md) for study modes, navigation, grading, progress, exports, offline behavior, feature evolution and current limitations.

## Licence and contributions

Copyright (c) 2026 **Ryan Nii Akwei Brown**, for his original app engine and user-interface/user-experience implementation, in source and compiled form. Study material and questions are excluded; their respective owners retain their rights. Third-party dependencies retain their own licences. See [NOTICE.md](NOTICE.md).

The app uses a custom [source-available licence](LICENSE), not an OSI open-source licence. Independent forks and derivatives require prior written permission. Authorized derivatives must publish their source, retain attribution and notify the owner under the licence terms. GitHub's separate right to copy public repositories through its platform still applies.

To contribute, contact the owner for the **main app repository**, rather than submitting changes to this course-adapted repo. The canonical repository URL and public contact method will be shared later. See [CONTRIBUTING.md](CONTRIBUTING.md).

## Run locally

Install dependencies with `npm ci`, then run `npm run dev`.
On Windows PowerShell, use `npm.cmd` if execution policy blocks `npm.ps1`.

`npm start` installs dependencies if needed, builds the app and offline cache, and serves the production build at http://localhost:4173.

## Question bank and study modes

The checked-in bank currently contains 735 questions: 379 from the consolidated quizzes (including Christian's 38 unique Quiz 1-4 questions), 161 from the IA bank (including Christian's 3 unique exam-review questions), 100 from SET5 (fill-ins), and 95 from SET4 (MCQ drill, 5 fewer after deduplication). It covers parts 0–13, from data protection and security concepts through encryption, number theory, hashes, MACs and digital signatures. See [PARSER_REPORT.md](PARSER_REPORT.md) for counts by part and question type.

Desmond's 77 unique exam-review questions are held out for now pending confirmation that their source (`data_files/received qus/desmond_dcit418_ia.md`) is genuinely IA-source material. See the TODO comment in `data_files/ia_bank/ia_clean.md` above its "Additional Questions" section.

- Practice: filter parts, source banks, question types and difficulty; optionally use only unseen questions.
- Read with answers: navigate questions and explanations without recording scored attempts.
- Fill-in drill: practise the security bank's fill-in questions. No supplemental sets are currently bundled.
- Mock: 4 guaranteed questions per part plus 4 random, 60 questions total, with a 60-minute deadline. Unseen questions are prioritised; previously seen questions fill remaining places. Answers appear after submission.
- Review and progress: revisit mistakes and inspect accuracy and timing.

Options shuffle while preserving the correct answer's identity. Multi-answer questions require all correct choices. Fill-ins support accepted alternatives and a manual correctness override.

## Progress and offline use

Progress and preferences use DCIT418-specific localStorage keys. Export progress for backups or transfer between devices. Imports require a DCIT418 course marker to prevent DCIT402 question IDs from being mistaken for security questions. Existing local DCIT418 progress remains readable; export it again from this version before transferring it.

The production build includes an offline service worker. Visit once while online and wait for offline readiness before disconnecting. HTTPS or localhost is required. Clearing browser data removes local progress and caches. There is no automatic device synchronisation.

## Regenerate the question bank

With Python installed, run:

```sh
npm run build:bank
```

This runs `scripts/parse_security_bank.py` against:
- `data_files/quiz_bank/quiz_clean.md`
- `data_files/ia_bank/ia_clean.md`
- `data_files/study_sets/SET4_clean.md`
- `data_files/study_sets/SET5_clean.md`

It rewrites `questions.json` and `PARSER_REPORT.md`. Review those changes, then rebuild. Parsing checks structure; it does not independently verify the academic correctness of every source answer.

Every `*_clean.md` file is a metadata-stripped copy of its original(s), produced so the parser reads plain question/answer/explanation content without attribution or checklists. `quiz_clean.md` and `ia_clean.md` also carry unique questions from contributor sources appended directly at the end, rather than being parsed as separate per-contributor batches: `quiz_clean.md` includes Christian's unique Quiz 1-4 questions, and `ia_clean.md` includes Christian's and Desmond's unique exam-review questions. The full per-contributor originals are kept for reference (and for re-deriving the merge, via `scripts/convert_chris_ia.py`, `scripts/convert_desmond_ia.py` and `scripts/convert_chris_quiz.py`) at `data_files/ia_bank/dcit418_ia_offsite.md` (the original 158-question IA bank), `data_files/quiz_bank/quiz.md` (the original 366-question quiz bank), `data_files/study_sets/SET4_MCQ_Drill_QUESTIONS.md` + `SET4_MCQ_Drill_ANSWER_KEY.md`, `data_files/study_sets/SET5_FillIns_QUESTIONS.md` + `SET5_FillIns_ANSWER_KEY.md`, `data_files/received qus/Chris/IA.md` and `Quiz 1.md`/`Quiz 2.md`/`Quiz 3.md`/`quiz_4.md`, and `data_files/received qus/desmond_dcit418_ia.md`. Human-readable review copies live at `data_files/ia_bank/CHRIS_IA_FORMATTED.md` and `data_files/ia_bank/DESMOND_IA_FORMATTED.md`.

`data_files/received qus/Chris/quiz_5.md` is excluded entirely: it is a garbled multilingual voice-transcript artifact where the real question text was never captured, only fragments of an AI's spoken-back explanation.

`data_files/study_sets/` contains exam papers and answer keys (e.g. `SET1_ANSWER_KEY.md`), most not yet parsed into the question bank: TODO for a future pass. **SET4 (MCQ Drill)** and **SET5 (Fill-ins)** are now parsed and included. The exception is Set 9, the timed 60-minute simulation, which the app surfaces directly from the Mock exam screen as a one-time paper with its own warning, not through the interactive question bank.

Emma's files under `received qus/` are not yet parsed; they remain as reference/comparison material.

The former management parser is disabled. Deployment uses the checked-in JSON and needs neither Python nor files outside this repository.

## Deploy to Vercel

Import this repository and select the directory containing `package.json` and `vercel.json` as the project root.

- Framework: Vite
- Build command: `npm run build`
- Output directory: `dist`

The existing `vercel.json` supplies SPA routing and cache headers. Commit the app, lockfile and question JSON before redeploying.

## Verification

```sh
python -m unittest discover -s tests -v
npm test
npm run build
npm run test:browser
```

Browser checks use installed Chrome and a production preview on port 4173. They cover practice, mocks, imports, mobile layout, reading, filtering and offline use.
