import { test, expect } from "@playwright/test";
import { practiceBank, questionKey, STORAGE, emptyProgress } from "../../src/model";

if (process.env.PLAYWRIGHT_BASE_URL) test.use({ baseURL: process.env.PLAYWRIGHT_BASE_URL });

test("only unseen excludes already-seen questions from the selected bank", async ({ page }) => {
  const seen = practiceBank.find((q) => q.batch === "quizbank")!;
  expect(seen).toBeTruthy();
  await page.goto("/");
  await page.evaluate(({ key, history }) => localStorage.setItem(key, JSON.stringify(history)), {
    key: STORAGE, history: { ...emptyProgress(), seen: [seen.id] },
  });
  await page.reload();
  await page.getByRole("button", { name: /^Let.*practise/ }).click();
  await page.getByRole("button", { name: "All questions", exact: true }).click();
  for (const checkbox of await page.locator(".source-grid input").all()) await checkbox.uncheck();
  await page.getByRole("checkbox", { name: /Consolidated Quiz Bank/ }).check();
  await expect(page.getByRole("checkbox", { name: "Only unseen", exact: true })).not.toBeChecked();
  await page.getByRole("checkbox", { name: "Only unseen", exact: true }).check();
  await page.screenshot({ path: "test-results/only-unseen-desktop.png", fullPage: true });
  await page.getByRole("button", { name: /^Start practice/ }).click();
  const ids: string[] = await page.evaluate((key) => JSON.parse(localStorage.getItem(key)!).session.ids, STORAGE);
  const questions = ids.map((id) => practiceBank.find((q) => q.id === id)!);
  expect(questions.length).toBeGreaterThan(0);
  expect(questions.every((q) => q.batch === "quizbank")).toBe(true);
  expect(questions.some((q) => questionKey(q) === questionKey(seen))).toBe(false);
  expect(new Set(questions.map(questionKey)).size).toBe(questions.length);
});

test("unseen filter also applies to fill-in reading", async ({ page }) => {
  const fill = practiceBank.filter((q) => q.type === "fill");
  const remaining = fill.filter((q) => questionKey(q) !== questionKey(fill[0]));
  await page.setViewportSize({ width: 390, height: 844 });
  await page.goto("/");
  await page.evaluate(({ key, history }) => localStorage.setItem(key, JSON.stringify(history)), {
    key: STORAGE, history: { ...emptyProgress(), seen: [fill[0].id] },
  });
  await page.reload();
  await page.getByRole("button", { name: /^Let.*practise/ }).click();
  await page.getByLabel("Fill-in set", { exact: true }).selectOption("original");
  await page.getByRole("checkbox", { name: "Only unseen", exact: true }).check();
  await page.screenshot({ path: "test-results/only-unseen-mobile.png", fullPage: true });
  expect(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth)).toBe(true);
  await page.getByRole("button", { name: "Read fill-in questions with answers" }).click();
  await expect(page.locator(".reader-navigation")).toContainText(`Question 1 of ${new Set(remaining.map(questionKey)).size}`);
  const seenIds: string[] = await page.evaluate((key) => JSON.parse(localStorage.getItem(key)!).seen, STORAGE);
  expect(seenIds.length).toBeGreaterThan(1);
  expect(questionKey(practiceBank.find((q) => q.id === seenIds.at(-1))!)).not.toBe(questionKey(fill[0]));
});
