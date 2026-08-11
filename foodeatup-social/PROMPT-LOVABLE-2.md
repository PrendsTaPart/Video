# Prompt Lovable nº 2 — les publications, le calendrier, le teasing

À passer **après** que le prompt nº 1 soit vérifié. Il charge les 150 épisodes et
leurs 600 publications, puis construit les trois écrans qui manquent.

---

Remplace intégralement `src/data/series.ts` par le contenu de ce fichier :

https://raw.githubusercontent.com/PrendsTaPart/Video/claude/foodeatup-video-factory-wtb7gs/foodeatup-social/src/data/series.ts

Il contient les 150 épisodes répartis sur 5 saisons, et pour chacun **les quatre
publications prêtes à partir** — une par réseau. Adapte les imports de tes
composants si tu utilisais d'autres noms.

Récupère aussi les 7 vignettes déjà extraites des masters et place-les dans
`public/posters/` :

```
EP001.jpg EP002.jpg EP003.jpg EP005.jpg EP006.jpg EP007.jpg EP010.jpg
```

depuis `https://raw.githubusercontent.com/PrendsTaPart/Video/claude/foodeatup-video-factory-wtb7gs/foodeatup-social/public/posters/EPxxx.jpg`

## Ce que le type `Publication` change

Chaque épisode porte maintenant, par réseau, **tout ce qu'il faut pour publier** :

```ts
type Publication = {
  statut: StatutReseau;   // "publie" | "planifie" | "brouillon" | "a_venir"
  date: string | null;    // "2026-08-11"
  heure: string;          // "12:00"
  compte: string;
  format: string;         // "Reel 9:16", "Vidéo native 9:16"…
  legende: string;        // le texte à coller, SANS les mots-dièse
  hashtags: string[];     // sans le "#", il est ajouté à l'affichage
  cta: string;            // "Voir le tutoriel complet"
  lienCta: string | null; // null sur Instagram et TikTok
  motsCles: string[];     // pour le référencement, pas pour la légende
  url?: string;           // le permalien, une fois en ligne
};
```

Le helper `texteAColler(publication)` recompose légende + ligne de mots-dièse.

L'objectif de tout ça : **le jour de la publication, il ne reste qu'à importer la
vidéo.** Le texte, les mots-dièse, le lien, l'heure et le compte sont déjà écrits.

Les quatre légendes d'un même épisode sont **volontairement différentes**, et il ne
faut surtout pas les uniformiser :

- Instagram et TikTok ne rendent pas les liens cliquables dans une légende — leur
  texte renvoie vers la bio, et leur `lienCta` est `null`.
- LinkedIn met le bénéfice métier avant l'anecdote.
- TikTok tient en deux lignes.
- Facebook accepte le lien dans le corps et un texte plus long.

## Écran 1 — le bloc « Prêt à publier » sur la page épisode

Remplace la section « Où on l'a publié » par un bloc plus riche : **un onglet par
réseau** (Facebook, Instagram, TikTok, LinkedIn), avec l'icône Simple Icons du
réseau dans l'onglet.

Dans l'onglet sélectionné :

1. Une ligne d'entête : icône, nom du compte, format (`Reel 9:16`), et une pastille
   d'état — verte « Publié le 11 août », bleue « Planifié pour le 11 août », ambre
   « Brouillon prêt », neutre « À venir le 3 septembre ».
2. **La légende**, dans un bloc de texte à fond blanc, chasse fixe, qui respecte les
   retours à la ligne (`whitespace-pre-line`). Un bouton « Copier la légende » en
   haut à droite du bloc, avec confirmation visuelle « Copié ! ».
3. **Les mots-dièse**, en puces bleu clair arrondies, précédés du `#`. Un bouton
   « Copier les mots-dièse ».
4. Un bouton principal orange **« Tout copier »** qui met dans le presse-papier le
   résultat de `texteAColler()` — légende + ligne de mots-dièse. C'est le bouton
   que la personne utilisera neuf fois sur dix : mets-le en évidence.
5. **Le CTA** : si `lienCta` existe, un bouton bleu portant le texte de `cta` et
   pointant sur `lienCta`. Sinon, une mention grise « {cta} — le lien n'est pas
   cliquable sur ce réseau, il est en bio ».
6. **Les mots-clés** en petit, en bas, sous un intitulé « Mots-clés visés » — ils ne
   vont pas dans la légende, ils servent au référencement et à la cohérence
   éditoriale. Ne les confonds pas avec les mots-dièse.

Si l'épisode n'est pas encore publié sur ce réseau, **le bloc entier est grisé** :
`opacity: 0.75`, texte en encre douce. Les boutons de copie restent actifs — c'est
justement à ce moment-là qu'on en a besoin.

## Écran 2 — le calendrier de contenu

La route `/calendrier` devient l'écran le plus utile du site. Deux vues, avec un
sélecteur en haut.

### Vue mois (par défaut)

Une grille de calendrier classique. Chaque jour qui porte un épisode affiche :

- la vignette en miniature (poster réel ou teasing, voir plus bas), en fond de case,
  très atténuée ;
- le numéro et le titre de l'épisode ;
- **quatre pastilles**, une par réseau, dans l'ordre horaire — LinkedIn 08:00,
  Facebook 12:00, Instagram 18:30, TikTok 19:00 — chacune à la couleur de son
  réseau, pleines si publié, en contour si à venir.

Cliquer sur un jour ouvre un panneau latéral avec les quatre publications de la
journée, dans l'ordre des heures, chacune avec sa légende et ses boutons de copie.

### Vue liste, groupée par réseau

Un onglet par réseau. Sous l'onglet, la liste chronologique de tout ce qui part sur
ce réseau : date, heure, vignette miniature, numéro et titre, état, et un bouton
« Tout copier ». C'est la vue qu'on ouvre quand on prépare une semaine d'un seul
réseau d'un coup.

### Le principe du calendrier — à respecter

Un objet `calendrier` est exporté avec le départ, la cadence et les créneaux.
Affiche la note qu'il contient sous le titre de la page : les horaires sont décalés
pour qu'un même épisode ne tombe pas quatre fois au même moment sur quatre fils.

**Les épisodes bloqués n'ont pas de date** (`datePrevue: null`) et ne prennent aucune
place dans la grille. Ils s'y insèrent quand leur tutoriel existe. Montre-les dans un
encart séparé sous le calendrier : « 32 épisodes en attente de leur tutoriel », avec
la liste et la raison. Ne leur invente pas une date.

## Écran 3 — la vignette de teasing

C'est la pièce qui fait tenir visuellement les 143 épisodes non sortis.

Quand `posterUrl` existe, on affiche l'image. Quand il vaut `null`, on **génère la
vignette en composant React** — pas d'image, pas de fichier à produire : ça doit
marcher pour les 150 épisodes à venir comme pour les prochaines séries.

Composant `<VignetteTeasing episode={...} />`, ratio 9:16, `border-radius: 1rem` :

- **Fond** : crème `#FCF9E6`, avec un halo radial très doux en haut à gauche dont la
  teinte est choisie **de façon déterministe d'après le nom du module** — une petite
  fonction de hachage sur la chaîne, puis un index dans une palette fixe de quatre
  teintes de marque : bleu à 8 %, orange à 8 %, marine à 6 %, crème profond. Deux
  épisodes du même module ont donc la même teinte, et la grille prend un rythme au
  lieu d'être une nappe uniforme.
- **En filigrane**, derrière : le numéro `EP013` en Fredoka, très gros (≈ 40 % de la
  hauteur de la carte), marine à 6 % d'opacité, centré, légèrement débordant en bas.
- **Au premier plan**, centré : **l'accroche de l'épisode**, en Fredoka bold marine,
  3 lignes maximum avec ellipse au-delà, centrée, avec de vraies marges (au moins
  12 % de chaque côté). C'est le texte qui donne envie — c'est celui qui est incrusté
  dans les trois premières secondes de la vidéo.
- **En bas** : le badge du module, et une puce d'état :
  - si `datePrevue` existe → icône horloge + « Prévu le 3 sept. » (format français
    court) ;
  - si l'épisode est `bloque` → icône cadenas + « Bientôt ».
- **Grain** : une très légère texture de bruit en superposition, faite en CSS pur
  (un `background-image` en SVG `feTurbulence` encodé en data-URI), opacité 3 %. Pas
  de fichier image.
- Bordure 1 px `#0F1A23` à 8 %, ombre douce.

Sur toutes les cartes dont l'épisode n'est pas sorti, applique en plus
`filter: grayscale(0.15)` et `opacity: 0.8` — grisé, mais toujours lisible. Un
teasing illisible ne tease rien.

Au survol d'une vignette de teasing : l'opacité remonte à 1 et la puce d'état passe
en bleu. Rien de plus, pas de zoom.

## Détail qui compte

Le bouton « Tout copier » doit copier **exactement** ce qui part en ligne, retours à
la ligne compris. Vérifie-le : si la légende arrive collée en un seul paragraphe dans
le presse-papier, le bloc ne sert à rien et il faudra tout retaper à la main.
