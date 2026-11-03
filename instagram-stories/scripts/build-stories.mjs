#!/usr/bin/env node
// Builds 5 Instagram Stories (1080x1920) from data/stories-source.json.
// Each story: HOOK card (logo + punchy line) -> BODY (footage pillarboxed,
// caption, watermark, VO) -> CTA card (logo + story punchline + button,
// shared brand VO). Timing computed from real audio durations (ffprobe) —
// never hand-authored, see hero-video/scripts/retime.mjs for why a guessed
// slot causes audible overlaps or dead air. Video/audio elements are always
// direct timed children, never nested inside another timed wrapper (that
// freezes/mutes them — see hero-video/scripts/build-static.mjs).
import { execSync } from 'node:child_process';
import { readFileSync, writeFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import path from 'node:path';

const ROOT = path.dirname(path.dirname(fileURLToPath(import.meta.url)));
const sourceFile = process.argv[2] || 'data/stories-source.json';
const src = JSON.parse(readFileSync(path.join(ROOT, sourceFile), 'utf8'));

const PAD = 0.4;
const CTA_TAIL = 2.5;
const HOOK_AIR = 0.25; // silence between the end of the bell and the first word
const round2 = (n) => Math.round(n * 100) / 100;

function realDuration(file) {
  const abs = path.join(ROOT, file);
  const out = execSync(`ffprobe -v error -show_entries format=duration -of csv=p=0 "${abs}"`).toString().trim();
  return parseFloat(out);
}

// The hook card lasts exactly as long as the bell needs to ring out, plus a
// beat of air. Hard-coding it shorter than the bell (it was 1.1s against a
// 1.52s sample) let the bell's tail run over the first syllable of the VO on
// every single story — the overlap the client heard.
const CLIN_DUR = round2(realDuration(src.clin));
const HOOK_DUR = round2(CLIN_DUR + HOOK_AIR);

const esc = (s) =>
  String(s ?? '')
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;');

const CSS = `
  :root { --navy: #1B2A41; --cream: #FCF9E6; --blue: #007BFF; --orange: #FFA500; }
  html, body { margin: 0; padding: 0; background: #000; }
  #ad {
    position: relative; width: 1080px; height: 1920px; overflow: hidden;
    background: var(--navy); font-family: "Nunito", "Poppins", system-ui, sans-serif;
  }
  .clip { position: absolute; inset: 0; visibility: hidden; }
  /* Landscape sources sit letterboxed on the brand navy ground rather than
     being blown up and cropped to 9:16, which would cut heads off. */
  video.media-fill { position: absolute; top: 50%; right: auto; bottom: auto; left: 0; width: 1080px; height: 607.5px; transform: translateY(-50%); object-fit: cover; display: block; }
  /* Sources already shot 9:16 fill the whole frame. */
  video.media-fill.native-vertical { top: 0; height: 1920px; transform: none; }

  .hook-card { display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 40px; background: var(--cream); text-align: center; padding: 0 90px; }
  .hook-card .logo { width: 220px; height: auto; }
  .hook-card .hook-line { color: var(--navy); font-size: 76px; font-weight: 900; line-height: 1.15; }

  .watermark { top: 64px; left: 56px; width: auto; height: auto; bottom: auto; right: auto; }
  .watermark img { width: 140px; height: auto; filter: drop-shadow(0 2px 10px rgba(0,0,0,0.35)); }

  .caption-bar { top: auto; height: auto; left: 0; right: 0; bottom: 0; padding: 48px 64px 120px; background: linear-gradient(to top, rgba(15,26,35,0.95) 0%, rgba(15,26,35,0.8) 55%, rgba(15,26,35,0) 100%); }
  .caption-bar span { display: block; color: #fff; font-size: 58px; font-weight: 800; line-height: 1.25; text-wrap: balance; }

  .cta-card { display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 36px; background: var(--cream); text-align: center; padding: 0 90px; }
  .cta-card .logo { width: 260px; height: auto; }
  .cta-card .punchline { color: var(--navy); font-size: 58px; font-weight: 900; line-height: 1.2; max-width: 880px; }
  .cta-card .cta-sub { color: #fff; background: var(--orange); font-size: 40px; font-weight: 800; padding: 24px 52px; border-radius: 999px; }
`;

const JS = `
(function () {
  var data = JSON.parse(document.getElementById('ad-data').textContent);
  var tl = gsap.timeline({ paused: true });
  document.querySelectorAll('.clip.beat').forEach(function (el) {
    var start = parseFloat(el.getAttribute('data-start'));
    if (Number.isNaN(start)) return;
    tl.fromTo(el, { opacity: 0, scale: 0.97 }, { opacity: 1, scale: 1, duration: 0.3, ease: 'power1.out' }, start);
  });
  var cta = document.querySelector('.cta-card');
  if (cta) {
    var s = parseFloat(cta.getAttribute('data-start'));
    tl.fromTo(cta.querySelector('.logo'), { opacity: 0, scale: 0.85 }, { opacity: 1, scale: 1, duration: 0.5, ease: 'back.out(1.6)' }, s);
    tl.fromTo(cta.querySelector('.punchline'), { opacity: 0, y: 16 }, { opacity: 1, y: 0, duration: 0.4, ease: 'power1.out' }, s + 0.25);
    tl.fromTo(cta.querySelector('.cta-sub'), { opacity: 0, y: 16 }, { opacity: 1, y: 0, duration: 0.4, ease: 'power1.out' }, s + 0.5);
  }
  tl.duration(data.durationSeconds);
  window.__timelines = window.__timelines || {};
  window.__timelines['ad'] = tl;
})();
`;

let idCounter = 0;
const nextId = (p) => `${p}-${++idCounter}`;

function buildStory(story) {
  idCounter = 0;
  const out = [];
  let cursor = 0;

  // HOOK
  const hookStart = cursor;
  out.push(`<div id="${nextId('hook')}" class="clip beat hook-card" data-start="${hookStart}" data-duration="${HOOK_DUR}" data-track-index="0">`);
  out.push(`<img class="logo" src="${esc(src.logo)}" alt="FoodEatUp" />`);
  out.push(`<div class="hook-line">${esc(story.hook)}</div>`);
  out.push('</div>');
  out.push(`<audio id="${nextId('audio')}" class="clip" src="${esc(src.clin)}" data-start="${hookStart}" data-duration="${CLIN_DUR}" data-track-index="1" data-volume="1" data-has-audio="true" preload="auto"></audio>`);
  cursor += HOOK_DUR;

  // BODY
  const voDur = realDuration(story.vo);
  const videoDur = realDuration(story.video);
  // Never truncate mid-action: some source clips are deliberate single
  // continuous shots choreographed beat-by-beat over their full length
  // (door opens -> action -> resolution) — cutting at VO length alone
  // would chop the payoff. Body runs at least as long as the footage.
  const bodyDur = round2(Math.max(voDur + PAD, videoDur));
  const bodyStart = round2(cursor);
  // Probe the real aspect: a source already shot 9:16 fills the frame,
  // anything wider is letterboxed instead of cropped.
  const dims = execSync(
    `ffprobe -v error -select_streams v:0 -show_entries stream=width,height -of csv=p=0 "${path.join(ROOT, story.video)}"`,
  ).toString().trim().split(',').map(Number);
  const isVertical = dims[1] > dims[0];
  const fillClass = isVertical ? 'media-fill native-vertical' : 'media-fill';
  out.push(`<video id="${nextId('video')}" class="clip beat ${fillClass}" src="${esc(story.video)}" data-start="${bodyStart}" data-duration="${bodyDur}" data-track-index="2" muted autoplay playsinline></video>`);
  out.push(`<div id="${nextId('caption')}" class="clip beat caption-bar" data-start="${bodyStart}" data-duration="${bodyDur}" data-track-index="3"><span>${esc(story.caption)}</span></div>`);
  out.push(`<div id="${nextId('wm')}" class="clip beat watermark" data-start="${bodyStart}" data-duration="${bodyDur}" data-track-index="4"><img src="${esc(src.logo)}" alt="" /></div>`);
  out.push(`<audio id="${nextId('audio')}" class="clip" src="${esc(story.vo)}" data-start="${bodyStart}" data-duration="${bodyDur}" data-track-index="2005" data-volume="1" data-has-audio="true" preload="auto"></audio>`);
  cursor = bodyStart + bodyDur;

  // CTA
  const ctaVoDur = realDuration(src.ctaVo);
  const ctaDur = round2(ctaVoDur + CTA_TAIL);
  const ctaStart = round2(cursor);
  out.push(`<div id="${nextId('cta')}" class="clip beat cta-card" data-start="${ctaStart}" data-duration="${ctaDur}" data-track-index="6">`);
  out.push(`<img class="logo" src="${esc(src.logo)}" alt="FoodEatUp" />`);
  out.push(`<div class="punchline">${esc(story.punchline)}</div>`);
  out.push(`<div class="cta-sub">${esc(src.ctaSub)}</div>`);
  out.push('</div>');
  out.push(`<audio id="${nextId('audio')}" class="clip" src="${esc(src.ctaVo)}" data-start="${ctaStart}" data-duration="${ctaDur}" data-track-index="2010" data-volume="1" data-has-audio="true" preload="auto"></audio>`);
  cursor = ctaStart + ctaDur;

  const durationSeconds = round2(cursor);
  const adData = { durationSeconds };
  const markup = out.join('\n');

  const html = `<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8" />
<title>FoodEatUp — Story ${esc(story.id)}</title>
<style>${CSS}</style>
</head>
<body>

<script id="ad-data" type="application/json">${JSON.stringify(adData)}</script>

<div id="ad" class="composition" data-composition-id="ad" data-width="1080" data-height="1920" data-start="0" data-duration="${durationSeconds}">
${markup}
</div>

<script>window.__timelines = window.__timelines || {};</script>
<script src="assets/vendor/gsap.min.js"></script>
<script>${JS}</script>
</body>
</html>
`;
  writeFileSync(path.join(ROOT, `${story.id}.html`), html);
  console.log(`build-stories: ${story.id}.html — ${durationSeconds}s`);
}

src.stories.forEach(buildStory);
