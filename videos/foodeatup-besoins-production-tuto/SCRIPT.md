# Tutoriel — Déduire ses besoins de production FoodEatUp

Module « StockVision AI » (1er tutoriel de ce module, 0/20 publiés jusqu'ici).
Intrants reçus de Michael : `assets/intro.jpg` (carte "DÉDUIRE SES BESOINS DE LA
PRODUCTION"), `assets/outro.jpg` (carte CTA standard, réutilisée telle quelle),
`assets/screen.mp4` (rush 1920x828, 28,24 s, H.264/AAC).

**STATUT : BROUILLON — en attente de validation du script avant génération VO
(règle FOODEATUP-TUTORIELS-WORKFLOW.md, § Étapes 3 et 6). Rien n'est encore
monté ni publié.**

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

## Voix off (brouillon, 9 lignes, à valider avant génération ElevenLabs Adam FR)

| # | Texte | Ancrage |
|---|---|---|
| N0 | Savoir ce qu'il vous manque pour un plat, en un clic ? C'est le rôle de Ma carte. | carte d'intro |
| N1 | Depuis Ma carte, repérez le badge Ingrédients manquants. | vue liste + badge |
| N2 | Ouvrez la fiche d'un plat pour voir le détail. | clic œil, Pizza Margherita |
| N3 | FoodEatUp compare chaque ingrédient requis à votre stock, et signale ce qui manque. | tableau Ingrédients requis |
| N4 | Cliquez sur Ajouter à la liste des courses. | clic bouton |
| N5 | L'ingrédient manquant rejoint aussitôt votre liste de courses, avec la quantité et le fournisseur. | écran Liste des courses |
| N6 | Vous pouvez aussi le faire depuis Claude : copiez ce prompt, remplacez les crochets. | étage 1+2 (réutilisable) |
| N7 | Collez-le dans la conversation : vos besoins de production sont calculés en quelques secondes. | étage 3 |
| N8 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | carte de fin (CTA, réutilisé tel quel) |

N8 réutilisable tel quel depuis un tuto existant (texte générique déjà en banque,
ex. `foodeatup-tva-tuto/vo/N8.mp3` ou `foodeatup-produits-tuto/vo/N8.mp3`) — même
texte que la carte outro fournie. Ordre des segments à confirmer une fois les durées
VO mesurées (règle : calibrer chaque segment sur sa ligne, pas l'inverse).

## Séquence Claude — module partagé (candidate)

Deux outils MCP FoodEatUp correspondent à ce que montre le rush :
`create_production_plan(establishment_id, item_id, planned_quantity, planned_date)`
(le champ "Qté à produire" + OK) et `get_production_ingredients(establishment_id,
production_id)` (le tableau Suffisant/Manquant). Prompt combiné proposé :

> Planifie une production de [quantité] [nom du plat] pour le [date], puis indique-moi
> les ingrédients manquants pour mon établissement FoodEatUp (ID [ID établissement]).

Même texte prévu côté fiche Lovable (`claudePrompt`). À confirmer : aucun outil MCP
FoodEatUp n'expose "ajouter à la liste de courses" en un appel direct — ce geste
précis (bouton "Ajouter à la liste des courses") n'a donc pas d'équivalent Claude
dans ce prompt ; seuls la planification et le diagnostic manquant/suffisant sont
couverts.

## Découpage (à faire — dépend de la VO validée)

Pas encore chronométré finement (zoom-punch, coordonnées de clic) : cette étape suit
la validation du script, pour ne pas refaire le calage si le texte change. Un montage
brut (intro + rush brut + outro, sans VO ni zoom-punch) a été assemblé à titre
d'aperçu rapide dans le scratchpad, à ne pas publier — juste pour visualiser
l'enchaînement carte/rush/carte avant de lancer le vrai montage.

## Statut publication

**En attente de validation de Michael sur le script ci-dessus.** Après accord (ou
ajustements), génération VO ElevenLabs, montage `build.py` (zoom-punch sur le clic
œil et le clic "Ajouter à la liste des courses"), vignette YouTube depuis
`assets/intro.jpg`, puis livraison pour validation finale avant toute publication
RapidoCMS/LinkedIn/Lovable.
