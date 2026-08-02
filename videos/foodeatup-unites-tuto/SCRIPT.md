# Tutoriel — Régler ses unités de mesure FoodEatUp

Dossier Drive « Configuration de ces unités ». Durée livrée : **30,5 s** — H.264
High/yuv420p, AAC 48 kHz stéréo, faststart. Audio : true peak **-7,2 dBFS**. Decode
0 erreur, moov avant mdat (faststart confirmé).

**Rebuild** : un v1 pré-existant avait déjà été committé sur cette branche lors d'une
session antérieure (concat simple sans xfade, loudnorm global au lieu de par ligne,
`alimiter` sans `level=disabled`, `-shortest`) — mêmes bugs déjà corrigés sur les autres
vidéos de la série. Son `intro.jpg` était aussi une version antérieure (titre
« Configurer ses unités de mesure », photo costume-cravate) remplacée depuis par Michael
par l'asset actuel (« Régler ses unités de mesure », photo chef). Reconstruit intégralement
sur le pipeline actuel avec les nouveaux assets.

## Pas de séquence Claude sur cette vidéo

Vérifié : `mcp__FoodEatUp__*` n'expose que `list_units` (référentiel global, lecture
seule) — aucun outil `create_unit`/`add_unit`. Pas d'équivalent MCP pour créer une unité
de mesure personnalisée, donc pas de séquence "Utilisez cette fonctionnalité avec
Claude" sur cette vidéo (règle : ne jamais inventer de prompt sans outil correspondant).

## Voix off (6 lignes)

| # | Texte | Durée | Ancrage |
|---|---|---:|---|
| N0 | Régler vos unités de mesure sur FoodEatUp, en quelques secondes. | 3,06 s | carte d'intro |
| N1 | Cliquez sur Ajouter une unité pour en créer une nouvelle. | 3,06 s | clic Ajouter une unité |
| N2 | Donnez-lui un nom, une abréviation, et si besoin un facteur de conversion vers une unité de base. | 5,69 s | formulaire (nom/abréviation/facteur/base) |
| N3 | Cliquez sur Créer l'unité : elle apparaît aussitôt dans votre liste. | 3,89 s | clic Créer l'unité → succès |
| N4 | Ces unités serviront ensuite pour vos ingrédients et vos recettes — par exemple, une gousse de vanille. | 5,46 s | bénéfice (précision de Michael sur l'usage aval) |
| N5 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | 5,02 s | carte de fin (CTA, réutilisé) |

N5 réutilisé tel quel depuis `foodeatup-tva-tuto/vo/N8.mp3` (CTA générique, texte
identique — zéro crédit ElevenLabs dépensé).

## Découpage

| Seg | Source | Sortie | Contenu |
|---|---|---:|---|
| intro | carte | 3,00 s | RÉGLER SES UNITÉS DE MESURE |
| A | 0,20 → 2,60 | 2,90 s | « Mes unités », liste existante (Cc, Cs, G, Kg, L, Ml, Pcs) |
| B | 2,60 → 2,90 | 0,90 s | **zoom-punch** sur Ajouter une unité (1619, 367) |
| C | 4,00 → 20,00 | 9,00 s | nom « Centilitre », abréviation « cl », facteur, unité de base « ml » |
| D | 20,00 → 20,30 | 0,90 s | **zoom-punch** sur Créer l'unité (1024, 748) |
| E | 20,30 → 33,28 | 4,00 s | toast « Unité créée avec succès ! » + liste mise à jour (8 unités) |
| outro | carte | ~11,3 s (auto-étendue) | CTA |

Coordonnées des boutons mesurées par seuillage colorimétrique sur les frames réelles
(script Python, pas à l'œil) — voir `build.py`.

## Animations

Mêmes principes que toute la série : Ken Burns sur les cartes, xfade (0,28 s), bandeaux
d'étape, encadré orange pulsant sur les 2 clics. Pas de clip avatar dans ce dossier.

## Statut publication

Validation demandée par Michael dans le même message que la livraison des rushs suivants
(pas de retour explicite distinct attendu vu la formulation directe "réalise la
publication") — publication effectuée.
