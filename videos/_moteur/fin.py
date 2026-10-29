"""Mixe vo.wav + musique, assemble frames.mp4 -> vidéo finale + SRT. Usage : python3 fin.py v40 nom [volume_musique]"""
import json, subprocess, sys
d, name = sys.argv[1], sys.argv[2]; vol = float(sys.argv[3]) if len(sys.argv) > 3 else 0.16
import os
_ici = os.path.dirname(os.path.abspath(__file__))
M = os.environ.get("MUSIQUE") or next(p for p in (os.path.join(_ici, "musique-produit.mp3"), os.path.join(_ici, "..", "planit-academy", "assets", "audio", "musique-produit.mp3")) if os.path.exists(p))
c = json.load(open(f"{d}/cfg.json")); dur = c["dur"]
run = lambda *a: subprocess.run(["ffmpeg", "-y", "-v", "error", *a], check=True)
run("-stream_loop", "6", "-i", M, "-t", str(dur), "-ar", "48000", "-ac", "2", f"{d}/bed.wav")
run("-i", f"{d}/vo.wav", "-i", f"{d}/bed.wav", "-filter_complex",
    f"[0:a]aresample=48000,asplit[v1][v2];[1:a]volume={vol},afade=t=out:st={dur-2.5}:d=2.5[mu];[mu][v1]sidechaincompress=threshold=0.03:ratio=8:attack=20:release=400[du];"
    f"[v2][du]amix=inputs=2:normalize=0:duration=first,loudnorm=I=-14:TP=-1.5:LRA=11,aresample=48000[o]", "-map", "[o]", "-t", str(dur), f"{d}/mix.wav")
out = f"{d}/{name}-{round(dur)}s.mp4"
run("-i", f"{d}/frames.mp4", "-i", f"{d}/mix.wav", "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-shortest", "-movflags", "+faststart", out)
def ts(x):
    ms = int(round(x * 1000)); h, ms = divmod(ms, 3600000); m, ms = divmod(ms, 60000); s, ms = divmod(ms, 1000); return f"{h:02}:{m:02}:{s:02},{ms:03}"
W = c["words"]; G = []; g = []
for k, w in enumerate(W):
    g.append(k); nx = W[k + 1] if k + 1 < len(W) else None
    if len(g) >= 7 or w[0][-1] in ".,:;?!…" or (nx and nx[2] != w[2]): G.append(g); g = []
if g: G.append(g)
cues = [(W[g[0]][1], (W[G[i + 1][0]][1] if i + 1 < len(G) else W[g[-1]][1] + .8), " ".join(W[k][0] for k in g)) for i, g in enumerate(G)]
open(f"{d}/{name}-sous-titres.srt", "w").write("\n".join(f"{i+1}\n{ts(a)} --> {ts(b)}\n{t}\n" for i, (a, b, t) in enumerate(cues)))
print(out)
