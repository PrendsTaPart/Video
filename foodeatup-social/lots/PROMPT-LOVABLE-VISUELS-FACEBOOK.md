# Prompt Lovable — les 150 visuels Facebook

À envoyer **en un seul tour**. Joindre la photo du chef en pièce jointe :
`public/brand/chef-foodeatup.jpg`.

---

## Ce que c'est, et surtout ce que ce n'est pas

Ce ne sont **pas des vignettes**.

Une vignette est une miniature : on la voit avant de cliquer, elle donne envie
d'ouvrir la vidéo, son texte tient en trois mots, et si on ne la lit pas ce
n'est pas grave — la vidéo dira le reste.

Un visuel Facebook **est la publication**. Personne ne clique dessus pour voir
autre chose. Il se regarde dans un fil, sans son, souvent sans que la légende
soit dépliée. Tout ce qu'il y a à comprendre doit donc être **dans l'image** :
la scène, la phrase qui accroche, et la chute.

Le projet contient déjà 150 vignettes dans `public/thumbnails/`. **Ne les
touche pas.** Celles-ci sont un format différent, dans un dossier différent.

## Ce que je te demande

Génère **150 images**, une par épisode.

Le prompt est **déjà écrit** dans les données du projet :

```ts
import { contenuDe } from "@/data/contenu";

contenuDe("EP001").imageFacebook.prompt;
```

Prends-le tel quel, envoie-le à ton générateur **avec la photo du chef en
image de référence**. N'invente pas, ne reformule pas.

## Où déposer les rendus

```
public/facebook/EP001.jpg
public/facebook/EP002.jpg
…
public/facebook/EP150.jpg
```

`src/components/PieceReseau.tsx` va chercher `/facebook/{id}.jpg` et
affiche un emplacement vide tant que le fichier manque.

**JPEG, 1080 × 1350 exactement, qualité 85.** Le 4:5 est le format que
Facebook affiche le plus grand dans un fil mobile ; un 1:1 perd un quart de
la surface, un 16:9 en perd la moitié.

## La composition, identique sur les 150

C'est ce qui fait qu'on reconnaît la série en descendant son fil.

```
┌─────────────────────────────┐
│  bande crème #FCF9E6        │  ← le hook, marine #0F1A23
│  (un cinquième de hauteur)  │     typographie arrondie très grasse
├─────────────────────────────┤
│                             │
│   la scène : le chef à       │  ← il occupe les deux tiers droits
│   droite, l'élément comique  │     l'élément comique est à gauche
│   à gauche                   │
│                             │
├─────────────────────────────┤
│  bandeau marine #0F1A23     │  ← la punchline, crème #FCF9E6
│  (un sixième de hauteur)    │     corps plus petit que le hook
└─────────────────────────────┘
```

## Les quatre interdits

Les mêmes que pour les carrousels, pour les mêmes raisons — trois cents
vignettes déjà produites, dont beaucoup à refaire.

1. **Le chef ne se redessine pas.** Même visage, même barbe, même toque, même
   veste, même tablier au logo FoodEatUp bleu, sur les 150. La photo jointe
   est la source, pas une inspiration.

2. **Pas de noir et blanc, pas de désaturation.** La charte est en couleur.

3. **Aucun logo dessiné par le générateur.** Le seul logo autorisé est celui
   du tablier, qui vient de la photo de référence. Un deuxième logo inventé se
   voit immédiatement.

4. **Une scène par épisode.** Le décor de chacun est décrit dans son prompt.
   Cent cinquante variations de la même cuisine, c'est un fil qu'on arrête de
   regarder au troisième.

## Le texte doit être net

Chaque prompt donne le texte exact des deux bandes, sa couleur et sa place.
Écris **ces mots-là**, sans en ajouter, sans faute, sans lettre déformée.

Si ton générateur rend mal le texte français — accents avalés, lettres
fondues — génère l'image **sans texte** et compose les deux bandes en
HTML/canvas avant d'enregistrer le JPEG. Un texte net vaut mieux qu'un texte
« intégré » qu'on ne peut pas lire.

## Vérification avant de me rendre la main

- [ ] 150 fichiers dans `public/facebook/`, nommés `EPxxx.jpg`
- [ ] tous en 1080 × 1350, tous en JPEG
- [ ] `public/thumbnails/` n'a pas bougé
- [ ] le même chef sur les 150
- [ ] aucune image en niveaux de gris, aucun deuxième logo
- [ ] les deux bandes portent le texte du prompt, sans faute

Un seul tour pour les 150 : ne relance pas épisode par épisode.
