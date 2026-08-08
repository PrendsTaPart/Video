#!/usr/bin/env python3
"""Génère les 11 scènes de S1 · Salle avant le service.

Premier film du parcours salle : le liseré passe du vert cuisine à l'orange
salle `#F59E0B`. C'est le seul changement de charte — tout le reste de la
grammaire est commun, et vit dans `_serie/serie.py`.

Bornes issues des timings réels de la voix (`assets/transcript.json`) :

   0,00  Neuf heures trente. La salle est vide…
   7,39  Je pointe, je récupère mes tâches…
  11,95  Mes réservations du jour, dans l'ordre…
  18,47  Cette nuit, pendant que personne n'était là, Caroline a décroché…
  29,52  Un appel ce matin, une réservation de plus…
  34,76  Ce soir je suis complet à vingt heures…
  40,68  La six est bancale, je la bloque…
  45,48  Je prépare mon plan de salle…
  51,24  Je vérifie les QR codes de mes tables…
  58,24  Onze heures quinze. Les commandes web sont déjà tombées…
  64,00  Onze heures quarante-cinq. Ma salle est prête…
  68,72  (fin de la voix, le film court jusqu'à 73,30)

La scène des appels est la plus longue du film (11,05 s), et c'est voulu :
c'est le seul plan de toute la série qui montre du travail fait par
quelqu'un d'autre pendant que le restaurant était fermé.
"""

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "_serie"))
from serie import Serie  # noqa: E402

s = Serie(metier=Serie.SALLE, sous="s1")

SCENES = {
    "s1-s1-salle-vide.html": s.carton(
        "s1-s1-salle-vide", "0.00", "7.39", "salle-vide", "vid-plate-salle",
        "Neuf heures trente", "La journée a déjà commencé sans moi",
        title_at=".8", sub_at="1.6",
    ),
    "s1-s2-ouverture.html": s.ecran(
        "s1-s2-ouverture", "7.39", "4.56", "09:30", "J'OUVRE MON POSTE",
        "SCENE-2", "vid-scene-2",
        ["Entrée pointée", "Tâches du jour"],
    ),
    "s1-s3-reservations.html": s.ecran(
        "s1-s3-reservations", "11.95", "6.52", "09:40", "MES RÉSERVATIONS DU JOUR",
        "SCENE-3", "vid-scene-3",
        ["Le nom", "L'heure", "Les couverts", "La table"],
    ),
    # Le plan clé du film.
    "s1-s4-appels.html": s.ecran(
        "s1-s4-appels", "18.47", "11.05", "09:50", "CAROLINE A DÉCROCHÉ CETTE NUIT",
        "SCENE-4", "vid-scene-4",
        ["Appels réécoutés", "Transcription lue", "Rien de perdu"],
    ),
    "s1-s5-ajout.html": s.ecran(
        "s1-s5-ajout", "29.52", "5.24", "10:00", "UNE RÉSERVATION DE PLUS",
        "SCENE-5", "vid-scene-5",
        ["Ajoutée", "Placée dans le service"],
    ),
    "s1-s6-creneaux.html": s.ecran(
        "s1-s6-creneaux", "34.76", "5.92", "10:10", "JE FERME UN CRÉNEAU",
        "SCENE-6", "vid-scene-6",
        ["Complet à 20 h", "Invisible en ligne"],
    ),
    "s1-s7-tables.html": s.ecran(
        "s1-s7-tables", "40.68", "4.80", "10:20", "LA SIX EST BANCALE",
        "SCENE-7", "vid-scene-7",
        ["Table bloquée", "Retirée du plan"],
    ),
    "s1-s8-plan.html": s.ecran(
        "s1-s8-plan", "45.48", "5.76", "10:30", "MON PLAN DE SALLE",
        "SCENE-8", "vid-scene-8",
        ["Qui va où", "Combien de couverts", "Quand ça se libère"],
    ),
    "s1-s9-qrcode.html": s.ecran(
        "s1-s9-qrcode", "51.24", "7.00", "10:40", "LES QR CODES DE MES TABLES",
        "SCENE-9", "vid-scene-9",
        ["QR vérifiés", "Prêts pour le service"],
    ),
    "s1-s10-web.html": s.ecran(
        "s1-s10-web", "58.24", "5.76", "11:15", "LES COMMANDES WEB SONT TOMBÉES",
        "SCENE-10", "vid-scene-10",
        ["Vues avant l'ouverture", "Pas pendant le coup de feu"],
    ),
    "s1-s11-prete.html": s.carton(
        "s1-s11-prete", "64.00", "9.30", "salle-prete", "vid-plate-prete",
        "Ma salle est prête", "Et je n'ai encore vu personne",
        amb_opacity=".9", title_at=".6", sub_at="1.4",
    ),
}

if __name__ == "__main__":
    s.ecrire(SCENES)
