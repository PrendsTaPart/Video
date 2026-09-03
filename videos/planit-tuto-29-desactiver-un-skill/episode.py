#!/usr/bin/env python3
"""Tutoriel 29 — Désactiver un skill ou un plugin.

Fiche MCP `tutoriel_spec(numero: 29)`, slug `desactiver-un-skill`.
Capture source : « Vidéo 27 — Liste et gestion des Plugins » — 26,4 s,
392 × 852.

La capture montre l'écran de gestion : la liste, la recherche, l'interrupteur
de chaque ligne, et l'avertissement « Connecteur requis » quand un plugin
réclame un branchement qui n'existe pas encore. C'est cet interrupteur qui fait
la fiche : il coupe et il rallume.

    python3 episode.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "planit-academy"))

from academie import Episode, Segment, build_episode  # noqa: E402

CROP = "crop=392:824:0:28"

EPISODE = Episode(
    numero=29,
    slug="desactiver-un-skill",
    titre="Désactiver un skill ou un plugin",
    titre_court="Désactiver un skill",
    promesse="Vous revenez en arrière sans rien casser.",
    presentation=(
        "Bienvenue dans l'Académie Plan'It. Aujourd'hui : désactiver un skill "
        "ou un plugin. Vous revenez en arrière sans rien casser."
    ),
    module_nom="Skills & Plugins",
    module_couleur="#B846E0",
    variante="B",
    suivant="Confirmer une action sensible",
    crop=CROP,
    ecran_vignette=24.0,        # l'état final : interrupteurs mêlés, allumés et éteints
    racine=Path(__file__).resolve().parent,
    segments=[
        Segment("N1",   0.2,  3.6, "1 · L'écran Plugins"),
        Segment("N2",   0.5,  4.0, "2 · Un interrupteur par ligne"),
        Segment("N3",   5.2,  8.6, "3 · La recherche"),
        Segment("N4",   8.4, 11.4, "4 · Le bon plugin, seul"),
        Segment("N5",  11.2, 13.4, "5 · La liste revient"),
        Segment("N6",  13.6, 17.2, "6 · Le même geste dans les deux sens"),
        Segment("N7",  16.8, 20.2, "7 · Connecteur requis"),
        Segment("N8",  18.6, 22.4, "8 · Elle vous emmène le brancher"),
        Segment("N9",  13.4, 19.0, "9 · La dernière ajoutée en premier"),
        Segment("N10", 22.8, 26.3, "10 · Rien n'est définitif"),
    ],
)

if __name__ == "__main__":
    build_episode(EPISODE)
