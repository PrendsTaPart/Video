#!/usr/bin/env python3
"""Série « Application Caisse mobile (gestes complémentaires) » : projets HyperFrames (montage commun outils-tutos/montage.py)."""
import os, sys
ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(ICI, "..", "outils-tutos"))
from montage import construire
from tutos import T
construire({"dossier": ICI, "captures": os.path.join(ICI, "captures"), "rubrique": "Caisse mobile",
            "nom_final": "FoodEatUp Caisse", "appareil": "telephone"}, T, sys.argv[1:] or None)
