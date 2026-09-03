#!/usr/bin/env python3
"""Tutoriel 15 — Sa première conversation avec un agent.

Fiche MCP `tutoriel_spec(numero: 15)`, slug `premiere-conversation`.
Capture source : « Vidéo 25 — Bandeau "Faire connaissance" dans le chat » —
7,1 s, 392 × 852.

Réserve. La capture montre l'accueil du chat et le bandeau qui propose de se
présenter à l'assistant avant d'écrire — elle ne montre pas la rédaction d'un
premier message. Les étapes 2 à 4 de la fiche (dire ce qu'on veut obtenir,
préciser le format, demander une correction) sont portées par la voix, pas par
l'écran.

Sept secondes de source pour dix plans : les plages se chevauchent largement,
et la vitesse reste au plancher de la bande lisible (×0,82).

    python3 episode.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "planit-academy"))

from academie import Episode, Segment, build_episode  # noqa: E402

CROP = "crop=392:824:0:28"

EPISODE = Episode(
    numero=15,
    slug="premiere-conversation",
    titre="Sa première conversation avec un agent",
    titre_court="Première conversation",
    promesse="Vous obtenez un résultat utile dès votre premier message.",
    presentation=(
        "Bienvenue dans l'Académie Plan'It. Aujourd'hui : votre première "
        "conversation. Un résultat utile dès le premier message."
    ),
    module_nom="Chat agentique",
    module_couleur="#9438F0",
    variante="A",
    suivant="Donner du contexte dans une conversation",
    crop=CROP,
    ecran_vignette=1.0,         # l'accueil du chat, avec la rangée d'agents
    racine=Path(__file__).resolve().parent,
    segments=[
        Segment("N1", 0.2, 4.6, "1 · L'accueil du chat"),
        Segment("N2", 0.4, 4.6, "2 · Le bandeau"),
        Segment("N3", 2.6, 4.6, "3 · Commencer"),
        Segment("N4", 4.0, 7.1, "4 · Huit sections"),
        Segment("N5", 4.4, 7.1, "5 · Plus précis à chaque réponse"),
        Segment("N6", 0.2, 4.4, "6 · Terminez par le format"),
        Segment("N7", 0.6, 4.4, "7 · Une consigne claire"),
    ],
)

if __name__ == "__main__":
    build_episode(EPISODE)
