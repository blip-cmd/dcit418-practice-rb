import { test, expect } from "@playwright/test";

async function setup(page: import("@playwright/test").Page) {
  await page.goto("/");
  await page.getByRole("button", { name: /^Let.*practise/ }).click();
  await page.getByLabel("Fill-in set", { exact: true }).selectOption("IT_Fill In Drill 100");
}

test("IT drill starts 100 questions in learning order and grades answers", async ({ page }) => {
  await setup(page);
  await expect(page.getByRole("button", { name: "Literal order" })).toHaveAttribute("aria-pressed", "true");
  await page.screenshot({ path: "test-results/it-fill-setup-desktop.png", fullPage: true });
  await page.getByRole("button", { name: "Start drill" }).click();
  await expect(page.locator(".question-body")).toContainText("Bringing people and resources together");
  const ids = await page.evaluate(() => JSON.parse(localStorage.getItem("dcit402-progress-v1")!).session.ids);
  expect(ids).toHaveLength(100);
  expect(ids[0]).toBe("IT-FILL-001");
  expect(ids[99]).toBe("IT-FILL-100");
  await page.getByRole("textbox").fill("management");
  await page.getByRole("button", { name: /check answer/i }).click();
  await expect(page.locator(".feedback.right")).toContainText("Management coordinates resources");
  await page.reload();
  await expect(page.locator(".feedback.right")).toBeVisible();
});

test("IT drill reader respects the selected set on mobile", async ({ page }) => {
  await page.setViewportSize({ width: 390, height: 844 });
  await setup(page);
  await page.getByRole("button", { name: "Read fill-in questions with answers" }).click();
  await expect(page.locator(".reader-navigation")).toContainText("Question 1 of 100");
  await expect(page.locator(".feedback.right")).toContainText("Management coordinates resources");
  await page.getByRole("button", { name: /Next/ }).click();
  await expect(page.locator(".question-body")).toContainText("recruits, selects and trains");
  expect(await page.evaluate(() => document.documentElement.scrollWidth <= window.innerWidth)).toBe(true);
  await page.screenshot({ path: "test-results/it-fill-reader-mobile.png", fullPage: true });
});
