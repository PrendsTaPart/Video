# Boucle 04 — HACCP

Slug : `boucle-04-haccp` · Durée cible 85 s · Agent : Jarvis.
Registre sobre : pas de gag, pas d'emballement visuel — c'est la boucle qui coûte
la fermeture, pas de la marge.

## Voix off (verbatim — ne pas réécrire)

Le contrôleur pousse la porte un mardi, à onze heures. Vous cherchez le classeur. Les
relevés du mois dernier ont été remplis d'un coup, la veille, de mémoire. Vous le savez.
Lui aussi.

"Frigo un : trois degrés."

Vous l'avez dit en cuisine, les mains prises. C'est enregistré, horodaté, rattaché à
l'équipement. Et si la valeur sort des limites — quatre degrés en froid positif, moins
dix-huit en congélation — l'anomalie remonte tout de suite, avec l'action corrective.

FoodEatUp ne remplit jamais un relevé à votre place : une température se mesure, elle ne
s'invente pas. Ce qu'il fait, c'est compter les trous. Les jours sans relevé. Les
livraisons sans contrôle à réception. Les zones jamais nettoyées.

"La livraison Metro est arrivée, tout est conforme." Le contrôle est validé, les
températures notées, le stock entré. La même phrase alimente StockVisionAI.

Résultat : un dossier horodaté, exportable en un clic.

Les sept autres boucles coûtent de la marge. Celle-ci coûte la fermeture.

## Squelette 7 plans

| # | Rôle |
|---|------|
| 1 | Le problème : contrôleur, mardi 11h, classeur, relevés remplis de mémoire la veille. |
| 2 | La phrase dite en cuisine, en gros : « Frigo un : trois degrés. » |
| 3 | (le plus long) Cascade : Plan de maîtrise → Relevés de températures → Contrôles à réception → Étiquetage DLC → Checklists → Plan de nettoyage → Journal quotidien → Action corrective. Calendrier du mois en overlay : jours sans relevé en cellule vide/pointillée, jours couverts en bleu plein — jamais de rouge (hors palette). |
| 4 | Score de complétude calculé (« 87 % — 4 jours sans relevé sur frigo 2 »). Texte à l'écran : un jour sans relevé est « non conforme », pas « probablement fait ». |
| 5 | Une seule boucle voisine s'allume : StockVisionAI. |
| 6 | Chiffres : dossier horodaté exportable en 1 clic · anomalie détectée le jour même. |
| 7 | « La seule boucle dont l'échec n'est pas financier, mais existentiel. » Preuve : 17 outils MCP. |

## Assets à réutiliser

- `mascots/chef-haccp.png` — agent Jarvis / HACCP (plan 2).
- `product-screenshots/etiqueteuse-dlc.png`, `ajouter-zone-nettoyage.png`,
  `controle-reception-manuel.png` — à intégrer si un plan a besoin d'un écran réel.
- Pas de nouveau visuel RapidoCMS prévu a priori (pas de plat en scène) — réévaluer
  pendant la construction du plan 1 (classeur/thermomètre) si un visuel dédié aide.

## Statut
`script` (VO pas encore générée).
