#!/usr/bin/env python3
"""Choisit, dans un segment HeyGen, la frame sur laquelle l'avatar peut attendre.

    python3 scripts/frame-attente.py assets/avatar/EP010.mp4     -> 0.83

`build-episode.sh` fait entrer l'avatar en retard et comble la tête du créneau
par une image fixe. Prendre la première frame venue ne marche pas : sur EP010
elle tombe en plein clignement, et l'avatar attend deux secondes et demie les
yeux fermés. Un visage figé les yeux fermés ne se lit pas comme une attente,
il se lit comme un plantage.

Comment on choisit
------------------
Un œil ouvert, c'est une pupille sombre dans une cornée claire : beaucoup de
contraste sur une bande horizontale étroite. Un œil fermé, c'est une paupière
de la couleur de la peau : presque plus rien. On mesure donc l'écart-type de
la luminance sur la bande des yeux, et on garde la frame où il est le plus
fort.

C'est grossier et c'est suffisant : on ne cherche pas à mesurer une ouverture
palpébrale, seulement à ne pas tomber sur le seul dixième de seconde où l'œil
est clos. Vingt frames candidates dans les deux premières secondes suffisent —
un clignement dure cent à cent cinquante millisecondes, il ne peut pas les
couvrir toutes.

La bande des yeux est déduite du cadrage HeyGen, constant sur les cinquante-
quatre segments : le visage occupe le tiers supérieur, les yeux tombent aux
alentours de 30 % de la hauteur.
"""
import pathlib
import subprocess
import sys
import tempfile

CANDIDATES = 20
FENETRE = 2.0          # on cherche dans les deux premières secondes
BANDE_HAUT, BANDE_BAS = 0.24, 0.38   # la bande des yeux, en fraction de hauteur


def luminance_ecart(png):
    from PIL import Image
    im = Image.open(png).convert("L")
    l, h = im.size
    bande = im.crop((int(l * 0.25), int(h * BANDE_HAUT),
                     int(l * 0.75), int(h * BANDE_BAS)))
    px = list(bande.tobytes())
    moy = sum(px) / len(px)
    return (sum((p - moy) ** 2 for p in px) / len(px)) ** 0.5


def choisir(video, fenetre=FENETRE, candidates=CANDIDATES):
    duree = float(subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "csv=p=0", str(video)], capture_output=True, text=True).stdout)
    fenetre = min(fenetre, max(0.1, duree - 0.05))
    pas = fenetre / candidates
    meilleur, score = 0.0, -1.0
    with tempfile.TemporaryDirectory() as d:
        for i in range(candidates):
            t = i * pas
            png = pathlib.Path(d) / f"{i}.png"
            subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", f"{t:.3f}",
                            "-i", str(video), "-frames:v", "1", "-update", "1",
                            str(png)], check=False)
            if not png.exists():
                continue
            e = luminance_ecart(png)
            if e > score:
                meilleur, score = t, e
    return meilleur


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("usage: frame-attente.py <segment.mp4>")
    print(f"{choisir(pathlib.Path(sys.argv[1])):.3f}")
