#!/usr/bin/env python3
"""Cherche l'adresse du compte de démonstration dans le montage fini.

Les gabarits sont découpés dans la capture source, aux instants où l'adresse
est lisible ; on les cherche ensuite sur chaque image du rendu, à plusieurs
échelles, le montage réduisant la capture. Le verdict ne vaut que si le
décodage a été complet : on compare le nombre d'images lues à la durée.
"""
import subprocess
import sys
from pathlib import Path

import cv2
import numpy as np

RACINE = Path(__file__).resolve().parent
SOURCE = RACINE / "assets" / "screencast.mp4"
MONTAGE = RACINE / "out" / "tuto-08-transformer-une-carte-en-routine.mp4"
# Un argument permet de viser un autre fichier — sert au témoin positif, qui
# passe un extrait fabriqué depuis une plage où l'adresse est bien à l'image :
# un vérificateur qui ne la trouve pas là ne prouve rien ailleurs.
if len(sys.argv) > 1:
    MONTAGE = Path(sys.argv[1])
SEUIL = 0.72

# academie.py recadre la capture en 392 × 824 puis l'étire à 1860 px de haut :
# le montage AGRANDIT la source de 1860 / 824. Les gabarits doivent donc être
# agrandis d'autant, pas réduits ; on garde ±3 % de jeu pour le rééchantillonnage.
ECHELLE = 1860 / 824
ECHELLES = (ECHELLE * 0.97, ECHELLE, ECHELLE * 1.03)

# Recherche en deux temps. À demi-résolution le texte fin devient une bouillie
# qui ressemble à n'importe quel champ rempli : un premier balayage à ce niveau
# ne sert qu'à désigner des candidats, avec un seuil bas. Chaque candidat est
# ensuite recoupé en pleine résolution, à l'endroit exact désigné, où seule la
# vraie chaîne de glyphes tient le seuil.
REDUCTION = 0.5
SEUIL_GROSSIER = 0.70
MARGE = 12

# instant de la capture, puis (x, y, largeur, hauteur) de la zone à découper.
# Zones relevées à la règle sur des images extraites par ffmpeg : cv2 ne se
# positionne pas sur la même image pour un même instant, et une zone relevée
# sur l'une puis découpée sur l'autre donne un gabarit qui n'est pas l'adresse
# — le premier essai cherchait ainsi le libellé « PROMPT CONTENT », qu'il
# retrouvait à 0,95 sur des écrans parfaitement propres.
GABARITS = [
    ("adresse-apercu-tache", 107.0, (36, 344, 224, 26)),
    ("adresse-champ-destinataire", 116.0, (36, 460, 224, 28)),
]

# Un motif trop petit finit par ressembler à n'importe quel bloc de texte : le
# gabarit de 344 × 30 découpé au jugé sur le clavier avait ainsi « trouvé »
# l'adresse sur 1 576 images d'un montage de 1 494. On refuse en dessous.
LARGEUR_MINIMALE = 120
HAUTEUR_MINIMALE = 10


def image_source(instant: float) -> np.ndarray:
    """Extrait une image de la capture par ffmpeg, en niveaux de gris."""
    brut = subprocess.run(
        ["ffmpeg", "-v", "error", "-ss", f"{instant}", "-i", str(SOURCE),
         "-frames:v", "1", "-f", "image2pipe", "-vcodec", "png", "-"],
        capture_output=True, check=True).stdout
    image = cv2.imdecode(np.frombuffer(brut, np.uint8), cv2.IMREAD_GRAYSCALE)
    if image is None:
        sys.exit(f"capture illisible à {instant} s")
    return image


def motif(instant: float, zone: tuple[int, int, int, int]) -> np.ndarray:
    """Découpe la zone puis la resserre sur ses pixels sombres."""
    image = image_source(instant)
    x, y, largeur, hauteur = zone
    bloc = image[y:y + hauteur, x:x + largeur]
    sombres = np.argwhere(bloc < 140)
    if sombres.size == 0:
        sys.exit(f"aucun texte dans la zone à {instant} s")
    (y0, x0), (y1, x1) = sombres.min(0), sombres.max(0)
    motif = bloc[y0:y1 + 1, x0:x1 + 1]
    h, l = motif.shape
    if l < LARGEUR_MINIMALE or h < HAUTEUR_MINIMALE:
        sys.exit(f"gabarit dégénéré à {instant} s : {l} × {h} px")
    return motif


def auto_controle(motifs) -> None:
    """Chaque gabarit doit se retrouver dans l'image d'où il vient."""
    for (nom, m), (_, instant, _) in zip(motifs, GABARITS):
        gris = image_source(instant)
        score = cv2.matchTemplate(gris, m, cv2.TM_CCOEFF_NORMED).max()
        print(f"  {nom} — {m.shape[1]} × {m.shape[0]} px, "
              f"retrouvé chez lui à {score:.3f}")
        if score < 0.95:
            sys.exit(f"gabarit {nom} introuvable dans sa propre image")


def main() -> int:
    motifs = [(nom, motif(t, z)) for nom, t, z in GABARITS]
    auto_controle(motifs)
    duree = float(subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "default=nw=1:nk=1", str(MONTAGE)],
        capture_output=True, text=True, check=True).stdout)
    attendu = int(duree * 30)

    cap = cv2.VideoCapture(str(MONTAGE))
    lues = 0
    touches = []
    while True:
        ok, image = cap.read()
        if not ok:
            break
        lues += 1
        plein = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        reduit = cv2.resize(plein, None, fx=REDUCTION, fy=REDUCTION)
        for nom, m in motifs:
            for e in ECHELLES:
                petit = cv2.resize(m, None, fx=e * REDUCTION, fy=e * REDUCTION)
                if (petit.shape[0] > reduit.shape[0]
                        or petit.shape[1] > reduit.shape[1]):
                    continue
                carte = cv2.matchTemplate(reduit, petit, cv2.TM_CCOEFF_NORMED)
                if carte.max() < SEUIL_GROSSIER:
                    continue
                grand = cv2.resize(m, None, fx=e, fy=e)
                gh, gl = grand.shape
                _, _, _, (cx, cy) = cv2.minMaxLoc(carte)
                x = int(cx / REDUCTION)
                y = int(cy / REDUCTION)
                fen = plein[max(y - MARGE, 0):y + gh + MARGE,
                            max(x - MARGE, 0):x + gl + MARGE]
                if fen.shape[0] < gh or fen.shape[1] < gl:
                    continue
                score = cv2.matchTemplate(fen, grand,
                                          cv2.TM_CCOEFF_NORMED).max()
                if score >= SEUIL:
                    touches.append((lues / 30, nom, e, score))
                    break
    cap.release()

    combinaisons = len(motifs) * len(ECHELLES)
    print(f"{lues} images lues sur {attendu} attendues, {combinaisons} gabarits")
    if lues < attendu * 0.98:
        print("décodage incomplet — verdict sans valeur", file=sys.stderr)
        return 2
    if touches:
        for t, nom, e, score in touches:
            print(f"  {t:6.2f} s  {nom}  ×{e}  {score:.3f}")
        return 1
    print("✓ aucune adresse retrouvée dans le montage")
    return 0


if __name__ == "__main__":
    sys.exit(main())
