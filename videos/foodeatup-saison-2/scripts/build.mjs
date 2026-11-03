#!/usr/bin/env node
// Génère, depuis la source de vérité (saison.json + episodes/*.json) :
//   prompts/ep{NN}-{slug}.md   — fiche prête à coller (2 prompts Seedance + directive montage)
//   episodes.json              — index fusionné, lisible par les outils
//   SAISON-2-EPISODES.md       — récapitulatif des 30 épisodes
//   voix-off/vo-saison-2.md / .json — les 30 phrases de voix off (batch ElevenLabs)
//   RAPPORT-CONTROLES.md       — contrôles automatiques (modules, marque, lexique, durée VO)
import { readFileSync, writeFileSync, readdirSync, mkdirSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const ROOT = join(dirname(fileURLToPath(import.meta.url)), "..");
const S = JSON.parse(readFileSync(join(ROOT, "saison.json"), "utf8"));
const EPISODES = readdirSync(join(ROOT, "episodes"))
  .filter((f) => f.endsWith(".json"))
  .sort()
  .flatMap((f) => JSON.parse(readFileSync(join(ROOT, "episodes", f), "utf8")))
  .sort((a, b) => a.num - b.num);

const NN = (n) => String(n).padStart(2, "0");
const CPS = 17.5;         // caractères/seconde, mesuré sur les 4 premières lignes ElevenLabs (16,3 à 19,1)
const FENETRE_VO_S = 6.4; // la voix de l'épisode démarre à 4,6 s et finit avant 11,0 s

/* ------------------------------------------------------------------ prompts */
function promptSeedance(ep, sc) {
  const refExtra = sc.ref_extra ? ` + ${sc.ref_extra}` : "";
  return [
    `REF: ${S.prompt.ref_michael}${refExtra}, ${S.prompt.ref_suffixe} ${sc.location_line}`,
    `FORMAT: ${sc.format_line}`,
    `SCENE: ${sc.scene}`,
    `ACTION:`,
    ...sc.action.map((a) => `${a.t}: ${a.texte}`),
    `${S.prompt.dialogue_prefixe} ${sc.dialogue}`,
    `CAMERA: ${sc.camera}`,
    `LIGHT & GRADE: ${sc.light}`,
    `AUDIO: ${sc.audio}`,
    S.prompt.bloc_final,
  ].join("\n");
}

function directiveMontage(ep) {
  const n = NN(ep.num);
  return `Tu es motion designer. Crée avec Remotion (React) une composition verticale 1080×1920, 30 fps,
300 images (10 s), export MP4 H.264, fichier ep${n}-outro.mp4.

Entrées dans ./assets :
- logo-foodeatup.svg : logo officiel. Ne jamais le redessiner, le déformer, le recolorer, le rogner.
  Zone de protection = 10 % de sa largeur.
- palette.json : couleurs officielles de la charte FoodEatUp (exportées du CMS). Seules couleurs
  autorisées, aucune couleur inventée.
- scene2-last-frame.png : dernière image de la scène Seedance 2 (extraite avec ffmpeg).
- vo.mp3 : voix off de l'épisode (ElevenLabs, même voix sur toute la saison).
- sfx/ : clap.wav, whoosh.wav, tick.wav, impact.wav.

STRUCTURE IMPOSÉE (identique sur les 30 épisodes — c'est la signature de la saison) :
${S.outro.structure.map((s) => `${s.t} : ${s.contenu}`).join("\n")}
${ep.final_saison ? "\nFINAL DE SAISON : le découpage ci-dessous REMPLACE la structure imposée (le clap reste à 0,4 s,\nle logo reste seul de 9 à 10 s).\n" : ""}
TRANSITION (identique sur les 30 épisodes, ne pas la réinventer) :
Texte à l'écran de 2,0 à 3,8 s, sur le plan figé qui finit de se désaturer : « ${S.transition.texte} »
Voix off de la transition calée à ${String(S.transition.cale_s).replace(".", ",")} s — une seule prise ElevenLabs sert les 30 épisodes.
Puis « Dans la vraie vie… » à 3,6 s et fondu vers l'animation à 3,9 s.

CONTENU DE CET ÉPISODE :
${ep.montage.beats.map((b) => `${b.t} : ${b.texte}`).join("\n")}
Modules affichés en cartes${ep.final_saison ? "" : " (7–9 s)"} : ${ep.montage.cartes.join(" · ")}
Texte à l'écran${ep.montage.texte_ecran_timing ? ` (${ep.montage.texte_ecran_timing})` : ""} : « ${ep.montage.texte_ecran} »
Voix off de l'épisode (démarre à 4,6 s, finie avant 11,0 s) : « ${ep.montage.vo} »
SFX : ${ep.montage.sfx}

RÈGLES : ${S.outro.regles.join(" ")}

SORTIES : ${S.outro.sorties.map((s) => s.replace("{NN}", n)).join(" · ")}
Titre de la miniature : « ${ep.titre} ».`;
}

function ficheEpisode(ep) {
  const n = NN(ep.num);
  const sel = ep.selecteurs;
  const L = [];
  L.push(`# ÉPISODE ${n} — « ${ep.titre.toUpperCase()} »`, "");
  L.push(`🎬 **Genre** : ${ep.genre}`);
  L.push(`🍽️ **Situation** : ${ep.situation}`);
  L.push(`⚙️ **Module** : ${ep.modules.join(" + ")}`);
  L.push(`🎯 **Hook (0–2 s)** : ${ep.hook}`, "");
  L.push(`## Sélecteurs Higgsfield`, "");
  L.push(`| Époque | Genre | Lumière | Physique | Objectif | Émotion | Montage |`);
  L.push(`|---|---|---|---|---|---|---|`);
  L.push(`| ${sel.epoque} | ${sel.genre} | ${sel.lumiere} | ${sel.physique} | ${sel.objectif} | ${sel.emotion} | ${sel.montage} |`, "");
  L.push(`> Le look du film se règle dans ces sélecteurs : ne le répétez pas dans le texte du prompt.`, "");
  for (const sc of ep.scenes) {
    L.push(`## SEEDANCE ${NN(sc.n)} — ${sc.titre}`, "");
    L.push(`*${sc.resume}*`, "");
    L.push("```text", promptSeedance(ep, sc), "```", "");
  }
  L.push(`## CLAUDE CODE — ${S.outro.duree_s} s (outro ep${n} : ${S.outro.duree_s - 10} s de transition + 10 s d'animation)`, "");
  L.push(`**Voix off — transition** (commune aux 30 épisodes, à 2,1 s) : « ${S.transition.texte} »`, "");
  L.push(`**Voix off — épisode** (à 4,6 s) : « ${ep.montage.vo} »`);
  if (ep.montage.vo_variante_courte) {
    L.push(``, `> ⚠️ Cette phrase dépasse la fenêtre de ${FENETRE_VO_S} s (2,0 s → 9,0 s) à débit posé.`);
    L.push(`> **Variante courte proposée** : « ${ep.montage.vo_variante_courte} »`);
  }
  L.push("");
  L.push("```text", directiveMontage(ep), "```", "");
  L.push(`## Contrôle avant publication`, "");
  L.push(`- [ ] Michael : même visage, même coiffure, même tenue sur les deux scènes.`);
  L.push(`- [ ] Aucun texte lisible généré par Seedance (enseigne, ticket, écran, sous-titre).`);
  L.push(`- [ ] Chaque réplique est compréhensible sans sous-titres.`);
  L.push(`- [ ] La chute est claire avant la fin de la scène 2 et Michael regarde la caméra.`);
  L.push(`- [ ] Le clap « COUPEZ ! » arrive à 0,4 s de l'outro.`);
  L.push(`- [ ] Modules affichés : ${ep.montage.cartes.join(" · ")} — libellés réels vérifiés.`);
  L.push(`- [ ] Logo FoodEatUp intact, centré, seul à l'écran de 9 à 10 s.`);
  L.push(`- [ ] La vidéo se comprend sans le son.`, "");
  L.push(`---`, `Source : \`episodes/\` + \`saison.json\` — fiche générée par \`scripts/build.mjs\`, ne pas éditer à la main.`);
  return L.join("\n");
}

/* ---------------------------------------------------------------- contrôles */
const MODULES = new Set(S.modules_autorises);
const MOTS_INTERDITS = ["malheureusement", "organisationnellement", "synchronisation", "approvisionnement", "spécifiquement"];
const MINEURS = ["child", "children", "kid", "kids", "boy", "girl", "teen", "teenager", "years old", "baby", "toddler"];
const alertes = [];
const add = (ep, niveau, texte) => alertes.push({ ep: ep ? NN(ep.num) : "—", niveau, texte });

if (EPISODES.length !== 30) add(null, "ERREUR", `${EPISODES.length} épisodes au lieu de 30.`);
const vus = new Set();
for (const ep of EPISODES) {
  if (vus.has(ep.num)) add(ep, "ERREUR", `numéro d'épisode en double.`);
  vus.add(ep.num);
  if (ep.scenes.length !== 2) add(ep, "ERREUR", `${ep.scenes.length} scène(s) au lieu de 2.`);
  for (const c of ep.montage.cartes) {
    if (!MODULES.has(c)) add(ep, "ERREUR", `module « ${c} » absent de la liste des libellés autorisés.`);
  }
  for (const sc of ep.scenes) {
    const bloc = `${sc.scene} ${sc.action.map((a) => a.texte).join(" ")} ${sc.dialogue}`;
    if (/foodeatup/i.test(sc.dialogue)) add(ep, "ERREUR", `scène ${sc.n} : « FoodEatUp » est prononcé par l'avatar (interdit, réservé à la voix off).`);
    const mineur = MINEURS.find((m) => new RegExp(`\\b${m}\\b`, "i").test(bloc));
    if (mineur) add(ep, "ERREUR", `scène ${sc.n} : mention « ${mineur} » — aucun mineur dans les prompts.`);
    const interdit = MOTS_INTERDITS.find((m) => sc.dialogue.toLowerCase().includes(m));
    if (interdit) add(ep, "ALERTE", `scène ${sc.n} : « ${interdit} » est dans la liste des mots à éviter (prononciation).`);
    if (!/«/.test(sc.dialogue)) add(ep, "ALERTE", `scène ${sc.n} : dialogue sans guillemets français.`);
    if (sc.action.length < 3) add(ep, "ALERTE", `scène ${sc.n} : moins de 3 plans dans l'ACTION.`);
  }
  const duree = ep.montage.vo.length / CPS;
  if (duree > FENETRE_VO_S) {
    add(ep, "ALERTE", `voix off ≈ ${duree.toFixed(1)} s (fenêtre ${FENETRE_VO_S} s)${ep.montage.vo_variante_courte ? " — variante courte proposée dans la fiche" : " — raccourcir ou accélérer le débit"}.`);
  }
}

/* ------------------------------------------------------------------ sorties */
mkdirSync(join(ROOT, "prompts"), { recursive: true });
mkdirSync(join(ROOT, "voix-off"), { recursive: true });

for (const ep of EPISODES) {
  writeFileSync(join(ROOT, "prompts", `ep${NN(ep.num)}-${ep.slug}.md`), ficheEpisode(ep) + "\n");
}

writeFileSync(join(ROOT, "episodes.json"), JSON.stringify({ ...S, episodes: EPISODES }, null, 1) + "\n");

const lot = (n) => Object.entries(S.lots_lumiere).find(([, v]) => v.includes(n))?.[0] ?? "—";
const index = [
  `# FoodEatUp — Saison 2 « Michael fait son cinéma » — Index des 30 épisodes`,
  ``,
  `30 épisodes · 60 prompts Seedance 2.5 (Higgsfield) · 30 outros Remotion · format ${S.format}.`,
  `1 épisode = 1 genre de film culte + 1 situation de restaurant + 1 module FoodEatUp.`,
  ``,
  `| # | Titre | Genre culte | Situation | Module FoodEatUp | Hook | Lot lumière |`,
  `|---|---|---|---|---|---|---|`,
  ...EPISODES.map((e) =>
    `| ${NN(e.num)} | [${e.titre}](prompts/ep${NN(e.num)}-${e.slug}.md) | ${e.genre_court} | ${e.situation} | ${e.modules.join(" + ")} | ${e.hook.replace(/\|/g, "/")} | ${lot(e.num)} |`
  ),
  ``,
  `## Tournage par lots de lumière`,
  ``,
  ...Object.entries(S.lots_lumiere).map(([k, v]) => `- **${k}** : ${v.map(NN).join(" · ")}`),
  ``,
  `Pilotes à produire en premier (480p) : ${S.pilotes.map(NN).join(" · ")}.`,
  `Rendu 1080p pour les épisodes phares : ${S.rendu_1080p.map(NN).join(" · ")}.`,
  ``,
  `---`,
  `Fichier généré par \`scripts/build.mjs\`, ne pas éditer à la main.`,
].join("\n");
writeFileSync(join(ROOT, "SAISON-2-EPISODES.md"), index + "\n");

const directiveCommune = [
  `# Directive de montage commune aux 30 épisodes`,
  ``,
  `À coller avant le bloc de l'épisode. Chaque fiche de \`prompts/\` contient déjà la version`,
  `complète, épisode substitué : ce fichier n'est là que comme référence de la structure.`,
  ``,
  "```text",
  `Tu es motion designer. Crée avec Remotion (React) une composition verticale 1080×1920, ${S.outro.fps} fps,`,
  `${S.outro.frames} images (${S.outro.duree_s} s), export MP4 H.264, fichier ep{NN}-outro.mp4.`,
  ``,
  `Entrées dans ./assets : logo-foodeatup.svg · palette.json · scene2-last-frame.png · vo.mp3 · sfx/`,
  `(clap.wav, whoosh.wav, tick.wav, impact.wav). Voir assets/README.md pour la provenance.`,
  ``,
  `STRUCTURE IMPOSÉE (identique sur les 30 épisodes — c'est la signature de la saison) :`,
  ...S.outro.structure.map((x) => `${x.t} : ${x.contenu}`),
  ``,
  `CONTENU DE CET ÉPISODE : [bloc de l'épisode — voir prompts/ep{NN}-*.md]`,
  ``,
  `RÈGLES : ${S.outro.regles.join(" ")}`,
  ``,
  `SORTIES : ${S.outro.sorties.join(" · ")}`,
  "```",
  ``,
  `## Libellés de modules autorisés (${S.modules_autorises.length})`,
  ``,
  S.modules_autorises.join(" · "),
  ``,
  `Aucun autre libellé ne peut apparaître à l'écran. \`npm run check\` le vérifie sur les 30 épisodes.`,
  ``,
  `---`,
  `Fichier généré par \`scripts/build.mjs\`, ne pas éditer à la main.`,
].join("\n");
writeFileSync(join(ROOT, "DIRECTIVE-MONTAGE.md"), directiveCommune + "\n");

const vo = EPISODES.map((e) => ({
  id: `ep${NN(e.num)}`,
  titre: e.titre,
  texte: e.montage.vo,
  caracteres: e.montage.vo.length,
  duree_estimee_s: +(e.montage.vo.length / CPS).toFixed(1),
  ...(e.montage.vo_variante_courte
    ? {
        variante_courte: e.montage.vo_variante_courte,
        variante_courte_duree_s: +(e.montage.vo_variante_courte.length / CPS).toFixed(1),
      }
    : {}),
}));
writeFileSync(join(ROOT, "voix-off", "vo-saison-2.json"), JSON.stringify({ voix: S.voix_off, cps: CPS, fenetre_s: FENETRE_VO_S, lignes: vo }, null, 1) + "\n");
writeFileSync(
  join(ROOT, "voix-off", "vo-saison-2.md"),
  [
    `# Voix off — Saison 2 (30 phrases, une passe ElevenLabs)`,
    ``,
    `**Voix de la saison** : \`${S.voix_off.voix}\` — \`${S.voix_off.voice_id}\`, modèle \`${S.voix_off.model_id}\`.`,
    `${S.voix_off.note}`,
    `Normalisation avant montage : **${S.voix_off.normalisation}**.`,
    ``,
    `Même voix et mêmes réglages de stabilité / rythme sur les 30 épisodes. La voix off démarre à`,
    `4,6 s de l'outro et se termine avant 11,0 s : la fenêtre utile est de **${FENETRE_VO_S} s**`,
    `(≈ ${Math.round(FENETRE_VO_S * CPS)} caractères au débit mesuré de ${String(CPS).replace(".", ",")} caractères/seconde).`,
    ``,
    `C'est la voix off — et elle seule — qui prononce « FoodEatUp ». L'avatar Seedance ne le dit jamais.`,
    ``,
    `## La ligne de transition (une seule prise pour les 30 épisodes)`,
    ``,
    `> « ${S.transition.texte} »`,
    ``,
    `${S.transition.role} Elle est dite à ${String(S.transition.cale_s).replace(".", ",")} s de l'outro, sur le plan figé,`,
    `entre le clap « COUPEZ ! » et « Dans la vraie vie… ». ${S.transition.note}`,
    ``,
    `Variantes validées, interchangeables sans retoucher le montage :`,
    ``,
    ...S.transition.alternatives.map((a) => `- « ${a} »`),
    ``,
    `## Les 30 lignes d'épisode`,
    ``,
    `| # | Épisode | Phrase | Car. | ≈ durée |`,
    `|---|---|---|---|---|`,
    ...vo.map((v, i) => `| ${NN(i + 1)} | ${v.titre} | ${v.texte} | ${v.caracteres} | ${v.duree_estimee_s} s${v.duree_estimee_s > FENETRE_VO_S ? " ⚠️" : ""} |`),
    ``,
    `⚠️ = dépasse la fenêtre. Le texte du brief est conservé tel quel ; une variante courte est`,
    `proposée ci-dessous pour ces épisodes — à valider avant d'enregistrer la voix.`,
    `L'estimation est indicative : c'est la durée réelle de la prise qui fait foi. L'épisode 04,`,
    `estimé à 6,6 s, sort à 6,08 s et tient sans retouche.`,
    ``,
    `| # | Épisode | Variante courte proposée | Car. | ≈ durée |`,
    `|---|---|---|---|---|`,
    ...vo.filter((v) => v.variante_courte).map((v) => `| ${v.id.slice(2)} | ${v.titre} | ${v.variante_courte} | ${v.variante_courte.length} | ${v.variante_courte_duree_s} s |`),
    ``,
    `---`,
    `Fichier généré par \`scripts/build.mjs\`, ne pas éditer à la main.`,
  ].join("\n") + "\n"
);

const erreurs = alertes.filter((a) => a.niveau === "ERREUR");
writeFileSync(
  join(ROOT, "RAPPORT-CONTROLES.md"),
  [
    `# Rapport de contrôles — Saison 2`,
    ``,
    `Généré par \`npm run build\` (\`scripts/build.mjs\`) sur ${EPISODES.length} épisodes / ${EPISODES.length * 2} prompts Seedance.`,
    ``,
    `## Ce qui est vérifié automatiquement`,
    `1. 30 épisodes, numéros uniques, 2 scènes par épisode.`,
    `2. Chaque module affiché en carte existe dans la liste des libellés FoodEatUp autorisés.`,
    `3. « FoodEatUp » n'est jamais prononcé par l'avatar Seedance (réservé à la voix off).`,
    `4. Aucun mineur mentionné dans les prompts (filtre de contenu Higgsfield).`,
    `5. Aucun mot de la liste « à éviter » du lexique voix dans les répliques.`,
    `6. Dialogues en guillemets français, au moins 3 plans par scène.`,
    `7. Voix off tenant dans la fenêtre de ${FENETRE_VO_S} s (4,6 s → 11,0 s).`,
    ``,
    `## Ce qui reste à l'œil humain`,
    `Identité de Michael d'une scène à l'autre · absence de texte lisible généré par Seedance ·`,
    `compréhension sans le son · clap à 0,4 s · logo intact de 9 à 10 s.`,
    ``,
    `## Résultat`,
    ``,
    erreurs.length === 0 ? `✅ Aucune erreur bloquante.` : `❌ ${erreurs.length} erreur(s) bloquante(s).`,
    ``,
    alertes.length === 0
      ? `Aucune alerte.`
      : [`| Épisode | Niveau | Détail |`, `|---|---|---|`, ...alertes.map((a) => `| ${a.ep} | ${a.niveau} | ${a.texte} |`)].join("\n"),
    ``,
  ].join("\n") + "\n"
);

console.log(`✅ ${EPISODES.length} fiches générées dans prompts/`);
console.log(`   index · voix off · episodes.json · RAPPORT-CONTROLES.md`);
for (const a of alertes) console.log(`   ${a.niveau === "ERREUR" ? "❌" : "⚠️ "} ep${a.ep} — ${a.texte}`);
if (erreurs.length) process.exitCode = 1;
