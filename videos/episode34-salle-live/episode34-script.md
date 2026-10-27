# Épisode 34/365 : « J'ai imaginé une salle de restaurant intelligente avec l'IA »

120 s · 9:16 · 1080 × 1920 · voix Noé (ElevenLabs `7pDdnNI6PhXmAp0pXFZm`, eleven_multilingual_v2, 72,6 s) · narration à la première personne.

## Narration

Aujourd'hui, un restaurateur m'a posé une question intéressante : comment savoir combien de temps ses clients restent à table, et comment améliorer la rotation de sa salle ?

Et là, j'ai eu une idée : pourquoi ne pas créer un plan de salle intelligent, capable de montrer en direct quelles tables sont libres, lesquelles sont occupées, et lesquelles doivent être débarrassées ?

Le plus intéressant, c'est de pouvoir suivre la durée d'occupation des tables. Avec ces informations, le restaurateur peut mieux comprendre son service, repérer les temps d'attente et analyser la rotation de ses places.

J'ai imaginé un système qui combine des caméras capables d'analyser la salle localement, des QR codes sur les tables, et les informations de la caisse FoodEatUp. L'objectif : réunir les événements utiles, sans suivre individuellement les clients.

L'idée, ce n'est pas seulement de regarder des couleurs. C'est aussi d'aider les équipes à agir : identifier une table à débarrasser, suivre les alertes, et avoir une meilleure visibilité pendant le service.

Et j'ai voulu aller plus loin : utiliser les historiques, les réservations et les prévisions d'affluence, pour aider le restaurateur à anticiper ses besoins en personnel et mieux organiser son service.

Pour transformer cette idée en application, j'ai utilisé Lovable, GitHub et l'écosystème FoodEatUp. En quelques itérations, j'ai construit une interface, un plan de salle interactif, et une démonstration du fonctionnement imaginé.

Et demain, je présente tout ça au restaurateur. Maintenant, la vraie question, c'est : est-ce que cette solution va répondre à son besoin ? Je vous montrerai la suite.

## Storyboard (`episode34-storyboard.jpg`)

| Temps | Image | Mention à l'écran |
|---|---|---|
| 0–12 s | Horloge, bulle avec la question, titre « COMMENT OPTIMISER LE ROULEMENT DES TABLES ? », démo 3D floutée en fond | — |
| 12–27 s | Démo 3D réelle : étapes 1 → 2 → 4 → 7 (vert → rouge → orange), légende des 4 couleurs | « Vraie démo publique Salle Live · scénario de démonstration, pas un vrai service » |
| 27–45 s | Plan 2D de la démo (0 % → 17 % → 92 % de remplissage, durées par table), zoom compteurs, flux d'événements JSON | « Chiffres de la démo… pas des mesures d'un restaurant » |
| 45–63 s | Schéma Caméra / QR / Caisse FoodEatUp → Salle Live, les 3 étapes du site, « 0 image enregistrée » | Caméra « imaginé », QR « codé », FoodEatUp « connexion codée · synchro à faire » ; « Aucune caméra installée à ce jour » |
| 63–80 s | Démo 3D étape 6 + les 7 règles d'alerte réelles du code | « Règles réelles du code · pas encore de données réelles » |
| 80–96 s | Extrait de `src/lib/forecast.ts`, texte réel de la page Planning IA, 3 fonctions | « Prévisionnel · aucun historique réel encore · aucun gain chiffré promis » |
| 96–110 s | Logos Lovable / GitHub / FoodEatUp, dépôt layout-manager-ai, fait / à faire | « Prototype en cours de validation client » |
| 110–120 s | Portrait, ÉPISODE 34/365 · SALLE LIVE × FOODEATUP · DÉMO CLIENT DEMAIN | — |

Short 45 s : problème (0–7,6) · idée (12,2–20,7) · durée (27,2–36,7) · alertes (63,2–72,6) · fin (110,2–120).
