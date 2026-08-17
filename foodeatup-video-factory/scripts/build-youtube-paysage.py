#!/usr/bin/env python3
"""Monte la version paysage 16:9 des vidéos YouTube.

    python3 scripts/build-youtube-paysage.py            (tout ce qui manque)
    python3 scripts/build-youtube-paysage.py EP001 le-coup-de-feu-S1

Pourquoi une deuxième version YouTube
-------------------------------------
`formatParReseau` le dit depuis le début : le format natif de YouTube est le
16:9. Le Short vertical existe et a sa place — il vit dans l'onglet Shorts, où
il se feuillette — mais la page d'une chaîne, la recherche, la suggestion et la
lecture sur téléviseur sont en paysage. Une vidéo verticale y arrive avec deux
bandes noires qui occupent les deux tiers de l'écran.

Ce que le cadre devient
-----------------------
Le plan Higgsfield est vertical et le restera : le recadrer en 16:9 couperait
la tête ou le plan de travail, c'est-à-dire le sujet. Il est donc posé en
pleine hauteur au centre, et les côtés sont comblés par une copie floutée et
assombrie du plan lui-même.

Ce traitement n'est pas inventé ici : c'est exactement celui des vignettes
`EPxxx-16x9.jpg` déjà produites, où la vignette verticale est centrée sur un
fond flou tiré de la même image. La vidéo et sa miniature se ressemblent donc,
ce qui est le minimum qu'on attend d'une miniature — et c'est aussi pourquoi la
donnée ne porte pas d'adresse de vignette : `vignetteEpisode(id, "youtube")`
sert déjà ce fichier.

Le carton de fin, lui, est refait en pleine largeur : il est fabriqué à la
volée, il n'y a aucune raison de le laisser en bande étroite entre deux
morceaux de flou.
"""
import sys

from montage_carton import Gabarit, main

PAYSAGE = Gabarit(
    dossier="youtube-paysage",
    largeur=1920,
    hauteur=1080,
    pieds=["@FoodEatUp"],
    corps_pied=[48],
    queue=4,
    fond_flou=True,
    # Un cadre large laisse respirer le titre : il tient sur une ligne bien
    # plus souvent qu'en vertical, et peut donc être écrit plus gros.
    coupe_titre=34,
    corps_titre=(84, 68),
    # Le fond flou occupe les deux tiers de l'image et se compresse pour rien à
    # CRF 20 : un cran au-dessus divise le poids par deux sans que le plan net,
    # qui est ce qu'on regarde, y perde quoi que ce soit.
    crf="22",
)


if __name__ == "__main__":
    main(PAYSAGE, sys.argv[1:])
