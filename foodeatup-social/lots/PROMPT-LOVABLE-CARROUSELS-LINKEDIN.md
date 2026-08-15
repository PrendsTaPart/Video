# Prompt Lovable — les 600 planches de carrousel LinkedIn

À envoyer **en un seul tour**. Joindre la photo du chef en pièce jointe :
`public/brand/chef-foodeatup.jpg`.

---

## Le contexte, en trois phrases

FoodEatUp Social est la vitrine d'une série de 150 vidéos promotionnelles.
Chaque épisode part sur cinq réseaux. LinkedIn ne reçoit pas la vidéo : il
reçoit un **carrousel de quatre planches**, publié en PDF.

Le site sait déjà convertir quatre JPEG en PDF — `src/lib/pdf.ts`, aucune
dépendance. Il ne manque que les images.

## Ce que je te demande

Génère **600 images** : quatre planches pour chacun des 150 épisodes.

Le prompt de chaque planche est **déjà écrit** et se trouve dans les données
du projet :

```ts
import { contenuDe } from "@/data/contenu";

const c = contenuDe("EP001");
c.carrousel.planches;   // 4 objets { n, role, titre, texte, prompt }
```

N'invente pas de prompt. N'améliore pas les prompts. Prends `planche.prompt`
et envoie-le tel quel à ton générateur d'images, **avec la photo du chef en
image de référence**.

## Où déposer les rendus

```
public/carrousels/EP001-1.jpg
public/carrousels/EP001-2.jpg
public/carrousels/EP001-3.jpg
public/carrousels/EP001-4.jpg
…
public/carrousels/EP150-4.jpg
```

Le nom du fichier est un contrat : `src/components/PieceReseau.tsx` va
chercher `/carrousels/{id}-{n}.jpg` et affiche un emplacement vide tant que le
fichier n'existe pas. Ne renomme rien, n'ajoute pas de suffixe de taille.

**JPEG obligatoire**, pas de PNG, pas de WebP. Le convertisseur PDF embarque
le flux JPEG tel quel (`/DCTDecode`) : un PNG produirait un PDF de pages
blanches. Format **1080 × 1350** exactement, qualité 85.

## Les quatre interdits

Ils viennent de trois cents vignettes déjà produites, dont une bonne partie a
dû être refaite. Ce ne sont pas des préférences.

1. **Le chef ne se redessine pas.** Même visage, même barbe, même toque, même
   veste, même tablier au logo FoodEatUp bleu, sur les 600 images. La photo de
   référence est jointe : elle est la source, pas une inspiration. Un
   générateur laissé libre invente un autre cuisinier à chaque appel et la
   série se dissout.

2. **Pas de noir et blanc, pas de désaturation.** Les rendus précédents
   sortaient en niveaux de gris « pour faire cinéma ». La charte est en
   couleur : crème `#FCF9E6`, marine `#0F1A23`, bleu `#007BFF`, orange
   `#FFA500`.

3. **Aucun logo dessiné par le générateur.** Il en invente un deuxième,
   approchant mais faux, et deux logos sur la même image se voient. Le seul
   logo autorisé est celui du tablier, qui vient de la photo de référence.

4. **Une scène par épisode.** Les 150 épisodes ne se passent pas dans la même
   cuisine. Le décor de chaque planche est décrit dans son prompt : suis-le.
   Quatre planches identiques à quatre autres, c'est un carrousel qu'on ne
   lit pas.

## Le texte est dans l'image

C'est la différence avec une vignette, et c'est le point qui compte le plus.

Personne ne clique sur une planche de carrousel pour voir autre chose : ce
qu'il y a à comprendre doit être écrit dedans, en entier, lisible sans son et
sans légende. Chaque prompt précise le texte exact, sa couleur, et où il se
pose — bande haute crème, bandeau bas marine. Écris **ces mots-là**, sans en
ajouter et sans en retrancher, sans faute, sans lettre déformée.

Si ton générateur rend mal le texte, génère l'image **sans texte** et compose
les bandes en HTML/canvas par-dessus avant d'enregistrer le JPEG. Un texte net
compte davantage qu'un texte « intégré ».

## L'ordre des planches raconte quelque chose

| Planche | Rôle | Ce qu'elle montre |
|---|---|---|
| 1 | La scène | le hook, le chef dans la situation comique |
| 2 | Le coût | ce que le problème coûte, resserré sur le détail qui coince |
| 3 | La réponse | le chef calme, tablette en main, la salle en ordre |
| 4 | La suite | le chef de face, l'invitation, sobre |

Ce n'est pas décoratif : c'est une démonstration. On sent le problème avant
d'entendre la réponse. Ne réordonne pas.

## Vérification avant de me rendre la main

- [ ] 600 fichiers dans `public/carrousels/`, nommés `EPxxx-n.jpg`
- [ ] tous en 1080 × 1350, tous en JPEG
- [ ] le même chef sur les 600
- [ ] aucune image en niveaux de gris
- [ ] aucun deuxième logo
- [ ] le texte de chaque planche est celui du prompt, sans faute

Ne relance pas un tour par épisode : un tour traite les 150.
