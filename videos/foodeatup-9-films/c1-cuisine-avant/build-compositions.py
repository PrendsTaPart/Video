#!/usr/bin/env python3
"""Génère les 8 scènes de C1 · Cuisine avant le service.

La grammaire de la série (charte, cadre, coches, fond animé, et les trois
pièges GSAP/HyperFrames payés une fois) vit dans `_serie/serie.py`, partagée
par les 9 films. Ici ne restent que les scènes propres à C1.

Sortie : studio-video/compositions/c1/*.html — versionnés, HyperFrames les
lit ; les régénérer ne doit jamais être nécessaire pour rendre le film.
"""

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "_serie"))
from serie import Serie  # noqa: E402

s = Serie(metier=Serie.CUISINE, sous="c1")

SCENES = {
    "c1-s1-ouverture.html": s.carton(
        "c1-s1-ouverture", "0.00", "4.61", "cuisine-vide", "vid-plate-cuisine",
        "Sept heures", "Dans quatre heures, tout doit être prêt",
    ),
    "c1-s2-ouverture-poste.html": s.ecran(
        "c1-s2-ouverture-poste", "4.61", "12.77", "07:00", "J'OUVRE MON POSTE",
        "SCENE-2", "vid-scene-2",
        ["Entrée pointée", "Tâches du jour", "Températures relevées"],
    ),
    "c1-s3-reception.html": s.ecran(
        "c1-s3-reception", "17.38", "16.13", "07:15", "LA LIVRAISON ARRIVE",
        "SCENE-3", "vid-scene-3",
        ["Réception validée", "EAN et DLC scannés", "Facture au scan", "Prix à jour"],
    ),
    "c1-s4-jarvis.html": s.ecran(
        "c1-s4-jarvis", "33.51", "9.78", "07:25", "JE PARLE, LE STOCK SUIT",
        "SCENE-4", "vid-scene-4",
        ["Sortie dictée", "Stock décrémenté"],
    ),
    "c1-s5-production.html": s.ecran(
        "c1-s5-production", "43.29", "8.47", "07:30", "MA PRODUCTION DU JOUR",
        "SCENE-5", "vid-scene-5",
        ["Fiches techniques", "Liste imprimée"],
    ),
    "c1-s6-etiquetage.html": s.ecran(
        "c1-s6-etiquetage", "51.76", "10.15", "08:30", "CHAQUE PRÉPARATION, SON ÉTIQUETTE",
        "SCENE-6", "vid-scene-6",
        ["Étiquettes générées", "DLC et allergènes", "Historique gardé"],
    ),
    "c1-s7-validation.html": s.ecran(
        "c1-s7-validation", "61.91", "8.97", "11:00", "JE VALIDE ET JE SONDE",
        "SCENE-7", "vid-scene-7",
        ["Production validée", "Plats sondés", "Matinée tracée"],
    ),
    "c1-s8-cta.html": s.carton(
        "c1-s8-cta", "70.88", "4.5", "chef-portrait", "vid-plate-chef",
        "Ma matinée est tracée", "Je n'ai pas ouvert un seul classeur",
        amb_opacity=".62", title_at=".35", sub_at=".85",
    ),
}

if __name__ == "__main__":
    s.ecrire(SCENES)
