#!/usr/bin/env node
// Construit index.html (composition HyperFrames 1080x1920) depuis un fichier timeline JSON.
// Tout le texte, le minutage et les médias viennent du JSON : modifier le JSON puis relancer.
// Le balisage est statique (une div .clip par élément) ; les animations sont pilotées par la
// timeline GSAP « main ».
//
//   node scripts/build.mjs data/reels/reel-01-lancement.json          -> version finale
//   node scripts/build.mjs data/reels/reel-01-lancement.json --draft  -> avec bandeau « version de travail »
//
// Types de scène : photo (media .jpg), video (type:"video"), countdown, clock, grid4, invite,
// menucard, endcard. Options communes : texts[], salle, list, rows, cards, celebrate, trans.
import { readFileSync, writeFileSync } from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const ROOT = path.dirname(path.dirname(fileURLToPath(import.meta.url)));
const SRC = process.argv.slice(2).find((a) => !a.startsWith('--')) || 'data/timeline.json';
const T = JSON.parse(readFileSync(path.join(ROOT, SRC), 'utf8'));
const DRAFT = process.argv.includes('--draft');
const DUR = T.format.duration;

const esc = (s) => String(s ?? '').replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
const r2 = (n) => Math.round(n * 1000) / 1000;
let seed = 2027;
const rnd = () => ((seed = (seed * 16807) % 2147483647) / 2147483647);

const clips = [];
const anim = [];
let id = 0;
const clip = (html, start, end, track, cls = '', style = '') => {
  const cid = `c${++id}`;
  clips.push(`<div id="${cid}" class="clip ${cls}" data-start="${r2(start)}" data-duration="${r2(end - start)}" data-track-index="${track}" style="${style}">${html}</div>`);
  return `#${cid}`;
};
const A = (s) => anim.push(s);

// Texte « cinétique » : chaque mot dans un span, révélé en cascade.
const KINETIC = new Set(['title', 'mid', 'big', 'headline', 'brand', 'tagline', 'low']);
const words = (t) => esc(t).split(' ').map((w) => `<span class="w"><span class="wi">${w}</span></span>`).join(' ');

// Transition d'entrée d'un plan (sauf le premier) : rotation automatique si non précisée.
const TRANS = ['whip', 'zoom', 'flash', 'rise'];
let transIdx = 0;
function enter(sel, s) {
  if (s.start <= 0 || s.trans === 'none') return;
  const t = s.trans ?? TRANS[transIdx++ % TRANS.length];
  if (t === 'whip') A(`tl.fromTo('${sel}', {x:420, filter:'blur(18px)'}, {x:0, filter:'blur(0px)', duration:0.28, ease:'power3.out'}, ${s.start});`);
  else if (t === 'zoom') A(`tl.fromTo('${sel}', {scale:1.35, opacity:0}, {scale:1, opacity:1, duration:0.32, ease:'power3.out'}, ${s.start});`);
  else if (t === 'rise') A(`tl.fromTo('${sel}', {y:520, filter:'blur(12px)'}, {y:0, filter:'blur(0px)', duration:0.3, ease:'power3.out'}, ${s.start});`);
  else A(`tl.fromTo('${sel}', {opacity:0}, {opacity:1, duration:0.15, ease:'none'}, ${s.start});`);
  if (t === 'flash' || t === 'zoom') {
    const f = clip('<div class="leak"></div>', s.start, s.start + 0.6, 30, 'layer');
    A(`tl.fromTo('${f} .leak', {opacity:0.95, xPercent:-30}, {opacity:0, xPercent:30, duration:0.55, ease:'power2.out'}, ${s.start});`);
  }
}

function texts(s) {
  for (const t of s.texts ?? []) {
    const end = t.end ?? s.end;
    const inner = KINETIC.has(t.role) ? `<span class="txt">${words(t.text)}</span>` : `<span class="txt">${esc(t.text)}</span>`;
    const sel = clip(`<div class="t-${t.role}">${t.label ? `<span class="lbl">${esc(t.label)}</span>` : ''}${inner}</div>`,
      t.at, end, 20, `layer pos-${t.role}`, t.top ? `top:${t.top}px` : '');
    if (KINETIC.has(t.role)) {
      A(`tl.fromTo('${sel} .wi', {yPercent:110, opacity:0}, {yPercent:0, opacity:1, duration:0.5, ease:'power4.out', stagger:0.07}, ${t.at});`);
    } else if (t.role === 'stamp') {
      A(`tl.fromTo('${sel} > div', {scale:3, opacity:0, rotate:-24}, {scale:1, opacity:1, rotate:-9, duration:0.35, ease:'back.out(2.4)'}, ${t.at});`);
    } else if (t.role === 'burst') {
      A(`tl.fromTo('${sel} > div', {opacity:0, scale:0.4}, {opacity:1, scale:1, duration:0.5, ease:'back.out(2.2)'}, ${t.at});`);
    } else {
      A(`tl.fromTo('${sel} > div', {opacity:0, y:40}, {opacity:1, y:0, duration:0.5, ease:'power3.out'}, ${t.at});`);
    }
    if (t.out) A(`tl.to('${sel} > div', {opacity:0, y:-40, duration:0.3, ease:'power2.in'}, ${r2(end - 0.3)});`);
  }
}

function photo(s, track = 1) {
  const d = s.end - s.start;
  const sel = clip(`<img src="${s.media}" alt="" style="object-position:${s.fx ?? '50% 50%'}"><div class="ov ov-${s.grade}"></div>`, s.start, s.end, track, `scene grade-${s.grade}`);
  const crop = s.cropBottom;
  const zin = s.zoom !== 'out';
  const from = crop ? 1.2 : zin ? 1.06 : 1.16;
  const to = crop ? 1.13 : zin ? 1.18 : 1.04;
  // léger mouvement latéral en plus du zoom : effet « caméra » sur photo
  const drift = s.drift ?? (rnd() > 0.5 ? 40 : -40);
  A(`tl.fromTo('${sel} img', {scale:${from}, x:${-drift / 2}, transformOrigin:'${crop ? '50% 12%' : '50% 50%'}'}, {scale:${to}, x:${drift / 2}, duration:${r2(d)}, ease:'none'}, ${s.start});`);
  enter(sel, s);
  return sel;
}

function video(s, track = 1, cls = '') {
  const d = s.end - s.start;
  const vid = `c${++id}`;
  clips.push(`<video id="${vid}" class="clip media grade-${s.grade} ${cls}" src="${s.media}" data-start="${s.start}" data-duration="${r2(d)}" data-track-index="${track}" muted playsinline></video>`);
  A(`tl.fromTo('#${vid}', {scale:1.04}, {scale:1.12, duration:${r2(d)}, ease:'none'}, ${s.start});`);
  clip(`<div class="ov ov-${s.grade}"></div>`, s.start, s.end, track + 1, 'scene');
  enter(`#${vid}`, s);
  return `#${vid}`;
}

for (const s of T.scenes) {
  if (s.type === 'video') video(s);
  else if (s.media && !s.type) photo(s);
  const layered = ['grid4', 'invite', 'menucard', 'clock'].includes(s.type);
  if (!layered) texts(s);

  if (s.salle) {
    const sel = clip(`<div class="salle salle-${s.grade}"><div class="s-num">${esc(s.salle.num)}</div><div class="s-name">${words(s.salle.name)}</div><div class="s-rule"></div>${s.salle.genres ? `<div class="s-genres">${esc(s.salle.genres)}</div>` : ''}</div>`,
      s.start + 0.05, s.end, 20, 'layer pos-salle');
    A(`tl.fromTo('${sel} .s-num', {opacity:0, x:-50}, {opacity:1, x:0, duration:0.35, ease:'power3.out'}, ${r2(s.start + 0.05)});`);
    A(`tl.fromTo('${sel} .wi', {yPercent:110}, {yPercent:0, duration:0.45, ease:'power4.out', stagger:0.06}, ${r2(s.start + 0.12)});`);
    A(`tl.fromTo('${sel} .s-rule', {scaleX:0}, {scaleX:1, duration:0.45, ease:'power2.out'}, ${r2(s.start + 0.35)});`);
    if (s.salle.genres) A(`tl.fromTo('${sel} .s-genres', {opacity:0, y:24}, {opacity:1, y:0, duration:0.4, ease:'power2.out'}, ${r2(s.start + 0.5)});`);
    salleFx(s);
  }

  if (s.list) {
    s.list.forEach((it, i) => {
      const sel = clip(`<div class="pill"><span class="dot"></span>${esc(it.text)}</div>`, it.at, s.end, 20, 'layer', `top:${430 + i * 190}px`);
      A(`tl.fromTo('${sel} .pill', {opacity:0, x:-120}, {opacity:1, x:0, duration:0.45, ease:'back.out(1.4)'}, ${it.at});`);
    });
  }

  if (s.rows) {
    const html = `<div class="rows">${s.rows.map((r, i) => `<div class="row r${i}"><span class="r-l">${esc(r.label)}</span><span class="r-p">${esc(r.price)}</span></div>`).join('')}</div>`;
    const sel = clip(html, s.start, s.end, 20, 'layer pos-rows');
    s.rows.forEach((r, i) => A(`tl.fromTo('${sel} .r${i}', {opacity:0, x:-80}, {opacity:1, x:0, duration:0.4, ease:'power3.out'}, ${r.at});`));
  }

  if (s.cards) {
    s.cards.forEach((c, i) => {
      const sel = clip(`<div class="card"><div class="c-big">${esc(c.big)}</div><div class="c-small">${esc(c.small)}</div></div>`, c.at, s.end, 20, 'layer', `top:${(s.cardsTop ?? 380) + i * 290}px`);
      A(`tl.fromTo('${sel} .card', {opacity:0, rotateX:-70, transformOrigin:'50% 0%'}, {opacity:1, rotateX:0, duration:0.5, ease:'power3.out'}, ${c.at});`);
    });
  }

  if (s.type === 'countdown') {
    if (s.bg) photo({ ...s.bg, start: s.start, end: s.end, trans: s.trans }, 1);
    else clip('<div class="cd-bg"></div>', s.start, s.end, 1, 'scene');
    s.beats.forEach((b, i) => {
      const end = s.beats[i + 1] ?? s.end;
      const sel = clip(`<div class="cd-num">${esc(s.labels[i])}</div><div class="cd-ring"></div>`, b, end, 20, 'layer pos-center');
      A(`tl.fromTo('${sel} .cd-num', {scale:2.4, opacity:0}, {scale:1, opacity:1, duration:${r2(Math.min(0.3, end - b))}, ease:'power4.out'}, ${b});`);
      A(`tl.fromTo('${sel} .cd-ring', {scale:0.4, opacity:0.9}, {scale:2.2, opacity:0, duration:0.7, ease:'power2.out'}, ${b});`);
    });
    clip(`<div class="cd-kicker">${esc(s.kicker ?? 'Minuit')}</div>`, s.start, s.end, 21, 'layer pos-cdk');
  }

  if (s.type === 'clock') clock(s);
  if (s.type === 'grid4') grid4(s);
  if (s.type === 'invite') invite(s);
  if (s.type === 'menucard') menucard(s);
  if (layered) texts(s);

  if (s.celebrate) {
    const f = clip('<div class="flash"></div>', s.start, s.start + 0.8, 30, 'layer');
    A(`tl.fromTo('${f} .flash', {opacity:1}, {opacity:0, duration:0.75, ease:'power2.out'}, ${s.start});`);
    confetti(s.start, s.end, 110, 1);
    bubbles(s.start + 0.3, s.end, 24);
  }

  if (s.type === 'endcard') endcard(s);
}

function salleFx(s) {
  const d = s.end - s.start;
  if (s.grade === 'salle-gen') {
    const b = clip('<div class="beam b1"></div><div class="beam b2"></div><div class="beam b3"></div>', s.start, s.end, 10, 'layer fx-beams');
    A(`tl.fromTo('${b} .b1', {rotate:-35}, {rotate:25, duration:${d}, ease:'sine.inOut'}, ${s.start});`);
    A(`tl.fromTo('${b} .b2', {rotate:30}, {rotate:-30, duration:${d}, ease:'sine.inOut'}, ${s.start});`);
  }
  if (s.grade === 'salle-retro') {
    clip('<div class="scan"></div>', s.start, s.end, 10, 'layer');
    const g = clip('<div class="grid80"></div>', s.start, s.end, 9, 'layer');
    A(`tl.fromTo('${g} .grid80', {backgroundPositionY:'0px'}, {backgroundPositionY:'480px', duration:${d}, ease:'none'}, ${s.start});`);
  }
  if (s.grade === 'salle-latino' || s.grade === 'salle-carib') {
    const p = clip('<div class="pulse"></div>', s.start, s.end, 10, `layer pulse-${s.grade}`);
    A(`tl.fromTo('${p} .pulse', {opacity:0.15}, {opacity:0.55, duration:0.25, ease:'sine.inOut', yoyo:true, repeat:${Math.max(1, Math.floor(d / 0.25) - 1)}}, ${s.start});`);
  }
}

// Horloge 23:59 → minuit : aiguilles qui tournent, heure digitale dessous.
function clock(s) {
  clip('<div class="cd-bg"></div>', s.start, s.end, 1, 'scene');
  const ticks = Array.from({ length: 60 }, (_, i) => `<i class="tick${i % 5 === 0 ? ' big' : ''}" style="transform:rotate(${i * 6}deg)"></i>`).join('');
  const sel = clip(`<div class="clock"><div class="face">${ticks}<div class="hand h"></div><div class="hand m"></div><div class="hand sec"></div><div class="pin"></div></div><div class="digital">${esc(s.digital ?? '23:59')}</div></div>`,
    s.start, s.end, 20, 'layer');
  const d = s.end - s.start;
  A(`tl.fromTo('${sel} .face', {scale:0.6, opacity:0}, {scale:1, opacity:1, duration:0.6, ease:'back.out(1.6)'}, ${s.start});`);
  A(`tl.fromTo('${sel} .h', {rotate:359}, {rotate:359.6, duration:${d}, ease:'none'}, ${s.start});`);
  A(`tl.fromTo('${sel} .m', {rotate:354}, {rotate:359.5, duration:${d}, ease:'none'}, ${s.start});`);
  A(`tl.fromTo('${sel} .sec', {rotate:0}, {rotate:${Math.round(d * 72)}, duration:${d}, ease:'none'}, ${s.start});`);
  A(`tl.fromTo('${sel} .digital', {opacity:0, y:40}, {opacity:1, y:0, duration:0.5, ease:'power3.out'}, ${r2(s.start + 0.3)});`);
}

// Écran partagé 2×2 des 4 salles, chaque case avec son étalonnage et son nom.
function grid4(s) {
  clip('<div class="cd-bg"></div>', s.start, s.end, 1, 'scene');
  const cells = s.grid.map((g, i) => `<div class="cell cell${i} grade-${g.grade}"><img src="${g.media}" alt="" style="object-position:${g.fx ?? '50% 50%'}"><div class="ov ov-${g.grade}"></div><div class="cell-l">${esc(g.label)}</div></div>`).join('');
  const sel = clip(`<div class="grid4" style="${s.gridStyle ?? ''}">${cells}</div>`, s.start, s.end, 2, 'layer');
  s.grid.forEach((g, i) => {
    const at = r2(s.start + (g.at ?? i * 0.4));
    A(`tl.fromTo('${sel} .cell${i}', {clipPath:'inset(50% 50% 50% 50%)'}, {clipPath:'inset(0% 0% 0% 0%)', duration:0.4, ease:'power3.out'}, ${at});`);
    A(`tl.fromTo('${sel} .cell${i} img', {scale:1.3}, {scale:1.05, duration:${r2(s.end - at)}, ease:'power1.out'}, ${at});`);
    A(`tl.fromTo('${sel} .cell${i} .cell-l', {opacity:0, y:30}, {opacity:1, y:0, duration:0.35, ease:'power3.out'}, ${r2(at + 0.15)});`);
  });
}

// Carton d'invitation doré qui se retourne (effet 3D) + reflet qui balaie la carte.
function invite(s) {
  if (s.bg?.type === 'video') video({ ...s.bg, start: s.start, end: s.end, trans: s.trans });
  else if (s.bg) photo({ ...s.bg, start: s.start, end: s.end, trans: s.trans });
  const i = s.invite;
  const sel = clip(`<div class="invite-wrap"><div class="invite"><div class="inv-k">${esc(i.kicker)}</div><img class="inv-logo" src="assets/brand/villa-beach-monogram.png" alt=""><div class="inv-t">${esc(i.title)}</div><div class="inv-rule"></div><div class="inv-d">${esc(i.date)}</div><div class="inv-v">${esc(i.venue)}</div><div class="shine"></div></div></div>`,
    s.start, s.end, 20, 'layer');
  const at = r2(s.start + (i.at ?? 0.2));
  A(`tl.fromTo('${sel} .invite', {rotateY:-100, rotateZ:-8, opacity:0, scale:0.8}, {rotateY:0, rotateZ:-3, opacity:1, scale:1, duration:0.9, ease:'power3.out'}, ${at});`);
  A(`tl.fromTo('${sel} .shine', {xPercent:-160}, {xPercent:160, duration:1.1, ease:'power2.inOut'}, ${r2(at + 0.8)});`);
  A(`tl.to('${sel} .invite', {rotateZ:2, y:-14, duration:${r2(Math.max(0.3, s.end - at - 0.9))}, ease:'sine.inOut'}, ${r2(at + 0.9)});`);
}

// Carte du menu du réveillon, avec tampon « exclusif ».
function menucard(s) {
  if (s.bg) photo({ ...s.bg, start: s.start, end: s.end, trans: s.trans });
  const m = s.menu;
  const items = m.courses.map((c, i) => `<div class="mc-i mc${i}"><div class="mc-k">${esc(c.k)}</div><div class="mc-v">${esc(c.v)}</div></div>`).join('');
  const sel = clip(`<div class="menucard"><div class="mc-h">${esc(m.kicker)}</div><div class="mc-t">${esc(m.title)}</div><div class="mc-rule"></div>${items}${m.stamp ? `<div class="mc-stamp">${esc(m.stamp)}</div>` : ''}</div>`,
    s.start, s.end, 20, 'layer pos-menucard');
  A(`tl.fromTo('${sel} .menucard', {opacity:0, y:120, rotate:4}, {opacity:1, y:0, rotate:0, duration:0.6, ease:'power3.out'}, ${r2(s.start + 0.1)});`);
  m.courses.forEach((c, i) => A(`tl.fromTo('${sel} .mc${i}', {opacity:0, x:-40}, {opacity:1, x:0, duration:0.4, ease:'power3.out'}, ${r2(s.start + (c.at ?? 0.5 + i * 0.45))});`));
  if (m.stamp) A(`tl.fromTo('${sel} .mc-stamp', {scale:3.2, opacity:0, rotate:-30}, {scale:1, opacity:1, rotate:-12, duration:0.35, ease:'back.out(2.6)'}, ${r2(s.start + (m.stampAt ?? 2.4))});`);
}

function endcard(s) {
  if (s.bgVideo) video({ media: s.bgVideo, grade: 'endvideo', start: s.start, end: s.end, trans: s.trans ?? 'flash' });
  else clip('<div class="end-bg"></div>', s.start, s.end, 1, 'scene');
  glitter(s.start, s.end, 40);
  const html = `
    <img class="e-logo" src="assets/brand/villa-beach-monogram.png" alt="Villa Beach">
    ${s.date ? `<div class="e-date">${esc(s.date)}</div>` : ''}
    <div class="e-title">${esc(s.title)}</div>
    ${s.note ? `<div class="e-note">${esc(s.note)}</div>` : ''}
    <div class="e-sub">${esc(s.sub)}</div>
    <div class="e-rule"></div>
    <div class="e-venue">${esc(s.venue)}</div>
    <div class="e-addr">${esc(s.address)}</div>
    <div class="e-phone"><span class="e-tel">Réservations</span>${esc(s.phone)}</div>
    ${s.url ? `<div class="e-url">${esc(s.url)}</div>` : ''}`;
  const sel = clip(html, s.start, s.end, 20, 'layer endcard');
  const parts = ['.e-logo', ...(s.date ? ['.e-date'] : []), '.e-title', ...(s.note ? ['.e-note'] : []), '.e-sub', '.e-rule', '.e-venue', '.e-addr', '.e-phone'];
  parts.forEach((p, i) => A(`tl.fromTo('${sel} ${p}', {opacity:0, y:30}, {opacity:1, y:0, duration:0.45, ease:'power3.out'}, ${r2(s.start + 0.05 + i * 0.07)});`));
  A(`tl.fromTo('${sel} .e-phone', {boxShadow:'0 0 0px rgba(232,211,154,0)'}, {boxShadow:'0 0 60px rgba(232,211,154,.6)', duration:0.8, ease:'sine.inOut', yoyo:true, repeat:5}, ${r2(s.start + 1.2)});`);
}

function confetti(start, end, n, density) {
  const colors = ['#E8D39A', '#C9A45C', '#F2EAD6', '#9C7B3B', '#E07A2F', '#ffffff'];
  let html = '';
  const items = [];
  for (let i = 0; i < n; i++) {
    const w = 10 + Math.round(rnd() * 14);
    html += `<i class="cf cf${i}" style="left:${Math.round(rnd() * 1080)}px;width:${w}px;height:${Math.round(w * (0.4 + rnd() * 0.5))}px;background:${colors[Math.floor(rnd() * colors.length)]}"></i>`;
    items.push({ i, delay: r2(rnd() * (end - start) * 0.5 * density), fall: r2(1.6 + rnd() * 2.2), rot: Math.round(rnd() * 720 - 360), drift: Math.round(rnd() * 160 - 80) });
  }
  const sel = clip(html, start, end, 25, 'layer confetti');
  for (const it of items) A(`tl.fromTo('${sel} .cf${it.i}', {y:-60, x:0, rotate:0}, {y:2000, x:${it.drift}, rotate:${it.rot}, duration:${it.fall}, ease:'none'}, ${r2(start + it.delay)});`);
}

function bubbles(start, end, n) {
  let html = '';
  const items = [];
  for (let i = 0; i < n; i++) {
    const sz = 10 + Math.round(rnd() * 26);
    html += `<i class="bb bb${i}" style="left:${Math.round(60 + rnd() * 960)}px;width:${sz}px;height:${sz}px"></i>`;
    items.push({ i, delay: r2(rnd() * Math.max(0.2, end - start - 1.5)), dur: r2(1.8 + rnd() * 1.6) });
  }
  const sel = clip(html, start, end, 24, 'layer bubbles');
  for (const it of items) A(`tl.fromTo('${sel} .bb${it.i}', {y:1980, opacity:0.9}, {y:900, opacity:0, duration:${it.dur}, ease:'power1.out'}, ${r2(start + it.delay)});`);
}

function glitter(start, end, n) {
  let html = '';
  const items = [];
  for (let i = 0; i < n; i++) {
    const sz = 3 + Math.round(rnd() * 6);
    html += `<i class="gl gl${i}" style="left:${Math.round(rnd() * 1080)}px;top:-20px;width:${sz}px;height:${sz}px"></i>`;
    items.push({ i, delay: r2(rnd() * (end - start)), dur: r2(4 + rnd() * 4) });
  }
  const sel = clip(html, start, end, 22, 'layer');
  for (const it of items) A(`tl.fromTo('${sel} .gl${it.i}', {y:-20, opacity:0}, {y:1960, opacity:1, duration:${it.dur}, ease:'none'}, ${r2(Math.max(0, start + it.delay - 4))});`);
}

// ---------- sous-titres ----------
for (const sub of T.subtitles ?? []) {
  const sel = clip(`<div class="sub">${esc(sub.text)}</div>`, sub.start, sub.end, 40, 'layer pos-sub');
  A(`tl.fromTo('${sel} .sub', {opacity:0, y:14}, {opacity:1, y:0, duration:0.16, ease:'power2.out'}, ${sub.start});`);
}

// ---------- couches permanentes ----------
const END = (T.scenes.find((x) => x.type === 'endcard') ?? { start: DUR }).start;
// Date du réveillon toujours visible en haut (hors carton final, qui l'affiche en grand).
if (T.dateBadge && END > 0) {
  const sel = clip(`<div class="datebadge"><span class="db-dot"></span>${esc(T.dateBadge)}</div>`, 0, END, 36, 'layer');
  A(`tl.fromTo('${sel} .datebadge', {opacity:0, y:-30}, {opacity:1, y:0, duration:0.5, ease:'power3.out'}, 0.05);`);
}
if (T.footer && END > 0) {
  const [fd, ft] = String(T.footer).split('|');
  clip(`<div class="footer"><img src="assets/brand/villa-beach-monogram.png" alt=""><span><span class="f-date">${esc(fd)}</span>${ft ? `<span class="f-tel">${esc(ft)}</span>` : ''}</span></div>`, 0, END, 35, 'layer');
} else if (!T.footer && END > 0) {
  clip('<img class="corner-logo" src="assets/brand/villa-beach-monogram.png" alt="">', 0, END, 35, 'layer');
}
// Grain pellicule léger, déplacé 12 fois par seconde.
const g = clip('<div class="grain"></div>', 0, DUR, 45, 'layer');
for (let t = 0; t < DUR; t += 1 / 12) A(`tl.set('${g} .grain', {backgroundPosition:'${Math.round(rnd() * 400)}px ${Math.round(rnd() * 400)}px'}, ${r2(t)});`);
if (DRAFT) clip(`<div class="draft">${esc(T.draftLabel ?? 'VERSION DE TRAVAIL')}</div>`, 0, DUR, 50, 'layer');

const html = `<!doctype html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=1080, height=1920">
<!-- GÉNÉRÉ par scripts/build.mjs depuis ${SRC} — ne pas éditer à la main -->
<script src="assets/vendor/gsap.min.js"></script>
<link rel="stylesheet" href="assets/style.css">
</head>
<body>
<div id="root" data-composition-id="main" data-start="0" data-duration="${DUR}" data-width="1080" data-height="1920">
${clips.join('\n')}
</div>
<script>
window.__timelines = window.__timelines || {};
const tl = gsap.timeline({ paused: true });
${anim.join('\n')}
tl.set({}, {}, ${DUR});
window.__timelines['main'] = tl;
</script>
</body>
</html>
`;
writeFileSync(path.join(ROOT, 'index.html'), html);
console.log(`${SRC} -> index.html : ${clips.length} clips, ${anim.length} animations, ${DUR}s${DRAFT ? ', brouillon' : ''}`);
