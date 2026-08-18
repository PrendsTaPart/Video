#!/usr/bin/env python3
"""Tutoriel 02 — Retrouver son mot de passe.

Fiche MCP `tutoriel_spec(numero: 2)`, slug `retrouver-son-mot-de-passe`.
Capture source : « Mot de passe oublié et réinitialisation » — 46,0 s,
590 × 1280, muette.

    python3 episode.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "planit-academy"))

from academie import Episode, Segment, build_episode  # noqa: E402

# Filigrane CapCut en haut à gauche : on entre à y=80 pour l'éliminer.
CROP = "crop=590:1180:0:80"

EPISODE = Episode(
    numero=2,
    slug="retrouver-son-mot-de-passe",
    titre="Retrouver son mot de passe",
    titre_court="Mot de passe oublié",
    promesse="Vous reprenez la main sur votre compte sans appeler personne.",
    presentation=(
        "Bienvenue dans l'Académie Plan'It. Aujourd'hui : retrouver son mot de passe. "
        "Vous reprenez la main sur votre compte sans appeler personne."
    ),
    module_nom="Authentification",
    module_couleur="#4F2DF9",
    variante="B",              # manipulation à l'écran : l'écran domine
    suivant="Les premiers réglages de votre entreprise",
    crop=CROP,
    ecran_vignette=4.0,        # l'écran « Mot de passe oublié ? »
    racine=Path(__file__).resolve().parent,
    segments=[
        # Coupes volontaires : 12,8 → 14,5 (sortie vers Gmail), 19,3 → 24,0
        # (bascule multitâche) et 41,4 → 43,3 (traitement).
        Segment("N1",  0.3,  2.5, "1 · « Mot de passe oublié ? »"),
        Segment("N2",  2.5,  6.4, "2 · L'adresse de votre compte"),
        Segment("N3",  6.4,  9.3, "3 · Envoyer le code"),
        Segment("N4",  9.3, 12.8, "4 · L'écran de vérification"),
        Segment("N5", 14.5, 19.3, "5 · Le code reçu par email"),
        Segment("N6", 24.0, 30.0, "6 · Saisir les six chiffres"),
        Segment("N7", 30.0, 41.4, "7 · Le nouveau mot de passe"),
        Segment("N8", 43.3, 45.9, "8 · Mot de passe actif"),
    ],
)

if __name__ == "__main__":
    build_episode(EPISODE)
