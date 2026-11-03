#!/usr/bin/env python3
"""Tutoriel 14 — Gérer et débrancher ses connecteurs.

Fiche MCP `tutoriel_spec(numero: 14)`, slug `gerer-ses-connecteurs`.
Capture source : « Vidéo 14 — Gestion d'un serveur MCP connecté » — 27,4 s, 392 × 852.

    python3 episode.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "planit-academy"))

from academie import Episode, Segment, build_episode  # noqa: E402

CROP = "crop=392:824:0:28"

EPISODE = Episode(
    numero=14,
    slug="gerer-ses-connecteurs",
    titre="Gérer et débrancher ses connecteurs",
    titre_court="Gérer les connecteurs",
    promesse="Vous voyez d'un coup d'œil qui a accès à quoi, et vous coupez en un geste.",
    presentation=(
        "Bienvenue dans l'Académie Plan'It. Aujourd'hui : gérer et débrancher ses connecteurs. Vous voyez qui a accès à quoi, et vous coupez en un geste."
    ),
    module_nom="Connexions API & MCP",
    module_couleur="#8236F8",
    variante="B",
    suivant="Déposer ses documents dans la base de connaissance",
    crop=CROP,
    ecran_vignette=8.0,
    racine=Path(__file__).resolve().parent,
    segments=[
        Segment("N1",    0.2,    3.0, "1 · Vos connecteurs"),
        Segment("N2",    3.0,    6.0, "2 · Ouvrir une fiche"),
        Segment("N3",    6.0,   10.0, "3 · Les outils accordés"),
        Segment("N4",   10.0,   14.0, "4 · Ceux marqués destructifs"),
        Segment("N5",   14.0,   18.5, "5 · Refermer la liste"),
        Segment("N6",   18.5,   23.0, "6 · Tester la connexion"),
        Segment("N7",   23.0,   25.5, "7 · Débrancher"),
        Segment("N8",   25.5,   27.3, "8 · Réversible"),
    ],
)

if __name__ == "__main__":
    build_episode(EPISODE)
