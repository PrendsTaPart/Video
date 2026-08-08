# Volet « sans FoodEatUp » — dossier de relecture juridique

À remettre à l'avocat **avant toute diffusion**, avec les neuf fichiers rendus.
NOTES §6.1 : ces films seront vus par les concurrents, et un seul plan ambigu
suffit à faire basculer le registre ironique en dénigrement.

## Le raisonnement de fond

Le texte des neuf films ne dit jamais qu'un logiciel du marché est mauvais. Il
dit : **vous en avez sept, et aucun ne parle aux autres.** La cible n'est pas un
acteur, c'est la dispersion. Aucun concurrent n'est donc désigné, ni nommé, ni
montré — ce qui, si le raisonnement tient, place les films hors du champ de la
publicité comparative des art. L122-1 et L122-2 du Code de la consommation.
C'est ce point que la relecture doit confirmer ou infirmer.

## Ce qui a été fait pour tenir cette ligne

**Toutes les interfaces à l'écran sont dessinées par nous.** Aucune capture
d'un logiciel tiers n'entre dans ces films, à aucun moment. Les maquettes sont
générées par `_serie/serie_sans.py` : rectangles gris `#8A9099`, typographie
système, aucun logo, aucune couleur d'éditeur, aucune disposition copiée d'un
produit existant.

**Les libellés désignent une fonction, jamais un produit.** « Tableur de
stock », « Cahier de cuisine », « Boîte mail », « Portail déclaratif ». Aucun
n'est assez étroit pour ne désigner qu'un seul acteur du marché. La liste
complète est dans `_serie/films_sans.py` (`ONGLETS`, `outils1`, `outils2`).

**Tous les chiffres sont des fourchettes** (§6.2) : 5 à 8 abonnements, 350 à
900 €/mois, 20 à 45 min par service selon les films. Aucune valeur unique,
aucun prix attribué à un acteur identifiable. **Ces fourchettes doivent être
sourcées avant diffusion** — une publicité comparative doit être vérifiable, et
la source n'est aujourd'hui pas documentée. C'est le point le plus faible du
dossier.

**Aucune marque n'est prononcée** en dehors de « FoodEatUp », dans le hook
d'ouverture et le carton final. Textes intégraux dans `_serie/films_sans.py`.

## Points à examiner en priorité

### 1. Le plan `sept-onglets` (photo, carton final de D1′ et D2′)

Écran d'ordinateur portable dans une pièce sombre, sept onglets de navigateur
ouverts, pense-bête collé au bord de l'écran.

Relu au zoom ×3,5 : les libellés d'onglets sont du **faux texte illisible**
produit par le modèle, les favicons sont des ronds gris uniformes, le
pense-bête porte une écriture manuscrite sans mot lisible. Le chrome du
navigateur est générique.

Un floutage de la barre a été essayé puis abandonné : il effaçait les onglets,
et un plan qui dit « sept onglets » sans qu'on puisse les compter ne dit plus
rien. **Le plan est donc monté en clair.** C'est le seul endroit de tout le
volet où un navigateur est visible ; à trancher.

### 2. Le plan `sans-onglets` (animé, ouverture de D1′ et D3′)

Même sujet en mouvement : le directeur devant son écran le soir. Fenêtres
empilées, texte illisible à l'image, aucun logo. Même question que ci-dessus.

### 3. Le plan `sans-tablettes` (animé, ouverture de S2′)

Trois tablettes dépareillées derrière un comptoir, chacune affichant une
interface grise unie. Générées avec la consigne explicite `no invented
software interface` : les écrans sont des aplats. À confirmer visuellement.

### 4. Les fourchettes chiffrées

Voir plus haut. Elles sont défendables dans leur forme, pas encore dans leur
source.

## Ce qui reste dû

- [ ] **`no-competitor-check.ts`** — échoue si un nom de marque apparaît dans
  un fichier du volet « sans » ou dans les champs `sans.*` des parcours.
  **Michael doit fournir la liste des marques à surveiller** ; le contrôle
  n'est pas écrit tant que la liste n'existe pas, parce qu'un contrôle avec une
  liste inventée donnerait une fausse assurance.
- [ ] **Sourcer les fourchettes** de 5–8 abonnements et 350–900 €/mois.
- [ ] **Relecture par un avocat**, ce document en main, avec les neuf fichiers.

## Inventaire des sources image

Aucun plan n'a été tourné pour ce volet : tout vient de la bibliothèque
Higgsfield déjà constituée, ré-étalonné au registre « sans » (désaturé, froid,
contraste écrasé) par `_serie/plans-sans.sh` et `_serie/photos-sans.sh`.

**La bibliothèque RapidoCMS n'a fourni aucune image.** Vérification faite sur
ses 691 fichiers : ce sont des visuels de marque FoodEatUp — palette bleue,
chef souriant, tableaux de bord lumineux — ou des vignettes de tutoriels
FoodEatUp. Aucun n'est montable dans un film qui raconte l'absence du produit,
et aucun n'est neutre au sens du §6.1.
