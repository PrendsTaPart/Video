"""Recale une composition à 120 s (épisodes 33, 34) sur une nouvelle voix plus courte.

Chaque section de l'ancienne voix est remplacée par la nouvelle : la partie parlée de la scène est
compressée à la durée de la nouvelle phrase, la partie musicale qui suit est raccourcie de moitié.
La page garde son render(t) d'origine ; on l'appelle avec un temps « ancien » calculé par morceaux.
Usage : python3 warp.py v33b
"""
import json, re, sys

d = sys.argv[1]
js = open(f"{d}/script.js").read()
A0 = json.loads(re.search(r"const A=(\[[^\]]*\])", js).group(1))
P0 = json.loads(re.search(r"P=(\[[^\]]*\])", js).group(1))
DUR = float(re.search(r"const DUR=([\d.]+)", js).group(1))
secs = json.load(open(f"{d}/aligned.json"))
A = [s[0][1] for s in secs]
E = [s[-1][2] for s in secs]
assert len(secs) == len(P0) == len(A0) - 1, (len(secs), len(P0), len(A0))

old_bp, new_bp = [0.0, P0[0]], [0.0, P0[0]]
Q = []
t = P0[0]
for i in range(len(P0)):
    Q.append(round(t, 3))
    o = A0[i + 1] - A0[i]
    n = (E[i] - A[i]) + 0.35
    nxt = P0[i + 1] if i + 1 < len(P0) else DUR
    tail = nxt - P0[i] - o
    last = i + 1 == len(P0)
    nt = max(tail, 3.5) if last else (tail if tail <= 1.2 else min(5.0, max(1.2, tail * 0.5)))
    old_bp += [P0[i] + o, nxt]
    t += n
    new_bp += [t, t + nt]
    t += nt
dur = round(t, 2)

cues, words = [], []
for i, s in enumerate(secs):
    g = lambda x, i=i: round(Q[i] + (x - A[i]), 2)
    words.append([[w[0], g(w[1])] for w in s])
    grp, cur = [], []
    for w in s:
        cur.append(w)
        if len(cur) >= 5 or w[0][-1] in ".,:;…?!":
            grp.append(cur); cur = []
    if cur:
        grp.append(cur)
    for j, c in enumerate(grp):
        a = g(c[0][1])
        b = g(grp[j + 1][0][1]) if j + 1 < len(grp) else g(c[-1][2]) + 0.35
        cues.append([a, b, " ".join(w[0] for w in c).rstrip(",;:")])

cfg = {"P": Q, "A": A, "E": E, "lead": 0.0, "dur": dur, "cues": cues, "words": words,
       "warp": {"new": [round(x, 3) for x in new_bp], "old": [round(x, 3) for x in old_bp]}}
json.dump(cfg, open(f"{d}/cfg.json", "w"), ensure_ascii=False)
open(f"{d}/cfg.js", "w").write("window.CFG=" + json.dumps(cfg, ensure_ascii=False) + ";")

inject = """<script src="cfg.js"></script>
<div id="sub2" style="position:absolute;left:60px;right:60px;top:1600px;text-align:center;z-index:90;display:none"><span style="display:inline;font-family:Poppins,sans-serif;font-weight:600;font-size:46px;line-height:1.45;padding:8px 20px;border-radius:12px;color:#FCF9E6;background:#0F1A23;-webkit-box-decoration-break:clone;box-decoration-break:clone"></span></div>
<script>
// Temps recalé sur la nouvelle voix : la scène d'origine est rejouée au temps « ancien » correspondant.
(function () {
  const C = window.CFG, N = C.warp.new, O = C.warp.old, base = window.render, sub = document.getElementById('sub2');
  const old = t => { for (let k = 1; k < N.length; k++) if (t <= N[k]) return O[k - 1] + (O[k] - O[k - 1]) * ((t - N[k - 1]) / Math.max(1e-6, N[k] - N[k - 1])); return O[O.length - 1]; };
  window.render = t => {
    base(Math.min(old(t), O[O.length - 1] - 0.001));
    const c = C.cues.find(c => t >= c[0] && t < c[1]);
    sub.style.display = c ? 'block' : 'none';
    if (c) sub.firstElementChild.textContent = c[2];
  };
  const th = window.thumb; window.thumb = () => { th(); sub.style.display = 'none'; };
})();
</script>
"""
h = open(f"{d}/index.html").read()
h = h.replace('<script src="script.js"></script>', '<script src="script.js"></script>\n' + inject, 1)
open(f"{d}/index.html", "w").write(h)
print(d, "dur", dur, "Q", Q)
