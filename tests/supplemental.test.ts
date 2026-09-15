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
