#!/usr/bin/env python3
"""Tutoriel 42 — Gérer ses appareils connectés.

Fiche MCP `tutoriel_spec(numero: 42)`, slug `gerer-ses-appareils`.
Capture source : « Vidéo 42 — Configuration des périphériques » — 22,81 s,
590 × 1280, sans filigrane.

Réserve de contenu : la fiche promet « chaque appareil connecté à votre compte »
et une coupure à distance. L'écran réel — « Voix & périphériques » — gère la
langue de Jarvis et l'appairage Bluetooth des oreillettes. Le montage suit
l'application, pas la fiche ; l'écart est reporté dans CONNAISSANCE-PLANIT.md.

    python3 episode.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "planit-academy"))

from academie import Episode, Segment, build_episode  # noqa: E402

# Capture propre : aucune bande noire, aucun filigrane à retirer.
CROP = "crop=590:1280:0:0"

EPISODE = Episode(
    numero=42,
    slug="gerer-ses-appareils",
    titre="Gérer ses appareils connectés",
    titre_court="Gérer ses appareils",
    promesse="Vous choisissez sur quoi Jarvis vous écoute et vous répond.",
    presentation=(
        "Bienvenue dans l'Académie Plan'It. Aujourd'hui : gérer ses appareils. "
        "Vous choisissez sur quoi Jarvis vous écoute et vous répond."
    ),
    module_nom="Appareils",
    module_couleur="#FE64D5",
    variante="B",
    suivant="",                # dernier épisode : la ligne « Prochain » est masquée
    crop=CROP,
    ecran_vignette=19.5,       # la liste des périphériques, remplie
    racine=Path(__file__).resolve().parent,
    segments=[
        Segment("N1",  0.0,  2.9, "1 · Paramètres"),
        Segment("N2",  2.9,  6.6, "2 · La langue de Jarvis"),
        Segment("N3",  6.6,  9.3, "3 · Périphériques audio Bluetooth"),
        Segment("N4",  9.3, 11.0, "4 · Associer un périphérique"),
        Segment("N5", 11.0, 14.8, "5 · Les réglages du téléphone"),
        Segment("N6", 14.8, 17.9, "6 · Connecter son oreillette"),
        Segment("N7", 17.9, 21.0, "7 · Appairé ou connecté"),
        Segment("N8", 21.0, 22.8, "8 · Retirer un appareil"),
    ],
)

if __name__ == "__main__":
    build_episode(EPISODE)
