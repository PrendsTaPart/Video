#!/usr/bin/env python3
"""Tutoriel 34 — Personnaliser la fiche de son agent.

Fiche MCP `tutoriel_spec(numero: 34)`, slug `personnaliser-la-fiche-agent`.
Capture source : « Vidéo 33 — Personnalisation de l'avatar » — 89,6 s, 392 × 852.

Réserve. La fiche demande d'écrire la mission de l'agent « en deux lignes » et
son ton. La capture ne filme pas ce champ : elle montre le renommage, le choix
de l'avatar, l'arrière-plan, l'import d'un modèle 3D et la voix. La voix off
suit l'écran ; seule l'astuce parle de la mission, sans prétendre la montrer.

    python3 episode.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "planit-academy"))

from academie import Episode, Segment, build_episode  # noqa: E402

CROP = "crop=392:824:0:28"

EPISODE = Episode(
    numero=34,
    slug="personnaliser-la-fiche-agent",
    titre="Personnaliser la fiche de son agent",
    titre_court="Personnaliser l'agent",
    promesse="Chaque agent a son rôle écrit noir sur blanc.",
    presentation=(
        "Bienvenue dans l'Académie Plan'It. Aujourd'hui : personnaliser la "
        "fiche de son agent. Chacun aura son rôle, et son visage."
    ),
    module_nom="Profil & Avatar 3D",
    module_couleur="#CA4DD8",
    variante="A",
    suivant="Écouter la réponse de son agent",
    crop=CROP,
    ecran_vignette=1.5,         # la galerie « Mes avatars »
    racine=Path(__file__).resolve().parent,
    segments=[
        Segment("N1",   0.2,  3.8, "1 · Mes avatars"),
        Segment("N2",  29.0, 32.4, "2 · Huit par défaut"),
        Segment("N3",  19.4, 21.2, "3 · Le renommage"),
        Segment("N4",  24.3, 26.7, "4 · Par leur métier"),
        Segment("N5",  35.9, 38.4, "5 · Avatar activé"),
        Segment("N6",  40.0, 42.2, "6 · Dans le chat"),
        Segment("N7",  51.2, 53.8, "7 · La personnalisation"),
        Segment("N8",  65.7, 68.9, "8 · L'arrière-plan"),
        Segment("N9",  78.0, 80.5, "9 · Le décor appliqué"),
        Segment("N10", 84.3, 87.2, "10 · Votre propre modèle 3D"),
        Segment("N11", 87.4, 89.2, "11 · La voix de l'assistant"),
        Segment("N12", 43.0, 46.7, "12 · Comme une fiche de poste"),
        Segment("N13", 81.6, 84.4, "13 · Un rôle défini"),
    ],
)

if __name__ == "__main__":
    build_episode(EPISODE)
