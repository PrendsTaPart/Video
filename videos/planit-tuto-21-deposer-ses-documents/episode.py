#!/usr/bin/env python3
"""Tutoriel 21 — Déposer ses documents dans la base de connaissance.

Fiche MCP `tutoriel_spec(numero: 21)`, slug `deposer-ses-documents`.
Capture source : « Vidéo 21 — Accueil de la base de connaissance » — 119,5 s, 392 × 852.

Dans l'app, la base ne se remplit pas par dépôt de fichiers mais par huit
sections rédigées — la voix off suit l'écran, pas le libellé de la fiche.

    python3 episode.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "planit-academy"))

from academie import Episode, Segment, build_episode  # noqa: E402

CROP = "crop=392:824:0:28"

EPISODE = Episode(
    numero=21,
    slug="deposer-ses-documents",
    titre="Déposer ses documents dans la base de connaissance",
    titre_court="Faire connaissance",
    promesse="Vos agents répondent avec vos informations, pas avec des généralités.",
    presentation=(
        "Bienvenue dans l'Académie Plan'It. Aujourd'hui : donner à vos agents de quoi vous connaître. Ils répondront avec vos informations, pas avec des généralités."
    ),
    module_nom="Base de connaissance",
    module_couleur="#A63FE8",
    variante="A",
    suivant="Organiser sa base de connaissance",
    crop=CROP,
    ecran_vignette=45.0,
    racine=Path(__file__).resolve().parent,
    segments=[
        Segment("N1",    0.3,    6.0, "1 · Faire connaissance"),
        Segment("N2",    6.0,   12.0, "2 · Huit sections"),
        Segment("N3",   12.0,   20.0, "3 · Votre entreprise"),
        Segment("N4",   20.0,   31.0, "4 · Avec vos mots"),
        Segment("N5",   34.0,   45.0, "5 · Ce que vous vendez"),
        Segment("N6",   45.0,   53.0, "6 · Enregistrer"),
        Segment("N7",   54.0,   62.0, "7 · La section suivante"),
        Segment("N8",   62.0,   78.0, "8 · Votre ton"),
        Segment("N9",   78.0,   92.0, "9 · Ce qui est interdit"),
        Segment("N10",  100.0,  110.0, "10 · Trois sections suffisent"),
        Segment("N11",  112.0,  119.4, "11 · Déjà utilisable"),
    ],
)

if __name__ == "__main__":
    build_episode(EPISODE)
