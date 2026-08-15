# Prompt Lovable — les 750 images, et les textes qui vont avec

À envoyer **en un seul tour**. Joindre en pièce jointe la photo du chef :
`public/brand/chef-foodeatup.jpg`.

---

## Ce que je te demande, en une phrase

Générer les 750 images qui manquent à partir des prompts déjà présents dans le
projet, les déposer aux emplacements que le code attend, et les brancher dans
le système d'aperçu qui existe déjà — sans le réécrire.

Trois choses, dans cet ordre. La troisième est la plus importante et c'est
celle qu'on rate d'habitude.

---

## 1. Les images

### Ce qu'il y a à générer

| Quoi | Combien | Où le déposer |
|---|---|---|
| Planches de carrousel LinkedIn | 600 — 4 par épisode | `public/carrousels/EP001-1.jpg` … `EP150-4.jpg` |
| Visuels Facebook | 150 — 1 par épisode | `public/facebook/EP001.jpg` … `EP150.jpg` |

Le nom de fichier est un contrat : `src/components/PieceReseau.tsx` va
chercher exactement ces chemins et affiche un emplacement vide tant que le
fichier n'existe pas. Ne renomme rien, n'ajoute pas de suffixe de taille, ne
crée pas de sous-dossier.

**JPEG obligatoire**, 1080 × 1350, qualité 85. Pas de PNG, pas de WebP : le
convertisseur PDF du site embarque le flux JPEG tel quel (`/DCTDecode`), et un
PNG produirait un carrousel de pages blanches.

### Les prompts sont déjà écrits

N'en invente aucun, n'en « améliore » aucun. Ils sont dans les données :

```ts
import { contenuDe } from "@/data/contenu";

const c = contenuDe("EP001");

c.carrousel.planches;        // 4 objets { n, role, titre, texte, prompt }
c.imageFacebook.prompt;      // 1 chaîne
```

Prends `prompt` tel quel et envoie-le à ton générateur d'images **avec la photo
du chef en image de référence**, à chaque appel, sans exception.

### Les quatre interdits

Ils viennent de trois cents vignettes déjà produites, dont une bonne partie a
dû être refaite. Ce ne sont pas des préférences de style.

1. **Le chef ne se redessine pas.** Même visage, même barbe, même toque, même
   veste, même tablier au logo FoodEatUp bleu, sur les 750 images. La photo
   jointe est la source, pas une inspiration. Un générateur laissé libre
   invente un autre cuisinier à chaque appel, et la série se dissout : c'est
   la même personne sur cent cinquante épisodes, c'est ce qui en fait une
   série.

2. **Pas de noir et blanc, pas de désaturation.** Les rendus précédents
   sortaient en niveaux de gris « pour faire cinéma ». La charte est en
   couleur : crème `#FCF9E6`, marine `#0F1A23`, bleu `#007BFF`, orange
   `#FFA500`.

3. **Aucun logo dessiné par le générateur.** Il en invente un deuxième,
   approchant mais faux, et deux logos sur la même image se voient au premier
   coup d'œil. Le seul logo autorisé est celui du tablier, qui vient de la
   photo de référence.

4. **Une scène par épisode.** Les 150 épisodes ne se passent pas dans la même
   cuisine. Le décor est décrit dans chaque prompt : suis-le.

### Le texte est DANS l'image

C'est la différence avec une vignette, et c'est ce qui compte le plus ici.

Une vignette est une miniature : on la voit avant de cliquer, la vidéo dira le
reste. Ces images-ci **sont** la publication. Personne ne clique dessus pour
voir autre chose. On les regarde dans un fil, sans son, la légende repliée.

Chaque prompt donne le texte exact, sa couleur et sa place — bande haute crème,
bandeau bas marine. Écris **ces mots-là**, sans en ajouter, sans en retrancher,
sans faute, sans lettre déformée.

Si ton générateur rend mal le français — accents avalés, lettres fondues —
génère l'image **sans texte** et compose les deux bandes en HTML/canvas avant
d'enregistrer le JPEG. Un texte net vaut mieux qu'un texte « intégré »
illisible.

### L'ordre des quatre planches est une démonstration

| Planche | Rôle | Ce qu'elle montre |
|---|---|---|
| 1 | La scène | le hook, le chef dans la situation comique |
| 2 | Le coût | ce que le problème coûte, resserré sur le détail qui coince |
| 3 | La réponse | le chef calme, tablette en main, la salle en ordre |
| 4 | La suite | le chef de face, l'invitation, sobre |

On doit sentir le problème avant d'entendre la réponse. Inverser 2 et 3 donne
une publicité. Ne réordonne pas.

---

## 2. Les textes à publier

Ils sont **déjà écrits** eux aussi — cinq par épisode, un par réseau :

```ts
import { contenuDe, texteAColler } from "@/data/contenu";

const c = contenuDe("EP001");
c.publications.facebook;   // { legende, hashtags, motsCles, cta, titre? }
c.publications.instagram;
c.publications.tiktok;
c.publications.linkedin;
c.publications.youtube;

texteAColler(c.publications.facebook);  // légende + ligne de mots-dièse
```

Ne les réécris pas, ne les résume pas, ne les traduis pas. Ils sortent d'un
générateur qui tient la voix de la série sur les cent cinquante épisodes.

**Un seul bouton de copie par post, discret**, qui prend le texte entier —
`texteAColler()`, légende et mots-dièse compris. Pas un bouton par champ, pas
un bouton par bloc. Le composant existe :

```ts
import { BoutonCopier } from "@/components/PublicationBloc";

<BoutonCopier texte={texteAColler(t)} libelle="Copier" variante="fantome" />
```

---

## 3. Le branchement — la partie qu'on rate

**Le système d'aperçu existe déjà. Ne le réécris pas, ne le remplace pas, ne le
duplique pas.**

```
src/components/ApercuReseau.tsx     819 lignes — les 5 maquettes de réseau
src/components/PublicationBloc.tsx  les onglets + le bouton de copie
src/components/CeQuilFautPublier.tsx la section « Ce qu'il faut publier »
```

`ApercuReseau` rend un post dans l'habillage de son réseau : la barre
Facebook, le carré Instagram, le fil LinkedIn. C'est ce qui permet de voir ce
que verra le client. Ce qui lui manque, c'est **la bonne image** : il montre
encore la vignette de la vidéo là où le post partira en image ou en carrousel.

Ce que tu changes, précisément :

- **`ApercuFacebook`** — afficher `/facebook/{episode.id}.jpg` à la place de la
  vignette. Si le fichier manque, garder le comportement actuel.
- **`ApercuLinkedIn`** — afficher les quatre planches
  `/carrousels/{episode.id}-{1..4}.jpg` dans un carrousel qu'on fait défiler,
  avec le compteur « 1 / 4 » que LinkedIn affiche. Sous l'aperçu, le bouton
  « Télécharger le PDF » : la fonction existe, `carrouselEnPdf()` dans
  `src/lib/pdf.ts`.
- **`ApercuInstagram`** — afficher la story `contenuDe(id).story.url` quand
  elle existe, en 9:16, muette et en lecture automatique comme le fait
  Instagram.
- **TikTok et YouTube** — ne touche à rien. Ils reçoivent le master, et le
  master n'a pas changé.

### Trois règles de cette maquette, déjà en vigueur

Elles sont dans le `CLAUDE.md` du projet. Les enfreindre, c'est refaire un
travail déjà fait.

1. **Aucun compteur de réactions inventé.** Pas de « 47 j'aime ». Les
   compteurs restent vides tant que le post n'est pas parti — un chiffre
   inventé dans une maquette finit toujours par être lu comme un vrai.
2. **Un seul bouton de copie, discret**, qui prend le texte entier.
3. **Tous les posts s'affichent, publiés ou non.** Le statut réseau est une
   information, pas un verrou : ne grise rien, ne masque rien. Ce qui reste
   grisé, ce sont les vignettes d'épisodes **non produits** — là, il n'y a
   réellement rien à montrer.

---

## Ce qu'il ne faut surtout pas faire

- Ne touche pas à `public/thumbnails/` : ce sont les vignettes, un autre
  format, déjà en place.
- Ne régénère pas `src/data/series.ts` ni `src/data/contenu.ts`. Ils sont
  produits par l'usine à vidéos et portent 240 épisodes ; une régénération
  côté site effacerait les saisons 7 et 8.
- Ne crée pas un second composant d'aperçu « plus simple ». Il y en a déjà eu
  un, il a fallu le supprimer.
- Ne relance pas un tour par épisode. Un tour traite les 150 : quinze tours au
  lieu de deux, c'est le budget de la saison.

---

## Vérification avant de me rendre la main

- [ ] 600 fichiers dans `public/carrousels/`, nommés `EPxxx-n.jpg`
- [ ] 150 fichiers dans `public/facebook/`, nommés `EPxxx.jpg`
- [ ] tous en JPEG, 1080 × 1350
- [ ] le même chef sur les 750 — ouvre-en dix au hasard et compare
- [ ] aucune image en niveaux de gris, aucun deuxième logo
- [ ] le texte de chaque image est celui du prompt, sans faute
- [ ] `public/thumbnails/` n'a pas bougé
- [ ] l'aperçu Facebook montre le visuel, l'aperçu LinkedIn le carrousel,
      l'aperçu Instagram la story
- [ ] aucun compteur de réactions inventé nulle part
- [ ] un seul bouton de copie par post, et il copie le texte entier
- [ ] `npm run build` passe
