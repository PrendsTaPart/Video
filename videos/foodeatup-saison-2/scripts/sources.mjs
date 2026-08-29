#!/usr/bin/env node
// Écrit renders/ep{NN}/SOURCES.md pour chaque épisode décrit dans renders/sources.json.
// La traçabilité des plans réutilisés est une donnée, pas un texte à réécrire à la main.
import { readFileSync, writeFileSync, existsSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const ROOT = join(dirname(fileURLToPath(import.meta.url)), "..");
const S = JSON.parse(readFileSync(join(ROOT, "episodes.json"), "utf8"));
const SRC = JSON.parse(readFileSync(join(ROOT, "renders", "sources.json"), "utf8"));
const fr = (n) => String(n).replace(".", ",");

for (const [n, src] of Object.entries(SRC.episodes)) {
  const ep = S.episodes.find((e) => e.num === Number(n));
  const dir = join(ROOT, "renders", `ep${n}`);
  if (!existsSync(dir)) continue;
  const L = [];
  L.push(`# Épisode ${n} « ${ep.titre} » — provenance`, "");
  L.push(`**Aucune génération Higgsfield n'a été lancée** (règle \`CLAUDE.md\`). Les deux plans de 10 s`);
  L.push(`existaient déjà dans la bibliothèque du compte et sont **réutilisés tels quels**.`, "");
  L.push(`| Plan | Generation ID Higgsfield | Fichier |`, `|---|---|---|`);
  L.push(`| Scène 1 — « ${ep.scenes[0].titre} » | \`${src.scene1}\` | \`source/ep${n}-scene1.mp4\` |`);
  L.push(`| Scène 2 — « ${ep.scenes[1].titre} » | \`${src.scene2}\` | \`source/ep${n}-scene2.mp4\` |`);
  if (src.scene1_alternative)
    L.push(`| Scène 1, prise alternative | \`${src.scene1_alternative}\` | \`source/ep${n}-scene1-prise-alternative.mp4\` |`);
  if (src.scene2_alternative)
    L.push(`| Scène 2, prise alternative | \`${src.scene2_alternative}\` | \`source/ep${n}-scene2-prise-alternative.mp4\` |`);
  L.push("");
  if (src.note) L.push(`> ${src.note}`, "");
  L.push(`Sources d'origine : 720×1280, 24 fps, ~10 s, audio AAC 32 kHz (dialogue français et ambiance`);
  L.push(`générés dans la même passe). Les prompts stockés côté Higgsfield correspondent à la fiche`);
  L.push(`\`prompts/ep${n}-${ep.slug}.md\`, à une différence près : la référence visage y est passée en`);
  L.push(`\`<<<image_1>>>\` (Reference Element) au lieu de \`@Image 1\`.`, "");
  L.push(`## Sorties`, "");
  L.push(`| Fichier | Contenu |`, `|---|---|`);
  L.push(`| \`ep${n}-${ep.slug}.mp4\` | **Le master** : scène 1 + scène 2 + transition + animation, 1080×1920, 30 fps, 32,1 s |`);
  L.push(`| \`ep${n}-outro.mp4\` | L'outro seul, 12 s, voix off + SFX |`);
  L.push(`| \`ep${n}-outro-muet.mp4\` | L'outro seul, 12 s, SFX uniquement |`);
  L.push(`| \`vo.mp3\` | La voix off de l'épisode, normalisée |`);
  L.push(`| \`ep${n}-thumb.png\` | Miniature : le plan figé du début de l'outro + le titre |`);
  L.push(`| \`scene2-last-frame.png\` | Dernière image de la scène 2, plaque de départ de l'outro |`, "");
  L.push(`## Voix off`, "");
  L.push(`| | |`, `|---|---|`);
  L.push(`| Voix | **${S.voix_off.voix}** \`${S.voix_off.voice_id}\`, modèle \`${S.voix_off.model_id}\` |`);
  L.push(`| Transition (commune aux 30 épisodes) | « ${S.transition.texte} » — prise \`${SRC.transition.generation_id}\` (${fr(SRC.transition.duree_s)} s), calée à ${fr(S.transition.cale_s)} s |`);
  L.push(`| Ligne de l'épisode | « ${ep.montage.vo} » |`);
  L.push(`| Prise retenue | \`${src.vo.generation_id}\` (${fr(src.vo.duree_s)} s) |`);
  const depart = Math.max(4.25, Math.min(4.6, 10.9 - src.vo.duree_s));
  L.push(`| Calage | démarre à **${fr(depart.toFixed(2))} s**, se termine à **${fr((depart + src.vo.duree_s).toFixed(2))} s** (fenêtre : avant 11,0 s) ${depart + src.vo.duree_s <= 11 ? "✅" : "⚠️"} |`, "");
  L.push(`Les prises ElevenLabs sortent très bas : chacune est normalisée à −16 LUFS / −1,5 dBTP.`);
  L.push(`Le départ de la voix est calculé pour qu'elle finisse avant 11,0 s : 4,60 s par défaut, avancé quand
la prise est longue. L'outro est ensuite calé au niveau de saison (−18,5 LUFS), puis le master normalisé`);
  L.push(`à −16 LUFS en gain linéaire (loudnorm deux passes), le standard des plateformes.`, "");
  if (src.catalogue) {
    L.push(`## Dépôt au catalogue Social FoodEatUp`, "");
    L.push(`| | |`, `|---|---|`);
    L.push(`| Épisode au catalogue | \`${src.catalogue.id}\` — série \`${src.catalogue.serie}\`, saison ${src.catalogue.saison} |`);
    L.push(`| Pièce | \`${src.catalogue.piece}\` |`);
    L.push(`| État | **${src.catalogue.etat}** |`);
    L.push(`| Fichier | ${src.catalogue.url} |`, "");
    L.push(`${SRC.catalogue.verrou}`, "");
  }
  L.push(`## Calage des SFX dans l'outro (secondes)`, "");
  L.push(`\`clap\` 0,40 · \`whoosh\` 2,00 (la punchline de transition) · \`tick\` 4,40 / 4,73 / 5,07`);
  L.push(`(l'élément clé qui devient des données) · \`whoosh\` 7,60 (l'action en un tap) · \`tick\``);
  L.push(`9,33 / 9,67 / 10,00 (les cartes modules) · \`whoosh\` 10,95 + \`impact\` 11,00 (le logo).`, "");
  L.push(`## Reconstruire`, "");
  L.push("```bash", `./scripts/monter-episode.sh ${n}`, "```", "");
  L.push(`---`, `Fichier généré par \`scripts/sources.mjs\` depuis \`renders/sources.json\`, ne pas éditer à la main.`);
  writeFileSync(join(dir, "SOURCES.md"), L.join("\n") + "\n");
  console.log(`✅ renders/ep${n}/SOURCES.md`);
}
