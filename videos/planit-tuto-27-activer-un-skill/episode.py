#!/usr/bin/env python3
"""Tutoriel 27 — Activer un skill sur un agent.

Fiche MCP `tutoriel_spec(numero: 27)`, slug `activer-un-skill`.
Capture source : « Vidéo 26 — Liste et gestion des Skills » — 40,3 s, 392 × 852.

    python3 episode.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "planit-academy"))

from academie import Episode, Segment, build_episode  # noqa: E402

CROP = "crop=392:824:0:28"

EPISODE = Episode(
    numero=27,
    slug="activer-un-skill",
    titre="Activer un skill sur un agent",
    titre_court="Activer un skill",
    promesse="Votre agent gagne un savoir-faire précis, sans devenir compliqué.",
    presentation=(
        "Bienvenue dans l'Académie Plan'It. Aujourd'hui : activer un skill. Votre agent gagne un savoir-faire précis, sans devenir compliqué."
    ),
    module_nom="Skills & Plugins",
    module_couleur="#B846E0",
    variante="B",
    suivant="Installer un plugin",
    crop=CROP,
    ecran_vignette=36.0,
    racine=Path(__file__).resolve().parent,
    segments=[
        Segment("N1",    0.2,    3.5, "1 · L'écran Skills"),
        Segment("N2",    3.5,    8.0, "2 · Ce que chacun sait faire"),
        Segment("N3",    8.0,   12.5, "3 · Ceux qui sont actifs"),
        Segment("N4",   12.5,   18.0, "4 · Chercher un skill"),
        Segment("N5",   18.0,   22.5, "5 · Le résultat"),
        Segment("N6",   22.5,   28.5, "6 · Vos skills à vous"),
        Segment("N7",   28.5,   34.5, "7 · Activer d'un geste"),
        Segment("N8",   34.5,   38.0, "8 · Connecteur requis"),
        # L'astuce se pose sur la liste des skills actifs, la capture n'ayant
        # pas de plan libre à la fin.
        Segment("N9",    8.0,   12.5, "9 · Trois par agent"),
        Segment("N10",  38.0,   40.2, "10 · Spécialiser"),
    ],
)

if __name__ == "__main__":
    build_episode(EPISODE)
