#!/usr/bin/env python3
"""Vignettes de la série « Application Menu digital »."""
import os, sys
ICI = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(ICI, "..", "outils-tutos"))
from vignette import vignette
from tutos import T
os.makedirs(os.path.join(ICI, "sortie"), exist_ok=True)
for i, v in enumerate(T):
    e = v.get("ecran_vignette") or v["ecrans"][min(1, len(v["ecrans"]) - 1)][0]
    vignette(os.path.join(ICI, "sortie", v["cle"] + "-vignette.jpg"), os.path.join(ICI, "captures", e), v["hook"],
             f"MENU DIGITAL · TUTO {i+1}/{len(T)}", v["chef"], appareil="tablette")
    print(v["cle"], e)
