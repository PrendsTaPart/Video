#!/usr/bin/env python3
"""Génère les 11 scènes de S2 · Salle pendant le service.

Liseré salle `#F59E0B`. La scène 7 n'est pas une capture d'écran mais un
schéma animé : les trois étapes du module Caisse POS — encaisser, séparer
l'addition, appliquer la remise — n'ont aucun tutoriel tourné, et la voix les
nomme dans la même respiration. Une seule note à l'écran, trois gestes
dessus, plutôt que trois scènes de deux secondes.

Bornes issues des timings réels de la voix (`assets/transcript.json`) :

   0,00  Midi. Premier client…
   2,15  Je le place, la table passe en occupée…
   7,10  Le client scanne le QR de sa table…
  13,04  Toutes mes commandes, dans une seule file…
  21,52  Une commande de livraison tombe…
  28,59  Treize heures. Deux couverts qui ne viendront pas…
  35,56  Au comptoir j'encaisse…                        (schéma animé)
  44,39  J'inscris un client à la fidélité…
  50,96  Et je valide une récompense…
  54,02  Dix-huit heures trente. Je reprends mes réservations…
  59,94  Le deuxième service commence…
  63,44  (fin de la voix, le film court jusqu'à 68,40)

Le carton d'ouverture ne dure que 2,15 s : c'est un film de service, la voix
attaque immédiatement sur l'action et le titre doit s'effacer devant elle.
"""

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "_serie"))
from serie import Serie  # noqa: E402

s = Serie(metier=Serie.SALLE, sous="s2")

SCENES = {
    "s2-s1-midi.html": s.carton(
        "s2-s1-midi", "0.00", "2.15", "serveur-accueil", "vid-plate-accueil",
        "Midi", "Premier client",
        title_at=".1", sub_at=".55",
    ),
    "s2-s2-placer.html": s.ecran(
        "s2-s2-placer", "2.15", "4.95", "12:00", "JE PLACE MON PREMIER CLIENT",
        "SCENE-2", "vid-scene-2",
        ["Table occupée", "Commande rattachée"],
    ),
    "s2-s3-qr.html": s.ecran(
        "s2-s3-qr", "7.10", "5.94", "12:05", "LE CLIENT COMMANDE LUI-MÊME",
        "SCENE-3", "vid-scene-3",
        ["QR scanné", "Direct en cuisine"],
    ),
    "s2-s4-canaux.html": s.ecran(
        "s2-s4-canaux", "13.04", "8.48", "12:15", "UNE SEULE FILE",
        "SCENE-4", "vid-scene-4",
        ["Salle", "Comptoir", "Site", "Livraison"],
    ),
    "s2-s5-livraison.html": s.ecran(
        "s2-s5-livraison", "21.52", "7.07", "12:30", "UNE LIVRAISON TOMBE",
        "SCENE-5", "vid-scene-5",
        ["Même file", "Même horloge", "Rien à recopier"],
    ),
    "s2-s6-noshow.html": s.ecran(
        "s2-s6-noshow", "28.59", "6.97", "13:00", "DEUX COUVERTS QUI NE VIENDRONT PAS",
        "SCENE-6", "vid-scene-6",
        ["No-show", "Table libérée"],
    ),
    # Schéma animé : les trois étapes de caisse n'ont aucun tutoriel tourné.
    "s2-s7-note.html": s.motion_note(
        "s2-s7-note", "35.56", "8.83", "13:30", "UNE NOTE, TROIS GESTES",
        "Table 7",
        [("2 × Menu du jour", "36,00 €"), ("3 × Verre de vin", "18,00 €"), ("1 × Café", "2,50 €")],
        "56,50 €", ["18,83 €", "18,83 €", "18,84 €"], "− 20 % midi",
    ),
    "s2-s8-fidelite.html": s.ecran(
        "s2-s8-fidelite", "44.39", "6.57", "13:50", "J'INSCRIS UN CLIENT",
        "SCENE-8", "vid-scene-8",
        ["Des points", "Pas une carte en carton"],
    ),
    "s2-s9-recompense.html": s.ecran(
        "s2-s9-recompense", "50.96", "3.06", "14:00", "UNE RÉCOMPENSE VALIDÉE",
        "SCENE-9", "vid-scene-9",
        ["Validée en salle"],
    ),
    "s2-s10-soir.html": s.ecran(
        "s2-s10-soir", "54.02", "5.92", "18:30", "MES RÉSERVATIONS DU SOIR",
        "SCENE-10", "vid-scene-10",
        ["Reprises", "Clients replacés"],
    ),
    "s2-s11-service.html": s.carton(
        "s2-s11-service", "59.94", "8.46", "salle-service", "vid-plate-service",
        "Le deuxième service commence", "Et la salle sait déjà où elle va",
        amb_opacity=".85", title_at=".5", sub_at="1.2",
    ),
}

if __name__ == "__main__":
    s.ecrire(SCENES)
