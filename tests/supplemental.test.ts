import { describe, it, expect } from "vitest";
import {
  bank,
  supplemental,
  grade,
  createSession,
  emptyProgress,
  parseProgress,
  mockIds,
  type Question,
} from "../src/model";

describe("supplemental fill-in sets", () => {
  it("loads 100 distinct IT drill questions with explanations and accepts every answer variant", () => {
    const drill = supplemental.filter((q) => q.setName === "IT_Fill In Drill 100");
    expect(drill).toHaveLength(100);
    expect(new Set(drill.map((q) => q.bodyMarkdown)).size).toBe(100);
    expect(drill[0].id).toBe("IT-FILL-001");
    expect(drill[99].id).toBe("IT-FILL-100");
    for (const q of drill) {
      expect(q.bodyMarkdown.match(/____/g)).toHaveLength(1);
      expect(q.sourceRef).toMatch(/bd\/|slides_in_pdf\//);
      expect(q.reason.length).toBeGreaterThan(30);
      for (const answer of q.answerBlanks![0]) {
        expect(grade(q, { answer, selected: null, seconds: 0 })).toBe(true);
      }
      expect(grade(q, { answer: "unrelated answer", selected: null, seconds: 0 })).toBe(false);
    }
    const session = createSession("practice", drill.map((q) => q.id));
    const restored = parseProgress(JSON.stringify({ ...emptyProgress(), session }));
    expect(restored.session?.ids).toEqual(drill.map((q) => q.id));
  });
  it("loads bank questions without errors and handles supplemental data", () => {
    expect(bank.length).toBeGreaterThan(0);
    expect(Array.isArray(supplemental)).toBe(true);
  });
  it("grades ordered multiple blanks and per-blank alternatives", () => {
    const dummy: Question = {
      ...bank[0],
      id: "test-drill-1",
      setName: "test_set",
      bodyMarkdown: "Fill in: ____ and ____",
      answerBlanks: [
        ["one", "1"],
        ["two", "2"],
      ],
      type: "fill",
      correctText: "one; two",
      acceptedAnswers: [],
      options: [],
    };
    expect(
      grade(dummy, { answer: "one; two", selected: null, seconds: 0 }),
    ).toBe(true);
    expect(
      grade(dummy, { answer: "1; 2", selected: null, seconds: 0 }),
    ).toBe(true);
    expect(
      grade(dummy, { answer: "two; one", selected: null, seconds: 0 }),
    ).toBe(false);
    expect(
      grade(dummy, { answer: "one", selected: null, seconds: 0 }),
    ).toBe(false);
  });
  it("supports saved sessions without expanding mock pool", () => {
    const p = {
      ...emptyProgress(),
      seen: ["P1-Q1"],
      session: createSession("practice", ["P1-Q1"]),
    };
    expect(parseProgress(JSON.stringify(p)).session!.ids).toEqual([
      "P1-Q1",
    ]);
    expect(mockIds(p.seen).every((id) => id.startsWith("P"))).toBe(true);
  });
});
