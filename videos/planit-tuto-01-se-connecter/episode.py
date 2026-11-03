#!/usr/bin/env python3
"""Tutoriel 01 — Se connecter à son espace.

Fiche MCP `tutoriel_spec(numero: 1)`, slug `se-connecter`.
Capture source : « Connexion et déconnexion » — 31,8 s, 590 × 1280, muette.

    python3 episode.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "planit-academy"))

from academie import Episode, Segment, build_episode  # noqa: E402

# La capture porte un filigrane CapCut en haut à gauche : on entre à y=80,
# ce qui l'élimine sans mordre sur le contenu de l'application.
CROP = "crop=590:1180:0:80"

EPISODE = Episode(
    numero=1,
    slug="se-connecter",
    titre="Se connecter à son espace",
    titre_court="Se connecter",
    promesse="Vous entrez dans votre espace en trois secondes, et vous en ressortez proprement.",
    presentation=(
        "Bienvenue dans l'Académie Plan'It. Aujourd'hui : se connecter à son espace. "
        "Vous entrez en trois secondes, et vous en ressortez tout aussi proprement."
    ),
    module_nom="Authentification",
    module_couleur="#4F2DF9",
    variante="B",              # manipulation à l'écran : l'écran domine
    suivant="Retrouver son mot de passe",
    crop=CROP,
    ecran_vignette=1.0,
    racine=Path(__file__).resolve().parent,
    segments=[
        Segment("N1",  0.3,  2.8, "1 · L'écran de connexion"),
        Segment("N2",  2.8,  5.6, "2 · Votre adresse professionnelle"),
        Segment("N3",  5.6, 13.2, "3 · Le mot de passe"),
        Segment("N4", 13.2, 17.8, "4 · Votre espace s'ouvre"),
        Segment("N5", 17.8, 24.5, "5 · Paramètres · Déconnexion"),
        Segment("N6", 24.5, 30.3, "6 · Confirmer la déconnexion"),
        Segment("N7", 30.3, 31.7, "7 · Compte fermé"),
    ],
)

if __name__ == "__main__":
    build_episode(EPISODE)
