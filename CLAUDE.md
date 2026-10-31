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

## Vignettes « Mes projets » : design des couvertures projet

Chaque vignette d'épisode Mes projets et chaque couverture de projet suit le
design des couvertures projet (référence : couverture RapidoCRM) — jamais une
image extraite de la vidéo :

1. Hook en gros (Poppins 800) avec le dernier mot surligné en orange, écran
   réel du projet dans un cadre tablette, photo d'entrepreneur de Michael dans
   un cercle à bordure bleue, punchline, logo officiel (tuile blanche, sinon le
   nom en texte) et badge bleu « MES PROJETS », fond bleu nuit.
2. Avant tout nouveau projet ou épisode : renseigner `hook` et `punchline` du
   projet (`modifier_projet`) et disposer d'un écran réel.
3. Composer avec `generer_couvertures_projet` quand le projet a un écran actif ;
   sinon avec `videos/mes-projets/vignettes/` (`data.json` + `node make.js`) :
   la 1080x1920 sert de miniature d'épisode, la 1280x720 de couverture projet
   (`source_url`). Ajouter chaque vignette à la bibliothèque (`ajouter_media`).

## Assets de projet : tout ce qui est créé y est rattaché

Chaque nouvelle image, icône, capture d'écran, miniature, couverture ou vidéo
liée à un projet est ajoutée aux assets de ce projet (`ajouter_asset_projet`,
ou `ajouter_media` avec le tag du slug) pour être réutilisée dans d'autres
vidéos. Avant un épisode, récupérer le kit du projet via le MCP
(`obtenir_projet`, `obtenir_page_projet`, `lister_assets(projet_slug)`) et
réutiliser ses écrans, icônes et cartes plutôt que d'en recréer.
