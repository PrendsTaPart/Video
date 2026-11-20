"""python3 melanger.py <slug> : voix (si présente) + musique -> final/villa-beach-<slug>.mp4 et sa miniature."""
import json, os, re, subprocess, sys
D = os.path.dirname(os.path.abspath(__file__)); s = sys.argv[1]; W = f"{D}/work/{s}"
P = {p["slug"]: p for p in json.load(open(f"{D}/plats.json"))}[s]
C = json.loads(re.sub(r"^window\.CFG=|;$", "", open(f"{D}/cfg/{s}.js").read().strip()))
MUS = {"magret": ("bistro", 0), "jarret-agneau": ("bistro", 3), "veloute": ("diner", 0), "supreme-poulet": ("diner", 8),
       "foie-gras": ("lounge", 0), "tagliatelles-burrata": ("lounge", 4), "burger-poulet": ("stories", 0),
       "pain-perdu": ("dessert", 0), "fondant-chocolat": ("dessert", 4)}
m, off = MUS[s]; dur = C["dur"]; os.makedirs(f"{D}/final", exist_ok=True)
def run(a): subprocess.run(["ffmpeg", "-y", "-v", "error", *a], check=True)
mus = f"[m0]aresample=48000,atrim={off}:{off + dur},asetpts=PTS-STARTPTS,afade=t=in:d=0.4,afade=t=out:st={dur - 1.2}:d=1.2"
if P["vo"]:
    fc = (f"[0:a]aresample=48000,adelay=500|500,apad=whole_dur={dur},acompressor=threshold=-18dB:ratio=2.5:attack=10:release=200,asplit[v1][v2];"
          f"[1:a]anull[m0];{mus},volume=0.6[m];[m][v1]sidechaincompress=threshold=0.03:ratio=6:attack=40:release=500[md];"
          f"[md][v2]amix=inputs=2:normalize=0,loudnorm=I=-14:TP=-1.5:LRA=9[a]")
    inp = ["-i", f"{D}/audio/{P['vo']}", "-i", f"{D}/audio/musique-{m}.mp3"]
else:
    fc = f"[0:a]anull[m0];{mus},loudnorm=I=-14:TP=-1.5:LRA=9[a]"
    inp = ["-i", f"{D}/audio/musique-{m}.mp3"]
run([*inp, "-filter_complex", fc, "-map", "[a]", "-ac", "2", "-t", str(dur), f"{W}/mix.wav"])
out = f"{D}/final/villa-beach-{s}.mp4"
run(["-i", f"{W}/visuel.mp4", "-i", f"{W}/mix.wav", "-map", "0:v", "-map", "1:a", "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-shortest", "-movflags", "+faststart", out])
t = (C["titre"][0] + C["titre"][1]) / 2
run(["-ss", str(t), "-i", f"{W}/base.mp4", "-i", f"{W}/titre.png", "-frames:v", "1", "-filter_complex", "overlay", "-q:v", "2", f"{D}/final/villa-beach-{s}-miniature.jpg"])
print(s, "ok", dur)
