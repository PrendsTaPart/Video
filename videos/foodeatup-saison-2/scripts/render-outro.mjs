#!/usr/bin/env node
// Rend l'outro de 10 s d'un épisode : HTML déterministe → 300 images → MP4.
// Usage : node scripts/render-outro.mjs <numéro d'épisode>
// Prérequis : la dernière image de la scène 2 dans renders/ep{NN}/scene2-last-frame.png
import { readFileSync, writeFileSync, mkdirSync, rmSync, existsSync } from "node:fs";
import { execFileSync } from "node:child_process";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";
import { createRequire } from "node:module";

// playwright est installé globalement dans cet environnement (pas de node_modules local)
const require = createRequire(import.meta.url);
const { chromium } = require(process.env.PLAYWRIGHT_MODULE || "/opt/node22/lib/node_modules/playwright");
const CHROME = process.env.CHROME_PATH || "/opt/pw-browsers/chromium-1194/chrome-linux/chrome";

const ROOT = join(dirname(fileURLToPath(import.meta.url)), "..");
const REPO = join(ROOT, "..", "..");
const NN = (n) => String(n).padStart(2, "0");
const num = Number(process.argv[2] || 1);
const n = NN(num);

const S = JSON.parse(readFileSync(join(ROOT, "episodes.json"), "utf8"));
const ep = S.episodes.find((e) => e.num === num);
if (!ep) throw new Error(`épisode ${n} introuvable`);

const EPDIR = join(ROOT, "renders", `ep${n}`);
const WORK = join(EPDIR, "work");          // intermédiaires, ignorés par git
const FRAMES = join(WORK, "frames");
const plate = join(EPDIR, "scene2-last-frame.png");
if (!existsSync(plate)) throw new Error(`manque ${plate} (ffmpeg -sseof -0.1 -i scene2.mp4 -frames:v 1 …)`);

const b64 = (p, mime) => `data:${mime};base64,${readFileSync(p).toString("base64")}`;
const html = readFileSync(join(ROOT, "outro", "template.html"), "utf8")
  .replace("__FONT__", b64(join(REPO, "studio-video/assets/vendor/fonts/Fredoka-Variable.woff2"), "font/woff2"))
  .replace("__LOGO__", b64(join(REPO, "studio-video/assets/brand/logo/foodeatup-logo-horizontal.png"), "image/png"))
  .replace("__PLATE__", b64(plate, "image/png"))
  .replace("__DATA__", JSON.stringify({ texte_ecran: ep.montage.texte_ecran, cartes: ep.montage.cartes, transition: S.transition.texte }));

rmSync(FRAMES, { recursive: true, force: true });
mkdirSync(FRAMES, { recursive: true });
mkdirSync(WORK, { recursive: true });
const page_html = join(WORK, "outro.html");
writeFileSync(page_html, html);

const FPS = S.outro.fps, DUR = S.outro.frames;
const browser = await chromium.launch({ executablePath: CHROME, args: ["--no-sandbox", "--force-device-scale-factor=1"] });
const page = await browser.newPage({ viewport: { width: 1080, height: 1920 }, deviceScaleFactor: 1 });
await page.goto("file://" + page_html);
await page.evaluate(() => document.fonts.ready);
for (let f = 0; f < DUR; f++) {
  await page.evaluate((i) => window.seek(i), f);
  await page.screenshot({ path: join(FRAMES, `f${String(f).padStart(4, "0")}.png`) });
  if (f % 60 === 0) process.stdout.write(`  ${f}/${DUR}\n`);
}
/* miniature : l'image à 2,5 s + le titre de l'épisode en gros */
const thumbHtml = `<meta charset="utf-8">
<style>
@font-face{font-family:"Goodly";src:url(${b64(join(REPO,"studio-video/assets/vendor/fonts/Fredoka-Variable.woff2"),"font/woff2")}) format("woff2");font-weight:300 700}
*{margin:0;box-sizing:border-box}html,body{width:1080px;height:1920px;overflow:hidden;background:#0F1A23}
body{font-family:"Goodly",system-ui,sans-serif}
img{position:absolute;inset:0;width:1080px;height:1920px;object-fit:cover}
.panel{position:absolute;left:0;right:0;bottom:0;height:760px;background:linear-gradient(180deg,rgba(15,26,35,0) 0%,rgba(15,26,35,.96) 26%,#0F1A23 100%);
  display:flex;flex-direction:column;justify-content:flex-end;align-items:center;padding:0 120px 300px}
.ep{font-size:56px;font-weight:600;letter-spacing:8px;color:#A6D0FF;margin-bottom:18px}
.t{font-size:190px;font-weight:700;color:#FCF9E6;line-height:.94;text-align:center;letter-spacing:-4px}
.p{font-size:56px;font-weight:500;color:#FFA500;margin-top:34px;text-align:center}
</style>
<img src="${b64(join(FRAMES, "f0000.png"), "image/png")}">
<div class="panel"><div class="ep">ÉPISODE ${n}</div><div class="t">${ep.titre.toUpperCase()}</div><div class="p">${ep.montage.texte_ecran}</div></div>`;
const thumbFile = join(WORK, "thumb.html");
writeFileSync(thumbFile, thumbHtml);
await page.goto("file://" + thumbFile);
await page.evaluate(() => document.fonts.ready);
await page.screenshot({ path: join(EPDIR, `ep${n}-thumb.png`) });

await browser.close();

const mp4 = join(WORK, `ep${n}-outro-sans-son.mp4`);
execFileSync("ffmpeg", ["-y", "-loglevel", "error", "-framerate", String(FPS), "-i", join(FRAMES, "f%04d.png"),
  "-c:v", "libx264", "-preset", "slow", "-crf", "16", "-pix_fmt", "yuv420p", mp4]);
console.log(`✅ ${mp4}`);
