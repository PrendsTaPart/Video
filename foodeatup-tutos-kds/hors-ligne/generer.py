#!/usr/bin/env python3
"""Tutoriel KDS n°14 (hors ligne) : projet HyperFrames par le montage commun outils-tutos/montage.py."""
import os, sys
ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(ICI, "..", "..", "outils-tutos"))
from montage import construire
from tutos import T
construire({"dossier": ICI, "captures": os.path.join(ICI, "..", "ecrans-hors-ligne"), "rubrique": "Application KDS",
            "nom_final": "FoodEatUp KDS", "appareil": "tablette", "total": 14}, T, sys.argv[1:] or None)
