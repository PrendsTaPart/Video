"""Construit un épisode : vo.mp3 -> words.json (faster-whisper) -> cfg.js + index.html + vo.wav.
Usage : python3 moteur/construire.py ep01-haccp-tofu [ep02-...]"""
import json, re, sys, difflib, subprocess, os, shutil
ICI = os.path.dirname(os.path.abspath(__file__)); RAC = os.path.dirname(ICI)
EPS = {e["slug"]: e for e in json.load(open(f"{RAC}/episodes.json"))}
ETIQ = {"tofu": "1/3 · Le problème", "mofu": "2/3 · Comment ça marche", "bofu": "3/3 · Passe à l'action"}
norm = lambda w: re.sub(r"[^a-z0-9àâäéèêëîïôöùûüç]", "", w.lower())
_m = None
def whisper(mp3):
    global _m
    from faster_whisper import WhisperModel
    import numpy as np
    if _m is None: _m = WhisperModel("small", compute_type="int8")
    r = subprocess.run(["ffmpeg", "-v", "error", "-i", mp3, "-f", "s16le", "-ac", "1", "-ar", "16000", "-"], capture_output=True).stdout
    segs, _ = _m.transcribe(np.frombuffer(r, np.int16).astype(np.float32) / 32768, language="fr", word_timestamps=True)
    return [(w.word.strip(), round(w.start, 2), round(w.end, 2)) for s in segs for w in s.words]

def align(toks, wh):
    a = [norm(x) for x in toks]; b = [norm(w[0]) for w in wh]; T = [None] * len(a)
    for blk in difflib.SequenceMatcher(None, a, b, autojunk=False).get_matching_blocks():
        for k in range(blk.size): T[blk.a + k] = wh[blk.b + k][1]
    if T[0] is None: T[0] = wh[0][1]
    if T[-1] is None: T[-1] = wh[-1][1]
    kn = [i for i, t in enumerate(T) if t is not None]
    for i in range(len(T)):
        if T[i] is None:
            lo = max(k for k in kn if k < i); hi = min(k for k in kn if k > i)
            T[i] = T[lo] + (T[hi] - T[lo]) * (i - lo) / (hi - lo)
    for i in range(1, len(T)): T[i] = max(T[i], T[i - 1] + 0.05)
    return T

for slug in sys.argv[1:]:
    e = EPS[slug]; d = f"{RAC}/episodes/{slug}"; O = 0.3
    if not os.path.exists(f"{d}/words.json"):
        json.dump(whisper(f"{d}/vo.mp3"), open(f"{d}/words.json", "w"), ensure_ascii=False)
    wh = json.load(open(f"{d}/words.json"))
    toks, idx = [], []
    for k, (txt, v) in enumerate(e["phrases"]):
        for w in txt.split(): toks.append(w); idx.append(k)
    T = align(toks, wh)
    words = [[w, round(t + O, 2), k] for w, t, k in zip(toks, T, idx)]
    end = wh[-1][2] + O; dur = round(end + 2.2, 2)
    starts = []
    for k in range(len(e["phrases"])):
        starts.append(0.0 if k == 0 else round(next(w[1] for w in words if w[2] == k) - 0.12, 2))
    scenes = [{"v": v, "t0": starts[k], "t1": starts[k + 1] if k + 1 < len(starts) else dur + 1} for k, (txt, v) in enumerate(e["phrases"])]
    # miniature : première scène avec écran, sinon la première
    th = next((s for s in scenes if s["v"][0] in "PD"), scenes[0]); thumbT = round(th["t0"] + 0.9, 2)
    court = e["titre"] if len(e["titre"]) <= 48 else e["titre"][:46] + "…"
    ep = dict(n=e["n"], nom=e["nom"], site=e["site"], note=e["note"], etiq=ETIQ[e["funnel"]], titreCourt=court)
    open(f"{d}/cfg.js", "w").write("window.CFG=" + json.dumps(dict(dur=dur, words=words, scenes=scenes, ep=ep, thumbT=thumbT), ensure_ascii=False) + ";")
    json.dump(dict(dur=dur, words=words), open(f"{d}/cfg.json", "w"), ensure_ascii=False)
    shutil.copy(f"{ICI}/modele.html", f"{d}/index.html")
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", f"{d}/vo.mp3", "-af", f"adelay={int(O*1000)}|{int(O*1000)},apad=whole_dur={dur}", "-t", str(dur), "-ac", "1", "-ar", "48000", f"{d}/vo.wav"], check=True)
    print(slug, "durée", dur, "s ·", len(words), "mots ·", len(scenes), "scènes")
