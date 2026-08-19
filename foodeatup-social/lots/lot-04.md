# Lot 4 — vignettes des épisodes EP038 à EP063

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


## EP038 — Le chariot fou · « MA LISTE COURSES »

*Saison 2 · StockVision · 4 - Ma liste de courses*

```
Photo réaliste, cadrage vertical 9:16. Le chef de l'image de référence — MÊME visage, même barbe, même toque blanche, même veste de cuisine blanche, même tablier blanc au logo FoodEatUp bleu. Ne change ni ses traits ni sa morphologie. Son expression : l'air de quelqu'un qui a déjà vu ça cent fois, un sourcil levé. Scène : le chariot fou. Le réappro du lundi. Décor : un bureau d'arrière-salle, classeurs, tickets de caisse, calculatrice, cartons de livraison. lumière rasante de néon adouci, ambiance fin de mois. Le chef occupe les deux tiers droits du cadre, en plan poitrine, l'élément comique est visible à gauche. Bande crème #FCF9E6 en haut du cadre sur un cinquième de la hauteur, portant UNIQUEMENT le texte « MA LISTE COURSES » en typographie arrondie très grasse, bleu marine #0F1A23, centré. Aucun autre texte, aucun logo ajouté, pas de filigrane, pas de bordure décorative.
```

## EP039 — Le ballon dans la soupe · « GÉRER ET NO-SHOWS »

*Saison 2 · Réservation · 3 - Gérer et no-shows*

```
Photo réaliste, cadrage vertical 9:16. Le chef de l'image de référence — MÊME visage, même barbe, même toque blanche, même veste de cuisine blanche, même tablier blanc au logo FoodEatUp bleu. Ne change ni ses traits ni sa morphologie. Son expression : un sourire en coin, parfaitement serein au milieu du désastre. Scène : le ballon dans la soupe. L'imprévu du service. Décor : un bureau d'arrière-salle, classeurs, tickets de caisse, calculatrice, cartons de livraison. lumière rasante de néon adouci, ambiance fin de mois. Le chef occupe les deux tiers droits du cadre, en plan poitrine, l'élément comique est visible à gauche. Bande crème #FCF9E6 en haut du cadre sur un cinquième de la hauteur, portant UNIQUEMENT le texte « GÉRER ET NO-SHOWS » en typographie arrondie très grasse, bleu marine #0F1A23, centré. Aucun autre texte, aucun logo ajouté, pas de filigrane, pas de bordure décorative.
```

## EP040 — La chèvre au potager · « AJOUTER UN MOUVEMENT »

*Saison 2 · StockVision · 17 - Ajouter un mouvement*

```
Photo réaliste, cadrage vertical 9:16. Le chef de l'image de référence — MÊME visage, même barbe, même toque blanche, même veste de cuisine blanche, même tablier blanc au logo FoodEatUp bleu. Ne change ni ses traits ni sa morphologie. Son expression : un sourire en coin, parfaitement serein au milieu du désastre. Scène : la chèvre au potager. Ton stock de basilic. Décor : un bureau d'arrière-salle, classeurs, tickets de caisse, calculatrice, cartons de livraison. lumière rasante de néon adouci, ambiance fin de mois. Le chef occupe les deux tiers droits du cadre, en plan poitrine, l'élément comique est visible à gauche. Bande crème #FCF9E6 en haut du cadre sur un cinquième de la hauteur, portant UNIQUEMENT le texte « AJOUTER UN MOUVEMENT » en typographie arrondie très grasse, bleu marine #0F1A23, centré. Aucun autre texte, aucun logo ajouté, pas de filigrane, pas de bordure décorative.
```

## EP041 — Le poulet fugueur · « SORTIE INGRÉDIENTS PRODUCTION »

*Saison 2 · StockVision · 15 - Sortie des ingrédients de la production*

```
Photo réaliste, cadrage vertical 9:16. Le chef de l'image de référence — MÊME visage, même barbe, même toque blanche, même veste de cuisine blanche, même tablier blanc au logo FoodEatUp bleu. Ne change ni ses traits ni sa morphologie. Son expression : faussement dépité, la main sur le front, mais l'œil qui rit. Scène : le poulet fugueur. Ton contrôle des portions. Décor : un bureau d'arrière-salle, classeurs, tickets de caisse, calculatrice, cartons de livraison. lumière rasante de néon adouci, ambiance fin de mois. Le chef occupe les deux tiers droits du cadre, en plan poitrine, l'élément comique est visible à gauche. Bande crème #FCF9E6 en haut du cadre sur un cinquième de la hauteur, portant UNIQUEMENT le texte « SORTIE INGRÉDIENTS PRODUCTION » en typographie arrondie très grasse, bleu marine #0F1A23, centré. Aucun autre texte, aucun logo ajouté, pas de filigrane, pas de bordure décorative.
```

## EP042 — La nappe et le vent · « MCP RAPIDOCMS IRIS »

*Saison 2 · Marketing · 21 - MCP RapidoCMS et Iris*

```
Photo réaliste, cadrage vertical 9:16. Le chef de l'image de référence — MÊME visage, même barbe, même toque blanche, même veste de cuisine blanche, même tablier blanc au logo FoodEatUp bleu. Ne change ni ses traits ni sa morphologie. Son expression : l'air satisfait de celui qui sait que le problème est déjà réglé. Scène : la nappe et le vent. Tout faire seul. Décor : un bureau d'arrière-salle, classeurs, tickets de caisse, calculatrice, cartons de livraison. lumière rasante de néon adouci, ambiance fin de mois. Le chef occupe les deux tiers droits du cadre, en plan poitrine, l'élément comique est visible à gauche. Bande crème #FCF9E6 en haut du cadre sur un cinquième de la hauteur, portant UNIQUEMENT le texte « MCP RAPIDOCMS IRIS » en typographie arrondie très grasse, bleu marine #0F1A23, centré. Aucun autre texte, aucun logo ajouté, pas de filigrane, pas de bordure décorative.
```

## EP044 — Les six stylos · « COMMANDER PAR QR »

*Saison 2 · Réservation · 5 - Commander par QR code*

```
Photo réaliste, cadrage vertical 9:16. Le chef de l'image de référence — MÊME visage, même barbe, même toque blanche, même veste de cuisine blanche, même tablier blanc au logo FoodEatUp bleu. Ne change ni ses traits ni sa morphologie. Son expression : un sourire en coin, parfaitement serein au milieu du désastre. Scène : les six stylos. Prendre la commande en 2026. Décor : un bureau d'arrière-salle, classeurs, tickets de caisse, calculatrice, cartons de livraison. lumière rasante de néon adouci, ambiance fin de mois. Le chef occupe les deux tiers droits du cadre, en plan poitrine, l'élément comique est visible à gauche. Bande crème #FCF9E6 en haut du cadre sur un cinquième de la hauteur, portant UNIQUEMENT le texte « COMMANDER PAR QR » en typographie arrondie très grasse, bleu marine #0F1A23, centré. Aucun autre texte, aucun logo ajouté, pas de filigrane, pas de bordure décorative.
```

## EP045 — La chambre froide · « STATISTIQUES PAR MODULE »

*Saison 2 · StockVision · 18 - Statistiques par module*

```
Photo réaliste, cadrage vertical 9:16. Le chef de l'image de référence — MÊME visage, même barbe, même toque blanche, même veste de cuisine blanche, même tablier blanc au logo FoodEatUp bleu. Ne change ni ses traits ni sa morphologie. Son expression : faussement dépité, la main sur le front, mais l'œil qui rit. Scène : la chambre froide. Personne ne sait où tu es. Décor : un bureau d'arrière-salle, classeurs, tickets de caisse, calculatrice, cartons de livraison. lumière rasante de néon adouci, ambiance fin de mois. Le chef occupe les deux tiers droits du cadre, en plan poitrine, l'élément comique est visible à gauche. Bande crème #FCF9E6 en haut du cadre sur un cinquième de la hauteur, portant UNIQUEMENT le texte « STATISTIQUES PAR MODULE » en typographie arrondie très grasse, bleu marine #0F1A23, centré. Aucun autre texte, aucun logo ajouté, pas de filigrane, pas de bordure décorative.
```

## EP061 — Le badge introuvable · « RAPPORT HACCP »

*Saison 3 · HACCP · Rapport HACCP*

```
Photo réaliste, cadrage vertical 9:16. Le chef de l'image de référence — MÊME visage, même barbe, même toque blanche, même veste de cuisine blanche, même tablier blanc au logo FoodEatUp bleu. Ne change ni ses traits ni sa morphologie. Son expression : l'air de quelqu'un qui a déjà vu ça cent fois, un sourcil levé. Scène : le badge introuvable. Ton système de pointage. Décor : une cuisine professionnelle en pleine brigade, inox, passe-plat, plannings punaisés au mur. lumière blanche et nette de cuisine, vapeur légère. Le chef occupe les deux tiers droits du cadre, en plan poitrine, l'élément comique est visible à gauche. Bande crème #FCF9E6 en haut du cadre sur un cinquième de la hauteur, portant UNIQUEMENT le texte « RAPPORT HACCP » en typographie arrondie très grasse, bleu marine #0F1A23, centré. Aucun autre texte, aucun logo ajouté, pas de filigrane, pas de bordure décorative.
```

## EP062 — La photo de pointage · « ROUTINE DU JOUR »

*Saison 3 · HACCP · Routine du jour*

```
Photo réaliste, cadrage vertical 9:16. Le chef de l'image de référence — MÊME visage, même barbe, même toque blanche, même veste de cuisine blanche, même tablier blanc au logo FoodEatUp bleu. Ne change ni ses traits ni sa morphologie. Son expression : un sourire en coin, parfaitement serein au milieu du désastre. Scène : la photo de pointage. Je te jure, j'étais là à 8 h. Décor : une cuisine professionnelle en pleine brigade, inox, passe-plat, plannings punaisés au mur. lumière blanche et nette de cuisine, vapeur légère. Le chef occupe les deux tiers droits du cadre, en plan poitrine, l'élément comique est visible à gauche. Bande crème #FCF9E6 en haut du cadre sur un cinquième de la hauteur, portant UNIQUEMENT le texte « ROUTINE DU JOUR » en typographie arrondie très grasse, bleu marine #0F1A23, centré. Aucun autre texte, aucun logo ajouté, pas de filigrane, pas de bordure décorative.
```

## EP063 — Le post-it perdu · « CRÉER UN EMPLOYÉ »

*Saison 3 · Équipe & Planning · Créer un employé*

```
Photo réaliste, cadrage vertical 9:16. Le chef de l'image de référence — MÊME visage, même barbe, même toque blanche, même veste de cuisine blanche, même tablier blanc au logo FoodEatUp bleu. Ne change ni ses traits ni sa morphologie. Son expression : faussement dépité, la main sur le front, mais l'œil qui rit. Scène : le post-it perdu. Ta demande de congé. Décor : une cuisine professionnelle en pleine brigade, inox, passe-plat, plannings punaisés au mur. lumière blanche et nette de cuisine, vapeur légère. Le chef occupe les deux tiers droits du cadre, en plan poitrine, l'élément comique est visible à gauche. Bande crème #FCF9E6 en haut du cadre sur un cinquième de la hauteur, portant UNIQUEMENT le texte « CRÉER UN EMPLOYÉ » en typographie arrondie très grasse, bleu marine #0F1A23, centré. Aucun autre texte, aucun logo ajouté, pas de filigrane, pas de bordure décorative.
```
