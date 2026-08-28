#!/usr/bin/env python3
"""Tutoriel 36 — Choisir les indicateurs de son accueil.

Fiche MCP `tutoriel_spec(numero: 36)`, slug `suivre-ses-indicateurs`.
Capture source : « Vidéo 4 — Tableau de bord et KPI » — 147,4 s, 392 × 852.

Seconde moitié de la capture : l'écran « Configurer l'accueil », la
réorganisation par glisser-déposer, le catalogue de widgets, les réglages d'un
widget et sa suppression. La première moitié sert la fiche 4.

Dans l'application, le bouton s'appelle « Configurer » et non « Personnaliser »
comme l'annonce la fiche : la voix off suit l'écran.

    python3 episode.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "planit-academy"))

from academie import Episode, Segment, build_episode  # noqa: E402

CROP = "crop=392:824:0:28"

EPISODE = Episode(
    numero=36,
    slug="suivre-ses-indicateurs",
    titre="Choisir les indicateurs de son accueil",
    titre_court="Choisir ses indicateurs",
    promesse="Votre écran d'accueil ne montre que ce qui vous concerne.",
    presentation=(
        "Bienvenue dans l'Académie Plan'It. Aujourd'hui : choisir les "
        "indicateurs de son accueil. Il ne montrera que ce qui vous concerne."
    ),
    module_nom="Accueil & Statistiques",
    module_couleur="#5C2DF7",
    variante="B",
    suivant="Lire le temps gagné par vos agents",
    crop=CROP,
    ecran_vignette=31.0,        # l'écran « Configurer l'accueil »
    racine=Path(__file__).resolve().parent,
    segments=[
        Segment("N1",   30.2,  33.1, "1 · Configurer"),
        Segment("N2",   33.2,  35.5, "2 · Poignée, œil, corbeille"),
        Segment("N3",   45.0,  48.2, "3 · Réordonner"),
        Segment("N4",   75.0,  77.4, "4 · Le catalogue"),
        Segment("N5",   78.0,  82.0, "5 · Ce qu'on peut ajouter"),
        Segment("N6",   85.0,  89.0, "6 · Régler un widget"),
        Segment("N7",   93.0,  95.0, "7 · Il apparaît sur l'accueil"),
        Segment("N8",  100.8, 104.3, "8 · Le retirer"),
        Segment("N9",  105.5, 108.7, "9 · Trois cartes maximum"),
        Segment("N10", 135.5, 138.4, "10 · Un accueil qu'on consulte"),
    ],
)

if __name__ == "__main__":
    build_episode(EPISODE)
