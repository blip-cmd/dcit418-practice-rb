import { describe, it, expect } from "vitest";
import { bank, unseenQuestions } from "../src/model";

describe("unseen questions across banks", () => {
  it("excludes a seen question under another ID regardless of case and punctuation", () => {
    const seen = bank[0];
    const duplicate = { ...seen, id: "another-bank-id", batch: "another-bank", bodyMarkdown: seen.bodyMarkdown.toUpperCase() + " !" };
    const fresh = { ...seen, id: "fresh", bodyMarkdown: "A distinct question about coordination?" };
    expect(unseenQuestions([duplicate, fresh], [seen.id])).toEqual([fresh]);
  });
  it("keeps only the first occurrence of an unseen question and ignores unknown history IDs", () => {
    const first = bank[0];
    const copy = { ...first, id: "copy" };
    expect(unseenQuestions([first, copy], ["deleted-question"])).toEqual([first]);
    expect(unseenQuestions([first, copy], [first.id])).toEqual([]);
  });
});
