#!/usr/bin/env python3
"""Monte les vidéos TikTok à partir des stories déjà montées.

    python3 scripts/build-tiktok.py            (tout ce qui manque)
    python3 scripts/build-tiktok.py EP001 le-coup-de-feu-S1

Attention au dossier
--------------------
`dist/tiktok/` n'est PAS la sortie de ce script : il porte les masters de
37,5 s, ceux que `videoUrl` sert au site depuis le début, et cinquante et un
épisodes en dépendent. Le nom est trompeur — il vient du premier réseau visé —
mais on ne le renomme pas : ces adresses sont publiées.

Ce script écrit dans `dist/tiktok-story/`, à côté de `youtube/`, `facebook/` et
`youtube-paysage/`, avec lesquels il forme une famille : même story de départ,
même carton de fin, une ligne de pied par réseau.

Ce que le carton dit ici
------------------------
Le compte, `@foodeatup`. Sur TikTok, le nom d'utilisateur est cliquable depuis
le lecteur — comme la chaîne sur YouTube, et contrairement à Facebook où une
vidéo native repartagée n'emporte plus aucun lien et où le carton doit donc
porter l'adresse du site en toutes lettres.
"""
import sys

from montage_carton import Gabarit, main

TIKTOK = Gabarit(
    dossier="tiktok-story",
    largeur=1080,
    hauteur=1920,
    pieds=["@foodeatup"],
    corps_pied=[46],
)


if __name__ == "__main__":
    main(TIKTOK, sys.argv[1:])
