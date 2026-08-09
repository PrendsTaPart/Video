# Les seize tutoriels sans rush

Les seize dernières fiches du catalogue étaient des coquilles : leur
`howItWorks` disait « Cette vidéo est en cours de tournage », leur `whatItsFor`
répétait le titre. Elles le sont restées parce qu'elles attendaient un rush —
une capture d'écran du produit — que personne n'avait tournée.

Ce dossier les livre **en motion design, en attendant**. Les films sont
remplaçables ; les scripts, non — c'est eux le travail long.

## Ce que ces films sont, et ne sont pas

**Aucun plan ne prétend être une capture d'écran.** Une planche schématique dit
« voici l'étape, voici ce qui compte » ; une fausse interface dirait « voici le
produit », ce qui serait faux tant que le rush n'existe pas. Le jour où le rush
arrive, on remonte le film sur la chaîne habituelle et le script ne bouge pas.

**Le contenu vient du connecteur MCP, pas de l'imagination.** Chaque outil porte
sa description, ses paramètres et ses contraintes : `record_pos_payment` dit que
le titre-restaurant ne rend jamais la monnaie, `close_pos_session` qu'il exige
une confirmation après avoir résumé le rapport X, `get_hubrise_status` qu'un
plat sans `sku_ref` est bloqué au push. Ce sont des faits du produit. C'est ce
qui sépare un tutoriel utile d'une paraphrase de menu.

**Un tutoriel a été réangle.** `retrouver-toutes-mes-commandes` portait le même
sujet que `mes-commandes-tous-canaux` et `retrouver-ses-commandes-multi-canal`,
tous deux déjà en ligne. Une troisième page sur la même intention se serait
cannibalisée avec les deux autres — exactement ce que le travail de
référencement combat. Elle devient « Retrouver la commande derrière une
facture », son angle comptable.

## L'image

Onze films ouvrent sur un **plan réel de la bibliothèque** — déjà tourné, déjà
payé, déjà ré-encodé au standard de la série. Aucune génération : les réutiliser
donne aux seize films la même image que les dix-huit déjà en ligne, et c'est la
même série.

Cinq sujets n'existaient pas dans cette bibliothèque, tournée pour une journée
de restaurant : livreur, roue cadeaux, connecteurs. Ils reçoivent une
**illustration fabriquée sur RapidoCMS**, animée en lent zoom.

⚠️ **Aucune marque tierce n'est visible dans les plans que ce dossier
fabrique.** « Uber Eats » et « Deliveroo » sont nommés dans le titre d'un
tutoriel — c'est un fait, et le dire est légitime. Le scooter et le sac
isotherme de l'illustration sont entièrement neutres.

La réserve porte ailleurs : **le carton d'intro Drive de ce tutoriel-là, lui,
affiche les deux logos.** C'est un asset FoodEatUp existant, tourné hors de ce
dossier et déjà utilisé par les tutoriels en ligne — il est repris tel quel,
pas retouché ici. Citer une marque pour décrire une interopérabilité réelle est
un usage nominatif défendable ; reproduire son logo relève en revanche des
chartes de marque d'Uber Eats et de Deliveroo, qui demandent une autorisation.
**À vérifier côté FoodEatUp**, pour ce carton comme pour les autres de la série
qui feraient de même — ce n'est pas une décision de montage.

## Le module Caisse POS reste en brouillon

Sept des seize appartiennent à `caisse-pos`, que le site annonce comme
« en préparation par notre équipe de développeurs · arrive en v2 ».

Ses huit outils MCP existent pourtant, et sont détaillés. La fonction est donc
là côté API. Mais **basculer un module en production n'est pas une décision de
montage** : publier sept tutoriels sous un module que le site annonce comme non
livré ferait dire au site deux choses contraires le même jour.

Les sept fiches reçoivent donc leur contenu réel et **restent en brouillon**.
Le jour où l'indicateur du module tombe, elles sont prêtes : un statut à
changer, pas un texte à écrire.

## La chaîne

```
1.  _tuto/scripts.py            la source : seize scripts, voix off, prompts
2.  _tuto/ecrire-scripts.py     → <sous>/SCRIPT.md, la vue lisible
3.  _tuto/vo.py                 → <sous>/assets/{vo.mp3, timing.json}
4.  _tuto/monter.py             → studio-video/compositions/<sous>{,.html}
5.  npx hyperframes lint        doit être à 0 erreur
6.  _tuto/rendre.sh             → <sous>/out/<sous>.mp4, avec contrôle
7.  _tuto/vignettes.py          → _vignettes/tuto-<slug>-thumbnail.jpg
8.  _tuto/remplir-fiches.py     → tutorials.ts + fiches.sql
```

## La vignette porte le nom que la bibliothèque attend

Le film est `tuto-<slug>-v1`, sa vignette `tuto-<slug>-thumbnail` : le `-v1` est
**remplacé**, jamais suffixé. Cent vingt et une des cent vingt-quatre fiches
déjà en ligne le font ainsi, et une vignette mal nommée ne casse rien — elle
laisse simplement une tuile creuse dans la grille, ce qui ne se voit qu'au
chargement du catalogue.

Quinze vignettes sont les cartons d'intro officiels récupérés sur le Drive,
ramenés au format de la bibliothèque (1280×720, ~100 ko — relevé sur une
vignette en ligne, et non sur le film : une tuile de catalogue servie en
1920×1080 ferait payer trois fois le poids utile à chaque visiteur).

La seizième n'a pas de carton — `retrouver-toutes-mes-commandes` a été réanglée
après le tournage des intros. Elle est **extraite de son propre film**, donc à
la même charte par construction.

**Le sens du montage est inversé, et c'est délibéré.** On ne génère pas une voix
d'un bloc pour y relever ensuite des bornes à la lecture : chaque segment est
généré séparément, donc sa durée est *mesurée*, et la scène qui le porte dure
exactement ce segment plus sa respiration. Les bornes ne sont pas déduites du
montage, c'est le montage qui est déduit des bornes. Il devient impossible
qu'une scène s'arrête avant sa phrase — le défaut le plus courant d'un montage
sur estimation, et celui qui ne se voit qu'au visionnage complet.

## Pièges payés une fois

- **Un clip imbriqué déclare sa durée en temps absolu du film**, pas en temps
  local de sa scène. Une scène qui commence à `A` et dure `D` déclare
  `data-duration = A + D`.
- **Les durées écrites dans le HTML sont dérivées des débuts arrondis**, jamais
  arrondies séparément : `18,226 + 4,107 = 22,333` s'écrit sinon « 18.23 » et
  « 4.11 », donc une fin à 22,34 pour un voisin qui commence à 22,33, et le lint
  refuse — à raison, deux scènes seraient visibles ensemble pendant une image.
- **GSAP réécrit tout le `transform`** dès qu'il anime `y` ou `scale`. Les
  cartes sont centrées par `align-items`, jamais par `translateY(-50%)`.
- **Le Chrome de rendu vit dans `~/.cache`.** Le vider pour récupérer du disque
  laisse le binaire sans ses données ICU, et l'outil accuse alors des
  bibliothèques système absentes qui, elles, sont parfaitement là.
  `npx hyperframes browser ensure` le réinstalle.
