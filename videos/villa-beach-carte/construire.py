"""vo.mp3 + scenes.json + carte.json -> words.json, cfg.js, cfg.json, vo.wav (même méthode que serie-10-applications/moteur/construire.py)."""
import json, os, re, subprocess, difflib
D = os.path.dirname(os.path.abspath(__file__))
norm = lambda w: re.sub(r"[^a-z0-9àâäéèêëîïôöùûüç]", "", w.lower())
if not os.path.exists(f"{D}/words.json"):
    from faster_whisper import WhisperModel
    import numpy as np
    m = WhisperModel("small", compute_type="int8")
    r = subprocess.run(["ffmpeg", "-v", "error", "-i", f"{D}/vo.mp3", "-f", "s16le", "-ac", "1", "-ar", "16000", "-"], capture_output=True).stdout
    segs, _ = m.transcribe(np.frombuffer(r, np.int16).astype(np.float32) / 32768, language="fr", word_timestamps=True)
    json.dump([(w.word.strip(), round(w.start, 2), round(w.end, 2)) for s in segs for w in s.words], open(f"{D}/words.json", "w"), ensure_ascii=False)
wh = json.load(open(f"{D}/words.json"))
SC = json.load(open(f"{D}/scenes.json"))
toks, idx = [], []
for k, (txt, v) in enumerate(SC):
    for w in txt.split(): toks.append(w); idx.append(k)
a = [norm(x) for x in toks]; b = [norm(w[0]) for w in wh]; T = [None] * len(a)
for blk in difflib.SequenceMatcher(None, a, b, autojunk=False).get_matching_blocks():
    for i in range(blk.size): T[blk.a + i] = wh[blk.b + i][1]
if T[0] is None: T[0] = wh[0][1]
if T[-1] is None: T[-1] = wh[-1][1]
kn = [i for i, t in enumerate(T) if t is not None]
for i in range(len(T)):
    if T[i] is None:
        lo = max(k for k in kn if k < i); hi = min(k for k in kn if k > i)
        T[i] = T[lo] + (T[hi] - T[lo]) * (i - lo) / (hi - lo)
for i in range(1, len(T)): T[i] = max(T[i], T[i - 1] + 0.05)
O = 0.3
words = [[w, round(t + O, 2), k] for w, t, k in zip(toks, T, idx)]
dur = round(wh[-1][2] + O + 2.5, 2)
starts = [0.0] + [round(next(w[1] for w in words if w[2] == k) - 0.12, 2) for k in range(1, len(SC))]
scenes = [{"v": v, "t0": starts[k], "t1": starts[k + 1] if k + 1 < len(SC) else dur + 1} for k, (t, v) in enumerate(SC)]
thumbT = round(scenes[4]["t0"] + 1.5, 2)
carte = json.load(open(f"{D}/carte.json"))
open(f"{D}/cfg.js", "w").write("window.CFG=" + json.dumps(dict(dur=dur, words=words, scenes=scenes, carte=carte, thumbT=thumbT), ensure_ascii=False) + ";")
json.dump(dict(dur=dur, words=words), open(f"{D}/cfg.json", "w"), ensure_ascii=False)
subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", f"{D}/vo.mp3", "-af", f"adelay={int(O*1000)}|{int(O*1000)},apad=whole_dur={dur}", "-t", str(dur), "-ac", "1", "-ar", "48000", f"{D}/vo.wav"], check=True)
print("durée", dur, "·", len(words), "mots ·", [s["t0"] for s in scenes])
