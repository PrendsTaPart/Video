# Vidéo de démo — review TikTok for Developers

Livrable : `renders/braindcast-tiktok-demo.mp4`
— 1 min 52 (112,4 s) · 1080 × 2316 · H.264 · 30 fps · **sans piste audio** · 7,9 Mo · `+faststart`.

Rush d'origine : `source/Screen_Recording_20260907_144503_Chrome.mp4` (125,8 s, 1080 × 2316).
Reconstruction : `./build.sh` (un seul passage ffmpeg, pas de ré-encodage intermédiaire).

---

## Bornes de coupe

Relevées image par image sur le rush, pas d'après des repères approximatifs — les
estimations du brief étaient décalées de plusieurs secondes et l'un des passages
parasites n'y figurait pas.

| Segment | Rush | Durée | Contenu |
|---|---|---|---|
| A | 0,0 → 79,1 s | 79,1 s | Connexion, choix du média, formulaire, publication, historique |
| B | 88,0 → 100,6 s | 12,6 s | Liste Publications et ses statuts |
| C | 103,0 → 111,5 s | 8,5 s | Profil TikTok, puis la vidéo publiée ouverte |

Trois passages retirés, pas deux :

1. **79,1 → 88,0 s** — sélection de texte accidentelle, menu « Copier / Partager /
   Tout sélectionner » et pop-up Google « Publié · Appuyer pour afficher les
   résultats de recherche ». Le brief l'estimait à 77–85 s ; le menu tient en fait
   jusqu'à 87,6 s inclus.
2. **100,6 → 103,0 s** — sélecteur d'onglets Chrome, laissant voir des onglets sans
   rapport (IONOS, Lovable). **Ce passage n'était pas repéré dans le brief.**
3. **111,5 s → fin** — page de connexion TikTok, sélecteur d'onglets, puis
   `lovable.dev`. Le brief le situait à 111,5 s : correct, mais il restait ensuite
   19 s de liste Publications déjà montrée en B, écartées elles aussi.

## Structure du montage

| Temps final | Élément |
|---|---|
| 0,0 → 4,0 | Carton d'ouverture (fond `#0E0E10`) |
| 4,0 → 83,1 | Segment A |
| 83,1 → 95,7 | Segment B |
| 95,7 → 104,2 | Segment C |
| 104,2 → 107,2 | Gel de la dernière image (la vidéo publiée), 3 s |
| 107,2 → 112,2 | Carton de clôture |

Pas de fondu, pas de musique, pas d'effet. Aucun logo ni élément graphique TikTok
dans les cartons.

## Sous-titres

`subs.ass`, incrustés au rendu (filtre `subtitles`). DejaVu Sans 46 px, blanc,
contour noir, bandeau noir opaque (`BorderStyle=4`, `Outline=14`), aligné en bas
centré, `MarginV=170` — au-dessus de la barre de navigation Android. Deux lignes
maximum, ≤ 42 caractères par ligne pour ne jamais déborder du cadre.

Chaque sous-titre a été calé sur l'image réellement affichée au même instant du
montage final, puis vérifié sur 25 images extraites du rendu.

Un seul décalage vertical ponctuel : le sous-titre 24,0 → 27,3 s porte
`MarginV=580`, sinon il masquait la ligne « Poids · 22,4 Mo » qu'il cite.

---

## Deux points à corriger dans l'application avant de soumettre

Ils ne relèvent pas du montage et **subsistent dans ce rendu**.

1. **`@Compte retiré`.** Chaque ligne de l'historique affiche `@Compte retiré` au
   lieu de `@rapidocmstest`. Le même défaut touche l'écran **Comptes** : la ligne du
   compte connecté n'affiche ni pseudo ni avatar, seulement le badge « Connecté ».
   C'est visible à 14–20 s et sur tout le segment B.

   L'écran de composition, lui, affiche correctement `rapidocmstest` /
   `@rapidocmstest` / « Ce post sera publié sur ce compte » (30 s). Le sous-titre
   s'appuie sur cet écran-là et ne revendique nulle part que le compte connecté est
   nommé ailleurs.

2. **La légende « Test ».** Les Content Sharing Guidelines demandent un créateur
   authentique publiant du contenu original. Une vraie légende
   (`Forgeage d'une bague en laiton — atelier, Aubervilliers #artisanat #fabrication`)
   change la lecture du dossier.

Après ces deux corrections, il faut refaire la prise et relancer `./build.sh` — les
bornes de coupe seront à relever à nouveau sur le nouveau rush.

## Ce que le rush ne démontre pas

Le brief prévoyait un sous-titre « Private visibility becomes unavailable » sur le
menu de confidentialité en mode contenu de marque. **Le rush ne le montre pas** : à
52 s « Moi uniquement » est sélectionnable et le créateur la sélectionne
effectivement, la divulgation commerciale étant alors activée sans case cochée. Le
sous-titre a été réécrit sur ce que l'image prouve. À filmer si l'on veut appuyer ce
point de conformité.

Les entrées rouges `failed` sont conservées : elles prouvent la gestion des codes
d'erreur de l'API, et un sous-titre l'explique (« Red is not a bug — it is the API
reason »).
