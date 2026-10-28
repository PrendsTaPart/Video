// Moteur de scènes commun aux épisodes 40+ (tout est fonction du temps t).
const C = window.CFG;
const cl = (x, a = 0, b = 1) => Math.min(b, Math.max(a, x));
const eo = x => 1 - Math.pow(1 - cl(x), 3);
const ebk = x => { x = cl(x); const c = 1.7; return 1 + (c + 1) * Math.pow(x - 1, 3) + c * Math.pow(x - 1, 2); };
const M = ph => { if (!(ph in C.marks)) throw new Error('repère ' + ph); return C.marks[ph]; };
const stage = document.getElementById('stage');
const SC = [], GLOBAL = [];
const KIT = '../kit/';
let CAP = { top: 1400, group: 4, kw: new Set(), names: {}, show: () => true };

function mk(html, cls) { const d = document.createElement('div'); d.className = cls || ''; d.innerHTML = html; return d; }
function scene(t0, t1, o = {}) {
  const el = mk('', 'sc ' + (o.cls || ''));
  el.style.zIndex = o.z || 1;
  if (o.bg) { const b = document.createElement('div'); b.className = 'bg'; b.style.backgroundImage = `url(${o.bg.includes('/') ? o.bg : KIT + o.bg})`; el.appendChild(b); el._bg = b; }
  if (o.bgColor) el.style.background = o.bgColor;
  stage.querySelector('#scenes').appendChild(el);
  const s = { node: el, t0, t1, o, items: [], fns: [] };
  s.img = (src, p = {}) => add(s, `<img src="${src.includes('/') ? src : KIT + src}">`, p, 'it im');
  s.txt = (html, p = {}) => add(s, html, p, 'it tx ' + (p.cls || ''));
  s.el = (html, p = {}) => add(s, html, p, 'it ' + (p.cls || ''));
  s.fn = f => (s.fns.push(f), s);
  SC.push(s); return s;
}
function add(s, html, p, cls) {
  const d = mk(html, cls);
  d.style.left = (p.x ?? 540) + 'px'; d.style.top = (p.y ?? 960) + 'px';
  if (p.w) d.style.width = p.w + 'px';
  if (p.h) d.style.height = p.h + 'px';
  if (p.z) d.style.zIndex = p.z;
  if (p.style) d.style.cssText += p.style;
  s.node.appendChild(d);
  const it = Object.assign({ d, at: s.t0, fx: 'pop', dur: .45 }, p);
  s.items.push(it); return it;
}
function onFrame(f) { GLOBAL.push(f); }

function fxT(it, t) {
  const p = (t - it.at) / it.dur;
  if (t < it.at) return [0, 'scale(.001)'];
  let o = 1, tr = '';
  const e = ebk(p), q = eo(p);
  switch (it.fx) {
    case 'pop': o = cl(p * 2); tr = `scale(${.4 + .6 * e})`; break;
    case 'slam': o = cl(p * 3); tr = `scale(${1.8 - .8 * q})`; break;
    case 'fade': o = q; break;
    case 'up': o = cl(p * 2); tr = `translateY(${(1 - e) * 140}px)`; break;
    case 'down': o = cl(p * 2); tr = `translateY(${(e - 1) * 220}px)`; break;
    case 'left': o = cl(p * 2); tr = `translateX(${(1 - e) * -700}px)`; break;
    case 'right': o = cl(p * 2); tr = `translateX(${(1 - e) * 700}px)`; break;
    case 'drop': o = cl(p * 3); tr = `translateY(${(1 - e) * -600}px) rotate(${(1 - e) * -12}deg)`; break;
    case 'none': break;
  }
  if (it.out !== undefined && t > it.out) { const r = cl((t - it.out) / .3); o *= 1 - r; tr += ` scale(${1 - .2 * r})`; }
  const a = t - it.at;
  switch (it.anim) {
    case 'bob': tr += ` translateY(${Math.sin(a * 3) * 10}px)`; break;
    case 'talk': tr += ` translateY(${-Math.abs(Math.sin(a * 9)) * 10}px)`; break;
    case 'shake': tr += ` rotate(${Math.sin(a * 40) * 4}deg)`; break;
    case 'pulse': tr += ` scale(${1 + Math.sin(a * 5) * .04})`; break;
    case 'sway': tr += ` rotate(${Math.sin(a * 2) * 3}deg)`; break;
    case 'float': tr += ` translateY(${Math.sin(a * 1.6) * 16}px) rotate(${Math.sin(a * 1.1) * 2}deg)`; break;
    case 'spin': tr += ` rotate(${a * 30}deg)`; break;
    case 'shiver': tr += ` translateX(${Math.sin(a * 60) * 4}px)`; break;
  }
  if (it.rot) tr += ` rotate(${it.rot}deg)`;
  if (it.flip) tr += ' scaleX(-1)';
  if (it.sc) tr += ` scale(${it.sc})`;
  return [o, tr];
}
let GROUPS = null;
function caption(t) {
  const cap = document.getElementById('cap'), who = document.getElementById('who');
  const W = C.words;
  if (!GROUPS) { GROUPS = []; let g = []; W.forEach((w, k) => { g.push(k); const nx = W[k + 1]; if (g.length >= CAP.group || /[.,:;?!…]$/.test(w[0]) || (nx && nx[2] !== w[2])) { GROUPS.push(g); g = []; } }); if (g.length) GROUPS.push(g); }
  let cur = -1; for (let k = 0; k < W.length; k++) if (t >= W[k][1] - .02) cur = k;
  const last = W[W.length - 1][1] + .9;
  if (cur < 0 || t > last || !CAP.show(t)) { cap.innerHTML = ''; if (who) who.style.display = 'none'; return; }
  const grp = GROUPS.find(g => g.includes(cur));
  // fin de groupe : on efface après la fin de la phrase si le groupe suivant tarde
  const nxt = W[grp[grp.length - 1] + 1];
  if (nxt && t > nxt[1] - .02 && !grp.includes(cur)) { cap.innerHTML = ''; return; }
  cap.innerHTML = grp.map(k => { const w = W[k], on = t >= w[1] - .02, c = w[0].replace(/[.,:;?!…«»"]/g, ''); const p = cl((t - w[1]) / .12);
    return `<i class="${CAP.kw.has(c) || CAP.kw.has(c.toLowerCase()) ? 'k' : ''} ${k === cur ? 'cur' : ''}" style="opacity:${on ? 1 : 0};transform:scale(${on ? .7 + .3 * ebk(p) : .7})">${w[0]}</i>`; }).join(' ');
  cap.style.top = (typeof CAP.top === 'function' ? CAP.top(t) : CAP.top) + 'px';
  if (who && C.lines.length) { const ln = C.lines[W[cur][2]]; const n = CAP.names[ln.sp]; if (n && t <= ln.t1 + .3) { who.style.display = 'block'; who.firstChild.textContent = n[0]; who.firstChild.style.background = n[1]; } else who.style.display = 'none'; }
}
function speaking(sp, t) { return C.lines.some(l => l.sp === sp && t >= l.t0 && t <= l.t1); }
function render(t) {
  SC.forEach((s, i) => {
    const on = t >= s.t0 && t < s.t1 + (s.o.hold || 0);
    s.node.style.display = on ? 'block' : 'none'; if (!on) return;
    const fi = s.o.tr === 'cut' ? 1 : cl((t - s.t0) / .22);
    s.node.style.opacity = fi;
    if (s.node._bg) { const kb = s.o.kb || [1, 1.08]; const p = cl((t - s.t0) / Math.max(1, s.t1 - s.t0)); s.node._bg.style.transform = `scale(${kb[0] + (kb[1] - kb[0]) * p})` + (s.o.pan ? ` translate(${s.o.pan[0] * p}px,${s.o.pan[1] * p}px)` : ''); }
    s.items.forEach(it => { const [o, tr] = fxT(it, t); it.d.style.opacity = o; it.d.style.transform = 'translate(-50%,-50%) ' + tr; });
    s.fns.forEach(f => f(t, s));
  });
  GLOBAL.forEach(f => f(t));
  caption(t);
}
function thumbAt(t, html) { window.thumb = () => { render(t); if (html) document.getElementById('cap').innerHTML = html; }; }
