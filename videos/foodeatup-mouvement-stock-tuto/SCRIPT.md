# Tutoriel — Saisir un mouvement de stock FoodEatUp

Module StockVision AI, dossier Drive « Ajouter et modifier un mouvement ».
Durée livrée : **52,2 s** — H.264 High/yuv420p, AAC 48 kHz stéréo, faststart.
Audio : true peak **-7,3 dBFS** (mesuré sur le MP4 final). Decode 0 erreur,
moov avant mdat (faststart confirmé).

## Ce que montre le rush

Première vidéo de la série à couvrir **deux actions dans un seul rush** : la
création d'un mouvement de stock **puis sa correction**. D'où 12 lignes de voix
off (au lieu des 9 habituelles) et 6 zoom-punches (au lieu de 2).

1. Gestion des stocks → bouton « Mouvement de stock » (pilule orange).
2. Page « Mouvements de Stock », vide → « + Ajouter un mouvement ».
3. Modal : produit Chocolat, type **Entrée**, quantité 3000, unité pièce,
   motif « Réception commande », fournisseur Carrefour → « Ajouter ».
4. Toast « Mouvement de stock enregistré avec succès », la ligne apparaît dans
   l'historique (Chocolat / Entrée / 3000 pièce / 23-07-2026 / dupont jean).
5. Menu Action (⋮) de la ligne → **Modifier** → même modal, pré-rempli.
6. Quantité 3000 → 5000 → « Ajouter » → toast « Mouvement de stock modifié
   avec succès », la liste affiche 5000 pièce.

Le menu Action expose aussi « Voir détails » et « Supprimer » — visibles à
l'écran mais non utilisés dans le rush, donc non commentés en voix off.

## Voix off (12 lignes)

| # | Texte | Durée | Ancrage |
|---|---|---:|---|
| N0 | Saisir un mouvement de stock sur FoodEatUp, en quelques clics. | 3,16 s | carte d'intro |
| N1 | Depuis la gestion des stocks, cliquez sur Mouvement de stock. | 3,00 s | A + clic B |
| N2 | Puis sur Ajouter un mouvement, pour ouvrir le formulaire. | 3,16 s | C + clic D |
| N3 | Choisissez le produit, le type entrée ou sortie, et la quantité. | 3,71 s | E |
| N4 | Complétez l'unité, le motif et le fournisseur, puis cliquez sur Ajouter. | 4,21 s | F + clic G |
| N5 | Le mouvement est enregistré, et apparaît aussitôt dans votre historique. | 3,76 s | H |
| N6 | Une erreur de saisie ? Ouvrez le menu Action, puis Modifier. | 3,47 s | clics I + J |
| N7 | Corrigez la quantité et validez : votre stock est mis à jour immédiatement. | 4,31 s | K + clic L |
| N8 | Chaque entrée et chaque sortie nourrit StockVision AI, pour un inventaire toujours juste. | 4,78 s | M (bénéfice) |
| N9 | Vous pouvez aussi le faire depuis Claude : copiez ce prompt, remplacez les crochets. | 4,41 s | **étages 1+2** |
| N10 | Collez-le dans la conversation : votre mouvement de stock est enregistré en quelques secondes. | 4,86 s | **étage 3** |
| N11 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | 5,02 s | carte de fin (CTA) |

N9 et N11 réutilisés tels quels depuis `foodeatup-tva-tuto/vo/` (N6 et N8
là-bas — texte générique, zéro crédit ElevenLabs dépensé). N10 est spécifique
au tutoriel : il nomme l'objet créé (« votre mouvement de stock »), il n'est
jamais recopié — cf. le bug relevé sur `foodeatup-fournisseurs-tuto`.

## Découpage

Les durées de segment sont **dérivées des durées de VO**, pas l'inverse : la
timeline voix (séquentielle, GAP 0,22 s) a été posée d'abord, puis chaque
segment dimensionné pour que la ligne qui le commente démarre dessus.

| Seg | Source | Sortie | Contenu |
|---|---|---:|---|
| intro | carte | 3,68 s | SAISIR UN MOUVEMENT DE STOCK |
| A | 0,30 → 4,20 | 2,78 s | liste « Gestion des stocks » (Chocolat, 2000 pièce) |
| B | 4,20 → 4,55 | 1,00 s | **zoom-punch** sur Mouvement de stock (1380, 355) |
| C | 4,70 → 8,00 | 2,96 s | page Mouvements de Stock, état vide |
| D | 8,00 → 8,35 | 1,00 s | **zoom-punch** sur Ajouter un mouvement (1638, 344) |
| E | 8,60 → 16,50 | 4,26 s | produit, type Entrée, quantité 3000 |
| F | 16,50 → 24,00 | 4,18 s | unité pièce, motif, fournisseur Carrefour |
| G | 24,00 → 24,35 | 1,00 s | **zoom-punch** sur Ajouter (1211, 734) |
| H | 24,60 → 30,55 | 4,21 s | toast succès + ligne dans l'historique |
| I | 30,55 → 31,00 | 1,08 s | **zoom-punch** sur le menu Action (1708, 400) |
| J | 31,05 → 31,70 | 1,13 s | **zoom-punch** sur Modifier (1545, 493) |
| K | 31,90 → 41,55 | 5,38 s | modal pré-rempli, quantité 3000 → 5000 |
| L | 41,55 → 41,95 | 1,00 s | **zoom-punch** sur Ajouter (1211, 734) |
| M | 42,10 → 46,05 | 5,90 s | toast « modifié » + liste à 5000 pièce |
| claude1 | carte générée | 3,24 s | reveal — prompt en gros, fond crème |
| claude2 | carte générée | 1,95 s | confirmation « Copié dans le presse-papiers ! » |
| claude3 | carte générée | 5,64 s | mockup chatbot Claude |
| outro | carte | 6,20 s | CTA |

Coordonnées des 5 boutons mesurées par seuillage colorimétrique sur les frames
réelles (`work/frames/`). Attention : la page **défile de ~158 px** une fois le
tableau des mouvements rempli — « Ajouter un mouvement » n'a donc pas le même y
avant (344) et après (186) ; seul le premier clic est zoomé, mais la mesure a
été refaite sur la frame correspondante à chaque fois.

M tourne **plus lent que le temps réel** (3,95 s de source étalés sur 5,90 s)
pour que la ligne bénéfice N8 se termine avant la séquence Claude. Le contenu
y est un toast statique sur un tableau stabilisé : le ralenti est invisible.

## Séquence Claude — module partagé

`mcp__FoodEatUp__adjust_stock(establishment_id, quantity, mode set|increment,
motif?, establishment_product_id | ingredient_id, allow_negative?)` existe —
schéma vérifié. La vidéo montre le cas « entrée », donc le prompt à l'écran est
celui en `increment` :

> Ajoute [quantité] [unité] de [produit] à mon stock, motif [motif], pour mon
> établissement FoodEatUp (ID [ID établissement]).

Même texte côté fiche Lovable, plus un second prompt `claudePrompts[]` pour le
cas `mode: "set"` (correction d'inventaire), qui correspond à la deuxième
moitié de la vidéo (modification d'un mouvement déjà saisi).

## Bug corrigé — le bandeau d'étape ne s'affichait pas (série entière)

Dans cet ffmpeg (6.1.1), **`drawbox` n'évalue pas `t`** dans ses expressions
`x/y/w/h` : un `drawbox` dont le `x` dépend de `t` est **silencieusement
ignoré** — pas d'erreur, pas de boîte. `drawtext`, lui, évalue bien `t` à
chaque frame.

Conséquence : le `banner()` historique (2 `drawbox` pour le filet orange et la
plaque bleue + 1 `drawtext` pour le libellé) ne rendait **que le texte blanc**
qui glissait sur la capture d'écran. Vérifié aussi sur le MP4 livré de
`foodeatup-produits-tuto` : même plaque manquante. Sur une UI claire, cela
donne du texte blanc sur fond quasi blanc — illisible.

`overlay` a été tenté d'abord : impasse. Son expression `x` se comporte comme
celle de `drawbox`, et il faut en plus boucler l'entrée image (`-loop 1`),
sinon l'overlay ne dure qu'une frame.

Correctif retenu : le bandeau est fait de **deux `drawtext`** partageant la
même expression de glissement.
- La plaque, c'est la `box` de `drawtext` : `boxborderw=16` autour d'une ligne
  de 31 px donne exactement la plaque de 62 px de haut prévue par la charte.
- Le filet orange, c'est la même plaque redessinée 10 px plus à gauche en
  orange : la plaque bleue la recouvre entièrement sauf ses 10 px de gauche.

À reprendre sur les prochains tutoriels (et à re-livrer si Michael veut
rattraper les 10 vidéos déjà publiées).

## Animations

Mêmes principes que toute la série : Ken Burns sur les cartes, xfade (0,28 s),
`slideleft` sur les coupes qui sautent du contenu et `fade` sur les enchaînements
continus, encadré orange pulsant sur les 6 clics, bandeaux d'étape sans
apostrophe (bug ingrédients). Pas de clip avatar dans ce dossier.

## Statut publication

Montée, vérifiée et publiée le 2026-08-03 à la demande explicite de Michael
(« Realise la video … puis publie sur le compte lovable »), sans passer par le
STOP de validation habituel. RapidoCMS : vidéo + vignette uploadées. Lovable :
tutoriel `saisir-un-mouvement-de-stock` ajouté au module `stockvision-ai`
(`claudePrompts[]` à 2 entrées + `chefTip`). Pas de programmation LinkedIn :
non demandée dans cette instruction.
