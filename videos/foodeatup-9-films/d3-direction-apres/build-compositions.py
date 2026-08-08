#!/usr/bin/env python3
"""Génère les 8 scènes de D3 · Direction après le service.

Dernier film de la série. Neuf étapes en sept scènes d'écran : la facture, le
devis et l'e-reporting tiennent dans une seule bobine, parce que la voix les
nomme d'une traite — « trois documents, aucune ressaisie ». Les découper en
trois scènes aurait démenti la phrase.

Bornes issues des timings réels de la voix (`assets/transcript.json`) :

   0,00  Quinze heures. Le service de midi est derrière moi…
   8,51  Une facture. Un devis. Mon e-reporting déclaré…
  17,19  Seize heures. Je pose mes questions à PrediBot…
  26,32  Et quand je ne sais pas quoi demander…
  33,61  Seize heures quarante-cinq. WhatsApp…
  42,49  Dix-sept heures trente. J'exporte mon classeur HACCP…
  50,53  Dix-huit heures. Le chiffre du jour…
  55,65  Ma journée est finie. Le service, lui, continue sans moi.
  59,56  (fin de la voix, le film court jusqu'à 64,30)

⚠️ Les deux plans d'ambiance sont ralentis à 70 % : ce sont des plans fixes
(un portrait tenu, une devanture dont les lumières s'éteignent) où le ralenti
ne se lit pas, et la bibliothèque n'offre aucun plan de direction inutilisé
au registre « avec ». Le seul disponible appartient au registre « sans » et
n'a rien à faire dans ce film.
"""

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "_serie"))
from serie import Serie  # noqa: E402

s = Serie(metier=Serie.DIRECTION, sous="d3")

SCENES = {
    "d3-s1-quinze-heures.html": s.carton(
        "d3-s1-quinze-heures", "0.00", "8.51", "directeur-portrait", "vid-plate-portrait",
        "Quinze heures", "L'heure des choses qu'on repousse toujours",
        title_at=".7", sub_at="1.5",
    ),
    "d3-s2-documents.html": s.ecran(
        "d3-s2-documents", "8.51", "8.68", "15:00", "TROIS DOCUMENTS, AUCUNE RESSAISIE",
        "SCENE-2", "vid-scene-2",
        ["Une facture", "Un devis", "L'e-reporting"],
    ),
    "d3-s3-predibot.html": s.ecran(
        "d3-s3-predibot", "17.19", "9.13", "16:00", "DES QUESTIONS DE PATRON",
        "SCENE-3", "vid-scene-3",
        ["Ce qui marche", "Ce qui coûte", "Ce qu'il faut arrêter"],
    ),
    "d3-s4-marketplace.html": s.ecran(
        "d3-s4-marketplace", "26.32", "7.29", "16:30", "LA MARKETPLACE DE PROMPTS",
        "SCENE-4", "vid-scene-4",
        ["Quelqu'un a déjà posé la question"],
    ),
    "d3-s5-whatsapp.html": s.ecran(
        "d3-s5-whatsapp", "33.61", "8.88", "16:45", "TOUT DEPUIS WHATSAPP",
        "SCENE-5", "vid-scene-5",
        ["Réceptions validées", "Stock piloté", "Aucun compte à créer"],
    ),
    "d3-s6-haccp.html": s.ecran(
        "d3-s6-haccp", "42.49", "8.04", "17:30", "MON CLASSEUR HACCP DU MOIS",
        "SCENE-6", "vid-scene-6",
        ["Tout est déjà dedans", "Je clique"],
    ),
    "d3-s7-chiffre.html": s.ecran(
        "d3-s7-chiffre", "50.53", "5.12", "18:00", "LE CHIFFRE DU JOUR",
        "SCENE-7", "vid-scene-7",
        ["Pas demain matin", "Maintenant"],
    ),
    "d3-s8-fin.html": s.carton(
        "d3-s8-fin", "55.65", "8.65", "devanture-nuit", "vid-plate-devanture",
        "Ma journée est finie", "Le service, lui, continue sans moi",
        amb_opacity=".85", title_at=".5", sub_at="1.3",
    ),
}

if __name__ == "__main__":
    s.ecrire(SCENES)
