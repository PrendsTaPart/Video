#!/usr/bin/env python3
"""Assemblage final : séquences + voix off + sous-titres incrustés + musique.

Deux modes, choisis automatiquement :

* `vo/vo_meta.json` présent  -> montage complet. Le minutage des sous-titres est
  calé sur la durée RÉELLE de chaque ligne, la musique passe sous la voix.
* absent                     -> animatique muette (musique + sous-titres estimés
  à 2,6 mots/s), pour valider la structure avant d'engager la voix.
"""
import os, sys, json, subprocess, shutil
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib_draw import FPS, FONTS

ROOT = os.path.dirname(os.path.abspath(__file__))
WORK, OUT, VO = f"{ROOT}/work", f"{ROOT}/out", f"{ROOT}/vo"
os.makedirs(OUT, exist_ok=True)
BGM = "/home/user/Video/videos/stories-foodeatup-30j/audio/bgm.mp3"
WPS = 2.6          # débit estimé, utilisé seulement en mode animatique
LEAD = 0.5         # silence en début de scène avant la 1re ligne
GAP = 0.28         # respiration entre deux lignes

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

def scene_starts():
    """Instant de départ de chaque séquence sur la timeline finale."""
    t, starts = 0.0, {}
    for fname, sid in TIMELINE:
        starts[fname] = t
        t += dur(f"{WORK}/{fname}")
    return starts, t

def split_line(t0, d, subs):
    """Répartit la durée d'une ligne entre ses blocs de sous-titres, au mot."""
    counts = [len(s.split()) for s in subs]
    total = sum(counts) or 1
    out, t = [], t0
    for s, c in zip(subs, counts):
        bd = d * c / total
        out.append((t, t + bd, s))
        t += bd
    return out

def plan(vo_meta):
    """Retourne (cues, placements VO, durée totale).

    placements : [(fichier mp3, instant de départ)] — vide en mode animatique.
    """
    script = json.load(open(f"{ROOT}/script/script.json"))
    scenes = {s["id"]: s for s in script["scenes"]}
    starts, total = scene_starts()
    cues, placements, overflow = [], [], []
    for fname, sid in TIMELINE:
        if not sid or sid == "S7" and not vo_meta:
            continue
        t0, d = starts[fname], dur(f"{WORK}/{fname}")
        sc = scenes[sid]
        if vo_meta:
            t = t0 + LEAD
            for line in sc["vo"]:
                m = vo_meta["lines"][line["id"]]
                placements.append((f"{VO}/{line['id']}.mp3", t))
                if sid != "S7":                      # la carte CTA porte déjà son texte
                    cues += split_line(t, m["duration"], line["sub"])
                t += m["duration"] + GAP
            if t - GAP > t0 + d:
                overflow.append((sid, round(t - GAP - (t0 + d), 2)))
        else:
            blocks = [(b, len(b.split())) for line in sc["vo"] for b in line["sub"]]
            words = sum(w for _, w in blocks)
            speech = words / WPS + GAP * (len(blocks) - 1)
            scale = min(1.0, (d - LEAD - 0.4) / speech) if speech else 1.0
            t = t0 + LEAD
            for b, w in blocks:
                bd = (w / WPS) * scale
                cues.append((t, t + bd, b))
                t += bd + GAP * scale
    if overflow:
        for sid, ex in overflow:
            print(f"  ⚠ {sid} : la voix dépasse de {ex}s — rallonger la séquence ou resserrer le texte")
    return cues, placements, total

def caption_filter(cs):
    """Sous-titres incrustés : blanc gras, contour noir épais, bas de cadre."""
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

def audio_args(placements, total):
    """Musique + lignes de voix off décalées ; limiteur en garde-fou."""
    if not placements:
        return (["-stream_loop", "-1", "-i", BGM],
                f"[1:a]volume=0.32,afade=in:st=0:d=1.2,afade=out:st={total-2.2:.2f}:d=2.0,"
                f"atrim=0:{total:.2f},asetpts=N/SR/TB[a]")
    inputs, chains, labels = [], [], []
    for i, (f, t) in enumerate(placements):
        inputs += ["-i", f]
        chains.append(f"[{i+1}:a]adelay={int(t*1000)}|{int(t*1000)}[v{i}]")
        labels.append(f"[v{i}]")
    bi = len(placements) + 1
    inputs += ["-stream_loop", "-1", "-i", BGM]
    # musique nettement sous la voix (convention du dépôt : ~-22 dB)
    chains.append(f"[{bi}:a]volume=0.10,afade=in:st=0:d=1.2,"
                  f"afade=out:st={total-2.2:.2f}:d=2.0,atrim=0:{total:.2f},asetpts=N/SR/TB[bg]")
    chains.append(f"{''.join(labels)}[bg]amix=inputs={len(placements)+1}:normalize=0:"
                  f"dropout_transition=0,alimiter=limit=0.6:level=disabled,"
                  f"atrim=0:{total:.2f},asetpts=N/SR/TB[a]")
    return inputs, ";".join(chains)

if __name__ == "__main__":
    vo_meta = None
    if os.path.exists(f"{VO}/vo_meta.json"):
        vo_meta = json.load(open(f"{VO}/vo_meta.json"))
        print("voix off détectée :", len(vo_meta["lines"]), "lignes")
    else:
        print("pas de voix off (vo/vo_meta.json absent) -> animatique muette")
    silent = concat([f"{WORK}/{f}" for f, _ in TIMELINE], f"{WORK}/_silent.mp4")
    cues, placements, total = plan(vo_meta)
    print(f"timeline : {total:.1f}s · {len(cues)} blocs de sous-titres")
    a_in, a_chain = audio_args(placements, total)
    suffix = "" if vo_meta else "-animatique-v0"
    out = f"{OUT}/foodeatup-prospect-9x16{suffix}.mp4"
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", silent, *a_in,
                    "-filter_complex", f"[0:v]{caption_filter(cues)}[v];{a_chain}",
                    "-map", "[v]", "-map", "[a]",
                    "-c:v", "libx264", "-preset", "medium", "-crf", "19", "-pix_fmt", "yuv420p",
                    "-c:a", "aac", "-b:a", "192k", "-shortest", out], check=True)
    print("->", out, f"{dur(out):.1f}s")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", "31", "-i", out, "-frames:v", "1",
                    "-q:v", "3", f"{OUT}/poster.jpg"], check=True)
    if vo_meta:
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", out, "-af", "astats", "-f", "null",
                        "/dev/null"], check=False)
