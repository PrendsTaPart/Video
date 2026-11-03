#!/usr/bin/env python3
"""Tutoriel 07 — Enregistrer sa propre carte de prompt.

Fiche MCP `tutoriel_spec(numero: 7)`, slug `enregistrer-sa-propre-carte`.
Capture source : « Vidéo 10 — Création et modification d'un prompt » — 97,4 s, 392 × 852.

    python3 episode.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "planit-academy"))

from academie import Episode, Segment, build_episode  # noqa: E402

CROP = "crop=392:824:0:28"

EPISODE = Episode(
    numero=7,
    slug="enregistrer-sa-propre-carte",
    titre="Enregistrer sa propre carte de prompt",
    titre_court="Enregistrer sa carte",
    promesse="Votre meilleure consigne devient réutilisable en un geste.",
    presentation=(
        "Bienvenue dans l'Académie Plan'It. Aujourd'hui : enregistrer sa propre carte de prompt. Votre meilleure consigne devient réutilisable en un geste."
    ),
    module_nom="Prompts",
    module_couleur="#772FF3",
    variante="B",
    suivant="Transformer une carte en routine",
    crop=CROP,
    ecran_vignette=52.0,
    racine=Path(__file__).resolve().parent,
    segments=[
        Segment("N1",    0.3,    4.5, "1 · Un nouveau prompt"),
        Segment("N2",    4.5,   12.0, "2 · Le nom"),
        Segment("N3",   12.0,   18.0, "3 · La description"),
        Segment("N4",   18.5,   26.0, "4 · Une première variable"),
        Segment("N5",   26.0,   34.0, "5 · Une deuxième"),
        Segment("N6",   44.0,   48.5, "6 · Le type de la variable"),
        Segment("N7",   50.0,   62.0, "7 · La troisième"),
        Segment("N8",   66.0,   73.0, "8 · Visibilité et création"),
        Segment("N9",   73.5,   79.0, "9 · Dans la bibliothèque"),
        Segment("N10",   79.5,   90.0, "10 · Modifier plus tard"),
        Segment("N11",   90.0,   94.0, "11 · Ce qui change"),
        Segment("N12",   94.0,   97.3, "12 · Réutilisable"),
    ],
)

if __name__ == "__main__":
    build_episode(EPISODE)
