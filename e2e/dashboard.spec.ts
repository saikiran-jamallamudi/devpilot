import { test, expect } from "@playwright/test";
test("dashboard renders the DevPilot workspace", async ({ page }) => {
  await page.goto("/");
  await expect(page.getByRole("heading", { name: /build software/i })).toBeVisible();
  await expect(page.getByText("Specification", { exact: true })).toBeVisible();
  await expect(page.getByText("Code review", { exact: true })).toBeVisible();
});
