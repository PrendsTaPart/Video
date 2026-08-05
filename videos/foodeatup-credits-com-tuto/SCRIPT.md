# Tutoriel — Suivre ses crédits SMS & WhatsApp (module Marketing, Fidélité & Iris)

Catalogue 157 tutoriels, module `marketing-fidelite` (item 10 : « Suivre ses **Crédits**
SMS & WhatsApp »). Correspond au slug déjà présent sur Lovable
`suivre-ses-credits-sms-whatsapp` (stub `order: 9` — attention, le champ `subcategory`
existant dit « 10 · WhatsApp, SMS & crédits », à conserver tel quel, ne pas le renuméroter).
Deuxième vidéo produite pour ce module (9/24 avant celle-ci). Rush source :
`assets/screen.mp4`, 1920x828, 25 fps, 22,44 s. Intrants fournis par Michael :
`assets/intro.jpg` (carte « SUIVI DES CRÉDITS COM »), `assets/outro.jpg` (carte CTA,
identique aux autres tutos).

## Ce que montre le rush

Écran de lecture seule (page Abonnement, défilement continu vers la section crédits) :

1. `0-3s` — Page Abonnement (comparatif des packs StockVision, plan actuel affiché).
2. `3-8s` — Défilement : comparatif détaillé des fonctionnalités par pack, puis les
   options d'agents IA additionnels (Caroline — agent vocal 79€/mois, PrediBot — assistant
   WhatsApp 49€/mois, PrediBot établissement supplémentaire, Avis & réputation Google,
   Iris — agent IA de communication).
3. `8-14s` — Section **Mes crédits & minutes** : *Quota du mois* (1500/1500 crédits,
   réinitialisé le 31 août, non reporté, total mobilisable = 1539 crédits disponibles) ;
   *Achats & dotations* (packs et dotations consommés après le quota du mois, ex. plusieurs
   « Geste commercial — 3/3 » avec dates d'expiration) ; *Minutes voix* (Caroline 0/200 min,
   Jarvis 0/0 min — le service ne coupe jamais en cours de mois, les dépassements sont
   régularisés au cycle suivant).
4. `14-20s` — Boutons de recharge à l'unité (+1000 · 59€, +2000 · 112€, +3000 · 166€,
   +4000 · 219€, +5000 · 271€, +10000 · 531€).
5. `20-22,4s` — Titre **Pack annuel intégral** (tout le catalogue pour chaque site, tarif
   dégressif selon le nombre d'établissements, annuel uniquement) — rush s'arrête au début
   de cette section.

## Séquence Claude — aucun outil MCP ne correspond

Aucun outil `mcp__Foodeatup__*` ne lit le solde de crédits, les dotations ou les minutes
voix consommées (ce sont des données de facturation/abonnement, pas des entités métier
exposées par le MCP). Pas de prompt inventé, conformément à la règle du pipeline — même
raisonnement que `creer-son-code-pin` ou `generer-qr-code-pointage`. Pas de séquence
animée en fin de vidéo ; le script reste sur le contenu à l'écran jusqu'à la carte de fin.

## Voix off proposée (7 lignes) — À VALIDER AVANT GÉNÉRATION AUDIO

| # | Texte | Ancrage |
|---|---|---|
| N0 | Suivre ses crédits Com sur FoodEatUp ? Un seul écran pour tout voir. | carte d'intro |
| N1 | Depuis Abonnement, descendez jusqu'à la section Mes crédits et minutes. | navigation + défilement |
| N2 | Votre quota du mois s'affiche en premier : quinze cents crédits, réinitialisés chaque mois, jamais reportés. | Quota du mois |
| N3 | Une fois le quota épuisé, les packs et dotations achetés prennent le relais, chacun avec sa date d'expiration. | Achats & dotations |
| N4 | Vos minutes voix Caroline et Jarvis sont suivies à part : le service ne coupe jamais en cours de mois, les dépassements se régularisent au cycle suivant. | Minutes voix |
| N5 | Besoin de plus ? Rechargez en un clic par palier, ou passez au pack annuel intégral si vous consommez beaucoup. | boutons de recharge + pack annuel |
| N6 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | carte de fin (CTA, réutilisable tel quel, mp3 copié) |

N6 : texte strictement identique au reste de la série, copie directe du `.mp3` existant
(0 crédit ElevenLabs). N0 à N5 sont spécifiques à cette vidéo → 6 lignes à générer.

## Statut

Script en attente de validation (STOP obligatoire du pipeline avant génération audio
ElevenLabs — voir `FOODEATUP-TUTORIELS-WORKFLOW.md`).
