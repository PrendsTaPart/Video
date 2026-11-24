#!/usr/bin/env node
// Construit index.html (composition HyperFrames 1080x1920) depuis data/timeline.json.
// Tout le texte, le minutage et les médias viennent du JSON : modifier le JSON puis
// relancer `npm run build`. Le balisage est statique (une div .clip par élément),
// seules les animations sont pilotées par la timeline GSAP « main ».
//
//   node scripts/build.mjs            -> version de travail (bandeau « VERSION DE TRAVAIL »)
//   node scripts/build.mjs --final    -> version diffusion (sans bandeau)
import { readFileSync, writeFileSync } from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const ROOT = path.dirname(path.dirname(fileURLToPath(import.meta.url)));
const SRC = process.argv.slice(2).find((a) => !a.startsWith('--')) || 'data/timeline.json';
const T = JSON.parse(readFileSync(path.join(ROOT, SRC), 'utf8'));
const FINAL = process.argv.includes('--final');
const DUR = T.format.duration;

const esc = (s) => String(s ?? '').replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
const r2 = (n) => Math.round(n * 1000) / 1000;
// Aléatoire déterministe (confettis, bulles, paillettes) : même rendu à chaque build.
let seed = 2027;
const rnd = () => ((seed = (seed * 16807) % 2147483647) / 2147483647);

const clips = [];
const anim = [];
let id = 0;
const clip = (html, start, end, track, cls = '', style = '') => {
  const cid = `c${++id}`;
  clips.push(
    `<div id="${cid}" class="clip ${cls}" data-start="${r2(start)}" data-duration="${r2(end - start)}" data-track-index="${track}" style="${style}">${html}</div>`,
  );
  return `#${cid}`;
};

// ---------- scènes ----------
for (const s of T.scenes) {
  const d = s.end - s.start;
  if (s.type === 'video') {
    const vid = `c${++id}`;
    clips.push(
      `<video id="${vid}" class="clip media grade-${s.grade}" src="${s.media}" data-start="${s.start}" data-duration="${r2(d)}" data-track-index="1" muted playsinline></video>`,
    );
    anim.push(`tl.fromTo('#${vid}', {scale:1.04}, {scale:1.12, duration:${r2(d)}, ease:'none'}, ${s.start});`);
    clip(`<div class="ov ov-${s.grade}"></div>`, s.start, s.end, 2, 'scene');
  } else if (s.media) {
    const sel = clip(
      `<img src="${s.media}" alt="" style="object-position:${s.fx}"><div class="ov ov-${s.grade}"></div>`,
      s.start, s.end, 1, `scene grade-${s.grade}`,
    );
    const zoomIn = s.zoom ? s.zoom === 'in' : (s.id.includes('salle') || /gen|latino|80|carib/.test(s.id));
    const crop = s.id === 's07-latino' || s.cropBottom;
    const from = crop ? 1.2 : zoomIn ? 1.06 : 1.14;
    const to = crop ? 1.13 : zoomIn ? 1.16 : 1.04;
    const origin = crop ? '50% 12%' : '50% 50%';
    anim.push(`tl.fromTo('${sel} img', {scale:${from}, transformOrigin:'${origin}'}, {scale:${to}, duration:${r2(d)}, ease:'none'}, ${s.start});`);
    // coupe : flash doré court à l'entrée de chaque plan (sauf le premier)
    if (s.start > 0) anim.push(`tl.fromTo('${sel}', {opacity:0}, {opacity:1, duration:0.18, ease:'power1.out'}, ${s.start});`);
  }

  for (const t of s.texts ?? []) {
    const sel = clip(`<div class="t-${t.role}"${t.color ? ` style="color:${t.color}"` : ''}>${t.label ? `<span class="lbl">${esc(t.label)}</span>` : ''}<span class="txt">${esc(t.text)}</span></div>`,
      t.at, t.end ?? s.end, 20, `layer pos-${t.role}`);
    const ease = t.role === 'burst' ? 'back.out(2.2)' : 'power3.out';
    anim.push(`tl.fromTo('${sel} > div', {opacity:0, y:${t.role === 'burst' ? 0 : 40}, scale:${t.role === 'burst' ? 0.4 : 1}}, {opacity:1, y:0, scale:1, duration:${t.role === 'burst' ? 0.5 : 0.55}, ease:'${ease}'}, ${t.at});`);
    if (t.role === 'burst') anim.push(`tl.to('${sel} > div', {opacity:0, y:-60, duration:0.4, ease:'power2.in'}, ${r2(t.at + 1.5)});`);
  }

  if (s.salle) {
    const sel = clip(
      `<div class="salle salle-${s.grade}"><div class="s-num">${esc(s.salle.num)}</div><div class="s-name">${esc(s.salle.name)}</div><div class="s-rule"></div><div class="s-genres">${esc(s.salle.genres)}</div></div>`,
      s.start + 0.1, s.end, 20, 'layer pos-salle',
    );
    anim.push(`tl.fromTo('${sel} .s-num', {opacity:0, x:-50}, {opacity:1, x:0, duration:0.4, ease:'power3.out'}, ${r2(s.start + 0.1)});`);
    anim.push(`tl.fromTo('${sel} .s-name', {opacity:0, y:60, scale:0.92}, {opacity:1, y:0, scale:1, duration:0.55, ease:'back.out(1.6)'}, ${r2(s.start + 0.2)});`);
    anim.push(`tl.fromTo('${sel} .s-rule', {scaleX:0}, {scaleX:1, duration:0.5, ease:'power2.out'}, ${r2(s.start + 0.45)});`);
    anim.push(`tl.fromTo('${sel} .s-genres', {opacity:0, y:24}, {opacity:1, y:0, duration:0.45, ease:'power2.out'}, ${r2(s.start + 0.6)});`);
    anim.push(`tl.to('${sel}', {opacity:0, duration:0.2}, ${r2(s.end - 0.2)});`);
    // traitement lumineux propre à chaque salle
    if (s.grade === 'salle-gen') {
      const b = clip('<div class="beam b1"></div><div class="beam b2"></div><div class="beam b3"></div>', s.start, s.end, 10, 'layer fx-beams');
      anim.push(`tl.fromTo('${b} .b1', {rotate:-35}, {rotate:25, duration:${d}, ease:'sine.inOut'}, ${s.start});`);
      anim.push(`tl.fromTo('${b} .b2', {rotate:30}, {rotate:-30, duration:${d}, ease:'sine.inOut'}, ${s.start});`);
      anim.push(`tl.fromTo('${b} .b3', {rotate:-5, opacity:.2}, {rotate:10, opacity:.7, duration:${d / 4}, ease:'sine.inOut', yoyo:true, repeat:3}, ${s.start});`);
    }
    if (s.grade === 'salle-retro') clip('<div class="scan"></div>', s.start, s.end, 10, 'layer');
    if (s.grade === 'salle-retro') {
      const g = clip('<div class="grid80"></div>', s.start, s.end, 9, 'layer');
      anim.push(`tl.fromTo('${g} .grid80', {backgroundPositionY:'0px'}, {backgroundPositionY:'480px', duration:${d}, ease:'none'}, ${s.start});`);
    }
    if (s.grade === 'salle-latino' || s.grade === 'salle-carib') {
      const p = clip('<div class="pulse"></div>', s.start, s.end, 10, `layer pulse-${s.grade}`);
      anim.push(`tl.fromTo('${p} .pulse', {opacity:0.15}, {opacity:0.55, duration:0.25, ease:'sine.inOut', yoyo:true, repeat:${Math.floor(d / 0.25) - 1}}, ${s.start});`);
    }
  }

  if (s.list) {
    s.list.forEach((it, i) => {
      const sel = clip(`<div class="pill"><span class="dot"></span>${esc(it.text)}</div>`, it.at, s.end, 20, 'layer', `top:${420 + i * 190}px`);
      anim.push(`tl.fromTo('${sel} .pill', {opacity:0, x:-120}, {opacity:1, x:0, duration:0.5, ease:'back.out(1.4)'}, ${it.at});`);
    });
    // cotillons qui tombent déjà en fin de séquence (annonce de minuit)
    if (s.confettiEnd !== false) confetti(s.end - 1.6, s.end, 40, 0.6);
  }

  if (s.type === 'countdown') {
    clip('<div class="cd-bg"></div>', s.start, s.end, 1, 'scene');
    s.beats.forEach((b, i) => {
      const end = s.beats[i + 1] ?? s.end;
      const sel = clip(`<div class="cd-num">${esc(s.labels[i])}</div><div class="cd-ring"></div>`, b, end, 20, 'layer pos-center');
      anim.push(`tl.fromTo('${sel} .cd-num', {scale:2.4, opacity:0}, {scale:1, opacity:1, duration:0.32, ease:'power4.out'}, ${b});`);
      anim.push(`tl.fromTo('${sel} .cd-ring', {scale:0.4, opacity:0.9}, {scale:2.2, opacity:0, duration:0.75, ease:'power2.out'}, ${b});`);
    });
    clip(`<div class="cd-kicker">${esc(s.kicker ?? 'Minuit')}</div>`, s.start, s.end, 21, 'layer pos-cdk');
  }

  if (s.id === 's12-minuit' || s.celebrate) {
    const f = clip('<div class="flash"></div>', s.start, s.start + 0.8, 30, 'layer');
    anim.push(`tl.fromTo('${f} .flash', {opacity:1}, {opacity:0, duration:0.75, ease:'power2.out'}, ${s.start});`);
    confetti(s.start, s.end, 120, 1);
    bubbles(s.start + 0.3, s.end, 28);
  }

  if (s.rows) {
    const html = `<div class="rows">${s.rows.map((r, i) => `<div class="row r${i}"><span class="r-l">${esc(r.label)}</span><span class="r-p">${esc(r.price)}</span></div>`).join('')}</div>`;
    const sel = clip(html, s.start, s.end, 20, 'layer pos-rows');
    s.rows.forEach((r, i) => anim.push(`tl.fromTo('${sel} .r${i}', {opacity:0, x:-80}, {opacity:1, x:0, duration:0.45, ease:'power3.out'}, ${r.at});`));
  }

  if (s.cards) {
    s.cards.forEach((c, i) => {
      const sel = clip(`<div class="card"><div class="c-big">${esc(c.big)}</div><div class="c-small">${esc(c.small)}</div></div>`, c.at, s.end, 20, 'layer', `top:${330 + i * 300}px`);
      anim.push(`tl.fromTo('${sel} .card', {opacity:0, y:50, scale:0.96}, {opacity:1, y:0, scale:1, duration:0.55, ease:'power3.out'}, ${c.at});`);
    });
  }

  if (s.type === 'endcard') {
    clip('<div class="end-bg"></div>', s.start, s.end, 1, 'scene');
    glitter(s.start, s.end, 46);
    const html = `
      <img class="e-logo" src="assets/brand/villa-beach-monogram.png" alt="Villa Beach">
      ${s.date ? `<div class="e-date">${esc(s.date)}</div>` : ''}
      <div class="e-title">${esc(s.title)}</div>
      <div class="e-sub">${esc(s.sub)}</div>
      <div class="e-rule"></div>
      <div class="e-venue">${esc(s.venue)}</div>
      <div class="e-addr">${esc(s.address)}</div>
      <div class="e-phone"><span class="e-tel">Réservations</span>${esc(s.phone)}</div>
      ${s.url ? `<div class="e-url">${esc(s.url)}</div>` : ''}`;
    const sel = clip(html, s.start, s.end, 20, 'layer endcard');
    const parts = ['.e-logo', ...(s.date ? ['.e-date'] : []), '.e-title', '.e-sub', '.e-rule', '.e-venue', '.e-addr', '.e-phone'];
    parts.forEach((p, i) => anim.push(`tl.fromTo('${sel} ${p}', {opacity:0, y:30}, {opacity:1, y:0, duration:0.5, ease:'power3.out'}, ${r2(s.start + 0.05 + i * 0.08)});`));
    anim.push(`tl.fromTo('${sel} .e-phone', {boxShadow:'0 0 0px rgba(232,211,154,0)'}, {boxShadow:'0 0 60px rgba(232,211,154,.55)', duration:0.8, ease:'sine.inOut', yoyo:true, repeat:5}, ${r2(s.start + 1.4)});`);
  }
}

function confetti(start, end, n, density) {
  const colors = ['#E8D39A', '#C9A45C', '#F2EAD6', '#9C7B3B', '#E07A2F', '#ffffff'];
  let html = '';
  const items = [];
  for (let i = 0; i < n; i++) {
    const x = Math.round(rnd() * 1080);
    const w = 10 + Math.round(rnd() * 14);
    const h = Math.round(w * (0.4 + rnd() * 0.5));
    const c = colors[Math.floor(rnd() * colors.length)];
    const delay = r2(rnd() * (end - start) * 0.5 * density);
    const fall = r2(1.6 + rnd() * 2.2);
    html += `<i class="cf cf${i}" style="left:${x}px;width:${w}px;height:${h}px;background:${c}"></i>`;
    items.push({ i, delay, fall, rot: Math.round(rnd() * 720 - 360), drift: Math.round(rnd() * 160 - 80) });
  }
  const sel = clip(html, start, end, 25, 'layer confetti');
  for (const it of items) {
    anim.push(`tl.fromTo('${sel} .cf${it.i}', {y:-60, x:0, rotate:0}, {y:2000, x:${it.drift}, rotate:${it.rot}, duration:${it.fall}, ease:'none'}, ${r2(start + it.delay)});`);
  }
}

function bubbles(start, end, n) {
  let html = '';
  const items = [];
  for (let i = 0; i < n; i++) {
    const x = Math.round(60 + rnd() * 960);
    const sz = 10 + Math.round(rnd() * 26);
    html += `<i class="bb bb${i}" style="left:${x}px;width:${sz}px;height:${sz}px"></i>`;
    items.push({ i, delay: r2(rnd() * (end - start - 1.5)), dur: r2(1.8 + rnd() * 1.6) });
  }
  const sel = clip(html, start, end, 24, 'layer bubbles');
  for (const it of items) anim.push(`tl.fromTo('${sel} .bb${it.i}', {y:1980, opacity:0.9}, {y:900, opacity:0, duration:${it.dur}, ease:'power1.out'}, ${r2(start + it.delay)});`);
}

function glitter(start, end, n) {
  let html = '';
  const items = [];
  for (let i = 0; i < n; i++) {
    const x = Math.round(rnd() * 1080);
    const sz = 3 + Math.round(rnd() * 6);
    html += `<i class="gl gl${i}" style="left:${x}px;top:-20px;width:${sz}px;height:${sz}px"></i>`;
    items.push({ i, delay: r2(rnd() * (end - start)), dur: r2(4 + rnd() * 4) });
  }
  const sel = clip(html, start, end, 5, 'layer');
  for (const it of items) anim.push(`tl.fromTo('${sel} .gl${it.i}', {y:-20, opacity:0}, {y:1960, opacity:1, duration:${it.dur}, ease:'none'}, ${r2(start + it.delay - 4)});`);
}

// ---------- sous-titres ----------
for (const sub of T.subtitles ?? []) {
  const sel = clip(`<div class="sub">${esc(sub.text)}</div>`, sub.start, sub.end, 40, 'layer pos-sub');
  anim.push(`tl.fromTo('${sel} .sub', {opacity:0, y:14}, {opacity:1, y:0, duration:0.16, ease:'power2.out'}, ${sub.start});`);
}

// petit monogramme en coin pendant les plans « réels » (pas sur le carton final qui l'affiche en grand)
const END = (T.scenes.find((x) => x.type === 'endcard') ?? { start: DUR }).start;
if (T.footer && END > 0) {
  // pied de page constant des stories : logo + date + téléphone, au-dessus de la barre de réponse Instagram
  clip(`<div class="footer"><img src="assets/brand/villa-beach-monogram.png" alt=""><span>${esc(T.footer)}</span></div>`, 0, END, 35, 'layer');
} else if (!T.footer) {
  clip('<img class="corner-logo" src="assets/brand/villa-beach-monogram.png" alt="">', 0, END, 35, 'layer');
}
if (!FINAL) clip(`<div class="draft">${esc(T.draftLabel ?? 'VERSION DE TRAVAIL · voix off et musique à finaliser')}</div>`, 0, DUR, 50, 'layer');

const html = `<!doctype html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=1080, height=1920">
<!-- GÉNÉRÉ par scripts/build.mjs depuis data/timeline.json — ne pas éditer à la main -->
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
console.log(`${SRC} -> index.html : ${clips.length} clips, ${anim.length} animations, ${DUR}s, ${FINAL ? 'FINAL' : 'version de travail'}`);
