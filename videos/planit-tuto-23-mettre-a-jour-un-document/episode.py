#!/usr/bin/env python3
"""Tutoriel 23 — Mettre à jour un document déjà déposé.

Fiche MCP `tutoriel_spec(numero: 23)`, slug `mettre-a-jour-un-document`.
Capture source : « Vidéo 23 — Aperçu et édition manuelle des sections » — 55,3 s, 392 × 852.

    python3 episode.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "planit-academy"))

from academie import Episode, Segment, build_episode  # noqa: E402

CROP = "crop=392:824:0:28"

EPISODE = Episode(
    numero=23,
    slug="mettre-a-jour-un-document",
    titre="Mettre à jour un document déjà déposé",
    titre_court="Mettre à jour",
    promesse="Vos agents citent la nouvelle version, jamais l'ancienne.",
    presentation=(
        "Bienvenue dans l'Académie Plan'It. Aujourd'hui : mettre à jour ce que vos agents savent. Ils citeront la nouvelle version, jamais l'ancienne."
    ),
    module_nom="Base de connaissance",
    module_couleur="#A63FE8",
    variante="B",
    suivant="Vérifier d'où vient une réponse",
    crop=CROP,
    ecran_vignette=5.0,
    racine=Path(__file__).resolve().parent,
    segments=[
        Segment("N1",    0.3,    3.5, "1 · Six sections sur huit"),
        Segment("N2",    3.5,    8.0, "2 · Ce que l'assistant sait"),
        Segment("N3",    8.0,   12.0, "3 · En lecture seule"),
        Segment("N4",   12.0,   17.0, "4 · Modifier via les sections"),
        Segment("N5",   17.0,   22.0, "5 · Ouvrir la section"),
        Segment("N6",   22.0,   31.0, "6 · Compléter, pas réécrire"),
        Segment("N7",   31.0,   41.0, "7 · Une précision de plus"),
        Segment("N8",   41.0,   47.0, "8 · Enregistrer"),
        Segment("N9",   47.0,   52.0, "9 · L'aperçu suit"),
        Segment("N10",   52.0,   55.2, "10 · Jamais l'ancienne"),
    ],
)

if __name__ == "__main__":
    build_episode(EPISODE)
