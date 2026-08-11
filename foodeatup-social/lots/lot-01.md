# Lot 1 — vignettes des épisodes EP001 à EP015

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


## EP001 — Le chien qui te regarde · « COMMANDES MULTI-CANAUX »

*Saison 1 · Service · 1 - Commandes multi-canaux*

```
Photo réaliste, cadrage vertical 9:16. Le chef de l'image de référence — MÊME visage, même barbe, même toque blanche, même veste de cuisine blanche, même tablier blanc au logo FoodEatUp bleu. Ne change ni ses traits ni sa morphologie. Son expression : faussement dépité, la main sur le front, mais l'œil qui rit. Scène : le chien qui te regarde. Lui aussi attend ta commande. Décor : une salle de restaurant en plein service, tables dressées, clients flous en arrière-plan. lumière chaude de fin de journée, reflets dorés. Le chef occupe les deux tiers droits du cadre, en plan poitrine, l'élément comique est visible à gauche. Bande crème #FCF9E6 en haut du cadre sur un cinquième de la hauteur, portant UNIQUEMENT le texte « COMMANDES MULTI-CANAUX » en typographie arrondie très grasse, bleu marine #0F1A23, centré. Aucun autre texte, aucun logo ajouté, pas de filigrane, pas de bordure décorative.
```

## EP002 — La chute en skateboard · « ENVOI DIRECT CUISINE »

*Saison 1 · Service · 3 - Envoi direct cuisine*

```
Photo réaliste, cadrage vertical 9:16. Le chef de l'image de référence — MÊME visage, même barbe, même toque blanche, même veste de cuisine blanche, même tablier blanc au logo FoodEatUp bleu. Ne change ni ses traits ni sa morphologie. Son expression : l'air satisfait de celui qui sait que le problème est déjà réglé. Scène : la chute en skateboard. Ton service du samedi soir. Décor : une salle de restaurant en plein service, tables dressées, clients flous en arrière-plan. lumière chaude de fin de journée, reflets dorés. Le chef occupe les deux tiers droits du cadre, en plan poitrine, l'élément comique est visible à gauche. Bande crème #FCF9E6 en haut du cadre sur un cinquième de la hauteur, portant UNIQUEMENT le texte « ENVOI DIRECT CUISINE » en typographie arrondie très grasse, bleu marine #0F1A23, centré. Aucun autre texte, aucun logo ajouté, pas de filigrane, pas de bordure décorative.
```

## EP003 — Le plat dans la piscine · « MA CARTE »

*Saison 1 · StockVision · 1 - Ma carte*

```
Photo réaliste, cadrage vertical 9:16. Le chef de l'image de référence — MÊME visage, même barbe, même toque blanche, même veste de cuisine blanche, même tablier blanc au logo FoodEatUp bleu. Ne change ni ses traits ni sa morphologie. Son expression : l'air de quelqu'un qui a déjà vu ça cent fois, un sourcil levé. Scène : le plat dans la piscine. Ta marge, en ce moment. Décor : une salle de restaurant en plein service, tables dressées, clients flous en arrière-plan. lumière chaude de fin de journée, reflets dorés. Le chef occupe les deux tiers droits du cadre, en plan poitrine, l'élément comique est visible à gauche. Bande crème #FCF9E6 en haut du cadre sur un cinquième de la hauteur, portant UNIQUEMENT le texte « MA CARTE » en typographie arrondie très grasse, bleu marine #0F1A23, centré. Aucun autre texte, aucun logo ajouté, pas de filigrane, pas de bordure décorative.
```

## EP005 — Le serveur qui glisse · « VUE D'ENSEMBLE »

*Saison 1 · Configuration · vue d'ensemble*

```
Photo réaliste, cadrage vertical 9:16. Le chef de l'image de référence — MÊME visage, même barbe, même toque blanche, même veste de cuisine blanche, même tablier blanc au logo FoodEatUp bleu. Ne change ni ses traits ni sa morphologie. Son expression : faussement dépité, la main sur le front, mais l'œil qui rit. Scène : le serveur qui glisse. Trois logiciels. Deux mains. Décor : une salle de restaurant en plein service, tables dressées, clients flous en arrière-plan. lumière chaude de fin de journée, reflets dorés. Le chef occupe les deux tiers droits du cadre, en plan poitrine, l'élément comique est visible à gauche. Bande crème #FCF9E6 en haut du cadre sur un cinquième de la hauteur, portant UNIQUEMENT le texte « VUE D'ENSEMBLE » en typographie arrondie très grasse, bleu marine #0F1A23, centré. Aucun autre texte, aucun logo ajouté, pas de filigrane, pas de bordure décorative.
```

## EP006 — La pizza frisbee · « AJOUTER MODIFIER MOUVEMENT »

*Saison 1 · StockVision · 17 - Ajouter et modifier un mouvement*

```
Photo réaliste, cadrage vertical 9:16. Le chef de l'image de référence — MÊME visage, même barbe, même toque blanche, même veste de cuisine blanche, même tablier blanc au logo FoodEatUp bleu. Ne change ni ses traits ni sa morphologie. Son expression : l'air satisfait de celui qui sait que le problème est déjà réglé. Scène : la pizza frisbee. Ta pizza part plus vite que ton stock. Décor : une salle de restaurant en plein service, tables dressées, clients flous en arrière-plan. lumière chaude de fin de journée, reflets dorés. Le chef occupe les deux tiers droits du cadre, en plan poitrine, l'élément comique est visible à gauche. Bande crème #FCF9E6 en haut du cadre sur un cinquième de la hauteur, portant UNIQUEMENT le texte « AJOUTER MODIFIER MOUVEMENT » en typographie arrondie très grasse, bleu marine #0F1A23, centré. Aucun autre texte, aucun logo ajouté, pas de filigrane, pas de bordure décorative.
```

## EP007 — La mamie qui goûte · « RÉPONDRE AUX AVIS »

*Saison 1 · Marketing · 3 - Répondre aux avis*

```
Photo réaliste, cadrage vertical 9:16. Le chef de l'image de référence — MÊME visage, même barbe, même toque blanche, même veste de cuisine blanche, même tablier blanc au logo FoodEatUp bleu. Ne change ni ses traits ni sa morphologie. Son expression : l'air de quelqu'un qui a déjà vu ça cent fois, un sourcil levé. Scène : la mamie qui goûte. Le seul avis client qui compte. Décor : une salle de restaurant en plein service, tables dressées, clients flous en arrière-plan. lumière chaude de fin de journée, reflets dorés. Le chef occupe les deux tiers droits du cadre, en plan poitrine, l'élément comique est visible à gauche. Bande crème #FCF9E6 en haut du cadre sur un cinquième de la hauteur, portant UNIQUEMENT le texte « RÉPONDRE AUX AVIS » en typographie arrondie très grasse, bleu marine #0F1A23, centré. Aucun autre texte, aucun logo ajouté, pas de filigrane, pas de bordure décorative.
```

## EP010 — Le flambage raté · « LIRE SES PRÉVISIONS »

*Saison 1 · PrediBot · 1 - Lire ses prévisions*

```
Photo réaliste, cadrage vertical 9:16. Le chef de l'image de référence — MÊME visage, même barbe, même toque blanche, même veste de cuisine blanche, même tablier blanc au logo FoodEatUp bleu. Ne change ni ses traits ni sa morphologie. Son expression : faussement dépité, la main sur le front, mais l'œil qui rit. Scène : le flambage raté. Toi, devant ta facture logicielle. Décor : une salle de restaurant en plein service, tables dressées, clients flous en arrière-plan. lumière chaude de fin de journée, reflets dorés. Le chef occupe les deux tiers droits du cadre, en plan poitrine, l'élément comique est visible à gauche. Bande crème #FCF9E6 en haut du cadre sur un cinquième de la hauteur, portant UNIQUEMENT le texte « LIRE SES PRÉVISIONS » en typographie arrondie très grasse, bleu marine #0F1A23, centré. Aucun autre texte, aucun logo ajouté, pas de filigrane, pas de bordure décorative.
```

## EP013 — L'avalanche de notifications · « PARLER À PREDIBOT »

*Saison 1 · PrediBot · 3 - Parler à PrediBot*

```
Photo réaliste, cadrage vertical 9:16. Le chef de l'image de référence — MÊME visage, même barbe, même toque blanche, même veste de cuisine blanche, même tablier blanc au logo FoodEatUp bleu. Ne change ni ses traits ni sa morphologie. Son expression : un sourire en coin, parfaitement serein au milieu du désastre. Scène : l'avalanche de notifications. Dix logiciels. Dix notifications. Décor : une salle de restaurant en plein service, tables dressées, clients flous en arrière-plan. lumière chaude de fin de journée, reflets dorés. Le chef occupe les deux tiers droits du cadre, en plan poitrine, l'élément comique est visible à gauche. Bande crème #FCF9E6 en haut du cadre sur un cinquième de la hauteur, portant UNIQUEMENT le texte « PARLER À PREDIBOT » en typographie arrondie très grasse, bleu marine #0F1A23, centré. Aucun autre texte, aucun logo ajouté, pas de filigrane, pas de bordure décorative.
```

## EP014 — Le raton laveur · « MOUVEMENTS DE STOCK »

*Saison 1 · StockVision · 16 - Mouvements de stock*

```
Photo réaliste, cadrage vertical 9:16. Le chef de l'image de référence — MÊME visage, même barbe, même toque blanche, même veste de cuisine blanche, même tablier blanc au logo FoodEatUp bleu. Ne change ni ses traits ni sa morphologie. Son expression : faussement dépité, la main sur le front, mais l'œil qui rit. Scène : le raton laveur. Ton gaspillage alimentaire. Décor : une salle de restaurant en plein service, tables dressées, clients flous en arrière-plan. lumière chaude de fin de journée, reflets dorés. Le chef occupe les deux tiers droits du cadre, en plan poitrine, l'élément comique est visible à gauche. Bande crème #FCF9E6 en haut du cadre sur un cinquième de la hauteur, portant UNIQUEMENT le texte « MOUVEMENTS DE STOCK » en typographie arrondie très grasse, bleu marine #0F1A23, centré. Aucun autre texte, aucun logo ajouté, pas de filigrane, pas de bordure décorative.
```

## EP015 — La tour d'assiettes · « RÉFÉRENTIELS »

*Saison 1 · Configuration · référentiels*

```
Photo réaliste, cadrage vertical 9:16. Le chef de l'image de référence — MÊME visage, même barbe, même toque blanche, même veste de cuisine blanche, même tablier blanc au logo FoodEatUp bleu. Ne change ni ses traits ni sa morphologie. Son expression : l'air satisfait de celui qui sait que le problème est déjà réglé. Scène : la tour d'assiettes. Ta gestion actuelle. Décor : une salle de restaurant en plein service, tables dressées, clients flous en arrière-plan. lumière chaude de fin de journée, reflets dorés. Le chef occupe les deux tiers droits du cadre, en plan poitrine, l'élément comique est visible à gauche. Bande crème #FCF9E6 en haut du cadre sur un cinquième de la hauteur, portant UNIQUEMENT le texte « RÉFÉRENTIELS » en typographie arrondie très grasse, bleu marine #0F1A23, centré. Aucun autre texte, aucun logo ajouté, pas de filigrane, pas de bordure décorative.
```
