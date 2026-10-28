"""Construit cfg.js d'un épisode à partir de spec.json.
mode narr : vo.mp3 + words.json (whisper) + disp (texte affiché) -> mots alignés.
mode dial : lignes [locuteur, fichier, début, fin, texte, écart] -> vo.wav + mots.
marks : liste de phrases (texte affiché) dont on veut le temps de début."""
import json, sys, re, difflib, subprocess
d = sys.argv[1]
S = json.load(open(f"{d}/spec.json"))
norm = lambda w: re.sub(r"[^a-z0-9àâäéèêëîïôöùûüç]", "", w.lower())

def align(disp_tokens, wh, offset):
    """Transfère les temps whisper vers les mots affichés (difflib + interpolation)."""
    a = [norm(x) for x in disp_tokens]; b = [norm(w[0]) for w in wh]
    T = [None] * len(a)
    for blk in difflib.SequenceMatcher(None, a, b, autojunk=False).get_matching_blocks():
        for k in range(blk.size):
            T[blk.a + k] = wh[blk.b + k][1]
    # bornes
    if T[0] is None: T[0] = wh[0][1]
    if T[-1] is None: T[-1] = wh[-1][1]
    known = [i for i, t in enumerate(T) if t is not None]
    for i in range(len(T)):
        if T[i] is None:
            lo = max(k for k in known if k < i); hi = min(k for k in known if k > i)
            T[i] = T[lo] + (T[hi] - T[lo]) * (i - lo) / (hi - lo)
    for i in range(1, len(T)):  # monotone
        T[i] = max(T[i], T[i - 1] + 0.05)
    return [[w, round(t + offset, 2)] for w, t in zip(disp_tokens, T)]

if S["mode"] == "narr":
    O = S.get("offset", 0.3)
    wh = json.load(open(f"{d}/words.json"))
    toks = [x for x in S["disp"].split(" ") if x]
    W = align(toks, wh, O)
    end = wh[-1][2] + O
    for w in W: w.append(0)
    lines = []
    dur = round(end + S.get("tail", 3.0), 2)
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", f"{d}/vo.mp3", "-af", f"adelay={int(O*1000)}|{int(O*1000)},apad=whole_dur={dur}", "-t", str(dur), "-ac", "1", "-ar", "48000", f"{d}/vo.wav"], check=True)
else:
    WH = json.load(open(f"{d}/words.json"))
    t, W, lines, ins, flt = 0.0, [], [], [], []
    for k, (sp, f, a, b, txt, gap) in enumerate(S["lines"]):
        t += gap
        src = f"{d}/a/{f}.mp3"
        wh = [w for w in WH[src] if a - 0.05 <= w[1] < b]
        v0 = wh[0][1] if wh else a
        toks = txt.split()
        if wh:
            ww = align(toks, wh, t - a)
        else:
            ww = [[x, round(t + (b - a) * i / len(toks), 2)] for i, x in enumerate(toks)]
        for w in ww: w.append(k)
        W += ww
        lines.append({"sp": sp, "t0": round(t, 2), "t1": round(t + b - a, 2), "txt": txt})
        ins += ["-i", src]; ms = int(t * 1000)
        flt.append(f"[{k}:a]atrim={a}:{b},asetpts=PTS-STARTPTS,afade=t=in:d=0.02,afade=t=out:st={max(0,b-a-0.05):.2f}:d=0.05,aresample=48000,adelay={ms}|{ms}[l{k}]")
        t += b - a
    dur = round(t + S.get("tail", 3.0), 2)
    n = len(S["lines"])
    flt.append("".join(f"[l{k}]" for k in range(n)) + f"amix=inputs={n}:normalize=0,apad=whole_dur={dur}[o]")
    subprocess.run(["ffmpeg", "-y", "-v", "error", *ins, "-filter_complex", ";".join(flt), "-map", "[o]", "-t", str(dur), "-ac", "1", f"{d}/vo.wav"], check=True)

def find(ph):
    p = [norm(x) for x in ph.split()]; a = [norm(w[0]) for w in W]
    for i in range(len(a) - len(p) + 1):
        if a[i:i + len(p)] == p: return W[i][1]
    raise SystemExit(f"repère introuvable : {ph}")
marks = {m: find(m) for m in S.get("marks", [])}
cfg = {"dur": dur, "words": W, "lines": lines, "marks": marks}
open(f"{d}/cfg.js", "w").write("window.CFG=" + json.dumps(cfg, ensure_ascii=False) + ";")
json.dump(cfg, open(f"{d}/cfg.json", "w"), ensure_ascii=False)
print(d, "dur", dur, "mots", len(W)); [print(f"  {v:6.2f} {k}") for k, v in marks.items()]
