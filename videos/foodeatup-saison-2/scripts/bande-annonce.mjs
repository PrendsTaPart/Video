#!/usr/bin/env node
// Rend les deux cartons de la bande-annonce : HTML déterministe → images → deux MP4 muets.
// Usage : node scripts/bande-annonce.mjs
// Produit dans renders/bande-annonce/work/ : carton-ouverture.mp4 (2 s), carton-fin.mp4 (5 s).
import { readFileSync, writeFileSync, mkdirSync, rmSync } from "node:fs";
import { execFileSync } from "node:child_process";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";
import { createRequire } from "node:module";

const require = createRequire(import.meta.url);
const { chromium } = require(process.env.PLAYWRIGHT_MODULE || "/opt/node22/lib/node_modules/playwright");
const CHROME = process.env.CHROME_PATH || "/opt/pw-browsers/chromium-1194/chrome-linux/chrome";

const ROOT = join(dirname(fileURLToPath(import.meta.url)), "..");
const REPO = join(ROOT, "..", "..");
const b64 = (p, mime) => `data:${mime};base64,${readFileSync(p).toString("base64")}`;

const html = readFileSync(join(ROOT, "outro", "bande-annonce.html"), "utf8")
  .replace("__FONT__", b64(join(REPO, "studio-video/assets/vendor/fonts/Fredoka-Variable.woff2"), "font/woff2"))
  .replace("__LOGO__", b64(join(REPO, "studio-video/assets/brand/logo/foodeatup-logo-horizontal.png"), "image/png"));

const DIR = join(ROOT, "renders", "bande-annonce");
const WORK = join(DIR, "work");
const FRAMES = join(WORK, "cartons");
rmSync(FRAMES, { recursive: true, force: true });
mkdirSync(FRAMES, { recursive: true });

const page_html = join(WORK, "cartons.html");
writeFileSync(page_html, html);

const browser = await chromium.launch({ executablePath: CHROME, args: ["--no-sandbox", "--force-device-scale-factor=1"] });
const page = await browser.newPage({ viewport: { width: 1080, height: 1920 }, deviceScaleFactor: 1 });
await page.goto("file://" + page_html);
await page.evaluate(() => document.fonts.ready);
const OUV = await page.evaluate(() => window.OUVERTURE);
const TOTAL = await page.evaluate(() => window.TOTAL);
for (let f = 0; f < TOTAL; f++) {
  await page.evaluate((i) => window.seek(i), f);
  await page.screenshot({ path: join(FRAMES, `f${String(f).padStart(4, "0")}.png`) });
  if (f % 60 === 0) process.stdout.write(`  ${f}/${TOTAL}\n`);
}
await browser.close();

// Les deux plages ne se suivent jamais à l'écran : on les sort en deux fichiers.
const encode = (debut, nb, sortie) =>
  execFileSync("ffmpeg", ["-y", "-loglevel", "error", "-framerate", "30",
    "-start_number", String(debut), "-i", join(FRAMES, "f%04d.png"), "-frames:v", String(nb),
    "-c:v", "libx264", "-preset", "slow", "-crf", "17", "-pix_fmt", "yuv420p",
    "-video_track_timescale", "15360", join(WORK, sortie)], { stdio: "inherit" });

encode(0, OUV, "carton-ouverture.mp4");
encode(OUV, TOTAL - OUV, "carton-fin.mp4");
console.log(`✅ ${join(WORK, "carton-ouverture.mp4")} (${OUV} images)`);
console.log(`✅ ${join(WORK, "carton-fin.mp4")} (${TOTAL - OUV} images)`);
