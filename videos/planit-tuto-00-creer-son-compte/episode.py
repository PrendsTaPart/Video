#!/usr/bin/env python3
"""Tutoriel 00 — Créer son compte Plan'It.

Fiche MCP `tutoriel_spec(numero: 0)`, slug `creer-son-compte`.
Capture source : « Inscription » — 78,0 s, 590 × 1280, muette.

    python3 episode.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "planit-academy"))

from academie import Episode, Segment, build_episode  # noqa: E402

# Cette capture n'a pas de filigrane : recadrage limité aux bandes noires.
CROP = "crop=590:1234:0:23"

EPISODE = Episode(
    numero=0,
    slug="creer-son-compte",
    titre="Créer son compte Plan'It",
    titre_court="Créer son compte",
    promesse="Votre compte existe et votre espace de travail est ouvert.",
    presentation=(
        "Bienvenue dans l'Académie Plan'It. Aujourd'hui, on commence par le tout "
        "début : créer votre compte. Une minute, et votre espace de travail est ouvert."
    ),
    module_nom="Authentification",
    module_couleur="#4F2DF9",
    variante="A",              # concept ou découverte : l'avatar domine
    suivant="Se connecter à son espace",
    crop=CROP,
    ecran_vignette=0.5,        # l'écran de connexion
    racine=Path(__file__).resolve().parent,
    segments=[
        # Coupes volontaires : 39,2 → 42,0 (sortie vers l'écran d'accueil du
        # téléphone), 47,0 → 50,5 (bascule multitâche) et 71,5 → 74,8
        # (squelettes de chargement, clavier encore ouvert).
        # Recalés le 27/08 : cinq plans sortaient de la bande lisible
        # (×0,82 – ×1,65), jusqu'à ×3,60 sur la saisie du mot de passe et ×2,47
        # sur la reconnexion. Les longues plages sont désormais échantillonnées
        # sur un moment représentatif plutôt qu'accélérées d'un bout à l'autre.
        Segment("N1",  0.0,  5.0, "1 · L'écran de connexion"),
        Segment("N2",  4.2, 11.5, "2 · Le formulaire d'inscription"),
        Segment("N3", 13.0, 17.5, "3 · L'adresse professionnelle"),
        Segment("N4", 26.0, 31.5, "4 · Mot de passe et confirmation"),
        # S'arrête avant que l'application quitte l'écran : la carte réduite
        # de la bascule y redevient lisible.
        Segment("N5", 34.2, 37.7, "5 · Le code à 6 chiffres"),
        Segment("N6", 42.0, 47.0, "6 · Le code reçu par email"),
        # Débute après la bascule multitâche : la carte réduite y laisse voir
        # l'adresse, trop petite pour être reconnue par le masquage.
        Segment("N7", 53.3, 58.5, "7 · Vérification du code"),
        Segment("N8", 64.5, 71.0, "8 · Première connexion"),
        Segment("N9", 73.0, 78.0, "9 · Votre espace est ouvert"),
    ],
)

if __name__ == "__main__":
    build_episode(EPISODE)
