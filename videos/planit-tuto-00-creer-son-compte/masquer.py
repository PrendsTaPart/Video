#!/usr/bin/env python3
"""Masque les adresses e-mail de la capture du tutoriel 00.

YouTube a refusé la première version de l'épisode : la capture laisse voir des
adresses e-mail. Deux sources, de gravité inégale :

* l'adresse du compte de démonstration, saisie puis rappelée sur plusieurs
  écrans — le formulaire d'inscription, l'écran « Vérifier le code », le
  formulaire de reconnexion ;
* **la barre de suggestions du clavier**, qui expose trois adresses réelles de
  tiers tirées de l'historique du téléphone. C'est la vraie fuite.

Des boîtes réglées à la main ne tiennent pas : la page défile en continu pendant
la saisie, et chaque écran revient plus tard à une position différente. Le
masquage est donc **détecté image par image** — on cherche le motif de
l'adresse (trois gabarits, un par écran) et le chevron de la barre de
suggestions, et on floute ce qui est trouvé, là où c'est trouvé.

    python3 masquer.py        # écrit assets/screencast.mp4 depuis l'original
"""

import shutil
import subprocess
import sys
from pathlib import Path

import cv2
import numpy as np

RACINE = Path(__file__).resolve().parent
ORIGINAL = RACINE / "assets" / "screencast-original.mp4"
CIBLE = RACINE / "assets" / "screencast.mp4"
BRUT = RACINE / ".masque-brut.mp4"

SEUIL = 0.72          # score de corrélation retenu comme une occurrence
MARGE = 10            # débord du flou autour du motif trouvé, en pixels

# Gabarits : (nom, instant de prélèvement, zone de recherche grossière).
# La zone est recadrée automatiquement sur les pixels sombres qu'elle contient,
# ce qui évite de régler le cadrage au pixel près.
GABARITS = [
    ("inscription", 25.0, (60, 385, 350, 45)),
    ("verification", 37.0, (30, 270, 360, 48)),
]

# La recherche est bornée à la bande où l'adresse peut apparaître : le champ du
# formulaire descend jusqu'à y ≈ 650 quand la page défile, le paragraphe de
# « Vérifier le code » monte jusqu'à y ≈ 270. Chercher hors de cette bande
# coûterait dix fois le temps de calcul sans rien trouver de plus. Le gabarit de
# l'inscription reconnaît aussi l'adresse du formulaire de reconnexion : même
# police, même corps, même champ.
ZONE = (20, 240, 560, 480)      # x, y, largeur, hauteur

# Pendant les bascules multitâche, l'application est rendue en réduction : le
# gabarit à taille réelle ne la reconnaît plus, alors que l'adresse y reste
# lisible. Chaque gabarit est donc essayé à plusieurs échelles.
ECHELLES = (1.0, 0.85, 0.70, 0.58, 0.48)

# La barre de suggestions du clavier ne se reconnaît pas au motif : les adresses
# qu'elle propose changent d'une fois à l'autre, et son chevron est trop petit
# pour servir de repère — un carré de 14 × 8 px se retrouve partout. Elle est
# donc traitée par ses deux fenêtres d'apparition, relevées à l'image :
# la saisie de l'inscription, puis celle de la reconnexion.
BANDE = (28, 745, 562, 58)
FENETRES_CLAVIER = [(11.0, 16.0), (60.0, 65.5)]


def image_a(cap, seconde: float) -> np.ndarray:
    cap.set(cv2.CAP_PROP_POS_MSEC, seconde * 1000)
    ok, frame = cap.read()
    if not ok:
        sys.exit(f"lecture impossible à {seconde} s")
    return frame


def motif(frame: np.ndarray, zone, sombre: int = 150) -> np.ndarray:
    """Recadre la zone sur les pixels sombres qu'elle contient, en gris."""
    x, y, w, h = zone
    gris = cv2.cvtColor(frame[y:y + h, x:x + w], cv2.COLOR_BGR2GRAY)
    ys, xs = np.where(gris < sombre)
    if len(xs) == 0:
        sys.exit(f"aucun texte trouvé dans la zone {zone}")
    return gris[ys.min():ys.max() + 1, xs.min():xs.max() + 1]


def flouter(frame: np.ndarray, x: int, y: int, w: int, h: int) -> None:
    x0, y0 = max(0, x - MARGE), max(0, y - MARGE)
    x1, y1 = min(frame.shape[1], x + w + MARGE), min(frame.shape[0], y + h + MARGE)
    zone = frame[y0:y1, x0:x1]
    if zone.size:
        frame[y0:y1, x0:x1] = cv2.GaussianBlur(zone, (0, 0), sigmaX=12, sigmaY=12)


def main() -> None:
    if not ORIGINAL.exists():
        shutil.copy2(CIBLE, ORIGINAL)
        print(f"original conservé — {ORIGINAL.name}")

    cap = cv2.VideoCapture(str(ORIGINAL))
    gabarits = []
    for nom, seconde, zone in GABARITS:
        plein = motif(image_a(cap, seconde), zone)
        print(f"  gabarit {nom:13} {plein.shape[1]} × {plein.shape[0]} px")
        for e in ECHELLES:
            reduit = plein if e == 1.0 else cv2.resize(
                plein, None, fx=e, fy=e, interpolation=cv2.INTER_AREA)
            gabarits.append((f"{nom} ×{e}", reduit))

    cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
    fps = cap.get(cv2.CAP_PROP_FPS)
    largeur = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    hauteur = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    sortie = cv2.VideoWriter(str(BRUT), cv2.VideoWriter_fourcc(*"mp4v"),
                             fps, (largeur, hauteur))

    compte = {nom: 0 for nom, _ in gabarits}
    compte["clavier"] = 0
    n = 0
    while True:
        ok, frame = cap.read()
        if not ok:
            break
        n += 1
        zx, zy, zw, zh = ZONE
        gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        bande = gris[zy:zy + zh, zx:zx + zw]
        for nom, g in gabarits:
            # Le gabarit à taille réelle ne peut apparaître que dans la bande
            # utile ; les versions réduites, elles, se promènent sur tout
            # l'écran pendant les transitions.
            vue, dx, dy = ((bande, zx, zy) if nom.endswith("×1.0")
                           else (gris, 0, 0))
            if g.shape[0] > vue.shape[0] or g.shape[1] > vue.shape[1]:
                continue
            score = cv2.matchTemplate(vue, g, cv2.TM_CCOEFF_NORMED)
            _, meilleur, _, position = cv2.minMaxLoc(score)
            if meilleur >= SEUIL:
                flouter(frame, dx + position[0], dy + position[1],
                        g.shape[1], g.shape[0])
                compte[nom] += 1
        seconde = (n - 1) / fps
        if any(t0 <= seconde <= t1 for t0, t1 in FENETRES_CLAVIER):
            flouter(frame, *BANDE)
            compte["clavier"] += 1
        sortie.write(frame)
    cap.release()
    sortie.release()

    print(f"  {n} images ; occurrences floutées : "
          + ", ".join(f"{k} {v}" for k, v in compte.items()))

    subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", str(BRUT),
                    "-c:v", "libx264", "-preset", "slow", "-crf", "17",
                    "-pix_fmt", "yuv420p", str(CIBLE)], check=True)
    BRUT.unlink()
    print(f"masqué — {CIBLE.name} ({CIBLE.stat().st_size} o)")


if __name__ == "__main__":
    main()
