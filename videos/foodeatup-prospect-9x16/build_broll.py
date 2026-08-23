#!/usr/bin/env python3
"""B-roll vertical (S1 et S7) à partir des plans 16:9 déjà présents dans le dépôt.

Les plans Higgsfield existants sont en 1280x720 : ils sont recadrés en bandeau
central sur un fond flouté, en attendant les plans verticaux natifs
(cf. PROMPTS-HIGGSFIELD.md). Pas de zoompan sur de la vidéo — ça gèle l'image.
"""
import os, sys, subprocess
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib_draw import *
from PIL import ImageDraw

ROOT = os.path.dirname(os.path.abspath(__file__))
WORK = f"{ROOT}/work"; os.makedirs(WORK, exist_ok=True)
SRC = "/home/user/Video/hero-video/assets/video"
VENC = ["-c:v", "libx264", "-preset", "medium", "-crf", "18", "-pix_fmt", "yuv420p", "-r", str(FPS)]

# plan source, début, durée, teinte (froide pour le chaos, neutre pour la fin)
S1_PLANS = [("hero-serveur-trois-tablettes.mp4", 0.4, 3.5, True),
            ("hero-directeur-sept-onglets.mp4", 1.0, 3.5, True),
            ("hero-chef-carnet-dlc.mp4", 0.5, 3.5, True),
            ("hero-kds-mural.mp4", 0.6, 3.5, True)]
S7_PLANS = [("hero-serveur-place-client.mp4", 0.5, 5.0, False)]

def vfill(src, ss, dur, cold, out):
    """1080x1920 : fond flouté + bandeau central net."""
    grade = "eq=saturation=0.62:contrast=1.06:brightness=-0.03" if cold else "eq=saturation=1.05:contrast=1.02"
    fc = ("[0:v]split=2[a][b];"
          "[a]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,"
          "gblur=sigma=34,eq=brightness=-0.12:saturation=0.55[bg];"
          f"[b]scale=-2:912,crop=1080:912,{grade}[fg];"
          "[bg][fg]overlay=(W-w)/2:(H-h)/2,format=yuv420p[v]")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", str(ss), "-t", str(dur), "-i", f"{SRC}/{src}",
                    "-filter_complex", fc, "-map", "[v]", *VENC, out], check=True)

def overlay_png(base, png, out, t0, t1):
    """Incruste un PNG RGBA avec fondu."""
    fc = (f"[1:v]format=rgba,fade=in:st={t0}:d=0.4:alpha=1,fade=out:st={t1-0.4}:d=0.4:alpha=1[ov];"
          f"[0:v][ov]overlay=0:0:enable='between(t,{t0},{t1})',format=yuv420p[v]")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", base, "-loop", "1", "-i", png,
                    "-filter_complex", fc, "-map", "[v]", "-t", "3.5", *VENC, out], check=True)

def postit_png(path):
    """Post-it « TOMATES — PÉREMPTION J-3 » posé en bas de cadre."""
    im = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    x0, y0, w_, h_ = 150, 120, 780, 300
    d.polygon([(x0, y0), (x0 + w_, y0 - 18), (x0 + w_ + 10, y0 + h_ - 20), (x0 - 6, y0 + h_)], fill=(255, 226, 120, 255))
    d.text((x0 + 54, y0 + 56), "TOMATES", font=F("800", 66), fill=(60, 48, 10))
    d.text((x0 + 54, y0 + 140), "PÉREMPTION", font=F("700", 48), fill=(90, 72, 16))
    d.text((x0 + 54, y0 + 202), "J - 3", font=F("800", 62), fill=(196, 84, 20))
    im.save(path)

def pills_png(path):
    """Pastilles de notification qui s'empilent (chaos multicanal)."""
    im = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    items = [("12 appels manqués", 96, RED), ("8 commandes en attente", 206, ORANGE),
             ("3 ruptures de stock", 316, RED), ("Dernier post : il y a 15 jours", 426, (90, 100, 112))]
    for lab, y, col in items:
        f = F("700", 42)
        tw = d.textlength(lab, font=f); w_ = int(tw + 120)
        d.rounded_rectangle((90, y, 90 + w_, y + 84), 42, fill=(255, 255, 255, 240))
        d.ellipse((122, y + 28, 150, y + 56), fill=col)
        d.text((176, y + 18), lab, font=f, fill=INK)
    im.save(path)

def concat(parts, out):
    lst = f"{WORK}/concat_{os.path.basename(out)}.txt"
    with open(lst, "w") as fh:
        for p in parts: fh.write(f"file '{p}'\n")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", lst,
                    "-c", "copy", out], check=True)

if __name__ == "__main__":
    postit_png(f"{WORK}/ov-postit.png"); pills_png(f"{WORK}/ov-pills.png")
    parts = []
    for i, (src, ss, dur, cold) in enumerate(S1_PLANS):
        raw = f"{WORK}/s1-{i}.mp4"; vfill(src, ss, dur, cold, raw)
        if i == 0:
            fin = f"{WORK}/s1-{i}-ov.mp4"; overlay_png(raw, f"{WORK}/ov-pills.png", fin, 0.8, 3.5)
        elif i == 2:
            fin = f"{WORK}/s1-{i}-ov.mp4"; overlay_png(raw, f"{WORK}/ov-postit.png", fin, 0.6, 3.5)
        else:
            fin = raw
        parts.append(fin); print("ok", fin)
    concat(parts, f"{WORK}/seq-s1.mp4")
    for i, (src, ss, dur, cold) in enumerate(S7_PLANS):
        out = f"{WORK}/seq-s7a.mp4"; vfill(src, ss, dur, cold, out); print("ok", out)
    print("b-roll terminé")
