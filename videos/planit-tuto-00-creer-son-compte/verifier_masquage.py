#!/usr/bin/env python3
"""Contrôle qu'aucune adresse n'a survécu dans le montage final.

Le masquage travaille sur la capture source ; ce script vérifie le résultat,
c'est-à-dire le fichier qui sera publié. Il y cherche le motif de l'adresse à
toutes les échelles plausibles — le screencast est agrandi puis animé dans le
cadre 1080 × 1920, et les transitions le réduisent — et signale chaque image où
il le retrouve.

    python3 verifier_masquage.py
"""

import sys
from pathlib import Path

import cv2
import numpy as np

RACINE = Path(__file__).resolve().parent
ORIGINAL = RACINE / "assets" / "screencast-original.mp4"
MONTAGE = RACINE / "out" / "tuto-00-creer-son-compte.mp4"

SEUIL = 0.70
GABARITS = [("inscription", 25.0, (60, 385, 350, 45)),
            ("verification", 37.0, (30, 270, 360, 48))]
# Le screencast est agrandi d'environ 1,83 pour remplir la largeur du cadre ;
# les entrées et sorties de plan le font passer sous et au-dessus de ce facteur.
ECHELLES = (2.10, 1.95, 1.83, 1.70, 1.55, 1.35, 1.15, 1.00, 0.85)


def motif(cap, seconde, zone, sombre=150):
    cap.set(cv2.CAP_PROP_POS_MSEC, seconde * 1000)
    ok, frame = cap.read()
    if not ok:
        sys.exit(f"lecture impossible à {seconde} s")
    x, y, w, h = zone
    gris = cv2.cvtColor(frame[y:y + h, x:x + w], cv2.COLOR_BGR2GRAY)
    ys, xs = np.where(gris < sombre)
    return gris[ys.min():ys.max() + 1, xs.min():xs.max() + 1]


source = cv2.VideoCapture(str(ORIGINAL))
gabarits = []
for nom, seconde, zone in GABARITS:
    plein = motif(source, seconde, zone)
    for e in ECHELLES:
        gabarits.append((f"{nom} ×{e}", cv2.resize(
            plein, None, fx=e, fy=e, interpolation=cv2.INTER_CUBIC)))
source.release()

cap = cv2.VideoCapture(str(MONTAGE))
fps = cap.get(cv2.CAP_PROP_FPS)
alertes, n = [], 0
while True:
    ok, frame = cap.read()
    if not ok:
        break
    gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    for nom, g in gabarits:
        if g.shape[0] > gris.shape[0] or g.shape[1] > gris.shape[1]:
            continue
        _, meilleur, _, pos = cv2.minMaxLoc(
            cv2.matchTemplate(gris, g, cv2.TM_CCOEFF_NORMED))
        if meilleur >= SEUIL:
            alertes.append((n / fps, nom, round(meilleur, 3), pos))
    n += 1
cap.release()

print(f"{n} images analysées, {len(gabarits)} gabarits")
if alertes:
    print(f"⚠ {len(alertes)} correspondance(s) :")
    for t, nom, score, pos in alertes[:40]:
        print(f"   {t:6.2f} s  {nom:18} score {score}  en {pos}")
    sys.exit(1)
print("✓ aucune adresse retrouvée dans le montage")
