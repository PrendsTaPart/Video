#!/usr/bin/env python3
"""Monte les Shorts YouTube à partir des stories déjà montées.

    python3 scripts/build-youtube.py            (tous ceux qui manquent)
    python3 scripts/build-youtube.py EP001 EP002

Pourquoi un format de plus
--------------------------
Les quatre autres réseaux poussent la vidéo dans un fil : on la croise. YouTube
est le seul où quelqu'un la cherche — il tape une question, il lit un titre, il
choisit. `gen-publications.py` en tient déjà compte côté texte, avec un titre
qui porte la requête et une description longue. Côté image, il manquait la
contrepartie : un plan qui dise de quelle série vient ce qu'on vient de voir,
et où trouver la suite.

D'où le carton de fin. La story s'arrête sur sa punchline, ce qui est juste
dans un fil qui défile tout seul ; sur YouTube elle s'arrête sur rien. Deux
secondes et demie de plus suffisent à poser le titre de l'épisode, la série, et
la chaîne.

Ce que le script ne refait pas
------------------------------
Le montage. La story porte déjà le clip Higgsfield, le hook, la punchline et le
son du plan — tout cela a été réglé une fois, il n'y a aucune raison de le
rejouer différemment ici. Le Short est donc la story, plus un carton. Un
épisode sans story n'a pas de Short : le script le dit et passe.

La mécanique du carton vit dans `montage_carton.py`, avec la version paysage et
la story Facebook. Ce fichier ne décrit plus que ce qui est propre à YouTube :
un cadre vertical, et une dernière ligne qui donne le nom de la chaîne.
"""
import sys

from montage_carton import Gabarit, main

YOUTUBE = Gabarit(
    dossier="youtube",
    largeur=1080,
    hauteur=1920,
    # La chaîne, et rien d'autre : depuis le lecteur YouTube, son nom suffit à
    # y aller. C'est ce qui distingue ce carton de celui de Facebook, où aucun
    # lien ne suit la vidéo quand elle est repartagée.
    pieds=["@FoodEatUp"],
    corps_pied=[46],
)


if __name__ == "__main__":
    main(YOUTUBE, sys.argv[1:])
