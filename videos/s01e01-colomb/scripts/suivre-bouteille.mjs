#!/usr/bin/env node
// Relève la position de la bouteille dans la dernière seconde du clip 3, pour que
// l'étiquette de l'annonceur y reste collée. Écrit le suivi dans episode.json.
//
// La bouteille est le seul objet franchement rouge et saturé du bas de l'image : on la
// repère à sa couleur plutôt qu'à l'estime. Le relevé est fait une fois et versionné —
// il décrit un fichier fixe, comme les identifiants Higgsfield des plans.
import { readFileSync, writeFileSync, rmSync, mkdirSync, existsSync } from "node:fs";
import { join } from "node:path";
import { createRequire } from "node:module";
import { EP, ROOT, WORK, FPS, L, H, ff, sonder, dossiers, s2 } from "./outils.mjs";

const require = createRequire(import.meta.url);
const { chromium } = require(process.env.PLAYWRIGHT_MODULE || "/opt/node22/lib/node_modules/playwright");

const ET = EP.film.etiquette_annonceur;
const clip3 = EP.film.clips[2];
const RELEVES = [ET.debut_s, (ET.debut_s + ET.fin_s) / 2, ET.fin_s];
const DIR = join(WORK, "suivi");

dossiers(WORK);
rmSync(DIR, { recursive: true, force: true });
mkdirSync(DIR, { recursive: true });

/* On sort les images en pleine définition de sortie : les coordonnées relevées sont
   directement celles du montage, sans conversion. Le dernier relevé tombe sur la fin
   exacte du clip, où il n'y a plus d'image : on prend la dernière, une image avant. */
const infos = sonder(join(ROOT, clip3.fichier));
const derniere_image_s = infos.duree_s - 2 / (infos.fps || FPS);   // le clip est à 24 ips, la sortie à 30
for (const t of RELEVES) {
  const dans_le_clip = Math.min(t - clip3.debut_s, derniere_image_s);
  const fichier = join(DIR, `t${String(t).replace(".", "_")}.png`);
  ff(["-ss", s2(dans_le_clip), "-i", join(ROOT, clip3.fichier),
      "-frames:v", "1", "-vf", `scale=${L}:${H}:flags=lanczos`, fichier]);
  if (!existsSync(fichier)) {
    throw new Error(`aucune image extraite à ${dans_le_clip.toFixed(3)} s du clip 3 (durée ${infos.duree_s} s).`);
  }
}

const navigateur = await chromium.launch({ executablePath: process.env.CHROME_PATH || "/opt/pw-browsers/chromium-1194/chrome-linux/chrome", args: ["--no-sandbox"] });
const page = await navigateur.newPage({ viewport: { width: 400, height: 300 } });

const suivi = [];
for (const t of RELEVES) {
  const fichier = join(DIR, `t${String(t).replace(".", "_")}.png`);
  const uri = "data:image/png;base64," + readFileSync(fichier).toString("base64");
  const boite = await page.evaluate(async ({ uri, L, H }) => {
    const img = new Image();
    img.src = uri;
    await img.decode();
    const c = document.createElement("canvas");
    c.width = L; c.height = H;
    const ctx = c.getContext("2d", { willReadFrequently: true });
    ctx.drawImage(img, 0, 0);
    // moitié basse seulement : c'est là que vit la bouteille
    const y0 = Math.round(H * 0.55);
    const d = ctx.getImageData(0, y0, L, H - y0).data;
    let xmin = L, xmax = 0, ymin = H, ymax = 0, n = 0;
    for (let i = 0; i < d.length; i += 4) {
      const r = d[i], g = d[i + 1], b = d[i + 2];
      const max = Math.max(r, g, b), min = Math.min(r, g, b);
      const sat = max === 0 ? 0 : (max - min) / max;
      // rouge dominant, franchement saturé, pas dans l'ombre
      if (r > 105 && r > g * 1.55 && r > b * 1.55 && sat > 0.45) {
        const p = i / 4;
        const x = p % L, y = y0 + Math.floor(p / L);
        if (x < xmin) xmin = x; if (x > xmax) xmax = x;
        if (y < ymin) ymin = y; if (y > ymax) ymax = y;
        n++;
      }
    }
    return { xmin, xmax, ymin, ymax, n };
  }, { uri, L, H });

  if (boite.n < 4000) {
    throw new Error(`à ${t} s : seulement ${boite.n} pixels rouges trouvés — la bouteille n'est pas repérable, le suivi serait faux.`);
  }
  /* L'étiquette occupe la partie basse et large du corps : sous l'épaule, sur toute la
     largeur du verre, moins une marge de courbure. */
  const largeurVerre = boite.xmax - boite.xmin;
  const marge = Math.round(largeurVerre * 0.1);
  suivi.push({
    t_s: t,
    x: boite.xmin + marge,
    y: Math.round(boite.ymin + (boite.ymax - boite.ymin) * 0.52),
    l: largeurVerre - 2 * marge,
    h: Math.round((boite.ymax - boite.ymin) * 0.33),
    bouteille: { x: boite.xmin, y: boite.ymin, l: largeurVerre, h: boite.ymax - boite.ymin, pixels: boite.n },
  });
}
await navigateur.close();

const ep = JSON.parse(readFileSync(join(ROOT, "episode.json"), "utf8"));
ep.film.etiquette_annonceur.suivi = suivi;
writeFileSync(join(ROOT, "episode.json"), JSON.stringify(ep, null, 2) + "\n");

console.log("✅ suivi de la bouteille relevé et écrit dans episode.json");
for (const s of suivi) {
  const b = s.bouteille;
  console.log(`   ${s.t_s}s · verre ${b.l}×${b.h} en (${b.x},${b.y}) — étiquette ${s.l}×${s.h} en (${s.x},${s.y})`);
  if (s.y + s.h > H) console.log(`      ⚠️  l'étiquette sort du cadre par le bas de ${s.y + s.h - H} px`);
}
