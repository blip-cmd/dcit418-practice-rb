import { describe, it, expect } from "vitest";
import {
  bank,
  byId,
  createSession,
  displayOption,
  emptyProgress,
  errorCsv,
  grade,
  makeAttempt,
  median,
  mockIds,
  parseProgress,
  reviewIds,
  submitMock,
} from "../src/model";

describe("exam integrity", () => {
  it("draws 60 unique unseen questions, exactly 10 per part", () => {
    const seen = bank.slice(0, 30).map((q) => q.id);
    const ids = mockIds(seen);
    expect(new Set(ids).size).toBe(60);
    expect(ids.some((id) => seen.includes(id))).toBe(false);
    for (let p = 1; p <= 6; p++)
      expect(ids.filter((id) => byId.get(id)!.part === p)).toHaveLength(10);
  });
  it("reuses questions in depleted parts without duplicates, even when all are seen", () => {
    for (const seen of [
      bank.filter((q) => q.part === 2).map((q) => q.id),
      bank.map((q) => q.id),
    ]) {
      const ids = mockIds(seen);
      expect(new Set(ids).size).toBe(60);
      for (let part = 1; part <= 6; part++)
        expect(ids.filter((id) => byId.get(id)!.part === part)).toHaveLength(
          10,
        );
    }
  });
  it("uses every remaining unseen question before filling a partial part", () => {
    const fresh = bank
      .filter((q) => q.part === 1)
      .slice(0, 3)
      .map((q) => q.id);
    const ids = mockIds(
      bank
        .filter((q) => q.part === 1 && !fresh.includes(q.id))
        .map((q) => q.id),
    );
    for (const id of fresh) expect(ids).toContain(id);
  });
  it("grades shuffled options by identity and fill-ins by normalized alternates", () => {
    const q = byId.get("P1-Q1")!;
    expect(
      grade(q, {
        answer: displayOption(q, q.correctIndex!),
        selected: q.correctIndex,
        seconds: 0,
      }),
    ).toBe(true);
    const fill = bank.find((x) => x.type === "fill")!;
    expect(
      grade(fill, { answer: `  ${fill.correctText.toLowerCase()}  `, selected: null, seconds: 0 }),
    ).toBe(true);
    expect(grade(fill, { answer: "completely_wrong_xyz", selected: null, seconds: 0 })).toBe(
      false,
    );
  });
  it("expands combination references without original letters", () => {
    const dummy = {
      ...byId.get("P1-Q1")!,
      options: ["Macro expansion", "File inclusion", "A and B", "All of the above"],
    };
    expect(displayOption(dummy, 2)).toBe("(Macro expansion) and (File inclusion)");
    expect(displayOption(dummy, 3)).toBe("All of these statements: (Macro expansion); (File inclusion)");
  });
  it("submits all 60 once, including blanks, and excludes the revealed paper from future mocks", () => {
    const s = createSession("mock", mockIds([]), 1000);
    const q = byId.get(s.ids[0])!;
    s.drafts[q.id] = {
      selected: q.correctIndex,
      answer: q.correctText,
      seconds: 19,
    };
    const p = submitMock({ ...emptyProgress(), session: s }, 3601000);
    expect(p.attempts).toHaveLength(60);
    expect(p.attempts.filter((a) => a.correct)).toHaveLength(1);
    expect(p.seen).toHaveLength(60);
    expect(submitMock(p).attempts).toHaveLength(60);
  });
  it("ranks frequent misses first and breaks ties by recency", () => {
    const s = createSession("review", ["P1-Q1", "P1-Q2"]);
    const a = makeAttempt(s, "P1-Q1", 1);
    const b = makeAttempt(s, "P1-Q2", 2);
    expect(reviewIds([a, b])).toEqual(["P1-Q2", "P1-Q1"]);
    expect(reviewIds([a, { ...a, id: "repeat" }, b])).toEqual([
      "P1-Q1",
      "P1-Q2",
    ]);
  });
  it("preserves active sessions and rejects malformed import data", () => {
    const p = {
      ...emptyProgress(),
      session: createSession("mock", mockIds([])),
    };
    expect(parseProgress(JSON.stringify(p)).session).toEqual(p.session);
    p.session.orders[p.session.ids[0]] = [999];
    expect(() => parseProgress(JSON.stringify(p))).toThrow("option order");
    expect(() =>
      parseProgress('{"version":1,"seen":["bad"],"attempts":[]}'),
    ).toThrow();
  });
  it("computes true medians and quotes multiline CSV safely", () => {
    expect(median([1, 2, 100, 200])).toBe(51);
    const s = createSession("practice", ["P1-Q1"]);
    s.drafts["P1-Q1"] = {
      answer: '=cmd,"x"\nnext',
      selected: null,
      seconds: 4,
    };
    const csv = errorCsv([makeAttempt(s, "P1-Q1")]);
    expect(csv).toContain('"\'=cmd,""x""\nnext"');
    expect(csv).toContain("The rule that fixes it");
  });
});
