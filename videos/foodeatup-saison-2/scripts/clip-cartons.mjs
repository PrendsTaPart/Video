#!/usr/bin/env node
// Rend les deux cartons du clip musical : HTML déterministe → images → MKV.
//
//   node scripts/clip-cartons.mjs
//
// Produit clip-musical/work/carton-ouverture.mkv et carton-fin.mkv, muets.
// Le son est posé au montage, pas ici : un carton qui porte déjà son son ne se
// recale plus si on change sa durée.
//
// Matroska et non MP4, pour la même raison que le reste de la chaîne du clip :
// le collage final passe par le FILTRE concat, qui remonte l'horloge à partir
// des images. Aucune durée de conteneur n'entre dans le calcul.
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
const WORK = join(ROOT, "clip-musical", "work");
const FPS = 30;

const b64 = (p, mime) => `data:${mime};base64,${readFileSync(p).toString("base64")}`;
const FONT = b64(join(REPO, "studio-video/assets/vendor/fonts/Fredoka-Variable.woff2"), "font/woff2");

// La variante à pastille bleue, et non la mascotte à contour transparent.
// Sur un carton anthracite comme en incrustation au-dessus d'un plan, la
// pastille porte son propre fond : elle reste lisible quel que soit ce qu'il y
// a derrière. La mascotte, elle, disparaît sur un plan clair ou bleu — et la
// charte interdit de lui ajouter un contour pour la rattraper.
const LOGO = b64(join(REPO, "studio-video/assets/brand/logo/foodeatup-logo-horizontal.png"), "image/png");

const CARTONS = [
  {
    nom: "ouverture",
    role: "ouverture",
    images: 105,                       // 3,50 s
    mention: "UN FILM RÉALISÉ PAR",
    credit: "FoodEatUp et Michael",
  },
  {
    nom: "fin",
    role: "fin",
    images: 150,                       // 5,00 s
    titre: "C'est ma maison",
    contexte: "Michael fait son cinéma · saison 2",
    signature: "Le système qui travaille avec vous.",
  },
];

const gabarit = readFileSync(join(ROOT, "clip-musical", "cartons.html"), "utf8");
const browser = await chromium.launch({ executablePath: CHROME, args: ["--no-sandbox", "--force-device-scale-factor=1"] });

for (const c of CARTONS) {
  const frames = join(WORK, `cartons-${c.nom}`);
  rmSync(frames, { recursive: true, force: true });
  mkdirSync(frames, { recursive: true });

  const html = gabarit
    .replace("__FONT__", FONT)
    .replace("__LOGO__", LOGO)
    .replace("__DATA__", JSON.stringify(c));
  const page_html = join(WORK, `carton-${c.nom}.html`);
  writeFileSync(page_html, html);

  const page = await browser.newPage({ viewport: { width: 1080, height: 1920 }, deviceScaleFactor: 1 });
  await page.goto("file://" + page_html);
  await page.evaluate(() => document.fonts.ready);
  for (let f = 0; f < c.images; f++) {
    await page.evaluate((i) => window.seek(i), f);
    await page.screenshot({ path: join(frames, `f${String(f).padStart(4, "0")}.png`) });
  }
  await page.close();

  const sortie = join(WORK, `carton-${c.nom}.mkv`);
  execFileSync("ffmpeg", [
    "-y", "-nostdin", "-loglevel", "error",
    "-framerate", String(FPS), "-i", join(frames, "f%04d.png"),
    "-frames:v", String(c.images),
    "-c:v", "libx264", "-preset", "slow", "-crf", "16", "-pix_fmt", "yuv420p",
    sortie,
  ], { stdio: "inherit" });
  console.log(`   carton ${c.nom} : ${c.images} images (${(c.images / FPS).toFixed(2)} s)`);
}

await browser.close();
console.log("✅ cartons rendus");
