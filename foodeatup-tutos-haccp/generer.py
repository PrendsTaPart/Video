#!/usr/bin/env python3
"""Série « Application tablette HACCP » : projets HyperFrames (montage commun outils-tutos/montage.py)."""
import os, sys
ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(ICI, "..", "outils-tutos"))
from montage import construire
from tutos import T
construire({"dossier": ICI, "captures": os.path.join(ICI, "captures"), "rubrique": "Application HACCP",
            "nom_final": "FoodEatUp HACCP", "appareil": "telephone"}, T, sys.argv[1:] or None)
