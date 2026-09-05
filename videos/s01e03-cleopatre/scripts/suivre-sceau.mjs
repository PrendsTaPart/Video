#!/usr/bin/env node
// Vérifie le suivi du sceau de cire : dessine la boîte d'episode.json sur trois images de
// la fenêtre, pour qu'on juge à l'œil si l'emblème de l'annonceur tomberait au bon endroit.
//
// Pourquoi à l'œil et pas à la couleur : sur ce plan le brasero est la source principale et
// inonde tout l'établi de la même teinte que la cire. Le suivi colorimétrique du module
// (scripts/suivre-couleur.mjs) sort une boîte de mille pixels de large là où le sceau en
// fait deux cent soixante — il a été essayé, il ne tient pas ici.
import { join } from "node:path";
import { EP, ROOT, WORK, L, H, ff, dossiers, s2 } from "./outils.mjs";

const IP = EP.film.incrustation_produit;
const clip3 = EP.film.clips[2];
const p = IP.suivi;
if (!p?.length) throw new Error("episode.json ne porte aucun point de suivi.");

const a = (t) => {
  for (let i = 0; i < p.length - 1; i++) {
    const [u, v] = [p[i], p[i + 1]];
    if (t <= v.t_s) {
      const k = (t - u.t_s) / (v.t_s - u.t_s);
      const m = (c) => Math.round(u[c] + k * (v[c] - u[c]));
      return { x: m("x"), y: m("y"), l: m("l"), h: m("h") };
    }
  }
  return p[p.length - 1];
};

dossiers(WORK);
const instants = [IP.debut_s, (IP.debut_s + IP.fin_s) / 2, IP.fin_s - 0.1];
const images = instants.map((t) => {
  const r = a(t);
  const f = join(WORK, `sceau-${String(t).replace(".", "_")}.png`);
  ff(["-ss", s2(t - clip3.debut_s), "-i", join(ROOT, clip3.fichier), "-frames:v", "1",
      "-vf", `scale=${L}:${H}:flags=lanczos,drawbox=x=${r.x}:y=${r.y}:w=${r.l}:h=${r.h}:color=magenta@0.95:t=5,` +
             `crop=${L}:560:0:1080,scale=430:223`, f]);
  console.log(`   ${t} s → ${r.l}×${r.h} en (${r.x},${r.y})`);
  return f;
});
const planche = join(WORK, "sceau-verification.png");
ff([...images.flatMap((f) => ["-i", f]), "-filter_complex",
    images.map((_, i) => `[${i}]`).join("") + `vstack=${images.length}`, planche]);
console.log(`✅ ${planche} — la boîte doit tomber sur le disque de cire aux trois instants.`);
