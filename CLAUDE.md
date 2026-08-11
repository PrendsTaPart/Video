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

## Vignettes : toujours avec la photo du chef

Toute vignette d'épisode — sur les réseaux comme sur FoodEatUp Social — se
génère **à partir de la photo de référence du chef** :

`foodeatup-social/public/brand/chef-foodeatup.jpg`
(en ligne : `https://raw.githubusercontent.com/PrendsTaPart/Video/claude/foodeatup-video-factory-wtb7gs/foodeatup-social/public/brand/chef-foodeatup.jpg`)

À chaque nouvel épisode, il faut donc produire **trois choses** — et rien d'autre :

1. **le prompt d'image**, déjà écrit dans `promptVignette` de l'épisode ;
2. **la photo du chef**, à joindre comme image de référence au générateur ;
3. **le lien de la vidéo montée**.

Le prompt impose au générateur de conserver le visage, la toque, la veste et le
tablier au logo FoodEatUp. Ne jamais laisser un générateur redessiner le chef ni
inventer un autre personnage : c'est la même personne sur les 150 épisodes, c'est
ce qui fait la série.

Le titre de la vignette fait **deux ou trois mots**, dans `troisMots`. Il vient du
chapitre, pas de l'accroche : c'est ce que la vidéo montre, pas ce qu'elle
raconte. Ne pas compléter à trois mots en collant le nom du module — ça produit
du français cassé (« TON CONFIGURER CAISSE ») ; deux mots justes valent mieux.

Ces champs sont générés par `foodeatup-video-factory/scripts/gen-publications.py`,
qui écrit aussi les cinq publications de chaque épisode (Facebook, Instagram,
TikTok, LinkedIn, YouTube). Il ne s'édite pas à la main.
