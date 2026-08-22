#!/usr/bin/env python3
"""Rend un gabarit d'habillage sans écrire une ligne de Python.

    python3 -m habillage ouverture --titre "Brancher un MCP" --numero 13
    python3 -m habillage fin --suivant "Gérer ses connecteurs" --couleur "#8236F8"
    python3 -m habillage presentatrice --titre "…" --promesse "…" --voix vo/N0.mp3

Sans `--sortie`, le fichier atterrit dans `./rendu/<gabarit>.mp4`.
"""

from __future__ import annotations

import argparse
from pathlib import Path

from . import (Fin, Ouverture, Presentatrice, rendre_fin, rendre_ouverture,
               rendre_presentatrice)
from .noyau import MODULES, duration_of


def main() -> None:
    parser = argparse.ArgumentParser(prog="habillage", description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--modules", action="store_true",
                        help="liste les couleurs de module et sort")
    sub = parser.add_subparsers(dest="gabarit")

    o = sub.add_parser("ouverture", help="carton d'entrée, 3,6 s")
    o.add_argument("--titre", required=True)
    o.add_argument("--numero", type=int)
    o.add_argument("--chapeau")
    o.add_argument("--marque", default="Plan'It")
    o.add_argument("--sortie", type=Path)

    p = sub.add_parser("presentatrice", help="bulle animée, durée de la voix")
    p.add_argument("--titre", required=True)
    p.add_argument("--promesse", required=True)
    p.add_argument("--voix", type=Path, required=True)
    p.add_argument("--numero", type=int)
    p.add_argument("--plan", type=Path, help="MP4 de l'avatar ; celui de la série par défaut")
    p.add_argument("--sortie", type=Path)

    f = sub.add_parser("fin", help="carton de sortie, 5,2 s")
    f.add_argument("--suivant", default="")
    f.add_argument("--couleur", default="#4F2DF9")
    f.add_argument("--baseline")
    f.add_argument("--sortie", type=Path)

    args = parser.parse_args()

    if args.modules:
        for nom, couleur in MODULES.items():
            print(f"{couleur}  {nom}")
        return
    if not args.gabarit:
        parser.print_help()
        return

    cible = args.sortie or Path("rendu") / f"{args.gabarit}.mp4"
    cible.parent.mkdir(parents=True, exist_ok=True)

    if args.gabarit == "ouverture":
        rendre_ouverture(Ouverture(titre=args.titre, numero=args.numero,
                                   chapeau=args.chapeau, marque=args.marque), cible)
    elif args.gabarit == "fin":
        cfg = Fin(suivant=args.suivant, couleur=args.couleur)
        if args.baseline:
            cfg.baseline = args.baseline
        rendre_fin(cfg, cible)
    else:
        cfg = Presentatrice(titre=args.titre, promesse=args.promesse,
                            voix=args.voix, numero=args.numero)
        if args.plan:
            cfg.plan = args.plan
        rendre_presentatrice(cfg, cible)

    print(f"✓ {cible} — {duration_of(cible):.2f} s")


if __name__ == "__main__":
    main()
