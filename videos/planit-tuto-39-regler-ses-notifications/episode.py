#!/usr/bin/env python3
"""Tutoriel 39 — Régler ses notifications.

Fiche MCP `tutoriel_spec(numero: 39)`, slug `regler-ses-notifications`.
Capture source : « Vidéo 35 — Centre de notifications » suivie de « Vidéo 36 —
Préférences de notifications », mises bout à bout — 42,9 s, 590 × 1280.

Les deux captures se répondent : la première montre le flot d'alertes « tâche
terminée », la seconde l'écran qui permet de le couper. C'est exactement
l'astuce de la fiche — on notifie ce qui attend une décision, pas ce qui est
fini — et il fallait les deux pour la démontrer.

    python3 episode.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "planit-academy"))

from academie import Episode, Segment, build_episode  # noqa: E402

CROP = "crop=590:1236:0:44"

EPISODE = Episode(
    numero=39,
    slug="regler-ses-notifications",
    titre="Régler ses notifications",
    titre_court="Régler les alertes",
    promesse="Vous êtes prévenu seulement quand cela mérite votre attention.",
    presentation=(
        "Bienvenue dans l'Académie Plan'It. Aujourd'hui : régler ses "
        "notifications. Vous serez prévenu seulement quand ça le mérite."
    ),
    module_nom="Notifications",
    module_couleur="#DC54D0",
    variante="B",
    suivant="Recevoir un rapport automatique",
    crop=CROP,
    ecran_vignette=30.0,        # l'écran des préférences
    racine=Path(__file__).resolve().parent,
    segments=[
        # 0 → 22,9 s : le centre de notifications. 22,9 → 42,9 s : ses réglages.
        Segment("N1",   0.2,  2.4, "1 · La cloche"),
        Segment("N2",   2.4,  4.5, "2 · Une ligne par tâche"),
        Segment("N3",   4.8,  8.0, "3 · Le détail"),
        Segment("N4",   8.5, 12.6, "4 · Tout remonte"),
        Segment("N5",  13.0, 16.6, "5 · La liste se remplit"),
        Segment("N6",  22.4, 25.1, "6 · L'engrenage"),
        Segment("N7",  25.4, 28.2, "7 · Trois réglages"),
        Segment("N8",  28.4, 32.0, "8 · Ce qu'on garde"),
        Segment("N9",  32.4, 36.3, "9 · La règle"),
        Segment("N10", 34.6, 37.5, "10 · Trop d'alertes"),
    ],
)

if __name__ == "__main__":
    build_episode(EPISODE)
