import { readFileSync, writeFileSync } from "node:fs";

const read = (path) => readFileSync(new URL(path, import.meta.url), "utf8");
const markdown = read("../../bd/it-fill-in-drill-100.md");
const metadata = JSON.parse(read("../../bd/it-fill-in-drill-100-metadata.json"));
const blocks = [...markdown.matchAll(/^### (\d+)\. (.+)\r?\n\r?\n\*\*Answer:\*\* (.+)\r?\n\r?\n\*\*Reason:\*\* (.+)/gm)];
if (blocks.length !== 100 || metadata.length !== 100) {
  throw new Error("IT fill-in drill must contain exactly 100 questions and metadata rows.");
}
const bodies = new Set();
const rows = blocks.map(([, number, bodyMarkdown, answer, reason], index) => {
  const meta = metadata[index];
  const key = bodyMarkdown.toLowerCase().replace(/[^a-z0-9]+/g, " ").trim();
  if (Number(number) !== index + 1 || meta.number !== index + 1 || bodies.has(key) ||
      (bodyMarkdown.match(/____/g) ?? []).length !== 1 || !meta.sourceRef) {
    throw new Error(`Invalid question or metadata at ${number}.`);
  }
  bodies.add(key);
  return {
    ...meta,
    id: `IT-FILL-${number.padStart(3, "0")}`,
    setName: "IT_Fill In Drill 100",
    batch: "itfill100",
    bodyMarkdown,
    answerBlanks: [[answer, ...meta.acceptedAnswers]],
    reason,
    checkMethod: "Adapted as a single-blank question from the source recorded in the companion metadata; answer and explanation are maintained in bd/it-fill-in-drill-100.md.",
  };
});
const target = new URL("../supplemental/drills.json", import.meta.url);
const existing = JSON.parse(readFileSync(target, "utf8"));
const otherSets = existing.filter((row) => row.setName !== "IT_Fill In Drill 100");
writeFileSync(target, JSON.stringify([...otherSets, ...rows], null, 2) + "\n");
console.log(`Built ${rows.length} unique IT fill-in questions from Markdown.`);
