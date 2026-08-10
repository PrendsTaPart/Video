#!/usr/bin/env python3
"""Dessine les coques d'appareil dans lesquelles s'incruste le screencast.

Deux variantes, choisies selon ce que montre le tutoriel :
  tablette.png        — écran seul, pour les tutoriels de gestion
  tablette-caisse.png — tablette posée sur un tiroir-caisse, pour la caisse POS

Dessiné, pas généré : une coque vectorielle a une géométrie d'écran exacte, donc
le screencast s'y incruste au pixel près. Un mockup produit par un modèle d'image
a une perspective et des proportions qui changent d'une image à l'autre, ce qui
obligerait à recalculer une homographie par épisode — pour un rendu moins net.
"""
import pathlib
from PIL import Image, ImageDraw

ROOT = pathlib.Path(__file__).resolve().parent.parent
SORTIE = ROOT / "templates"

# Le screencast est un 1920x828. L'écran garde ce ratio exact.
ECRAN_W, ECRAN_H = 960, 414
BORD = 26          # épaisseur de coque autour de l'écran
RAYON = 26
COQUE = (26, 32, 44, 255)
REFLET = (255, 255, 255, 26)
TIROIR = (38, 46, 60, 255)
TIROIR_FACE = (52, 62, 78, 255)
METAL = (150, 162, 178, 255)


def coque(largeur, hauteur, marge_bas=0):
    """Toile transparente + coque arrondie ; renvoie l'image et le rect écran."""
    img = Image.new("RGBA", (largeur, hauteur + marge_bas), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    d.rounded_rectangle([0, 0, largeur - 1, hauteur - 1], RAYON, fill=COQUE)
    # liseré clair en haut : ce qui fait lire « verre » plutôt que « rectangle »
    d.rounded_rectangle([1, 1, largeur - 2, hauteur - 2], RAYON - 1, outline=REFLET, width=2)
    # l'écran est un trou : le screencast passe dessous, la coque par-dessus
    ecran = (BORD, BORD, BORD + ECRAN_W, BORD + ECRAN_H)
    d.rectangle(ecran, fill=(0, 0, 0, 0))
    return img, ecran


def tablette():
    img, ecran = coque(ECRAN_W + BORD * 2, ECRAN_H + BORD * 2)
    d = ImageDraw.Draw(img)
    cx = img.width // 2
    d.ellipse([cx - 4, BORD // 2 - 4, cx + 4, BORD // 2 + 4], fill=(70, 80, 96, 255))
    return img, ecran


def tablette_caisse():
    """La même tablette, posée sur un tiroir-caisse vu de trois quarts face."""
    larg = ECRAN_W + BORD * 2
    haut = ECRAN_H + BORD * 2
    tiroir_h = 132
    img, ecran = coque(larg, haut, marge_bas=tiroir_h)
    d = ImageDraw.Draw(img)

    cx = larg // 2
    d.ellipse([cx - 4, BORD // 2 - 4, cx + 4, BORD // 2 + 4], fill=(70, 80, 96, 255))

    # pied qui relie la tablette au tiroir
    d.rectangle([cx - 46, haut - 8, cx + 46, haut + 26], fill=(46, 55, 70, 255))

    # corps du tiroir, plus large que la tablette
    y0 = haut + 22
    d.rounded_rectangle([-30, y0, larg + 29, y0 + tiroir_h - 24], 10, fill=TIROIR)
    # face avant, séparée par une arête claire
    d.rectangle([-30, y0 + 40, larg + 29, y0 + 44], fill=(70, 82, 100, 255))
    d.rounded_rectangle([-24, y0 + 52, larg + 23, y0 + tiroir_h - 34], 6, fill=TIROIR_FACE)
    # poignée
    d.rounded_rectangle([cx - 108, y0 + 74, cx + 108, y0 + 88], 7, fill=METAL)
    return img, ecran


for nom, fabrique in (("tablette", tablette), ("tablette-caisse", tablette_caisse)):
    img, ecran = fabrique()
    chemin = SORTIE / f"{nom}.png"
    img.save(chemin)
    print(f"{chemin.name}  {img.width}x{img.height}  écran {ecran[0]},{ecran[1]} "
          f"{ecran[2]-ecran[0]}x{ecran[3]-ecran[1]}")
