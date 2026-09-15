import { existsSync } from "node:fs";
import { spawnSync } from "node:child_process";
const npm = process.platform === "win32" ? "npm.cmd" : "npm";
function run(args) {
  const r = spawnSync(npm, args, {
    stdio: "inherit",
    shell: process.platform === "win32",
  });
  if (r.status !== 0) process.exit(r.status ?? 1);
}
if (!existsSync("node_modules/vite")) run(["ci"]);
run(["run", "build"]);
run(["run", "preview", "--", "--port", "4173"]);
