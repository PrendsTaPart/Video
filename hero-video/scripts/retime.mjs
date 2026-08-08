#!/usr/bin/env node
// Retimes data/hero.json against REAL audio durations (ffprobe), removing:
// 1. Voice overlaps — beats whose VO is longer than their old slot were
//    bleeding into the next beat's VO (confirmed: all 6 narrator lines,
//    s1-chef, s2-serveur, s6-chef, s4-beatD-iris).
// 2. Dead-air blanks — beats whose VO is shorter than their old slot held
//    the frame in silence before cutting.
// Every VO beat becomes exactly its real audio length + a short breathing
// pad. S4 stays locked at exactly 45s (its slack is redistributed evenly
// across its own beats, never dropped). Sequence boundaries, wipe/clin/sfx
// cue timings, and music-bed tiling are all recomputed from the new beat
// times — nothing here is hand-authored, re-run after any VO change.
import { execSync } from 'node:child_process';
import { readFileSync, writeFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import path from 'node:path';

const ROOT = path.dirname(path.dirname(fileURLToPath(import.meta.url)));
const heroPath = path.join(ROOT, 'data/hero.json');
const hero = JSON.parse(readFileSync(heroPath, 'utf8'));

const PAD = 0.4; // standard breathing room after a line before the cut
const round2 = (n) => Math.round(n * 100) / 100;

const durCache = new Map();
function realDuration(file) {
  if (durCache.has(file)) return durCache.get(file);
  const abs = path.join(ROOT, file);
  const out = execSync(`ffprobe -v error -show_entries format=duration -of csv=p=0 "${abs}"`).toString().trim();
  const d = parseFloat(out);
  durCache.set(file, d);
  return d;
}

// --- Beats: assign real-audio-based durations, sequence by sequence ---
let cursor = 0;
for (const seq of hero.sequences) {
  seq.fromSeconds = round2(cursor);

  const natural = seq.beats.map((beat) => {
    if (beat.id === 's0-cuisine-vide') {
      // Establishing shot: keep a short silent hold after the line for the
      // grey<->colour "dédoublement" visual beat described in its note —
      // shortened from the original fixed 15s, not eliminated.
      return round2(realDuration(beat.vo.file) + 3.0);
    }
    if (beat.id === 's7-logo-cta') {
      // No VO; trims the old 12s static logo hold to keep pace without
      // losing brand presence.
      return 8;
    }
    if (beat.vo && beat.vo.file) {
      return round2(realDuration(beat.vo.file) + PAD);
    }
    // No VO, no special case (s7-triptyque, s7-noir): deliberate silent
    // beats from the brief, left untouched.
    return beat.durationSeconds;
  });

  let durations = natural;
  if (seq.locked) {
    // S4 must total exactly its locked duration. Redistribute the
    // difference evenly across its own beats instead of leaving one giant
    // blank or shaving the lock.
    const sum = natural.reduce((a, b) => a + b, 0);
    const slack = (seq.durationSeconds - sum) / natural.length;
    durations = natural.map((d) => round2(d + slack));
    const drift = round2(seq.durationSeconds - durations.reduce((a, b) => a + b, 0));
    durations[durations.length - 1] = round2(durations[durations.length - 1] + drift);
  }

  let beatCursor = cursor;
  seq.beats.forEach((beat, i) => {
    beat.fromSeconds = round2(beatCursor);
    beat.durationSeconds = durations[i];
    beatCursor += durations[i];
  });

  seq.durationSeconds = round2(beatCursor - cursor);
  cursor = beatCursor;
}

const totalDuration = round2(cursor);
hero.durationSeconds = totalDuration;

if (hero.sequences.find((s) => s.id === 'S4').durationSeconds !== 45) {
  throw new Error('retime: S4 drifted off 45s, aborting.');
}

// --- Wipe transitions: recompute at every sans<->avec sequence boundary ---
const sansToAvec = [];
const avecToSans = [];
for (let i = 0; i < hero.sequences.length - 1; i++) {
  const a = hero.sequences[i];
  const b = hero.sequences[i + 1];
  if (a.state === 'sans' && b.state === 'avec') sansToAvec.push(b.fromSeconds);
  if (a.state === 'avec' && b.state === 'sans') avecToSans.push(b.fromSeconds);
}
hero.wipe.sansToAvec.atSeconds = sansToAvec;
hero.wipe.avecToSans.atSeconds = avecToSans;

// --- Beat lookup by id, for clin/sfx retargeting ---
const beatsById = new Map();
for (const seq of hero.sequences) for (const beat of seq.beats) beatsById.set(beat.id, beat);
const b = (id) => beatsById.get(id);

// --- Clin: 3 diegetic bell moments, retargeted to the same beats as before ---
hero.clin.atSeconds = [
  round2(b('s4-beatC-envoi-chef').fromSeconds), // "Plat prêt." — bell rings on the line itself
  round2(b('s6-directeur').fromSeconds + Math.max(0, b('s6-directeur').durationSeconds - 0.5)), // closing bell as he states his numbers
  round2(b('s7-logo-cta').fromSeconds + Math.min(1.5, b('s7-logo-cta').durationSeconds * 0.3)), // soft solo wink before the CTA
];

// --- Punctual SFX cues: retargeted to the same beats as before ---
hero.sfxCues = [
  { file: 'assets/sfx/son-scanner-bip.mp3', atSeconds: round2(b('s2-chef').fromSeconds + 1), note: 'Chef scanne le carton (S2).' },
  { file: 'assets/sfx/son-jarvis-ecoute.mp3', atSeconds: round2(b('s4-beatB-jarvis-chef1').fromSeconds), note: 'Jarvis écoute (beat B, chef).' },
  { file: 'assets/sfx/son-jarvis-compris.mp3', atSeconds: round2(b('s4-beatB-jarvis-chef2').fromSeconds), note: 'Jarvis a compris (beat B, chef2).' },
  { file: 'assets/sfx/son-imprimante-z.mp3', atSeconds: round2(b('s6-serveur').fromSeconds + 0.3), note: 'Ticket Z (S6).' },
  { file: 'assets/sfx/son-iris-publie.mp3', atSeconds: round2(b('s4-beatD-iris').fromSeconds), note: 'Iris publie (beat D).' },
  { file: 'assets/sfx/son-validation-haccp.mp3', atSeconds: round2(b('s6-chef').fromSeconds), note: 'Photo IA nettoyage (S6).' },
];

// --- Music beds: record real duration so build-static.mjs can tile them
// across a sequence instead of letting them run out mid-scene (silence). ---
for (const key of Object.keys(hero.musicBeds)) {
  hero.musicBeds[key].naturalDurationSeconds = round2(realDuration(hero.musicBeds[key].file));
}

writeFileSync(heroPath, JSON.stringify(hero, null, 2) + '\n');
console.log(`retime: new total duration ${totalDuration}s (was 225s)`);
console.log(`retime: wipe sans->avec @ ${sansToAvec.join(', ')} | avec->sans @ ${avecToSans.join(', ')}`);
console.log(`retime: clin @ ${hero.clin.atSeconds.join(', ')}`);
