# Règles pour ce dépôt

## Higgsfield : ne jamais générer de nouvelles vidéos

Ne PAS générer de nouveaux plans vidéo via l'API/MCP Higgsfield. Si un plan
vidéo est nécessaire :

1. **Chercher d'abord dans la bibliothèque Higgsfield existante** (assets déjà
   générés dans ce projet, ex. `hero-video/assets/video/`) et réutiliser un
   plan déjà généré plutôt que d'en produire un nouveau.
2. Si aucun plan existant ne convient, **ne pas appeler Higgsfield** — donner
   à l'utilisateur le prompt (texte + Reference Elements/character IDs
   nécessaires) pour qu'il le génère lui-même dans l'interface Higgsfield.

Cette règle s'applique à toutes les sessions futures sur ce dépôt.

## Une seule prise : ElevenLabs et vidéos

Toute génération (voix ElevenLabs, vidéo, image) se fait en **une seule prise** :
`generations_count=1`, jamais la valeur par défaut (2 prises pour la voix).
Ne jamais relancer une génération déjà faite ni « pour comparer » : réutiliser
la prise existante (flow ElevenLabs, fichier du dépôt). Pas de doublon.

## Bibliothèque : toute nouvelle image ou thème y est ajouté

Objectif : ne jamais payer deux fois pour la même image.

1. **Avant de créer ou chercher une image** (logo, portrait, décor, personnage,
   capture), consulter la bibliothèque du Journal (MCP Journal :
   `lister_assets`, `lister_medias`) et la réutiliser si elle existe.
2. **Chaque nouvelle image** (logo récupéré sur internet, photo Wikimedia,
   image générée, capture, miniature) est **ajoutée à la bibliothèque** avec
   `ajouter_media` dès sa création : clé, titre, catégorie, URL https stable
   (raw GitHub sur un commit, ou S3 RapidoCMS), dimensions et vraie source
   (licence et crédit obligatoire pour Wikimedia, « génération IA » si générée).
3. **Chaque nouveau thème visuel** (palette, typo, style d'un épisode) est
   ajouté à la bibliothèque : sa planche d'aperçu via `ajouter_media`
   (catégorie `video`, tag `theme`) et sa définition dans
   `videos/_journal-63-72/themes.json`.
4. Les assets créés par Lovable (projet michael-au-quotidien) suivent la même
   règle : ils sont référencés dans la bibliothèque du Journal avant usage.

## Portrait de Michael

Utiliser la photo d'entrepreneur (veste) : `videos/_journal-63-72/commun/michael-rond.png`
ou `michael-portrait.jpg`. Ne pas utiliser la photo en tenue de chef
(`michael-chef-mascot.jpg`) sauf demande explicite.
