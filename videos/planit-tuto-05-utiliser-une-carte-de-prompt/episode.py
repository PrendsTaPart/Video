#!/usr/bin/env python3
"""Tutoriel 05 — Utiliser une carte de prompt.

Fiche MCP `tutoriel_spec(numero: 5)`, slug `utiliser-une-carte-de-prompt`.
Capture source : « Vidéo 6 — Création et modification d'une tâche » — 121,5 s,
392 × 852, sonore (le son de la capture n'est pas repris).

Dans l'app, une carte de prompt s'emploie depuis le formulaire de tâche, par la
bascule « Prompt existant » : c'est ce parcours que suit le montage.

    python3 episode.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "planit-academy"))

from academie import Episode, Segment, build_episode  # noqa: E402

# Barre de statut Android sur les 28 premières lignes : on entre à y=28.
CROP = "crop=392:824:0:28"

EPISODE = Episode(
    numero=5,
    slug="utiliser-une-carte-de-prompt",
    titre="Utiliser une carte de prompt",
    titre_court="Utiliser une carte",
    promesse="Vous lancez une consigne éprouvée sans rien rédiger.",
    presentation=(
        "Bienvenue dans l'Académie Plan'It. Aujourd'hui : utiliser une carte de prompt. "
        "Vous lancez une consigne éprouvée, sans rien rédiger."
    ),
    module_nom="Prompts",
    module_couleur="#772FF3",
    variante="B",              # manipulation à l'écran : l'écran domine
    suivant="Chercher la bonne carte de prompt",
    crop=CROP,
    ecran_vignette=28.5,       # la carte choisie et ses variables
    racine=Path(__file__).resolve().parent,
    segments=[
        # Le plan 2 vient de 92,4 s : la feuille « Choisis comment tu veux créer
        # ta tâche » n'apparaît dans la capture qu'au second passage sur « + »,
        # alors qu'elle précède le formulaire dans le parcours réel.
        Segment("N1",   0.4,   3.2, "1 · Vos tâches"),
        Segment("N2",  92.4,  96.0, "2 · Trois façons de créer"),
        Segment("N3",   3.6,  12.2, "3 · Partir d'un prompt existant"),
        Segment("N4",  12.4,  24.0, "4 · Le titre de la tâche"),
        Segment("N5",  25.0,  30.0, "5 · Choisir la carte"),
        Segment("N6",  30.0,  45.0, "6 · La consigne est déjà écrite"),
        Segment("N7",  45.0,  58.5, "7 · Remplir les variables"),
        Segment("N8",  61.0,  67.5, "8 · La fréquence"),
        Segment("N9",  67.5,  82.0, "9 · Le jour et l'heure"),
        Segment("N10", 82.5,  92.0, "10 · Créer la tâche"),
        Segment("N11", 103.0, 114.0, "11 · Modifier après coup"),
        Segment("N12", 114.0, 118.0, "12 · Gardez ce qui marche"),
        Segment("N13", 118.0, 121.4, "13 · Sans rien rédiger"),
    ],
)

if __name__ == "__main__":
    build_episode(EPISODE)
