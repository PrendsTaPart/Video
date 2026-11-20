"""python3 construire.py <slug> : base vidéo 1080x1920 (plans + fondus) et cfg/<slug>.js pour habillage.html.
Les photos viennent de la bibliothèque d'assets FoodEatUp (établissement 46, Villa Beach)."""
import json, os, re, subprocess, sys
D = os.path.dirname(os.path.abspath(__file__)); FPS = 30; XF = 0.4; O = 0.5
P = {p["slug"]: p for p in json.load(open(f"{D}/plats.json"))}[sys.argv[1]]
W = f"{D}/work/{P['slug']}"; os.makedirs(W, exist_ok=True)
norm = lambda w: re.sub(r"[^a-z0-9àâäéèêëîïôöùûüç]", "", w.lower())
def run(a): subprocess.run(["ffmpeg", "-y", "-v", "error", *a], check=True)
lignes = []
if P["vo"]:
    wf = f"{W}/words.json"
    if not os.path.exists(wf):
        from faster_whisper import WhisperModel; import numpy as np
        m = WhisperModel("small", compute_type="int8")
        r = subprocess.run(["ffmpeg", "-v", "error", "-i", f"{D}/audio/{P['vo']}", "-f", "s16le", "-ac", "1", "-ar", "16000", "-"], capture_output=True).stdout
        segs, _ = m.transcribe(np.frombuffer(r, np.int16).astype(np.float32) / 32768, language="fr", word_timestamps=True)
        json.dump([(w.word.strip(), w.start, w.end) for s in segs for w in s.words], open(wf, "w"), ensure_ascii=False)
    wh = json.load(open(wf)); k = 0; starts = []
    for _, mot in P["lignes"]:
        while norm(wh[k][0]) != norm(mot): k += 1
        starts.append(wh[k][1] + O - 0.1); k += 1
    k2 = next(i for i in range(k, len(wh)) if norm(wh[i][0]) in ("à", "a"))  # « À la Villa Beach »
    t_titre = wh[k2][1] + O - 0.15; fin_vo = wh[-1][2] + O
    t_carte = round(max(fin_vo + 0.9, t_titre + 2.4), 2)
else:
    starts = [0.5, 3.1, 5.7]; t_titre = 8.2; t_carte = 10.6
dur = round(t_carte + 3.4, 2)
bornes = [0.0, starts[1] - 0.1, starts[2] - 0.1, t_titre - 0.1, t_carte]
for i, (h, *_) in enumerate(P["lignes"]):
    lignes.append([round(starts[i], 2), round((starts[i + 1] if i + 1 < len(starts) else t_titre) - 0.15, 2), h])
# plans avec fondus enchaînés
segs = []
for i, (photo, z0, z1, fx, fy) in enumerate(P["plans"]):
    d = bornes[i + 1] - bornes[i] + (XF if i < 3 else 0); n = int(round(d * FPS)); out = f"{W}/p{i}.mp4"; segs.append((out, d))
    z = f"({z0}+({z1}-{z0})*t/{d:.3f})"
    flt = (f"[0:v]fps={FPS},setsar=1,scale=1080:1920:force_original_aspect_ratio=increase,"
           f"scale=w='trunc(iw*{z}/2)*2':h='trunc(ih*{z}/2)*2':eval=frame,"
           f"crop=1080:1920:x='clip(iw*{fx}-540,0,iw-1080)':y='clip(ih*{fy}-960,0,ih-1920)',"
           f"eq=contrast=1.05:saturation=1.1,vignette=PI/5,setsar=1,format=yuv420p[v]")
    run(["-loop", "1", "-framerate", str(FPS), "-t", f"{d:.3f}", "-i", f"{D}/photos/{photo}.jpg", "-filter_complex", flt,
         "-map", "[v]", "-frames:v", str(n), "-c:v", "libx264", "-preset", "veryfast", "-crf", "16", out])
dc = dur - t_carte
run(["-f", "lavfi", "-i", f"color=c=0x0d0a07:s=1080x1920:r={FPS}:d={dc:.3f}", "-frames:v", str(int(round(dc * FPS))), "-c:v", "libx264", "-crf", "16", "-pix_fmt", "yuv420p", "-vf", "setsar=1", f"{W}/carte.mp4"])
inp = sum((["-i", s] for s, _ in segs), []) + ["-i", f"{W}/carte.mp4"]
fc, prev, off = "", "[0:v]", 0.0
for i in range(1, 4):
    off += segs[i - 1][1] - XF
    fc += f"{prev}[{i}:v]xfade=transition=fade:duration={XF}:offset={off:.3f}[x{i}];"; prev = f"[x{i}]"
fc += f"{prev}[4:v]concat=n=2:v=1:a=0,setsar=1,format=yuv420p[v]"
run([*inp, "-filter_complex", fc, "-map", "[v]", "-r", str(FPS), "-c:v", "libx264", "-preset", "medium", "-crf", "17", f"{W}/base.mp4"])
cfg = dict(dur=dur, nom=P["titre"], lignes=lignes, titre=[round(t_titre, 2), t_carte], carte=t_carte,
           coupes=[round(b, 2) for b in bornes[1:4]], fond=f"photos/{P['plans'][0][0]}.jpg")
open(f"{D}/cfg/{P['slug']}.js", "w").write("window.CFG=" + json.dumps(cfg, ensure_ascii=False) + ";")
print(P["slug"], "durée", dur, "carte", t_carte, [l[0] for l in lignes], "titre", round(t_titre, 2))
