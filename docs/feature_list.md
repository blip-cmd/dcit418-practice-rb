# Exam-practice app: comprehensive feature list

Last reviewed: **16 September 2026**. Code snapshot: **`8be3cb5`** in [blip-cmd/dcit418-practice-rb](https://github.com/blip-cmd/dcit418-practice-rb).

This document describes the app's features, user flows, behavior, and implementation boundaries, using the latest DCIT418 repository as the reference. The same app has been adapted for DCIT408, DCIT402, and DCIT418; those course changes supply context rather than define the feature inventory. Current behavior was checked against source code and bundled data.

## 1. What the app is

Security Lab is a browser-based exam-practice and revision app for **DCIT418: Systems and Network Security**. It supports answering questions, reading answers directly, drilling fill-ins, taking generated timed mocks, reviewing mistakes, inspecting progress, and exporting study material.

The app is a static React/TypeScript application. Its question bank ships with the app. Attempts and preferences stay in the browser. There is no application backend, database server, login, account system, or automatic cross-device synchronization.

The current working study loop is:

1. Choose course parts and source banks, then practise or read with answers.
2. Use fill-in drills for precise recall and review mode for previous mistakes.
3. Take a generated 60-question, 60-minute mock.
4. Review results and export mistakes or filtered question decks.
5. Optionally open the separate Set 9 written simulation and mark it with its supplied key.

## 2. How the feature set grew

The app began as a local exam-practice tool for a supplied question bank: parse the questions and answer keys, preserve their formatting, let students practise, and save progress without accounts or a backend. It was subsequently adapted from DCIT408 to DCIT402 and then DCIT418. The reusable study features are the focus here; course names, banks and sampling quotas are configuration/content details.

The main stages of feature development were:

| Stage | Features added or developed | Student benefit |
|---|---|---|
| Question-bank foundation | Structured question records, source references, answer keys, explanations, validation and grading. | Turn source material into answerable, traceable questions. |
| Interactive practice | Responsive question cards, shuffled options, immediate feedback, answer timing and saved drafts. | Practise in short sessions and resume after reload. |
| Exam and progress tools | Timed mocks, delayed answers, results, mistake review, dashboard and mock history. | Rehearse a paper and use past performance to direct revision. |
| Local portability | Progress import/export, error CSV, production offline caching and one-command startup. | Study locally, back up progress and transfer it manually. |
| Faster revision | Read with answers, arrow navigation, sequential order, collapsible sidebar and appearance settings. | Switch between recall practice and direct reading with less navigation. |
| Continued learning | Reuse seen questions when fresh mock pools run out; dedicated fill-in drills and supplemental multi-blank support. | Keep studying after the first pass through the bank. |
| Focused content selection | Source-bank selection, filters, normalized-text Only unseen behavior and source explanations. | Narrow a session to relevant material and avoid previously exposed stems. |
| Shareable study material | Filtered Markdown, CSV and print/PDF deck exports, with controls collapsed by default. | Take selected questions and answers outside the app. |
| Fixed paper revision | Separate study documents and the integrated Set 9 paper/answer-key viewer. | Work through a written simulation and self-mark it. |

This progression is supported by the repositories' Git histories. It describes accumulated capabilities; the sections below distinguish implemented behavior from data-dependent features and remaining limits.

## 3. User-facing feature inventory

### 3.1 Overview and navigation

- Course-branded overview with entry points for practice, generated mock exams, mistake review, and progress.
- Summary cards show question-bank size, overall accuracy, remaining unseen IDs, and median answer time.
- Sidebar destinations include Overview, Practice, Read with answers, Mock exam, Review mistakes, Your progress, and Appearance.
- Collapse/expand sidebar button; preference persists locally. On first use, mobile-sized screens default to collapsed.
- Local-save, offline/network, cache-readiness, and storage-error messages.
- Progress import/export controls in the sidebar; storage recovery export when saved data cannot be read.

### 3.2 Practice setup and filters

- Select multiple course parts; select/unselect all parts.
- Choose source banks independently: consolidated Quizzes 1–5 and/or Offsite IA.
- Core / Variants / All scope controls remain available. All current records are core, so Variants alone has no matching content.
- Choose random or sequential **question order**. Sequential order does not imply alphabetical/original answer-option order.
- Filter by source-origin/`week`, level, and question type.
- **Only unseen** filters out previously exposed question text and duplicate text within the candidate list. It uses seen IDs plus recorded attempt IDs, normalized through `questionKey`.
- Text normalization lowercases and replaces non-alphanumeric runs with spaces. It catches case/punctuation differences, not semantic paraphrases.
- No-match messages prevent starting an empty session.
- Starting another scored session is disabled while a session is active; resume/end/submit the existing session first.

### 3.3 Answering a practice question

- One question per screen, with ID, part, source-origin, level and type tags.
- Untimed practice, with per-question elapsed time recorded.
- Select an MCQ/True-False option, select all applicable answers for `multi`, or type a fill-in answer.
- Answers and explanations are hidden until an answer is submitted.
- After submission: correctness, expected answer, explanation, source, trap text and working when available; checking notes are behind a disclosure.
- Next question and end-session controls; ending retains already recorded attempts.
- Drafts and the active session are persisted. Reload returns to the active scored session.
- Navigating without submission preserves the draft and records exposure, but does not add a scored attempt.

### 3.4 Answer identity and grading

| Type | Rule |
|---|---|
| Single-choice MCQ / True-False | Compare selected original option index to `correctIndex`, regardless of displayed position. |
| Multi-answer | Selected indices must match the complete correct set; no partial credit. |
| Ordinary fill-in | Case-insensitive, outer-whitespace-trimmed match against `correctText` and `acceptedAnswers`. |
| Supplemental multi-blank schema | Match ordered answers, separated by semicolons or commas, against each blank's accepted alternatives. Supports the inherited notation normalization. No such supplemental records are bundled now. |

Options shuffle when sessions are created; they remain stable through typing and timer updates. Revisited unanswered questions can reshuffle in random-order mode. The app expands combination references such as “A and B” into statement text so shuffling does not change their meaning.

Fill-in mismatches offer **I was right, override** and **I was wrong**. An override changes the attempt to correct and sets `override: true`. It is not a mathematical or semantic equivalence engine. Current ordinary fill-ins carry no parser-generated alternative list; the model supports alternatives if data supplies them.

### 3.5 Read with answers

- Show the question, correct answer and explanation immediately, without a quiz submission step.
- Show all options under a disclosure; include accepted alternatives, source, traps, working and checking notes where present.
- Previous/Next buttons and left/right keys; navigation stays within the available list.
- Mark displayed questions as seen; create no scored attempts and do not alter accuracy.
- Sidebar reading honors selected source banks. **Read instead** in Practice also applies the selected filters and Only unseen.
- **Read fill-ins** applies the fill-in pool and relevant filters.
- Direct reading is blocked during an unsubmitted generated mock.
- Reader position is component state, not a persisted scored session; reload does not restore a reading-only cursor.

### 3.6 Fill-in drill

- Dedicated Practice panel, with a fill-in-set selector, **Start fill-in drill**, and **Read fill-ins**.
- Current selectable content is the main bank's **53 fill-in questions**, subject to selected source/part/origin/level/unseen filters.
- Drill mode bypasses core/variant scope restriction and uses fill questions; starting it sets the UI type to `fill` and scope to `all`.
- Free text, immediate explanation, elapsed time, ordinary practice scoring, manual override, saved drafts and review integration.
- The selector can expose named supplemental sets and an All option if supplemental content is supplied in future; those options are currently absent because the supplemental JSON is empty.

### 3.7 Generated mock exam

The current generated mock is **60 questions in 60 minutes**:

- Four guaranteed questions from each of Parts 0–13: **56 questions**.
- Four additional random questions from the remaining bank: **60 total**.
- Fresh IDs are selected before seen IDs, both within each part and for the additional random places.
- Reuse keeps mocks available even after the whole bank has been seen.
- No duplicate question IDs within one generated paper.
- Quotas are capped by available records if a future part is smaller; the total is derived from available data rather than assumed universally constant.
- Mock construction uses the complete main bank, independently of Practice filters/source selection. Supplemental records are excluded by the model's `bank` boundary.
- The paper and each question have timers. The saved absolute deadline continues while away or after reload; an expired paper is submitted when the app runs again.
- Numbered paper navigation, answered counts, revisitable drafts, Save & next, and explicit Submit paper.
- Explanations and grading remain hidden until the whole paper is submitted; blanks count as incorrect.
- Submission produces one attempt per question, marks the full revealed paper seen, and is idempotent for the same completed session.

Freshness here is **ID-based**. The stricter normalized-text filtering used by Only unseen in Practice is a separate mechanism. The current 524 bodies are distinct under that text normalization, but the mechanisms should not be described as interchangeable.

### 3.8 Generated-mock results and history

- Immediate results: total correct/total questions, percentage, scores by all 14 parts using the actual sampled denominators, and expandable question-level feedback.
- Missed questions show their topic/source and the submitted answer; fill-in results retain override support.
- A history section groups mock attempts by session, dates them, and retains total scores and missed-question lists.
- **Known inherited limitation:** `src/MockHistory.tsx` still renders only Parts 1–6 with `/10` denominators. The immediate results component is dynamic and correct for the current distribution, but the historical per-part cards need migration. Do not use those cards as authoritative DCIT418 per-part scores.

### 3.9 Set 9 fixed written simulation

- Separate buttons on the Mock setup page open the fixed paper or its answer key.
- The paper is presented as a **60-minute, 100-mark, Chapters 1–13** written simulation.
- The actual file contains 30 MCQs, eight numbered fill-in items totaling 25 blanks/marks, and seven essay prompts with selection instructions. Read the file's section instructions for what to attempt.
- Confirmation text encourages taking it last; the first-open date is saved, and reopening shows a reminder.
- Answer-key access has its own confirmation. A paper view also offers “I've finished — reveal answer key.”
- This is a Markdown document viewer with self-marking, **not** an automatically timed, scored or locked generated mock. The viewer does not create question attempts, score essays, enforce first-use-only access, or prohibit scrolling back.
- Claims about exam format/coverage in the study files are supplied study guidance, not independently verified examination guarantees.

### 3.10 Review mistakes

- Includes IDs from previous incorrect attempts.
- Sorts by number of misses descending, then latest miss descending.
- Uses normal practice answering, explanations, timing and persistence.
- A later correct attempt does not erase prior misses. Overriding a particular miss removes that attempt's contribution to the miss count.
- Displays an empty-state/no-matching-questions message when there are no eligible mistakes.

### 3.11 Progress dashboard

- Overall accuracy over recorded attempts, correct-answer count, total attempts, median seconds and manual-override count.
- Breakdowns by part, `week`/source assessment, level and type.
- Flags parts below 70% accuracy and question types whose median time exceeds 60 seconds.
- True median calculation, including averaging the middle pair for even-sized samples.
- Latest 20 attempts with question ID, mode, timestamp, correctness/override status and seconds.
- Mock-history totals and missed topics, subject to the inherited card limitation above.
- Reading exposure affects seen counts but never contributes an accuracy denominator. Submitted blank mock answers do contribute incorrect attempts.
- Time is elapsed wall-clock time accumulated while a question is current, not a measure of verified active attention.

### 3.12 Exports and import

| Action | Output / behavior | Scope |
|---|---|---|
| Export progress | `dcit418-progress.json` | Attempts, seen IDs and active scored session; course marker and schema version included. |
| Import progress | Validate and merge JSON | Merges seen IDs and deduplicates attempts by attempt ID; restores an imported active session. A conflicting different active session must be ended/submitted first. |
| Copy & download error log | `dcit418-errors.csv` plus clipboard when available | All incorrect attempts and the explanation/rule to revise. Download still works when clipboard access fails. |
| Export deck: Markdown | `dcit418-deck.md` | Filtered questions/options, collapsible answer blocks, explanations and sources. |
| Export deck: CSV | `dcit418-deck.csv` | `id`, `part`, `type`, `question`, `options`, `correct_answer`, `explanation`, `source`. |
| Export deck: PDF | Browser print dialog | Opens an HTML print view; the user chooses Save as PDF. No PDF-generation service. Pop-ups must be allowed. |

Deck export lives in a **collapsed-by-default disclosure** in Practice. It honors part, source, scope, origin, level, type and Only unseen filters; its count is previewed. Exporting a deck does not itself mark questions seen or record attempts. Every deck format includes answers: there is no separate question-only export setting.

The error CSV columns are: Question ID, Part, Week, Topic source, What I answered, Correct answer, The rule that fixes it. That exporter escapes CSV and guards formula-leading cells. The newer deck CSV uses its own quoting helper and does **not** have the same formula-prefix guard. The printable deck escapes text but does not run the in-app GFM renderer, so it should not be described as preserving full Markdown/table/diagram fidelity.

### 3.13 Keyboard, rendering and appearance

| Control | Behavior |
|---|---|
| `1`–`5` | Select an option; toggle a choice for multi-answer questions. |
| `Enter` | Submit/save the answer, then advance after feedback; focused native controls retain their own action where excluded by the handler. |
| `Space` | Check/reveal in practice/review; disabled as reveal during mocks and retained as ordinary text entry inside fields. |
| `←` / `→` | Navigate questions without grading; text fields/selects/content-editable regions and code blocks are excluded from navigation interception. |
| `Tab` and button activation | Reach and activate normal interface controls. |

- Markdown rendering through `react-markdown` with GFM tables.
- Fenced code uses monospace text with whitespace preservation and horizontal scrolling instead of wrapping.
- Responsive desktop/mobile layouts, scrollable tables, numbered option controls and visible focus styles.
- Appearance presets: **Sage, Dark, Ocean, Sunset**, plus custom accent color.
- Four size settings (`sm`, `md`, `lg`, `xl`) scale the interface by **0.9 / 1 / 1.15 / 1.3**.
- Theme, custom accent, size and sidebar preference persist in DCIT418-specific browser keys.

## 4. Current question content

Source: [`questions.json`](../questions.json), independently counted during this documentation pass and consistent with [`PARSER_REPORT.md`](../PARSER_REPORT.md).

| Metric | Current value |
|---|---:|
| Main bank records | 524 |
| Distinct question bodies under the app's normalized-text key | 524 |
| Consolidated quiz bank (`quizbank`) | 366 |
| Offsite IA bank (`iabank`) | 158 |
| Four-option MCQs | 401 |
| Five-option MCQs | 0 currently bundled; supported by the model |
| Multi-answer questions | 17 |
| Fill-in questions | 53 |
| True/False questions | 53 |
| Supplemental drill records | 0 (`supplemental/drills.json` is `[]`) |
| Core questions | 524 |
| Variant questions | 0 |
| Distinct cognitive-level labels | 1: `Recall` |

### 4.1 Course parts

| Part | Subject | Questions |
|---:|---|---:|
| 0 | Data Protection & IT Security Policy | 91 |
| 1 | Overview & Computer Security Concepts | 167 |
| 2 | Classical Encryption Techniques | 11 |
| 3 | Block Ciphers & the Data Encryption Standard | 19 |
| 4 | Number Theory & Finite Fields | 10 |
| 5 | Advanced Encryption Standard | 35 |
| 6 | Block Cipher Operation | 20 |
| 7 | Pseudorandom Number Generation & Stream Ciphers | 32 |
| 8 | More Number Theory: Primes & Primality | 18 |
| 9 | Public-Key Cryptography & RSA | 31 |
| 10 | Other Public-Key Cryptosystems | 23 |
| 11 | Cryptographic Hash Functions | 16 |
| 12 | Message Authentication Codes | 18 |
| 13 | Digital Signatures | 33 |

The schema field called `week` currently identifies the source assessment: **Quiz 1 (99), Quiz 2 (35), Quiz 3 (75), Quiz 4 (68), Quiz 5 (89), or IA Offsite (158)**. It is not a verified teaching-week mapping. Likewise, `Recall` is a uniform parser-assigned label, not a differentiated difficulty assessment.

### 4.2 Material present separately from the scored bank

- `data_files/study_sets/` contains Sets 1, 2, 2B, 3–9 and available answer keys: factual knowledge, reasoning, why-questions, exam papers, MCQs, fill-ins, essays, confusion pairs, and tools/labs.
- **Set 9 is wired into the UI as a Markdown paper/key viewer**, via raw imports in `src/main.tsx`.
- Other study-set files are repository resources, not selectable scored banks. In particular, the Set 5 fill-in document is not yet part of the 53-question drill.
- `data_files/dcit418_fill_ins_cheatsheet.md` and chapter/source mapping documents provide additional repository study material.
- The DCIT408 `revision_set`/`final_set` content is historical. It is not bundled as Security Lab supplemental content.

## 5. Persistence, offline use and deployment

Source: [`src/model.ts`](../src/model.ts), [`src/main.tsx`](../src/main.tsx), [`scripts/cache.mjs`](../scripts/cache.mjs), [`vercel.json`](../vercel.json).

### Stored state

- Main storage key: `dcit418-progress-v1`.
- Progress format: `course: "dcit418"`, `version: 1`, `attempts`, `seen`, `session`.
- Attempt fields: ID, session ID, question ID, answer, correctness, seconds, mode, timestamp and override flag.
- Session fields: ID, mode, question IDs, cursor, shuffled option orders, drafts, start/visit times, deadline, submitted status.
- Drafts preserve answer text, single/multiple selections and elapsed seconds.
- Separate keys: `dcit418-sidebar-collapsed`, `dcit418-theme`, `dcit418-custom-accent`, `dcit418-font-size`, `dcit418-set9-opened`.
- Import requires the course marker so overlapping IDs from DCIT402 cannot silently become security answers. Legacy markerless local DCIT418 progress remains readable; re-export it before transferring.
- Unknown IDs, malformed attempt fields, invalid option orders and invalid mock structures are rejected.

There is no automatic device sync. Transfer uses export/import. Filters, question-order choices, export-format choice and reader position are runtime UI state rather than part of the progress backup. Clearing browser data removes local history. Concurrent tabs/devices do not have a conflict-resolution service.

### Offline cache

- Production build generates a service worker and precaches `index.html` plus the built asset files, including the bundled bank and imported Set 9 documents.
- Cache names contain a build-content hash and the `dcit418-security-lab-` prefix.
- Activation cleans older matching Security Lab caches and inherited Management/Compiler Lab cache prefixes on the same origin.
- Same-origin GET requests use cache-first lookup; navigation has an offline index fallback. No arbitrary external downloads or all repository Markdown files are automatically cached.
- Offline caching requires an initial successful visit and HTTPS or localhost. Development mode does not register the production service worker.
- Clearing site storage/cache requires another online visit. A browser that disallows caching can still run the online app.

### Local commands and static hosting

| Command | Purpose |
|---|---|
| `npm ci` | Install pinned dependencies. |
| `npm run dev` | Vite development server exposed on the host network. |
| `npm start` | Install dependencies if missing, build, generate offline cache and preview on port 4173. |
| `npm run build` | Strict TypeScript check, Vite production bundle, service-worker generation. |
| `npm run preview` | Serve `dist/` locally. |
| `npm run build:bank` | Run the security-bank parser; rewrites the bank/report/maps. |

PowerShell may need `npm.cmd`. Hosting consumes `dist/`; the checked-in JSON means normal deployment does not need Python or source files outside the repository. `vercel.json` configures Vite, SPA routing, revalidation of `sw.js` and immutable caching for hashed assets. This configuration is implementation evidence, not proof of a currently working public deployment.

## 6. Content ingestion and maintenance

The main pipeline is [`scripts/parse_security_bank.py`](../scripts/parse_security_bank.py):

1. Read `data_files/quiz_bank/quiz_clean.md` and `data_files/ia_bank/ia_clean.md`.
2. Extract numbered question headings, options, correct-answer fields, intuition/reason text, and quiz-section origin.
3. Detect single-choice, True/False, multi-answer and no-option fill-in questions.
4. Classify course parts using keyword rules over question/reason text; use Part 1 as the fallback.
5. Deduplicate by the first 80 characters of normalized question text. Prefer IA over quiz records when they collide, then longer explanations within equal source priority.
6. Sort and assign `P{part}-Q{number}` IDs.
7. Write `questions.json`, `PARSER_REPORT.md` and per-source question-to-chapter maps.

The originals are preserved beside clean sources. `compile_quiz_bank.py` is a separate preprocessing utility for consolidating quiz sources. The inherited management parser remains in the repository but is disabled as the current entry point; it must not be used to rebuild Security Lab data.

Important maintenance implications:

- The current parser is not the original DCIT408 “exactly 339 or fail” parser. Unsupported/malformed blocks may be skipped and missing source files produce warnings; a PASS report does not independently prove no source questions were lost.
- Prefix-based deduplication may conflate distinct stems with a shared opening. Keyword part classification is a heuristic, not academic validation.
- Reassigning IDs after changing classification/content can change their meaning. Saved progress references IDs, so bank changes require compatibility review.
- Source-key agreement does not establish that a supplied academic answer is correct. Current `checkMethod` text refers to the source key, not independent textbook checking.
- Preserve multiline Markdown when adding future content. The security parser primarily takes question headings as bodies and one-line option matches; the original Compilers parser's broad diagram-preservation guarantees should not be assumed for this different parser.

## 7. Code ownership map

| File / folder | Responsibility |
|---|---|
| `src/main.tsx` | Application shell, filters, practice/mock interactions, timing, imports/exports, dashboard, appearance, Set 9 viewer. |
| `src/model.ts` | Question/session types, grading, shuffle, text-based unseen filtering, mock sampling, review sorting, median, error CSV, import validation. |
| `src/Reader.tsx` | Immediate-answer reader and reading keyboard navigation. |
| `src/MockHistory.tsx` | Historical mock summaries; contains the six-part migration limitation. |
| `src/style.css` | Layout, themes, responsive behavior, typography and Markdown/code styling. |
| `questions.json` | Runtime main-bank data. |
| `supplemental/drills.json` | Optional supplemental-data boundary; empty now. |
| `scripts/parse_security_bank.py` | Current bank parser and chapter classification. |
| `scripts/compile_quiz_bank.py` | Quiz-source consolidation utility. |
| `scripts/start.mjs`, `scripts/cache.mjs` | One-command startup and production offline-cache generation. |
| `data_files/` | Source banks, mapping references, cheatsheet and revision papers. |
| `tests/` | Python parser checks, TypeScript model tests and Playwright browser scenarios. |

## 8. Verification evidence and scope

For this documentation pass, the checked-in JSON was independently counted, Git histories were read, and the relevant implementation was inspected.

Executed on **16 September 2026** in this DCIT418 repository:

- `npm test`: **15 tests passed across three files**.
- `python -m unittest discover -s tests -v`: **5 tests passed**.

Existing automated coverage includes:

- Mock sample size/quotas, reuse after exhaustion, fresh-question preference, grading, combination expansion, idempotent submission, review ranking, medians, course-safe import and CSV escaping.
- Supplemental-schema grading and saved-session behavior, despite no bundled supplemental records.
- Normalized-text unseen filtering and repeated-question exclusion.
- Browser scenarios for practice/reload, fill overrides, mobile cards, generated mocks, expiry, offline reload, progress transfer, dashboard/error export, reading, arrows, sidebar collapse, depleted-bank mocks, fill-in drills and unseen filters.

Browser tests are configured for installed Chrome and a production preview on port 4173. `npm run test:browser` builds first; its server setting can reuse an already running preview, so ensure that preview belongs to this repository when validating multiple course copies.

A fresh production build, full browser suite, physical-phone test, external hosting check, academic answer audit and deck-export fidelity/security audit were **not performed as part of this documentation-only task**. Test definitions describe coverage; they do not establish a passing run today. Existing tests also do not comprehensively validate the new deck exporters, Set 9 workflow or historical score-card migration.

## 9. Current feature limits

| Item | Actual state at this snapshot |
|---|---|
| README mock description | Stale: says up to 15 per part / 203 questions. Code uses 4 guaranteed per each of 14 parts + 4 random = 60. README's Part 2 count of 8 is also stale; JSON contains 11. |
| README study-set description | Too broad: study sets are not parsed into scored bank records, but Set 9 is already available through a document viewer. |
| Historical per-part mock cards | Still Parts 1–6, denominator 10; needs DCIT418 migration. Immediate results use dynamic totals. |
| `revision_set` / `final_set` | Present in the DCIT408 predecessor, absent from the current Security Lab supplemental JSON. |
| Study Sets 1–8 / 2B | Files available for study, not integrated scored sessions. |
| Set 9 timer and marking | User-managed; no automated essay grading or dedicated running timer for the fixed document. |
| Level and variant filtering | Controls exist, but current bank is entirely `Recall` and core. |
| Week reporting | Groups source assessments, not verified teaching weeks. |
| Cross-device continuation | Manual JSON transfer; no accounts/cloud sync. |
| Appearance transfer | Local preferences are separate from progress export. |
| Deck PDF | Browser printing, not a generated PDF download with verified Markdown fidelity. |
| Academic correctness / exam coverage | Source-grounded ingestion, not a guarantee of textbook correctness or future exam coverage. |
| Exam secrecy | Client-side study tool: answers ship in the bundle and exporters can reveal answers. It is not a secure assessment platform. |

## 10. Updating this document

When adding a feature, update its behavior section, the feature-development table and any limits it resolves. Recount `questions.json` when changing banks. Check mock constants, source filters, imports and historical result rendering together when changing course structure. Keep reusable capabilities distinct from the current bank's content and labels. Record the exact verification run rather than carrying forward old pass claims.
