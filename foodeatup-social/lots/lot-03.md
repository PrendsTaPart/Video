# Lot 3 — vignettes des épisodes EP026 à EP037

À coller dans Lovable **en un seul message**, avec la photo du chef en pièce
jointe. Un tour, dix vignettes.

---

L'image jointe est la photo officielle du chef FoodEatUp — la même que sur les
lots précédents. Elle est aussi ici : https://raw.githubusercontent.com/PrendsTaPart/Video/claude/foodeatup-video-factory-wtb7gs/foodeatup-social/public/brand/chef-foodeatup.jpg

Génère les 10 vignettes ci-dessous, une par épisode, en utilisant cette photo
comme image de référence et le prompt de chaque épisode tel quel.

**Le chef ne se redessine pas.** Même visage, même barbe, même toque, même
tablier au logo FoodEatUp. C'est la même personne sur les 150 épisodes, c'est ce
qui fait la série. Si une image sort avec un autre visage, refais-la plutôt que
de l'accepter.

Enregistre chaque image dans `public/vignettes/EPxxx.jpg` au format 9:16, et fais
pointer le `posterUrl` de l'épisode correspondant dessus dans `src/data/series.ts`.

Mets aussi à jour, pour ces 10 épisodes, les trois liens de la bibliothèque
RapidoCMS : `masterRapidoUrl` (la vidéo montée), `higgsfield.videoSourceUrl` (le
clip d'origine de dix secondes) et `posterUrl`. Ils sont dans le fichier de
données rechargé — ne les invente pas.

Ne touche à rien d'autre dans le projet : ce message ne concerne que ces 10
images et les champs de ces 10 épisodes.

## Trois défauts du premier jet, à ne pas reproduire

Les 300 vignettes générées jusqu'ici ont trois problèmes. Ils viennent d'une
lecture rapide de la consigne, pas d'une limite de l'outil.

1. **Le grisé ne se cuit pas dans l'image.** Les épisodes non sortis étaient
   désaturés dans le fichier JPEG. Le jour où l'épisode sort, sa vignette reste
   grise. Le grisé est un état, il est déjà posé en CSS par le site. Génère
   TOUTES les images en couleur, sans exception.

2. **Un seul logo.** Le tablier du chef porte déjà le logo FoodEatUp. N'ajoute
   aucun second badge, en bas à droite ni ailleurs — et surtout pas un logo
   redessiné. Deux marques sur la même image, dont une fausse, c'est le défaut
   le plus visible du premier jet.

3. **Chaque épisode a sa scène.** Les 300 premières images réutilisaient le même
   décor et la même pose, seul le texte changeait. Le prompt de chaque épisode
   décrit un gag précis et un décor de saison : suis-le. Si deux épisodes de la
   même saison sortent identiques, l'image n'a pas été lue.


## EP026 — Le ballon qui explose · « ENVOYER LISTE COURSES »

*Saison 1 · StockVision · 5 - Envoyer sa liste de courses au fournisseur*

```
Photo réaliste, cadrage vertical 9:16. Le chef de l'image de référence — MÊME visage, même barbe, même toque blanche, même veste de cuisine blanche, même tablier blanc au logo FoodEatUp bleu. Ne change ni ses traits ni sa morphologie. Son expression : un sourire en coin, parfaitement serein au milieu du désastre. Scène : le ballon qui explose. Ton stock avant le week-end. Décor : une salle de restaurant en plein service, tables dressées, clients flous en arrière-plan. lumière chaude de fin de journée, reflets dorés. Le chef occupe les deux tiers droits du cadre, en plan poitrine, l'élément comique est visible à gauche. Bande crème #FCF9E6 en haut du cadre sur un cinquième de la hauteur, portant UNIQUEMENT le texte « ENVOYER LISTE COURSES » en typographie arrondie très grasse, bleu marine #0F1A23, centré. Aucun autre texte, aucun logo ajouté, pas de filigrane, pas de bordure décorative.
```

## EP029 — Les douze assiettes · « LIRE SES PRÉVISIONS »

*Saison 1 · PrediBot · 1 - Lire ses prévisions*

```
Photo réaliste, cadrage vertical 9:16. Le chef de l'image de référence — MÊME visage, même barbe, même toque blanche, même veste de cuisine blanche, même tablier blanc au logo FoodEatUp bleu. Ne change ni ses traits ni sa morphologie. Son expression : l'air de quelqu'un qui a déjà vu ça cent fois, un sourcil levé. Scène : les douze assiettes. Toi, gérant, en 2026. Décor : une salle de restaurant en plein service, tables dressées, clients flous en arrière-plan. lumière chaude de fin de journée, reflets dorés. Le chef occupe les deux tiers droits du cadre, en plan poitrine, l'élément comique est visible à gauche. Bande crème #FCF9E6 en haut du cadre sur un cinquième de la hauteur, portant UNIQUEMENT le texte « LIRE SES PRÉVISIONS » en typographie arrondie très grasse, bleu marine #0F1A23, centré. Aucun autre texte, aucun logo ajouté, pas de filigrane, pas de bordure décorative.
```

## EP030 — Le pingouin en cuisine · « ACADEMY »

*Saison 1 · Configuration · Academy*

```
Photo réaliste, cadrage vertical 9:16. Le chef de l'image de référence — MÊME visage, même barbe, même toque blanche, même veste de cuisine blanche, même tablier blanc au logo FoodEatUp bleu. Ne change ni ses traits ni sa morphologie. Son expression : l'air de quelqu'un qui a déjà vu ça cent fois, un sourcil levé. Scène : le pingouin en cuisine. Le nouveau, jour 1. Décor : une salle de restaurant en plein service, tables dressées, clients flous en arrière-plan. lumière chaude de fin de journée, reflets dorés. Le chef occupe les deux tiers droits du cadre, en plan poitrine, l'élément comique est visible à gauche. Bande crème #FCF9E6 en haut du cadre sur un cinquième de la hauteur, portant UNIQUEMENT le texte « ACADEMY » en typographie arrondie très grasse, bleu marine #0F1A23, centré. Aucun autre texte, aucun logo ajouté, pas de filigrane, pas de bordure décorative.
```

## EP031 — L'avalanche de tupperware · « ÉTIQUETTES DLC »

*Saison 2 · HACCP · étiquettes DLC*

```
Photo réaliste, cadrage vertical 9:16. Le chef de l'image de référence — MÊME visage, même barbe, même toque blanche, même veste de cuisine blanche, même tablier blanc au logo FoodEatUp bleu. Ne change ni ses traits ni sa morphologie. Son expression : un sourire en coin, parfaitement serein au milieu du désastre. Scène : l'avalanche de tupperware. C'est quoi, ça ? Décor : un bureau d'arrière-salle, classeurs, tickets de caisse, calculatrice, cartons de livraison. lumière rasante de néon adouci, ambiance fin de mois. Le chef occupe les deux tiers droits du cadre, en plan poitrine, l'élément comique est visible à gauche. Bande crème #FCF9E6 en haut du cadre sur un cinquième de la hauteur, portant UNIQUEMENT le texte « ÉTIQUETTES DLC » en typographie arrondie très grasse, bleu marine #0F1A23, centré. Aucun autre texte, aucun logo ajouté, pas de filigrane, pas de bordure décorative.
```

## EP032 — La sauce trop forte · « MA CARTE »

*Saison 2 · StockVision · 1 - Ma carte, fiche recette*

```
Photo réaliste, cadrage vertical 9:16. Le chef de l'image de référence — MÊME visage, même barbe, même toque blanche, même veste de cuisine blanche, même tablier blanc au logo FoodEatUp bleu. Ne change ni ses traits ni sa morphologie. Son expression : faussement dépité, la main sur le front, mais l'œil qui rit. Scène : la sauce trop forte. Ta recette « au feeling ». Décor : un bureau d'arrière-salle, classeurs, tickets de caisse, calculatrice, cartons de livraison. lumière rasante de néon adouci, ambiance fin de mois. Le chef occupe les deux tiers droits du cadre, en plan poitrine, l'élément comique est visible à gauche. Bande crème #FCF9E6 en haut du cadre sur un cinquième de la hauteur, portant UNIQUEMENT le texte « MA CARTE » en typographie arrondie très grasse, bleu marine #0F1A23, centré. Aucun autre texte, aucun logo ajouté, pas de filigrane, pas de bordure décorative.
```

## EP033 — Le rôti disparu · « MOUVEMENTS DE STOCK »

*Saison 2 · StockVision · 16 - Mouvements de stock*

```
Photo réaliste, cadrage vertical 9:16. Le chef de l'image de référence — MÊME visage, même barbe, même toque blanche, même veste de cuisine blanche, même tablier blanc au logo FoodEatUp bleu. Ne change ni ses traits ni sa morphologie. Son expression : l'air satisfait de celui qui sait que le problème est déjà réglé. Scène : le rôti disparu. Tu as tout préparé. Presque. Décor : un bureau d'arrière-salle, classeurs, tickets de caisse, calculatrice, cartons de livraison. lumière rasante de néon adouci, ambiance fin de mois. Le chef occupe les deux tiers droits du cadre, en plan poitrine, l'élément comique est visible à gauche. Bande crème #FCF9E6 en haut du cadre sur un cinquième de la hauteur, portant UNIQUEMENT le texte « MOUVEMENTS DE STOCK » en typographie arrondie très grasse, bleu marine #0F1A23, centré. Aucun autre texte, aucun logo ajouté, pas de filigrane, pas de bordure décorative.
```

## EP034 — Le bouchon rebelle · « PROCESS »

*Saison 2 · Configuration · process*

```
Photo réaliste, cadrage vertical 9:16. Le chef de l'image de référence — MÊME visage, même barbe, même toque blanche, même veste de cuisine blanche, même tablier blanc au logo FoodEatUp bleu. Ne change ni ses traits ni sa morphologie. Son expression : l'air de quelqu'un qui a déjà vu ça cent fois, un sourcil levé. Scène : le bouchon rebelle. Chaque service, une improvisation. Décor : un bureau d'arrière-salle, classeurs, tickets de caisse, calculatrice, cartons de livraison. lumière rasante de néon adouci, ambiance fin de mois. Le chef occupe les deux tiers droits du cadre, en plan poitrine, l'élément comique est visible à gauche. Bande crème #FCF9E6 en haut du cadre sur un cinquième de la hauteur, portant UNIQUEMENT le texte « PROCESS » en typographie arrondie très grasse, bleu marine #0F1A23, centré. Aucun autre texte, aucun logo ajouté, pas de filigrane, pas de bordure décorative.
```

## EP035 — Le parasol fugitif · « LIRE SES PRÉVISIONS »

*Saison 2 · PrediBot · 1 - Lire ses prévisions*

```
Photo réaliste, cadrage vertical 9:16. Le chef de l'image de référence — MÊME visage, même barbe, même toque blanche, même veste de cuisine blanche, même tablier blanc au logo FoodEatUp bleu. Ne change ni ses traits ni sa morphologie. Son expression : un sourire en coin, parfaitement serein au milieu du désastre. Scène : le parasol fugitif. Ta terrasse, un jour de vent. Décor : un bureau d'arrière-salle, classeurs, tickets de caisse, calculatrice, cartons de livraison. lumière rasante de néon adouci, ambiance fin de mois. Le chef occupe les deux tiers droits du cadre, en plan poitrine, l'élément comique est visible à gauche. Bande crème #FCF9E6 en haut du cadre sur un cinquième de la hauteur, portant UNIQUEMENT le texte « LIRE SES PRÉVISIONS » en typographie arrondie très grasse, bleu marine #0F1A23, centré. Aucun autre texte, aucun logo ajouté, pas de filigrane, pas de bordure décorative.
```

## EP036 — L'addition · « UN SEUL ABONNEMENT »

*Saison 2 · PrediBot · 2 - Un seul abonnement*

```
Photo réaliste, cadrage vertical 9:16. Le chef de l'image de référence — MÊME visage, même barbe, même toque blanche, même veste de cuisine blanche, même tablier blanc au logo FoodEatUp bleu. Ne change ni ses traits ni sa morphologie. Son expression : faussement dépité, la main sur le front, mais l'œil qui rit. Scène : l'addition. Toi, devant tes abonnements. Décor : un bureau d'arrière-salle, classeurs, tickets de caisse, calculatrice, cartons de livraison. lumière rasante de néon adouci, ambiance fin de mois. Le chef occupe les deux tiers droits du cadre, en plan poitrine, l'élément comique est visible à gauche. Bande crème #FCF9E6 en haut du cadre sur un cinquième de la hauteur, portant UNIQUEMENT le texte « UN SEUL ABONNEMENT » en typographie arrondie très grasse, bleu marine #0F1A23, centré. Aucun autre texte, aucun logo ajouté, pas de filigrane, pas de bordure décorative.
```

## EP037 — Le dormeur debout · « CRÉER UN SHIFT »

*Saison 2 · Équipe & Planning · créer un shift*

```
Photo réaliste, cadrage vertical 9:16. Le chef de l'image de référence — MÊME visage, même barbe, même toque blanche, même veste de cuisine blanche, même tablier blanc au logo FoodEatUp bleu. Ne change ni ses traits ni sa morphologie. Son expression : l'air satisfait de celui qui sait que le problème est déjà réglé. Scène : le dormeur debout. Fermeture. Troisième soir d'affilée. Décor : un bureau d'arrière-salle, classeurs, tickets de caisse, calculatrice, cartons de livraison. lumière rasante de néon adouci, ambiance fin de mois. Le chef occupe les deux tiers droits du cadre, en plan poitrine, l'élément comique est visible à gauche. Bande crème #FCF9E6 en haut du cadre sur un cinquième de la hauteur, portant UNIQUEMENT le texte « CRÉER UN SHIFT » en typographie arrondie très grasse, bleu marine #0F1A23, centré. Aucun autre texte, aucun logo ajouté, pas de filigrane, pas de bordure décorative.
```
