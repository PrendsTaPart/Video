# Demande Lovable — ajouter les shorts aux épisodes du Journal

Projet : Michael Au Quotidien (https://lovable.dev/projects/255f6f6f-ae7c-4ba7-8c89-c6e431c71eef)

## Prompt à coller dans Lovable

Ajoute la gestion des « shorts » (version courte verticale, 20 à 45 s) aux vidéos de la série :
1. Dans la table des vidéos, ajoute une colonne `short_url` (texte, URL https, facultative).
2. Sur la page de chaque épisode (/videos/<slug>), si `short_url` existe, affiche un onglet ou un bouton « Version courte » qui lit le short (lecteur vertical 9:16, même style que la vidéo principale).
3. Ajoute une page publique /shorts : grille verticale de tous les shorts publiés (vignette = miniature de l'épisode, titre, lien vers l'épisode), du plus récent au plus ancien.
4. Dans l'admin des vidéos, ajoute le champ « Short (URL) ».
5. Dans le serveur MCP du Journal : ajoute `short_url` aux outils creer_video, modifier_video, obtenir_video et lister_videos.
6. Renseigne tout de suite les shorts existants avec la liste ci-dessous (épisode → URL).
Ne change rien d'autre (statuts, textes, miniatures).

## Liste des shorts (déjà hébergés dans la bibliothèque RapidoCMS)

| Épisode | Short |
|---|---|
| 7 | https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/episode7-short.mp4 |
| 31 | https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/episode31-short.mp4 |
| 32 | https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/episode32-short.mp4 |
| 33 | https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/episode33-short.mp4 |
| 34 | https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/episode34-short.mp4 |
| 35 | https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/episode35-short.mp4 |
| 36 | https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/episode36-short.mp4 |
| 37 | https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/episode37-short.mp4 |
| 62 | https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/episode62-short.mp4 |
| 63 | https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/episode63-short.mp4 |
| 64 | https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/episode64-short.mp4 |
| 65 | https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/episode65-short.mp4 |
| 66 | https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/episode66-short.mp4 |
| 67 | https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/episode67-short.mp4 |
| 68 | https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/episode68-short.mp4 |
| 69 | https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/episode69-short.mp4 |
| 70 | https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/episode70-short.mp4 |
| 71 | https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/episode71-short.mp4 |
| 72 | https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/episode72-short.mp4 |

Épisodes 0 à 6, 8 à 30 et 38 à 61 : aucun short trouvé (ni dans le dépôt, ni dans RapidoCMS).
