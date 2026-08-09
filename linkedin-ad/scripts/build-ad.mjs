#!/usr/bin/env node
// Builds the LinkedIn ad from data/ad-source.json: computes real timing from
// ffprobe (never hand-authored, see hero-video/scripts/retime.mjs for why —
// a hand-guessed slot shorter than the real VO causes audible overlaps, a
// slot too long leaves dead air), writes the fully-timed data/ad.json, and
// bakes static markup into index.html (HyperFrames plans its audio mix from
// a static parse of the HTML before launching Chrome — elements built by
// runtime JS are invisible to it and render silently).
import { execSync } from 'node:child_process';
import { readFileSync, writeFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import path from 'node:path';

const ROOT = path.dirname(path.dirname(fileURLToPath(import.meta.url)));
const src = JSON.parse(readFileSync(path.join(ROOT, 'data/ad-source.json'), 'utf8'));

const PAD = 0.4; // breathing room after each line before the cut
const round2 = (n) => Math.round(n * 100) / 100;

function realDuration(file) {
  const abs = path.join(ROOT, file);
  const out = execSync(`ffprobe -v error -show_entries format=duration -of csv=p=0 "${abs}"`).toString().trim();
  return parseFloat(out);
}

let cursor = 0;
const beats = src.beats.map((b) => {
  const dur = round2(realDuration(b.vo) + PAD);
  const beat = { ...b, fromSeconds: round2(cursor), durationSeconds: dur };
  cursor += dur;
  return beat;
});

// The closing card: sting, then the tagline, then what FoodEatUp actually is.
// Two things were wrong before. The sting fired 0.15s into the card while the
// tagline VO was already speaking, so it stepped on the first word — the same
// defect the client heard on the stories. And the ad closed on a tagline that
// never says what the product is, so a viewer meeting FoodEatUp on LinkedIn
// learned five benefits and no category. The bell now rings out in the clear
// before anyone speaks, and the explanation follows the tagline.
const STING_AIR = 0.25; // silence between the end of the bell and the first word
const BEAT_GAP = 0.4;   // breath between the tagline and the explanation
const ctaStart = round2(cursor);
const clinDur = round2(realDuration(src.clin));
const clinAt = ctaStart;
const ctaVoAt = round2(ctaStart + clinDur + STING_AIR);
const ctaVoDur = round2(realDuration(src.cta.vo));
const explainAt = round2(ctaVoAt + ctaVoDur + BEAT_GAP);
const explainDur = round2(realDuration(src.cta.explainVo));
// The card is static artwork, not footage, so it can run as long as the two
// lines need without freezing on a last video frame.
const ctaDur = round2(explainAt + explainDur + src.cta.tailHoldSeconds - ctaStart);
const cta = {
  ...src.cta,
  fromSeconds: ctaStart,
  durationSeconds: ctaDur,
  voFromSeconds: ctaVoAt,
  voDurationSeconds: ctaVoDur,
  explainFromSeconds: explainAt,
  explainDurationSeconds: explainDur,
};
cursor = ctaStart + ctaDur;

const ad = {
  title: src.title,
  fps: src.fps,
  width: src.width,
  height: src.height,
  durationSeconds: round2(cursor),
  beats,
  cta,
  clin: { file: src.clin, atSeconds: clinAt, durationSeconds: clinDur },
};
writeFileSync(path.join(ROOT, 'data/ad.json'), JSON.stringify(ad, null, 2) + '\n');

// --- Static markup ---
const esc = (s) =>
  String(s ?? '')
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;');

let idCounter = 0;
const nextId = (prefix) => `${prefix}-${++idCounter}`;
const out = [];

function videoTag(src, start, duration, track) {
  const id = nextId('video');
  out.push(
    `<video id="${id}" class="clip beat media-fill" src="${esc(src)}" data-start="${start}" data-duration="${duration}" data-track-index="${track}" muted autoplay playsinline></video>`,
  );
}
function audioTag(src, start, duration, track) {
  const id = nextId('audio');
  out.push(
    `<audio id="${id}" class="clip" src="${esc(src)}" data-start="${start}" data-duration="${duration}" data-track-index="${track}" data-volume="1" data-has-audio="true" preload="auto"></audio>`,
  );
}

// Video and caption bar are siblings, both timed directly (never nest a
// <video data-start> inside another data-start wrapper — HyperFrames
// freezes it, confirmed by lint: video_nested_in_timed_element).
let track = 0;
ad.beats.forEach((b) => {
  videoTag(b.video, b.fromSeconds, b.durationSeconds, track++);
  const captionId = nextId('caption');
  out.push(
    `<div id="${captionId}" class="clip beat caption-bar" data-start="${b.fromSeconds}" data-duration="${b.durationSeconds}" data-track-index="${track++}"><span>${esc(b.caption)}</span></div>`,
  );
  audioTag(b.vo, b.fromSeconds, b.durationSeconds, 2000 + track++);
});

out.push(`<div id="${nextId('cta')}" class="clip beat cta-card" data-start="${ad.cta.fromSeconds}" data-duration="${ad.cta.durationSeconds}" data-track-index="${track++}">`);
out.push(`<img class="logo" src="${esc(ad.cta.logo)}" alt="FoodEatUp" />`);
out.push(`<div class="cta-line2">${esc(ad.cta.line2)}</div>`);
out.push(`<div class="cta-explain">${esc(ad.cta.explain)}</div>`);
out.push(`<div class="cta-sub">${esc(ad.cta.subCta)}</div>`);
out.push('</div>');
// Each closing sound gets exactly its own slot, back to back — the bell's real
// measured length, then the tagline, then the explanation. Hard-coding 1.5s for
// a 1.52s sample is how the bell used to bleed over the voice.
audioTag(ad.clin.file, ad.clin.atSeconds, ad.clin.durationSeconds, 2000 + track++);
audioTag(ad.cta.vo, ad.cta.voFromSeconds, ad.cta.voDurationSeconds, 2000 + track++);
audioTag(ad.cta.explainVo, ad.cta.explainFromSeconds, ad.cta.explainDurationSeconds, 2000 + track++);

const staticMarkup = out.join('\n');

const indexPath = path.join(ROOT, 'index.html');
let html = readFileSync(indexPath, 'utf8');
html = html.replace(
  /(<div id="ad" class="composition"[^>]*data-duration=")[^"]*(")/,
  `$1${ad.durationSeconds}$2`,
);
const marker = /(<div id="ad"[^>]*>)([\s\S]*?)(<\/div>\s*<script>window\.__timelines)/;
if (!marker.test(html)) throw new Error('build-ad: could not find the #ad container to inject into.');
html = html.replace(marker, (_m, open, _old, tail) => `${open}\n${staticMarkup}\n${tail}`);

const dataMarker = '<script id="ad-data" type="application/json">';
const start = html.indexOf(dataMarker) + dataMarker.length;
const end = html.indexOf('</script>', start);
html = html.slice(0, start) + '\n' + JSON.stringify(ad) + '\n' + html.slice(end);

writeFileSync(indexPath, html);
console.log(`build-ad: total ${ad.durationSeconds}s, wrote ${staticMarkup.split('\n').length} markup lines`);
