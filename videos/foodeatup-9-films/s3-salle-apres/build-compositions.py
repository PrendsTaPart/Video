#!/usr/bin/env python3
"""Génère les 8 scènes de S3 · Salle après le service.

Le film le plus court de la série (61,40 s) et le plus pauvre en captures :
trois de ses sept étapes relèvent du module Caisse POS, qui n'est pas tourné.
Chacune est traitée selon ce qu'elle est, pas selon ce qui manque :

- **les deux clôtures** passent sur un plan tourné — l'imprimante thermique
  qui déroule le ticket Z. Le ticket Z est un objet physique ; un plan réel
  vaut mieux qu'un schéma, et il dit la même chose plus vite ;
- **les écarts de caisse** passent en schéma animé, parce que le sujet est un
  rapprochement de chiffres, que rien ne filme.

Le même plan de ticket Z sert aux deux clôtures. C'est délibéré : la voix dit
« deuxième clôture, même geste, même ticket ». Remonter un plan différent
aurait contredit le texte.

Bornes issues des timings réels de la voix (`assets/transcript.json`) :

   0,00  Quatorze heures trente. Le dernier client de midi est parti…
   5,67  Je clôture. Le ticket Z sort…                    (plan tourné)
  13,86  Je compte mon tiroir. Deux euros de moins…       (schéma animé)
  22,77  Je pointe mes zones de nettoyage… puis ma coupure
  28,88  Vingt-deux heures trente. Deuxième clôture…      (plan tourné)
  36,68  Vingt-deux heures quarante-cinq. Les avis…
  46,60  Vingt-trois heures. Je pointe ma sortie…
  56,42  (fin de la voix, le film court jusqu'à 61,40)
"""

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "_serie"))
from serie import Serie  # noqa: E402

s = Serie(metier=Serie.SALLE, sous="s3")

SCENES = {
    "s3-s1-fin-midi.html": s.carton(
        "s3-s1-fin-midi", "0.00", "5.67", "salle-apres-midi", "vid-plate-apres",
        "Quatorze heures trente", "Le dernier client de midi est parti",
        title_at=".5", sub_at="1.2",
    ),
    "s3-s2-ticket-z.html": s.carton(
        "s3-s2-ticket-z", "5.67", "8.19", "ticket-z", "vid-plate-z-midi",
        "Le ticket Z", "Salle, comptoir, en ligne, livraison — un seul total",
        amb_opacity=".92", title_at=".6", sub_at="1.4",
    ),
    "s3-s3-ecarts.html": s.motion_ecart(
        "s3-s3-ecarts", "13.86", "8.91", "14:40", "JE COMPTE MON TIROIR",
        [("Théorique", "1 248,50 €"), ("Compté", "1 246,50 €")],
        "Écart : − 2,00 €",
        ["Écrit", "Daté", "Plus à chercher"],
    ),
    "s3-s4-nettoyage.html": s.ecran(
        "s3-s4-nettoyage", "22.77", "6.11", "15:00", "MES ZONES DE NETTOYAGE",
        "SCENE-4", "vid-scene-4",
        ["Zone par zone", "Coupure pointée"],
    ),
    # Même plan que la scène 2 : la voix dit « même geste, même ticket ».
    "s3-s5-ticket-z-soir.html": s.carton(
        "s3-s5-ticket-z-soir", "28.88", "7.80", "ticket-z", "vid-plate-z-soir",
        "Deuxième clôture", "La journée entière sur une seule ligne",
        amb_opacity=".92", title_at=".5", sub_at="1.3",
    ),
    "s3-s6-avis.html": s.ecran(
        "s3-s6-avis", "36.68", "9.92", "22:45", "LES AVIS DE LA JOURNÉE",
        "SCENE-6", "vid-scene-6",
        ["Tous au même endroit", "Je réponds ce soir", "Je m'en souviens encore"],
    ),
    "s3-s7-sortie.html": s.ecran(
        "s3-s7-sortie", "46.60", "4.90", "23:00", "JE POINTE MA SORTIE",
        "SCENE-7", "vid-scene-7",
        ["Caisse juste", "Avis traités"],
    ),
    "s3-s8-fermeture.html": s.carton(
        "s3-s8-fermeture", "51.50", "9.90", "serveur-fermeture", "vid-plate-fermeture",
        "Demain matin, personne ne cherchera", "Ce qui s'est passé ce soir",
        amb_opacity=".88", title_at=".6", sub_at="1.5",
    ),
}

if __name__ == "__main__":
    s.ecrire(SCENES)
