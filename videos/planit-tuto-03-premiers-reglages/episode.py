#!/usr/bin/env python3
"""Tutoriel 03 — Les premiers réglages de votre entreprise.

Fiche MCP `tutoriel_spec(numero: 3)`, slug `premiers-reglages`.
Capture source : « Vidéo 25 — Bandeau "Faire connaissance" dans le chat » —
7,1 s, 392 × 852.

La fiche demande de renseigner l'activité, la clientèle et le ton. Dans
l'application c'est l'entretien « Faire connaissance » et ses huit sections qui
recueillent exactement cela : le montage suit ce parcours, du bandeau proposé
dans le chat jusqu'à la liste des sections à remplir.

    python3 episode.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "planit-academy"))

from academie import Episode, Segment, build_episode  # noqa: E402

CROP = "crop=392:824:0:28"

EPISODE = Episode(
    numero=3,
    slug="premiers-reglages",
    titre="Les premiers réglages de votre entreprise",
    titre_court="Premiers réglages",
    promesse="Vos agents savent qui vous êtes, ce que vous vendez et à qui.",
    presentation=(
        "Bienvenue dans l'Académie Plan'It. Aujourd'hui : les premiers réglages "
        "de votre entreprise. Vos agents sauront qui vous êtes et ce que vous "
        "vendez."
    ),
    module_nom="Authentification",
    module_couleur="#4F2DF9",
    variante="B",
    suivant="Utiliser une carte de prompt",
    crop=CROP,
    ecran_vignette=5.5,         # l'entretien et ses huit sections
    racine=Path(__file__).resolve().parent,
    segments=[
        Segment("N1", 0.2, 4.0, "1 · Le bandeau"),
        Segment("N2", 1.9, 3.8, "2 · Commencer"),
        Segment("N3", 4.0, 7.1, "3 · Huit sections"),
        Segment("N4", 4.4, 7.1, "4 · Zéro sur huit"),
        Segment("N5", 4.2, 7.1, "5 · Des réponses personnalisées"),
        Segment("N6", 0.2, 4.4, "6 · Le ton en une phrase"),
        Segment("N7", 0.6, 4.0, "7 · Utile plutôt que générique"),
    ],
)

if __name__ == "__main__":
    build_episode(EPISODE)
