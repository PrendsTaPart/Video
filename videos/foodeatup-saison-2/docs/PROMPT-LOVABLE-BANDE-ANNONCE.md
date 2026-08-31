# Prompt Lovable — la bande-annonce d'une saison

Projet **FoodEatUp Social Hub** (`food-series-hub`), workspace **Braind's Lovable**
(`78f6380983eca2a8298e`), projet `05bb6b0d-8c57-4347-b29b-d850b916ddde`.

## Pourquoi ce prompt existe

Le catalogue sait aujourd'hui : série → saison → épisode. Une saison porte une
**affiche** (une image), et c'est tout. Il n'existe **aucun champ ni aucun outil
MCP** pour lui rattacher une bande-annonce — vérifié le 31 août 2026 :

- `lister_series` rend `{ numero, titre, episodes, premierEpisode, dernierEpisode, affiche }` ;
- les outils vidéo (`deposer_episode`, `publier_video`, `definir_url_video`,
  `lister_urls_video`, `verifier_pieces`) travaillent tous **par épisode** ;
- `publier_clip_musical` existe pour les clips, qui sont une autre entité, avec
  leur propre `slug` — une bande-annonce n'est pas un clip.

La bande-annonce de la saison 2 de « Michael fait son cinéma » est montée,
déposée en bibliothèque et publiée sur le site, mais elle n'a nulle part où
vivre dans le catalogue.

---

## Le prompt à envoyer

> Ajoute au catalogue la notion de **bande-annonce de saison** : dans la donnée,
> dans les pages, et dans le serveur MCP. Une saison en a une, au plus. Ce n'est
> pas un épisode et ce n'est pas un clip musical : c'est la vidéo qui annonce la
> saison entière.
>
> ### 1. Le modèle de données
>
> Dans `src/data/series.ts`, ajoute à `Saison` un champ **optionnel** :
>
> ```ts
> type BandeAnnonce = {
>   url: string;              // la vidéo, servie par la bibliothèque RapidoCMS
>   vignette: string | null;  // l'image d'attente
>   dureeSecondes: number | null;
>   statut: Statut;           // le même vocabulaire que pour un épisode
>   reseaux: Record<Reseau, Diffusion>;  // le même que pour un épisode
> };
>
> type Saison = {
>   numero: number;
>   titre: string;
>   pitch: string;
>   bandeAnnonce?: BandeAnnonce;   // ← nouveau, facultatif
>   episodes: Episode[];
> };
> ```
>
> **Optionnel, et c'est important** : la plupart des saisons n'en auront jamais.
> Toute page doit se rendre correctement quand le champ est absent — pas de
> cadre vide, pas de « bande-annonce à venir », rien du tout.
>
> Réutilise `Statut`, `Reseau` et `Diffusion` tels quels. Ne crée pas de types
> parallèles : le jour où l'on ajoute un réseau, il doit s'ajouter à un seul
> endroit.
>
> Renseigne dès maintenant la bande-annonce de la saison de
> `michael-fait-son-cinema` :
>
> ```ts
> bandeAnnonce: {
>   url: "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/michael-fait-son-cinema-saison-2-bande-annonce",
>   vignette: "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/michael-fait-son-cinema-saison-2-bande-annonce-vignette",
>   dureeSecondes: 28,
>   statut: "monte",
>   reseaux: { facebook: …, instagram: …, tiktok: …, linkedin: … }  // tous « a_venir », date null
> }
> ```
>
> ### 2. Les pages
>
> **Page série** (`/series/:slug`) — au-dessus de la liste des saisons, si la
> saison la plus récente a une bande-annonce : un lecteur vidéo 9:16, largeur
> maximale 420 px, centré, `controls playsinline preload="metadata"`, avec la
> vignette en `poster`. Une légende sous le lecteur : « Bande-annonce · saison N
> · 28 s ». Aucune lecture automatique, aucun son au chargement.
>
> **Page saison** — le même lecteur, en tête, avant la grille d'épisodes.
>
> **Page d'accueil** — sur la carte d'une série dont une saison a une
> bande-annonce, une petite pastille « Bande-annonce » en accent orange
> `#FFA500`, texte blanc. Elle mène à la page série, elle ne lance rien.
>
> Le lecteur est un composant réutilisable, `<LecteurBandeAnnonce />`, pas trois
> copies. Il respecte `prefers-reduced-motion` et reste utilisable au clavier.
>
> ### 3. Les outils MCP
>
> Trois ajouts au serveur MCP, dans le vocabulaire des outils existants — en
> français, avec des descriptions qui disent quoi faire et pas seulement quoi
> lire.
>
> **`deposer_bande_annonce`** — écrit l'URL de la bande-annonce d'une saison.
> Paramètres : `serie` (slug), `saison` (numéro), `url`, `vignette` (facultatif),
> `duree_secondes` (facultatif), `note` (facultatif, journalisée).
> Il **contrôle l'URL avant d'écrire**, exactement comme `deposer_episode` : un
> 200 ou 206 avec un content-type vidéo, sinon rien n'est écrit et l'échec est
> rendu tel quel. Il passe le statut à `pret`. **Il ne valide jamais** : `valide`
> reste un geste humain dans `/admin/production`, aucun outil ne l'expose.
>
> **`obtenir_bande_annonce`** — rend la bande-annonce d'une saison : URL,
> vignette, durée, statut, état de diffusion par réseau, et `manquant` quand il
> n'y en a pas. Un objet qui dit « il n'y en a pas » vaut mieux qu'une erreur.
>
> **`lister_series`** gagne, pour chaque saison, un champ `bandeAnnonce` :
> `null` quand il n'y en a pas, sinon `{ url, vignette, duree_secondes, statut }`.
> Ne change rien d'autre à sa sortie — d'autres outils la lisent.
>
> Étends aussi **`verifier_pieces`** pour qu'il teste les bandes-annonces comme
> il teste les pièces d'épisode : interrogation HTTP réelle, `heberge`
> (`bibliotheque` / `depot` / `externe` / `absent`) et `repond`. C'est le
> contrôle qui compte — un fichier servi depuis `raw.githubusercontent.com` a
> déjà été refusé en 403 par YouTube.
>
> ### 4. Ce qu'il ne faut pas faire
>
> - Ne touche pas au modèle `Episode`, ni aux outils par épisode.
> - Ne crée pas d'entité « bande-annonce » séparée avec son propre slug : c'est
>   un attribut de saison, pas un objet du catalogue.
> - N'expose aucun outil qui écrirait `valide`.
> - Ne code en dur aucun slug de série ni numéro de saison, nulle part — la
>   contrainte fondatrice du projet tient : ajouter une série reste ajouter un
>   objet dans un tableau.
>
> ### 5. Critères de recette
>
> 1. Une saison sans `bandeAnnonce` se rend exactement comme avant, sans espace
>    réservé ni libellé.
> 2. La page de `michael-fait-son-cinema` lit la vidéo et affiche sa vignette
>    avant lecture.
> 3. `deposer_bande_annonce` avec une URL qui répond 404 n'écrit rien et le dit.
> 4. `obtenir_bande_annonce` sur une saison qui n'en a pas rend `manquant`, pas
>    une erreur.
> 5. `lister_series` reste lisible par ses appelants actuels.

---

## Une question à trancher avant, ou en même temps

`lister_series` annonce **une seule saison** pour `michael-fait-son-cinema`
(numéro 1, EPC01 → EPC30). Mais `lister_episodes` répond aux **deux** filtres :

| Appel | Résultat |
|---|---|
| `saison: 1` | 30 épisodes, EPC01 → EPC30, dates du 1er septembre 2026 |
| `saison: 2` | 30 épisodes, EPC01 → EPC30, dates du 13 août 2027 |

Mêmes identifiants, mêmes titres, deux numéros de saison et deux calendriers.
Une bande-annonce s'adresse par `serie` + `saison` : tant que ce couple ne
désigne pas une chose unique, `deposer_bande_annonce` peut écrire au mauvais
endroit sans que rien ne le signale. **À vérifier côté données avant de se fier
au dépôt.**
