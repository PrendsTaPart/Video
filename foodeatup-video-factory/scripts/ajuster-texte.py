#!/usr/bin/env python3
"""Fait tenir une phrase incrustée dans la largeur du cadre.

    python3 scripts/ajuster-texte.py "Personne ne touche à ta dernière frite." 62

Écrit sur la sortie standard : la taille de police retenue, puis le texte
éventuellement replié sur deux ou trois lignes, séparés par un saut de ligne.

Pourquoi ce script existe
-------------------------
`drawtext` ne replie pas et ne rétrécit pas : il dessine la phrase sur une
ligne, à la taille demandée, et ce qui dépasse du cadre est perdu. Sur EP017 —
« Personne ne touche à ta dernière frite. » — le master sorti montrait
« ersonne ne touche à ta dernière frit » : le premier et le dernier mot coupés
net, sur l'accroche, c'est-à-dire sur la seule phrase que le spectateur lit
pendant les trois premières secondes.

Rien ne prévenait : ffmpeg dessine sans se plaindre, et la coupe ne se voit
qu'à l'image. D'où une mesure réelle plutôt qu'un comptage de caractères : on
dessine la phrase, on regarde où s'arrête l'encre, et on décide.
"""
import re
import subprocess
import sys

MARGE = 50          # de chaque côté : le texte ne colle jamais au bord
CADRE = 1080
MAXW = CADRE - 2 * MARGE
# Jusqu'où on rétrécit avant d'ajouter une ligne. Sur une seule ligne on
# s'arrête tôt : une accroche à 42 px sur un téléphone se lit moins bien que la
# même phrase sur deux lignes à 56. Avec deux ou trois lignes, l'œil descend et
# la taille peut baisser davantage.
MIN_PAR_LIGNES = {1: 50, 2: 44, 3: 40}
MIN_POLICE = 40
POLICE = "templates/Poppins-800.ttf"


def largeur(texte, taille):
    """Largeur d'encre réelle, en pixels, mesurée sur un rendu drawtext."""
    # Le texte est passé par un fichier : une apostrophe dans la phrase
    # refermerait le text='…' du filtre au milieu du mot.
    with open("/tmp/_mesure.txt", "w") as f:
        f.write(texte)
    brut = subprocess.run(
        ["ffmpeg", "-v", "error", "-f", "lavfi",
         "-i", f"color=c=black:s={CADRE}x400:d=1",
         "-frames:v", "1",
         "-vf", (f"drawtext=fontfile={POLICE}:textfile=/tmp/_mesure.txt:"
                 f"fontsize={taille}:fontcolor=white:x=(w-text_w)/2:y=100,"
                 "format=gray"),
         "-f", "rawvideo", "-"],
        capture_output=True).stdout
    if not brut:
        return MAXW + 1
    colonnes = [False] * CADRE
    for ligne in range(0, len(brut) - CADRE, CADRE):
        rang = brut[ligne:ligne + CADRE]
        for x, v in enumerate(rang):
            if v > 40:
                colonnes[x] = True
    encre = [x for x, plein in enumerate(colonnes) if plein]
    return (encre[-1] - encre[0] + 1) if encre else 0


def replier(texte, lignes):
    """Coupe la phrase en `lignes` morceaux de longueur aussi proche que possible."""
    mots = texte.split()
    if len(mots) < lignes:
        return [texte]
    cible = len(texte) / lignes
    coupes, courant, sortie = [], "", []
    for mot in mots:
        essai = (courant + " " + mot).strip()
        if courant and len(essai) > cible and len(sortie) < lignes - 1:
            sortie.append(courant)
            courant = mot
        else:
            courant = essai
    sortie.append(courant)
    return sortie


def ajuster(texte, depart):
    texte = " ".join(texte.split())
    for lignes in (1, 2, 3):
        morceaux = replier(texte, lignes)
        taille = depart
        plancher = MIN_PAR_LIGNES[lignes]
        while taille >= plancher:
            if max(largeur(m, taille) for m in morceaux) <= MAXW:
                return taille, morceaux
            # On rétrécit par pas de 2 : un pas de 1 double le nombre de rendus
            # pour un gain d'un pixel, un pas de 4 saute la bonne taille.
            taille -= 2
        # Une ligne de plus rend de la largeur : on repart de la taille pleine.
    return MIN_POLICE, replier(texte, 3)


if __name__ == "__main__":
    phrase = sys.argv[1]
    depart = int(sys.argv[2]) if len(sys.argv) > 2 else 62
    taille, morceaux = ajuster(phrase, depart)
    print(taille)
    print("\n".join(morceaux))
