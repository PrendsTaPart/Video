#!/usr/bin/env node
// QA gate for the hero film, per brief §"QA (npm run qa:hero)".
// Fails (non-zero exit) on any check below. Run from the hero-video/ directory.
import { readFileSync, existsSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import path from 'node:path';

const ROOT = path.dirname(path.dirname(fileURLToPath(import.meta.url)));
const hero = JSON.parse(readFileSync(path.join(ROOT, 'data/hero.json'), 'utf8'));

const failures = [];
const warn = (msg) => console.warn('  ⚠  ' + msg);
const fail = (msg) => failures.push(msg);

// 1. Le "clin" doit sonner exactement 3 fois.
if (!Array.isArray(hero.clin.atSeconds) || hero.clin.atSeconds.length !== 3) {
  fail(`Le "clin" doit être référencé exactement 3 fois (trouvé: ${hero.clin.atSeconds?.length ?? 0}).`);
}
if (hero.clin.status !== 'READY' ) {
  warn(`Le fichier du clin (${hero.clin.file}) n'est pas encore un vrai enregistrement (status: ${hero.clin.status}). Le rendu final ne doit pas sortir tant que ce n'est pas résolu.`);
}

// 2. S4 doit rester intouchée (45s).
const s4 = hero.sequences.find((s) => s.id === 'S4');
if (!s4 || s4.durationSeconds !== 45 || !s4.locked) {
  fail('S4 doit durer exactement 45s et porter locked:true. Ne jamais la raccourcir.');
}

// 3. Les balayages sans->avec durent 0.7s, avec->sans durent 0.4s.
if (hero.wipe.sansToAvec.durationSeconds !== 0.7) {
  fail(`Le balayage bleu (sans->avec) doit durer 0.7s (trouvé: ${hero.wipe.sansToAvec.durationSeconds}s).`);
}
if (hero.wipe.avecToSans.durationSeconds !== 0.4) {
  fail(`Le repli gris (avec->sans) doit durer 0.4s (trouvé: ${hero.wipe.avecToSans.durationSeconds}s).`);
}
if (hero.wipe.sansToAvec.atSeconds.length !== 3) {
  fail(`Le balayage bleu doit apparaître exactement 3 fois (trouvé: ${hero.wipe.sansToAvec.atSeconds.length}).`);
}
if (hero.wipe.avecToSans.atSeconds.length !== 2) {
  fail(`Le repli gris doit apparaître exactement 2 fois (trouvé: ${hero.wipe.avecToSans.atSeconds.length}).`);
}

// 4. Le beat Jarvis (compréhension peu importe qui parle en cuisine) ne doit
//    plus contenir de volet en langue étrangère (le commis en espagnol a été
//    retiré sur demande explicite : "enlève toutes les voix anglais").
const s4beats = Object.fromEntries((s4?.beats ?? []).map((b) => [b.id, b]));
if (s4beats['s4-beatB-jarvis-commis']) {
  fail('Le beat commis (langue étrangère) doit être supprimé, pas seulement ignoré.');
}
if (!s4beats['s4-beatB-jarvis-chef1'] || !s4beats['s4-beatB-jarvis-chef2']) {
  fail('Le beat Jarvis doit conserver ses deux volets chef1/chef2 (en français).');
}

// 5. Aucun nom de marque concurrente dans les données ou le code de la composition.
const COMPETITOR_NAMES = ['Zenchef', 'TheFork', 'L\'Addition', 'Addition', 'Tiller', 'Lightspeed', 'Deliverect', 'Innovorder'];
const textBlobs = [
  readFileSync(path.join(ROOT, 'data/hero.json'), 'utf8'),
  readFileSync(path.join(ROOT, 'index.html'), 'utf8'),
  readFileSync(path.join(ROOT, 'hero-build.js'), 'utf8'),
];
for (const name of COMPETITOR_NAMES) {
  for (const blob of textBlobs) {
    if (blob.includes(name)) fail(`Nom de marque concurrente détecté: "${name}".`);
  }
}

// 6. Chaque asset référencé dans hero.json doit exister sur disque.
function collectAssetPaths(node, out) {
  if (node && typeof node === 'object') {
    if (node.source) {
      const keys = Array.isArray(node.source.key) ? node.source.key : [node.source.key];
      for (const k of keys) {
        if (typeof k === 'string' && k.startsWith('assets/')) out.push(k);
      }
      if (node.source.logo) out.push(node.source.logo);
    }
    if (node.vo?.file) out.push(node.vo.file);
    for (const v of Object.values(node)) collectAssetPaths(v, out);
  } else if (Array.isArray(node)) {
    for (const v of node) collectAssetPaths(v, out);
  }
}
const assetPaths = [];
collectAssetPaths(hero.sequences, assetPaths);
const missing = [...new Set(assetPaths)].filter((p) => !existsSync(path.join(ROOT, p)));
for (const m of missing) fail(`Asset référencé mais absent du disque: ${m}`);

// --- Report ---
console.log(`QA hero-video — ${failures.length === 0 ? 'PASS' : 'FAIL'}`);
if (failures.length) {
  console.log('\nÉchecs:');
  for (const f of failures) console.log('  ✗ ' + f);
  process.exit(1);
}
console.log('Tous les contrôles mécaniques passent. Rappel: le clin, les SFX et la musique restent des enregistrements réels en attente (voir README).');
