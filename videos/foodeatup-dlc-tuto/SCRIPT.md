# Tutoriel — Poser une DLC sur ses productions FoodEatUp

Module 4 « HACCP ». Réutilise le même écran que « Créer les étiquettes de vos
productions » (fourni par Michael) : poser une DLC se fait dans le même flux
que la création d'étiquette HACCP, ce tutoriel isole et zoome sur la partie
DLC spécifiquement. Durée livrée : **44,5 s** — H.264 High/yuv420p, AAC 48 kHz
stéréo, faststart. Audio : true peak **-7,3 dBFS** (mesuré sur le MP4 final).
Décode 0 erreur, moov avant mdat (faststart confirmé).

## Voix off (9 lignes)

| # | Texte | Durée | Ancrage |
|---|---|---:|---|
| N0 | Poser une DLC sur vos productions FoodEatUp ? Elle est déjà calculée, à vous de la vérifier. | 5,15 s | carte d'intro |
| N1 | Ouvrez une production : chaque ingrédient affiche déjà sa DLC. | 3,79 s | modal détail production, colonne DLC |
| N2 | Cliquez sur Créer étiquette HACCP pour la reporter sur l'étiquette. | 4,26 s | **zoom-punch** sur Créer étiquette HACCP (1015, 722) |
| N3 | La DLC de votre produit est pré-remplie, prête à imprimer. | 3,60 s | modal Étiqueteuse, DLC 01/08/2026 visible |
| N4 | Besoin de l'ajuster ? Cliquez directement dans le champ date. | 3,06 s | **zoom-punch** (still) sur le champ DLC (563, 607) |
| N5 | Validez : vos étiquettes partent à l'historique, DLC incluse. | 4,26 s | **zoom-punch** sur Valider → Historique (1253, 342) + confirmation |
| N6 | Vous pouvez aussi le faire depuis Claude : copiez ce prompt, remplacez les crochets. | 4,41 s | **étage 1+2** (reveal + copié) — réutilisé tel quel depuis `foodeatup-categories-tuto/vo/N6.mp3`, texte identique |
| N7 | Collez-le dans la conversation : votre étiquette HACCP est créée avec sa DLC en quelques secondes. | 7,55 s | **étage 3** (mockup chatbot) |
| N8 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | 5,02 s | carte de fin (CTA) — réutilisé tel quel depuis `foodeatup-tva-tuto/vo/N8.mp3` |

N6/N8 copiés depuis les tutoriels précédents (texte identique, même voix) —
zéro crédit ElevenLabs dépensé sur ces deux lignes.

## Découpage

| Seg | Source | Sortie | Contenu |
|---|---|---:|---|
| intro | carte | 5,50 s | POSER UNE DLC SUR SES PRODUCTIONS (image fournie par Michael, non retouchée) |
| A | 5,50 → 8,80 | 5,00 s | modal détail production, colonne DLC par ingrédient (tomates, DLC 25/07/2026) |
| B | 8,80 → 9,10 | 0,90 s | **zoom-punch** sur Créer étiquette HACCP (1015, 722) |
| C | 9,30 → 13,50 | 5,00 s | modal Étiqueteuse, carte produit avec DLC pré-remplie (01/08/2026) |
| D | still (frame figée à 12,5 s du rush) | 4,50 s | **zoom-punch tenu** sur le champ DLC — voir "Bug corrigé" ci-dessous |
| E | 35,50 → 35,80 | 0,90 s | **zoom-punch** sur Valider → Historique (1253, 342) |
| F | 35,80 → 40,80 | 5,50 s | confirmation « 2 étiquette(s) créée(s) » puis « Étiquettes validées ! » |
| claude1 | carte générée | 2,60 s | reveal — prompt en gros, fond crème |
| claude2 | carte générée | 1,80 s | confirmation « Copié dans le presse-papiers ! » |
| claude3 | carte générée | 8,00 s | mockup chatbot Claude (logo + bulles) |
| outro | carte | 7,40 s | CTA (auto-étendu depuis 5,60 s pour absorber le reliquat de voix, voir plus bas) |

Transitions : `slideleft` sur la bascule vers/entre les 3 étages Claude,
`fade` partout ailleurs (action continue à l'écran).

## Bug corrigé : le zoom sur le champ DLC dérivait vers un autre champ

Premier rendu : le segment D utilisait une plage de rush en temps réel
(13,5 → 18,0 s). Or la modale **scrolle** pendant cette fenêtre (vérifié
frame par frame) — le crop fixe calé sur la position du champ DLC en
tombait donc, quelques secondes plus tard, sur « Équipement de stockage »
au lieu de la DLC. Corrigé en figeant une **image fixe** (frame à 12,5 s,
position confirmée stable) pour tout le segment D plutôt que de rejouer le
rush en direct — même logique que les cartes intro/outro/Claude, juste
appliquée à un extrait d'écran. Rendu re-vérifié frame par frame après
correction : l'encadré orange tombe bien sur le champ DLC pendant toute
la durée du segment.

## Séquence Claude — module partagé

`mcp__FoodEatUp__create_haccp_label(establishment_id, ingredient_name, dlc?,
lot_number?, type?, ...)` existe et expose un paramètre `dlc` explicite —
schéma vérifié avant rédaction du prompt. Séquence rendue par
`videos/_shared/claude_prompt_sequence.py`, seuls changent le texte du
prompt et la réplique assistant :

> Crée une étiquette HACCP pour [nom du produit] avec une DLC au [date DLC]
> pour mon établissement FoodEatUp (ID [ID établissement]).

Réplique assistant : « Bien sûr ! Je crée cette étiquette HACCP avec sa DLC
pour votre établissement… ». Même texte de prompt côté fiche Lovable
(`claudePrompt`) le jour où cette vidéo sera ajoutée au site.

## Animations

Mêmes principes que toute la série : Ken Burns sur les cartes, xfade
(0,28 s), bandeaux d'étape, encadré orange pulsant sur les clics/le champ
DLC. Pas de clip avatar dans ce dossier.

## Statut publication

**Montage terminé, en attente de validation de Michael avant toute
publication** (règle « STOP obligatoire » de
`videos/FOODEATUP-TUTORIELS-WORKFLOW.md` — ne pas publier tant que la
vidéo n'est pas validée). Livré via `SendUserFile`. Une fois l'accord donné :
upload RapidoCMS + vignette, ajout sur Lovable (`src/data/tutorials.ts`,
module `haccp`, `claudePrompt` ci-dessus), et entrée dans le tableau
"Tutoriels publiés" de `LOVABLE-FOODEATUP-DOCS.md`.
