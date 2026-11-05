# Caisse mobile : 3 tutoriels pour les gestes que les 6 vidéos du 03/11 ne couvrent pas.
# Écrans : captures du test de l'application (test/screenshots/capture_screens_test.dart,
# restaurant fictif « Le Bistrot du Marché »), recadrées en 9:16 sans rien couper.
W0, H0, PAD = 780, 1688, (950 - 780) / 2
def p(x, y): return round((x + PAD) / 950, 3), round(y / H0, 3)
P = "caisse-mobile-"
T = [
 {"cle": P+"reservations-et-attente", "titre": "Voir les réservations et installer un client", "chef": "mission-table-action.webp",
  "hook": "Les réservations dans la poche",
  "ecrans": [["916-03-accueil.png", *p(390, 1620)], ["916-10-reservations.png", *p(615, 504)]],
  "etapes": ["Touche Résas en bas de l'écran", "Les réservations du jour, heure par heure", "Touche Installer à l'arrivée du client", "La liste d'attente est dans l'onglet voisin"],
  "voix": "[excited] Les réservations, dans ta poche ! Je touche Résas en bas de l'écran : les réservations du jour s'affichent, heure par heure, avec le nombre de couverts. [amazed] Le client arrive ? Je touche Installer. Et la liste d'attente est juste à côté. Le service est fluide, t'as vu ?"},
 {"cle": P+"tickets-du-jour", "titre": "Retrouver et réimprimer un ticket du jour", "chef": "mission-caisse-reussi.webp",
  "hook": "Un ticket retrouvé en 2 secondes",
  "ecrans": [["916-17-tickets-du-jour.png", *p(390, 486)], ["916-22-ticket.png"]],
  "etapes": ["Ouvre Tickets du jour", "Cherche par numéro, table ou client", "Touche le ticket", "Réimprime-le ou envoie-le"],
  "voix": "[excited] Un client a perdu son ticket ? Retrouvé en deux secondes ! J'ouvre Tickets du jour, et je cherche par numéro, par table ou par client. [amazed] Je touche le ticket : il s'affiche en entier, prêt à être réimprimé ou envoyé. Le total officiel reste celui du Z. Pratique, non ?"},
 {"cle": P+"rapport-x-et-cloture", "titre": "Faire le point X et clôturer la caisse", "chef": "mission-caisse-action.webp",
  "hook": "Le point de caisse sans rien fermer",
  "ecrans": [["916-03-accueil.png", *p(570, 720)], ["916-11-session-caisse.png", *p(390, 597)]],
  "etapes": ["Touche Session de caisse", "Rapport X : le point en cours de service", "Rien n'est fermé avec le X", "Clôturer la caisse : le Z du soir"],
  "voix": "[excited] Le point de caisse, sans rien fermer ! Je touche Session de caisse : poste, heure d'ouverture et fond de caisse. [amazed] Le rapport X fait le point en plein service, sans rien fermer. Le soir, après avoir compté les espèces, je touche Clôturer la caisse : c'est le Z. Simple et carré !"},
]
for v in T: v["ecran_vignette"] = v["ecrans"][1][0]
