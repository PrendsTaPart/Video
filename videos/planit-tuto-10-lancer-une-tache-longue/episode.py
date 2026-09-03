#!/usr/bin/env python3
"""Tutoriel 10 — Lancer une tâche qui prend du temps.

Fiche MCP `tutoriel_spec(numero: 10)`, slug `lancer-une-tache-longue`.
Capture source : « Vidéo 37 — Navigation depuis une notification » — 10,0 s,
392 × 852.

La capture ne couvre que la seconde moitié de la fiche : la notification qui
arrive et le résultat qu'on retrouve. Le geste « Exécuter en tâche de fond »
n'est pas filmé — la présentation le porte, l'écran ne le montre pas.

    python3 episode.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "planit-academy"))

from academie import Episode, Segment, build_episode  # noqa: E402

CROP = "crop=392:824:0:28"

EPISODE = Episode(
    numero=10,
    slug="lancer-une-tache-longue",
    titre="Lancer une tâche qui prend du temps",
    titre_court="Lancer une tâche",
    promesse="Vous confiez un travail long et vous fermez l'application sans rien perdre.",
    presentation=(
        "Bienvenue dans l'Académie Plan'It. Aujourd'hui : confier un travail long. "
        "Vous lancez, vous fermez l'application, et vous êtes prévenu."
    ),
    module_nom="Tâches",
    module_couleur="#6A2EF5",
    variante="B",
    suivant="Suivre l'avancement de ses tâches",
    crop=CROP,
    ecran_vignette=5.5,        # la tâche terminée, à l'écran
    racine=Path(__file__).resolve().parent,
    segments=[
        # La capture ne fait que dix secondes : les spans se chevauchent pour
        # tenir la vitesse de chaque plan autour de ×1, sans ralenti visible.
        Segment("N1", 0.3,  3.4, "1 · La notification"),
        Segment("N2", 2.6,  3.9, "2 · Un geste"),
        Segment("N3", 3.6,  6.4, "3 · La tâche s'ouvre"),
        Segment("N4", 5.0,  7.8, "4 · Exécutée à 19 h 40"),
        Segment("N5", 7.8, 10.0, "5 · Retour à l'accueil"),
        Segment("N6", 4.6,  7.4, "6 · Partir pendant que ça travaille"),
    ],
)

if __name__ == "__main__":
    build_episode(EPISODE)
