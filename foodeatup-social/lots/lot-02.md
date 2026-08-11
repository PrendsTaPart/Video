# Lot 2 — vignettes des épisodes EP016 à EP025

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


## EP016 — Le geyser à café · « DÉPENSES »

*Saison 1 · Comptabilité · dépenses*

```
Photo réaliste, cadrage vertical 9:16. Le chef de l'image de référence — MÊME visage, même barbe, même toque blanche, même veste de cuisine blanche, même tablier blanc au logo FoodEatUp bleu. Ne change ni ses traits ni sa morphologie. Son expression : l'air de quelqu'un qui a déjà vu ça cent fois, un sourcil levé. Scène : le geyser à café. Tes coûts, ce trimestre. Décor : une salle de restaurant en plein service, tables dressées, clients flous en arrière-plan. lumière chaude de fin de journée, reflets dorés. Le chef occupe les deux tiers droits du cadre, en plan poitrine, l'élément comique est visible à gauche. Bande crème #FCF9E6 en haut du cadre sur un cinquième de la hauteur, portant UNIQUEMENT le texte « DÉPENSES » en typographie arrondie très grasse, bleu marine #0F1A23, centré. Aucun autre texte, aucun logo ajouté, pas de filigrane, pas de bordure décorative.
```

## EP017 — Le ninja de la frite · « CRÉATION D'UN RAPPORT »

*Saison 1 · StockVision · 19 - Création d'un rapport*

```
Photo réaliste, cadrage vertical 9:16. Le chef de l'image de référence — MÊME visage, même barbe, même toque blanche, même veste de cuisine blanche, même tablier blanc au logo FoodEatUp bleu. Ne change ni ses traits ni sa morphologie. Son expression : un sourire en coin, parfaitement serein au milieu du désastre. Scène : le ninja de la frite. Personne ne touche à ta dernière frite. Décor : une salle de restaurant en plein service, tables dressées, clients flous en arrière-plan. lumière chaude de fin de journée, reflets dorés. Le chef occupe les deux tiers droits du cadre, en plan poitrine, l'élément comique est visible à gauche. Bande crème #FCF9E6 en haut du cadre sur un cinquième de la hauteur, portant UNIQUEMENT le texte « CRÉATION D'UN RAPPORT » en typographie arrondie très grasse, bleu marine #0F1A23, centré. Aucun autre texte, aucun logo ajouté, pas de filigrane, pas de bordure décorative.
```

## EP018 — Le serveur Baywatch · « SITE »

*Saison 1 · Service · 2 - Site, vocal et QR code*

```
Photo réaliste, cadrage vertical 9:16. Le chef de l'image de référence — MÊME visage, même barbe, même toque blanche, même veste de cuisine blanche, même tablier blanc au logo FoodEatUp bleu. Ne change ni ses traits ni sa morphologie. Son expression : faussement dépité, la main sur le front, mais l'œil qui rit. Scène : le serveur baywatch. Le rush de vingt heures. Décor : une salle de restaurant en plein service, tables dressées, clients flous en arrière-plan. lumière chaude de fin de journée, reflets dorés. Le chef occupe les deux tiers droits du cadre, en plan poitrine, l'élément comique est visible à gauche. Bande crème #FCF9E6 en haut du cadre sur un cinquième de la hauteur, portant UNIQUEMENT le texte « SITE » en typographie arrondie très grasse, bleu marine #0F1A23, centré. Aucun autre texte, aucun logo ajouté, pas de filigrane, pas de bordure décorative.
```

## EP019 — Le burger qui rebondit · « PRÉDICTIONS DES COMMANDES »

*Saison 1 · StockVision · 3 - Prédictions des commandes*

```
Photo réaliste, cadrage vertical 9:16. Le chef de l'image de référence — MÊME visage, même barbe, même toque blanche, même veste de cuisine blanche, même tablier blanc au logo FoodEatUp bleu. Ne change ni ses traits ni sa morphologie. Son expression : l'air satisfait de celui qui sait que le problème est déjà réglé. Scène : le burger qui rebondit. Ton chiffre d'affaires, sans outil. Décor : une salle de restaurant en plein service, tables dressées, clients flous en arrière-plan. lumière chaude de fin de journée, reflets dorés. Le chef occupe les deux tiers droits du cadre, en plan poitrine, l'élément comique est visible à gauche. Bande crème #FCF9E6 en haut du cadre sur un cinquième de la hauteur, portant UNIQUEMENT le texte « PRÉDICTIONS DES COMMANDES » en typographie arrondie très grasse, bleu marine #0F1A23, centré. Aucun autre texte, aucun logo ajouté, pas de filigrane, pas de bordure décorative.
```

## EP020 — Le chien qui a réservé · « AJOUTER UNE RÉSERVATION »

*Saison 1 · Réservation · 2 - Ajouter une réservation*

```
Photo réaliste, cadrage vertical 9:16. Le chef de l'image de référence — MÊME visage, même barbe, même toque blanche, même veste de cuisine blanche, même tablier blanc au logo FoodEatUp bleu. Ne change ni ses traits ni sa morphologie. Son expression : l'air satisfait de celui qui sait que le problème est déjà réglé. Scène : le chien qui a réservé. Lui, il a réservé. Décor : une salle de restaurant en plein service, tables dressées, clients flous en arrière-plan. lumière chaude de fin de journée, reflets dorés. Le chef occupe les deux tiers droits du cadre, en plan poitrine, l'élément comique est visible à gauche. Bande crème #FCF9E6 en haut du cadre sur un cinquième de la hauteur, portant UNIQUEMENT le texte « AJOUTER UNE RÉSERVATION » en typographie arrondie très grasse, bleu marine #0F1A23, centré. Aucun autre texte, aucun logo ajouté, pas de filigrane, pas de bordure décorative.
```

## EP021 — Chef contre imprimante · « CRÉER TES POSTES »

*Saison 1 · KDS · 1 - Créer tes postes KDS*

```
Photo réaliste, cadrage vertical 9:16. Le chef de l'image de référence — MÊME visage, même barbe, même toque blanche, même veste de cuisine blanche, même tablier blanc au logo FoodEatUp bleu. Ne change ni ses traits ni sa morphologie. Son expression : l'air de quelqu'un qui a déjà vu ça cent fois, un sourcil levé. Scène : chef contre imprimante. Le vrai ennemi du service. Décor : une salle de restaurant en plein service, tables dressées, clients flous en arrière-plan. lumière chaude de fin de journée, reflets dorés. Le chef occupe les deux tiers droits du cadre, en plan poitrine, l'élément comique est visible à gauche. Bande crème #FCF9E6 en haut du cadre sur un cinquième de la hauteur, portant UNIQUEMENT le texte « CRÉER TES POSTES » en typographie arrondie très grasse, bleu marine #0F1A23, centré. Aucun autre texte, aucun logo ajouté, pas de filigrane, pas de bordure décorative.
```

## EP022 — La facture qui fait pleurer · « MARKETPLACE DE PROMPTS »

*Saison 1 · PrediBot · 2 - Marketplace de prompts*

```
Photo réaliste, cadrage vertical 9:16. Le chef de l'image de référence — MÊME visage, même barbe, même toque blanche, même veste de cuisine blanche, même tablier blanc au logo FoodEatUp bleu. Ne change ni ses traits ni sa morphologie. Son expression : un sourire en coin, parfaitement serein au milieu du désastre. Scène : la facture qui fait pleurer. Mille euros par mois. Décor : une salle de restaurant en plein service, tables dressées, clients flous en arrière-plan. lumière chaude de fin de journée, reflets dorés. Le chef occupe les deux tiers droits du cadre, en plan poitrine, l'élément comique est visible à gauche. Bande crème #FCF9E6 en haut du cadre sur un cinquième de la hauteur, portant UNIQUEMENT le texte « MARKETPLACE DE PROMPTS » en typographie arrondie très grasse, bleu marine #0F1A23, centré. Aucun autre texte, aucun logo ajouté, pas de filigrane, pas de bordure décorative.
```

## EP023 — L'aspirateur robot · « CALENDRIER IA AVEC »

*Saison 1 · Marketing · 24 - Calendrier IA avec Iris*

```
Photo réaliste, cadrage vertical 9:16. Le chef de l'image de référence — MÊME visage, même barbe, même toque blanche, même veste de cuisine blanche, même tablier blanc au logo FoodEatUp bleu. Ne change ni ses traits ni sa morphologie. Son expression : faussement dépité, la main sur le front, mais l'œil qui rit. Scène : l'aspirateur robot. Ton automatisation actuelle. Décor : une salle de restaurant en plein service, tables dressées, clients flous en arrière-plan. lumière chaude de fin de journée, reflets dorés. Le chef occupe les deux tiers droits du cadre, en plan poitrine, l'élément comique est visible à gauche. Bande crème #FCF9E6 en haut du cadre sur un cinquième de la hauteur, portant UNIQUEMENT le texte « CALENDRIER IA AVEC » en typographie arrondie très grasse, bleu marine #0F1A23, centré. Aucun autre texte, aucun logo ajouté, pas de filigrane, pas de bordure décorative.
```

## EP024 — La mouette braqueuse · « CRÉER SITE PAR »

*Saison 1 · Mon Site · 5 - Créer un site par IA*

```
Photo réaliste, cadrage vertical 9:16. Le chef de l'image de référence — MÊME visage, même barbe, même toque blanche, même veste de cuisine blanche, même tablier blanc au logo FoodEatUp bleu. Ne change ni ses traits ni sa morphologie. Son expression : l'air satisfait de celui qui sait que le problème est déjà réglé. Scène : la mouette braqueuse. Encore une commission en moins. Décor : une salle de restaurant en plein service, tables dressées, clients flous en arrière-plan. lumière chaude de fin de journée, reflets dorés. Le chef occupe les deux tiers droits du cadre, en plan poitrine, l'élément comique est visible à gauche. Bande crème #FCF9E6 en haut du cadre sur un cinquième de la hauteur, portant UNIQUEMENT le texte « CRÉER SITE PAR » en typographie arrondie très grasse, bleu marine #0F1A23, centré. Aucun autre texte, aucun logo ajouté, pas de filigrane, pas de bordure décorative.
```

## EP025 — Le mixeur sans couvercle · « CAMPAGNE 100 % »

*Saison 1 · Marketing · 6 - Campagne 100 % IA*

```
Photo réaliste, cadrage vertical 9:16. Le chef de l'image de référence — MÊME visage, même barbe, même toque blanche, même veste de cuisine blanche, même tablier blanc au logo FoodEatUp bleu. Ne change ni ses traits ni sa morphologie. Son expression : l'air de quelqu'un qui a déjà vu ça cent fois, un sourcil levé. Scène : le mixeur sans couvercle. Quand tu lances une promo sans données. Décor : une salle de restaurant en plein service, tables dressées, clients flous en arrière-plan. lumière chaude de fin de journée, reflets dorés. Le chef occupe les deux tiers droits du cadre, en plan poitrine, l'élément comique est visible à gauche. Bande crème #FCF9E6 en haut du cadre sur un cinquième de la hauteur, portant UNIQUEMENT le texte « CAMPAGNE 100 % » en typographie arrondie très grasse, bleu marine #0F1A23, centré. Aucun autre texte, aucun logo ajouté, pas de filigrane, pas de bordure décorative.
```
