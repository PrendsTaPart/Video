#!/usr/bin/env python3
"""Découpe + recadrage RGPD des rushes PrediBot. Extraits muets, crop WA ou BR + delogo."""
import os, subprocess
os.chdir(os.path.dirname(os.path.abspath(__file__)))
os.makedirs("extraits", exist_ok=True)
FPS = 30
WA = "crop=1514:984:392:44,delogo=x=1058:y=890:w=430:h=70"
BR = "crop=1904:930:8:100,delogo=x=1440:y=830:w=440:h=70"
VENC = ["-c:v", "libx264", "-preset", "medium", "-crf", "20", "-pix_fmt", "yuv420p", "-r", str(FPS), "-an"]

# id, source, start, end, crop
SEGS = [
    ("e08a", "config", 3.0, 14.0, WA),
    ("e08b", "config", 18.5, 22.5, BR),
    ("e08c", "config", 60.0, 74.0, WA),
    ("e08d", "config", 77.3, 79.8, BR),
    ("e09",  "haccp", 2.0, 9.0, WA),
    ("e10",  "haccp", 10.3, 15.0, BR),
    ("e11a", "fournisseur", 6.0, 20.0, WA),
    ("e11b", "fournisseur", 22.0, 26.0, BR),
    ("e12",  "rh", 8.0, 34.0, WA),
    ("e13",  "stock", 0.0, 12.0, WA),
    ("e14",  "stock", 44.0, 52.0, BR),
    ("e15a", "production", 64.0, 96.0, WA),
    ("e15b", "production", 104.0, 112.5, BR),
]

def dur(f):
    return float(subprocess.check_output(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",f]).strip())

for sid, src, a, b, crop in SEGS:
    out = f"extraits/{sid}.mp4"
    cmd = ["ffmpeg","-y","-ss",f"{a:.2f}","-to",f"{b:.2f}","-i",f"rushes/{src}.mp4",
           "-vf",f"{crop},setsar=1"] + VENC + [out]
    r = subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)
    if r.returncode != 0:
        print("ERR", sid, r.stderr.decode()[-600:]); raise SystemExit(1)
    print("ok", sid, f"{src} {a}-{b}", round(dur(out),2), "s")
print("DONE extracts")
