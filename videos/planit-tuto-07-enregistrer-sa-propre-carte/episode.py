#!/usr/bin/env python3
"""Tutoriel 07 — Enregistrer sa propre carte de prompt.

Fiche MCP `tutoriel_spec(numero: 7)`, slug `enregistrer-sa-propre-carte`.
Capture source : « Vidéo 10 — Création et modification d'un prompt » (2ᵉ version) — 97,4 s, 392 × 852.

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
    ecran_vignette=63.0,
    racine=Path(__file__).resolve().parent,
    segments=[
        # Spans resserrés pour garder la vitesse de chaque plan entre ×0,85 et
        # ×1,7 : au-delà, une saisie au clavier devient illisible.
        Segment("N1",   0.2,  4.8, "1 · Un nouveau prompt"),
        Segment("N2",   4.8,  9.4, "2 · Le nom"),
        Segment("N3",  36.0, 42.0, "3 · La description"),
        Segment("N4",  14.0, 21.5, "4 · Une première variable"),
        Segment("N5",  30.0, 34.0, "5 · Une deuxième"),
        Segment("N7",  48.0, 52.0, "6 · La troisième"),
        Segment("N6",  52.0, 57.5, "7 · Le type de la variable"),
        Segment("N8",  57.5, 62.0, "8 · Créer le prompt"),
        Segment("N9",  61.5, 65.5, "9 · Dans la bibliothèque"),
        Segment("N10", 65.5, 72.0, "10 · Modifier plus tard"),
        # L'astuce revient sur la pose d'une variable, le geste qu'elle commente.
        Segment("N11", 22.0, 28.0, "11 · Ce qui change"),
        Segment("N12", 73.5, 78.3, "12 · Réutilisable"),
    ],
)

if __name__ == "__main__":
    build_episode(EPISODE)
