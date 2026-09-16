import React, { useCallback, useEffect, useRef, useState } from "react";
import { createRoot } from "react-dom/client";
import Markdown from "react-markdown";
import remarkGfm from "remark-gfm";
import {
  practiceBank as bank,
  supplemental,
  byId,
  COURSE_PARTS,
  createSession,
  displayOption,
  emptyProgress,
  errorCsv,
  makeAttempt,
  median,
  mockIds,
  MOCK_PER_PART,
  MOCK_RANDOM_EXTRA,
  mockQuota,
  mockTotalTarget,
  parseProgress,
  reviewIds,
  shuffle,
  STORAGE,
  submitMock,
  weeks,
  questionKey,
  unseenQuestions,
} from "./model";
import type {
  Attempt,
  Draft,
  Mode,
  Progress,
  Question,
  Session,
} from "./model";
import "./style.css";
import { MockHistory } from "./MockHistory";
import { Reader } from "./Reader";
import set9Paper from "../data_files/study_sets/SET9_Timed_Sakai_Simulation.md?raw";
import set9Key from "../data_files/study_sets/SET9_Timed_Sakai_Simulation_ANSWER_KEY.md?raw";

const titles = [
  "Data Protection & IT Security Policy",
  "Overview & Computer Security Concepts",
  "Classical Encryption Techniques",
  "Block Ciphers & the Data Encryption Standard",
  "Number Theory & Finite Fields",
  "Advanced Encryption Standard (AES)",
  "Block Cipher Operation",
  "Pseudorandom Number Generation & Stream Ciphers",
  "More Number Theory (Primes & Primality)",
  "Public-Key Cryptography & RSA",
  "Other Public-Key Cryptosystems",
  "Cryptographic Hash Functions",
  "Message Authentication Codes",
  "Digital Signatures",
];
const sourceBanks = [
  {
    id: "quizbank",
    label: "Consolidated Quiz Bank (Quiz 1-5)",
    file: "data_files/quiz_bank/quiz_clean.md",
  },
  {
    id: "iabank",
    label: "IA Offsite bank",
    file: "data_files/ia_bank/ia_clean.md",
  },
  {
    id: "set4",
    label: "SET4 MCQ Drill",
    file: "data_files/study_sets/SET4_clean.md",
  },
  {
    id: "set5",
    label: "SET5 Fill-ins",
    file: "data_files/study_sets/SET5_clean.md",
  },
  {
    id: "chris",
    label: "Christian's Exam Review",
    file: "data_files/ia_bank/chris_clean.md",
  },
  {
    id: "desmond",
    label: "Desmond's Exam Review",
    file: "data_files/ia_bank/desmond_clean.md",
  },
] as const;
const uniqueQuestionCount = (items: Question[]) =>
  new Set(items.map(questionKey)).size;
const mockTotal = mockTotalTarget();
const md = (text: string) => (
  <Markdown remarkPlugins={[remarkGfm]}>{text}</Markdown>
);
const clock = (seconds: number) =>
  `${Math.floor(seconds / 60)
    .toString()
    .padStart(2, "0")}:${Math.floor(seconds % 60)
    .toString()
    .padStart(2, "0")}`;
function download(name: string, text: string, type: string) {
  const url = URL.createObjectURL(new Blob([text], { type }));
  const a = document.createElement("a");
  a.href = url;
  a.download = name;
  a.click();
  setTimeout(() => URL.revokeObjectURL(url), 1000);
}
const deckAnswer = (q: Question) =>
  q.correctIndex === null ? q.correctText : displayOption(q, q.correctIndex);
function buildDeckMarkdown(questions: Question[]): string {
  const labels = "ABCDE";
  const lines = [
    "# DCIT 418: Systems and Network Security, Exported Question Deck",
    "",
    `${questions.length} questions, exported ${new Date().toLocaleDateString()}.`,
    "",
    "---",
    "",
  ];
  questions.forEach((q, i) => {
    lines.push(`### ${i + 1}. ${q.bodyMarkdown}`);
    q.options.forEach((opt, idx) => lines.push(`- ${labels[idx]}. ${opt}`));
    lines.push("<details>", "<summary>Reveal Answer</summary>", "");
    lines.push(`**Correct Answer:** ${deckAnswer(q)}`);
    if (q.reason) lines.push("", `*Explanation:* ${q.reason}`);
    lines.push("</details>", "", `*Source: ${q.sourceRef}*`, "", "---", "");
  });
  return lines.join("\n");
}
function csvCell(value: string): string {
  return /[",\n]/.test(value) ? `"${value.replace(/"/g, '""')}"` : value;
}
function buildDeckCsv(questions: Question[]): string {
  const header = [
    "id",
    "part",
    "type",
    "question",
    "options",
    "correct_answer",
    "explanation",
    "source",
  ];
  const rows = questions.map((q) =>
    [
      q.id,
      String(q.part),
      q.type,
      q.bodyMarkdown,
      q.options.join(" | "),
      deckAnswer(q),
      q.reason,
      q.sourceRef,
    ]
      .map(csvCell)
      .join(","),
  );
  return [header.join(","), ...rows].join("\n");
}
function buildDeckHtml(questions: Question[], title: string): string {
  const labels = "ABCDE";
  const esc = (s: string) =>
    s
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;");
  const body = questions
    .map((q, i) => {
      const options = q.options.length
        ? `<ul>${q.options
            .map((o, idx) => `<li>${labels[idx]}. ${esc(o)}</li>`)
            .join("")}</ul>`
        : "";
      return `<div class="q"><h3>${i + 1}. ${esc(q.bodyMarkdown)}</h3>${options}<p><strong>Answer:</strong> ${esc(
        deckAnswer(q),
      )}</p>${
        q.reason
          ? `<p class="reason"><strong>Explanation:</strong> ${esc(q.reason)}</p>`
          : ""
      }</div>`;
    })
    .join("\n");
  return `<!doctype html><html><head><meta charset="utf-8"><title>${esc(title)}</title><style>
body{font-family:Georgia,serif;max-width:760px;margin:32px auto;padding:0 16px;color:#1c2a20;}
h1{font-size:20px;} .q{margin-bottom:20px;page-break-inside:avoid;} h3{font-size:14px;margin-bottom:6px;}
ul{margin:4px 0 8px 20px;padding:0;} li{margin:2px 0;} .reason{color:#445;font-size:13px;}
@media print{body{margin:0;}}
</style></head><body><h1>${esc(title)}</h1><p>${questions.length} questions</p><hr/>${body}</body></html>`;
}
function printDeckPdf(questions: Question[], title: string) {
  const w = window.open("", "_blank");
  if (!w) return false;
  w.document.write(buildDeckHtml(questions, title));
  w.document.close();
  w.focus();
  setTimeout(() => w.print(), 300);
  return true;
}
function load(): Progress {
  const text = localStorage.getItem(STORAGE);
  return text ? parseProgress(text) : emptyProgress();
}

function App() {
  const [sidebarCollapsed, setSidebarCollapsed] = useState(() => {
    try {
      const saved = localStorage.getItem("dcit418-sidebar-collapsed");
      return saved === null
        ? window.matchMedia("(max-width: 760px)").matches
        : saved === "true";
    } catch {
      return false;
    }
  });
  function toggleSidebar() {
    const collapsed = !sidebarCollapsed;
    setSidebarCollapsed(collapsed);
    try {
      localStorage.setItem("dcit418-sidebar-collapsed", String(collapsed));
    } catch {
      /* Keep the toggle usable without browser storage. */
    }
  }
  const [theme, setTheme] = useState<
    "default" | "dark" | "ocean" | "sunset" | "custom"
  >(() => {
    try {
      return (localStorage.getItem("dcit418-theme") as never) || "default";
    } catch {
      return "default";
    }
  });
  const [customAccent, setCustomAccent] = useState(() => {
    try {
      return localStorage.getItem("dcit418-custom-accent") || "#214d3c";
    } catch {
      return "#214d3c";
    }
  });
  const [fontSize, setFontSize] = useState<"sm" | "md" | "lg" | "xl">(() => {
    try {
      return (localStorage.getItem("dcit418-font-size") as never) || "md";
    } catch {
      return "md";
    }
  });
  function applyTheme(next: typeof theme) {
    setTheme(next);
    try {
      localStorage.setItem("dcit418-theme", next);
    } catch {
      /* Keep the picker usable without browser storage. */
    }
  }
  // Mirrored onto <html> so the page background outside .shell - the overscroll
  // area and any gap below short pages - uses the same palette.
  useEffect(() => {
    const root = document.documentElement;
    root.dataset.theme = theme === "custom" ? "default" : theme;
    root.style.colorScheme = theme === "dark" ? "dark" : "light";
  }, [theme]);
  function applyCustomAccent(hex: string) {
    setCustomAccent(hex);
    try {
      localStorage.setItem("dcit418-custom-accent", hex);
    } catch {
      /* Keep the picker usable without browser storage. */
    }
  }
  function applyFontSize(next: typeof fontSize) {
    setFontSize(next);
    try {
      localStorage.setItem("dcit418-font-size", next);
    } catch {
      /* Keep the picker usable without browser storage. */
    }
  }
  const zoomBySize = { sm: 0.9, md: 1, lg: 1.15, xl: 1.3 }[fontSize];
  const [message, setMessage] = useState("");
  const [progress, setProgress] = useState<Progress>(() => {
    try {
      return load();
    } catch {
      return emptyProgress();
    }
  });
  const [storageError, setStorageError] = useState(() => {
    try {
      load();
      return "";
    } catch {
      return "Saved progress could not be read. Export a backup before making changes; your old browser data has been retained.";
    }
  });
  const [view, setView] = useState<
    "home" | "practice" | "mock" | "review" | "dashboard" | "read" | "settings"
  >(progress.session ? progress.session.mode : "home");
  const [parts, setParts] = useState([...COURSE_PARTS]);
  const [scope, setScope] = useState("core");
  const [order, setOrder] = useState<"random" | "sequential">("random");
  const [week, setWeek] = useState("");
  const [level, setLevel] = useState("");
  const [type, setType] = useState("");
  const [onlyUnseen, setOnlyUnseen] = useState(false);
  const filterUnseen = (items: Question[]) =>
    onlyUnseen
      ? unseenQuestions(items, [...progress.seen, ...progress.attempts.map((a) => a.questionId)])
      : items;
  const [selectedSources, setSelectedSources] = useState<string[]>(
    sourceBanks.map((source) => source.id),
  );
  const [drillSet, setDrillSet] = useState("original");
  const [exportFormat, setExportFormat] = useState<"markdown" | "csv" | "pdf">(
    "markdown",
  );
  const [readingIds, setReadingIds] = useState(bank.map((q) => q.id));
  const [set9View, setSet9View] = useState<null | "paper" | "key">(null);
  const [set9OpenedAt, setSet9OpenedAt] = useState(() => {
    try {
      return localStorage.getItem("dcit418-set9-opened");
    } catch {
      return null;
    }
  });
  function openSet9Paper() {
    const warning = set9OpenedAt
      ? `You already opened Set 9 on ${new Date(set9OpenedAt).toLocaleDateString()}. Its value comes entirely from being the first time you see it. Retaking it won't tell you anything new. Open it again anyway?`
      : "Set 9 is the timed 60-minute simulation across all 13 chapters, the true mock for this course. Do this ONCE, and do it last, after everything else. Phone away, timer running, no notes, no scrolling back. Continue?";
    if (!window.confirm(warning)) return;
    if (!set9OpenedAt) {
      const now = new Date().toISOString();
      try {
        localStorage.setItem("dcit418-set9-opened", now);
      } catch {
        /* Still let them take it without the persisted flag. */
      }
      setSet9OpenedAt(now);
    }
    setSet9View("paper");
  }
  function openSet9Key() {
    if (
      !window.confirm(
        "Only open the answer key after you've stopped the timer and finished the paper honestly. Continue?",
      )
    )
      return;
    setSet9View("key");
  }
  const sourceSelected = (q: Question) =>
    selectedSources.includes(q.batch) ||
    (!!q.setName && !sourceBanks.some((source) => source.id === q.batch));
  const toggleSource = (id: string) =>
    setSelectedSources((sources) =>
      sources.includes(id)
        ? sources.filter((source) => source !== id)
        : [...sources, id],
    );
  const markRead = useCallback((id: string) => {
    setProgress((p) =>
      p.seen.includes(id) ? p : { ...p, seen: [...p.seen, id] },
    );
  }, []);
  function drillPool() {
    return bank.filter((q) => q.type === "fill" &&
      (drillSet === "all" || (drillSet === "original" ? !q.setName : q.setName === drillSet)));
  }
  function startReading(filtered = false, fillDrill = false) {
    if (progress.session?.mode === "mock" && !progress.session.submitted) {
      setMessage("Submit your active mock before opening answers.");
      return;
    }
    const candidates = (fillDrill ? drillPool() : bank)
      .filter(
        (q) =>
          // Unfiltered reading still honours the chosen source banks, so the
          // reader never shows questions from a bank you switched off.
          sourceSelected(q) &&
          (!filtered ||
            (parts.includes(q.part) &&
              (fillDrill || scope === "all" || (scope === "core" ? q.isCore : !q.isCore)) &&
              (!week || weeks(q).includes(week)) &&
              (!level || q.level === level) &&
              (fillDrill || !type || q.type === type))),
      );
    const ids = (filtered ? filterUnseen(candidates) : candidates).map((q) => q.id);
    if (!ids.length) {
      setMessage("No questions match. Adjust your filters.");
      return;
    }
    setReadingIds(ids);
    setView("read");
    setMessage("");
  }
  function exportCandidates(): Question[] {
    const candidates = bank.filter(
      (q) =>
        sourceSelected(q) &&
        parts.includes(q.part) &&
        (scope === "all" || (scope === "core" ? q.isCore : !q.isCore)) &&
        (!week || weeks(q).includes(week)) &&
        (!level || q.level === level) &&
        (!type || q.type === type),
    );
    return filterUnseen(candidates);
  }
  function downloadDeck() {
    const questions = exportCandidates();
    if (!questions.length) {
      setMessage("No questions match your filters. Adjust and try again.");
      return;
    }
    const title = "DCIT 418 Exported Question Deck";
    if (exportFormat === "markdown") {
      download(
        "dcit418-deck.md",
        buildDeckMarkdown(questions),
        "text/markdown;charset=utf-8",
      );
    } else if (exportFormat === "csv") {
      download(
        "dcit418-deck.csv",
        buildDeckCsv(questions),
        "text/csv;charset=utf-8",
      );
    } else if (!printDeckPdf(questions, title)) {
      setMessage("Allow pop-ups to export as PDF, then try again.");
      return;
    }
    setMessage(`Deck exported: ${questions.length} questions.`);
  }
  const [now, setNow] = useState(Date.now());
  const [offline, setOffline] = useState(!navigator.onLine);
  const [cacheReady, setCacheReady] = useState(false);
  useEffect(() => {
    if ("serviceWorker" in navigator)
      void navigator.serviceWorker.ready.then(() => setCacheReady(true));
  }, []);
  const file = useRef<HTMLInputElement>(null);
  const current = useRef(progress);
  current.current = progress;
  const session = progress.session;
  const active = session && view === session.mode ? session : null;
  const q = active ? byId.get(active.ids[active.index])! : null;
  const attempt =
    active && q
      ? progress.attempts.find((a) => a.id === `${active.id}:${q.id}`)
      : undefined;
  const draft =
    q && active
      ? (active.drafts[q.id] ?? { answer: "", selected: null, seconds: 0 })
      : null;
  useEffect(() => {
    if (storageError) return;
    try {
      localStorage.setItem(STORAGE, JSON.stringify(progress));
    } catch {
      setStorageError(
        "Browser storage is full or unavailable. Export your progress now to keep a backup.",
      );
    }
  }, [progress, storageError]);
  useEffect(() => {
    const timer = setInterval(() => setNow(Date.now()), 250);
    const on = () => setOffline(!navigator.onLine);
    window.addEventListener("online", on);
    window.addEventListener("offline", on);
    return () => {
      clearInterval(timer);
      window.removeEventListener("online", on);
      window.removeEventListener("offline", on);
    };
  }, []);
  function stamp(s: Session, at = Date.now()): Session {
    const id = s.ids[s.index];
    const d = s.drafts[id] ?? { answer: "", selected: null, seconds: 0 };
    const end = s.deadline ? Math.min(at, s.deadline) : at;
    return {
      ...s,
      visitedAt: at,
      drafts: {
        ...s.drafts,
        [id]: {
          ...d,
          seconds: d.seconds + Math.max(0, (end - s.visitedAt) / 1000),
        },
      },
    };
  }
  useEffect(() => {
    const s = current.current.session;
    if (s?.mode === "mock" && !s.submitted && s.deadline && now >= s.deadline) {
      setProgress((p) =>
        p.session ? submitMock({ ...p, session: stamp(p.session) }, now) : p,
      );
      setView("mock");
      setMessage("Time is up. Your paper has been submitted.");
    }
  }, [now]);
  function start(mode: Mode, fillDrill = false) {
    try {
      let ids: string[];
      if (mode === "mock") ids = mockIds(progress.seen);
      else if (mode === "review") ids = reviewIds(progress.attempts);
      else {
        const pool = fillDrill ? drillPool() : bank;
        const filtered = pool
          .filter(
            (q) =>
              parts.includes(q.part) &&
              (fillDrill ||
                scope === "all" ||
                (scope === "core" ? q.isCore : !q.isCore)) &&
              sourceSelected(q) &&
              (!week || weeks(q).includes(week)) &&
              (!level || q.level === level) &&
              (fillDrill ? q.type === "fill" : !type || q.type === type),
          );
        const available = filterUnseen(filtered).map((q) => q.id);
        ids = order === "sequential" ? available : shuffle(available);
      }
      if (!ids.length) {
        setMessage(
          "No questions match. Adjust your filters or practise first.",
        );
        return;
      }
      const s = createSession(mode, ids);
      if (fillDrill) {
        setType("fill");
        setScope("all");
      }
      setProgress((p) => ({
        ...p,
        session: s,
        seen: [...new Set([...p.seen, ids[0]])],
      }));
      setView(mode);
      setMessage("");
    } catch (e) {
      setMessage(e instanceof Error ? e.message : "Could not start session.");
    }
  }
  function change(value: Partial<Draft>) {
    if (
      !active ||
      !q ||
      attempt ||
      active.submitted ||
      (active.deadline !== null && Date.now() >= active.deadline)
    )
      return;
    setProgress((p) => {
      const s = p.session!;
      return {
        ...p,
        session: {
          ...s,
          drafts: {
            ...s.drafts,
            [q.id]: {
              ...(s.drafts[q.id] ?? { answer: "", selected: null, seconds: 0 }),
              ...value,
            },
          },
        },
      };
    });
  }
  function move(index: number) {
    if (!active) return;
    if (index >= active.ids.length) {
      setProgress((p) => ({ ...p, session: null }));
      setView("home");
      setMessage("Session complete. Your results are saved.");
      return;
    }
    setProgress((p) => {
      const s = stamp(p.session!);
      const id = s.ids[index];
      const answered = p.attempts.some((a) => a.id === `${s.id}:${id}`);
      return {
        ...p,
        seen: [...new Set([...p.seen, id])],
        session: {
          ...s,
          index,
          orders:
            answered || order === "sequential"
              ? s.orders
              : { ...s.orders, [id]: shuffle(s.orders[id]) },
        },
      };
    });
  }
  function answer() {
    if (
      !active ||
      !q ||
      !draft ||
      attempt ||
      active.submitted ||
      (active.deadline !== null && Date.now() >= active.deadline)
    )
      return;
    if (!draft.answer.trim()) {
      setMessage("Choose an option or enter an answer first.");
      return;
    }
    if (active.mode === "mock") {
      if (active.index < active.ids.length - 1) move(active.index + 1);
      else
        setMessage(
          "You have reached the last question. Submit the paper when ready.",
        );
      return;
    }
    setProgress((p) => {
      const s = stamp(p.session!);
      return {
        ...p,
        session: s,
        attempts: [...p.attempts, makeAttempt(s, q.id)],
      };
    });
    setMessage("");
  }
  function override(a: Attempt) {
    setProgress((p) => ({
      ...p,
      attempts: p.attempts.map((item) =>
        item.id === a.id ? { ...item, correct: true, override: true } : item,
      ),
    }));
  }
  useEffect(() => {
    const handler = (e: KeyboardEvent) => {
      if (
        !active ||
        !q ||
        active.submitted ||
        e.altKey ||
        e.ctrlKey ||
        e.metaKey
      )
        return;
      const target = e.target as HTMLElement;
      const typing = ["INPUT", "TEXTAREA", "SELECT"].includes(target.tagName);
      if (
        !typing &&
        !target.isContentEditable &&
        !target.closest("pre") &&
        (e.key === "ArrowLeft" || e.key === "ArrowRight")
      ) {
        e.preventDefault();
        const index = active.index + (e.key === "ArrowRight" ? 1 : -1);
        if (index >= 0 && index < active.ids.length) move(index);
        return;
      }
      if (!typing && /^[1-5]$/.test(e.key) && !attempt) {
        const original = active.orders[q.id][Number(e.key) - 1];
        if (original !== undefined) {
          e.preventDefault();
          if (q.type === "multi") {
            const picked = (draft?.selectedMulti ?? []).includes(original);
            const next = picked
              ? (draft?.selectedMulti ?? []).filter((v) => v !== original)
              : [...(draft?.selectedMulti ?? []), original];
            change({
              selectedMulti: next,
              answer: next
                .slice()
                .sort((a, b) => a - b)
                .map((idx) => displayOption(q, idx))
                .join(" and "),
            });
          } else {
            change({ selected: original, answer: displayOption(q, original) });
          }
        }
      }
      if (
        e.key === "Enter" &&
        (target.tagName !== "BUTTON" || target.closest(".option")) &&
        target.tagName !== "SELECT"
      ) {
        e.preventDefault();
        if (attempt) move(active.index + 1);
        else answer();
      }
      if (
        e.code === "Space" &&
        !typing &&
        (target.tagName !== "BUTTON" || target.closest(".option")) &&
        active.mode !== "mock"
      ) {
        e.preventDefault();
        answer();
      }
    };
    window.addEventListener("keydown", handler);
    return () => window.removeEventListener("keydown", handler);
  });
  function navigate(v: typeof view) {
    if (v === "read") {
      startReading();
      return;
    }
    setView(v);
    setMessage("");
  }
  async function importFile(f: File) {
    try {
      const imported = parseProgress(await f.text(), { requireCourse: true });
      if (
        progress.session &&
        !progress.session.submitted &&
        imported.session &&
        imported.session.id !== progress.session.id
      )
        throw new Error(
          "End or submit the current session before importing another active session.",
        );
      setProgress((p) => ({
        ...p,
        session: imported.session ?? p.session,
        seen: [...new Set([...p.seen, ...imported.seen])],
        attempts: [
          ...new Map(
            [...p.attempts, ...imported.attempts].map((a) => [a.id, a]),
          ).values(),
        ],
      }));
      setStorageError("");
      if (imported.session) setView(imported.session.mode);
      setMessage(
        "Progress imported, including any active session. Duplicate attempts were merged.",
      );
    } catch (e) {
      setMessage(e instanceof Error ? e.message : "Import failed.");
    }
  }
  async function exportErrors() {
    const csv = errorCsv(progress.attempts);
    download("dcit418-errors.csv", csv, "text/csv;charset=utf-8");
    try {
      await navigator.clipboard.writeText(csv);
      setMessage("Error log downloaded and copied to clipboard.");
    } catch {
      setMessage("CSV downloaded. Clipboard is unavailable in this browser.");
    }
  }
  const accuracy = progress.attempts.length
    ? Math.round(
        (progress.attempts.filter((a) => a.correct).length /
          progress.attempts.length) *
          100,
      )
    : null;
  const unseen = bank.filter((q) => !progress.seen.includes(q.id)).length;
  return (
    <div
      className={`shell ${sidebarCollapsed ? "sidebar-collapsed" : ""}`}
      data-theme={theme === "custom" ? "default" : theme}
      style={{
        // @ts-expect-error custom property
        "--ui-zoom": zoomBySize,
        ...(theme === "custom"
          ? ({
              "--accent": customAccent,
              "--accent-strong": customAccent,
            } as React.CSSProperties)
          : {}),
      }}
    >
      <aside id="study-sidebar" aria-hidden={sidebarCollapsed}>
        <a
          className="brand"
          href="#"
          onClick={(e) => {
            e.preventDefault();
            navigate("home");
          }}
        >
          <span className="brand-icon">
            S<span>_</span>
          </span>
          <span>
            Security Lab<small>DCIT 418 · EXAM PRACTICE</small>
          </span>
        </a>
        <div className="nav-label">YOUR WORKSPACE</div>
        <nav>
          {(
            [
              ["home", "Overview", "◫"],
              ["practice", "Practice", "▷"],
              ["read", "Read with answers", "▤"],
              ["mock", "Mock exam", "◷"],
              ["review", "Review mistakes", "↺"],
              ["dashboard", "Your progress", "▥"],
              ["settings", "Appearance", "◐"],
            ] as const
          ).map(([v, label, icon]) => (
            <button
              key={v}
              className={view === v ? "nav active" : "nav"}
              onClick={() => navigate(v)}
            >
              <span>{icon}</span>
              {label}
              {v === "review" && <em>{reviewIds(progress.attempts).length}</em>}
            </button>
          ))}
        </nav>
        <div className="sidebar-note">
          <span className="dot" />{" "}
          {offline ? "Offline mode" : "Local-first learning"}
          <p>
            Your progress stays in this browser. Export it to continue on
            another device.
          </p>
          <button
            className="text-button"
            onClick={() =>
              download(
                "dcit418-progress.json",
                JSON.stringify(progress, null, 2),
                "application/json",
              )
            }
          >
            Export progress ↗
          </button>
          <button className="text-button" onClick={() => file.current?.click()}>
            Import progress ↙
          </button>
          <input
            hidden
            ref={file}
            type="file"
            accept="application/json,.json"
            onChange={(e) => {
              const f = e.target.files?.[0];
              if (f) void importFile(f);
              e.target.value = "";
            }}
          />
        </div>
        <div className="sidebar-bottom">{uniqueQuestionCount(bank)} questions. One confident you.</div>
      </aside>
      <main>
        <header>
          <button
            className="sidebar-toggle"
            onClick={toggleSidebar}
            aria-controls="study-sidebar"
            aria-expanded={!sidebarCollapsed}
            aria-label={
              sidebarCollapsed ? "Expand sidebar" : "Collapse sidebar"
            }
            title={sidebarCollapsed ? "Expand sidebar" : "Collapse sidebar"}
          >
            <span aria-hidden="true">☰</span>
          </button>
          <span>
            UNIVERSITY OF GHANA <span className="muted">/</span> COMPUTER
            SCIENCE
          </span>
          <span className="status">
            <span className="dot" />{" "}
            {storageError
              ? "Storage needs attention"
              : offline
                ? "Offline"
                : cacheReady
                  ? "Saved locally ? offline ready"
                  : "Saved locally ? offline cache unavailable"}
          </span>
        </header>
        {storageError && (
          <div role="alert" className="notice error">
            {storageError}
            <button
              onClick={() => {
                const old = localStorage.getItem(STORAGE);
                if (old)
                  download("dcit418-recovery.json", old, "application/json");
              }}
            >
              Export stored data
            </button>
          </div>
        )}
        {message && (
          <div role="status" className="notice">
            {message}
            <button aria-label="Dismiss message" onClick={() => setMessage("")}>
              ×
            </button>
          </div>
        )}
        {set9View ? (
          <section className="setup-card">
            <div className="session-title">
              <h1>
                {set9View === "paper"
                  ? "Set 9: Timed Sakai Simulation"
                  : "Set 9: Answer Key"}
              </h1>
              <button className="secondary" onClick={() => setSet9View(null)}>
                Close
              </button>
            </div>
            <div className="markdown">
              {md(set9View === "paper" ? set9Paper : set9Key)}
            </div>
            {set9View === "paper" && (
              <button className="primary" onClick={openSet9Key}>
                I've finished, reveal answer key
              </button>
            )}
          </section>
        ) : view === "read" ? (
          <Reader ids={readingIds} onSeen={markRead} />
        ) : active ? (
          active.submitted && active.mode === "mock" ? (
            <MockResults
              session={active}
              attempts={progress.attempts.filter(
                (a) => a.sessionId === active.id,
              )}
              onOverride={override}
              onClose={() => {
                setProgress((p) => ({ ...p, session: null }));
                navigate("dashboard");
              }}
            />
          ) : (
            q &&
            draft && (
              <>
                <div className="page-heading">
                  <div className="eyebrow">
                    {active.mode.toUpperCase()} SESSION · PART {q.part}
                  </div>
                  <div className="session-title">
                    <h1>{titles[q.part]}</h1>
                    <div className="timer">
                      {active.mode === "mock" && (
                        <strong>
                          {clock(
                            Math.max(
                              0,
                              Math.ceil(
                                ((active.deadline ?? now) - now) / 1000,
                              ),
                            ),
                          )}{" "}
                          <small>remaining</small>
                        </strong>
                      )}
                      <span>
                        {clock(
                          draft.seconds +
                            (attempt
                              ? 0
                              : Math.max(0, (now - active.visitedAt) / 1000)),
                        )}{" "}
                        <small>on question</small>
                      </span>
                    </div>
                  </div>
                </div>
                <div className="question-progress">
                  <span>
                    Question {active.index + 1}{" "}
                    <span className="muted">of {active.ids.length}</span>
                  </span>
                  <span>
                    {active.mode === "mock"
                      ? "Answers stay hidden until submission"
                      : "Take your time. Build your understanding."}
                  </span>
                </div>
                <div className="track">
                  <i
                    style={{
                      width: `${((active.index + 1) / active.ids.length) * 100}%`,
                    }}
                  />
                </div>
                <section className="question-card">
                  <div className="tags">
                    <span>{q.id}</span>
                    <span>{q.week}</span>
                    <span>{q.level}</span>
                    <span>
                      {q.type === "fill"
                        ? "Fill in the blank"
                        : q.type === "tf"
                          ? "True / False"
                          : q.type === "multi"
                            ? "Select all that apply"
                            : "Multiple choice"}
                    </span>
                  </div>
                  <div className="markdown question-body">
                    {md(q.bodyMarkdown)}
                  </div>
                  {q.type === "fill" ? (
                    <label className="fill-label">
                      Your answer
                      {q.answerBlanks && q.answerBlanks.length > 1 && (
                        <span>
                          {" "}
                          · {q.answerBlanks.length} blanks: separate answers
                          with semicolons, in order
                        </span>
                      )}
                      <input
                        autoComplete="off"
                        aria-label="Your answer"
                        value={draft.answer}
                        disabled={!!attempt}
                        onChange={(e) => change({ answer: e.target.value })}
                        placeholder="Type your answer…"
                      />
                    </label>
                  ) : q.type === "multi" ? (
                    <div className="options">
                      {active.orders[q.id].map((original, i) => {
                        const picked = (draft.selectedMulti ?? []).includes(
                          original,
                        );
                        return (
                          <button
                            key={original}
                            disabled={!!attempt}
                            aria-pressed={picked}
                            className={`option ${picked ? "selected" : ""} ${attempt && q.correctIndices?.includes(original) ? "correct-option" : ""}`}
                            onClick={() => {
                              const next = picked
                                ? (draft.selectedMulti ?? []).filter(
                                    (v) => v !== original,
                                  )
                                : [...(draft.selectedMulti ?? []), original];
                              change({
                                selectedMulti: next,
                                answer: next
                                  .slice()
                                  .sort((a, b) => a - b)
                                  .map((idx) => displayOption(q, idx))
                                  .join(" and "),
                              });
                            }}
                          >
                            <span className="option-number">{i + 1}</span>
                            <div className="markdown">
                              {md(displayOption(q, original))}
                            </div>
                            <span className="radio">{picked ? "☑" : "☐"}</span>
                          </button>
                        );
                      })}
                    </div>
                  ) : (
                    <div className="options">
                      {active.orders[q.id].map((original, i) => (
                        <button
                          key={original}
                          disabled={!!attempt}
                          aria-pressed={draft.selected === original}
                          className={`option ${draft.selected === original ? "selected" : ""} ${attempt && original === q.correctIndex ? "correct-option" : ""}`}
                          onClick={() =>
                            change({
                              selected: original,
                              answer: displayOption(q, original),
                            })
                          }
                        >
                          <span className="option-number">{i + 1}</span>
                          <div className="markdown">
                            {md(displayOption(q, original))}
                          </div>
                          <span className="radio">
                            {draft.selected === original ? "●" : ""}
                          </span>
                        </button>
                      ))}
                    </div>
                  )}
                  {attempt && (
                    <Feedback
                      key={attempt.id}
                      q={q}
                      attempt={attempt}
                      onOverride={() => override(attempt)}
                    />
                  )}
                  <div className="question-actions">
                    <span className="key-hint">
                      {q.type !== "fill" && (
                        <>
                          {" "}
                          <kbd>1–5</kbd> select ·{" "}
                        </>
                      )}
                      <kbd>Enter</kbd> {attempt ? "next" : "submit"}
                      {active.mode !== "mock" && (
                        <>
                          {" "}
                          · <kbd>Space</kbd> reveal
                        </>
                      )}
                    </span>
                    <button
                      className="secondary-action prev-question"
                      disabled={active.index === 0}
                      onClick={() => move(active.index - 1)}
                    >
                      ← <span>Previous</span>
                    </button>
                    {attempt ? (
                      <button
                        className="primary"
                        onClick={() => move(active.index + 1)}
                      >
                        {active.index === active.ids.length - 1
                          ? "Finish session"
                          : "Next question"}{" "}
                        →
                      </button>
                    ) : (
                      <button className="primary" onClick={answer}>
                        {active.mode === "mock"
                          ? "Save & next"
                          : "Check answer"}{" "}
                        →
                      </button>
                    )}
                  </div>
                </section>
                {active.mode === "mock" ? (
                  <section className="paper-nav">
                    <h3>
                      Your paper{" "}
                      <span>
                        {
                          Object.values(active.drafts).filter((d) =>
                            d.answer.trim(),
                          ).length
                        }
                        /{active.ids.length} answered
                      </span>
                    </h3>
                    <div>
                      {active.ids.map((id, i) => (
                        <button
                          key={id}
                          aria-label={`Go to question ${i + 1}`}
                          className={`${i === active.index ? "current" : ""} ${active.drafts[id]?.answer ? "answered" : ""}`}
                          onClick={() => move(i)}
                        >
                          {i + 1}
                        </button>
                      ))}
                    </div>
                    <button
                      className="primary"
                      onClick={() => {
                        setProgress((p) =>
                          submitMock({ ...p, session: stamp(p.session!) }),
                        );
                      }}
                    >
                      Submit paper
                    </button>
                    <p>
                      Unanswered questions count as incorrect. Submission ends
                      this paper.
                    </p>
                  </section>
                ) : (
                  <button
                    className="text-button end-session"
                    onClick={() => {
                      setProgress((p) => ({ ...p, session: null }));
                      navigate("home");
                    }}
                  >
                    End session · keep saved answers
                  </button>
                )}
              </>
            )
          )
        ) : view === "home" ? (
          <>
            <div className="page-heading">
              <div className="eyebrow">A LITTLE PRACTICE, EVERY DAY</div>
              <h1>Make the concepts click.</h1>
              <p>
                Your systems and network security question bank, turned into a
                focused study routine.
              </p>
            </div>
            <div className="hero">
              <div>
                <span className="pill">DCIT 418 / SYSTEMS &amp; NETWORK SECURITY</span>
                <h2>
                  From cipher fundamentals
                  <br />
                  to exam confidence.
                </h2>
                <p>
                  Start with the core. Strengthen the tricky chapters.
                  <br />
                  Then put it all together in a timed mock.
                </p>
                <button
                  className="light-button"
                  onClick={() => navigate("practice")}
                >
                  Let’s practise <span>→</span>
                </button>
              </div>
              <div className="compiler-art" aria-hidden="true">
                <div>
                  <b>01</b> SYMMETRIC CIPHERS{" "}
                  <code>
                    DES, AES, block cipher modes;
                    <br />
                    diffusion and confusion.
                  </code>
                </div>
                <span>↓</span>
                <div>
                  <b>02</b> ASYMMETRIC CIPHERS{" "}
                  <span className="art-nodes">○ ── ◇ ── ◎</span>
                </div>
                <span>↓</span>
                <div>
                  <b>03</b> DATA INTEGRITY <strong>Hashes, MACs &amp; signatures. ✓</strong>
                </div>
              </div>
            </div>
            <div className="stats">
              <Stat
                label="Question bank"
                value={String(uniqueQuestionCount(bank))}
                detail={`Across ${titles.length} course parts`}
              />
              <Stat
                label="Overall accuracy"
                value={accuracy === null ? "—" : `${accuracy}%`}
                detail={`${progress.attempts.length} answers recorded`}
              />
              <Stat
                label="Still unseen"
                value={String(unseen)}
                detail="Reserved for fresh challenges"
              />
              <Stat
                label="Median answer time"
                value={
                  progress.attempts.length
                    ? `${Math.round(median(progress.attempts.map((a) => a.seconds)))}s`
                    : "—"
                }
                detail="Your pace, across all modes"
              />
            </div>
            <div className="section-heading">
              <h2>Choose your next step</h2>
              <span>A study loop that works.</span>
            </div>
            <div className="mode-grid">
              {(
                [
                  [
                    "practice",
                    "01",
                    "Build your foundation",
                    "Pick your topics and practise at your own pace. Get an explanation after every answer.",
                    "Start practising",
                  ],
                  [
                    "mock",
                    "02",
                    "Test your readiness",
                    `${mockTotal} questions. 60 minutes. Unseen questions first, with repeats when needed.`,
                    "Set up a mock",
                  ],
                  [
                    "review",
                    "03",
                    "Learn from the misses",
                    "Return to the questions that need another look, with your most-missed topics first.",
                    "Review mistakes",
                  ],
                ] as const
              ).map(([mode, n, title, description, action]) => (
                <button
                  className="mode-card"
                  key={mode}
                  onClick={() => navigate(mode)}
                >
                  <span className="mode-number">{n}</span>
                  <h3>{title}</h3>
                  <p>{description}</p>
                  <strong>
                    {action} <span>↗</span>
                  </strong>
                </button>
              ))}
            </div>
            <div className="bottom-note">
              <span>⌘</span> Built for focus. Keyboard friendly, distraction
              free, and ready offline after your first visit.
            </div>
          </>
        ) : view === "dashboard" ? (
          <Dashboard
            attempts={progress.attempts}
            onExport={() => void exportErrors()}
          />
        ) : view === "settings" ? (
          <Appearance
            theme={theme}
            onTheme={applyTheme}
            customAccent={customAccent}
            onCustomAccent={applyCustomAccent}
            fontSize={fontSize}
            onFontSize={applyFontSize}
          />
        ) : (
          <>
            <div className="page-heading">
              <div className="eyebrow">
                {view === "practice"
                  ? "MAKE IT YOURS"
                  : view === "mock"
                    ? "THE FULL EXAM EXPERIENCE"
                    : "TURN MISTAKES INTO PROGRESS"}
              </div>
              <h1>
                {view === "practice"
                  ? "Your practice, your pace."
                  : view === "mock"
                    ? "Ready for a mock?"
                    : "Give it another look."}
              </h1>
              <p>
                {view === "practice"
                  ? "Choose what to work on. Every answer is a chance to understand more."
                  : view === "mock"
                    ? `${mockTotal} questions: ${MOCK_PER_PART} guaranteed from each of ${COURSE_PARTS.length} parts, plus ${MOCK_RANDOM_EXTRA} random. Unseen questions first, with previously seen questions filling any gaps.`
                    : "Previously missed questions, ranked by miss count, then most recent miss."}
              </p>
            </div>
            {session && (
              <div className="notice">
                You have {session.submitted ? "a completed" : "an ongoing"}{" "}
                {session.mode} session.
                <button onClick={() => navigate(session.mode)}>Resume →</button>
              </div>
            )}
            <section className="setup-card">
              {view === "practice" ? (
                <>
                  <h2>
                    01 <span>Choose your parts</span>
                    <button
                      className="text-button"
                      onClick={() =>
                        setParts(
                          parts.length === COURSE_PARTS.length
                            ? []
                            : [...COURSE_PARTS],
                        )
                      }
                    >
                      {parts.length === COURSE_PARTS.length
                        ? "Unselect all"
                        : "Select all"}
                    </button>
                  </h2>
                  <div className="part-grid">
                    {titles.map((title, i) => (
                      <button
                        aria-pressed={parts.includes(i)}
                        className={
                          parts.includes(i) ? "part chosen" : "part"
                        }
                        key={title}
                        onClick={() =>
                          setParts((p) =>
                            p.includes(i)
                              ? p.filter((n) => n !== i)
                              : [...p, i],
                          )
                        }
                      >
                        <span>PART {i}</span>
                        <strong>{title}</strong>
                        <small>
                          {bank.filter((q) => q.part === i).length}{" "}
                          questions <b>{parts.includes(i) ? "✓" : "+"}</b>
                        </small>
                      </button>
                    ))}
                  </div>
                  <h2>
                    02 <span>Set your scope</span>
                  </h2>
                  <div className="segmented">
                    {[
                      ["core", "Core only"],
                      ["variants", "Variants only"],
                      ["all", "All questions"],
                    ].map(([v, l]) => (
                      <button
                        key={v}
                        aria-pressed={scope === v}
                        className={scope === v ? "chosen" : ""}
                        onClick={() => setScope(v)}
                      >
                        {l}
                      </button>
                    ))}
                  </div>
                  <div className="segmented">
                    {[
                      ["random", "Shuffle order"],
                      ["sequential", "Literal order"],
                    ].map(([v, l]) => (
                      <button
                        key={v}
                        aria-pressed={order === v}
                        className={order === v ? "chosen" : ""}
                        onClick={() => setOrder(v as "random" | "sequential")}
                      >
                        {l}
                      </button>
                    ))}
                  </div>
                  <h2>
                    03 <span>Choose source banks</span>
                  </h2>
                  {view === "practice" && (
                    <div className="segmented">
                      <label className={onlyUnseen ? "chosen" : ""}>
                        <input
                          type="checkbox"
                          checked={onlyUnseen}
                          onChange={(event) => setOnlyUnseen(event.target.checked)}
                        />{" "}
                        Only unseen
                      </label>
                    </div>
                  )}
                  <div className="source-grid">
                    {sourceBanks.map((source) => {
                      const checked = selectedSources.includes(source.id);
                      return (
                        <label
                          className={checked ? "source-bank chosen" : "source-bank"}
                          key={source.id}
                        >
                          <input
                            type="checkbox"
                            checked={checked}
                            onChange={() => toggleSource(source.id)}
                          />
                          <span>
                            <strong>{source.label}</strong>
                            <small>
                              {uniqueQuestionCount(
                                bank.filter((q) => q.batch === source.id),
                              )} questions
                            </small>
                          </span>
                        </label>
                      );
                    })}
                  </div>
                  <details>
                    <summary>
                      Fine-tune your session{" "}
                      <span>Source, level & question type</span>
                    </summary>
                    <div className="filters">
                      {[
                        [
                          "Source",
                          week,
                          setWeek,
                          [...new Set(bank.flatMap(weeks))].sort(),
                        ],
                        [
                          "Level",
                          level,
                          setLevel,
                          [...new Set(bank.map((q) => q.level))],
                        ],
                        [
                          "Type",
                          type,
                          setType,
                          ["mcq4", "mcq5", "multi", "fill", "tf"],
                        ],
                      ].map(([label, value, setter, options]) => (
                        <label key={String(label)}>
                          {String(label)}
                          <select
                            value={String(value)}
                            onChange={(e) =>
                              (
                                setter as React.Dispatch<
                                  React.SetStateAction<string>
                                >
                              )(e.target.value)
                            }
                          >
                            <option value="">All</option>
                            {(options as string[]).map((v) => (
                              <option key={v}>{v}</option>
                            ))}
                          </select>
                        </label>
                      ))}
                    </div>
                  </details>
                  <details>
                    <summary>
                      Export your deck{" "}
                      <span>Markdown, CSV or PDF, with answers</span>
                    </summary>
                    <div className="segmented">
                      {(
                        [
                          ["markdown", "Markdown"],
                          ["csv", "CSV"],
                          ["pdf", "PDF"],
                        ] as const
                      ).map(([v, l]) => (
                        <button
                          key={v}
                          aria-pressed={exportFormat === v}
                          className={exportFormat === v ? "chosen" : ""}
                          onClick={() => setExportFormat(v)}
                        >
                          {l}
                        </button>
                      ))}
                    </div>
                    <p className="export-note">
                      Downloads exactly what your current filters match:{" "}
                      {exportCandidates().length} questions, with answers and
                      explanations included.
                    </p>
                    <button className="secondary" onClick={downloadDeck}>
                      Download deck
                    </button>
                  </details>
                </>
              ) : view === "mock" ? (
                <>
                  <div className="mock-facts">
                    <Stat
                      label="Questions"
                      value={String(mockTotal)}
                      detail={`${MOCK_PER_PART} guaranteed per part, ${MOCK_RANDOM_EXTRA} random`}
                    />
                    <Stat
                      label="Time limit"
                      value="60 min"
                      detail="Auto-submit at zero"
                    />
                    <Stat
                      label="Question pool"
                      value={String(unseen)}
                      detail="Unseen first; reuse when needed"
                    />
                  </div>
                  <h3>Your next paper by part</h3>
                  <div className="availability">
                    {titles.map((title, i) => {
                      const count = bank.filter(
                        (q) => q.part === i && !progress.seen.includes(q.id),
                      ).length;
                      const quota = mockQuota(i);
                      return (
                        <div key={title}>
                          <span>
                            Part {i} · {title}
                          </span>
                          <strong className="good">
                            {Math.min(count, quota)} fresh ·{" "}
                            {Math.max(0, quota - count)} reused
                          </strong>
                        </div>
                      );
                    })}
                  </div>
                  <p>
                    The timer continues if you leave or reload. You can revisit
                    questions before submitting. Explanations appear only after
                    the whole paper is submitted.
                  </p>
                  <div className="set9-panel">
                    <h3>
                      The one you save for last
                      {set9OpenedAt && (
                        <span className="flag">
                          Opened {new Date(set9OpenedAt).toLocaleDateString()}
                        </span>
                      )}
                    </h3>
                    <p>
                      Set 9 is a fixed 60-minute, 100-mark paper across all 13
                      chapters: 30 MCQ, 8 fill-ins, 7 essay questions. Do it
                      ONCE, and do it last, after everything else. Pen and
                      paper, timer running, no notes.
                    </p>
                    <div className="fill-in-actions">
                      <button className="secondary-action" onClick={openSet9Paper}>
                        Open Set 9 paper
                      </button>
                      <button className="secondary-action" onClick={openSet9Key}>
                        Reveal answer key
                      </button>
                    </div>
                  </div>
                </>
              ) : (
                <>
                  <div className="review-count">
                    {reviewIds(progress.attempts).length}
                    <span>questions to revisit</span>
                  </div>
                  <p>
                    Questions remain available here even after you answer them
                    correctly, so you can reinforce what you learned.
                  </p>
                </>
              )}
              <div className="setup-footer">
                <span>
                  {view === "practice"
                    ? "Untimed · instant explanations"
                    : view === "mock"
                      ? "Timed · answers at the end"
                      : "Untimed · focused repetition"}
                </span>
                {view === "practice" && (
                  <button
                    className="secondary-action"
                    aria-label="Read these questions with answers"
                    onClick={() => startReading(true)}
                  >
                    Read instead
                  </button>
                )}
                <button
                  className="primary"
                  disabled={!!session && !session.submitted}
                  onClick={() => start(view as Mode)}
                >
                  {view === "practice"
                    ? "Start practice"
                    : view === "mock"
                      ? "Start 60-minute mock"
                      : "Start review"}{" "}
                  →
                </button>
              </div>
              {view === "practice" && (
                <div className="drill-panel">
                  <h3>
                    Fill-in drill <span>Type the answer instead of choosing</span>
                  </h3>
                  <div className="fill-in-tools">
                    <label className="drill-set-label">
                      <span>Fill-in set</span>
                      <select
                        aria-label="Fill-in set"
                        value={drillSet}
                        onChange={(e) => {
                          setDrillSet(e.target.value);
                        }}
                      >
                        <option value="original">
                          Bank fill-ins - {uniqueQuestionCount(bank.filter((q) => q.type === "fill" && !q.setName))} questions
                        </option>
                        {[...new Set(supplemental.map((q) => q.setName).filter(Boolean))].map((name) => (
                          <option key={name} value={name!}>
                            {name} - {uniqueQuestionCount(supplemental.filter((q) => q.setName === name))} questions
                          </option>
                        ))}
                        {supplemental.length > 0 && (
                          <option value="all">
                            All fill-ins - {uniqueQuestionCount([
                              ...bank.filter((q) => q.type === "fill"),
                            ])} questions
                          </option>
                        )}
                      </select>
                    </label>
                    <div className="fill-in-actions">
                      <button
                        className="primary"
                        disabled={!!session && !session.submitted}
                        onClick={() => start("practice", true)}
                      >
                        Start drill →
                      </button>
                      <button
                        className="secondary-action"
                        aria-label="Read fill-in questions with answers"
                        onClick={() => startReading(true, true)}
                      >
                        Read instead
                      </button>
                    </div>
                  </div>
                  <small>
                    Your selected parts, week and level still apply.
                  </small>
                </div>
              )}
              {session && !session.submitted && (
                <small>
                  Resume or end your current session before starting another.
                </small>
              )}
            </section>
          </>
        )}
        <footer>
          SECURITY LAB <span>Master the ciphers. Defend with confidence.</span>
          <span>DCIT 418</span>
        </footer>
      </main>
    </div>
  );
}

function Stat({
  label,
  value,
  detail,
}: {
  label: string;
  value: string;
  detail: string;
}) {
  return (
    <div className="stat">
      <span>{label}</span>
      <strong>{value}</strong>
      <small>{detail}</small>
    </div>
  );
}
function Feedback({
  q,
  attempt,
  onOverride,
}: {
  q: Question;
  attempt: Attempt;
  onOverride: () => void;
}) {
  const [confirmed, setConfirmed] = useState(false);
  return (
    <section
      className={`feedback ${attempt.correct ? "right" : "wrong"}`}
      aria-live="polite"
    >
      <h3>
        {attempt.correct ? "✓ Correct" : "↺ Not quite"}
        {attempt.override ? " · manually overridden" : ""}
      </h3>
      <div className="markdown">
        <strong>Expected answer</strong>
        {md(
          q.correctIndex === null
            ? q.correctText
            : displayOption(q, q.correctIndex),
        )}
        <strong>The rule that fixes it</strong>
        {md(q.reason)}
        <strong>Tempting wrong answer</strong>
        {md(q.trap)}
        <strong>Source</strong>
        {md(q.sourceRef)}
        {q.workingMarkdown && (
          <>
            <strong>Working</strong>
            {md(q.workingMarkdown)}
          </>
        )}
        <details>
          <summary>How this was checked</summary>
          {md(q.checkMethod)}
        </details>
      </div>
      {q.type === "fill" && !attempt.correct && !confirmed && (
        <div className="override">
          <p>Equivalent notation? You can correct the grading.</p>
          <button onClick={onOverride}>I was right, override</button>
          <button onClick={() => setConfirmed(true)}>I was wrong</button>
        </div>
      )}
    </section>
  );
}
function MockResults({
  session,
  attempts,
  onOverride,
  onClose,
}: {
  session: Session;
  attempts: Attempt[];
  onOverride: (a: Attempt) => void;
  onClose: () => void;
}) {
  const correct = attempts.filter((a) => a.correct).length;
  const total = attempts.length;
  return (
    <>
      <div className="page-heading">
        <div className="eyebrow">
          PAPER SUBMITTED · {new Date(session.startedAt).toLocaleDateString()}
        </div>
        <h1>Your mock results.</h1>
        <p>Every missed question is another concept you can make yours.</p>
      </div>
      <section className="setup-card">
        <div className="result-score">
          {correct}
          <span>/ {total}</span>
          <small>{Math.round((correct / total) * 100)}% accuracy</small>
        </div>
        <div className="part-scores">
          {titles.map((title, i) => {
            const partAttempts = attempts.filter(
              (a) => byId.get(a.questionId)!.part === i,
            );
            if (partAttempts.length === 0) return null;
            return (
              <div key={title}>
                <span>Part {i}</span>
                <strong>
                  {partAttempts.filter((a) => a.correct).length}/
                  {partAttempts.length}
                </strong>
                <small>{title}</small>
              </div>
            );
          })}
        </div>
        <button className="primary" onClick={onClose}>
          Back to progress →
        </button>
      </section>
      <h2 className="miss-heading">
        Review your paper · {total - correct} misses
      </h2>
      {attempts.map((a) => {
        const q = byId.get(a.questionId)!;
        return (
          <details className="result-item" key={a.id}>
            <summary>
              <span className={a.correct ? "good" : "bad"}>
                {a.correct ? "✓" : "↺"}
              </span>{" "}
              {q.id} · {q.source}{" "}
              <span>{a.correct ? "Correct" : "Missed"}</span>
            </summary>
            <div className="markdown">
              {md(q.bodyMarkdown)}
              <strong>Your answer</strong>
              {md(a.answer || "Unanswered")}
            </div>
            <Feedback q={q} attempt={a} onOverride={() => onOverride(a)} />
          </details>
        );
      })}
    </>
  );
}
function Dashboard({
  attempts,
  onExport,
}: {
  attempts: Attempt[];
  onExport: () => void;
}) {
  const score = attempts.filter((a) => a.correct).length;
  return (
    <>
      <div className="page-heading">
        <div className="eyebrow">YOUR LEARNING, IN VIEW</div>
        <h1>Progress you can build on.</h1>
        <p>
          Every attempt counts. Find your strengths and what deserves more time.
        </p>
      </div>
      <div className="stats">
        <Stat
          label="Overall accuracy"
          value={
            attempts.length
              ? `${Math.round((score / attempts.length) * 100)}%`
              : "—"
          }
          detail={`${score} correct answers`}
        />
        <Stat
          label="Attempts"
          value={String(attempts.length)}
          detail="Practice, review & submitted mocks"
        />
        <Stat
          label="Median time"
          value={
            attempts.length
              ? `${Math.round(median(attempts.map((a) => a.seconds)))}s`
              : "—"
          }
          detail="Per answered question"
        />
        <Stat
          label="Manual overrides"
          value={String(attempts.filter((a) => a.override).length)}
          detail="Included as correct"
        />
      </div>
      {!attempts.length && (
        <div className="notice">
          Your story starts with one question. Start a practice session to see
          your progress here.
        </div>
      )}
      {(["part", "week", "level", "type"] as const).map((group) => {
        const groups =
          group === "week"
            ? [...new Set(bank.flatMap(weeks))].sort()
            : group === "part"
              ? [...new Set(bank.map((q) => q.part))]
                  .sort((a, b) => a - b)
                  .map(String)
              : [...new Set(bank.map((q) => String(q[group])))];
        return (
          <section className="breakdown" key={group}>
            <h2>Accuracy by {group}</h2>
            <div className="table-scroll">
              <table>
                <thead>
                  <tr>
                    <th>{group}</th>
                    <th>Attempts</th>
                    <th>Accuracy</th>
                    <th>Median time</th>
                    <th>Focus</th>
                  </tr>
                </thead>
                <tbody>
                  {groups.map((value) => {
                    const list = attempts.filter((a) =>
                      group === "week"
                        ? weeks(byId.get(a.questionId)!).includes(value)
                        : String(byId.get(a.questionId)![group]) === value,
                    );
                    const accuracy = list.length
                      ? (list.filter((a) => a.correct).length / list.length) *
                        100
                      : 0;
                    const time = median(list.map((a) => a.seconds));
                    return (
                      <tr key={value}>
                        <th>
                          {group === "part"
                            ? `Part ${value} · ${titles[Number(value)]}`
                            : value}
                        </th>
                        <td>{list.length}</td>
                        <td>
                          {list.length ? `${Math.round(accuracy)}%` : "—"}
                          <div className="mini-track">
                            <i style={{ width: `${accuracy}%` }} />
                          </div>
                        </td>
                        <td>{list.length ? `${Math.round(time)}s` : "—"}</td>
                        <td>
                          {list.length > 0 &&
                          group === "part" &&
                          accuracy < 70 ? (
                            <span className="flag">Below 70%</span>
                          ) : list.length > 0 &&
                            group === "type" &&
                            time > 60 ? (
                            <span className="flag">Over 60s</span>
                          ) : (
                            "—"
                          )}
                        </td>
                      </tr>
                    );
                  })}
                </tbody>
              </table>
            </div>
          </section>
        );
      })}
      <MockHistory attempts={attempts} />
      <section className="export-card">
        <div>
          <h2>Take your lessons with you.</h2>
          <p>
            Export every wrong answer and the rule that fixes it to your notes.
          </p>
        </div>
        <button className="primary" onClick={onExport}>
          Copy & download error log ↗
        </button>
      </section>
      <section className="breakdown">
        <h2>Recent attempts</h2>
        {[...attempts]
          .sort((a, b) => b.timestamp - a.timestamp)
          .slice(0, 20)
          .map((a) => (
            <div className="history-row" key={a.id}>
              <strong>{a.questionId}</strong>
              <span>
                {a.mode} · {new Date(a.timestamp).toLocaleString()}
              </span>
              <span className={a.correct ? "good" : "bad"}>
                {a.correct ? "Correct" : "Wrong"}
                {a.override ? " (override)" : ""}
              </span>
              <span>{Math.round(a.seconds)}s</span>
            </div>
          ))}
      </section>
    </>
  );
}

function Appearance({
  theme,
  onTheme,
  customAccent,
  onCustomAccent,
  fontSize,
  onFontSize,
}: {
  theme: "default" | "dark" | "ocean" | "sunset" | "custom";
  onTheme: (t: "default" | "dark" | "ocean" | "sunset" | "custom") => void;
  customAccent: string;
  onCustomAccent: (hex: string) => void;
  fontSize: "sm" | "md" | "lg" | "xl";
  onFontSize: (s: "sm" | "md" | "lg" | "xl") => void;
}) {
  const themes = [
    ["default", "Sage", "#f7f8f4", "#214d3c"],
    ["dark", "Dark", "#161e1a", "#6fae7d"],
    ["ocean", "Ocean", "#f3f7fa", "#1c5c7a"],
    ["sunset", "Sunset", "#fbf5ee", "#b5551f"],
  ] as const;
  return (
    <>
      <div className="page-heading">
        <div className="eyebrow">MAKE IT YOURS</div>
        <h1>Appearance.</h1>
        <p>Pick a preset theme, or set your own accent colour and text size.</p>
      </div>
      <section className="breakdown">
        <h2>Theme</h2>
        <div className="mode-grid">
          {themes.map(([id, label, bg, accent]) => (
            <button
              key={id}
              className="mode-card"
              aria-pressed={theme === id}
              onClick={() => onTheme(id)}
              style={{
                borderColor: theme === id ? accent : undefined,
                borderWidth: theme === id ? 2 : undefined,
              }}
            >
              <span
                aria-hidden="true"
                style={{
                  display: "block",
                  height: 40,
                  borderRadius: 6,
                  marginBottom: 12,
                  background: bg,
                  border: `1px solid ${accent}`,
                }}
              >
                <span
                  style={{
                    display: "block",
                    width: "40%",
                    height: "100%",
                    borderRadius: "6px 0 0 6px",
                    background: accent,
                  }}
                />
              </span>
              <strong>{label}</strong>
            </button>
          ))}
          <button
            className="mode-card"
            aria-pressed={theme === "custom"}
            onClick={() => onTheme("custom")}
            style={{
              borderColor: theme === "custom" ? customAccent : undefined,
              borderWidth: theme === "custom" ? 2 : undefined,
            }}
          >
            <span
              aria-hidden="true"
              style={{
                display: "block",
                height: 40,
                borderRadius: 6,
                marginBottom: 12,
                background: "#f7f8f4",
                border: `1px solid ${customAccent}`,
              }}
            >
              <span
                style={{
                  display: "block",
                  width: "40%",
                  height: "100%",
                  borderRadius: "6px 0 0 6px",
                  background: customAccent,
                }}
              />
            </span>
            <strong>Custom</strong>
            <label
              onClick={(e) => e.stopPropagation()}
              style={{
                marginTop: 8,
                display: "flex",
                gap: 8,
                alignItems: "center",
              }}
            >
              <input
                type="color"
                value={customAccent}
                onChange={(e) => {
                  onCustomAccent(e.target.value);
                  onTheme("custom");
                }}
              />
              <span style={{ fontSize: 11 }}>{customAccent}</span>
            </label>
          </button>
        </div>
      </section>
      <section className="breakdown">
        <h2>Text size</h2>
        <div className="segmented" style={{ maxWidth: 470 }}>
          {(
            [
              ["sm", "Small"],
              ["md", "Default"],
              ["lg", "Large"],
              ["xl", "Extra large"],
            ] as const
          ).map(([id, label]) => (
            <button
              key={id}
              aria-pressed={fontSize === id}
              className={fontSize === id ? "chosen" : ""}
              onClick={() => onFontSize(id)}
            >
              {label}
            </button>
          ))}
        </div>
      </section>
    </>
  );
}

createRoot(document.getElementById("root")!).render(<App />);
if ("serviceWorker" in navigator && import.meta.env.PROD)
  navigator.serviceWorker.register("./sw.js").catch(() => {
    /* App remains usable when browser disallows offline caching. */
  });
