# Tutoriel — Déduire ses besoins de production FoodEatUp

Module « StockVision AI » (1er tutoriel de ce module, 0/20 publiés jusqu'ici).
Intrants reçus de Michael : `assets/intro.jpg` (carte "DÉDUIRE SES BESOINS DE LA
PRODUCTION"), `assets/outro.jpg` (carte CTA standard, réutilisée telle quelle),
`assets/screen.mp4` (rush 1920x828, 28,24 s, H.264/AAC).

Durée livrée : **38,64 s** — H.264 High/yuv420p, AAC 48 kHz stéréo, faststart.
Audio : true peak **-7,3 dBFS** (mesuré sur le MP4 final, `astats`). Script
validé par Michael le 2026-08-03.

**STATUT : montage terminé, à livrer à Michael pour validation avant toute
publication (règle FOODEATUP-TUTORIELS-WORKFLOW.md, § Étape 6). Pas encore
publié sur RapidoCMS/LinkedIn/Lovable.**

## Ce que montre le rush

Écran « Ma carte » (liste des plats, badge « Ingrédients manquants : 1 »). Clic sur
l'icône œil de « Pizza Margherita napolitaine » → fiche plat : prix, portions, temps,
chef, puis tableau « Ingrédients requis » comparant quantité nécessaire / en stock /
manquant / statut — Tomate et Farine en `Suffisant`, Fromage (tranches) en `Manquant`
(100 g requis, 0 g en stock). Clic sur « Ajouter à la liste des courses ». Bascule sur
l'écran « Liste des courses » : le Fromage (tranches) apparaît désormais sous
« Fournisseur non défini » avec sa quantité recommandée et son coût, aux côtés des
produits déjà présents (Lait, Tomates, Sauce soja, Algues nori, Avocat...), liste
groupée par fournisseur avec totaux (10 produits, 3 fournisseurs, 361 245,00 €) et
actions Consolider / Email / Commander.

Chaque carte plat a aussi un champ « Qté à produire » + bouton OK (visible en haut du
rush, non actionné dans ce rush précis) : c'est ce qui pilote la quantité produite et
donc le recalcul des besoins/manquants.

## Voix off (validée, 9 lignes, voix Adam FR `TGAegA0zNRi8I6nUdq3i`, `eleven_multilingual_v2`)

| # | Texte | Durée | Ancrage |
|---|---|---:|---|
| N0 | Savoir ce qu'il vous manque pour un plat, en un clic ? C'est le rôle de Ma carte. | 4,31 s | carte d'intro |
| N1 | Depuis Ma carte, repérez le badge Ingrédients manquants. | 3,00 s | vue liste + badge (segment A) |
| N2 | Ouvrez la fiche d'un plat pour voir le détail. | 2,32 s | clic œil (B) + en-tête fiche (C) |
| N3 | FoodEatUp compare chaque ingrédient requis à votre stock, et signale ce qui manque. | 4,60 s | tableau Ingrédients requis (D) |
| N4 | Cliquez sur Ajouter à la liste des courses. | 2,12 s | clic bouton (E) |
| N5 | L'ingrédient manquant rejoint aussitôt votre liste de courses, avec la quantité et le fournisseur. | 5,51 s | écran Liste des courses (F) |
| N6 | Vous pouvez aussi le faire depuis Claude : copiez ce prompt, remplacez les crochets. | 4,41 s | étage 1+2 (réutilisé) |
| N7 | Collez-le dans la conversation : vos besoins de production sont calculés en quelques secondes. | 4,49 s | étage 3 |
| N8 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | 5,02 s | carte de fin (CTA, réutilisé) |

N6/N8 réutilisés tels quels depuis `foodeatup-produits-tuto/vo/` (texte générique
identique, zéro crédit ElevenLabs dépensé pour ces deux lignes).

## Découpage (build.py, coordonnées mesurées par seuillage colorimétrique)

| Seg | Source | Sortie | Contenu |
|---|---|---:|---|
| intro | carte | 4,60 s | DÉDUIRE SES BESOINS DE LA PRODUCTION |
| A | 0,20 → 4,00 | 3,00 s | Ma carte, badge Ingrédients manquants (1) |
| B | 4,00 → 4,30 | 0,90 s | **zoom-punch** icône œil, Pizza Margherita (868, 54) |
| C | 4,30 → 5,20 | 2,00 s | fiche plat : Prix/Portions/Temps/Chef |
| D | 5,20 → 7,60 | 4,50 s | tableau Ingrédients requis (Tomate/Farine Suffisant, Fromage tranches Manquant) |
| E | 7,60 → 7,90 | 0,90 s | **zoom-punch** "Ajouter à la liste des courses" (1033, 784) |
| F | 7,90 → 28,24 | 6,00 s | Liste des courses : Fromage (tranches) ajouté sous Fournisseur non défini |
| claude1 | carte générée | 3,00 s | reveal — prompt en gros, fond crème |
| claude2 | carte générée | 2,30 s | confirmation « Copié dans le presse-papiers ! » |
| claude3 | carte générée | 5,30 s | mockup chatbot Claude |
| outro | carte | 8,73 s (auto-étendue depuis 6,20 s pour porter N8) | CTA |

Offsets VO réels vérifiés (`build.py`, impression `offsets:`) : chaque ligne démarre
sur son ancrage ou légèrement après (dérive max +3,16 s sur N6, absorbée par le
séquencement `max(anchor, fin_précédente + GAP)` — pattern déjà accepté sur la série,
voir `foodeatup-produits-tuto/SCRIPT.md`). Aucun chevauchement.

## Séquence Claude — module partagé

Deux outils MCP FoodEatUp correspondent à ce que montre le rush :
`create_production_plan(establishment_id, item_id, planned_quantity, planned_date)`
(le champ "Qté à produire" + OK) et `get_production_ingredients(establishment_id,
production_id)` (le tableau Suffisant/Manquant). Prompt combiné :

> Planifie une production de [quantité] [nom du plat] pour le [date], puis indique-moi
> les ingrédients manquants pour mon établissement FoodEatUp (ID [ID établissement]).

Même texte prévu côté fiche Lovable (`claudePrompt`). Aucun outil MCP FoodEatUp
n'expose "ajouter à la liste de courses" en un appel direct — ce geste précis (bouton
"Ajouter à la liste des courses") n'a donc pas d'équivalent Claude dans ce prompt ;
seuls la planification et le diagnostic manquant/suffisant sont couverts.

## Animations

Mêmes principes que toute la série : Ken Burns sur les cartes, xfade (0,28 s),
bandeaux d'étape (aucune apostrophe), encadré orange pulsant sur les 2 clics. Pas de
clip avatar dans ce dossier.

## Statut publication

**Script validé par Michael (2026-08-03), vidéo livrée puis validation reçue le
même jour ("ok publi sur lovable").**

- **Lovable : publié.** Fiche `deduire-ses-besoins-de-production` ajoutée à
  `src/data/tutorials.ts` du projet FoodEatUp Academy (workspace
  Contact.prendstapart, projet `55ff35b7-c442-42c4-950c-8c7fd420c645`),
  premier tutoriel du module StockVision AI — `howItWorks`/`whatItsFor`/
  `chefTip`/`chefTipAvatar`/`claudePrompt` cohérents avec le reste de la
  série. `videoUrl`/`thumbnailUrl` pointent vers les `raw.githubusercontent.com`
  de ce dépôt (branche `claude/foodeatup-tutorial-video-buhrdu`). Commit Lovable
  `75d4397`.
- **RapidoCMS / LinkedIn : non demandé.** Michael a validé explicitement
  "Lovable" — pas encore d'upload RapidoCMS ni de draft LinkedIn programmé.
  À faire sur demande explicite.
