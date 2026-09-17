---
name: verify-changes
description: Use after any change to src/model.ts, src/main.tsx, scripts/parse_security_bank.py, questions.json, or any *_clean.md source file in this DCIT 418 practice app, before considering the change done. Also use when asked to "verify", "run the tests", or "make sure nothing broke". Lists the exact commands, what each one actually catches, and known environment gotchas (the encoding trap that hides real bugs, the default python vs. the one with PyMuPDF, why a single browser test run isn't enough after a UI change).
---

# Verifying a change in this repo

A change here is not done until all four of these pass. Skipping any one of them has let a real bug through before in this exact codebase.

## 1. Python parser tests

```sh
python -m unittest discover -s tests -v
```

Covers `scripts/parse_security_bank.py`: part classification, keyword-boundary correctness (a keyword like `"des "` without a leading-space boundary once matched inside the word "modes", silently misclassifying dozens of questions), and `questions.json` structural integrity.

## 2. TypeScript typecheck and vitest

```sh
npx tsc --noEmit
npm test
```

`tsc` alone does not run the app; it only proves the types are internally consistent. `npm test` (vitest) covers `model.ts`'s grading, mock-exam sampling and session logic.

## 3. Production build

```sh
npm run build
```

This runs `tsc --noEmit && vite build && node scripts/cache.mjs`. A clean typecheck does not guarantee a clean build, run this even if step 2 passed.

## 4. Browser end-to-end tests

```sh
npx playwright test
```

Uses installed Chrome (`channel: "chrome"` in `playwright.config.ts`) and a production preview on port 4173. This is the only layer that catches issues the other three cannot: a new field missing from the UI's own `sourceBanks` filter list (content present in `questions.json` but invisible in Practice/Read/Export), a new overlay (like the welcome tour) blocking every other test by covering the page on load, or markdown-rendering differences between what a test asserts and what actually reaches the DOM.

If you add a first-load overlay, a tour, a "what's new" banner, anything gated on a fresh localStorage, add its suppressing flag to the shared `test.beforeEach` in `tests/browser/app.spec.ts` and `unseen.spec.ts`, *and* remember that `page.addInitScript` re-runs on every navigation including `page.reload()`. A script that clears a flag to test "does it show on first visit" will also clear it on the reload that's supposed to prove persistence; use a fresh, independent `browser.newContext()` for that specific test instead of fighting the shared beforeEach.

## Gotchas specific to this machine

- **Terminal display of non-ASCII characters is not proof of file corruption.** A raw byte check (`open(path,'rb').read()` then `.decode('utf-8')`, or `ord()` on the actual character) has repeatedly shown that a "�" printed to this Windows terminal was really a correctly-decoded ×, ', or ≡, just a codepage limitation in the console, not real data corruption. Verify with `ord()`/byte inspection before treating a garbled-looking character as a real bug.
- **The default `python`/`python3` on this machine may not have PyMuPDF.** Check `pip show pymupdf` under a few interpreters (this repo has needed `/c/Users/HP/AppData/Local/Python/pythoncore-3.12-64/python.exe` specifically at times) rather than assuming a PDF-reading script will just work with whatever `python3` resolves to.
- **A question count staying the same after a source-level change isn't automatically a red flag.** Consolidating several small per-contributor batches into `ia_clean.md`/`quiz_clean.md` directly, or fixing a parser bug that changes *which* batch a duplicate is attributed to, can leave the total question count unchanged while still being a real, verifiable improvement, confirm what actually changed (batch counts, classification, explanation text) rather than only checking the top-line total.
