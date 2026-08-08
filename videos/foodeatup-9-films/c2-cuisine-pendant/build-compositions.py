#!/usr/bin/env python3
"""Génère les 8 scènes de C2 · Cuisine pendant le service.

Les durées ne sont pas choisies : elles viennent des timings réels de la voix
off, relevés au mot près par `npx hyperframes transcribe` sur `assets/vo.mp3`
(`assets/transcript.json`). Chaque scène commence exactement là où la phrase
qui la porte commence.

  0,00  Midi. Les premières commandes tombent…
  7,48  J'affiche mon écran de cuisine, poste par poste…
 20,32  Les commandes arrivent de partout…
 35,80  Je fais avancer les plats…
 44,20  Un plat en rupture ?…
 50,92  Dix-huit heures. Je pointe mon retour…
 57,60  PrediBot a lu mes trois dernières semaines…
 67,99  Dix-neuf heures. Je relance mon écran…
 73,07  (fin de la voix, le film court jusqu'à 77,58)
"""

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "_serie"))
from serie import Serie  # noqa: E402

s = Serie(metier=Serie.CUISINE, sous="c2")

SCENES = {
    "c2-s1-midi.html": s.carton(
        "c2-s1-midi", "0.00", "7.48", "cloche", "vid-plate-cloche",
        "Midi", "Les premières commandes tombent",
    ),
    "c2-s2-postes.html": s.ecran(
        "c2-s2-postes", "7.48", "12.84", "12:10", "CHAQUE POSTE, SON ÉCRAN",
        "SCENE-2", "vid-scene-2",
        ["Chaud", "Pass", "Froid"],
    ),
    "c2-s3-canaux.html": s.ecran(
        "c2-s3-canaux", "20.32", "15.48", "12:15", "TOUS LES CANAUX, UNE SEULE FILE",
        "SCENE-3", "vid-scene-3",
        ["Salle", "Comptoir", "Site", "Livraison"],
    ),
    "c2-s4-avancement.html": s.ecran(
        "c2-s4-avancement", "35.80", "8.40", "12:20", "JE FAIS AVANCER LES PLATS",
        "SCENE-4", "vid-scene-4",
        ["Un geste par plat", "La salle suit"],
    ),
    # Aucun tutoriel n'existe pour la mise en rupture : plutôt que d'inventer
    # une interface, la scène reste sur le geste et la voix porte l'info.
    "c2-s5-rupture.html": s.carton(
        "c2-s5-rupture", "44.20", "6.72", "chef-kds", "vid-plate-kds",
        "Un plat en rupture", "Je le retire une fois, il disparaît partout",
        amb_opacity=".72", title_at=".3", sub_at=".9",
    ),
    "c2-s6-retour.html": s.ecran(
        "c2-s6-retour", "50.92", "6.68", "18:00", "JE REPRENDS MON POSTE",
        "SCENE-6", "vid-scene-6",
        ["Retour pointé", "Températures"],
    ),
    "c2-s7-predibot.html": s.ecran(
        "c2-s7-predibot", "57.60", "10.39", "18:10", "PREDIBOT ANNONCE LA SOIRÉE",
        "SCENE-7", "vid-scene-7",
        ["Prévisions lues", "Production validée", "Avant le coup de feu"],
    ),
    "c2-s8-soir.html": s.carton(
        "c2-s8-soir", "67.99", "9.59", "deux-chefs", "vid-plate-deux-chefs",
        "Le service du soir peut commencer", "Dix-neuf heures",
        amb_opacity=".68", title_at=".4", sub_at="1.0",
    ),
}

if __name__ == "__main__":
    s.ecrire(SCENES)
