#!/usr/bin/env python3
"""Génère les 13 scènes de S1 · Salle avant le service.

Premier film du parcours salle : le liseré passe du vert cuisine à l'orange
salle `#F59E0B`. C'est le seul changement de charte — le reste de la
grammaire est commun et vit dans `_serie/serie.py`.

**Deux scènes ne sont pas des captures d'écran mais des schémas animés.** Le
retrait d'un plat de la carte et l'ouverture du fond de caisse n'ont aucun
tutoriel filmé : le premier n'a pas de fiche, le second attend le tournage du
module Caisse POS. Les escamoter laissait deux trous dans un parcours qui se
veut exhaustif ; inventer une fausse capture d'écran est interdit par la
règle du projet. Un schéma explicite le mécanisme sans jamais se faire passer
pour l'interface — et dans le cas du retrait de carte, il montre mieux que ne
le ferait une capture ce qui compte vraiment : la **simultanéité** sur les
trois canaux.

Bornes issues des timings réels de la voix (`assets/transcript.json`) :

   0,00  Neuf heures trente. La salle est vide…
   7,97  Je pointe, je récupère mes tâches…
  12,76  Mes réservations du jour, dans l'ordre…
  19,76  Cette nuit, Caroline a décroché…
  30,64  Un appel ce matin, une réservation de plus…
  36,67  Ce soir je suis complet à vingt heures…
  42,73  La six est bancale, je la bloque…
  46,99  Je prépare mon plan de salle…
  53,00  Je vérifie les QR codes de mes tables…
  58,98  Onze heures. Le tartare est en rupture…      (schéma animé)
  66,24  Onze heures quinze. Les commandes web…
  74,36  Onze heures quarante-cinq. J'ouvre mon fond de caisse…  (schéma animé)
  80,96  Ma salle est prête…
  84,40  (fin de la voix, le film court jusqu'à 89,20)
"""

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "_serie"))
from serie import Serie  # noqa: E402

s = Serie(metier=Serie.SALLE, sous="s1")

SCENES = {
    "s1-s1-salle-vide.html": s.carton(
        "s1-s1-salle-vide", "0.00", "7.97", "salle-vide", "vid-plate-salle",
        "Neuf heures trente", "La journée a déjà commencé sans moi",
        title_at=".8", sub_at="1.6",
    ),
    "s1-s2-ouverture.html": s.ecran(
        "s1-s2-ouverture", "7.97", "4.79", "09:30", "J'OUVRE MON POSTE",
        "SCENE-2", "vid-scene-2",
        ["Entrée pointée", "Tâches du jour"],
    ),
    "s1-s3-reservations.html": s.ecran(
        "s1-s3-reservations", "12.76", "7.00", "09:40", "MES RÉSERVATIONS DU JOUR",
        "SCENE-3", "vid-scene-3",
        ["Le nom", "L'heure", "Les couverts", "La table"],
    ),
    # Le plan clé du film.
    "s1-s4-appels.html": s.ecran(
        "s1-s4-appels", "19.76", "10.88", "09:50", "CAROLINE A DÉCROCHÉ CETTE NUIT",
        "SCENE-4", "vid-scene-4",
        ["Appels réécoutés", "Transcription lue", "Rien de perdu"],
    ),
    "s1-s5-ajout.html": s.ecran(
        "s1-s5-ajout", "30.64", "6.03", "10:00", "UNE RÉSERVATION DE PLUS",
        "SCENE-5", "vid-scene-5",
        ["Ajoutée", "Placée dans le service"],
    ),
    "s1-s6-creneaux.html": s.ecran(
        "s1-s6-creneaux", "36.67", "6.06", "10:10", "JE FERME UN CRÉNEAU",
        "SCENE-6", "vid-scene-6",
        ["Complet à 20 h", "Invisible en ligne"],
    ),
    "s1-s7-tables.html": s.ecran(
        "s1-s7-tables", "42.73", "4.26", "10:20", "LA SIX EST BANCALE",
        "SCENE-7", "vid-scene-7",
        ["Table bloquée", "Retirée du plan"],
    ),
    "s1-s8-plan.html": s.ecran(
        "s1-s8-plan", "46.99", "6.01", "10:30", "MON PLAN DE SALLE",
        "SCENE-8", "vid-scene-8",
        ["Qui va où", "Combien de couverts", "Quand ça se libère"],
    ),
    "s1-s9-qrcode.html": s.ecran(
        "s1-s9-qrcode", "53.00", "5.98", "10:40", "LES QR CODES DE MES TABLES",
        "SCENE-9", "vid-scene-9",
        ["QR vérifiés", "Prêts pour le service"],
    ),
    # Schéma animé : aucune fiche n'existe pour le retrait de carte.
    "s1-s10-rupture.html": s.motion_retrait_carte(
        "s1-s10-rupture", "58.98", "7.26", "11:00", "UN PLAT EN RUPTURE",
        "Tartare de bœuf", "19,50 €", ["Site", "Plateformes", "Salle"],
    ),
    "s1-s11-web.html": s.ecran(
        "s1-s11-web", "66.24", "8.12", "11:15", "LES COMMANDES WEB SONT TOMBÉES",
        "SCENE-11", "vid-scene-11",
        ["Vues avant l'ouverture", "Pas pendant le coup de feu"],
    ),
    # Schéma animé : le module Caisse POS n'est pas encore tourné.
    "s1-s12-caisse.html": s.motion_fond_caisse(
        "s1-s12-caisse", "74.36", "6.60", "11:45", "J'OUVRE MON FOND DE CAISSE",
        "150", ["Comptés", "Notés", "Caisse ouverte"],
    ),
    "s1-s13-prete.html": s.carton(
        "s1-s13-prete", "80.96", "8.24", "salle-prete", "vid-plate-prete",
        "Ma salle est prête", "Et je n'ai encore vu personne",
        amb_opacity=".9", title_at=".5", sub_at="1.2",
    ),
}

if __name__ == "__main__":
    s.ecrire(SCENES)
