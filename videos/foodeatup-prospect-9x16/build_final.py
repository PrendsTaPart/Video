#!/usr/bin/env python3
"""Assemblage final : séquences + sous-titres incrustés + musique.

Animatique v0 : la voix off n'est PAS encore générée (script à valider, cf.
FOODEATUP-TUTORIELS-WORKFLOW.md étape 3). Le minutage des sous-titres est
calculé à partir du débit estimé de la voix (2,6 mots/s) ; il sera recalé sur
les vraies durées ElevenLabs dès validation.
"""
import os, sys, json, subprocess, shutil
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib_draw import FPS, FONTS

ROOT = os.path.dirname(os.path.abspath(__file__))
WORK, OUT = f"{ROOT}/work", f"{ROOT}/out"
os.makedirs(OUT, exist_ok=True)
BGM = "/home/user/Video/videos/stories-foodeatup-30j/audio/bgm.mp3"
WPS = 2.6          # mots par seconde (débit voix off estimé)
LEAD = 0.5         # silence en début de scène avant la 1re ligne
GAP = 0.28         # respiration entre deux lignes

# ordre de montage : (fichier séquence, id de scène du script ou None)
TIMELINE = [("seq-s1.mp4", "S1"), ("seq-s2.mp4", "S2"), ("seq-s3.mp4", "S3"),
            ("seq-s4.mp4", "S4"), ("seq-s5.mp4", "S5"), ("seq-s6.mp4", "S6"),
            ("seq-s7a.mp4", None), ("seq-s7.mp4", "S7")]

def dur(f):
    return float(subprocess.check_output(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", f]).strip())

def concat(parts, out):
    lst = f"{WORK}/_timeline.txt"
    with open(lst, "w") as fh:
        for p in parts: fh.write(f"file '{p}'\n")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", lst,
                    "-c", "copy", out], check=True)
    return out

def cues():
    """Calcule (début, fin, texte) de chaque bloc de sous-titre sur la timeline."""
    script = json.load(open(f"{ROOT}/script/script.json"))
    scenes = {s["id"]: s for s in script["scenes"]}
    out, t0 = [], 0.0
    for fname, sid in TIMELINE:
        d = dur(f"{WORK}/{fname}")
        if sid and sid != "S7":
            sc = scenes[sid]
            blocks = [(b, len(b.split())) for line in sc["vo"] for b in line["sub"]]
            words = sum(w for _, w in blocks)
            speech = words / WPS + GAP * (len(blocks) - 1)
            avail = d - LEAD - 0.4
            scale = min(1.0, avail / speech) if speech > 0 else 1.0
            t = t0 + LEAD
            for b, w in blocks:
                bd = (w / WPS) * scale
                out.append((t, t + bd, b))
                t += bd + GAP * scale
        t0 += d
    return out, t0

def caption_filter(cs):
    """Chaîne de drawtext : texte blanc gras, contour noir épais, bas de cadre."""
    tdir = f"{WORK}/cues"; shutil.rmtree(tdir, ignore_errors=True); os.makedirs(tdir)
    parts = []
    for i, (a, b, txt) in enumerate(cs):
        fp = f"{tdir}/c{i:03d}.txt"
        open(fp, "w").write(txt)
        parts.append(
            f"drawtext=fontfile='{FONTS}/Poppins-800.ttf':textfile='{fp}':"
            f"fontsize=64:fontcolor=white:borderw=12:bordercolor=black@0.9:"
            f"x=(w-text_w)/2:y=h-236:enable='between(t,{a:.2f},{b:.2f})'")
    return ",".join(parts)

if __name__ == "__main__":
    parts = [f"{WORK}/{f}" for f, _ in TIMELINE]
    silent = concat(parts, f"{WORK}/_silent.mp4")
    cs, total = cues()
    print(f"timeline : {total:.1f}s · {len(cs)} blocs de sous-titres")
    vf = caption_filter(cs)
    out = f"{OUT}/foodeatup-prospect-9x16-animatique-v0.mp4"
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", silent, "-stream_loop", "-1", "-i", BGM,
                    "-filter_complex",
                    f"[0:v]{vf}[v];"
                    f"[1:a]volume=0.32,afade=in:st=0:d=1.2,afade=out:st={total-2.2:.2f}:d=2.0,"
                    f"atrim=0:{total:.2f},asetpts=N/SR/TB[a]",
                    "-map", "[v]", "-map", "[a]",
                    "-c:v", "libx264", "-preset", "medium", "-crf", "19", "-pix_fmt", "yuv420p",
                    "-c:a", "aac", "-b:a", "160k", "-shortest", out], check=True)
    print("->", out, f"{dur(out):.1f}s")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", "31", "-i", out, "-frames:v", "1",
                    "-q:v", "3", f"{OUT}/poster.jpg"], check=True)
