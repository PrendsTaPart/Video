// Épisodes 74 à 83 : une scène par phrase de la voix, au-dessus de journal.js.
// I.make(o) : o = {ep, keyword, duo, theme:{cls, vars}, kw, red, hookHl, steps, scenes:[par ligne 1..n-2], cta:{guideTitle, items}, thumbAt}
// Types de scène : big (icône + mot), step (étape numérotée), img (capture réelle), chips (liste), duo (avant / après),
// gauge (jauge vert → rouge), projet (carte du projet avec sa capture).
const I = {};
I.make = function (o) {
  const C = window.CFG;
  const {t0, w} = J;
  J.init({episode: o.ep, keyword: o.keyword, duoLogo: o.duo || 'claude', stepLabel: o.stepLabel || 'ÉTAPE', theme: o.theme, kw: o.kw || [], red: o.red || []});
  document.head.insertAdjacentHTML('beforeend', `<style>
  .ibig{font-size:180px;line-height:1}.iword{display:inline-block;background:var(--accent);color:var(--hlfg,#111);font-weight:900;font-size:72px;padding:10px 30px;border-radius:22px;white-space:nowrap}
  .icard{background:var(--surf);border:3px solid var(--line);border-radius:30px;overflow:hidden;box-shadow:0 30px 70px rgba(0,0,0,.35)}.icard img{width:100%;display:block}
  .icap{font-size:30px;color:var(--mute);font-weight:600}.ichip{display:flex;align-items:center;gap:18px;background:var(--surf);border:2px solid var(--line);border-radius:22px;padding:18px 26px;font-size:40px;font-weight:700;color:var(--text)}
  .ichip b{display:inline-flex;width:58px;height:58px;border-radius:16px;background:var(--accent);color:var(--hlfg,#111);align-items:center;justify-content:center;font-size:34px}
  .iduo{width:440px;border-radius:26px;padding:26px;text-align:center;font-size:40px;font-weight:800}.iko{background:rgba(229,57,53,.16);border:3px solid #E53935;color:#E53935}.iok{background:rgba(63,182,107,.16);border:3px solid #3FB66B;color:#3FB66B}
  .iduo small{display:block;font-size:28px;font-weight:600;color:var(--text);margin-top:10px}.igauge{width:820px;height:64px;border-radius:32px;background:var(--line);overflow:hidden}.igauge i{display:block;height:100%;width:0}
  .itag{display:inline-block;font-size:24px;font-weight:700;letter-spacing:2px;color:var(--mute);border:2px solid var(--line);border-radius:999px;padding:6px 18px}
  </style>`);
  if (o.steps) J.progress(o.steps);
  const last = C.lines.length - 1;
  let s = J.hook(0, t0(1), {line: 0, hl: o.hookHl || [], y: o.hookY || 360, sticker: o.sticker});
  if (o.hookImg) s.add(`<div class="icard" style="width:760px"><img src="${o.hookImg}"></div>`, {x: 540, w: 760, y: 900, at: .6, an: 'up'});
  if (o.tag) s.add(`<div class="itag">${o.tag}</div>`, {x: 540, w: 0, y: 1160, at: .8, an: 'fade', css: {transform: 'translateX(-50%)'}});
  (o.scenes || []).forEach((c, k) => {
    const i = k + 1, a = t0(i), b = i + 1 <= last ? t0(i + 1) : t0(last);
    const sc = J.scene(a, b);
    if (c.step) J.step(sc, c.step, c.title || '', c.hl || '');
    const at = c.w ? w(i, c.w) : a + .2, y0 = c.step ? 300 : 230;
    if (c.t === 'big') {
      if (c.icon) sc.text(`<span class="ibig">${c.icon}</span>`, {y: y0 + 40, at: a, an: 'pop'});
      sc.add(`<div class="iword">${c.txt}</div>`, {x: 540, w: 0, y: y0 + 300, at, an: 'slam', css: {transform: 'translateX(-50%)'}});
      if (c.sub) sc.text(`<span class="icap">${c.sub}</span>`, {y: y0 + 440, at: at + .3});
    } else if (c.t === 'img') {
      sc.add(`<div class="icard" style="width:${c.wd || 860}px"><img src="${c.src}"></div>`, {x: 540, w: c.wd || 860, y: y0 + 20, at: a, an: 'up'});
      if (c.txt) sc.add(`<div class="iword">${c.txt}</div>`, {x: 540, w: 0, y: c.ty || 860, at, an: 'stamp', css: {transform: 'translateX(-50%)'}});
      if (c.cap) sc.text(`<span class="icap">${c.cap}</span>`, {y: (c.ty || 860) + 130, at: at + .2});
    } else if (c.t === 'chips') {
      c.items.forEach((x, j) => sc.add(`<div class="ichip"><b>${c.icons ? c.icons[j] : j + 1}</b>${x}</div>`, {x: 540, w: 820, y: y0 + 40 + j * 150, at: (c.ws ? w(i, c.ws[j]) : a + .2 + j * .35), an: 'left'}));
    } else if (c.t === 'duo') {
      sc.add(`<div class="iduo iko">✗ ${c.ko}<small>${c.kos || ''}</small></div>`, {x: 290, w: 440, y: y0 + 120, at: c.wko ? w(i, c.wko) : a + .2, an: 'left'});
      sc.add(`<div class="iduo iok">✓ ${c.ok}<small>${c.oks || ''}</small></div>`, {x: 790, w: 440, y: y0 + 120, at: c.wok ? w(i, c.wok) : a + .7, an: 'right'});
      if (c.txt) sc.add(`<div class="iword">${c.txt}</div>`, {x: 540, w: 0, y: y0 + 520, at, an: 'slam', css: {transform: 'translateX(-50%)'}});
    } else if (c.t === 'gauge') {
      const g = sc.add(`<div class="igauge"><i></i></div>`, {x: 540, w: 820, y: y0 + 260, at: a, an: 'fade'});
      sc.add(`<div class="iword">${c.txt}</div>`, {x: 540, w: 0, y: y0 + 420, at, an: 'slam', css: {transform: 'translateX(-50%)'}});
      sc.on(t => {const q = J.clamp((t - a) / Math.max(.6, (b - a) * .8)); const v = c.from + (c.to - c.from) * q; const bar = g.querySelector('i'); bar.style.width = v + '%'; bar.style.background = v < 55 ? '#3FB66B' : v < 80 ? '#FFB020' : '#E53935';});
    } else if (c.t === 'projet') {
      sc.add(`<div class="icard" style="width:880px"><img src="${c.src}"></div>`, {x: 540, w: 880, y: 220, at: a, an: 'zoom'});
      sc.add(`<div style="display:inline-flex;align-items:center;gap:18px;background:#fff;border-radius:22px;padding:14px 28px">${c.logo ? `<img src="${c.logo}" style="height:54px">` : ''}<span style="font-weight:900;font-size:44px;color:#111">${c.nom}</span></div>`, {x: 540, w: 0, y: 820, at: at, an: 'pop', css: {transform: 'translateX(-50%)', whiteSpace: 'nowrap'}});
      if (c.url) sc.text(`<span class="icap">${c.url}</span>`, {y: 950, at: at + .3});
    }
    if (c.note) sc.text(`<span class="itag">${c.note}</span>`, {y: 1160, at: a + .3, an: 'fade'});
  });
  J.cta(t0(last), o.cta);
  J.cfg.thumbAt = o.thumbAt ?? t0(1) + .8;
};
