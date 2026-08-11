# Prompt Lovable — FoodEatUp Social

À coller tel quel dans Lovable pour créer le projet. Le fichier de données
(`data/series.json`, 150 épisodes) se dépose ensuite dans `src/data/series.ts`.

---

Crée **FoodEatUp Social** — le site public qui héberge toutes les vidéos sociales de
FoodEatUp (logiciel de gestion de restaurant), organisées par série, par saison et par
épisode, avec l'état de diffusion sur chaque réseau.

## La contrainte qui commande tout le reste

De nouvelles séries arriveront dans les prochains mois, chacune avec ses propres
saisons. Le modèle de données est donc **série → saison → épisode**, à trois niveaux,
dès maintenant — même s'il n'existe aujourd'hui qu'une seule série.

Concrètement, ça veut dire :

- aucune route ne code en dur un slug de série ni un numéro de saison ;
- aucun compteur n'est écrit à la main, tout se dérive du tableau `series` ;
- la page d'accueil doit fonctionner avec une série comme avec six ;
- les titres de saison viennent de la donnée, jamais d'un `switch` dans un composant.

Ajouter une deuxième série doit se résumer à ajouter **un objet dans un tableau**.

## Identité visuelle — charte officielle FoodEatUp, à respecter strictement

- Fond principal : crème `#FCF9E6`
- Texte / encre : marine foncé `#0F1A23`
- Accent primaire (liens, boutons, catégories) : bleu `#007BFF`
- Accent secondaire (CTA, badges, surlignages) : orange `#FFA500`
- Sur fond orange, le texte est **toujours** blanc
- Typographie : « Fredoka » (repli « Poppins ») en bold sur les titres, « Inter » en corps
- Cartes arrondies (`radius: 1rem`), ombres douces, pas de gris terne
- Thème clair uniquement, pas de mode sombre
- Logo officiel, à utiliser tel quel — ne jamais redessiner un logo maison :
  - Header : `https://raw.githubusercontent.com/PrendsTaPart/Video/claude/107-tutorial-videos-feasibility-p170aw/studio-video/assets/brand/logo/foodeatup-logo-mascot.png`
  - Favicon : `https://raw.githubusercontent.com/PrendsTaPart/Video/claude/107-tutorial-videos-feasibility-p170aw/studio-video/assets/brand/logo/foodeatup-mark-eight.png`

Pour les icônes de réseaux sociaux, utilise **Simple Icons** en SVG inline (Lucide ne
fournit pas les marques déposées), avec les couleurs officielles portées par la donnée :
Facebook `#1877F2`, Instagram `#E1306C`, TikTok `#000000`, LinkedIn `#0A66C2`. Sur fond
crème l'icône est pleine couleur ; dans une pastille de couleur elle est blanche.

## Modèle de données

Tout vit dans **un seul fichier** `src/data/series.ts`, typé et exporté — jamais en dur
dans les composants, puisque les épisodes arrivent au fil des semaines.

```ts
type Statut = "publie" | "monte" | "a_produire" | "bloque";
type StatutReseau = "publie" | "planifie" | "brouillon" | "a_venir";
type Reseau = "facebook" | "instagram" | "tiktok" | "linkedin";

type Diffusion = { statut: StatutReseau; date: string | null; compte: string; url?: string };

type Episode = {
  id: string;            // "EP001"
  numero: number;        // 1 → 150, continu sur toute la série
  saison: number;
  slug: string;          // "ep001-le-chien-qui-te-regarde"
  titre: string;
  module: string;
  chapitre: string;
  accroche: string;      // le texte incrusté à l'écran sur les 3 premières secondes
  punchline: string;     // la réplique off
  resume: string;        // ce que dit l'avatar : le contenu utile
  statut: Statut;
  blocage?: string;
  dureeSecondes: number | null;
  videoUrl: string | null;
  tutorielUrl: string | null;
  reseaux: Record<Reseau, Diffusion>;
};

type Saison = { numero: number; titre: string; pitch: string; episodes: Episode[] };

type Serie = {
  slug: string; nom: string; pitch: string; format: string;
  statut: "en-cours" | "terminee" | "a-venir";
  premiereDiffusion: string;
  saisons: Saison[];
};
```

`statut` d'un épisode et `statut` d'une diffusion sont **deux choses distinctes** : un
épisode peut être monté sans être publié nulle part, et publié sur Facebook tout en
restant à venir sur TikTok. La page épisode montre les deux.

Démarre avec la série ci-dessous, une saison, deux épisodes d'exemple — je remplacerai
le fichier par les 150 épisodes réels juste après.

```ts
export const series: Serie[] = [{
  slug: "le-coup-de-feu",
  nom: "Le Coup de Feu",
  pitch: "Trente secondes : une scène de restaurant qui part en vrille, puis la fonctionnalité FoodEatUp qui l'aurait évitée.",
  format: "Vertical 1080×1920 · 37,5 s · un épisode par jour",
  statut: "en-cours",
  premiereDiffusion: "2026-08-11",
  saisons: [{
    numero: 1,
    titre: "Le service, sans les cris",
    pitch: "Salle, cuisine, commandes : ce qui se joue pendant le coup de feu.",
    episodes: [
      {
        id: "EP001", numero: 1, saison: 1, slug: "ep001-le-chien-qui-te-regarde",
        titre: "Le chien qui te regarde", module: "Service",
        chapitre: "1 - Commandes multi-canaux",
        accroche: "Lui aussi attend ta commande.",
        punchline: "Sauf que lui, il est patient. Tes clients, non.",
        resume: "Ici, toutes tes commandes arrivent au même endroit : la salle, le téléphone, le site, la livraison. Une seule file, dans l'ordre d'arrivée. Plus personne n'attend parce qu'on a oublié un ticket.",
        statut: "publie", dureeSecondes: 37.5,
        videoUrl: "https://raw.githubusercontent.com/PrendsTaPart/Video/claude/foodeatup-video-factory-wtb7gs/foodeatup-video-factory/dist/tiktok/EP001.mp4",
        tutorielUrl: "https://drive.google.com/file/d/10GjJltEF3utZtfmwHR0qLZ8CTQr5_ioC/view",
        reseaux: {
          facebook:  { statut: "planifie", date: "2026-08-11", compte: "FoodEatUp" },
          instagram: { statut: "brouillon", date: null, compte: "foodeatup.cocuisinage" },
          tiktok:    { statut: "a_venir",   date: null, compte: "foodeatup" },
          linkedin:  { statut: "a_venir",   date: null, compte: "FoodEatUp" },
        },
      },
      {
        id: "EP004", numero: 4, saison: 1, slug: "ep004-le-tiroir-caisse-recalcitrant",
        titre: "Le tiroir-caisse récalcitrant", module: "Caisse POS",
        chapitre: "1 - Configurer sa caisse",
        accroche: "Ta caisse, le jour de l'ouverture.",
        punchline: "Elle va se calmer.",
        resume: "Tu branches ton TPE, tu choisis ton format de ticket, et la caisse est prête. Une seule configuration, valable sur tous tes postes.",
        statut: "bloque",
        blocage: "Le chapitre correspondant n'a pas encore de vidéo dans le Drive interne.",
        dureeSecondes: null, videoUrl: null, tutorielUrl: null,
        reseaux: {
          facebook:  { statut: "a_venir", date: null, compte: "FoodEatUp" },
          instagram: { statut: "a_venir", date: null, compte: "foodeatup.cocuisinage" },
          tiktok:    { statut: "a_venir", date: null, compte: "foodeatup" },
          linkedin:  { statut: "a_venir", date: null, compte: "FoodEatUp" },
        },
      },
    ],
  }],
}];

export const reseaux = [
  { slug: "facebook",  nom: "Facebook",  compte: "FoodEatUp",              url: "https://www.facebook.com/profile.php?id=201499969703551", couleur: "#1877F2" },
  { slug: "instagram", nom: "Instagram", compte: "foodeatup.cocuisinage",  url: "https://www.instagram.com/foodeatup.cocuisinage/",        couleur: "#E1306C" },
  { slug: "tiktok",    nom: "TikTok",    compte: "foodeatup",              url: "https://www.tiktok.com/@foodeatup",                       couleur: "#000000" },
  { slug: "linkedin",  nom: "LinkedIn",  compte: "FoodEatUp",              url: "https://www.linkedin.com/company/foodeatup/",             couleur: "#0A66C2" },
];
```

## Routes

| Route | Écran |
|---|---|
| `/` | Accueil — le hub |
| `/series` | Toutes les séries |
| `/series/:serieSlug` | Une série, avec sélecteur de saison |
| `/series/:serieSlug/saison/:numero` | Une saison |
| `/episode/:episodeSlug` | Un épisode — **le gabarit le plus important** |
| `/reseaux/:reseauSlug` | Tout ce qui passe sur un réseau |
| `/calendrier` | Ce qui part, quand, où |

L'épisode a une URL courte, sans la série ni la saison dans le chemin : un lien partagé
sur les réseaux doit rester lisible et survivre à une réorganisation des saisons. Le fil
d'Ariane, lui, reconstruit le chemin complet depuis la donnée.

## Les écrans

### Accueil

- Header sticky : logo à gauche, recherche live sur le titre et l'accroche des épisodes,
  CTA orange « Essayer FoodEatUp gratuitement » à droite.
- Hero sur fond crème : **« Le restaurant, en trente secondes. »** en Fredoka bold,
  sous-titre « Une scène qui part en vrille, puis la fonctionnalité qui l'aurait évitée.
  Un épisode par jour. », bouton bleu « Voir le dernier épisode ».
- **À l'affiche** : le dernier épisode publié, en grand, lecteur à gauche et texte à droite
  sur desktop, empilé sur mobile.
- **Cette semaine** : les épisodes dont une diffusion est planifiée dans les 7 jours, en
  ligne horizontale scrollable, avec la date et l'icône du réseau.
- **Nos séries** : une carte par série — nom, pitch, format, barre de progression
  « 7 épisodes sortis sur 150 », vignettes des 5 saisons.
- **Où nous suivre** : les quatre réseaux, icône Simple Icons dans une pastille à la
  couleur de la marque, nom du compte, nombre d'épisodes qui y sont passés.

### Série et saison

Bandeau de la série (nom, pitch, format, progression), puis un sélecteur de saison en
onglets. Chaque saison affiche son titre et son pitch, puis la grille des 30 épisodes.

Filtres au-dessus de la grille : par statut (tous / sortis / à venir) et par module.
Les filtres se dérivent des données présentes, ils ne sont pas codés en dur.

Carte d'épisode : numéro en petit (`EP001`), titre, accroche en italique, badge de module,
pastille d'état, et les icônes des réseaux où l'épisode est passé. Les épisodes non
produits sont grisés mais **restent visibles** — c'est ce qui montre qu'il y a une série
de 150 derrière, pas 7 vidéos isolées.

### Épisode — le gabarit à soigner

1. Fil d'Ariane : Accueil > Le Coup de Feu > Saison 1 > Épisode 1.
2. Lecteur `<video controls playsinline>` au ratio 9:16, contraint à `max-height: 80vh`
   pour qu'un format vertical ne pousse pas la page sur trois écrans. Pas de player custom.
   `preload="metadata"` ici, `preload="none"` partout ailleurs — sinon une page de saison
   déclenche trente téléchargements de plusieurs mégaoctets au chargement.
3. Titre en grand, numéro d'épisode, badge de module, durée.
4. **L'histoire** : l'accroche et la punchline, présentées comme des répliques, pas comme
   des champs de formulaire.
5. **Ce que ça change dans ton resto** : le champ `resume`, en texte courant.
6. **Où on l'a publié** : une ligne par réseau — icône, nom du compte, état lisible
   (« Publié le 11 août », « Planifié pour le 11 août », « Brouillon prêt », « À venir »),
   et le lien vers le post quand il existe.
7. **Le tutoriel complet** : encart bleu clair avec un lien « Voir le pas-à-pas dans
   l'Academy », affiché seulement si `tutorielUrl` existe.
8. Navigation « Épisode précédent · Épisode suivant », qui traverse les saisons : après
   le 30, on passe au 31.

Si `statut` vaut `a_produire` ou `bloque` : pas de lecteur, un bloc crème à la place avec
« Cet épisode arrive » et, s'il y a un `blocage`, la raison en une phrase. L'accroche et
le titre restent affichés — on annonce la couleur, on ne cache pas la page.

### Réseau

Le logo du réseau, le nom du compte, un lien vers le profil, et la liste chronologique de
tout ce qui y est passé ou planifié. État vide : « Rien n'est encore parti sur TikTok.
Ça ne va pas tarder. »

### Calendrier

Vue par semaine, une colonne par jour, les épisodes planifiés posés dessus avec l'icône du
réseau. Le passé en encre normale, le futur en encre douce.

## Ton et wording

Direct, tutoiement, phrases courtes, zéro jargon marketing. Pas de « solutions
innovantes », pas de « révolutionner votre établissement ». C'est le ton des vidéos.

- Compteur de saison : « {publies} épisodes sortis sur {total} »
- Saison vide : « Cette saison arrive. Les épisodes se dévoilent un par jour. »
- Épisode bloqué : « Cet épisode attend son tutoriel. On le tourne bientôt. »
- Pied de page : « Une démo ? 06 14 18 92 25 — foodeatup.com », plus les quatre icônes
  de réseaux et un lien WhatsApp vers `https://wa.me/33614189225`.

## Technique

Stack par défaut (React + Tailwind + shadcn/ui). Pas de backend : les données vivent dans
`src/data/series.ts`. Site responsive, mobile d'abord — l'essentiel du trafic viendra des
réseaux, donc d'un téléphone.

Balises Open Graph par épisode (titre, accroche, vignette) : ces pages seront partagées
depuis les réseaux, une carte de partage vide serait un gâchis.
