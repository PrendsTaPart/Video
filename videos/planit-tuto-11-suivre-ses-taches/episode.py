#!/usr/bin/env python3
"""Tutoriel 11 — Suivre l'avancement de ses tâches.

Fiche MCP `tutoriel_spec(numero: 11)`, slug `suivre-ses-taches`.
Capture source : « Vidéo 5 — Liste des tâches et filtres » — 48,3 s, 392 × 852.

    python3 episode.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "planit-academy"))

from academie import Episode, Segment, build_episode  # noqa: E402

CROP = "crop=392:824:0:28"

EPISODE = Episode(
    numero=11,
    slug="suivre-ses-taches",
    titre="Suivre l'avancement de ses tâches",
    titre_court="Suivre ses tâches",
    promesse="Vous savez sans demander où en est chaque travail confié.",
    presentation=(
        "Bienvenue dans l'Académie Plan'It. Aujourd'hui : suivre l'avancement de ses tâches. Vous savez sans demander où en est chaque travail confié."
    ),
    module_nom="Tâches",
    module_couleur="#6A2EF5",
    variante="B",
    suivant="Créer sa première automatisation",
    crop=CROP,
    ecran_vignette=1.0,
    racine=Path(__file__).resolve().parent,
    segments=[
        Segment("N1",    0.3,    4.0, "1 · Vos tâches"),
        Segment("N2",    4.0,    8.5, "2 · Celles d'aujourd'hui"),
        Segment("N3",    8.5,   13.0, "3 · Celles qui sont finies"),
        Segment("N4",   13.5,   18.0, "4 · Le panneau de filtres"),
        Segment("N5",   18.0,   23.0, "5 · La période"),
        Segment("N6",   23.0,   29.5, "6 · La fréquence"),
        Segment("N7",   29.5,   35.0, "7 · La liste filtrée"),
        Segment("N8",   38.0,   44.0, "8 · Tout réinitialiser"),
        Segment("N9",   44.0,   48.2, "9 · Sans demander"),
    ],
)

if __name__ == "__main__":
    build_episode(EPISODE)
