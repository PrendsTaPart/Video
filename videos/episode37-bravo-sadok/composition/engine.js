// Moteur commun : tout est fonction du temps t (render(t)).
// data-at="s:k" = mot k de la section s de la voix ; data-at="+x" = x s après le début de la scène.
// data-fx : pop (défaut), slam, fade, left ; class kb = zoom lent ; data-scroll="px" = défilement de l'image.
const C = window.CFG;
const cl = (x, a = 0, b = 1) => Math.min(b, Math.max(a, x));
const eout = x => 1 - Math.pow(1 - x, 3);
const scenes = [...document.querySelectorAll('.scene')];
const bounds = scenes.map((el, i) => [C.P[i], i + 1 < C.P.length ? C.P[i + 1] : C.dur]);
const T = (spec, i) => {
  if (spec[0] === '+') return bounds[i][0] + parseFloat(spec.slice(1));
  const [s, k] = spec.split(':').map(Number);
  return C.words[s][k][1];
};
const items = scenes.map((el, i) => [...el.querySelectorAll('[data-at]')].map(e => [e, T(e.dataset.at, i), e.dataset.fx || 'pop', parseFloat(e.dataset.d || .45)]));
const kbs = scenes.map(el => [...el.querySelectorAll('.kb,[data-scroll]')]);
const sub = document.getElementById('sub');

function render(t) {
  document.getElementById('thumb').style.display = 'none';
  scenes.forEach((el, i) => {
    const [a, b] = bounds[i];
    const on = t >= a && t < b + (i === scenes.length - 1 ? 1 : 0);
    el.style.display = on ? 'block' : 'none';
    if (!on) return;
    const fi = i === 0 ? 1 : cl((t - a) / .25), fo = i === scenes.length - 1 ? 1 : 1 - cl((t - (b - .2)) / .2);
    el.style.opacity = Math.min(fi, fo);
    for (const [e, at, fx, d] of items[i]) {
      const p = eout(cl((t - at) / d));
      e.style.opacity = fx === 'slam' ? (t >= at ? 1 : 0) : p;
      if (fx === 'pop') e.style.transform = `translateY(${(1 - p) * 50}px)`;
      else if (fx === 'left') e.style.transform = `translateX(${(1 - p) * -80}px)`;
      else if (fx === 'slam') { const x = cl((t - at) / .3); e.style.transform = `scale(${1.5 - .5 * eout(x)})`; }
    }
    for (const e of kbs[i]) {
      const q = cl((t - a) / (b - a));
      if (e.dataset.scroll) e.firstElementChild.style.transform = `translateY(${-parseFloat(e.dataset.scroll) * (q * q * (3 - 2 * q))}px)`;
      else e.firstElementChild.style.transform = `scale(${1 + .07 * q})`;
    }
  });
  const c = C.cues.find(c => t >= c[0] && t < c[1]);
  sub.style.display = c ? 'block' : 'none';
  if (c) sub.firstElementChild.textContent = c[2];
}
function thumb() { scenes.forEach(e => e.style.display = 'none'); sub.style.display = 'none'; document.getElementById('thumb').style.display = 'block'; }
window.render = render; window.thumb = thumb;
