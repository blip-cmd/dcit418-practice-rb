# Security Lab · DCIT 418

Browser exam practice for **Systems and Network Security**, built with React, TypeScript and Vite. Progress stays in your browser; there is no backend or account.

## Run locally

Install dependencies with `npm ci`, then run `npm run dev`.
On Windows PowerShell, use `npm.cmd` if execution policy blocks `npm.ps1`.

`npm start` installs dependencies if needed, builds the app and offline cache, and serves the production build at http://localhost:4173.

## Question bank and study modes

The checked-in bank currently contains 524 questions: 366 from the consolidated quizzes and 158 from the offsite IA. It covers parts 0–13, from data protection and security concepts through encryption, number theory, hashes, MACs and digital signatures. See [PARSER_REPORT.md](PARSER_REPORT.md) for counts by part and question type.

- Practice: filter parts, source banks, question types and difficulty; optionally use only unseen questions.
- Read with answers: navigate questions and explanations without recording scored attempts.
- Fill-in drill: practise the security bank's fill-in questions. No supplemental sets are currently bundled.
- Mock: up to 15 questions per part (203 with the current bank, since Part 2 has only 8 source questions), with a 60-minute deadline. Unseen questions are prioritised; previously seen questions fill remaining places. Answers appear after submission.
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
- `data_files/quiz_bank/quiz.md`
- `data_files/ia_bank/ia_clean.md`

It rewrites `questions.json` and `PARSER_REPORT.md`. Review those changes, then rebuild. Parsing checks structure; it does not independently verify the academic correctness of every source answer.

`data_files/ia_bank/ia_clean.md` is a metadata-stripped copy of `data_files/ia_bank/dcit418_ia_offsite.md`, the original 158-question IA bank kept alongside it with its provider attribution and question-frequency/coverage tables intact. `data_files/quiz_bank/quiz.md` and `data_files/quiz_bank/quiz_bank.md` are identical; only `quiz.md` is read by the parser.

`data_files/study_sets/` (mock exam papers and answer keys, e.g. `SET1_ANSWER_KEY.md`) is not yet parsed into the question bank — TODO for a future pass.

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
