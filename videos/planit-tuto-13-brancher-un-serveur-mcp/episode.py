#!/usr/bin/env python3
"""Tutoriel 13 — Brancher un serveur MCP.

Fiche MCP `tutoriel_spec(numero: 13)`, slug `brancher-un-serveur-mcp`.
Capture source : « Vidéo 13 — Connexion des serveurs MCP (OAuth PKCE) » — 19,4 s, 392 × 852.

    python3 episode.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "planit-academy"))

from academie import Episode, Segment, build_episode  # noqa: E402

CROP = "crop=392:824:0:28"

EPISODE = Episode(
    numero=13,
    slug="brancher-un-serveur-mcp",
    titre="Brancher un serveur MCP",
    titre_court="Brancher un MCP",
    promesse="Vous ajoutez n'importe quel logiciel compatible en collant une adresse.",
    presentation=(
        "Bienvenue dans l'Académie Plan'It. Aujourd'hui : brancher un serveur MCP. Vos logiciels métier deviennent utilisables par vos agents."
    ),
    module_nom="Connexions API & MCP",
    module_couleur="#8236F8",
    variante="B",
    suivant="Gérer et débrancher ses connecteurs",
    crop=CROP,
    ecran_vignette=13.5,
    racine=Path(__file__).resolve().parent,
    segments=[
        Segment("N1",    0.2,    3.5, "1 · L'onglet MCP"),
        Segment("N2",    3.5,    6.5, "2 · Les serveurs proposés"),
        Segment("N3",    6.5,    9.0, "3 · Connecter"),
        Segment("N4",    9.0,   11.5, "4 · L'autorisation"),
        Segment("N5",   11.5,   15.5, "5 · Les outils arrivent"),
        Segment("N6",   15.5,   19.3, "6 · Connecté"),
    ],
)

if __name__ == "__main__":
    build_episode(EPISODE)
