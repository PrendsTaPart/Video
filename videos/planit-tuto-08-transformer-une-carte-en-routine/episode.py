#!/usr/bin/env python3
"""Tutoriel 08 — Transformer une carte en routine.

Fiche MCP `tutoriel_spec(numero: 8)`, slug `transformer-une-carte-en-routine`.
Capture source : « Vidéo 6 — Création et modification d'une tâche » — 121,5 s,
392 × 852.

**La capture affiche l'adresse du compte de démonstration** dans le champ
« RECIPIENT EMAIL », dans la barre de suggestions du clavier et dans l'aperçu du
contenu du prompt. Le relevé image par image en donne quatre, plus larges que
l'estimation de départ : 53–67 s, 93–99 s, 105–109 s et 113–121 s. Aucun
plan du montage n'y touche : l'épisode est construit sur les plages propres,
plutôt que de flouter après coup comme il a fallu le faire pour le tutoriel 00.
La variable montrée est donc « EMAIL SUBJECT », qui ne porte aucune donnée
personnelle.

    python3 episode.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "planit-academy"))

from academie import Episode, Segment, build_episode  # noqa: E402

CROP = "crop=392:824:0:28"

EPISODE = Episode(
    numero=8,
    slug="transformer-une-carte-en-routine",
    titre="Transformer une carte en routine",
    titre_court="Créer une routine",
    promesse="La consigne se relance toute seule, au rythme que vous fixez.",
    presentation=(
        "Bienvenue dans l'Académie Plan'It. Aujourd'hui : transformer une carte "
        "en routine. La consigne se relancera toute seule."
    ),
    module_nom="Tâches",
    module_couleur="#6A2EF5",
    variante="A",
    suivant="Partager une carte à son équipe",
    crop=CROP,
    ecran_vignette=2.0,         # l'écran d'une nouvelle tâche
    racine=Path(__file__).resolve().parent,
    segments=[
        Segment("N1",    2.5,   4.2, "1 · Une nouvelle tâche"),
        Segment("N2",    4.3,   7.5, "2 · Deux chemins"),
        Segment("N3",   12.0,  14.2, "3 · Le titre"),
        Segment("N4",   27.2,  30.2, "4 · Votre bibliothèque"),
        Segment("N5",   30.4,  32.4, "5 · Les variables"),
        Segment("N6",   36.0,  39.0, "6 · Remplies une fois"),
        Segment("N7",   68.0,  71.3, "7 · Le rythme"),
        Segment("N8",   72.0,  74.2, "8 · La première exécution"),
        Segment("N9",   78.0,  83.9, "9 · Une heure avant le besoin"),
        Segment("N10",  98.5, 101.5, "10 · Dans vos tâches"),
        Segment("N11", 101.4, 104.2, "11 · Ça arrive tout seul"),
    ],
)

if __name__ == "__main__":
    build_episode(EPISODE)
