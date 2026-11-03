#!/usr/bin/env node
// Bakes data/hero.json into static markup inside index.html.
//
// Why: HyperFrames' render pipeline plans its audio mix from a STATIC parse
// of index.html (it needs the list of <audio>/<video> elements before it
// launches Chrome). Elements created at runtime by client-side JS are
// invisible to that planning pass — confirmed by a real render: the visual
// output was correct but silent (`hasAudio:false`) even though `npx
// hyperframes validate`, which DOES execute the page in a live browser, saw
// the audio elements and even validated their durations. The fix is to
// generate literal markup here rather than construct the DOM at runtime.
//
// hero.json remains the single source of truth — nothing here is
// hand-authored, this script is deterministic and re-run after any edit to
// data/hero.json (see package.json → "build").
import { readFileSync, writeFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import path from 'node:path';

const ROOT = path.dirname(path.dirname(fileURLToPath(import.meta.url)));
const hero = JSON.parse(readFileSync(path.join(ROOT, 'data/hero.json'), 'utf8'));

const esc = (s) =>
  String(s ?? '')
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;');

const STATE_CLASS = { avec: 'seq-avec', sans: 'seq-sans', neutre: 'seq-neutre' };
let trackCounter = 0;
const out = [];

let idCounter = 0;
function nextId(prefix) {
  idCounter += 1;
  return `${prefix}-${idCounter}`;
}

function clipOpen(cls, start, duration, track, extraAttrs = '') {
  out.push(
    `<div class="clip${cls ? ' ' + cls : ''}" data-start="${start}" data-duration="${duration}" data-track-index="${track}"${extraAttrs ? ' ' + extraAttrs : ''}>`,
  );
}
function clipClose() {
  out.push('</div>');
}
// Audio/video timing lives on the media element itself, never on a wrapping
// div: HyperFrames' StaticGuard freezes/mutes media nested inside a div that
// also carries data-start (confirmed by a real render going silent). Each
// media element also needs a unique id — the renderer's static discovery
// pass requires one to find <audio> at all ("this audio will be SILENT in
// renders" without it).
function audioTag(file, start, duration, track) {
  const id = nextId('audio');
  out.push(
    `<audio id="${id}" class="clip" src="${esc(file)}" data-start="${start}" data-duration="${duration}" data-track-index="${track}" data-volume="1" data-has-audio="true" preload="auto"></audio>`,
  );
}
function videoTag(cls, src, start, duration, track, mediaStart) {
  const id = nextId('video');
  out.push(
    `<video id="${id}" class="clip${cls ? ' ' + cls : ''}" src="${esc(src)}" data-start="${start}" data-duration="${duration}" data-track-index="${track}" muted autoplay playsinline data-media-start="${mediaStart || 0}"></video>`,
  );
}

// All motion graphics are wordless by design: no HTML labels, no baked-in
// captions. Everything they used to spell out in text is already said in
// the beat's own VO — repeating it as on-screen text was pure clutter (and
// exactly what the brief itself warns against: the visual adds information,
// it never repeats what's already said out loud).
function motionGraphic(key, beat) {
  if (key === 'convergence-multicanal') {
    const icons = (beat.source && beat.source.icons) || [];
    const target = (beat.source && beat.source.targetIcon) || 'assets/brand/foodeatup-mark-eight.png';
    out.push('<div class="converge-stage">');
    const corners = ['tl', 'tr', 'bl', 'br'];
    corners.forEach((c, i) => {
      if (!icons[i]) return;
      out.push(`<div class="converge-node" data-corner="${c}"><img src="${esc(icons[i])}" alt="" /></div>`);
    });
    out.push(`<div class="converge-target"><img src="${esc(target)}" alt="" /></div>`);
    out.push('</div>');
    return;
  }
  if (key === 'notification-cascade-iris') {
    const icon = (beat.source && beat.source.icon) || 'assets/image/icons/icon-notification.jpg';
    out.push('<div class="iris-stage">');
    for (let s = 1; s <= 3; s++) {
      out.push(`<div class="iris-device" data-slot="${s}"><div class="toast"><img src="${esc(icon)}" alt="" /></div></div>`);
    }
    out.push('</div>');
    return;
  }
  if (key === 'noir') {
    out.push('<div class="black-frame"></div>');
    return;
  }
  if (key === 'logo-cta') {
    const logo = (beat.source && beat.source.logo) || 'assets/brand/foodeatup-logo-mascot.png';
    out.push(`<div class="cta-card"><img class="logo" src="${esc(logo)}" alt="FoodEatUp" /></div>`);
    return;
  }
  // trois-visages-silence is handled directly in renderBeat (needs the
  // beat's own timing on each <video>, which this helper doesn't receive).
  out.push('<div style="position:absolute;inset:0;background:#111"></div>');
}

function renderTriptych(keys, start, duration, track) {
  out.push('<div class="triptych">');
  keys.forEach((k, i) => {
    out.push('<div class="panel">');
    videoTag(null, k, start, duration, track * 10 + i);
    out.push('</div>');
  });
  out.push('</div>');
}

function renderMedia(beat, track) {
  const src = beat.source;
  const keys = Array.isArray(src.key) ? src.key : [src.key];

  if (keys.length > 1) {
    renderTriptych(keys, beat.fromSeconds, beat.durationSeconds, track);
    return;
  }

  const key = keys[0];
  const isVideo = /\.mp4$/i.test(key);
  if (isVideo) {
    videoTag('media-fill', key, beat.fromSeconds, beat.durationSeconds, track, src.mediaStartSeconds || 0);
  } else {
    clipOpen('media-fill', beat.fromSeconds, beat.durationSeconds, track);
    out.push(`<img src="${esc(key)}" alt="" />`);
    clipClose();
  }
}

function renderBeat(beat, track) {
  const src = beat.source;
  if (src) {
    if (src.kind === 'footage' || src.kind === 'image') {
      renderMedia(beat, track);
    } else if (src.kind === 'motion' && src.key === 'trois-visages-silence') {
      renderTriptych(
        [
          'assets/video/hero-portrait-chef.mp4',
          'assets/video/hero-portrait-serveur.mp4',
          'assets/video/hero-portrait-directeur.mp4',
        ],
        beat.fromSeconds,
        beat.durationSeconds,
        track,
      );
    } else if (src.kind === 'motion') {
      clipOpen(null, beat.fromSeconds, beat.durationSeconds, track);
      motionGraphic(src.key, beat);
      clipClose();
    }
  }

  // No burned-in speaker tags or subtitles: the film is meant to be watched
  // with sound, and the .vtt track (scripts outside this build) already
  // carries the same text for accessibility / SEO without cluttering the
  // frame. Only the audio track is emitted here.
  if (beat.vo && beat.vo.file) {
    audioTag(beat.vo.file, beat.fromSeconds, beat.durationSeconds, track + 2000);
  }
}

for (const seq of hero.sequences) {
  out.push(
    `<div class="${STATE_CLASS[seq.state] || 'seq-avec'}" data-sequence-id="${esc(seq.id)}" style="position:absolute;inset:0">`,
  );
  for (const beat of seq.beats) {
    const track = trackCounter++;
    renderBeat(beat, track);
  }
  out.push('</div>');
}

// Blue wipe (sans -> avec) and grey snap (avec -> sans) overlays.
(hero.wipe.sansToAvec.atSeconds || []).forEach((t, i) => {
  clipOpen('wipe-sweep', t - hero.wipe.sansToAvec.durationSeconds / 2, hero.wipe.sansToAvec.durationSeconds, 9000 + i, 'data-wipe-kind="sans-to-avec"');
  out.push('<div class="line"></div>');
  clipClose();
});
(hero.wipe.avecToSans.atSeconds || []).forEach((t, i) => {
  clipOpen('wipe-sweep snap-sweep', t - hero.wipe.avecToSans.durationSeconds / 2, hero.wipe.avecToSans.durationSeconds, 9100 + i, 'data-wipe-kind="avec-to-sans"');
  out.push('<div class="line"></div>');
  clipClose();
});

// The "clin" — exactly 3 occurrences.
if (hero.clin && hero.clin.file) {
  (hero.clin.atSeconds || []).forEach((t, i) => audioTag(hero.clin.file, t, 1.2, 9200 + i));
}

// Music beds, one per sequence matching its avec/sans/resolution state.
// Tiled back-to-back across the full sequence length (data-duration per
// tag never exceeds the bed's real length) so a short bed never runs out
// and leaves silence for the rest of the scene — confirmed happening
// before this fix on S6/S7, both scored with the 15s "resolution" bed
// while running 25-30s.
if (hero.musicBeds) {
  for (const seq of hero.sequences) {
    const bedKey = seq.music === 'silence' ? null : seq.music;
    const bed = bedKey && hero.musicBeds[bedKey];
    if (!bed) continue;
    const bedDuration = bed.naturalDurationSeconds || seq.durationSeconds;
    let offset = 0;
    while (offset < seq.durationSeconds) {
      const clipDuration = Math.min(bedDuration, seq.durationSeconds - offset);
      audioTag(bed.file, seq.fromSeconds + offset, clipDuration, 9300 + trackCounter++);
      offset += bedDuration;
    }
  }
}

// Punctual SFX cues.
(hero.sfxCues || []).forEach((cue, i) => audioTag(cue.file, cue.atSeconds, 1.5, 9400 + i));

const staticMarkup = out.join('\n');

const indexPath = path.join(ROOT, 'index.html');
let html = readFileSync(indexPath, 'utf8');

// Keep the root composition's data-duration in sync with hero.json — it's
// hand-authored markup, not part of the generated block below, and was
// found stale (still "225" after a retime dropped the real total to
// 208.06s) because nothing else here ever touched it.
html = html.replace(
  /(<div id="hero" class="composition"[^>]*data-duration=")[^"]*(")/,
  `$1${hero.durationSeconds}$2`,
);

const heroDivOpenMarker = /(<div id="hero"[^>]*>)([\s\S]*?)(<\/div>\s*<script>window\.__timelines)/;
if (!heroDivOpenMarker.test(html)) {
  throw new Error('build-static: could not find the #hero container to inject into — check index.html structure.');
}
html = html.replace(heroDivOpenMarker, (_m, open, _old, tail) => `${open}\n${staticMarkup}\n${tail}`);

// Re-inline the latest hero.json (kept in sync, used by hero-build.js for
// the GSAP timeline logic — the wipe tweens, Beat A/D animations).
const dataMarker = '<script id="hero-data" type="application/json">';
const start = html.indexOf(dataMarker) + dataMarker.length;
const end = html.indexOf('</script>', start);
const heroJsonText = readFileSync(path.join(ROOT, 'data/hero.json'), 'utf8').trim();
html = html.slice(0, start) + '\n' + heroJsonText + '\n' + html.slice(end);

writeFileSync(indexPath, html);
console.log(`build-static: wrote ${staticMarkup.split('\n').length} static markup lines into index.html`);
