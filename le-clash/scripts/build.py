import json, math, random
from collections import deque

random.seed(7)
FPS, W, H = 30, 1080, 1920
grid  = json.load(open("work/beatgrid.json"))
lines = json.load(open("work/lines.json"))
CAT   = json.load(open("work/catalogue.json"))
BEAT, PHASE = grid["period"], grid["phase"]
DUR = 202.920

import subprocess, os
def probe(p):
    return float(subprocess.run(["ffprobe","-v","error","-show_entries","format=duration",
        "-of","csv=p=0",p],capture_output=True,text=True).stdout.strip())
SRC, SDUR = {}, {}
for k in CAT:
    p = f"sources/{k}.mp4" if os.path.exists(f"sources/{k}.mp4") else f"sources-local/{k}.mp4"
    SRC[k] = p; SDUR[k] = probe(p)

def snap(t):
    k = round((t - PHASE) / BEAT)
    return round(PHASE + k * BEAT, 4)
def beats(t, n):
    return round(t + n * BEAT, 4)

L = {}
for ln in lines: L.setdefault(ln["section"], []).append(ln)
def line_at(sec, prefix):
    return next(x for x in L[sec] if x["text"].startswith(prefix))
def word_time(ln, word):
    return next(w["s"] for w in ln["words"] if w["w"].lower().strip("«»,;:?!") == word)

# ---------- réserve de plans : chaque (source, fenêtre) n'est utilisée qu'une fois ----------
class Pool:
    def __init__(self, side, exclude=()):
        ids = [k for k, v in CAT.items() if v[0] == side and k not in exclude]
        random.shuffle(ids)
        self.q = deque(ids); self.cur = {k: 0.10 for k in ids}; self.wrap = 0
    def take(self, dur, src=None):
        if src is not None:
            off = self.cur.get(src, 0.10)
            if off + dur > SDUR[src] - 0.05:
                off = 0.10; self.wrap += 1
            self.cur[src] = off + dur + 0.12
            if src in self.q: self.q.remove(src); self.q.append(src)
            return src, round(off, 3)
        for _ in range(len(self.q)):
            k = self.q.popleft(); self.q.append(k)
            off = self.cur[k]
            if off + dur <= SDUR[k] - 0.05:
                self.cur[k] = off + dur + 0.12
                return k, round(off, 3)
        k = self.q.popleft(); self.q.append(k)
        self.cur[k] = 0.10 + dur + 0.12; self.wrap += 1
        return k, 0.10

CHAOS = Pool("chaos", exclude=())
MAIT  = Pool("maitrise", exclude=())

SHOTS = []
def shot(t0, t1, side, layer="full", src=None, sin=None, pool=None, **kw):
    d = round(t1 - t0, 4)
    if d <= 0.02: return None
    if src is None:
        p = pool or (CHAOS if side == "chaos" else MAIT)
        src, sin = p.take(d, None)
    elif sin is None:
        p = pool or (CHAOS if side == "chaos" else MAIT)
        src, sin = p.take(d, src)
    s = dict(t0=round(t0,4), t1=round(t1,4), dur=d, side=side, layer=layer,
             src=src, sin=sin, file=SRC[src], titre=CAT[src][1], **kw)
    SHOTS.append(s); return s

def fill(t0, t1, side, layer="full", nbeats=1.0, pool=None, first_src=None, **kw):
    """découpe [t0,t1] en coupes de nbeats temps, toutes calées sur la grille"""
    t = t0; first = True
    while t < t1 - 0.05:
        nxt = min(beats(t, nbeats), t1)
        if t1 - nxt < BEAT * nbeats * 0.6: nxt = t1
        shot(t, nxt, side, layer, src=(first_src if first else None), pool=pool, **kw)
        first = False; t = nxt

# ================= INTRO =================
V1 = snap(L["COUPLET 1"][0]["start"])                       # 12.487
SHOTS.append(dict(t0=0.0, t1=snap(2.1), dur=None, side="noir", layer="card",
                  src=None, sin=None, file=None, titre="noir", card="black"))
t_black = snap(2.1)
t_cry   = beats(V1, -4)                                     # 4 temps avant le couplet
SHOTS.append(dict(t0=t_black, t1=t_cry, side="carte", layer="card", src=None, sin=None,
                  file=None, titre="carton 20:15", card="2015", dur=round(t_cry-t_black,4)))
t_calm  = beats(t_cry, 1)
shot(t_cry, t_calm, "chaos", src="EP083", sin=0.0, note="le cri")
shot(t_calm, V1, "duel", src="EP142", sin=0.0, note="le calme (EP142 0–1,5 s)")

# ================= COUPLET 1 : grammaire « subit » =================
MAP1 = {
 "Le ticket sort":"EP008", "L'imprimante crache":"EP021", "J'crie":"EP083",
 "Le passe est plein":"EP108", "Dix applis":"EP087", "J'éteins l'une":"EP045",
 "Un tupperware":"EP031", "J'ouvre, j'renifle":"hf2-24-chambre-froide",
 "Le planning au marqueur":"EP064", "Deux qui posent":"EP131",
 "Une étoile sur le web,":"EP088", "J'la vois lundi":"EP099",
 "Empile les assiettes":"EP029",
}
C1 = L["COUPLET 1"]
for i, ln in enumerate(C1):
    a = snap(ln["start"]); b = snap(C1[i+1]["start"]) if i+1 < len(C1) else snap(66.30)
    if ln["text"].startswith("Une seule qui bouge"):
        continue                                            # absorbé par EP015 ci-dessous
    if ln["text"].startswith("et y'a plus rien"):
        continue
    if ln["text"].startswith("Empile les assiettes"):
        b = snap(56.20)
    src = next((v for k, v in MAP1.items() if ln["text"].startswith(k)), None)
    nb = 1.0 if i < 8 else 1.5                              # ça s'accélère puis respire
    fill(a, b, "chaos", nbeats=nb, first_src=src, ligne=ln["text"])

REF1 = snap(L["REFRAIN"][0]["start"])                       # 66.30
t15 = round(REF1 - 10.08, 4)                                # EP015 en entier, chute pile sur le refrain
shot(snap(56.20), snap(t15), "chaos", ligne="Empile encore")
shot(snap(t15), REF1, "chaos", src="EP015", sin=0.0,
     ligne="Une seule qui bouge en bas / plus rien qui tient debout",
     note="EP015 en entier — l'écroulement finit sur le 1er temps du refrain")

# ================= REFRAIN 1 : split-screen =================
lnA = line_at("REFRAIN", "Y'en a un qui court")
T_FREEZE = snap(lnA["start"])                                # « y'en a un qui court derrière »
T_OPEN   = snap(lnA["words"][6]["s"])                        # « y'en a un qui a d'l'avance »
REF1_END = snap(L["COUPLET 2"][0]["start"])                  # 86.36
fill(REF1, T_FREEZE, "chaos",    layer="top",    nbeats=1.5, section="refrain1")
fill(REF1, T_FREEZE, "maitrise", layer="bottom", nbeats=4.0, section="refrain1")
shot(T_FREEZE, T_OPEN, "chaos", layer="top", freeze=True, nb=True,
     note="moitié haute figée en noir et blanc")
fill(T_FREEZE, T_OPEN, "maitrise", layer="bottom", nbeats=4.0)
fill(T_OPEN, REF1_END, "maitrise", nbeats=4.0, note="la moitié basse s'ouvre en plein cadre")

# ================= COUPLET 2 : grammaire « tient » =================
MAP2 = {
 "Chez moi le ticket":"hf2-21-chef-tablette", "Chaque poste voit":"hero-kds-mural",
 "Table six":"EP141", "J'envoie avant":"hf2-10-notification-depart",
 "Quarante couverts":"EP103", "J'ai sorti":"EP143",
 "Une étoile sur le web ?":"EP088", "Le procès":"EP144",
 "Le ring light":"EP100", "J'poste, j'encaisse":"EP114",
 "Le frigo trois":"EP067", "Et le classeur":"EP072",
}
C2 = L["COUPLET 2"]; PONT0 = snap(L["PONT"][0]["start"] - 0.54)
for i, ln in enumerate(C2):
    a = snap(ln["start"]); b = snap(C2[i+1]["start"]) if i+1 < len(C2) else PONT0
    src = next((v for k, v in MAP2.items() if ln["text"].startswith(k)), None)
    if src == "EP141":
        shot(a, beats(a, 5), "maitrise", src="EP141", sin=0.0,
             ligne=ln["text"], note="le plan le plus long du clip (2,08 s)")
        fill(beats(a, 5), b, "maitrise", nbeats=3.0, ligne=ln["text"])
    else:
        fill(a, b, "maitrise", nbeats=4.0, first_src=src, ligne=ln["text"])

# ================= PONT : aucun texte, aucune incrustation =================
PONT = L["PONT"]
T142 = snap(149.54 - 8.6)                                    # EP142 : le dressage tombe sur la ligne
for i, ln in enumerate(PONT[:4]):
    a = snap(ln["start"]) if i else PONT0
    b = snap(PONT[i+1]["start"]) if i+1 < 4 else T142
    side = "chaos" if i % 2 == 0 else "maitrise"
    fill(a, b, side, nbeats=(b-a)/BEAT, ligne=ln["text"], note="réplique du pont")
shot(T142, T142+5.0, "duel", src="EP142", sin=0.0, note="pont — duel western, sans coupe")
shot(T142+5.0, T142+5.6, "duel", src="EP142", sin=5.0, freeze=True, flash=True,
     note="les spatules dégainées : gel 0,6 s + flash blanc 2 images")
shot(T142+5.6, T142+10.68, "duel", src="EP142", sin=5.0, note="suite sans coupe — le dressage")
C3_0 = snap(L["COUPLET 3"][0]["start"])
shot(T142+10.68, C3_0, "duel", src="EP142", sin=9.90, freeze=True,
     note="tenue sur les deux assiettes dressées")

# ================= COUPLET 3 : le split se referme =================
ln1 = L["COUPLET 3"][0]
T_MERGE = snap(word_time(ln1, "lundi") - 0.30)
fill(C3_0, T_MERGE, "chaos",    layer="top",    nbeats=2.0, section="couplet3")
fill(C3_0, T_MERGE, "maitrise", layer="bottom", nbeats=2.0, section="couplet3")
C3 = L["COUPLET 3"]; RF0 = snap(L["REFRAIN FINAL"][0]["start"])
t = T_MERGE
for i, ln in enumerate(C3):
    b = snap(C3[i+1]["start"]) if i+1 < len(C3) else RF0
    if b <= t: continue
    fill(t, b, "maitrise" if i % 2 else "chaos", nbeats=3.0, ligne=ln["text"])
    t = b

# ================= REFRAIN FINAL : alternance sur le même temps =================
OUT0 = snap(189.76)
t, k = RF0, 0
while t < OUT0 - 0.05:
    nxt = min(beats(t, 1.0), OUT0)
    shot(t, nxt, "chaos" if k % 2 == 0 else "maitrise", section="refrain final")
    t = nxt; k += 1

# ================= OUTRO =================
T_END_FREEZE = snap(192.40)
T_STING = snap(198.75)
fill(OUT0, T_END_FREEZE, "maitrise", nbeats=3.0, section="outro")
shot(T_END_FREEZE, T_STING, "duel", src="EP142", sin=9.90, freeze=True,
     card="outro", note="image figée sur les deux assiettes dressées")
SHOTS.append(dict(t0=T_STING, t1=DUR, dur=round(DUR-T_STING,4), side="sting", layer="full",
                  src="STING", sin=0.0, file="work/sting.mp4",
                  titre="sting logo FoodEatUp", note="animation de fin — logo FoodEatUp"))

SHOTS.sort(key=lambda s: s["t0"])
# contrôle : continuité par couche et calage sur la grille
errs = []
def check_chain(seq, label, t_from, t_to):
    prev = t_from
    for s in seq:
        if abs(s["t0"] - prev) > 0.001:
            errs.append(f"{label} : trou/chevauchement à {s['t0']} (attendu {prev})")
        prev = s["t1"]
    if abs(prev - t_to) > 0.05: errs.append(f"{label} : fin {prev} ≠ {t_to}")

main = [s for s in SHOTS if s["layer"] in ("full", "card", "top")]
check_chain(main, "principale", 0.0, DUR)
splits = []
for s in SHOTS:
    if s["layer"] == "top":
        if splits and abs(splits[-1][1] - s["t0"]) < 0.001: splits[-1][1] = s["t1"]
        else: splits.append([s["t0"], s["t1"]])
for a, b in splits:
    check_chain([s for s in SHOTS if s["layer"] == "bottom" and a - 0.001 <= s["t0"] < b],
                f"moitié basse {a}-{b}", a, b)
for s in SHOTS:
    n = (s["t0"] - PHASE) / (BEAT / 2)
    if abs(n - round(n)) > 0.02 and s["t0"] > 0: errs.append(f"hors grille : {s['t0']}")

used = {}
for s in SHOTS:
    if s["src"] and s["src"] in CAT: used[s["src"]] = used.get(s["src"], 0) + 1
json.dump({"audio":"audio/le-clash.mp3","fps":FPS,"size":[W,H],"bpm":grid["bpm"],
           "beat":BEAT,"phase":PHASE,"duration":DUR,
           "sections":{k:[round(min(x['start'] for x in v),2),round(max(x['end'] for x in v),2)]
                       for k,v in L.items()},
           "shots":SHOTS}, open("shotlist.json","w"), ensure_ascii=False, indent=1)

print(f"{len(SHOTS)} plans | {len(used)} sources distinctes utilisées sur {len(CAT)}")
print(f"réemplois de fenêtre (0 = aucun visuel répété) : chaos {CHAOS.wrap}, maîtrise {MAIT.wrap}")
print(f"erreurs de grille : {len(errs)}")
for e in errs[:8]: print("  !", e)
top = sorted(used.items(), key=lambda x: -x[1])[:6]
print("sources les plus sollicitées :", ", ".join(f"{k}×{v}" for k, v in top))
