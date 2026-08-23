#!/usr/bin/env python3
"""B-roll vertical (S1 et S7).

Depuis le retour de Moody (viser les franchises), S1 et S7 s'appuient sur des
photos verticales de snack / boulangerie / borne générées via RapidoCMS
(`assets/rapidocms/`), animées en Ken Burns. Les plans Higgsfield 16:9 restent
disponibles via `vfill()` pour un montage bistro, mais ne sont plus utilisés.

Ken Burns : zoompan est utilisé ici sur des IMAGES fixes (son usage prévu) —
jamais sur de la vidéo, où il gèle l'image (bug déjà rencontré sur ce dépôt).
"""
import os, sys, shutil, subprocess
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib_draw import *
from PIL import Image, ImageDraw, ImageEnhance

ROOT = os.path.dirname(os.path.abspath(__file__))
WORK = f"{ROOT}/work"; os.makedirs(WORK, exist_ok=True)
SRC = "/home/user/Video/hero-video/assets/video"
VENC = ["-c:v", "libx264", "-preset", "medium", "-crf", "18", "-pix_fmt", "yuv420p", "-r", str(FPS)]

IMG = f"{ROOT}/assets/rapidocms"

# image, durée, sens du zoom, incrustation éventuelle
S1_IMAGES = [("snack-comptoir.jpg", 4.0, "in", "pills"),
             ("snack-tacos-rush.jpg", 4.0, "out", "postit"),
             ("boulangerie-vitrine.jpg", 4.0, "in", None),
             ("borne-commande.jpg", 4.0, "out", None)]
S7_IMAGES = [("equipe-fin-service.jpg", 5.0, "in", None)]

# plans Higgsfield 16:9 conservés pour mémoire (montage bistro), plus utilisés
S1_PLANS_BISTRO = [("hero-serveur-trois-tablettes.mp4", 0.4, 4.0, True),
                   ("hero-directeur-sept-onglets.mp4", 1.0, 4.0, True),
                   ("hero-chef-carnet-dlc.mp4", 0.5, 4.0, True),
                   ("hero-kds-mural.mp4", 0.6, 4.0, True)]

def kenburns(img, dur, sens, out, cold=False):
    """Photo verticale -> plan 1080x1920 animé (léger travelling avant/arrière).

    Rendu image par image avec PIL plutôt qu'avec `zoompan` : sur une image en
    boucle, zoompan émet `d` images POUR CHAQUE image d'entrée (12 000 images
    pour un plan de 4 s), ce qui est à la fois faux et très lent.
    """
    n = int(round(dur * FPS))
    d = f"{WORK}/kb_{os.path.splitext(img)[0]}"
    shutil.rmtree(d, ignore_errors=True); os.makedirs(d)
    src = Image.open(f"{IMG}/{img}").convert("RGB")
    if cold:                       # palette plus froide pour les scènes de rush
        src = ImageEnhance.Color(src).enhance(0.78)
        src = ImageEnhance.Contrast(src).enhance(1.05)
    sw, sh = src.size
    cw = min(sw, int(sh * W / H))  # fenêtre 9:16 la plus large possible
    ch = int(cw * H / W)
    for i in range(n):
        p = i / max(1, n - 1)
        zoom = 1.0 + 0.12 * (p if sens == "in" else 1 - p)
        w_, h_ = int(cw / zoom), int(ch / zoom)
        x, y = (sw - w_) // 2, (sh - h_) // 2
        src.crop((x, y, x + w_, y + h_)).resize((W, H), Image.LANCZOS).save(f"{d}/f{i:05d}.png")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-framerate", str(FPS), "-i", f"{d}/f%05d.png",
                    *VENC, out], check=True)
    shutil.rmtree(d, ignore_errors=True)

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

def overlay_png(base, png, out, t0, t1, hold=4.0):
    """Incruste un PNG RGBA avec fondu."""
    fc = (f"[1:v]format=rgba,fade=in:st={t0}:d=0.4:alpha=1,fade=out:st={t1-0.4}:d=0.4:alpha=1[ov];"
          f"[0:v][ov]overlay=0:0:enable='between(t,{t0},{t1})',format=yuv420p[v]")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", base, "-loop", "1", "-i", png,
                    "-filter_complex", fc, "-map", "[v]", "-t", str(hold), *VENC, out], check=True)

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
    for i, (img, d, sens, ov) in enumerate(S1_IMAGES):
        raw = f"{WORK}/s1-{i}.mp4"
        kenburns(img, d, sens, raw, cold=True)
        if ov:
            fin = f"{WORK}/s1-{i}-ov.mp4"
            overlay_png(raw, f"{WORK}/ov-{ov}.png", fin, 0.7, d, hold=d)
        else:
            fin = raw
        parts.append(fin); print("ok", fin)
    concat(parts, f"{WORK}/seq-s1.mp4")
    for img, d, sens, _ in S7_IMAGES:
        out = f"{WORK}/seq-s7a.mp4"; kenburns(img, d, sens, out); print("ok", out)
    print("b-roll terminé")
