#!/usr/bin/env node
// Découpe la passe unique de voix off en ses sept lignes, cale chacune sur son timecode,
// et écrit une piste de 15 s alignée sur le bloc méthode.
//
// La passe est enregistrée d'un trait pour garder la ligne mélodique. Elle dure 23,7 s
// là où le plan de montage en donne 15 : chaque ligne est donc accélérée du minimum
// nécessaire pour tenir dans son créneau. atempo conserve la hauteur de voix, et aucune
// ligne ne dépasse TEMPO_MAX — au-delà on l'entendrait.
import { existsSync, writeFileSync } from "node:fs";
import { join } from "node:path";
import { EP, ROOT, WORK, VARIANTE, ff, sonder, silences, dossiers, s2 } from "./outils.mjs";

const SOURCE = join(ROOT, "audio", "vo-methode-passe-unique.mp3");
const SORTIE = join(ROOT, "audio", `vo-methode-calee-${VARIANTE}.wav`);
const DECOUPE = join(ROOT, "audio", `vo-decoupe-${VARIANTE}.json`);
/* La ligne la plus serrée de cette prise sort à 1,35× ; le garde-fou est un peu au-dessus,
   pour attraper une prise franchement trop lente plutôt que pour discuter des centièmes. */
const TEMPO_MAX = 1.4;

if (!existsSync(SOURCE)) throw new Error(`manque ${SOURCE} — la passe unique ElevenLabs.`);
dossiers(WORK);

const lignes = EP.methode.lignes;
const duree_passe = sonder(SOURCE).duree_s;
const pauses = silences(SOURCE, { seuil_db: 40, duree_min_s: 0.2 });
if (pauses.length < lignes.length - 1) {
  throw new Error(`seulement ${pauses.length} pause(s) dans la passe : impossible d'y trouver ${lignes.length} lignes.`);
}

/* Où couper ? Ni la longueur des pauses ni celle des textes ne suffit à le deviner :
   sur cette prise, les six pauses les plus longues collent « Trois » à « Quatre » et
   coupent la dernière phrase en deux, et le nombre de caractères se trompe autrement,
   parce que « MCP », « RapidoCMS » et « HyperFrames » se disent lentement.
   Les instants de coupe sont donc relevés sur la prise et écrits dans episode.json.
   Ce script ne les redécouvre pas, il les vérifie : chacun doit tomber dans un silence,
   et les bornes de la ligne sont les bords de ce silence — pas l'instant lui-même. */
const coupes = EP.methode.voix.decoupe_s ?? [];
if (coupes.length !== lignes.length - 1) {
  throw new Error(
    `episode.json donne ${coupes.length} instant(s) de coupe pour ${lignes.length} lignes : ` +
    `il en faut ${lignes.length - 1}.`
  );
}

const bornes = coupes.map((t) => {
  const dans = pauses.find((p) => t >= p.debut_s && t <= p.fin_s);
  if (!dans) {
    const proches = pauses.map((p) => `${p.debut_s.toFixed(2)}–${p.fin_s.toFixed(2)}`).join(" · ");
    throw new Error(
      `la coupe à ${t} s ne tombe dans aucun silence de la prise — ce n'est pas la même prise, ` +
      `ou le texte a changé. Silences détectés : ${proches}.`
    );
  }
  return dans;
});

const segments = [];
let curseur = 0;
for (const b of bornes) { segments.push({ debut_s: curseur, fin_s: b.debut_s }); curseur = b.fin_s; }
/* la prise finit sur un souffle : on s'arrête au dernier silence plutôt qu'à la fin du fichier */
const queue = pauses[pauses.length - 1];
segments.push({ debut_s: curseur, fin_s: queue.fin_s >= duree_passe - 0.05 ? queue.debut_s : duree_passe });

const trace = [];
const morceaux = [];
segments.forEach((seg, i) => {
  const ligne = lignes[i];
  const dit = seg.fin_s - seg.debut_s;
  const creneau = ligne.fin_s - ligne.debut_s;
  const tempo = Math.max(1, dit / creneau);
  if (tempo > TEMPO_MAX) {
    throw new Error(
      `ligne ${i + 1} « ${ligne.vo} » : ${dit.toFixed(2)} s à tenir en ${creneau.toFixed(2)} s, ` +
      `soit ${tempo.toFixed(2)}× — au-delà de ${TEMPO_MAX}× la voix s'entend accélérée. ` +
      `Raccourcir le texte ou allonger le créneau dans episode.json.`
    );
  }
  const fichier = join(WORK, `vo-l${i + 1}.wav`);
  ff(["-ss", s2(seg.debut_s), "-to", s2(seg.fin_s), "-i", SOURCE,
      "-filter:a", `atempo=${tempo.toFixed(6)}`, "-ar", "48000", "-ac", "2", fichier]);
  morceaux.push({ fichier, debut_s: ligne.debut_s });
  trace.push({
    ligne: i + 1, vo: ligne.vo,
    dit_s: +dit.toFixed(3), creneau_s: +creneau.toFixed(3), tempo: +tempo.toFixed(3), cale_a_s: ligne.debut_s,
  });
});

/* Chaque ligne est décalée à son timecode, puis toutes sont mélangées sur 15 s de silence :
   la piste tombe pile sur le bloc méthode et se pose telle quelle dans le montage. */
const debut = EP.methode.debut_s;
const duree = EP.methode.fin_s - debut;
const entrees = morceaux.flatMap((m) => ["-i", m.fichier]);
const decales = morceaux.map((m, i) => `[${i}:a]adelay=${Math.round((m.debut_s - debut) * 1000)}:all=1[d${i}]`).join(";");
const melange = morceaux.map((_, i) => `[d${i}]`).join("");
ff([...entrees,
    "-filter_complex", `${decales};${melange}amix=inputs=${morceaux.length}:normalize=0:dropout_transition=0[v];[v]apad[o]`,
    "-map", "[o]", "-t", s2(duree), "-ar", "48000", "-ac", "2", "-c:a", "pcm_s16le", SORTIE]);

writeFileSync(DECOUPE, JSON.stringify({
  source: "audio/vo-methode-passe-unique.mp3",
  variante: EP.variante,
  voix: EP.methode.voix,
  passe_duree_s: +duree_passe.toFixed(3),
  pauses_detectees: pauses.length,
  coupes_s: coupes,
  pauses_retenues_s: bornes.map((b) => +b.duree_s.toFixed(3)),
  tempo_max: TEMPO_MAX,
  lignes: trace,
}, null, 1) + "\n");

console.log(`✅ ${SORTIE} — variante ${VARIANTE}, ${duree} s, ${trace.length} lignes calées`);
for (const t of trace) {
  console.log(`   ${String(t.ligne).padStart(2)} · ${t.dit_s.toFixed(2)}s → ${t.creneau_s.toFixed(2)}s (${t.tempo.toFixed(2)}×)  « ${t.vo} »`);
}
