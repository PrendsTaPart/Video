#!/usr/bin/env python3
"""Tutoriel 25 — Retirer un document de la base.

Fiche MCP `tutoriel_spec(numero: 25)`, slug `retirer-un-document`.
Capture source : « Vidéo 24 — Réinitialisation de la base de connaissance » — 32,4 s, 590 × 1280.

    python3 episode.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "planit-academy"))

from academie import Episode, Segment, build_episode  # noqa: E402

CROP = "crop=590:1236:0:44"

EPISODE = Episode(
    numero=25,
    slug="retirer-un-document",
    titre="Retirer un document de la base",
    titre_court="Repartir de zéro",
    promesse="Ce qui ne doit plus être cité disparaît des réponses.",
    presentation=(
        "Bienvenue dans l'Académie Plan'It. Aujourd'hui : retirer ce que vos agents ne doivent plus citer. Deux portées, deux gestes différents."
    ),
    module_nom="Base de connaissance",
    module_couleur="#A63FE8",
    variante="A",
    suivant="Comprendre à quoi servent les skills",
    crop=CROP,
    ecran_vignette=4.5,
    racine=Path(__file__).resolve().parent,
    segments=[
        Segment("N1",    0.2,    2.5, "1 · Votre base remplie"),
        Segment("N2",    2.5,    6.0, "2 · Réinitialiser ?"),
        Segment("N3",    6.0,   10.0, "3 · Deux portées"),
        Segment("N4",   10.0,   14.0, "4 · Reprendre l'entretien"),
        Segment("N5",   14.0,   19.0, "5 · La conversation repart"),
        Segment("N6",   19.0,   23.5, "6 · Tout effacer"),
        Segment("N7",   23.5,   28.0, "7 · Plus rien"),
        Segment("N8",   28.0,   32.3, "8 · Ce qu'il lit, ce qu'il dit"),
    ],
)

if __name__ == "__main__":
    build_episode(EPISODE)
