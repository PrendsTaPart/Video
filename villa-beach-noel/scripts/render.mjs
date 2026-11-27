#!/usr/bin/env node
// Rendu image par image de composition/index.html (Playwright) -> MP4 H.264 1080x1920 30 fps,
// puis mixage audio : voix ElevenLabs (audio/vo/voNN.mp3) + musique (audio/music/music.mp3)
// avec ducking automatique sous la voix et normalisation -14 LUFS (standard Reels/TikTok).
//
//   node scripts/render.mjs --tl main  --out renders/villa-beach-noel-23-decembre.mp4 [--wip]
//   node scripts/render.mjs --tl reel1 --out renders/reels/reel-1.mp4 [--wip]
//   node scripts/render.mjs --tl main  --stills 1,5,9,13      (captures PNG de contrôle)
import { createRequire } from "node:module";
const { chromium } = createRequire(import.meta.url)("playwright");
import { spawn, execSync } from "node:child_process";
import { createServer } from "node:http";
import { readFileSync, existsSync, mkdirSync, writeFileSync } from "node:fs";
import path from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";

const ROOT = path.dirname(path.dirname(fileURLToPath(import.meta.url)));
const COMP = path.join(ROOT, "composition");
const arg = (k, d) => { const i = process.argv.indexOf("--" + k); return i < 0 ? d : (process.argv[i + 1]?.startsWith("--") || process.argv[i + 1] === undefined ? true : process.argv[i + 1]); };
const tlName = arg("tl", "main");
const wip = !!arg("wip", false);
const FPS = parseInt(arg("fps", "30"));
const out = path.resolve(ROOT, arg("out", `renders/${tlName}.mp4`));
const stills = arg("stills", null);

const { TIMELINES, VO } = await import(pathToFileURL(path.join(COMP, "timelines.js")));
const TL = TIMELINES[tlName];

// durées réelles des voix présentes
const dur = (f) => parseFloat(execSync(`ffprobe -v error -show_entries format=duration -of csv=p=0 "${f}"`).toString());
const vodur = {};
for (const v of TL.vo) { const f = path.join(ROOT, "audio/vo", v.id + ".mp3"); if (existsSync(f)) vodur[v.id] = +dur(f).toFixed(2); }
// contrôle de chevauchement voix
TL.vo.forEach((v, i) => {
  const end = v.at + (vodur[v.id] ?? VO[v.id].est); const next = TL.vo[i + 1];
  if (next && end > next.at - 0.15) console.warn(`⚠ ${v.id} finit à ${end.toFixed(2)}s, ${next.id} démarre à ${next.at}s`);
  if (end > TL.duration) console.warn(`⚠ ${v.id} dépasse la fin du film`);
});

// serveur statique
const MIME = { ".html": "text/html", ".js": "text/javascript", ".jpg": "image/jpeg", ".png": "image/png", ".woff2": "font/woff2" };
const server = createServer((req, res) => {
  const p = path.join(COMP, decodeURIComponent(new URL(req.url, "http://x").pathname));
  if (!p.startsWith(COMP) || !existsSync(p)) { res.writeHead(404); return res.end(); }
  res.writeHead(200, { "content-type": MIME[path.extname(p)] || "application/octet-stream" }); res.end(readFileSync(p));
}).listen(0);
const port = server.address().port;

const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: 1080, height: 1920 }, deviceScaleFactor: 1 });
const q = new URLSearchParams({ tl: tlName, wip: wip ? "1" : "0", vodur: JSON.stringify(vodur) });
await page.goto(`http://127.0.0.1:${port}/index.html?${q}`);
await page.waitForFunction(() => window.READY === true, null, { timeout: 60000 });

if (stills) {
  const dir = path.join(ROOT, "renders/stills"); mkdirSync(dir, { recursive: true });
  for (const t of String(stills).split(",").map(Number)) {
    await page.evaluate((t) => window.seek(t), t);
    await page.screenshot({ path: path.join(dir, `${tlName}-${String(t).padStart(5, "0")}.png`) });
  }
  await browser.close(); server.close(); console.log("stills ->", dir); process.exit(0);
}

mkdirSync(path.dirname(out), { recursive: true });
const silent = out.replace(/\.mp4$/, ".video.mp4");
const ff = spawn("ffmpeg", ["-y", "-loglevel", "error", "-f", "image2pipe", "-framerate", String(FPS), "-i", "-",
  "-c:v", "libx264", "-preset", "medium", "-crf", "18", "-pix_fmt", "yuv420p", "-r", String(FPS), silent], { stdio: ["pipe", "inherit", "inherit"] });
const N = Math.round(TL.duration * FPS);
const t0 = Date.now();
for (let i = 0; i < N; i++) {
  await page.evaluate((t) => window.seek(t), i / FPS);
  const buf = await page.screenshot({ type: "jpeg", quality: 92 });
  if (!ff.stdin.write(buf)) await new Promise((r) => ff.stdin.once("drain", r));
  if (i % 150 === 0) console.log(`${tlName}: ${i}/${N} images (${((Date.now() - t0) / 1000).toFixed(0)} s)`);
}
ff.stdin.end(); await new Promise((r) => ff.on("close", r));
await browser.close(); server.close();

// ---------- audio ----------
const inputs = ["-i", silent]; const filt = []; let idx = 1; const voLabels = [];
for (const v of TL.vo) {
  const f = path.join(ROOT, "audio/vo", v.id + ".mp3"); if (!existsSync(f)) continue;
  inputs.push("-i", f); const ms = Math.round(v.at * 1000);
  filt.push(`[${idx}:a]aresample=48000,adelay=${ms}|${ms},apad=whole_dur=${TL.duration}[v${idx}]`); voLabels.push(`[v${idx}]`); idx++;
}
const musicFile = path.join(ROOT, "audio/music/music.mp3");
const hasMusic = existsSync(musicFile);
if (hasMusic) {
  inputs.push("-i", musicFile);
  filt.push(`[${idx}:a]aresample=48000,atrim=${TL.musicOffset || 0}:${(TL.musicOffset || 0) + TL.duration},asetpts=PTS-STARTPTS,volume=${TL.musicVolume},afade=t=in:d=0.8,afade=t=out:st=${TL.duration - 2.2}:d=2.2,apad=whole_dur=${TL.duration}[mus]`); idx++;
}
let final;
if (voLabels.length) {
  filt.push(`${voLabels.join("")}amix=inputs=${voLabels.length}:normalize=0,volume=1.0[vox]`);
  if (hasMusic) {
    filt.push(`[vox]asplit[vx1][vx2]`, `[mus][vx1]sidechaincompress=threshold=0.02:ratio=5:attack=30:release=450[md]`, `[md][vx2]amix=inputs=2:normalize=0[mix]`);
    final = "[mix]";
  } else final = "[vox]";
} else if (hasMusic) final = "[mus]";
const args = ["-y", "-loglevel", "error", ...inputs];
if (final) {
  filt.push(`${final}loudnorm=I=-14:TP=-1.5:LRA=11,atrim=0:${TL.duration}[aout]`);
  args.push("-filter_complex", filt.join(";"), "-map", "0:v", "-map", "[aout]", "-c:a", "aac", "-b:a", "192k", "-ar", "48000");
} else {
  args.push("-f", "lavfi", "-i", `anullsrc=r=48000:cl=stereo`, "-map", "0:v", "-map", `${idx}:a`, "-c:a", "aac", "-shortest");
}
args.push("-c:v", "copy", "-movflags", "+faststart", "-t", String(TL.duration), out);
execSync("ffmpeg " + args.map((a) => `'${a.replace(/'/g, "'\\''")}'`).join(" "), { stdio: "inherit" });
execSync(`rm -f "${silent}"`);

// sous-titres SRT (toutes les répliques)
const fmt = (s) => { const ms = Math.round(s * 1000); const h = Math.floor(ms / 3600000), m = Math.floor(ms / 60000) % 60, ss = Math.floor(ms / 1000) % 60; return `${String(h).padStart(2, "0")}:${String(m).padStart(2, "0")}:${String(ss).padStart(2, "0")},${String(ms % 1000).padStart(3, "0")}`; };
const srt = TL.vo.map((v, i) => `${i + 1}\n${fmt(v.at)} --> ${fmt(v.at + (vodur[v.id] ?? VO[v.id].est))}\n${VO[v.id].text}\n`).join("\n");
writeFileSync(out.replace(/\.mp4$/, ".srt"), srt);
console.log(`✔ ${out}  (voix: ${voLabels.length}/${TL.vo.length}, musique: ${hasMusic ? "oui" : "non"})`);
