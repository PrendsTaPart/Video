# Prompt Lovable — les images des séries « Une journée » et « L'IA dans FoodEatUp »

À envoyer **en un seul tour**. Joindre en pièce jointe :
`public/brand/chef-foodeatup.jpg`.

---

## Ce qui est nouveau, et pourquoi ça change les images

Le projet contenait une série — *Le Coup de Feu*, 240 épisodes. Il en contient
trois. Les deux nouvelles n'ont **ni le même sujet, ni le même personnage, ni
la même charte**, et c'est délibéré : les traiter comme la première produirait
des images fausses.

| Série | Personnage | Charte | Ce qu'on filme |
|---|---|---|---|
| Le Coup de Feu | le chef FoodEatUp | crème + marine | une scène comique |
| **Une journée** | **dix métiers différents** | marine + crème | **un poste de travail, sans logiciel** |
| **L'IA dans FoodEatUp** | le chef FoodEatUp | **RapidoCMS — bleu #03A9F5, gris #383838, blanc** | un objet réel qui change d'état |

## Ce qu'il y a à générer

| Quoi | Combien | Où |
|---|---|---|
| Vignettes — Une journée | 31 | `public/thumbnails/EP301.jpg` … `EP331.jpg` |
| Vignettes — L'IA dans FoodEatUp | 31 | `public/thumbnails/EP401.jpg` … `EP431.jpg` |
| Planches de carrousel LinkedIn | 248 — 4 par épisode | `public/carrousels/EPxxx-n.jpg` |
| Visuels Facebook | 62 | `public/facebook/EPxxx.jpg` |

**372 images.** JPEG uniquement — le convertisseur PDF du site embarque le flux
JPEG tel quel (`/DCTDecode`), un PNG produirait un carrousel de pages blanches.
Vignettes en **1080 × 1920** (9:16), carrousels et visuels en **1080 × 1350**
(4:5), qualité 85.

## Les prompts existent déjà — ne les réécris pas

```ts
import { contenuDe } from "@/data/contenu";
import { series } from "@/data/series";

const ep = series.find(s => s.slug === "une-journee")!
  .saisons.flatMap(sa => sa.episodes).find(e => e.id === "EP301")!;

ep.promptVignette;                      // la vignette
contenuDe("EP301")?.carrousel;          // 4 planches, si présent
contenuDe("EP301")?.imageFacebook;      // le visuel
```

Prends `prompt` tel quel. N'invente rien, n'améliore rien.

## Série « Une journée » — la règle qui compte

**Ce n'est pas le chef FoodEatUp.** Ce sont dix métiers différents : chef de
cuisine, second, chef de partie, cuisinier, plongeur, patron, chef de rang,
serveur, responsable de la communication, client. Chacun doit être **une
personne distincte et reconnaissable**, la même d'un épisode à l'autre de son
métier — trois épisodes par métier, donc trois images du même visage.

La photo du chef jointe sert de **référence de style** — lumière, grain,
réalisme, cadrage — et non de référence de visage. Le chef FoodEatUp
n'apparaît dans aucune de ces 31 vignettes.

**Aucun écran allumé, aucune tablette, aucune interface visible.** La série
montre le geste, pas l'outil. Un écran dans le cadre bascule l'épisode du côté
de la démonstration, ce qui est exactement ce qu'elle évite.

Le champ `phase` donne l'heure et la lumière :

| Phase | Heure | Lumière |
|---|---|---|
| Avant le service | 07h00 | froide, avant l'aube, une seule source |
| Pendant le service | 20h15 | chaude, saturée, vapeur, mouvement |
| Après le service | 23h30 | crue, néons, surfaces vides |

## Série « L'IA dans FoodEatUp » — l'autre charte

Ici **c'est bien le chef FoodEatUp**, et la photo jointe est la référence de
visage : même visage, même barbe, même toque, même veste, même tablier.

Mais la charte est **RapidoCMS** : bleu `#03A9F5`, gris `#383838`, blanc, tons
clairs. **Pas de crème, pas d'orange** — ce sont les couleurs de l'autre série
et les mélanger brouille les deux.

Le bleu est **dans le décor** — un écran éteint qui reflète, une lumière, un
objet — et ne forme **jamais un logo**.

Et une interdiction propre à cette série : **aucun schéma, aucun diagramme,
aucune infographie**. Une série sur l'IA filme d'habitude des flèches et des
boîtes. Celle-ci filme ce que la phrase déclenche — le bac de saumon, le
téléphone, la chambre froide. L'abstraction est dans le commentaire, pas dans
l'image.

## Les quatre interdits, valables partout

Appris sur trois cents vignettes déjà produites, dont beaucoup à refaire.

1. **Le personnage ne se redessine pas.** Sur *L'IA*, c'est le chef de la photo
   de référence. Sur *Une journée*, c'est le même visage sur les trois épisodes
   d'un même métier. Un générateur laissé libre invente quelqu'un d'autre à
   chaque appel.
2. **Pas de noir et blanc, pas de désaturation.** Aucune des deux chartes n'est
   grise.
3. **Aucun logo dessiné par le générateur.** Il en invente un deuxième,
   approchant mais faux. Le seul logo autorisé sur *L'IA* est celui du tablier,
   qui vient de la photo.
4. **Une scène par épisode.** Le décor est dans chaque prompt : suis-le.

## Le texte est dans l'image

Les carrousels et les visuels Facebook **sont** la publication : on les regarde
dans un fil, sans son, la légende repliée. Chaque prompt donne le texte exact,
sa couleur et sa place. Écris ces mots-là, sans faute, sans lettre déformée.

Si ton générateur rend mal le français, génère l'image **sans texte** et
compose les bandes en HTML/canvas avant d'enregistrer le JPEG.

## Ce qu'il ne faut surtout pas faire

- **Ne touche pas aux 240 épisodes du Coup de Feu** ni à leurs images
  existantes dans `public/thumbnails/`, `public/carrousels/`, `public/facebook/`.
- **Ne régénère pas** `src/data/series.ts` ni `src/data/contenu.ts`. Ils sont
  produits par l'usine à vidéos et portent maintenant 302 épisodes.
- **Ne réécris pas** `ApercuReseau.tsx`, `PublicationBloc.tsx`,
  `CeQuilFautPublier.tsx` ni `BlocBoucle.tsx`. Ils gèrent déjà les trois séries.
- **Ne relance pas un tour par épisode.** Un tour traite les 372 images.

## Vérification avant de me rendre la main

- [ ] 62 vignettes `EP301`–`EP331` et `EP401`–`EP431` en 1080 × 1920
- [ ] 248 planches `EPxxx-1..4.jpg` et 62 visuels, en 1080 × 1350
- [ ] tout en JPEG
- [ ] sur *Une journée* : dix personnes distinctes, chacune identique sur ses
      trois épisodes, et **aucun écran allumé** dans le cadre
- [ ] sur *L'IA* : le chef de la photo, charte RapidoCMS, **aucun schéma**
- [ ] les images du *Coup de Feu* n'ont pas bougé
- [ ] aucune image en niveaux de gris, aucun deuxième logo
- [ ] `npm run build` passe
