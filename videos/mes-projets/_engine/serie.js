// Série « Mes projets » : un épisode = un projet. Moteur commun au-dessus de journal.js.
// P.make(o) : o = {ep, nom, url, theme:{...vars}, kw, red, labels:[...par ligne], clips:[[ligne, départ dans la vidéo source]], src, cta:{titre, sous}, visuel}
// Les vidéos du projet sont incrustées ensuite par post.py dans la zone ECRAN (window.CLIPS).
const P = {};
P.ECRAN = {x: 40, y: 470, w: 1000, h: 563};
P.make = function (o) {
  const C = window.CFG;
  const {t0, w} = J;
  J.init({episode: o.ep, keyword: 'PROJET', duoLogo: 'foodeatup', theme: {vars: o.theme}, kw: o.kw || [], red: o.red || []});
  document.getElementById('epi').textContent = `MES PROJETS · ÉPISODE ${o.ep}`;
  const E = P.ECRAN, last = C.lines.length - 1;
  document.head.insertAdjacentHTML('beforeend', `<style>
  .serie{display:inline-flex;align-items:center;gap:14px;background:rgba(255,255,255,.08);border:2px solid rgba(255,255,255,.18);border-radius:999px;padding:10px 22px 10px 12px;font-weight:800;font-size:26px;letter-spacing:3px}
  .serie i{font-style:normal;background:var(--accent);color:#fff;border-radius:999px;padding:4px 14px;letter-spacing:1px}
  .ecran{position:absolute;border-radius:28px;background:#0b141c;border:4px solid rgba(255,255,255,.14);box-shadow:0 40px 90px rgba(0,0,0,.55)}
  .lab{display:inline-block;background:var(--accent);color:#fff;font-weight:900;font-size:56px;padding:14px 34px;border-radius:22px;letter-spacing:-.5px;box-shadow:0 20px 40px rgba(0,0,0,.35)}
  .lab.b{background:#fff;color:var(--bg)}
  .voir{display:inline-flex;align-items:center;gap:20px;background:var(--accent);color:#fff;font-weight:900;font-size:64px;padding:26px 50px;border-radius:30px;box-shadow:0 30px 70px rgba(0,0,0,.45)}
  .url{display:inline-block;background:#fff;color:var(--bg);font-weight:800;font-size:40px;padding:14px 32px;border-radius:999px}
  .fl{font-size:120px;line-height:1;color:var(--accent2)}
  .hook .hookt{font-size:74px!important;line-height:1.08}
  </style>`);
  // fond commun : bandeau série + logo FoodEatUp
  J.fx.push(() => {});
  const head = (s, a) => {
    s.add(`<div class="serie"><i>MES PROJETS</i>ÉPISODE ${o.ep}</div>`, {x: 540, w: 0, y: 60, at: a, an: 'none', css: {transform: 'translateX(-50%)', whiteSpace: 'nowrap'}});
    s.add(`<div style="background:#fff;border-radius:18px;padding:12px 22px;display:inline-flex"><img src="../mes-projets/_engine/logo-foodeatup.webp" style="height:46px"></div>`, {x: 540, w: 0, y: 150, at: a, an: 'none', css: {transform: 'translateX(-50%)'}});
  };
  const ecran = (s, a) => s.add(`<div class="ecran" style="width:${E.w + 8}px;height:${E.h + 8}px"></div>`, {x: E.x - 4 + (E.w + 8) / 2, w: E.w + 8, y: E.y - 4, at: a, an: 'none'});
  const clips = [];
  o.clips.forEach(([li, ss]) => clips.push([o.src, Math.max(0, t0(li) - (li === 0 ? .35 : .15)), li + 1 <= last ? t0(li + 1) - .15 : t0(last), ss, 1]));
  window.CLIPS = clips;
  // ligne 0 : le hook
  let s = J.hook(0, t0(1), {line: 0, hl: o.hookHl || [], y: 215, w: 1000});
  ecran(s, 0);
  // lignes intermédiaires : écran + étiquette
  for (let i = 1; i < last; i++) {
    s = J.scene(t0(i), t0(i + 1));
    head(s, t0(i)); ecran(s, t0(i));
    const lab = o.labels[i];
    if (lab) s.add(`<div class="lab${i === 1 ? ' b' : ''}">${lab}</div>`, {x: 540, w: 0, y: 1100, at: t0(i) + .25, an: i === 1 ? 'pop' : 'stamp', css: {transform: 'translateX(-50%)', whiteSpace: 'nowrap'}});
  }
  // dernière ligne : le CTA « Voir le projet »
  s = J.scene(t0(last), C.dur + 1, {noDuo: false});
  head(s, t0(last));
  s.add(`<div style="width:820px;border-radius:30px;overflow:hidden;border:4px solid rgba(255,255,255,.18);box-shadow:0 40px 90px rgba(0,0,0,.5)"><img src="${o.visuel}" style="width:100%;display:block"></div>`, {x: 540, w: 820, y: 290, at: t0(last), an: 'up'});
  s.text(`<span style="font-size:58px">${o.nom}</span>`, {y: 790, at: t0(last) + .2});
  s.add(`<div class="voir">Voir le projet <span>↓</span></div>`, {x: 540, w: 0, y: 900, at: w(last, 'lien'), an: 'slam', css: {transform: 'translateX(-50%)', whiteSpace: 'nowrap'}});
  s.add(`<div class="url">${o.url}</div>`, {x: 540, w: 0, y: 1090, at: w(last, 'vidéo'), an: 'pop', css: {transform: 'translateX(-50%)', whiteSpace: 'nowrap'}});
  s.text(`<span style="font-size:34px;color:var(--mute)">le lien est sous la vidéo</span>`, {y: 1190, at: w(last, 'clique')});
  J.cfg.thumbAt = o.thumbAt ?? t0(1) + 1;
};
