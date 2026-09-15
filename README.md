# Management Lab · DCIT 402

A local browser exam-practice app for DCIT 402: Principles of Management. HTML entry point, React + strict TypeScript, Vite, Tailwind, and GFM Markdown. No backend, database, login, analytics, or remote fonts.

## Run with one command

Install Node.js 20+ (Node 22/24 tested), then run from this folder:

```sh
npm start
```

On Windows PowerShell, use `npm.cmd start` if execution policy blocks `npm.ps1`.

The command installs locked dependencies on the first run, builds the app and its offline cache, and serves it at **http://localhost:4173**. First installation needs internet. Subsequent starts work offline with installed dependencies. Keep the terminal running during the first visit. Stop with Ctrl+C. `npm run dev` starts the development server; offline caching is tested on the production build served by `npm start`.

## Study modes

- **Read with answers:** click the sidebar button to read the entire bank in source order, or use the button in Practice setup to apply your part/scope/optional filters. Answers, reasons, traps, sources, and working appear immediately. Previous/Next buttons and left/right arrow keys navigate. Reading marks each displayed question as seen for future mock selection, but adds no attempts or scores. Reading is unavailable during an active mock.

- **Fill-in drill:** in Practice setup, click **Start fill-in drill** for fill-in questions in the selected parts/week/level. Free-text answers, immediate explanations, and manual overrides use the existing practice scoring.
- **Practice:** choose multiple parts, Core / Variants / All, and optional week, level, and type filters. Explanations appear after submission. Week ranges participate in each covered week's filter and statistics.
- **Mock:** 60 unique questions, prioritizing unseen ones, exactly 10 per part (across 6 course parts), with a 60-minute deadline and cumulative question timers. Choices and deadline survive reloads. The deadline continues while away; an expired paper submits when reopened. Answers remain hidden until submission. Blanks count as wrong. Once results reveal the paper, all 60 questions count as seen. When a part has fewer than 10 unseen questions, previously seen questions fill its remaining places. There are no duplicates within a paper, even when the entire bank has been seen.
- **Review:** every previously missed question, sorted by miss count descending and most recent miss as the tie-breaker. A later correct response does not remove earlier misses. An overridden attempt counts as correct.
- **Progress:** accuracy by part, week, level, and type; median time; parts below 70%; types above 60 seconds; recent attempts and past mock totals, per-part scores, and missed topics. A multi-week question contributes to each relevant week, but only once to the overall total.

Options use numeric positions and shuffle on each new session and question revisit. They remain stable during typing, selection, and timer updates to prevent moving targets. Correctness follows the original option identity. Combination answers expand letter references into actual statements before shuffling.

Fill-ins compare the trimmed, case-insensitive answer against the primary answer and alternates. Equivalent notation can be marked **I was right, override**; the override is recorded.

Keyboard: **1–5** selects, **Enter** submits and then advances, **Space** checks/reveals in practice/review. Space works normally inside text fields. Tab reaches every action, including mock navigation and submission.

## Offline and other devices

After the header says **offline ready**, the production app and full bank are cached. Progress lives in localStorage on that browser and origin. Clearing browser data removes it, so export a backup regularly.

Use **Export progress** and **Import progress** to transfer history and an active session between browsers/devices. Imports validate data and merge duplicate attempt IDs. An active mock keeps its original deadline. There is no automatic cloud synchronization. Avoid practising concurrently in multiple tabs or independently on two copies of the same active session.

For another device on the same network, use the host computer's reachable network address printed by Vite, with port 4173. Firewall/network settings may need to permit access. Ordinary LAN HTTP supports the app and local progress, but service workers require **HTTPS** (or localhost) for offline caching; the header indicates cache availability. For offline use on a phone, serve the built `dist/` folder from an HTTPS static host.

**Copy & download error log** exports the seven requested CSV columns, with CSV quoting and spreadsheet-formula protection. If browser clipboard permission is unavailable, the download still works.

## Deploy to Vercel

### Option 1: Vercel Web Dashboard (Git Integration)
1. Push this repository to GitHub.
2. In [Vercel](https://vercel.com/), click **Add New...** → **Project** and select your repository.
3. If importing the full repository:
   - Set **Root Directory** to `dcit402-practice` (or leave as root, as a root fallback `vercel.json` is also provided).
   - **Framework Preset**: Vite (automatically detected).
   - **Build Command**: `npm run build`
   - **Output Directory**: `dist`
4. Click **Deploy**.

### Option 2: Vercel CLI
From within the `dcit402-practice` directory, run:
```sh
npx vercel
```
For production release:
```sh
npx vercel --prod
```

Both options automatically apply `vercel.json` header policies for service worker cache revalidation (`sw.js`) and long-term asset caching.

```sh
python scripts/parse_management_bank.py
```

Requires Python 3.10+, no third-party packages. Parses the three source question files from `bd/`:
1. `dcit402-sakai-quiz1.md` (60 questions)
2. `principles-and-practices-of-management-questions-mbamcq.md` (413 questions)
3. `dcit402-it-class-combined-tagged-quiz-bank.md` (191 questions)

Deduplicates identical questions across sources and generates `questions.json` (621 verified questions across 6 parts) along with `PARSER_REPORT.md`. Rebuild the app after regenerating the JSON.

### Course Part Structure

| Part | Title | Questions |
|---|---|---:|
| 1 | Management Foundations | 305 |
| 2 | Planning & Mission | 104 |
| 3 | Organising & Structure | 53 |
| 4 | Leadership | 43 |
| 5 | Motivation, Communication & Control | 92 |
| 6 | Evolution of Management | 24 |
| **Total** | | **621** |

## Verification

```sh
python -m unittest discover -s tests -v
npm test
npm run build
```

Verified on Windows with Node 22/24:
- Parser: 621 matching questions and verified schema across 6 parts.
- App logic: 12 unit tests covering sampling, depleted pools, grading, combinations, duplicate submission, review ranking, import validation, medians, CSV escaping, and supplemental sessions.
- Strict TypeScript and production build pass with offline service worker caching.
