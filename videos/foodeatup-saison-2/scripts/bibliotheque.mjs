#!/usr/bin/env node
// Écrit BIBLIOTHEQUE-PLANS.md : les plans Seedance déjà générés, réutilisables tels quels.
//
// La règle du dépôt (CLAUDE.md) interdit de générer un nouveau plan sans avoir d'abord
// cherché dans ce qui existe. Cette fiche est cette bibliothèque : un plan par ligne,
// avec son identifiant Higgsfield, son lien direct, et de quoi juger s'il peut resservir.
//
//   node scripts/bibliotheque.mjs

import { readFileSync, writeFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const ROOT = join(dirname(fileURLToPath(import.meta.url)), "..");
const lire = (f) => JSON.parse(readFileSync(join(ROOT, f), "utf8"));

const S = lire("saison.json");
const { episodes: EPS } = lire("episodes.json");
const SRC = lire("renders/sources.json");

const parNum = new Map(EPS.map((e) => [e.num, e]));
const plans = Object.entries(SRC.plans).map(([id, p]) => {
  const ep = parNum.get(p.episode);
  const sc = ep.scenes[p.scene - 1];
  return { id, ...p, ep, sc };
});
plans.sort((a, b) => a.episode - b.episode || a.scene - b.scene);

// Le lieu se lit dans la ligne REF du prompt : « Location = … ».
const lieu = (sc) => (sc.location_line.match(/Location[s]? = (.+)$/)?.[1] ?? sc.location_line).replace(/\.$/, "");

const L = [];
L.push(`# 🎞️ Bibliothèque de plans Seedance — Saison 2`);
L.push("");
L.push(
  `${plans.length} plans générés et déjà montés. **Avant de faire générer un nouveau plan, cherchez ici.**`,
  `C'est la règle du dépôt : on réutilise un plan existant, ou on donne le prompt à l'utilisateur`,
  `pour qu'il le génère lui-même — on n'appelle jamais Higgsfield depuis une session.`,
);
L.push("");
L.push(`Chaque lien pointe sur le rendu Higgsfield d'origine (720×1280, 10 s, audio compris).`);
L.push(`Les mêmes fichiers sont dans le dépôt, sous \`renders/ep{NN}/source/\`.`);
L.push("");

L.push(`## Les plans, épisode par épisode`);
L.push("");
L.push(`| # | Épisode | Sc. | Titre du plan | Genre | Lieu | Plan |`);
L.push(`|---|---|---|---|---|---|---|`);
for (const p of plans) {
  const nn = String(p.episode).padStart(2, "0");
  L.push(
    `| ${nn} | ${p.ep.titre} | ${p.scene} | ${p.sc.titre} | ${p.ep.genre_court} | ${lieu(p.sc)} | [voir](${p.url}) |`,
  );
}
L.push("");

L.push(`## Ce que chaque plan contient`);
L.push("");
for (const p of plans) {
  const nn = String(p.episode).padStart(2, "0");
  L.push(`### ep${nn} · scène ${p.scene} — « ${p.sc.titre} »`);
  L.push("");
  L.push(`- **Identifiant Higgsfield** : \`${p.id}\``);
  L.push(`- **Lien direct** : ${p.url}`);
  L.push(`- **Genre** : ${p.ep.genre}`);
  L.push(`- **Lieu** : ${lieu(p.sc)}`);
  L.push(`- **Ce qui s'y passe** : ${p.sc.resume}`);
  L.push(`- **Dialogue** : ${p.sc.dialogue}`);
  // Seules les réserves qui portent sur l'image comptent ici : elles décident si le plan resservira.
  const note = SRC.episodes[nn]?.note;
  if (note?.startsWith("⚠️")) L.push(`- **Réserve sur l'épisode** : ${note.replace(/^⚠️\s*/, "")}`);
  L.push("");
}

L.push(`## Références de saison`);
L.push("");
L.push(`Les plans partagent tous le même bloc de références, à reprendre tel quel :`);
L.push("");
L.push("```text");
L.push(S.prompt.ref_michael);
L.push("```");
L.push("");
for (const r of S.references) L.push(`- **${r.cle}** — ${r.role}`);
L.push("");
L.push(`---`);
L.push(
  `Source : \`renders/sources.json\` + \`episodes.json\` — fiche générée par \`scripts/bibliotheque.mjs\`, ne pas éditer à la main.`,
);

writeFileSync(join(ROOT, "BIBLIOTHEQUE-PLANS.md"), L.join("\n") + "\n");
console.log(`✅ BIBLIOTHEQUE-PLANS.md — ${plans.length} plans`);
