#!/usr/bin/env python3
"""Tutoriel 22 — Organiser sa base de connaissance.

Fiche MCP `tutoriel_spec(numero: 22)`, slug `organiser-sa-base-de-connaissance`.
Capture source : « Vidéo 22 — Entretien conversationnel » — 199,4 s, 392 × 852.

L'entretien dure plus de trois minutes : le montage retient onze fenêtres
courtes plutôt que d'accélérer la frappe.

    python3 episode.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "planit-academy"))

from academie import Episode, Segment, build_episode  # noqa: E402

CROP = "crop=392:824:0:28"

EPISODE = Episode(
    numero=22,
    slug="organiser-sa-base-de-connaissance",
    titre="Organiser sa base de connaissance",
    titre_court="Passer l'entretien",
    promesse="Vos informations sont rangées par thème, donc retrouvées par vos agents.",
    presentation=(
        "Bienvenue dans l'Académie Plan'It. Aujourd'hui : organiser sa base de connaissance. L'assistant vous interroge, et range vos réponses pour vous."
    ),
    module_nom="Base de connaissance",
    module_couleur="#A63FE8",
    variante="B",
    suivant="Mettre à jour un document déjà déposé",
    crop=CROP,
    ecran_vignette=52.0,
    racine=Path(__file__).resolve().parent,
    segments=[
        Segment("N1",    0.3,    5.0, "1 · L'entretien"),
        Segment("N2",   12.0,   17.0, "2 · Répondre avec ses mots"),
        Segment("N3",   22.0,   27.0, "3 · Une question à la fois"),
        Segment("N4",   40.0,   46.0, "4 · L'assistant relance"),
        Segment("N5",   48.0,   53.5, "5 · Une section rangée"),
        Segment("N6",   60.0,   65.0, "6 · La proposition de valeur"),
        Segment("N7",   88.0,   93.0, "7 · Les preuves"),
        Segment("N8",  108.0,  113.5, "8 · Les concurrents"),
        Segment("N9",  130.0,  135.0, "9 · Ce qui vous distingue"),
        Segment("N10",  160.0,  166.0, "10 · Autant de tours qu'il faut"),
        Segment("N11",  190.0,  199.3, "11 · Six sections sur huit"),
    ],
)

if __name__ == "__main__":
    build_episode(EPISODE)
