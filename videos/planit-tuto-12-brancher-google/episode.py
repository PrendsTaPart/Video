#!/usr/bin/env python3
"""Tutoriel 12 — Brancher Google Agenda et Gmail.

Fiche MCP `tutoriel_spec(numero: 12)`, slug `brancher-google`.
Capture source : « Vidéo 12 — Connexion des services Google » — 56,4 s, 392 × 852.

    python3 episode.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "planit-academy"))

from academie import Episode, Segment, build_episode  # noqa: E402

CROP = "crop=392:824:0:28"

EPISODE = Episode(
    numero=12,
    slug="brancher-google",
    titre="Brancher Google Agenda et Gmail",
    titre_court="Brancher Google",
    promesse="Votre agent peut lire votre agenda et préparer vos courriels.",
    presentation=(
        "Bienvenue dans l'Académie Plan'It. Aujourd'hui : brancher Google Agenda et Gmail. Votre agent pourra lire votre agenda et préparer vos courriels."
    ),
    module_nom="Connexions API & MCP",
    module_couleur="#8236F8",
    variante="B",
    suivant="Brancher un serveur MCP",
    crop=CROP,
    ecran_vignette=44.0,
    racine=Path(__file__).resolve().parent,
    segments=[
        Segment("N1",    0.3,    4.0, "1 · L'onglet Services"),
        Segment("N2",    4.0,    8.5, "2 · Gmail, Agenda, Drive"),
        Segment("N3",    8.5,   14.0, "3 · L'écran de Google"),
        Segment("N4",   14.0,   18.0, "4 · Choisir son compte"),
        Segment("N5",   18.0,   22.0, "5 · Cocher les accès"),
        Segment("N6",   22.0,   26.5, "6 · Confirmer"),
        Segment("N7",   26.5,   32.0, "7 · Authentifié"),
        Segment("N8",   32.0,   41.0, "8 · Un service après l'autre"),
        Segment("N9",   41.0,   50.0, "9 · La pastille verte"),
        Segment("N10",   50.0,   56.2, "10 · Et l'on coupe aussi vite"),
    ],
)

if __name__ == "__main__":
    build_episode(EPISODE)
