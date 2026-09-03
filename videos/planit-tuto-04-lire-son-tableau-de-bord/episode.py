#!/usr/bin/env python3
"""Tutoriel 04 — Lire son tableau de bord.

Fiche MCP `tutoriel_spec(numero: 4)`, slug `lire-son-tableau-de-bord`.
Capture source : « Vidéo 4 — Tableau de bord et KPI » — 147,4 s, 392 × 852.

La capture couvre deux fiches. Sa première moitié — l'accueil, les indicateurs
et leurs formules — sert celle-ci ; sa seconde, « Configurer l'accueil », sert
la fiche 36. Les deux montages se partagent le même fichier source sans se
chevaucher.

    python3 episode.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "planit-academy"))

from academie import Episode, Segment, build_episode  # noqa: E402

CROP = "crop=392:824:0:28"

EPISODE = Episode(
    numero=4,
    slug="lire-son-tableau-de-bord",
    titre="Lire son tableau de bord",
    titre_court="Lire son tableau",
    promesse="Vous savez en dix secondes ce que vos agents ont fait pour vous.",
    presentation=(
        "Bienvenue dans l'Académie Plan'It. Aujourd'hui : lire son tableau de "
        "bord. Dix secondes pour savoir ce que vos agents ont fait."
    ),
    module_nom="Accueil & Statistiques",
    module_couleur="#5C2DF7",
    variante="C",
    suivant="Choisir les indicateurs de son accueil",
    crop=CROP,
    ecran_vignette=1.5,         # l'accueil et ses deux indicateurs
    racine=Path(__file__).resolve().parent,
    segments=[
        Segment("N1",   0.2,  2.1, "1 · L'accueil"),
        Segment("N2",   0.4,  3.7, "2 · Les deux chiffres du haut"),
        Segment("N3",   6.2,  9.6, "3 · La formule"),
        Segment("N4",  10.8, 13.1, "4 · Jours d'autonomie"),
        Segment("N5",  15.2, 18.7, "5 · L'activité des agents"),
        Segment("N6",  18.4, 21.3, "6 · Votre activité"),
        Segment("N7",  21.4, 25.0, "7 · L'état de l'assistant"),
        Segment("N8",  22.6, 24.7, "8 · Les prompts les plus utilisés"),
        # La fin de la capture revient sur l'accueil : de quoi poser l'astuce
        # et la promesse sans réutiliser les plans du début.
        Segment("N9",  121.0, 126.0, "9 · La tendance, pas le point"),
        Segment("N10", 135.5, 138.5, "10 · Sans mesure"),
    ],
)

if __name__ == "__main__":
    build_episode(EPISODE)
