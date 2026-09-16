import { test, expect, type Page } from "@playwright/test";
import {
  bank,
  COURSE_PARTS,
  mockQuota,
  mockTotalTarget,
  practiceBank,
  byId,
  createSession,
  emptyProgress,
  mockIds,
  STORAGE,
  type Progress,
} from "../../src/model";

const fillQuestion = bank.find((q) => q.type === "fill")!;
const MOCK_TOTAL = mockTotalTarget();

async function seed(page: Page, progress: Progress) {
  await page.goto("/");
  await page.evaluate(
    ({ key, value }) => localStorage.setItem(key, JSON.stringify(value)),
    { key: STORAGE, value: progress },
  );
  await page.reload();
}
test("home, practice setup, keyboard answer and persistence", async ({
  page,
}) => {
  await page.goto("/");
  await expect(
    page.getByRole("heading", { name: "Make the concepts click." }),
  ).toBeVisible();
  await expect(page).toHaveTitle("Security Lab · DCIT 418");
  await expect.poll(async () => {
    const sidebar = await page.locator("#study-sidebar").boundingBox();
    const content = await page.locator("main").boundingBox();
    return content!.x >= sidebar!.x + sidebar!.width;
  }).toBe(true);
  await page.screenshot({
    path: "test-results/home-desktop.png",
    fullPage: true,
    animations: "disabled",
  });
  await page.getByRole("button", { name: "Let’s practise" }).click();
  await page.getByRole("button", { name: "Start practice" }).click();
  await expect(page.locator(".question-card")).toBeVisible();
  await expect(page.locator(".feedback")).toHaveCount(0);
  if (await page.getByRole("textbox").count())
    await page.getByRole("textbox").fill("test answer");
  else await page.keyboard.press("1");
  await page.locator("h1").click();
  await page.keyboard.press("Enter");
  await expect(page.locator(".feedback")).toBeVisible();
  await page.reload();
  await expect(page.locator(".feedback")).toBeVisible();
  await page.keyboard.press("Enter");
  await expect(page.locator(".feedback")).toHaveCount(0);
  const p = await page.evaluate(
    (key) => JSON.parse(localStorage.getItem(key)!),
    STORAGE,
  );
  expect(p.attempts).toHaveLength(1);
  expect(p.seen).toHaveLength(2);
});
test("fill override records correctness and removes the miss from review", async ({
  page,
}) => {
  await seed(page, {
    ...emptyProgress(),
    seen: [fillQuestion.id],
    session: createSession("practice", [fillQuestion.id]),
  });
  await page.getByRole("textbox").fill("my equivalent notation");
  await page.keyboard.press("Enter");
  await page.getByRole("button", { name: "I was right, override" }).click();
  await expect(
    page.getByRole("heading", { name: /Correct.*manually overridden/ }),
  ).toBeVisible();
  const p = await page.evaluate(
    (key) => JSON.parse(localStorage.getItem(key)!),
    STORAGE,
  );
  expect(p.attempts[0].override).toBe(true);
  expect(p.attempts[0].correct).toBe(true);
});
for (const id of ["P1-Q1", fillQuestion.id])
  test(`mobile diagram and card preservation ${id}`, async ({ page }) => {
    await page.setViewportSize({ width: 390, height: 844 });
    await seed(page, {
      ...emptyProgress(),
      seen: [id],
      session: createSession("practice", [id]),
    });
    await expect(page.locator(".question-card")).toBeVisible();
    expect(
      await page.evaluate(
        () => document.documentElement.scrollWidth <= window.innerWidth,
      ),
    ).toBe(true);
    await page.screenshot({
      path: `test-results/${id}-mobile.png`,
      fullPage: true,
    });
  });
test("mock hides answers, preserves choices and deadline, and submits the full paper", async ({
  page,
}) => {
  await page.goto("/");
  await page.getByRole("button", { name: "Mock exam" }).click();
  await page.getByRole("button", { name: "Start 60-minute mock" }).click();
  const before = await page.evaluate(
    (key) => JSON.parse(localStorage.getItem(key)!),
    STORAGE,
  );
  expect(before.session.ids).toHaveLength(MOCK_TOTAL);
  await expect(page.locator(".feedback")).toHaveCount(0);
  if (await page.getByRole("textbox").count())
    await page.getByRole("textbox").fill("answer");
  else await page.keyboard.press("1");
  await page.reload();
  const after = await page.evaluate(
    (key) => JSON.parse(localStorage.getItem(key)!),
    STORAGE,
  );
  expect(after.session.deadline).toBe(before.session.deadline);
  expect(after.session.drafts[after.session.ids[0]].answer).not.toBe("");
  await page.getByRole("button", { name: "Submit paper", exact: true }).click();
  await expect(
    page.getByRole("heading", { name: "Your mock results." }),
  ).toBeVisible();
  const final = await page.evaluate(
    (key) => JSON.parse(localStorage.getItem(key)!),
    STORAGE,
  );
  expect(final.attempts).toHaveLength(MOCK_TOTAL);
  expect(final.seen).toHaveLength(MOCK_TOTAL);
  await page.reload();
  expect(
    (
      await page.evaluate(
        (key) => JSON.parse(localStorage.getItem(key)!),
        STORAGE,
      )
    ).attempts,
  ).toHaveLength(MOCK_TOTAL);
});
test("expired mock auto-submits on reload", async ({ page }) => {
  await seed(page, {
    ...emptyProgress(),
    session: createSession("mock", mockIds([]), Date.now() - 3601000),
  });
  await expect(
    page.getByRole("heading", { name: "Your mock results." }),
  ).toBeVisible();
  expect(
    (
      await page.evaluate(
        (key) => JSON.parse(localStorage.getItem(key)!),
        STORAGE,
      )
    ).attempts,
  ).toHaveLength(MOCK_TOTAL);
});
test("offline cache reloads the full app", async ({ page, context }) => {
  await page.goto("/");
  await page.evaluate(() => navigator.serviceWorker.ready);
  await page.reload();
  await context.setOffline(true);
  await page.reload();
  await expect(
    page.getByRole("heading", { name: "Make the concepts click." }),
  ).toBeVisible();
  await page.getByRole("button", { name: "Let’s practise" }).click();
  await page.getByRole("button", { name: "Start practice" }).click();
  await expect(page.locator(".question-card")).toBeVisible();
});

test("export and import resumes the active question on another device", async ({
  page,
  browser,
}) => {
  const s = createSession("practice", [fillQuestion.id, "P1-Q1"]);
  await seed(page, { ...emptyProgress(), session: s, seen: [fillQuestion.id] });
  await page.getByRole("textbox").fill(fillQuestion.correctText);
  const downloaded = page.waitForEvent("download");
  await page.getByRole("button", { name: "Export progress" }).click();
  const path = await (await downloaded).path();
  const other = await browser.newContext();
  const second = await other.newPage();
  await second.goto("/");
  await second.locator("input[type=file]").setInputFiles(path!);
  await expect(second.getByRole("textbox")).toHaveValue(fillQuestion.correctText);
  await second.getByRole("button", { name: "Check answer" }).click();
  await expect(
    second.getByRole("heading", { name: "✓ Correct", exact: true }),
  ).toBeVisible();
  await second.getByRole("button", { name: "Your progress" }).click();
  await expect(
    second.getByRole("heading", { name: "Accuracy by part" }),
  ).toBeVisible();
  await other.close();
});

test("dashboard flags, review queue and CSV download reflect actual mistakes", async ({
  page,
}) => {
  const s = createSession("practice", ["P1-Q1"]);
  await seed(page, {
    ...emptyProgress(),
    seen: ["P1-Q1"],
    attempts: [
      {
        id: "a",
        sessionId: s.id,
        questionId: "P1-Q1",
        answer: 'Wrong, "quoted"',
        correct: false,
        seconds: 75,
        mode: "practice",
        timestamp: Date.now(),
        override: false,
      },
    ],
  });
  await page.getByRole("button", { name: "Your progress" }).click();
  await expect(page.getByText("Below 70%", { exact: true })).toBeVisible();
  await expect(page.getByText("Over 60s", { exact: true })).toBeVisible();
  const downloaded = page.waitForEvent("download");
  await page.getByRole("button", { name: "Copy & download error log" }).click();
  expect((await downloaded).suggestedFilename()).toBe("dcit418-errors.csv");
  await page.getByRole("button", { name: /Review mistakes/ }).click();
  await page.getByRole("button", { name: "Start review" }).click();
  await expect(
    page.locator(".tags").getByText("P1-Q1", { exact: true }),
  ).toBeVisible();
});

test("reading shows answers immediately, navigates with arrows and records no attempts", async ({
  page,
}) => {
  await page.goto("/");
  await page.getByRole("button", { name: "Read with answers" }).click();
  await expect(
    page.getByRole("heading", { name: "Read with answers." }),
  ).toBeVisible();
  await expect(
    page.getByRole("heading", { name: "Answer", exact: true }),
  ).toBeVisible();
  const firstId = practiceBank[0].id;
  const secondId = practiceBank[1].id;
  await expect(page.locator(".feedback")).toContainText(
    byId.get(firstId)!.reason.replace(/\*\*/g, ""),
  );
  await expect(page.getByRole("button", { name: "Previous" })).toBeDisabled();
  await page.keyboard.press("ArrowRight");
  await expect(page.locator(".tags")).toContainText(secondId);
  await page.keyboard.press("ArrowLeft");
  await expect(
    page.locator(".tags").getByText(firstId, { exact: true }),
  ).toBeVisible();
  const saved = await page.evaluate(
    (key) => JSON.parse(localStorage.getItem(key)!),
    STORAGE,
  );
  expect(saved.attempts).toHaveLength(0);
  expect(saved.seen).toEqual([firstId, secondId]);
  await page.setViewportSize({ width: 390, height: 844 });
  expect(
    await page.evaluate(
      () => document.documentElement.scrollWidth <= innerWidth,
    ),
  ).toBe(true);
});

test("reading uses practice filters and cannot expose answers during a mock", async ({
  page,
}) => {
  await page.goto("/");
  await page.getByRole("button", { name: /^Let/ }).click();
  await page
    .locator(".setup-footer")
    .getByRole("button", { name: "Read these questions with answers" })
    .click();
  const coreCount = practiceBank.filter((q) => q.isCore).length;
  await expect(page.locator(".reader-navigation")).toContainText(
    `of ${coreCount}`,
  );
  await page.keyboard.press("ArrowRight");
  await expect(
    page.locator(".tags").getByText(practiceBank[1].id, { exact: true }),
  ).toBeVisible();
  await seed(page, {
    ...emptyProgress(),
    session: createSession("mock", mockIds([])),
  });
  await page.getByRole("button", { name: "Read with answers" }).click();
  await expect(page.getByRole("status")).toContainText(
    "Submit your active mock",
  );
  await expect(page.locator(".feedback")).toHaveCount(0);
});

test("quiz arrows navigate without grading and leave text cursor keys intact", async ({
  page,
}) => {
  await seed(page, {
    ...emptyProgress(),
    seen: [fillQuestion.id],
    session: createSession("practice", [fillQuestion.id, "P1-Q1"]),
  });
  await page.getByRole("textbox").fill(fillQuestion.correctText);
  await page.keyboard.press("ArrowRight");
  await expect(page.locator(".tags")).toContainText(fillQuestion.id);
  await page.locator("h1").click();
  await page.keyboard.press("ArrowRight");
  await expect(page.locator(".tags")).toContainText("P1-Q1");
  await page.keyboard.press("ArrowLeft");
  await expect(page.getByRole("textbox")).toHaveValue(fillQuestion.correctText);
  expect(
    (
      await page.evaluate(
        (key) => JSON.parse(localStorage.getItem(key)!),
        STORAGE,
      )
    ).attempts,
  ).toHaveLength(0);
});

test("sidebar collapses, remembers preference, and expands on mobile", async ({
  page,
}) => {
  await page.goto("/");
  await page
    .getByRole("button", { name: "Collapse sidebar", exact: true })
    .click();
  await expect(page.locator("#study-sidebar")).toBeHidden();
  await expect(
    page.getByRole("button", { name: "Expand sidebar", exact: true }),
  ).toHaveAttribute("aria-expanded", "false");
  await page.reload();
  await expect(page.locator("#study-sidebar")).toBeHidden();
  await page.setViewportSize({ width: 390, height: 844 });
  await page
    .getByRole("button", { name: "Expand sidebar", exact: true })
    .focus();
  await page.keyboard.press("Enter");
  await expect(page.locator("#study-sidebar")).toBeVisible();
  await expect(
    page.getByRole("button", { name: "Collapse sidebar", exact: true }),
  ).toHaveAttribute("aria-expanded", "true");
  expect(
    await page.evaluate(
      () => document.documentElement.scrollWidth <= innerWidth,
    ),
  ).toBe(true);
  await page
    .getByRole("button", { name: "Collapse sidebar", exact: true })
    .click();
  expect(
    await page.evaluate(
      () => document.documentElement.scrollWidth <= innerWidth,
    ),
  ).toBe(true);
});

test("fully seen bank still starts a balanced mock", async ({ page }) => {
  await seed(page, { ...emptyProgress(), seen: practiceBank.map((q) => q.id) });
  await page.getByRole("button", { name: "Mock exam" }).click();
  await expect(page.getByText("0 fresh", { exact: false })).toHaveCount(COURSE_PARTS.length);
  await page.getByRole("button", { name: "Start 60-minute mock" }).click();
  await expect(page.locator(".question-card")).toBeVisible();
  const saved = await page.evaluate(
    (key) => JSON.parse(localStorage.getItem(key)!),
    STORAGE,
  );
  expect(new Set(saved.session.ids).size).toBe(MOCK_TOTAL);
  // Each part is guaranteed its quota; the random top-up can add more to any part.
  for (const part of COURSE_PARTS)
    expect(
      saved.session.ids.filter((id: string) => byId.get(id)!.part === part).length,
    ).toBeGreaterThanOrEqual(mockQuota(part));
});

test("fill-in drill starts only fill questions and accepts a correct answer", async ({
  page,
}) => {
  await page.goto("/");
  await page.getByRole("button", { name: /^Let/ }).click();
  await page.getByRole("button", { name: "Start drill" }).click();
  await expect(page.getByRole("textbox")).toBeVisible();
  const saved = await page.evaluate(
    (key) => JSON.parse(localStorage.getItem(key)!),
    STORAGE,
  );
  expect(saved.session.ids.length).toBe(
    bank.filter((q) => q.type === "fill").length,
  );
  expect(
    saved.session.ids.every((id: string) => byId.get(id)!.type === "fill"),
  ).toBe(true);
  await page
    .getByRole("textbox")
    .fill(byId.get(saved.session.ids[0])!.correctText);
  await page.getByRole("button", { name: "Check answer" }).click();
  await expect(page.locator(".feedback.right")).toBeVisible();
});
