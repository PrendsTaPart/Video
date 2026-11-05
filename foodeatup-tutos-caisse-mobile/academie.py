#!/usr/bin/env python3
"""Écrit src/data/fiches-app-caisse-mobile.ts : 3 gestes de la caisse mobile non couverts par les 6 vidéos du 03/11."""
import os, sys
ICI = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(ICI, "..", "outils-tutos"))
from fiches_academie import fiches, titres_academie
from tutos import T
D = sys.argv[1]
X = {
 "reservations-et-attente": ("Voir les réservations du jour depuis le téléphone et installer un client à son arrivée, avec la liste d'attente à côté.", "Installer un client depuis la réservation ouvre sa note sur la bonne table : rien à ressaisir.", "scanner-le-qr-code-de-la-table"),
 "tickets-du-jour": ("Retrouver un ticket du jour par numéro, table ou client, puis le réimprimer ou l'envoyer.", "Le total officiel de la journée reste celui du Z : cette liste sert à retrouver un ticket, pas à compter la caisse.", "encaisser-une-commande"),
 "rapport-x-et-cloture": ("Faire le point de caisse en plein service avec le rapport X, puis clôturer la caisse le soir avec le Z.", "Comptez les espèces avant de clôturer : le Z fige la journée.", "encaisser-une-commande"),
}
cfg = {"export": "fichesAppCaisseMobile", "prefixe_rapido": "foodeatup-", "prefixe_cle": "", "module": "caisse-pos",
       "section": "L'application mobile", "ordre": 41, "app": "l'application FoodEatUp Caisse Mobile", "nom": "FoodEatUp Caisse Mobile", "dossier": ICI,
       "origine": "Écrans réels de l'application 0.21.0 (dépôt PrendsTaPart/foodeatup-caisse-mobile), capturés par son test avec le restaurant fictif « Le Bistrot du Marché ». Gestes non couverts par les 6 vidéos du 03/11/2026."}
titres = titres_academie(D)
for s, (_, _, l) in X.items(): assert l is None or l in titres, l
open(os.path.join(D, "src/data/fiches-app-caisse-mobile.ts"), "w").write(fiches(T, cfg, {"caisse-mobile-" + k: v for k, v in X.items()}, titres))
print("ok")
