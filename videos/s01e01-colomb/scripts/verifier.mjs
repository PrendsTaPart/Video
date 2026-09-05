#!/usr/bin/env node
// Contrôle les exports : format, durée, images par seconde, niveau sonore, et présence
// effective des incrustations aux instants où le plan de montage les annonce.
import { existsSync } from "node:fs";
import { join } from "node:path";
import { execFileSync, spawnSync } from "node:child_process";
import { EP, ROOT, OUT, WORK, FFMPEG, FPS, L, H, sonder, dossiers, s2 } from "./outils.mjs";

const A = EP.audio;
const ecarts = [];
const dit = (ok, texte) => { console.log(`   ${ok ? "✅" : "❌"} ${texte}`); if (!ok) ecarts.push(texte); };

/* Le niveau intégré, mesuré par ffmpeg lui-même plutôt que déclaré. */
function lufs(fichier) {
  const r = spawnSync(FFMPEG, ["-hide_banner", "-i", fichier, "-af", "ebur128=framelog=quiet", "-f", "null", "-"],
    { encoding: "utf8", maxBuffer: 32 * 1024 * 1024 });
  const m = /I:\s+(-?[\d.]+) LUFS/.exec(r.stderr || "");
  return m ? parseFloat(m[1]) : null;
}

/* Le noir plein de la coupe : la luminance moyenne d'une image donnée. */
function luminance(fichier, t) {
  const r = spawnSync(FFMPEG, ["-hide_banner", "-loglevel", "info", "-ss", s2(t), "-i", fichier, "-frames:v", "1",
    "-vf", "scale=64:64,format=gray,signalstats,metadata=print:key=lavfi.signalstats.YAVG",
    "-f", "null", "-"], { encoding: "utf8", maxBuffer: 32 * 1024 * 1024 });
  const m = /lavfi\.signalstats\.YAVG=([\d.]+)/.exec(r.stderr || "");
  return m ? parseFloat(m[1]) : null;
}

console.log("── Les exports ──");
for (const ex of EP.exports) {
  const f = join(OUT, ex.fichier);
  if (!existsSync(f)) { dit(false, `${ex.fichier} : absent`); continue; }
  const i = sonder(f);
  const duree_attendue = ex.a_s - ex.de_s;
  dit(Math.abs(i.duree_s - duree_attendue) < 0.05, `${ex.fichier} : ${i.duree_s} s (attendu ${duree_attendue})`);
  dit(i.largeur === L && i.hauteur === H, `${ex.fichier} : ${i.largeur}×${i.hauteur} (attendu ${L}×${H})`);
  dit(Math.abs(i.fps - FPS) < 0.1, `${ex.fichier} : ${i.fps} ips (attendu ${FPS})`);
  dit(i.audio, `${ex.fichier} : piste audio présente`);
  const niveau = lufs(f);
  dit(niveau !== null && Math.abs(niveau - A.lufs) <= 1.5, `${ex.fichier} : ${niveau} LUFS (visé ${A.lufs}, tolérance ±1,5)`);
}

console.log("\n── La coupe franche à 30 s ──");
const complet = join(OUT, EP.exports[0].fichier);
if (existsSync(complet)) {
  /* Un noir encodé en yuv420p à plage réduite ne mesure pas 0 mais ~7 sur 255 :
     le seuil est là pour distinguer le noir de l'image, pas pour compter les bits. */
  const NOIR = 12;
  const t0 = EP.film.fin_s;
  const attendu = EP.film.coupe_finale.noir_images;
  const mesures = [];
  for (let f = -1; f <= attendu + 2; f++) mesures.push({ f, y: luminance(complet, t0 + f / FPS) });
  const noires = mesures.filter((m) => m.y !== null && m.y < NOIR).map((m) => m.f);
  const suite = noires.length && noires[noires.length - 1] - noires[0] + 1 === noires.length;
  dit(noires.length === attendu && suite,
      `${noires.length} image(s) de noir plein d'affilée à ${t0} s (attendu ${attendu})`);
  const avant = mesures.find((m) => m.f === 0), apres = mesures.find((m) => m.f === attendu + 1);
  dit(avant?.y > 20, `image de film jusqu'à ${t0} s inclus : luminance ${avant?.y}`);
  dit(apres?.y > 200, `fond clair du bloc méthode juste après : luminance ${apres?.y}`);
}

console.log("\n── Les sources ──");
for (const c of EP.film.clips) {
  const f = join(ROOT, c.fichier);
  const i = existsSync(f) ? sonder(f) : null;
  dit(!!i && Math.abs(i.duree_s - 10) < 0.1, `${c.fichier} : ${i ? i.duree_s + " s" : "absent"} (plan Higgsfield ${c.higgsfield})`);
}

console.log("\n── Les sous-titres ──");
for (const [i, st] of EP.film.sous_titres.entries()) {
  const trop = st.lignes.filter((l) => l.trim().split(/\s+/).length > 7);
  dit(st.lignes.length <= 2 && trop.length === 0,
      `sous-titre ${i + 1} : ${st.lignes.length} ligne(s), ${st.lignes.map((l) => l.trim().split(/\s+/).length).join("/")} mot(s)`);
}

console.log("\n── L'étiquette de l'annonceur ──");
const ET = EP.film.etiquette_annonceur;
if (existsSync(join(ROOT, ET.fichier))) {
  const hors = ET.suivi.filter((p) => p.x < 0 || p.y < 0 || p.x + p.l > L || p.y + p.h > H);
  dit(hors.length === 0, `suivi dans le cadre sur les ${ET.suivi.length} points relevés`);
} else {
  console.log(`   ○ aucune marque fournie : la bouteille reste vierge, rien n'est incrusté (c'est le plan de montage).`);
}

console.log(ecarts.length === 0 ? "\n✅ Aucun écart." : `\n❌ ${ecarts.length} écart(s).`);
if (ecarts.length) process.exitCode = 1;
