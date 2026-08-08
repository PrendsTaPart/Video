#!/usr/bin/env python3
"""Génère les 11 scènes de C3 · Cuisine après le service.

Les bornes viennent des timings réels de la voix off, relevés au mot près par
`npx hyperframes transcribe` (`assets/transcript.json`). Chaque scène commence
exactement là où commence la phrase qui la porte.

   0,00  Quatorze heures trente. Le service est fini…
   2,99  Ce qu'il reste sur les plans de travail…
  19,08  J'imprime mes étiquettes, je les colle…
  24,59  Ce qui est parti en pertes, je le saisis…
  33,46  Ma traçabilité du midi se referme…
  38,03  Vingt-deux heures quinze…
  45,17  Puis je pointe mes zones de nettoyage…
  51,05  Une photo. L'intelligence artificielle regarde à ma place…
  61,55  Ma check-list de conformité…
  65,81  Vingt-trois heures. Je pointe ma sortie…
  71,42  (fin de la voix, le film court jusqu'à 76,00)

Le film a deux mouvements — fermeture du midi, fermeture du soir — séparés
par le carton de 38,03 s. C'est la seule coupure franche du parcours cuisine :
les huit heures qui séparent les deux services ne sont pas racontées, elles
sont sautées.
"""

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "_serie"))
from serie import Serie  # noqa: E402

s = Serie(metier=Serie.CUISINE, sous="c3")

SCENES = {
    # Carton court : le titre doit être posé en moins de 3 s, donc il entre
    # plus tôt que sur les autres cartons de la série.
    "c3-s1-fin-service.html": s.carton(
        "c3-s1-fin-service", "0.00", "2.99", "chef-nettoie", "vid-plate-nettoie",
        "Quatorze heures trente", "Le service est fini",
        title_at=".15", sub_at=".7",
    ),
    "c3-s2-dlc.html": s.ecran(
        "c3-s2-dlc", "2.99", "16.09", "14:30", "CHAQUE RESTE, SA DATE LIMITE",
        "SCENE-2", "vid-scene-2",
        ["Le plat", "La quantité", "L'équipement"],
    ),
    "c3-s3-etiquettes.html": s.ecran(
        "c3-s3-etiquettes", "19.08", "5.51", "14:35", "J'IMPRIME MES ÉTIQUETTES",
        "SCENE-3", "vid-scene-3",
        ["Étiquettes posées", "Frigo lisible"],
    ),
    "c3-s4-stock.html": s.ecran(
        "c3-s4-stock", "24.59", "8.87", "14:45", "PERTES ET MOUVEMENTS",
        "SCENE-4", "vid-scene-4",
        ["Pertes saisies", "Transformations", "Stock relevé"],
    ),
    "c3-s5-tracabilite.html": s.ecran(
        "c3-s5-tracabilite", "33.46", "4.57", "14:55", "MA TRAÇABILITÉ SE REFERME",
        "SCENE-5", "vid-scene-5",
        ["Service tracé", "Coupure pointée"],
    ),
    "c3-s6-soir.html": s.carton(
        "c3-s6-soir", "38.03", "7.14", "cuisine-nuit", "vid-plate-nuit",
        "Vingt-deux heures quinze", "Le vrai travail de fermeture commence",
        amb_opacity=".85", title_at=".5", sub_at="1.2",
    ),
    "c3-s7-nettoyage.html": s.ecran(
        "c3-s7-nettoyage", "45.17", "5.88", "22:30", "MES ZONES DE NETTOYAGE",
        "SCENE-7", "vid-scene-7",
        ["Zone par zone", "Au fur et à mesure"],
    ),
    # Le plan clé du film.
    "c3-s8-photo-ia.html": s.ecran(
        "c3-s8-photo-ia", "51.05", "10.50", "22:40", "UNE PHOTO, L'IA CONTRÔLE",
        "SCENE-8", "vid-scene-8",
        ["Photo envoyée", "Analyse immédiate", "Je peux encore corriger"],
    ),
    "c3-s9-conformite.html": s.ecran(
        "c3-s9-conformite", "61.55", "4.26", "22:45", "CONFORMITÉ ET TEMPÉRATURES",
        "SCENE-9", "vid-scene-9",
        ["Check-list faite", "Dernier relevé"],
    ),
    "c3-s10-sortie.html": s.ecran(
        "c3-s10-sortie", "65.81", "5.19", "23:00", "JE POINTE MA SORTIE",
        "SCENE-10", "vid-scene-10",
        ["Journée écrite", "Rien recopié"],
    ),
    "c3-s11-nuit.html": s.carton(
        "c3-s11-nuit", "71.00", "5.00", "devanture-nuit", "vid-plate-devanture",
        "Ma journée entière est écrite", "Et je n'ai rien recopié",
        amb_opacity=".8", title_at=".3", sub_at=".9",
    ),
}

if __name__ == "__main__":
    s.ecrire(SCENES)
