# FoodEatUp Social — architecture

Le site public qui héberge **toutes les vidéos sociales de FoodEatUp**, organisées par
série, par saison et par épisode, avec l'état de diffusion sur chaque réseau.

Ce n'est pas un clone de l'Academy. L'Academy (`tutoriel.foodeatup.com`) explique
**comment on fait**, chapitre par chapitre. FoodEatUp Social montre **ce qu'on
publie**, épisode par épisode. Les deux se citent l'un l'autre : chaque épisode
renvoie vers son tutoriel Academy, et l'Academy peut renvoyer vers l'épisode qui
met le module en scène.

## La contrainte qui commande tout le reste

De nouvelles séries arriveront dans les prochains mois, chacune avec ses propres
saisons. Le modèle de données est donc **série → saison → épisode**, à trois
niveaux, dès maintenant — même s'il n'existe aujourd'hui qu'une seule série.

Un site construit autour d'une liste plate de 150 vidéos serait à réécrire au
premier « on lance une deuxième série ». Un site construit autour de trois niveaux
absorbe une nouvelle série en ajoutant **un objet dans un tableau**, sans toucher à
une seule route ni à un seul composant.

Corollaires, tous vérifiables :

- Aucune route ne code en dur `le-coup-de-feu` ni un numéro de saison.
- Aucun compteur (« 7 épisodes publiés ») n'est écrit à la main : tout se dérive du
  tableau `series`.
- La page d'accueil fonctionne avec une série comme avec six.
- Les libellés de saison (« Saison 1 — Le service, sans les cris ») viennent de la
  donnée, jamais d'un `switch` dans un composant.

## Routes

| Route | Écran | Ce qu'on y voit |
|---|---|---|
| `/` | Accueil | Le hub : séries en cours, derniers épisodes publiés, ce qui sort cette semaine |
| `/series` | Toutes les séries | Une carte par série, avec son avancement et ses saisons |
| `/series/:serieSlug` | Une série | Pitch, format, sélecteur de saison, grille d'épisodes |
| `/series/:serieSlug/saison/:numero` | Une saison | Les 30 épisodes de la saison, filtrables |
| `/episode/:episodeSlug` | Un épisode | **Le gabarit le plus important** : lecteur, textes, réseaux, tutoriel lié |
| `/reseaux/:reseauSlug` | Un réseau | Tout ce qui est publié ou planifié sur Facebook, Instagram, TikTok, LinkedIn |
| `/calendrier` | Calendrier | Ce qui part, quand, sur quel réseau |

L'épisode a son URL propre, sans la série ni la saison dans le chemin : un lien
partagé sur les réseaux doit rester court et survivre à une réorganisation des
saisons. Le fil d'Ariane, lui, reconstruit le chemin complet depuis la donnée.

## Modèle de données

Un seul fichier, `src/data/series.ts`, typé, exporté depuis `data/series.json`.

```ts
type Statut = "publie" | "monte" | "a_produire" | "bloque";
type StatutReseau = "publie" | "planifie" | "brouillon" | "a_venir";

type Diffusion = {
  statut: StatutReseau;
  date: string | null;     // ISO court, "2026-08-11"
  compte: string;
  url?: string;            // le permalien, une fois le post en ligne
};

type Episode = {
  id: string;              // "EP001", l'identifiant de production
  numero: number;          // 1 → 150, continu sur toute la série
  saison: number;
  slug: string;            // "ep001-le-chien-qui-te-regarde"
  titre: string;
  module: string;          // le module FoodEatUp mis en scène
  chapitre: string;        // le chapitre Academy correspondant
  accroche: string;        // le texte incrusté sur le hook
  punchline: string;       // la réplique off à 5,0 s
  resume: string;          // ce que dit l'avatar : le vrai contenu utile
  statut: Statut;
  blocage?: string;        // pourquoi il n'est pas produit, si bloqué
  dureeSecondes: number | null;
  videoUrl: string | null;
  tutorielUrl: string | null;   // le chapitre Academy
  reseaux: Record<"facebook" | "instagram" | "tiktok" | "linkedin", Diffusion>;
};

type Saison = { numero: number; titre: string; pitch: string; episodes: Episode[] };

type Serie = {
  slug: string;
  nom: string;
  pitch: string;
  format: string;
  statut: "en-cours" | "terminee" | "a-venir";
  premiereDiffusion: string;
  saisons: Saison[];
};
```

`statut` d'un épisode et `statut` d'une diffusion sont deux choses distinctes, et
les confondre serait une erreur : un épisode peut être **monté** sans être publié
nulle part, et **publié** sur Facebook tout en restant **à venir** sur TikTok.
L'écran d'épisode montre les deux.

## Les quatre états, et ce qu'ils affichent

| État | Pastille | Ce que voit le visiteur |
|---|---|---|
| `publie` | verte | La vidéo se lit, les réseaux où elle est passée sont listés |
| `monte` | bleue | La vidéo se lit, mention « pas encore diffusée » |
| `a_produire` | ambre | Carte grisée, titre et accroche visibles, pas de lecteur |
| `bloque` | neutre | Idem, plus la raison — jamais un « erreur », c'est un état normal de production |

Un site qui masquerait les 143 épisodes non produits afficherait une série de
7 vidéos. En les montrant grisés, il affiche une série de 150 dont 7 sont sorties :
c'est la promesse d'une série, et c'est ce qui donne envie de revenir.

## Wording

Le ton est celui des vidéos : direct, tutoiement, phrases courtes, zéro jargon
marketing. Pas de « solutions innovantes », pas de « révolutionner ».

| Emplacement | Texte |
|---|---|
| Titre du site | FoodEatUp Social |
| Baseline | Toutes nos vidéos sociales, saison après saison. |
| Hero — titre | Le restaurant, en trente secondes. |
| Hero — sous-titre | Une scène qui part en vrille, puis la fonctionnalité qui l'aurait évitée. Un épisode par jour. |
| CTA principal | Voir le dernier épisode |
| CTA secondaire | Essayer FoodEatUp gratuitement |
| Section accueil 1 | À l'affiche |
| Section accueil 2 | Cette semaine |
| Section accueil 3 | Nos séries |
| Section accueil 4 | Où nous suivre |
| Grille saison | Saison {n} — {titre} |
| Compteur saison | {publies} épisodes sortis sur {total} |
| Épisode — section 1 | L'histoire |
| Épisode — section 2 | Ce que ça change dans ton resto |
| Épisode — section 3 | Où on l'a publié |
| Épisode — section 4 | Le tutoriel complet |
| Lien Academy | Voir le pas-à-pas dans l'Academy |
| Nav épisode | Épisode précédent · Épisode suivant |
| Vide (saison) | Cette saison arrive. Les épisodes se dévoilent un par jour. |
| Vide (réseau) | Rien n'est encore parti sur {réseau}. Ça ne va pas tarder. |
| Bloqué | Cet épisode attend son tutoriel. On le tourne bientôt. |
| Pied de page | Une démo ? 06 14 18 92 25 — foodeatup.com |

## Charte

Reprise telle quelle de l'Academy, sans réinterprétation.

| Rôle | Valeur |
|---|---|
| Fond | crème `#FCF9E6` |
| Encre | marine `#0F1A23` |
| Accent primaire | bleu `#007BFF` |
| Accent secondaire | orange `#FFA500` |
| Titres | Fredoka, repli Poppins |
| Corps | Inter |
| Rayon | `1rem`, cartes arrondies, ombres douces |
| Thème | clair uniquement |

Logos officiels, à utiliser tels quels — ne jamais redessiner :

- Horizontal avec mascotte (header) :
  `https://raw.githubusercontent.com/PrendsTaPart/Video/claude/107-tutorial-videos-feasibility-p170aw/studio-video/assets/brand/logo/foodeatup-logo-mascot.png`
- Symbole seul (favicon) :
  `https://raw.githubusercontent.com/PrendsTaPart/Video/claude/107-tutorial-videos-feasibility-p170aw/studio-video/assets/brand/logo/foodeatup-mark-eight.png`

Icônes de réseaux : `lucide-react` ne fournit pas de marques déposées. On utilise
**Simple Icons** (`simple-icons` en SVG inline), couleurs officielles portées par la
donnée (`reseaux[].couleur`) — Facebook `#1877F2`, Instagram `#E1306C`,
TikTok `#000000`, LinkedIn `#0A66C2`. Sur fond crème, l'icône est pleine couleur ;
sur une pastille de couleur, elle est blanche.

## Le lecteur

Lecteur HTML5 natif, `<video controls playsinline>`, ratio 9:16 contraint à
`max-height: 80vh` pour qu'un format vertical ne pousse pas la page sur trois écrans.
Pas de player custom : les masters sont des MP4 H.264/AAC, tous les navigateurs
les lisent.

`preload="none"` sur les grilles, `preload="metadata"` sur la page épisode. Sans ça,
une page de saison déclenche trente téléchargements de 8 Mo au chargement.

## Ce que le site ne fait pas

- Pas de compte, pas de connexion, pas de commentaire.
- Pas de back-office : les épisodes arrivent par mise à jour du fichier de données,
  qui est régénéré par l'usine à vidéos.
- Pas de mode sombre.
