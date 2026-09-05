#!/usr/bin/env node
// Construit la queue animée de l'épisode : la voix off (deux lignes à lui, six au module)
// puis le rendu des 30 s d'animation. Passe --apercu 31,36,49,55 pour ne sortir que des images.
import { join } from "node:path";
import { createRequire } from "node:module";
import { EP, ROOT, WORK, CHROME, PLAYWRIGHT, ff, sonder, silences, dossiers, s2 } from "./outils.mjs";
import { construireVoix } from "../../module-methode-rapidocms/scripts/voix.mjs";
import { donneesAnimation, rendre } from "../../module-methode-rapidocms/scripts/rendre.mjs";

const require = createRequire(import.meta.url);
const { chromium } = require(PLAYWRIGHT);

dossiers(WORK);
const { cales } = construireVoix({
  EP, ROOT, work: WORK, ff, sonder, silences, s2,
  trace: join(ROOT, "audio", "vo-queue-decoupe.json"),
});
for (const c of cales) {
  console.log(`   ${c.cle.padEnd(10)} ${c.dit_s.toFixed(2)}s → ${(c.ligne.fin_s - c.ligne.debut_s).toFixed(2)}s (${c.tempo.toFixed(2)}×)  « ${c.ligne.vo} »`);
}
console.log(`✅ voix de la queue — ${EP.queue.fin_s - EP.queue.debut_s} s, étapes reprises du module`);

const donnees = donneesAnimation({ EP, logosDir: join(ROOT, "assets", "logos"), charte: EP.charte });
const arg = process.argv.indexOf("--apercu");
const apercus = arg >= 0 ? process.argv[arg + 1].split(",").map((t) => +t - EP.queue.debut_s) : null;
const r = await rendre({
  donnees, work: WORK, sortie: join(WORK, "queue-muette.mp4"),
  chromium, chrome: CHROME, ff, apercus,
});
console.log(apercus ? `   aperçus : ${r.join(" · ")}` : `✅ ${r} — ${donnees.frames} images à ${donnees.fps} ips`);
