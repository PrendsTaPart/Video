#!/usr/bin/env python3
"""Tutoriel 28 — Installer un plugin.

Fiche MCP `tutoriel_spec(numero: 28)`, slug `installer-un-plugin`.
Capture source : « Vidéo 29 — Import de Skills/Plugins personnels en ZIP » —
30,4 s, 392 × 852.

Dans l'application, un plugin s'ajoute en important son archive ZIP depuis
l'écran Skills : c'est ce parcours que suit le montage.

    python3 episode.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "planit-academy"))

from academie import Episode, Segment, build_episode  # noqa: E402

CROP = "crop=392:824:0:28"

EPISODE = Episode(
    numero=28,
    slug="installer-un-plugin",
    titre="Installer un plugin",
    titre_court="Installer un plugin",
    promesse="Votre agent gagne un nouvel outil venu de l'extérieur.",
    presentation=(
        "Bienvenue dans l'Académie Plan'It. Aujourd'hui : installer un plugin. "
        "Votre agent gagne un outil venu de l'extérieur."
    ),
    module_nom="Skills & Plugins",
    module_couleur="#B846E0",
    variante="B",
    suivant="Désactiver un skill ou un plugin",
    crop=CROP,
    ecran_vignette=11.0,        # le bandeau « 1 skill importé »
    racine=Path(__file__).resolve().parent,
    segments=[
        Segment("N1",   0.2,  3.0, "1 · L'écran Skills"),
        Segment("N2",   3.0,  5.6, "2 · Importer un ZIP"),
        Segment("N3",   3.8,  7.2, "3 · Choisir le fichier"),
        Segment("N4",   6.5,  8.7, "4 · L'archive"),
        Segment("N5",   9.5, 13.5, "5 · Importé"),
        Segment("N6",  17.0, 20.6, "6 · Le retrouver"),
        Segment("N7",  20.6, 25.4, "7 · Marqué « Perso »"),
        Segment("N8",  25.4, 30.3, "8 · Le retirer"),
        # L'astuce se pose sur le choix du fichier, la capture n'ayant pas de
        # plan libre à la fin.
        Segment("N9",   3.8,  8.7, "9 · Ce que vous utiliserez"),
        Segment("N10", 10.0, 13.5, "10 · Sans une ligne de code"),
    ],
)

if __name__ == "__main__":
    build_episode(EPISODE)
