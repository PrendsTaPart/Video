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
