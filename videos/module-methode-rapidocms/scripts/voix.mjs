// Assemble la voix off de la queue animée : la ligne d'ouverture et la punchline de fin
// de l'épisode, posées autour des six lignes d'étapes déjà rendues une fois pour la série.
//
// Un épisode ne génère donc que deux lignes chez ElevenLabs. Les étapes ne bougent jamais :
// les regénérer coûterait des crédits et ferait varier le timbre au milieu du module.
import { readFileSync, writeFileSync } from "node:fs";
import { join } from "node:path";

export const MODULE = join(import.meta.dirname, "..");
const TEMPO_MAX = 1.4;
const GAP = 0.08;          // la respiration qu'on laisse entre deux phrases d'une même ligne
const MIN_PHRASE_S = 0.15; // en deçà, c'est un reste de souffle, pas une phrase

/* Une prise ElevenLabs contient des respirations et finit sur du silence. On garde les
   phrases, on ramène les respirations à un souffle, et on ne compte que ce qui est dit. */
function phrasesDe(fichier, { sonder, silences }) {
  const total = sonder(fichier).duree_s;
  const pauses = silences(fichier, { seuil_db: 40, duree_min_s: 0.15 });
  const finale = pauses.length && pauses[pauses.length - 1].fin_s >= total - 0.05 ? pauses.pop() : null;
  const bouts = [];
  let curseur = 0;
  for (const p of pauses) { bouts.push({ debut_s: curseur, fin_s: p.debut_s }); curseur = p.fin_s; }
  bouts.push({ debut_s: curseur, fin_s: finale ? finale.debut_s : total });
  const retenues = bouts.filter((p) => p.fin_s - p.debut_s >= MIN_PHRASE_S);
  if (!retenues.length) throw new Error(`aucune parole trouvée dans ${fichier}.`);
  const dit = retenues.reduce((s, p) => s + (p.fin_s - p.debut_s), 0) + GAP * (retenues.length - 1);
  return { phrases: retenues, dit_s: dit, prise_s: total };
}

/* Une ligne = ses phrases recollées, puis accélérées du minimum nécessaire à son créneau. */
function caler({ nom, fichier, creneau_s, work, ff, s2, sonder, silences }) {
  const { phrases, dit_s, prise_s } = phrasesDe(fichier, { sonder, silences });
  const tempo = Math.max(1, dit_s / creneau_s);
  if (tempo > TEMPO_MAX) {
    throw new Error(
      `${nom} : ${dit_s.toFixed(2)} s à tenir en ${creneau_s.toFixed(2)} s, soit ${tempo.toFixed(2)}× — ` +
      `au-delà de ${TEMPO_MAX}× la voix s'entend accélérée. Raccourcir le texte ou allonger le créneau.`
    );
  }
  const bouts = phrases.map((p, i) => {
    const f = join(work, `${nom}-${i + 1}.wav`);
    ff(["-ss", s2(p.debut_s), "-to", s2(p.fin_s), "-i", fichier, "-ar", "48000", "-ac", "2", f]);
    return f;
  });
  const sortie = join(work, `${nom}-calee.wav`);
  ff([...bouts.flatMap((f) => ["-i", f]),
      "-filter_complex",
      bouts.map((_, i) => `[${i}:a]`).join("") +
        `concat=n=${bouts.length}:v=0:a=1[j];[j]atempo=${tempo.toFixed(6)}[o]`,
      "-map", "[o]", "-ar", "48000", "-ac", "2", sortie]);
  return { fichier: sortie, phrases: phrases.length, dit_s, prise_s, tempo };
}

export function construireVoix({ EP, ROOT, work, ff, sonder, silences, s2, trace }) {
  const Q = EP.queue;
  const t0 = Q.debut_s;
  const etapes = join(MODULE, "audio", "vo-etapes-2a7.wav");
  const mod = JSON.parse(readFileSync(join(MODULE, "module.json"), "utf8"));

  const aCaler = [
    { cle: "ouverture", ligne: Q.lignes.find((l) => l.ecran === "ouverture") },
    { cle: "hook", ligne: Q.lignes.find((l) => l.ecran === "hook") },
  ];
  const cales = aCaler.map(({ cle, ligne }) => {
    if (!ligne) throw new Error(`queue.lignes n'a pas de ligne « ${cle} ».`);
    const r = caler({
      nom: cle,
      fichier: join(ROOT, ligne.source),
      creneau_s: ligne.fin_s - ligne.debut_s,
      work, ff, s2, sonder, silences,
    });
    return { cle, ligne, ...r };
  });

  /* Chaque ligne rejoint sa place dans les trente secondes, par-dessus les étapes. */
  const entrees = [...cales.flatMap((c) => ["-i", c.fichier]), "-i", etapes];
  const decales = cales
    .map((c, i) => `[${i}:a]adelay=${Math.round((c.ligne.debut_s - t0) * 1000)}:all=1[d${i}]`)
    .join(";");
  const pistes = cales.map((_, i) => `[d${i}]`).join("") + `[${cales.length}:a]`;
  const sortie = join(ROOT, "audio", "vo-queue.wav");
  ff([...entrees,
      "-filter_complex",
      `${decales};${pistes}amix=inputs=${cales.length + 1}:normalize=0:dropout_transition=0[v];[v]apad[o]`,
      "-map", "[o]", "-t", s2(Q.fin_s - t0), "-ar", "48000", "-ac", "2", "-c:a", "pcm_s16le", sortie]);

  if (trace) {
    writeFileSync(trace, JSON.stringify({
      voix: mod.voix,
      etapes: "module — lignes 2 à 7, jamais regénérées",
      lignes_de_l_episode: cales.map((c) => ({
        role: c.cle, vo: c.ligne.vo, source: c.ligne.source,
        prise_s: +c.prise_s.toFixed(3), phrases: c.phrases,
        dit_s: +c.dit_s.toFixed(3), creneau_s: +(c.ligne.fin_s - c.ligne.debut_s).toFixed(3),
        tempo: +c.tempo.toFixed(3), cale_a_s: c.ligne.debut_s,
      })),
    }, null, 1) + "\n");
  }
  return { sortie, cales };
}
