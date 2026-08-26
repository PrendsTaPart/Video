#!/usr/bin/env python3
"""Tutoriel 33 — Choisir l'avatar 3D de son agent.

Fiche MCP `tutoriel_spec(numero: 33)`, slug `choisir-son-avatar`.
Capture source : « Vidéo 32 — Création et génération d'un avatar 3D » —
96,2 s, 590 × 1280.

    python3 episode.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "planit-academy"))

from academie import Episode, Segment, build_episode  # noqa: E402

# Capture 590 × 1280 : barre de statut sur les 44 premières lignes.
CROP = "crop=590:1236:0:44"

EPISODE = Episode(
    numero=33,
    slug="choisir-son-avatar",
    titre="Choisir l'avatar 3D de son agent",
    titre_court="Choisir un avatar",
    promesse="Votre équipe d'agents devient reconnaissable d'un coup d'œil.",
    presentation=(
        "Bienvenue dans l'Académie Plan'It. Aujourd'hui : donner un visage à son agent. "
        "Votre équipe devient reconnaissable d'un coup d'œil."
    ),
    module_nom="Profil & Avatar 3D",
    module_couleur="#CA4DD8",
    variante="A",              # concept et découverte : l'avatar domine
    suivant="Personnaliser la fiche de son agent",
    crop=CROP,
    ecran_vignette=87.5,       # « Avatar créé ! »
    racine=Path(__file__).resolve().parent,
    segments=[
        # Spans resserrés pour tenir chaque plan sous ×1,7 : les longues plages
        # de barre de progression sont échantillonnées, pas accélérées.
        Segment("N1",   0.2,  5.0, "1 · Créer son avatar"),
        Segment("N2",   6.0, 11.0, "2 · L'identité"),
        Segment("N3",  12.5, 16.7, "3 · L'apparence"),
        Segment("N4",  17.0, 23.0, "4 · La tenue"),
        Segment("N5",  23.0, 28.0, "5 · Le style 3D"),
        Segment("N6",  28.0, 34.0, "6 · Une précision libre"),
        Segment("N7",  35.5, 40.0, "7 · Générer"),
        Segment("N8",  42.0, 46.2, "8 · L'attente"),
        Segment("N9",  47.0, 52.5, "9 · La progression"),
        Segment("N10", 70.0, 74.5, "10 · Presque fini"),
        Segment("N11", 85.5, 90.5, "11 · Avatar créé"),
        Segment("N12", 89.0, 93.5, "12 · Toute l'équipe"),
        # L'astuce se pose sur la galerie des rôles, le seul plan qui montre
        # plusieurs agents côte à côte.
        Segment("N13", 92.0, 96.2, "13 · Un métier, un visage"),
        Segment("N14", 85.5, 89.0, "14 · Une équipe lisible"),
    ],
)

if __name__ == "__main__":
    build_episode(EPISODE)
