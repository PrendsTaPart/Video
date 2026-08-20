# Lot 5 — vignettes des épisodes EP064 à EP074

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


## EP064 — Le planning au marqueur · « PLANNING SEMAINE »

*Saison 3 · Équipe & Planning · Planning semaine*

```
Photo réaliste, cadrage vertical 9:16. Le chef de l'image de référence — MÊME visage, même barbe, même toque blanche, même veste de cuisine blanche, même tablier blanc au logo FoodEatUp bleu. Ne change ni ses traits ni sa morphologie. Son expression : l'air satisfait de celui qui sait que le problème est déjà réglé. Scène : le planning au marqueur. Le planning de la semaine. Décor : une cuisine professionnelle en pleine brigade, inox, passe-plat, plannings punaisés au mur. lumière blanche et nette de cuisine, vapeur légère. Le chef occupe les deux tiers droits du cadre, en plan poitrine, l'élément comique est visible à gauche. Bande crème #FCF9E6 en haut du cadre sur un cinquième de la hauteur, portant UNIQUEMENT le texte « PLANNING SEMAINE » en typographie arrondie très grasse, bleu marine #0F1A23, centré. Aucun autre texte, aucun logo ajouté, pas de filigrane, pas de bordure décorative.
```

## EP065 — Le stagiaire au bureau · « POINTAGES »

*Saison 3 · Équipe & Planning · Pointages*

```
Photo réaliste, cadrage vertical 9:16. Le chef de l'image de référence — MÊME visage, même barbe, même toque blanche, même veste de cuisine blanche, même tablier blanc au logo FoodEatUp bleu. Ne change ni ses traits ni sa morphologie. Son expression : l'air de quelqu'un qui a déjà vu ça cent fois, un sourcil levé. Scène : le stagiaire au bureau. Qui a accès à quoi ? Décor : une cuisine professionnelle en pleine brigade, inox, passe-plat, plannings punaisés au mur. lumière blanche et nette de cuisine, vapeur légère. Le chef occupe les deux tiers droits du cadre, en plan poitrine, l'élément comique est visible à gauche. Bande crème #FCF9E6 en haut du cadre sur un cinquième de la hauteur, portant UNIQUEMENT le texte « POINTAGES » en typographie arrondie très grasse, bleu marine #0F1A23, centré. Aucun autre texte, aucun logo ajouté, pas de filigrane, pas de bordure décorative.
```

## EP066 — Le grille-pain qui ne répond pas · « CONGÉS »

*Saison 3 · Équipe & Planning · Congés*

```
Photo réaliste, cadrage vertical 9:16. Le chef de l'image de référence — MÊME visage, même barbe, même toque blanche, même veste de cuisine blanche, même tablier blanc au logo FoodEatUp bleu. Ne change ni ses traits ni sa morphologie. Son expression : un sourire en coin, parfaitement serein au milieu du désastre. Scène : le grille-pain qui ne répond pas. Ta cuisine n'a personne à qui parler. Décor : une cuisine professionnelle en pleine brigade, inox, passe-plat, plannings punaisés au mur. lumière blanche et nette de cuisine, vapeur légère. Le chef occupe les deux tiers droits du cadre, en plan poitrine, l'élément comique est visible à gauche. Bande crème #FCF9E6 en haut du cadre sur un cinquième de la hauteur, portant UNIQUEMENT le texte « CONGÉS » en typographie arrondie très grasse, bleu marine #0F1A23, centré. Aucun autre texte, aucun logo ajouté, pas de filigrane, pas de bordure décorative.
```

## EP067 — Le thermomètre humain · « CONTRATS »

*Saison 3 · Équipe & Planning · Contrats*

```
Photo réaliste, cadrage vertical 9:16. Le chef de l'image de référence — MÊME visage, même barbe, même toque blanche, même veste de cuisine blanche, même tablier blanc au logo FoodEatUp bleu. Ne change ni ses traits ni sa morphologie. Son expression : faussement dépité, la main sur le front, mais l'œil qui rit. Scène : le thermomètre humain. Ton relevé de température. Décor : une cuisine professionnelle en pleine brigade, inox, passe-plat, plannings punaisés au mur. lumière blanche et nette de cuisine, vapeur légère. Le chef occupe les deux tiers droits du cadre, en plan poitrine, l'élément comique est visible à gauche. Bande crème #FCF9E6 en haut du cadre sur un cinquième de la hauteur, portant UNIQUEMENT le texte « CONTRATS » en typographie arrondie très grasse, bleu marine #0F1A23, centré. Aucun autre texte, aucun logo ajouté, pas de filigrane, pas de bordure décorative.
```

## EP069 — Le livreur fantôme · « RECRUTEMENT »

*Saison 3 · Équipe & Planning · Recrutement*

```
Photo réaliste, cadrage vertical 9:16. Le chef de l'image de référence — MÊME visage, même barbe, même toque blanche, même veste de cuisine blanche, même tablier blanc au logo FoodEatUp bleu. Ne change ni ses traits ni sa morphologie. Son expression : l'air de quelqu'un qui a déjà vu ça cent fois, un sourcil levé. Scène : le livreur fantôme. Tu as vérifié la livraison ? Décor : une cuisine professionnelle en pleine brigade, inox, passe-plat, plannings punaisés au mur. lumière blanche et nette de cuisine, vapeur légère. Le chef occupe les deux tiers droits du cadre, en plan poitrine, l'élément comique est visible à gauche. Bande crème #FCF9E6 en haut du cadre sur un cinquième de la hauteur, portant UNIQUEMENT le texte « RECRUTEMENT » en typographie arrondie très grasse, bleu marine #0F1A23, centré. Aucun autre texte, aucun logo ajouté, pas de filigrane, pas de bordure décorative.
```

## EP070 — La dalle propre · « ONBOARDING »

*Saison 3 · Équipe & Planning · Onboarding*

```
Photo réaliste, cadrage vertical 9:16. Le chef de l'image de référence — MÊME visage, même barbe, même toque blanche, même veste de cuisine blanche, même tablier blanc au logo FoodEatUp bleu. Ne change ni ses traits ni sa morphologie. Son expression : l'air de quelqu'un qui a déjà vu ça cent fois, un sourcil levé. Scène : la dalle propre. C'est fait. Décor : une cuisine professionnelle en pleine brigade, inox, passe-plat, plannings punaisés au mur. lumière blanche et nette de cuisine, vapeur légère. Le chef occupe les deux tiers droits du cadre, en plan poitrine, l'élément comique est visible à gauche. Bande crème #FCF9E6 en haut du cadre sur un cinquième de la hauteur, portant UNIQUEMENT le texte « ONBOARDING » en typographie arrondie très grasse, bleu marine #0F1A23, centré. Aucun autre texte, aucun logo ajouté, pas de filigrane, pas de bordure décorative.
```

## EP071 — La liste à l'envers · « MULTI-POSTES »

*Saison 3 · Équipe & Planning · Multi-postes*

```
Photo réaliste, cadrage vertical 9:16. Le chef de l'image de référence — MÊME visage, même barbe, même toque blanche, même veste de cuisine blanche, même tablier blanc au logo FoodEatUp bleu. Ne change ni ses traits ni sa morphologie. Son expression : un sourire en coin, parfaitement serein au milieu du désastre. Scène : la liste à l'envers. La check-list du soir. Décor : une cuisine professionnelle en pleine brigade, inox, passe-plat, plannings punaisés au mur. lumière blanche et nette de cuisine, vapeur légère. Le chef occupe les deux tiers droits du cadre, en plan poitrine, l'élément comique est visible à gauche. Bande crème #FCF9E6 en haut du cadre sur un cinquième de la hauteur, portant UNIQUEMENT le texte « MULTI-POSTES » en typographie arrondie très grasse, bleu marine #0F1A23, centré. Aucun autre texte, aucun logo ajouté, pas de filigrane, pas de bordure décorative.
```

## EP072 — Le classeur · « ABSENCES »

*Saison 3 · Équipe & Planning · Absences*

```
Photo réaliste, cadrage vertical 9:16. Le chef de l'image de référence — MÊME visage, même barbe, même toque blanche, même veste de cuisine blanche, même tablier blanc au logo FoodEatUp bleu. Ne change ni ses traits ni sa morphologie. Son expression : faussement dépité, la main sur le front, mais l'œil qui rit. Scène : le classeur. Contrôle sanitaire. Ce matin. Décor : une cuisine professionnelle en pleine brigade, inox, passe-plat, plannings punaisés au mur. lumière blanche et nette de cuisine, vapeur légère. Le chef occupe les deux tiers droits du cadre, en plan poitrine, l'élément comique est visible à gauche. Bande crème #FCF9E6 en haut du cadre sur un cinquième de la hauteur, portant UNIQUEMENT le texte « ABSENCES » en typographie arrondie très grasse, bleu marine #0F1A23, centré. Aucun autre texte, aucun logo ajouté, pas de filigrane, pas de bordure décorative.
```

## EP073 — Pile ou face · « ÉTABLISSEMENT »

*Saison 3 · Configuration · Établissement*

```
Photo réaliste, cadrage vertical 9:16. Le chef de l'image de référence — MÊME visage, même barbe, même toque blanche, même veste de cuisine blanche, même tablier blanc au logo FoodEatUp bleu. Ne change ni ses traits ni sa morphologie. Son expression : l'air satisfait de celui qui sait que le problème est déjà réglé. Scène : pile ou face. Combien tu commandes pour samedi ? Décor : une cuisine professionnelle en pleine brigade, inox, passe-plat, plannings punaisés au mur. lumière blanche et nette de cuisine, vapeur légère. Le chef occupe les deux tiers droits du cadre, en plan poitrine, l'élément comique est visible à gauche. Bande crème #FCF9E6 en haut du cadre sur un cinquième de la hauteur, portant UNIQUEMENT le texte « ÉTABLISSEMENT » en typographie arrondie très grasse, bleu marine #0F1A23, centré. Aucun autre texte, aucun logo ajouté, pas de filigrane, pas de bordure décorative.
```

## EP074 — La liste oubliée · « CATÉGORIES »

*Saison 3 · Configuration · Catégories*

```
Photo réaliste, cadrage vertical 9:16. Le chef de l'image de référence — MÊME visage, même barbe, même toque blanche, même veste de cuisine blanche, même tablier blanc au logo FoodEatUp bleu. Ne change ni ses traits ni sa morphologie. Son expression : l'air de quelqu'un qui a déjà vu ça cent fois, un sourcil levé. Scène : la liste oubliée. Tu as oublié la liste. Décor : une cuisine professionnelle en pleine brigade, inox, passe-plat, plannings punaisés au mur. lumière blanche et nette de cuisine, vapeur légère. Le chef occupe les deux tiers droits du cadre, en plan poitrine, l'élément comique est visible à gauche. Bande crème #FCF9E6 en haut du cadre sur un cinquième de la hauteur, portant UNIQUEMENT le texte « CATÉGORIES » en typographie arrondie très grasse, bleu marine #0F1A23, centré. Aucun autre texte, aucun logo ajouté, pas de filigrane, pas de bordure décorative.
```
