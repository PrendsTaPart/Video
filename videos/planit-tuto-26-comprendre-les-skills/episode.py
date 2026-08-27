#!/usr/bin/env python3
"""Tutoriel 26 — Comprendre à quoi servent les skills.

Fiche MCP `tutoriel_spec(numero: 26)`, slug `comprendre-les-skills`.
Capture source : « Vidéo 28 — Actualisation du catalogue depuis GitHub » —
19,5 s, 590 × 1280.

La fiche demande d'ouvrir la liste des compétences et de lire ce que chacune
ajoute. La capture fait exactement cela, puis montre d'où vient le catalogue :
un bouton « Actualiser » qui va rechercher la liste à jour. Les deux écrans —
Skills puis Plugins — répondent de la même façon.

    python3 episode.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "planit-academy"))

from academie import Episode, Segment, build_episode  # noqa: E402

CROP = "crop=590:1236:0:44"

EPISODE = Episode(
    numero=26,
    slug="comprendre-les-skills",
    titre="Comprendre à quoi servent les skills",
    titre_court="Comprendre les skills",
    promesse="Vous savez quand ajouter une compétence plutôt que réécrire une consigne.",
    presentation=(
        "Bienvenue dans l'Académie Plan'It. Aujourd'hui : à quoi servent les "
        "skills. Quand ajouter une compétence plutôt que répéter une consigne."
    ),
    module_nom="Skills & Plugins",
    module_couleur="#B846E0",
    variante="B",
    suivant="Activer un skill sur un agent",
    crop=CROP,
    ecran_vignette=3.0,         # la liste des skills, chacun avec sa description
    racine=Path(__file__).resolve().parent,
    # La capture n'offre que quatre plages stables — le menu Assistant, la liste
    # Skills, le retour au menu, la liste Plugins. Les plans s'y chevauchent
    # volontairement pour tenir la vitesse dans la bande lisible.
    segments=[
        Segment("N1",   0.0,  3.0, "1 · Le menu Assistant"),
        Segment("N2",   2.2,  6.0, "2 · La liste des skills"),
        Segment("N3",   2.5,  5.5, "3 · Ce que dit chaque ligne"),
        Segment("N4",   3.0,  7.0, "4 · Une méthode, pas une consigne"),
        Segment("N5",   4.8,  8.0, "5 · Actualiser"),
        Segment("N6",   6.2, 10.5, "6 · La liste se met à jour"),
        Segment("N7",  13.0, 17.0, "7 · Les plugins"),
        Segment("N8",  15.8, 19.4, "8 · Déjà à jour"),
        Segment("N9",   2.5,  7.5, "9 · Le skill qui manque"),
        Segment("N10",  9.0, 13.0, "10 · Installé une fois"),
    ],
)

if __name__ == "__main__":
    build_episode(EPISODE)
