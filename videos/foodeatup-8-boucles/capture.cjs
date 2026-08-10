/* Capture déterministe d'une composition en PNG, frame par frame.
 *
 * Repris de videos/boucle-stockvision/capture.cjs (même moteur pour toute la
 * série), avec deux ajouts : le mode `--frames` pour n'extraire que quelques
 * images de contrôle sans rendre la vidéo entière, et l'attente explicite de
 * document.fonts.ready (sans quoi la première seconde sort en police système).
 *
 * Usage :
 *   node capture.cjs --html 01-.../index.html --out work/frames --fps 30 --duree 82
 *   node capture.cjs --html 01-.../index.html --out work/qa --at 3,25,48,70
 */
const path = require("path");
const fs = require("fs");

function arg(nom, def) {
  const i = process.argv.indexOf("--" + nom);
  return i >= 0 && i + 1 < process.argv.length ? process.argv[i + 1] : def;
}

(async () => {
  const groot = process.env.GROOT || require("child_process")
    .execSync("npm root -g").toString().trim();
  const { chromium } = require(path.join(groot, "playwright"));

  const html = path.resolve(arg("html"));
  const out = path.resolve(arg("out", "work/frames"));
  const fps = parseInt(arg("fps", "30"), 10);
  const at = arg("at", null);
  fs.mkdirSync(out, { recursive: true });

  const nav = await chromium.launch({ args: ["--no-sandbox", "--force-color-profile=srgb"] });
  const page = await nav.newPage({ deviceScaleFactor: 1 });
  await page.goto("file://" + html);

  // La taille de scène est portée par la composition elle-même (--W/--H).
  const dim = await page.evaluate(() => ({ w: window.__VIDEO.W, h: window.__VIDEO.H }));
  await page.setViewportSize({ width: dim.w, height: dim.h });
  await page.evaluate(async () => { await document.fonts.ready; });

  const duree = parseFloat(arg("duree", "0")) || await page.evaluate(() => window.__duree);
  const clip = { x: 0, y: 0, width: dim.w, height: dim.h };

  if (at) {
    // Mode contrôle : quelques instants précis, nommés par leur timestamp.
    for (const s of at.split(",")) {
      const t = parseFloat(s);
      await page.evaluate((x) => window.render(x), t);
      await page.screenshot({ path: path.join(out, `t${s}.png`), clip });
      console.log("qa t=" + s);
    }
  } else {
    const n = Math.round(duree * fps);
    for (let i = 0; i < n; i++) {
      await page.evaluate((x) => window.render(x), i / fps);
      await page.screenshot({
        path: path.join(out, `f${String(i).padStart(5, "0")}.png`), clip,
      });
      if (i % 300 === 0) console.log(`frame ${i}/${n}`);
    }
    console.log("DONE " + n + " frames");
  }
  await nav.close();
})().catch((e) => { console.error(e); process.exit(1); });
