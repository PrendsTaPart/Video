#!/usr/bin/env node
// Assemble l'épisode : bloc film (30 s) + bloc méthode (15 s), audio mixé, trois exports
// et la vignette. Ne génère aucune vidéo — les trois plans viennent de source/.
import { existsSync, writeFileSync, readFileSync, rmSync, mkdirSync } from "node:fs";
import { join } from "node:path";
import { createRequire } from "node:module";
import { EP, ROOT, WORK, OUT, CHROME, PLAYWRIGHT, FPS, L, H, ff, sonder, dossiers, s2 } from "./outils.mjs";

const require = createRequire(import.meta.url);
const { chromium } = require(PLAYWRIGHT);

const F = EP.film, M = EP.methode, A = EP.audio;
const INCRUST = join(WORK, "incrustations");
const METHODE_MUET = join(WORK, "methode-muet.mp4");
const VO = join(ROOT, "audio", "vo-methode-calee.wav");
const NAPPE = join(ROOT, "assets", "musique", "nappe-methode.mp3");

for (const [quoi, chemin] of [["le bloc méthode", METHODE_MUET], ["la voix off calée", VO]]) {
  if (!existsSync(chemin)) throw new Error(`manque ${quoi} : ${chemin} — lancer npm run methode et npm run voix d'abord.`);
}

dossiers(WORK, OUT);
rmSync(INCRUST, { recursive: true, force: true });
mkdirSync(INCRUST, { recursive: true });

/* ───────────────────────────── 1. les incrustations ─────────────────────────────
   Accroche et sous-titres sont fixes pendant leur créneau : une image PNG chacun,
   posée par ffmpeg au bon moment, plutôt que 900 images de plus à rendre. */
const Y_ACCROCHE = 1290;     // tiers bas, au-dessus de la zone d'interface des réseaux
const Y_SOUSTITRE = 1440;    // au-dessus de l'étiquette de la bouteille (qui commence à 1532)

const navigateur = await chromium.launch({ executablePath: CHROME, args: ["--no-sandbox", "--force-device-scale-factor=1"] });
const page = await navigateur.newPage({ viewport: { width: L, height: H }, deviceScaleFactor: 1 });
const page_html = join(WORK, "incrustations.html");
writeFileSync(page_html, readFileSync(join(ROOT, "outro", "incrustations.html"), "utf8").replace("__DATA__", JSON.stringify({})));
await page.goto("file://" + page_html);
await page.evaluate(() => document.fonts.ready);

const incrustations = [];
await page.evaluate((a) => window.montrer(a), { type: "accroche", ...F.accroche, y: Y_ACCROCHE });
const fAccroche = join(INCRUST, "accroche.png");
await page.screenshot({ path: fAccroche, omitBackground: true });
incrustations.push({ fichier: fAccroche, debut_s: F.accroche.debut_s, fin_s: F.accroche.fin_s });

for (const [i, st] of F.sous_titres.entries()) {
  if (st.lignes.length > 2) throw new Error(`sous-titre ${i + 1} : ${st.lignes.length} lignes, deux au maximum.`);
  for (const ligne of st.lignes) {
    const mots = ligne.trim().split(/\s+/).length;
    if (mots > 7) throw new Error(`sous-titre ${i + 1} : « ${ligne} » fait ${mots} mots, sept au maximum.`);
  }
  await page.evaluate((s) => window.montrer(s), { type: "soustitre", lignes: st.lignes, y: Y_SOUSTITRE });
  const fichier = join(INCRUST, `st${i + 1}.png`);
  await page.screenshot({ path: fichier, omitBackground: true });
  incrustations.push({ fichier, debut_s: st.debut_s, fin_s: st.fin_s });
}
await navigateur.close();

/* ───────────────────────── 2. l'étiquette de l'annonceur ─────────────────────────
   Si aucune marque n'est fournie, l'étiquette reste vierge : rien n'est incrusté.
   Sinon elle suit la bouteille, sur les trois points relevés par suivre-bouteille.mjs. */
const ET = F.etiquette_annonceur;
const etiquette = existsSync(join(ROOT, ET.fichier)) ? join(ROOT, ET.fichier) : null;
if (!etiquette) console.log(`   étiquette annonceur : aucune marque fournie, la bouteille reste vierge.`);

/* ────────────────────────────── 3. le bloc film ──────────────────────────────
   Les trois plans bout à bout, raccords francs, aucune transition, aucun fondu.
   Les sources sont en 720×1280 à 24 ips : on monte en 1080×1920 à 30 ips. */
const entrees = F.clips.flatMap((c) => ["-i", join(ROOT, c.fichier)]);
const nIncrust = incrustations.length;
const entreesIncrust = incrustations.flatMap((i) => ["-loop", "1", "-i", i.fichier]);
const entreeEtiquette = etiquette ? ["-loop", "1", "-i", etiquette] : [];

const chaine = [];
F.clips.forEach((_, i) => {
  chaine.push(`[${i}:v]scale=${L}:${H}:flags=lanczos,fps=${FPS},setsar=1,format=yuv420p[c${i}]`);
});
chaine.push(`${F.clips.map((_, i) => `[c${i}][${i}:a]`).join("")}concat=n=${F.clips.length}:v=1:a=1[fv][fa]`);

let courant = "fv";
incrustations.forEach((inc, k) => {
  const src = F.clips.length + k;
  const sortie = `o${k}`;
  chaine.push(
    `[${courant}][${src}:v]overlay=0:0:enable='between(t,${s2(inc.debut_s)},${s2(inc.fin_s)})':format=auto[${sortie}]`
  );
  courant = sortie;
});

if (etiquette) {
  /* Suivi linéaire entre les points relevés : la bouteille bouge de trois pixels sur la
     seconde, le plan étant fixe depuis la quatrième — trois points suffisent. */
  const src = F.clips.length + nIncrust;
  const p = ET.suivi;
  const interp = (champ) => {
    const morceaux = [];
    for (let i = 0; i < p.length - 1; i++) {
      const [a, b] = [p[i], p[i + 1]];
      const pente = (b[champ] - a[champ]) / (b.t_s - a.t_s);
      morceaux.push(`if(lt(t,${s2(b.t_s)}), ${a[champ]}+(t-${s2(a.t_s)})*${pente.toFixed(4)}`);
    }
    return morceaux.join(", ") + `, ${p[p.length - 1][champ]}` + ")".repeat(p.length - 1);
  };
  chaine.push(`[${src}:v]scale=${p[0].l}:${p[0].h}[etiq]`);
  chaine.push(
    `[${courant}][etiq]overlay=x='${interp("x")}':y='${interp("y")}':` +
    `enable='between(t,${s2(ET.debut_s)},${s2(ET.fin_s)})'[oe]`
  );
  courant = "oe";
}

const FILM = join(WORK, "film.mp4");
ff([...entrees, ...entreesIncrust, ...entreeEtiquette,
    "-filter_complex", chaine.join(";"),
    "-map", `[${courant}]`, "-map", "[fa]",
    "-t", s2(F.fin_s - F.debut_s),
    "-c:v", "libx264", "-preset", "slow", "-crf", "17", "-pix_fmt", "yuv420p",
    "-c:a", "aac", "-b:a", "256k", "-ar", "48000", FILM]);
console.log(`✅ bloc film — ${sonder(FILM).duree_s} s`);

/* ──────────────────────────── 4. le bloc méthode ────────────────────────────
   Quatre images de noir plein à 30,0 s : la coupe franche entre les deux blocs.
   La nappe démarre à 30,2 s, la voix off est déjà calée sur ses timecodes. */
const noir_s = F.coupe_finale.noir_images / FPS;
const dureeMethode = M.fin_s - M.debut_s;
const nappeDecalage = A.nappe_methode_debut_s - M.debut_s;

const METHODE = join(WORK, "methode.mp4");
ff(["-i", METHODE_MUET, "-i", VO, "-i", NAPPE,
    "-filter_complex", [
      // noir plein sur les premières images
      `[0:v]drawbox=x=0:y=0:w=${L}:h=${H}:color=black@1:t=fill:enable='lt(t,${s2(noir_s)})'[mv]`,
      // la nappe entre à 30,2 s, sous la voix, et se termine avec le bloc
      `[2:a]atrim=0:${s2(dureeMethode - nappeDecalage)},asetpts=PTS-STARTPTS,` +
        `adelay=${Math.round(nappeDecalage * 1000)}:all=1,volume=0.22,` +
        `afade=t=in:st=${s2(nappeDecalage)}:d=0.4[nappe]`,
      // la voix commande : la nappe passe dessous de 6 dB dès qu'il parle
      `[nappe][1:a]sidechaincompress=threshold=0.03:ratio=6:attack=12:release=280:makeup=1[duck]`,
      `[duck][1:a]amix=inputs=2:normalize=0:dropout_transition=0[ma]`,
    ].join(";"),
    "-map", "[mv]", "-map", "[ma]", "-t", s2(dureeMethode),
    "-c:v", "libx264", "-preset", "slow", "-crf", "17", "-pix_fmt", "yuv420p",
    "-c:a", "aac", "-b:a", "256k", "-ar", "48000", METHODE]);
console.log(`✅ bloc méthode — ${sonder(METHODE).duree_s} s`);

/* ──────────────────────────── 5. les trois exports ────────────────────────────
   Le son du film est coupé net à 30,0 s : les deux blocs sont concaténés tels quels,
   sans fondu enchaîné, puis l'ensemble est normalisé à −14 LUFS. */
const liste = join(WORK, "blocs.txt");
writeFileSync(liste, [FILM, METHODE].map((f) => `file '${f}'`).join("\n") + "\n");
const COMPLET = join(WORK, "complet.mp4");
ff(["-f", "concat", "-safe", "0", "-i", liste, "-c", "copy", COMPLET]);

const total = EP.format.duree_s;
for (const ex of EP.exports) {
  const duree = ex.a_s - ex.de_s;
  const sortie = join(OUT, ex.fichier);
  const fondu = A.fondu_sortie_s;
  ff(["-ss", s2(ex.de_s), "-i", COMPLET, "-t", s2(duree),
      "-af", `loudnorm=I=${A.lufs}:TP=-1.5:LRA=11,afade=t=out:st=${s2(duree - fondu)}:d=${fondu}`,
      "-c:v", "libx264", "-preset", "slow", "-crf", "18", "-pix_fmt", "yuv420p",
      "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-movflags", "+faststart", sortie]);
  const i = sonder(sortie);
  console.log(`✅ ${ex.fichier} — ${i.duree_s} s · ${i.largeur}×${i.hauteur} · ${i.fps} ips`);
}

/* ──────────────────────────── 6. la vignette ──────────────────────────── */
const vignette = join(OUT, EP.vignette.fichier);
ff(["-ss", s2(EP.vignette.t_s), "-i", COMPLET, "-frames:v", "1", "-q:v", "2", vignette]);
console.log(`✅ ${EP.vignette.fichier} — image à ${EP.vignette.t_s} s`);
