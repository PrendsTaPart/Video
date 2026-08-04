# Tutoriel — Historique de la production et traçabilité

Dossier Drive « Tracer ses productions — Historique ». Rush source : 52,84 s,
1920x828, 25 fps.

## Voix off (12 lignes, Adam FR `TGAegA0zNRi8I6nUdq3i`)

| # | Texte | Segment |
|---|---|---|
| N0 | Retrouver l'historique complet de vos productions ? Tout se passe dans Mes productions. | carte intro |
| N1 | Ici, vous voyez d'un coup d'œil le total, les productions en attente, prêtes à produire et déjà réalisées. | A |
| N2 | Filtrez par statut pour isoler celles qui attendent encore des ingrédients. | clic B + C |
| N3 | Ou celles qui sont prêtes à produire, avec leur progression et le nombre d'ingrédients manquants. | D |
| N4 | Sur une production réalisée, le bouton Voir la traçabilité ouvre tout l'historique du plat. | E |
| N5 | Une recette précise à retrouver ? Tapez son nom dans la recherche. | F |
| N6 | Choisissez une date de début et une date de fin, puis cliquez sur Appliquer. | clic G + H |
| N7 | Vous obtenez l'historique exact de la période, et vous pouvez l'exporter en PDF. | clic I + J |
| N8 | De quoi justifier chaque production en cas de contrôle sanitaire, sans fouiller dans vos classeurs. | K (bénéfice) |
| N9 | Vous pouvez aussi le faire depuis Claude : copiez ce prompt, remplacez les crochets. | étages 1+2 (réutilisé de `tva/N6`) |
| N10 | Collez-le dans la conversation : votre historique de production remonte en quelques secondes. | étage 3 |
| N11 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | carte de fin (réutilisé de `tva/N8`) |

N9 et N11 réutilisés tels quels (règle du workflow) ; N10 est spécifique au tutoriel
(il nomme l'objet remonté par Claude — ne jamais le copier tel quel d'un autre tuto).

## Découpage (timeline du rush)

| Seg | Source | Sortie | Contenu |
|---|---|---:|---|
| intro | carte | 3,00 s | TRACER SES PRODUCTIONS — HISTORIQUE |
| A | 0,30 → 5,20 | 5,60 s | page Mes productions : 4 compteurs (Total 532 / En attente 81 / Prêts 116 / Réalisés 204) + scroll sur les cartes |
| B | 7,30 → 7,65 | 0,90 s | **zoom-punch** sur le sélecteur de statut (1139, 197) |
| C | 7,70 → 10,50 | 4,40 s | statut « En attente d'ingrédients » — 81 productions |
| D | 10,60 → 13,60 | 5,40 s | statut « Prêt à produire » — 116, progression, ingrédients manquants, Valider la production |
| E | 13,90 → 21,40 | 5,20 s | statut « Réalisée » — 204, bouton Voir la traçabilité |
| F | 21,60 → 26,60 | 4,40 s | recherche par nom de recette (« a » → 185) puis effacement |
| G | 27,75 → 28,10 | 0,90 s | **zoom-punch** sur le filtre de dates (1675, 197) |
| H | 28,20 → 38,80 | 4,60 s | panneau de période : date de début, date de fin, raccourcis |
| I | 38,80 → 39,15 | 0,90 s | **zoom-punch** sur Appliquer (1675, 421) |
| J | 39,20 → 44,60 | 4,00 s | 2 productions sur la période, badge « 27 juil. - 2 août 2026 » |
| K | 44,60 → 52,80 | 5,00 s | autres périodes (30/06→30/07 = 4, puis 29 janv. 2027 = 29) |
| claude1 | carte générée | 6,00 s | reveal — prompt en gros, fond crème |
| claude2 | carte générée | 3,00 s | « Copié dans le presse-papiers ! » |
| claude3 | carte générée | 6,00 s | mockup chatbot Claude |
| outro | carte | 6,20 s (auto-étendue) | CTA |

Coordonnées des 3 boutons mesurées par seuillage colorimétrique sur les frames réelles
(`work/frames/`), pas à l'œil. Les instants de clic ont été localisés à 0,2 s près en
suivant le changement de valeur du compteur « Total » (532 → 81 à 7,60 s ; 204 → 2 à
39,00 s) et l'apparition du panneau de dates (28,20 s).

## Séquence Claude — module partagé

`mcp__FoodEatUp__list_production_plans(establishment_id, start_date, end_date, status)`
recouvre exactement ce que montre le rush : filtre par statut **et** par période. Prompt :

> Liste mes productions au statut [statut] entre le [date de début] et le [date de fin]
> pour mon établissement FoodEatUp (ID [ID établissement]).

Même texte côté fiche Lovable (premier `claudePrompts[]`). Second prompt côté site
uniquement (`list_top_productions`, pas montré à l'écran donc pas dans la vidéo) :

> Quels sont les plats que j'ai le plus produits ces [nombre] derniers jours dans mon
> établissement FoodEatUp (ID [ID établissement]) ?

## Animations

Mêmes principes que toute la série : Ken Burns sur les cartes, xfade 0,28 s, bandeaux
d'étape (aucune apostrophe — bug `drawtext` connu), encadré orange pulsant sur les
3 clics, `setpts` pour la vitesse (jamais `zoompan` sur du rush).

## Statut publication

Vidéo livrée à Michael + fiche publiée sur le site Lovable FoodEatUp Academy
(module `haccp`).
