#!/usr/bin/env node
// Exporte les 10 publications Instagram (1080x1350, PNG) depuis composition/posts.html.
//   node scripts/posts.mjs            -> posts/post-01.png ... post-10.png
import { createRequire } from "node:module";
import { createServer } from "node:http";
import { readFileSync, existsSync, mkdirSync } from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";
const { chromium } = createRequire(import.meta.url)("playwright");

const ROOT = path.dirname(path.dirname(fileURLToPath(import.meta.url)));
const COMP = path.join(ROOT, "composition");
const MIME = { ".html": "text/html", ".js": "text/javascript", ".jpg": "image/jpeg", ".woff2": "font/woff2" };
const server = createServer((req, res) => {
  const p = path.join(COMP, decodeURIComponent(new URL(req.url, "http://x").pathname));
  if (!p.startsWith(COMP) || !existsSync(p)) { res.writeHead(404); return res.end(); }
  res.writeHead(200, { "content-type": MIME[path.extname(p)] || "application/octet-stream" }); res.end(readFileSync(p));
}).listen(0);
const port = server.address().port;
const outDir = path.join(ROOT, "posts"); mkdirSync(outDir, { recursive: true });
const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: 1080, height: 1350 }, deviceScaleFactor: 1 });
for (let n = 1; n <= 10; n++) {
  await page.goto(`http://127.0.0.1:${port}/posts.html?n=${n}`, { waitUntil: "networkidle" });
  await page.waitForFunction(() => window.READY === true);
  const f = path.join(outDir, `post-${String(n).padStart(2, "0")}.png`);
  await page.screenshot({ path: f });
  console.log("✔", f);
}
await browser.close(); server.close();
