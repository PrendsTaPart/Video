#!/usr/bin/env node
/**
 * quai-monter.mjs — assemble un plan de la série B « Le Quai » à partir du
 * gabarit _gabarit-quai/ et le rend en deux sorties (film + social).
 *
 * CE QUE CE SCRIPT FAIT (déterministe, aucun réseau, aucune horloge) :
 *   1. lit videos/{slug}/quai.config.json
 *   2. vérifie assets/video/plan.mp4 (ffprobe : 10s ± 0.3, 720x1280)
 *   3. vérifie assets/voice/vo.wav (durée ≤ 6.0s, sinon ARRÊT explicite)
 *   4. copie les fichiers du gabarit dans videos/{slug}/ (idempotent — ne
 *      touche jamais un fichier déjà présent hors des cibles de gabarit)
 *   5. injecte les valeurs de quai.config.json + caption_groups.json dans
 *      index-film.html / index-social.html / compositions/*.html — par
 *      remplacement de jetons uniques (__QUAI_...__), jamais d'édition
 *      manuelle
 *   6. génère {slug}.vtt depuis caption_groups.json
 *   7. rend index-film.html puis index-social.html (npx hyperframes render)
 *   8. contrôle les deux rendus (dimensions, durées 10.0s/12.0s, piste
 *      audio non silencieuse)
 *
 * CE QUE CE SCRIPT NE FAIT PAS — parce qu'il n'a pas accès aux outils MCP
 * du studio (ceux-ci ne sont exposés qu'à l'agent Claude dans la
 * conversation, jamais à un processus Node autonome) :
 *   - appeler obtenir_episode, enregistrer_script_voix, demander_url_televersement,
 *     enregistrer_master (studio Plani't) — l'agent les appelle directement
 *   - synthétiser la voix ElevenLabs et transcrire au mot — l'agent les
 *     appelle directement, avec le voice_id figé dans
 *     references/planit-brand.md, puis écrit assets/voice/vo.wav et
 *     caption_groups.json avant de lancer ce script
 *   - télécharger le plan depuis son adresse (Drive, etc.) — l'agent le
 *     fait puis écrit assets/video/plan.mp4 avant de lancer ce script
 *
 * Autrement dit : l'agent orchestre (appels MCP), ce script assemble et
 * rend (déterministe, rejouable). C'est ce qui garantit « deux exécutions
 * sur le même épisode donnent le même résultat ».
 *
 * Usage :
 *   node scripts/quai-monter.mjs <chemin-du-dossier-episode>
 *
 * Pré-requis dans ce dossier avant de lancer le script :
 *   quai.config.json          (rempli avec les vraies données du studio)
 *   assets/video/plan.mp4     (le plan source téléchargé)
 *   assets/voice/vo.wav       (la voix off synthétisée)
 *   caption_groups.json       (transcription au mot, groupée par le worker
 *                              qui a appelé ElevenLabs — un groupe = une
 *                              ligne à l'écran, jamais de virgule/point/
 *                              points de suspension en fin de groupe)
 */

import { existsSync, mkdirSync, readFileSync, writeFileSync, cpSync, readdirSync, statSync } from "node:fs";
import { execFileSync } from "node:child_process";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const GABARIT_DIR = __dirname.endsWith(path.join("scripts")) ? path.dirname(__dirname) : __dirname;

const FILM_DURATION = 10.0;
const SOCIAL_DURATION = 12.0;
const VOICE_START = 1.0;
const VOICE_MAX_DURATION = 6.0;
const DURATION_TOLERANCE = 0.3;

function die(message) {
  console.error(`\n✗ ARRÊT — ${message}\n`);
  process.exit(1);
}

function ok(message) {
  console.log(`✓ ${message}`);
}

function dbToLinear(db) {
  return Math.pow(10, db / 20);
}

function ffprobeJson(file, args) {
  const out = execFileSync("ffprobe", ["-v", "error", "-print_format", "json", ...args, file], {
    encoding: "utf8",
  });
  return JSON.parse(out);
}

function probeVideo(file) {
  const data = ffprobeJson(file, [
    "-select_streams",
    "v:0",
    "-show_entries",
    "stream=width,height,r_frame_rate:format=duration",
  ]);
  const stream = data.streams?.[0] || {};
  const duration = Number(data.format?.duration || 0);
  return { width: stream.width, height: stream.height, duration };
}

function probeAudioDuration(file) {
  const data = ffprobeJson(file, ["-show_entries", "format=duration"]);
  return Number(data.format?.duration || 0);
}

function meanVolumeDb(file, start, dur) {
  const args = ["-v", "error"];
  if (start != null) args.push("-ss", String(start));
  if (dur != null) args.push("-t", String(dur));
  args.push("-i", file, "-af", "volumedetect", "-f", "null", "-");
  let out;
  try {
    execFileSync("ffmpeg", args, { encoding: "utf8" });
    out = "";
  } catch (e) {
    // ffmpeg -f null writes stats to stderr and exits 0 normally; if it
    // threw, stderr is still on the error object
    out = e.stderr ? e.stderr.toString() : "";
  }
  const m = out.match(/mean_volume:\s*(-?[\d.]+)\s*dB/);
  return m ? Number(m[1]) : null;
}

function readConfig(episodeDir) {
  const configPath = path.join(episodeDir, "quai.config.json");
  if (!existsSync(configPath)) die(`quai.config.json introuvable dans ${episodeDir}`);
  const config = JSON.parse(readFileSync(configPath, "utf8"));
  for (const field of ["id", "slug", "acte", "plan", "epoque", "titre", "voix", "planSource", "ambianceDb"]) {
    if (config[field] === undefined || config[field] === null || config[field] === "") {
      die(`quai.config.json : champ "${field}" manquant ou vide`);
    }
  }
  return config;
}

function checkPlanSource(episodeDir, config) {
  const planPath = path.join(episodeDir, config.planSource);
  if (!existsSync(planPath)) die(`plan source introuvable : ${config.planSource}`);
  const { width, height, duration } = probeVideo(planPath);
  if (width !== 720 || height !== 1280) {
    die(`plan source ${width}x${height} — attendu 720x1280`);
  }
  if (Math.abs(duration - FILM_DURATION) > DURATION_TOLERANCE) {
    die(`plan source ${duration.toFixed(2)}s — attendu 10s ± ${DURATION_TOLERANCE}s`);
  }
  ok(`plan source : ${width}x${height}, ${duration.toFixed(2)}s`);
  return duration;
}

function checkVoice(episodeDir) {
  const voicePath = path.join(episodeDir, "assets", "voice", "vo.wav");
  if (!existsSync(voicePath)) die(`voix off introuvable : assets/voice/vo.wav`);
  const duration = probeAudioDuration(voicePath);
  if (duration > VOICE_MAX_DURATION) {
    die(
      `la voix off dure ${duration.toFixed(2)}s, au-delà des ${VOICE_MAX_DURATION}s autorisées. ` +
        `La phrase est trop longue : il faut la raccourcir dans le script (enregistrer_script_voix), ` +
        `pas accélérer la synthèse.`
    );
  }
  ok(`voix off : ${duration.toFixed(2)}s (≤ ${VOICE_MAX_DURATION}s)`);
  return duration;
}

/** Copie les fichiers du gabarit dans le dossier épisode, sans jamais
 * écraser assets/video/, assets/voice/, quai.config.json, ni
 * caption_groups.json (déjà fournis par l'agent avant l'appel). */
function scaffold(episodeDir) {
  mkdirSync(episodeDir, { recursive: true });
  const skip = new Set(["assets", "quai.config.json", "caption_groups.json", "renders", "deliverable", ".git"]);
  for (const entry of readdirSync(GABARIT_DIR)) {
    if (skip.has(entry)) continue;
    const src = path.join(GABARIT_DIR, entry);
    const dst = path.join(episodeDir, entry);
    if (!existsSync(dst)) {
      cpSync(src, dst, { recursive: true });
    }
  }
  // assets/ : copier fonts/vendor/brand (jamais video/voice, propres à l'épisode)
  for (const sub of ["fonts", "vendor", "brand", "sfx"]) {
    const src = path.join(GABARIT_DIR, "assets", sub);
    const dst = path.join(episodeDir, "assets", sub);
    if (existsSync(src) && !existsSync(dst)) cpSync(src, dst, { recursive: true });
  }
  mkdirSync(path.join(episodeDir, "assets", "video"), { recursive: true });
  mkdirSync(path.join(episodeDir, "assets", "voice"), { recursive: true });
  ok(`fichiers du gabarit en place dans ${episodeDir}`);
}

/** Remplace les jetons __QUAI_..._​_ dans un template lu depuis le gabarit,
 * puis écrit le résultat dans le dossier épisode. Ne modifie jamais le
 * gabarit lui-même. */
function injectTokensToFile(relPath, episodeDir, tokens) {
  let content = readFileSync(path.join(GABARIT_DIR, relPath), "utf8");
  for (const [token, value] of Object.entries(tokens)) {
    content = content.split(token).join(String(value));
  }
  writeFileSync(path.join(episodeDir, relPath), content, "utf8");
}

function loadCaptionGroups(episodeDir) {
  const p = path.join(episodeDir, "caption_groups.json");
  if (!existsSync(p)) return [];
  const groups = JSON.parse(readFileSync(p, "utf8"));
  for (const g of groups) {
    const text = String(g.text || "");
    if (/[.,…]\s*$/.test(text.trim())) {
      die(`caption_groups.json : le groupe "${text}" se termine par une ponctuation interdite (. , …)`);
    }
  }
  return groups;
}

function genVtt(groups, outPath) {
  function ts(t) {
    const ms = Math.round((t % 1) * 1000);
    const s = Math.floor(t) % 60;
    const m = Math.floor(t / 60) % 60;
    const h = Math.floor(t / 3600);
    const pad = (n, w = 2) => String(n).padStart(w, "0");
    return `${pad(h)}:${pad(m)}:${pad(s)}.${pad(ms, 3)}`;
  }
  let vtt = "WEBVTT\n\n";
  groups.forEach((g, i) => {
    vtt += `${i + 1}\n${ts(g.start)} --> ${ts(g.end)}\n${g.text}\n\n`;
  });
  writeFileSync(outPath, vtt, "utf8");
  ok(`sous-titres .vtt générés (${groups.length} groupes)`);
}

function assemble(episodeDir, config) {
  const voiceDuration = checkVoice(episodeDir);
  const groups = loadCaptionGroups(episodeDir);
  const groupsLiteral = JSON.stringify(groups);

  const commonTokens = {
    __QUAI_PLAN_SRC__: config.planSource,
    __QUAI_AMBIANCE_VOLUME__: dbToLinear(config.ambianceDb).toFixed(6),
    __QUAI_VOICE_SRC__: "assets/voice/vo.wav",
    __QUAI_VOICE_DURATION__: voiceDuration.toFixed(6),
  };

  injectTokensToFile("index-film.html", episodeDir, commonTokens);
  injectTokensToFile("index-social.html", episodeDir, commonTokens);
  injectTokensToFile("compositions/cartouche-date.html", episodeDir, { __QUAI_EPOQUE__: config.epoque });

  // sous-titres.html : remplace littéralement la ligne `var GROUPS = [];`
  let subs = readFileSync(path.join(GABARIT_DIR, "compositions", "sous-titres.html"), "utf8");
  subs = subs.replace("var GROUPS = [];", `var GROUPS = ${groupsLiteral};`);
  writeFileSync(path.join(episodeDir, "compositions", "sous-titres.html"), subs, "utf8");

  genVtt(groups, path.join(episodeDir, `${config.slug}.vtt`));
  ok("jetons injectés dans index-film.html, index-social.html et les compositions");
}

function render(episodeDir, entry, outName) {
  console.log(`\n… rendu de ${entry}`);
  execFileSync(
    "npx",
    ["hyperframes", "render", ".", "-c", entry, "-o", `renders/${outName}`],
    { cwd: episodeDir, stdio: "inherit" }
  );
  const outPath = path.join(episodeDir, "renders", outName);
  if (!existsSync(outPath)) die(`rendu manquant : ${outName}`);
  return outPath;
}

function validateRender(file, expectedDuration, label) {
  const { width, height, duration } = probeVideo(file);
  if (width !== 720 || height !== 1280) die(`${label} : ${width}x${height} — attendu 720x1280`);
  if (Math.abs(duration - expectedDuration) > 0.1) {
    die(`${label} : durée ${duration.toFixed(2)}s — attendu ${expectedDuration.toFixed(1)}s`);
  }
  const mean = meanVolumeDb(file);
  if (mean === null || mean < -90) {
    die(`${label} : piste audio silencieuse (mean_volume ${mean})`);
  }
  ok(`${label} : ${width}x${height}, ${duration.toFixed(2)}s, audio ${mean.toFixed(1)}dB`);
  return { width, height, duration, sizeBytes: statSync(file).size };
}

function main() {
  const episodeDir = process.argv[2];
  if (!episodeDir) die("usage : node scripts/quai-monter.mjs <chemin-du-dossier-episode>");
  const resolvedDir = path.resolve(episodeDir);

  const config = readConfig(resolvedDir);
  console.log(`\n== ${config.slug} (acte ${config.acte}, plan ${config.plan}) ==`);

  scaffold(resolvedDir);
  checkPlanSource(resolvedDir, config);
  assemble(resolvedDir, config);

  const filmPath = render(resolvedDir, "index-film.html", "film.mp4");
  const socialPath = render(resolvedDir, "index-social.html", "social.mp4");

  const filmStats = validateRender(filmPath, FILM_DURATION, "index-film.html");
  const socialStats = validateRender(socialPath, SOCIAL_DURATION, "index-social.html");

  console.log("\n== Résumé ==");
  console.table({
    "film.mp4": { ...filmStats, sizeMB: (filmStats.sizeBytes / 1e6).toFixed(1) },
    "social.mp4": { ...socialStats, sizeMB: (socialStats.sizeBytes / 1e6).toFixed(1) },
  });
  console.log(`\nProchaine étape (agent) : téléverser ${filmPath} et ${socialPath} sur le studio`);
  console.log("(demander_url_televersement + confirmer_televersement + enregistrer_master).");
}

main();
