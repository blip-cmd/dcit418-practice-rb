import raw from "../questions.json" with { type: "json" };
import drillRows from "../supplemental/drills.json" with { type: "json" };
export type Kind = "mcq4" | "mcq5" | "fill" | "tf" | "multi";
export type Mode = "practice" | "review" | "mock";
export interface Question {
  id: string;
  part: number;
  batch: string;
  family: string;
  isCore: boolean;
  week: string;
  source: string;
  level: string;
  type: Kind;
  bodyMarkdown: string;
  options: string[];
  correctIndex: number | null;
  correctIndices?: number[] | null;
  correctText: string;
  acceptedAnswers: string[];
  reason: string;
  trap: string;
  sourceRef: string;
  checkMethod: string;
  workingMarkdown: string;
  setName?: string;
  answerBlanks?: string[][];
}
export interface DrillRow {
  id: string;
  setName: string;
  number: number;
  bodyMarkdown: string;
  answerBlanks: string[][];
  part: number;
  week: string;
  topic: string;
  batch?: string;
  reason?: string;
  sourceRef?: string;
  checkMethod?: string;
}
export const bank = raw as Question[];
export const supplemental: Question[] = (drillRows as DrillRow[]).map((row) => ({
  ...row,
  batch: row.batch ?? row.setName,
  family: row.id,
  isCore: true,
  source: row.topic,
  level: "Recall",
  type: "fill",
  options: [],
  correctIndex: null,
  correctText: row.answerBlanks.map((a) => a[0]).join("; "),
  acceptedAnswers:
    row.answerBlanks.length === 1 ? row.answerBlanks[0].slice(1) : [],
  reason: row.reason ?? `Expected terms, in blank order: ${row.answerBlanks.map((a) => a.join(" / ")).join("; ")}.`,
  trap: "Check the exact term and the order of the blanks.",
  sourceRef: row.sourceRef ?? `User-provided ${row.setName}, question ${row.number}. Topic/week grouping is an app classification, not a verified course citation.`,
  checkMethod:
    row.checkMethod ?? "Transcribed from the supplied answer key. Equivalent notation can be manually overridden.",
  workingMarkdown: "",
}));
export const practiceBank: Question[] = [...bank, ...supplemental];
export const byId = new Map([...bank, ...supplemental].map((q) => [q.id, q]));
export const questionKey = (q: Question) =>
  q.bodyMarkdown.toLowerCase().replace(/[^a-z0-9]+/g, " ").trim();

export function unseenQuestions(items: Question[], seenIds: string[]): Question[] {
  const excluded = new Set(
    seenIds.flatMap((id) => {
      const question = byId.get(id);
      return question ? [questionKey(question)] : [];
    }),
  );
  return items.filter((question) => {
    const key = questionKey(question);
    if (excluded.has(key)) return false;
    excluded.add(key);
    return true;
  });
}
export interface Attempt {
  id: string;
  questionId: string;
  answer: string;
  correct: boolean;
  seconds: number;
  mode: Mode;
  timestamp: number;
  override: boolean;
  sessionId: string;
}
export interface Draft {
  answer: string;
  selected: number | null;
  selectedMulti?: number[];
  seconds: number;
}
export interface Session {
  id: string;
  mode: Mode;
  ids: string[];
  index: number;
  orders: Record<string, number[]>;
  drafts: Record<string, Draft>;
  startedAt: number;
  visitedAt: number;
  deadline: number | null;
  submitted: boolean;
}
export interface Progress {
  course: "dcit418";
  version: 1;
  attempts: Attempt[];
  seen: string[];
  session: Session | null;
}
export const emptyProgress = (): Progress => ({
  course: "dcit418",
  version: 1,
  attempts: [],
  seen: [],
  session: null,
});
export const STORAGE = "dcit418-progress-v1";
export function weeks(q: Question): string[] {
  return [q.week];
}
export function shuffle<T>(items: T[], random = Math.random): T[] {
  const a = [...items];
  for (let i = a.length - 1; i > 0; i--) {
    const j = Math.floor(random() * (i + 1));
    [a[i], a[j]] = [a[j], a[i]];
  }
  return a;
}
export function grade(q: Question, draft: Draft): boolean {
  if (q.answerBlanks) {
    const normalize = (s: string) =>
      s
        .trim()
        .toLowerCase()
        .replace(/`/g, "")
        .replace(/\\(?:varepsilon|epsilon)/g, "ε")
        .replace(/epsilon/g, "ε")
        .replace(/\\emptyset/g, "∅")
        .replace(/\\[{}]/g, (s) => s.slice(1))
        .replace(/[_\s-]/g, "");
    const answers =
      q.answerBlanks.length === 1 ? [draft.answer] : draft.answer.split(/[;,]/);
    return (
      answers.length === q.answerBlanks.length &&
      q.answerBlanks.every((accepted, i) =>
        accepted.some((a) => normalize(a) === normalize(answers[i])),
      )
    );
  }
  if (q.type === "fill")
    return [q.correctText, ...q.acceptedAnswers].some(
      (a) => a.trim().toLowerCase() === draft.answer.trim().toLowerCase(),
    );
  if (q.type === "multi") {
    const expected = [...(q.correctIndices ?? [])].sort((a, b) => a - b);
    const given = [...(draft.selectedMulti ?? [])].sort((a, b) => a - b);
    return (
      expected.length > 0 &&
      expected.length === given.length &&
      expected.every((v, i) => v === given[i])
    );
  }
  return draft.selected === q.correctIndex;
}
export function displayOption(q: Question, index: number): string {
  const text = q.options[index];
  // Resolve combination references to their actual statements before shuffling.
  if (
    /^(?:[A-E](?:\s+(?:and|or)\s+[A-E])+|All of the above|None of the above)$/i.test(
      text.trim(),
    )
  ) {
    if (/^(All|None)/i.test(text)) {
      const statements = q.options.filter(
        (o) =>
          !/^(?:[A-E](?:\s+(?:and|or)\s+[A-E])+|All of the above|None of the above)$/i.test(
            o.trim(),
          ),
      );
      return `${/^All/i.test(text) ? "All" : "None"} of these statements: ${statements.map((s) => `(${s})`).join("; ")}`;
    }
    return text.replace(
      /\b[A-E]\b/g,
      (letter) => `(${q.options[letter.charCodeAt(0) - 65]})`,
    );
  }
  return text;
}
export function createSession(
  mode: Mode,
  ids: string[],
  now = Date.now(),
): Session {
  return {
    id:
      typeof crypto.randomUUID === "function"
        ? crypto.randomUUID()
        : `${now}-${Array.from(crypto.getRandomValues(new Uint32Array(4))).join("-")}`,
    mode,
    ids,
    index: 0,
    orders: Object.fromEntries(
      ids.map((id) => [id, shuffle(byId.get(id)!.options.map((_, i) => i))]),
    ),
    drafts: {},
    startedAt: now,
    visitedAt: now,
    deadline: mode === "mock" ? now + 3600000 : null,
    submitted: false,
  };
}
export const COURSE_PARTS = Array.from({ length: 14 }, (_, i) => i); // Part 0 .. Part 13
export const MOCK_PER_PART = 4;
export const MOCK_RANDOM_EXTRA = 4;
export function mockQuota(part: number): number {
  return Math.min(MOCK_PER_PART, bank.filter((q) => q.part === part).length);
}
export function mockGuaranteedTotal(): number {
  return COURSE_PARTS.reduce((sum, part) => sum + mockQuota(part), 0);
}
export function mockTotalTarget(): number {
  return Math.min(mockGuaranteedTotal() + MOCK_RANDOM_EXTRA, bank.length);
}
export function mockIds(seen: string[]): string[] {
  const used = new Set(seen);
  const ids: string[] = [];
  for (const part of COURSE_PARTS) {
    const pool = bank.filter((q) => q.part === part && !used.has(q.id));
    const repeats = bank.filter((q) => q.part === part && used.has(q.id));
    ids.push(
      ...[...shuffle(pool), ...shuffle(repeats)]
        .slice(0, mockQuota(part))
        .map((q) => q.id),
    );
  }
  const selected = new Set(ids);
  const extraNeeded = mockTotalTarget() - ids.length;
  const extraPool = bank.filter((q) => !selected.has(q.id) && !used.has(q.id));
  const extraRepeats = bank.filter(
    (q) => !selected.has(q.id) && used.has(q.id),
  );
  ids.push(
    ...[...shuffle(extraPool), ...shuffle(extraRepeats)]
      .slice(0, extraNeeded)
      .map((q) => q.id),
  );
  return shuffle(ids);
}
export function reviewIds(attempts: Attempt[]): string[] {
  const misses = new Map<string, { count: number; last: number }>();
  for (const a of attempts.filter((a) => !a.correct)) {
    const old = misses.get(a.questionId);
    misses.set(a.questionId, {
      count: (old?.count ?? 0) + 1,
      last: Math.max(old?.last ?? 0, a.timestamp),
    });
  }
  return [...misses]
    .sort((a, b) => b[1].count - a[1].count || b[1].last - a[1].last)
    .map(([id]) => id);
}
export function median(values: number[]): number {
  const s = [...values].sort((a, b) => a - b);
  return s.length
    ? (s[Math.floor((s.length - 1) / 2)] + s[Math.floor(s.length / 2)]) / 2
    : 0;
}
export function makeAttempt(
  s: Session,
  qid: string,
  now = Date.now(),
): Attempt {
  const q = byId.get(qid)!;
  const d = s.drafts[qid] ?? { answer: "", selected: null, seconds: 0 };
  return {
    id: `${s.id}:${qid}`,
    sessionId: s.id,
    questionId: qid,
    answer: d.answer,
    correct: grade(q, d),
    seconds: d.seconds,
    mode: s.mode,
    timestamp: now,
    override: false,
  };
}
export function submitMock(p: Progress, now = Date.now()): Progress {
  const s = p.session;
  if (!s || s.mode !== "mock" || s.submitted) return p;
  const attempts = s.ids.map((id) => makeAttempt(s, id, now));
  return {
    ...p,
    seen: [...new Set([...p.seen, ...s.ids])],
    attempts: [...p.attempts.filter((a) => a.sessionId !== s.id), ...attempts],
    session: { ...s, submitted: true },
  };
}
export function errorCsv(attempts: Attempt[]): string {
  const rows = [
    [
      "Question ID",
      "Part",
      "Week",
      "Topic source",
      "What I answered",
      "Correct answer",
      "The rule that fixes it",
    ],
    ...attempts
      .filter((a) => !a.correct)
      .map((a) => {
        const q = byId.get(a.questionId)!;
        return [
          q.id,
          String(q.part),
          q.week,
          q.source,
          a.answer,
          q.correctText,
          q.reason,
        ];
      }),
  ];
  return (
    "\uFEFF" +
    rows
      .map((row) =>
        row
          .map((value) => {
            const safe = /^[=+@\-\t\r]/.test(value) ? `'${value}` : value;
            return `"${safe.replaceAll('"', '""')}"`;
          })
          .join(","),
      )
      .join("\r\n")
  );
}
export function parseProgress(text: string, { requireCourse = false } = {}): Progress {
  const p: unknown = JSON.parse(text);
  if (
    !p ||
    typeof p !== "object" ||
    !("version" in p) ||
    p.version !== 1 ||
    !("attempts" in p) ||
    !Array.isArray(p.attempts) ||
    !("seen" in p) ||
    !Array.isArray(p.seen)
  )
    throw new Error("Invalid progress file.");
  if (("course" in p && p.course !== "dcit418") || (requireCourse && !("course" in p)))
    throw new Error("Import a DCIT 418 progress export. For older DCIT 418 backups, export again from the updated app.");
  // Question IDs are reassigned sequentially per part every time the bank is
  // regenerated, so an ID like "P3-Q15" saved before a content change can
  // legitimately stop existing, or start pointing at a different question,
  // without the saved data itself being corrupt. Rejecting the whole file
  // over a few stale IDs would strand a user's entire history behind one
  // unresolvable reference; instead, structural corruption (wrong types,
  // malformed shape) still throws, but a merely-unrecognized question ID is
  // dropped and the rest of the record is kept.
  const seenValid = (p.seen as unknown[]).filter(
    (id): id is string => typeof id === "string" && byId.has(id),
  );
  const attempts: Attempt[] = [];
  for (const a of p.attempts as unknown[]) {
    if (!a || typeof a !== "object") throw new Error("Invalid attempt.");
    const r = a as Record<string, unknown>;
    if (
      typeof r.id !== "string" ||
      typeof r.sessionId !== "string" ||
      typeof r.questionId !== "string" ||
      typeof r.answer !== "string" ||
      typeof r.correct !== "boolean" ||
      typeof r.override !== "boolean" ||
      typeof r.seconds !== "number" ||
      !Number.isFinite(r.seconds) ||
      r.seconds < 0 ||
      typeof r.timestamp !== "number" ||
      !Number.isFinite(r.timestamp) ||
      !["practice", "mock", "review"].includes(String(r.mode))
    )
      throw new Error("Invalid attempt data.");
    if (byId.has(r.questionId)) attempts.push(r as unknown as Attempt);
  }
  let session: Session | null = null;
  if ("session" in p && p.session !== null) {
    // A session referencing a question ID the current bank no longer has,
    // or a mock paper whose size no longer matches today's mock target, is
    // stale rather than corrupt: drop it and keep the rest of the import.
    // Anything else invalid about the session (malformed option order, a
    // draft that doesn't match its question, wrong field types) is real
    // corruption and should still fail loudly via validateSession below.
    if (!sessionLooksStale(p.session)) session = validateSession(p.session);
  }
  return {
    version: 1,
    course: "dcit418",
    attempts,
    seen: [...new Set([...seenValid, ...attempts.map((a) => a.questionId)])],
    session,
  };
}

function sessionLooksStale(value: unknown): boolean {
  if (!value || typeof value !== "object") return false;
  const s = value as Record<string, unknown>;
  if (!Array.isArray(s.ids)) return false;
  const ids = s.ids as unknown[];
  if (!ids.every((id) => typeof id === "string" && byId.has(id))) return true;
  if (s.mode === "mock") {
    const known = ids as string[];
    if (known.length !== mockTotalTarget()) return true;
    if (
      COURSE_PARTS.some(
        (part) =>
          known.filter((id) => byId.get(id)!.part === part).length <
          mockQuota(part),
      )
    )
      return true;
  }
  return false;
}

function validateSession(value: unknown): Session {
  if (!value || typeof value !== "object") throw new Error("Invalid session.");
  const s = value as Record<string, unknown>;
  if (
    typeof s.id !== "string" ||
    !["practice", "review", "mock"].includes(String(s.mode)) ||
    !Array.isArray(s.ids) ||
    !s.ids.length ||
    !s.ids.every((id) => typeof id === "string" && byId.has(id)) ||
    new Set(s.ids).size !== s.ids.length ||
    typeof s.index !== "number" ||
    !Number.isInteger(s.index) ||
    s.index < 0 ||
    s.index >= s.ids.length ||
    typeof s.startedAt !== "number" ||
    !Number.isFinite(s.startedAt) ||
    typeof s.visitedAt !== "number" ||
    !Number.isFinite(s.visitedAt) ||
    typeof s.submitted !== "boolean" ||
    !s.orders ||
    typeof s.orders !== "object" ||
    !s.drafts ||
    typeof s.drafts !== "object"
  )
    throw new Error("Invalid saved session.");
  if (
    s.mode === "mock" &&
    (typeof s.deadline !== "number" ||
      !Number.isFinite(s.deadline) ||
      s.deadline !== s.startedAt + 3600000 ||
      s.ids.length !== mockTotalTarget() ||
      COURSE_PARTS.some(
        (part) =>
          (s.ids as string[]).filter((id) => byId.get(id)!.part === part)
            .length < mockQuota(part),
      ))
  )
    throw new Error("Invalid mock paper.");
  const orders = s.orders as Record<string, unknown>;
  for (const id of s.ids as string[]) {
    const order = orders[id];
    const size = byId.get(id)!.options.length;
    if (
      !Array.isArray(order) ||
      order.length !== size ||
      new Set(order).size !== size ||
      !order.every((i) => Number.isInteger(i) && i >= 0 && i < size)
    )
      throw new Error("Invalid option order.");
  }
  for (const [id, value] of Object.entries(s.drafts)) {
    if (
      !(s.ids as string[]).includes(id) ||
      !value ||
      typeof value !== "object"
    )
      throw new Error("Invalid answer draft.");
    const d = value as Record<string, unknown>;
    const q = byId.get(id)!;
    if (
      typeof d.answer !== "string" ||
      typeof d.seconds !== "number" ||
      !Number.isFinite(d.seconds) ||
      d.seconds < 0 ||
      (d.selected !== null &&
        (typeof d.selected !== "number" ||
          !Number.isInteger(d.selected) ||
          d.selected < 0 ||
          d.selected >= q.options.length)) ||
      (d.selectedMulti !== undefined &&
        (!Array.isArray(d.selectedMulti) ||
          !d.selectedMulti.every(
            (i) =>
              Number.isInteger(i) && i >= 0 && i < q.options.length,
          )))
    )
      throw new Error("Invalid answer draft.");
  }
  return value as Session;
}
