#!/usr/bin/env node
// Assemble l'épisode. Le montage lui-même est celui de la série, partagé par tous les épisodes.
import { createRequire } from "node:module";
import { EP, ROOT, WORK, OUT, CHROME, PLAYWRIGHT, FFMPEG, ff, sonder, dossiers, s2 } from "./outils.mjs";
import { monter } from "../../module-methode-rapidocms/scripts/monter.mjs";

const require = createRequire(import.meta.url);
const { chromium } = require(PLAYWRIGHT);

dossiers(WORK, OUT);
await monter({
  EP, ROOT, WORK, OUT, chromium, chrome: CHROME, ff, sonder, s2, FFMPEG,
  // l'accroche au tiers bas ; les sous-titres au-dessus du produit, qui occupe le bas du cadre
  y: { accroche: 1290, soustitre: EP.film.incrustation_produit.y_soustitre ?? 1250 },
});
