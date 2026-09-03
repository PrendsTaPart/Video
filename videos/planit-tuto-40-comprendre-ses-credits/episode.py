#!/usr/bin/env python3
"""Tutoriel 40 — Comprendre ses crédits.

Fiche MCP `tutoriel_spec(numero: 40)`, slug `comprendre-ses-credits`.
Capture source : « Vidéo 40 — Historique des consommations » — 24,0 s, 392 × 852.

Réserve : la fiche mentionne une alerte de seuil (« Fixez une alerte de
seuil »). L'écran n'en propose pas — la voix off n'en parle donc pas.

    python3 episode.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "planit-academy"))

from academie import Episode, Segment, build_episode  # noqa: E402

CROP = "crop=392:824:0:28"

EPISODE = Episode(
    numero=40,
    slug="comprendre-ses-credits",
    titre="Comprendre ses crédits",
    titre_court="Comprendre les crédits",
    promesse="Vous savez ce que vous consommez et pourquoi, avant de lancer.",
    presentation=(
        "Bienvenue dans l'Académie Plan'It. Aujourd'hui : comprendre ses "
        "crédits. Vous saurez ce que vous consommez, et pourquoi."
    ),
    module_nom="Crédits & Facturation",
    module_couleur="#F45FC4",
    variante="B",
    suivant="Gérer son abonnement et ses factures",
    crop=CROP,
    ecran_vignette=1.0,         # le solde en tête d'écran
    racine=Path(__file__).resolve().parent,
    segments=[
        Segment("N1",   0.2,  3.4, "1 · Mes crédits IA"),
        Segment("N2",   0.6,  3.4, "2 · Le solde"),
        Segment("N3",   3.4,  6.2, "3 · L'historique"),
        Segment("N4",   8.2, 12.4, "4 · Ligne par ligne"),
        Segment("N5",  11.6, 14.4, "5 · Ce qui est inclus"),
        Segment("N6",  12.6, 15.8, "6 · La période"),
        Segment("N7",  16.4, 19.6, "7 · Soixante-deux actions"),
        Segment("N8",  20.6, 23.9, "8 · Les crédits reçus"),
        Segment("N9",   8.2, 12.0, "9 · Le seul ratio qui compte"),
        Segment("N10",  0.4,  3.2, "10 · Le prix avant"),
    ],
)

if __name__ == "__main__":
    build_episode(EPISODE)
