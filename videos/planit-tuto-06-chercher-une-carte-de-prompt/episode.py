#!/usr/bin/env python3
"""Tutoriel 06 — Chercher la bonne carte de prompt.

Fiche MCP `tutoriel_spec(numero: 6)`, slug `chercher-une-carte-de-prompt`.
Capture source : « Vidéo 9 — Liste des prompts et recherche » — 37,4 s,
392 × 852, sonore (le son de la capture n'est pas repris).

    python3 episode.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "planit-academy"))

from academie import Episode, Segment, build_episode  # noqa: E402

# Barre de statut Android sur les 28 premières lignes : on entre à y=28.
CROP = "crop=392:824:0:28"

EPISODE = Episode(
    numero=6,
    slug="chercher-une-carte-de-prompt",
    titre="Chercher la bonne carte de prompt",
    titre_court="Chercher une carte",
    promesse="Vous trouvez en dix secondes la consigne qui correspond à votre besoin du jour.",
    presentation=(
        "Bienvenue dans l'Académie Plan'It. Aujourd'hui : chercher la bonne carte de prompt. "
        "Vous trouvez en dix secondes la consigne qui correspond à votre besoin."
    ),
    module_nom="Prompts",
    module_couleur="#772FF3",
    variante="B",              # manipulation à l'écran : l'écran domine
    suivant="Enregistrer sa propre carte de prompt",
    crop=CROP,
    ecran_vignette=33.0,       # la recherche « calendar » et son résultat, clavier refermé
    racine=Path(__file__).resolve().parent,
    segments=[
        Segment("N1",   0.3,  4.4, "1 · La bibliothèque"),
        Segment("N2",   4.4,  8.6, "2 · Lire une carte"),
        Segment("N3",   8.6, 13.5, "3 · Les filtres"),
        Segment("N4",  13.5, 16.4, "4 · Mes prompts privés"),
        Segment("N5",  16.4, 20.4, "5 · Filtrer par outil"),
        Segment("N6",  20.4, 24.5, "6 · Un autre outil"),
        Segment("N7",  24.6, 29.6, "7 · La recherche"),
        Segment("N8",  29.6, 33.6, "8 · Le résultat"),
        # L'astuce se pose sur le défilement du début, la capture n'ayant pas
        # de plan libre à la fin.
        Segment("N9",   4.4,  9.4, "9 · Cherchez par verbe"),
        Segment("N10", 33.6, 37.3, "10 · En dix secondes"),
    ],
)

if __name__ == "__main__":
    build_episode(EPISODE)
