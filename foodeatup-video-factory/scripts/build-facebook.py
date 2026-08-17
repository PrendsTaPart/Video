#!/usr/bin/env python3
"""Monte les stories Facebook à partir des stories déjà montées.

    python3 scripts/build-facebook.py            (tout ce qui manque)
    python3 scripts/build-facebook.py EP001 le-coup-de-feu-S1

Pourquoi un carton différent de celui de YouTube
------------------------------------------------
Le format est le même — `Vidéo native 9:16`, comme le dit la fiche réseau — et
l'image est la même story. Ce qui change, c'est ce qu'on attend du spectateur
à la fin.

Sur YouTube, la suite est sur la chaîne : le carton donne son nom, et le
spectateur y va d'un clic depuis le lecteur. Sur Facebook, une vidéo native
n'emporte pas son lien avec elle — elle est repartagée, elle réapparaît dans le
fil d'un tiers, la légende reste derrière. Le carton porte donc l'appel à
l'action et l'adresse que la fiche réseau déclare déjà (`cta`, `lienCta`),
plutôt qu'un nom de page que personne ne peut cliquer.

Le reste — l'empilement du bloc, les fondus, le son — vit dans
`montage_carton.py`, avec le Short YouTube et la version paysage.
"""
import sys

from montage_carton import Gabarit, main

FACEBOOK = Gabarit(
    dossier="facebook",
    largeur=1080,
    hauteur=1920,
    # Deux lignes de pied : l'invitation, puis l'adresse. L'adresse est plus
    # petite — c'est ce qu'on relit, pas ce qu'on lit.
    pieds=["Découvrir FoodEatUp", "site.foodeatup.com"],
    corps_pied=[46, 36],
)


if __name__ == "__main__":
    main(FACEBOOK, sys.argv[1:])
