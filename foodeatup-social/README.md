# FoodEatUp Social

Le site public qui héberge toutes les vidéos sociales de FoodEatUp, organisées
par série, par saison et par épisode, avec l'état de diffusion sur chaque réseau.

Projet Lovable : https://lovable.dev/projects/05bb6b0d-8c57-4347-b29b-d850b916ddde

| Fichier | Ce que c'est |
|---|---|
| `PROMPT-LOVABLE.md` | Le prompt de création, à recoller si le projet est reparti de zéro |
| `ARCHITECTURE.md` | Routes, modèle de données, wording, charte — la référence |
| `data/series.json` | Les 150 épisodes, format neutre |
| `src/data/series.ts` | Le même contenu, typé, avec les sélecteurs — **à déposer dans le projet Lovable** |

## Régénérer les données

`src/data/series.ts` est **généré**, jamais édité à la main. La source est
`foodeatup-video-factory/content/episodes.json` plus l'état de production
(`state/episodes/*.json`) et la carte Drive (`content/drive-map.json`).

Quand un épisode est monté ou publié, son statut change dans l'usine : il faut
régénérer ce fichier et le repousser dans le projet Lovable.

## Pourquoi trois niveaux dès maintenant

De nouvelles séries arrivent dans les prochains mois, chacune avec ses saisons.
Un site construit autour d'une liste plate de 150 vidéos serait à réécrire au
premier « on lance une deuxième série ». Avec `série > saison > épisode`, une
nouvelle série est un objet de plus dans un tableau — aucune route, aucun
composant à toucher.
