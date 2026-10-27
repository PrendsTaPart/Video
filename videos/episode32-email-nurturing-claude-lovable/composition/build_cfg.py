"""Construit cfg.js (timeline) et config.json pour un épisode à partir de aligned.json.
Usage : python3 build_cfg.py v32 [pause] [fin]"""
import json, sys

d = sys.argv[1]
PAUSE = float(sys.argv[2]) if len(sys.argv) > 2 else 2.6
FIN = float(sys.argv[3]) if len(sys.argv) > 3 else 5.0
LEAD = 0.35
secs = json.load(open(f"{d}/aligned.json"))
A = [s[0][1] for s in secs]
E = [s[-1][2] for s in secs]
P, t = [], 0.0
for i in range(len(secs)):
    P.append(round(t, 2))
    t += (E[i] - A[i]) + LEAD + PAUSE
dur = round(t - PAUSE + FIN, 2)

# Sous-titres : groupes de 5 mots max, coupés après une ponctuation forte.
subs = []
for i, s in enumerate(secs):
    cur = []
    for w in s:
        cur.append(w)
        if len(cur) >= 5 or w[0][-1] in ".,:;…?!":
            subs.append(cur); cur = []
    if cur:
        subs.append(cur)
    for c in subs[-len(subs):]:
        pass
cues = []
k = 0
for i, s in enumerate(secs):
    g = lambda x, i=i: round(P[i] + LEAD + (x - A[i]), 2)
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
        txt = " ".join(w[0] for w in c).rstrip(",;:")
        cues.append([a, b, txt])

W = [[[w[0], round(P[i] + LEAD + (w[1] - A[i]), 2)] for w in s] for i, s in enumerate(secs)]
cfg = {"P": P, "A": A, "E": E, "lead": LEAD, "dur": dur, "cues": cues, "words": W}
open(f"{d}/cfg.js", "w").write("window.CFG=" + json.dumps(cfg, ensure_ascii=False) + ";")
json.dump(cfg, open(f"{d}/cfg.json", "w"), ensure_ascii=False)
print(d, "dur", dur, "P", P)
