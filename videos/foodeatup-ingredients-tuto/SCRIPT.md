# Tutoriel — Saisir ses ingrédients FoodEatUp

Dossier Drive « Configuration de ces ingrédients ». Durée livrée : **60,0 s** —
H.264 High/yuv420p, AAC 48 kHz stéréo, faststart. Audio : true peak **-7,2 dBFS**.
Decode 0 erreur, moov avant mdat (faststart confirmé).

Rush le plus dense de la série jusqu'ici (104 s, un seul ingrédient — « Huile d'olive »
— mais un formulaire à de nombreuses sections : nom/fournisseur/unité/prix, coefficient
de transformation, type/particularités/plats associés, stock/seuil (remonté plus haut
dans le formulaire), allergènes, valeurs nutritionnelles, composition).

## Bug rencontré et corrigé : apostrophe dans un bandeau

Premier build en échec : le bandeau "4 · Stock et seuil d'alerte" contient une
apostrophe, qui ferme prématurément le guillemet simple de `text='{text}'` dans
l'argument `-vf` de `drawtext` — exactement le même type de bug que le `%` dans les
prompts Claude, mais jamais rencontré sur un bandeau jusqu'ici. Corrigé en reformulant
sans apostrophe : "4 · Stock et seuil minimum". Ajouté à la liste des pièges dans
`FOODEATUP-TUTORIELS-WORKFLOW.md`.

## Leçon sur le calage voix/image (nouvelle, différente du fix TVA)

Un premier calage complet (forcer zéro dérive à *chaque* frontière de segment) a
produit un segment de 15 s pour "reveal" du prompt Claude — un ralenti artificiel
absurde, parce qu'une ligne de bénéfice longue (N7, l'exemple pâte à tartiner/Nutella,
6,87 s) n'est rattachée à aucune action précise à l'écran et ne "doit" pas forcément
finir avant que la carte suivante commence. Corrigé en (1) raccourcissant N7 à 5,51 s,
(2) acceptant une dérive contenue et volontaire au niveau des clics (comme sur les
autres vidéos) plutôt que de viser zéro partout, et (3) élargissant les 3 étages Claude
(7,00 / 3,00 / 6,00 s au lieu du défaut [2.20, 1.30, 2.50]) pour qu'ils absorbent cette
dérive sans la répercuter plus loin. Vérifié par simulation puis à l'image : N8
(explique le prompt) est bien audible pendant les étages 1 et 2, N9 (coller le prompt)
pendant l'étage 3. Voir le commentaire dans `build.py` (`CLAUDE_STAGE_D`).

## Voix off (11 lignes, ordre narratif ≠ ordre des fichiers)

Les fichiers N0-N10 ont été générés dans un ordre différent de leur ordre de lecture ;
`keys` dans `build.py` liste l'ordre réel utilisé par l'algorithme de placement séquentiel.

| # (fichier) | Texte | Durée | Segment |
|---|---|---:|---|
| N0 | Saisir vos ingrédients sur FoodEatUp : la base de vos recettes et de vos produits. | 4,31 s | intro |
| N1 | Cliquez sur Ajouter un ingrédient pour créer sa fiche. | 2,87 s | clic Ajouter un ingrédient |
| N2 | Donnez-lui un nom, un fournisseur, une unité et un prix unitaire. | 3,66 s | C — nom/fournisseur/unité/prix |
| N5 | Classez-le par type, ses particularités alimentaires, et associez-le directement à vos plats. | 4,96 s | D — type/particularités/plats |
| N3 | Renseignez votre stock actuel et un seuil d'alerte pour ne jamais être pris de court. | 4,44 s | E — stock/seuil |
| N4 | Ajoutez ses allergènes et ses valeurs nutritionnelles, pour des fiches toujours complètes. | 4,62 s | F — allergènes/nutrition/composition |
| N6 | Cliquez sur Enregistrer : votre ingrédient est prêt à rejoindre vos recettes. | 4,26 s | clic Enregistrer |
| N7 | Exemple : la pâte à tartiner est l'ingrédient de vos recettes, le Nutella est le produit que vous commandez. | 5,51 s | H — résultat (bénéfice, précision de Michael) |
| N8 | Vous pouvez aussi le faire depuis Claude : copiez ce prompt, remplacez les crochets. | 4,41 s | étages 1+2 (réutilisé) |
| N9 | Collez-le dans la conversation : votre ingrédient est créé en quelques secondes. | 4,21 s | étage 3 |
| N10 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | 5,02 s | carte de fin (CTA, réutilisé) |

N8/N10 réutilisés tels quels depuis `foodeatup-tva-tuto/vo/` (texte générique — zéro
crédit ElevenLabs dépensé).

## Séquence Claude — module partagé

`mcp__FoodEatUp__create_ingredient(establishment_id, name, unit, price_per_unit,
quantity_in_stock, calories?, proteins?, carbs?, fats?, cooking_coefficient?,
alert_threshold?, description?)` existe — schéma vérifié avant rédaction du prompt :

> Crée l'ingrédient [nom] en [unité], prix [prix]€, quantité en stock [quantité],
> pour mon établissement FoodEatUp (ID [ID établissement]).

Même texte côté fiche Lovable (`claudePrompt`). Michael a demandé en plus un second
prompt (facture → Claude → création automatique des ingrédients) et l'usage de sa
photo de chef pour l'astuce — à intégrer côté Lovable (voir message de suivi).

## Animations

Mêmes principes que toute la série : Ken Burns sur les cartes, xfade (0,28 s), bandeaux
d'étape, encadré orange pulsant sur les 2 clics. Pas de clip avatar dans ce dossier.

## Statut publication

Validée par Michael (demande directe de publication) — publication RapidoCMS +
LinkedIn + Lovable en cours.
