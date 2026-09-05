#!/usr/bin/env node
// Rend le bloc méthode + orchestration (30 → 45 s) : HTML déterministe → 450 images → MP4 muet.
// Usage : node scripts/rendre-methode.mjs [--apercu 41.5,43.2]
import { readFileSync, writeFileSync, rmSync, mkdirSync } from "node:fs";
import { join } from "node:path";
import { createRequire } from "node:module";
import { EP, ROOT, WORK, CHROME, PLAYWRIGHT, FPS, L, H, ff, dossiers } from "./outils.mjs";

const require = createRequire(import.meta.url);
const { chromium } = require(PLAYWRIGHT);

const M = EP.methode;
const DEBUT = M.debut_s, FIN = M.fin_s;
const IMAGES = Math.round((FIN - DEBUT) * FPS);
const IMAGES_DIR = join(WORK, "methode-images");
const MUET = join(WORK, "methode-muet.mp4");

const apercuArg = process.argv.find((a) => a.startsWith("--apercu"));
const apercus = apercuArg ? (apercuArg.split("=")[1] || process.argv[process.argv.indexOf(apercuArg) + 1] || "").split(",").map(Number) : null;

/* Les logos sont incorporés en data: URI — la page est ouverte en file:// et doit se
   suffire à elle-même, comme les gabarits d'outro du reste du dépôt. */
const b64 = (rel, mime) => `data:${mime};base64,${readFileSync(join(ROOT, rel)).toString("base64")}`;
const svg = (rel) => readFileSync(join(ROOT, "assets/logos", rel), "utf8");

const logos = {
  rapidocms: b64("assets/logos/rapidocms.png", "image/png"),
  higgsfield: b64("assets/logos/higgsfield.png", "image/png"),
  heygen: b64("assets/logos/heygen.png", "image/png"),
  claude: "data:image/svg+xml;base64," + Buffer.from(teinter(svg("claude.svg"), "#D97757")).toString("base64"),
  elevenlabs: "data:image/svg+xml;base64," + Buffer.from(teinter(svg("elevenlabs.svg"), "#000000")).toString("base64"),
};

/* Simple Icons livre des tracés monochromes sans couleur : on pose celle de la marque
   sur le SVG plutôt que de le redessiner. */
function teinter(source, couleur) {
  return source.replace("<svg ", `<svg fill="${couleur}" `);
}

const creneaux = M.lignes.filter((l) => l.ecran === "etape").map((l) => ({ debut_s: l.debut_s, fin_s: l.fin_s }));
if (creneaux.length !== M.etapes.length) {
  throw new Error(`${creneaux.length} créneaux de voix off pour ${M.etapes.length} cartes d'étape — episode.json est incohérent.`);
}

const donnees = {
  fps: FPS, frames: IMAGES, debut_s: DEBUT, fin_s: FIN,
  etapes: M.etapes, creneaux, orchestration: M.orchestration,
  logos,
  reseaux_svg: Object.fromEntries(M.orchestration.reseaux.map((n) => [n, svg(`${n}.svg`)])),
  couleurs_reseaux: EP.charte.reseaux,
};

dossiers(WORK);
rmSync(IMAGES_DIR, { recursive: true, force: true });
mkdirSync(IMAGES_DIR, { recursive: true });

const page_html = join(WORK, "methode.html");
writeFileSync(page_html, readFileSync(join(ROOT, "outro", "methode.html"), "utf8").replace("__DATA__", JSON.stringify(donnees)));

const navigateur = await chromium.launch({ executablePath: CHROME, args: ["--no-sandbox", "--force-device-scale-factor=1"] });
const page = await navigateur.newPage({ viewport: { width: L, height: H }, deviceScaleFactor: 1 });
const erreurs = [];
page.on("pageerror", (e) => erreurs.push(String(e)));
await page.goto("file://" + page_html);
await page.evaluate(() => document.fonts.ready);
if (erreurs.length) throw new Error(`la page du bloc méthode lève une erreur : ${erreurs.join(" | ")}`);

if (apercus) {
  for (const t of apercus) {
    const f = Math.round((t - DEBUT) * FPS);
    await page.evaluate((i) => window.seek(i), f);
    const fichier = join(WORK, `apercu-${String(t).replace(".", "s")}.png`);
    await page.screenshot({ path: fichier });
    console.log(`   aperçu ${t}s → ${fichier}`);
  }
  await navigateur.close();
  process.exit(0);
}

for (let f = 0; f < IMAGES; f++) {
  await page.evaluate((i) => window.seek(i), f);
  await page.screenshot({ path: join(IMAGES_DIR, `f${String(f).padStart(4, "0")}.png`) });
  if (f % 90 === 0) process.stdout.write(`   ${f}/${IMAGES}\n`);
}
if (erreurs.length) throw new Error(`la page du bloc méthode a levé une erreur pendant le rendu : ${erreurs.join(" | ")}`);
await navigateur.close();

ff(["-framerate", String(FPS), "-i", join(IMAGES_DIR, "f%04d.png"),
    "-c:v", "libx264", "-preset", "slow", "-crf", "16", "-pix_fmt", "yuv420p", MUET]);
console.log(`✅ ${MUET} — ${IMAGES} images à ${FPS} ips`);
