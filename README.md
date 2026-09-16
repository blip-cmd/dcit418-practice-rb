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

The checked-in bank currently contains 799 questions: 366 from the consolidated quizzes, 158 from the offsite IA, 100 from SET5 (fill-ins), 95 from SET4 (MCQ drill, 5 fewer after deduplication), 77 from Desmond's comprehensive exam review, and 3 from Christian's comprehensive exam review (97 of his 100 were duplicates of existing questions). It covers parts 0–13, from data protection and security concepts through encryption, number theory, hashes, MACs and digital signatures. See [PARSER_REPORT.md](PARSER_REPORT.md) for counts by part and question type.

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
- `data_files/ia_bank/chris_clean.md`
- `data_files/ia_bank/desmond_clean.md`

It rewrites `questions.json` and `PARSER_REPORT.md`. Review those changes, then rebuild. Parsing checks structure; it does not independently verify the academic correctness of every source answer.

All six `*_clean.md` files are metadata-stripped copies of the originals, produced so the parser reads plain question/answer/explanation content without attribution or checklists. The originals are kept alongside them: `data_files/ia_bank/dcit418_ia_offsite.md` (158-question IA bank), `data_files/quiz_bank/quiz.md` (366-question quiz bank), `data_files/study_sets/SET4_MCQ_Drill_QUESTIONS.md` + `SET4_MCQ_Drill_ANSWER_KEY.md`, `data_files/study_sets/SET5_FillIns_QUESTIONS.md` + `SET5_FillIns_ANSWER_KEY.md`, `data_files/received qus/Chris/IA.md` (100-question Christian's exam review), and `data_files/received qus/desmond_dcit418_ia.md` (Desmond's exam review, 78 recoverable questions, one lost to a PDF extraction gap). Human-readable review copies with the same content live at `data_files/ia_bank/CHRIS_IA_FORMATTED.md` and `data_files/ia_bank/DESMOND_IA_FORMATTED.md`.

`data_files/study_sets/` contains exam papers and answer keys (e.g. `SET1_ANSWER_KEY.md`), most not yet parsed into the question bank: TODO for a future pass. **SET4 (MCQ Drill)** and **SET5 (Fill-ins)** are now parsed and included. The exception is Set 9, the timed 60-minute simulation, which the app surfaces directly from the Mock exam screen as a one-time paper with its own warning, not through the interactive question bank.

`data_files/received qus/Chris/IA.md` is **Christian's comprehensive exam review** and `data_files/received qus/desmond_dcit418_ia.md` is **Desmond's comprehensive exam review** (both parsed and included as dedicated banks). Chris's Quiz 1-5 files and Emma's files under `received qus/` are not yet parsed; they remain as reference/comparison material.

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
