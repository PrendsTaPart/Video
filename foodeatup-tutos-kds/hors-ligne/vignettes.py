#!/usr/bin/env python3
"""Vignette du tutoriel KDS n°14."""
import os, sys
ICI = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(ICI, "..", "..", "outils-tutos"))
from vignette import vignette
from tutos import T
os.makedirs(os.path.join(ICI, "sortie"), exist_ok=True)
for v in T:
    vignette(os.path.join(ICI, "sortie", v["cle"] + "-vignette.jpg"), os.path.join(ICI, "..", "ecrans-hors-ligne", "hors-ligne-02.png"),
             v["hook"], "KDS · TUTO 14/14", v["chef"], appareil="tablette")
