// Chemins, binaires et petites fonctions partagées par les scripts de montage.
import { execFileSync, spawnSync } from "node:child_process";
import { readFileSync, mkdirSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";
import { createRequire } from "node:module";

const require = createRequire(import.meta.url);

export const ROOT = join(dirname(fileURLToPath(import.meta.url)), "..");
const WORK_BASE = join(ROOT, "work");           // intermédiaires, ignorés par git
export const OUT = join(ROOT, "deliverable");
const SOURCE_EP = JSON.parse(readFileSync(join(ROOT, "episode.json"), "utf8"));

/* Une variante ne duplique pas le plan de montage : elle ne redit que ce qui change.
   Le bloc film, les logos, la charte et les contrôles restent les mêmes — seuls les
   créneaux de voix off, la fin du bloc méthode et les exports diffèrent. */
function fondre(base, dessus) {
  if (Array.isArray(dessus) || dessus === null || typeof dessus !== "object") return dessus;
  const res = { ...base };
  for (const [cle, val] of Object.entries(dessus)) {
    res[cle] = cle in base && !Array.isArray(base[cle]) && typeof base[cle] === "object" && base[cle] !== null
      ? fondre(base[cle], val) : val;
  }
  return res;
}

const argv = process.argv.slice(2);
const drapeau = argv.findIndex((a) => a === "--variante");
export const VARIANTE =
  (drapeau >= 0 ? argv[drapeau + 1] : null) ||
  process.env.VARIANTE ||
  SOURCE_EP.variante_par_defaut ||
  "45s";

const declaree = SOURCE_EP.variantes?.[VARIANTE];
if (!declaree) {
  throw new Error(
    `variante « ${VARIANTE} » inconnue — episode.json en déclare : ${Object.keys(SOURCE_EP.variantes ?? {}).join(", ") || "aucune"}.`
  );
}

/* Les créneaux d'une variante ne portent que des instants : le texte des lignes,
   lui, ne change jamais d'une variante à l'autre. */
const surcharge = { ...declaree };
if (surcharge.methode?.lignes) {
  surcharge.methode = {
    ...surcharge.methode,
    lignes: SOURCE_EP.methode.lignes.map((l, i) => ({ ...l, ...surcharge.methode.lignes[i] })),
  };
}
delete surcharge.nom; delete surcharge.note;

export const EP = fondre(SOURCE_EP, surcharge);
EP.variante = { id: VARIANTE, nom: declaree.nom, note: declaree.note };

/* ffmpeg n'est pas installé sur cette machine : le paquet npm ffmpeg-static en fournit
   un complet (libx264 + aac), là où celui livré avec Playwright est amputé de tout. */
export const FFMPEG = process.env.FFMPEG_PATH || require("ffmpeg-static");
export const CHROME = process.env.CHROME_PATH || "/opt/pw-browsers/chromium-1194/chrome-linux/chrome";
export const PLAYWRIGHT = process.env.PLAYWRIGHT_MODULE || "/opt/node22/lib/node_modules/playwright";

export const WORK = join(WORK_BASE, VARIANTE);
export const { largeur: L, hauteur: H, fps: FPS } = EP.format;

export function ff(args, { silencieux = true } = {}) {
  return execFileSync(FFMPEG, ["-y", "-hide_banner", "-loglevel", silencieux ? "error" : "info", ...args], {
    encoding: "utf8",
    maxBuffer: 64 * 1024 * 1024,
  });
}

/* ffprobe n'est pas disponible non plus : ffmpeg écrit ce qu'il faut sur sa sortie d'erreur. */
/* ffmpeg écrit ce qu'il sait d'un fichier sur sa sortie d'erreur, qu'il finisse bien ou mal :
   on la lit dans les deux cas plutôt que de compter sur un code de sortie. */
function stderrDe(args) {
  const r = spawnSync(FFMPEG, ["-hide_banner", ...args], { encoding: "utf8", maxBuffer: 64 * 1024 * 1024 });
  return r.stderr || "";
}

export function sonder(fichier) {
  const sortie = stderrDe(["-i", fichier]);
  const duree = /Duration: (\d+):(\d+):([\d.]+)/.exec(sortie);
  const video = /Video: .*?, (\d+)x(\d+)/.exec(sortie);
  const fps = /, ([\d.]+) fps/.exec(sortie);
  return {
    duree_s: duree ? +duree[1] * 3600 + +duree[2] * 60 + parseFloat(duree[3]) : null,
    largeur: video ? +video[1] : null,
    hauteur: video ? +video[2] : null,
    fps: fps ? parseFloat(fps[1]) : null,
    audio: /Audio: /.test(sortie),
    brut: sortie,
  };
}

/* Les silences d'un fichier, tels que ffmpeg les entend. Sert à découper la passe unique
   de voix off en lignes sans avoir à deviner où elles tombent. */
export function silences(fichier, { seuil_db = 40, duree_min_s = 0.2 } = {}) {
  const sortie = stderrDe(["-i", fichier, "-af", `silencedetect=noise=-${seuil_db}dB:d=${duree_min_s}`, "-f", "null", "-"]);
  const trous = [];
  let debut = null;
  for (const ligne of sortie.split("\n")) {
    const d = /silence_start: ([\d.]+)/.exec(ligne);
    const f = /silence_end: ([\d.]+)/.exec(ligne);
    if (d) debut = parseFloat(d[1]);
    if (f && debut !== null) {
      trous.push({ debut_s: debut, fin_s: parseFloat(f[1]), duree_s: parseFloat(f[1]) - debut });
      debut = null;
    }
  }
  return trous;
}

export const dossiers = (...chemins) => chemins.forEach((c) => mkdirSync(c, { recursive: true }));
export const s2 = (n) => n.toFixed(3);
