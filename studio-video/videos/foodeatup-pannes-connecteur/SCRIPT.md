# Connecteur FoodEatUp : les 5 pannes fréquentes — 47 s, vertical 1080×1920

Les cinq pannes réelles au branchement du connecteur et leur solution.

**Source du contenu :** `src/data/connecteur-mcp.ts` (ERREURS_FREQUENTES : symptôme, cause, solution).

- Voix : **Adam - Instructor** (`TGAegA0zNRi8I6nUdq3i`), `eleven_multilingual_v2`, prise 1 sur 2.
- Musique : ElevenLabs Music v2.5 (`m-tech4`), instrumentale, sous la voix.
- Audio normalisé à −16 LUFS ; scènes, éléments et sous-titres calés sur la transcription mot à mot ElevenLabs Scribe.
- Flow ElevenLabs : `XBWW3jSkIoTotuA5WrkJ`. Montage généré par `tools/gen_page_video.py`.

## Voix off

Votre connecteur FoodEatUp ne répond pas ? Voici les cinq pannes les plus fréquentes. Un : connecté, mais aucun outil. Vérifiez que l'adresse finit bien par /mcp, puis retirez et rajoutez le connecteur. Deux : le client réclame une clé. Choisissez aucune authentification : le connecteur de l'Académie est public. Trois : erreur 406. L'en-tête Accept doit annoncer JSON et event stream ; les clients officiels le font seuls. Quatre : l'assistant répond de mémoire. Nommez la source : avec le connecteur de l'Académie FoodEatUp. Cinq : les réponses arrivent en anglais. Écrivez votre question en français. Et la page santé du connecteur affiche le nombre d'outils réellement servis.

## Scènes

| Début | Scène | Éléments |
|---|---|---|
| 0.00 s | Accroche | 5 pannes |
| 4.75 s | 1 · Aucun outil | L'adresse finit par /mcp · Retirer, puis rajouter |
| 13.22 s | 2 · Il réclame une clé | Authentification : aucune · Le connecteur de l'Académie est public |
| 19.96 s | 3 · Erreur 406 | Accept: application/json, text/event-stream · Les clients officiels le font seuls |
| 29.20 s | 4 · Réponse de mémoire | Avec le connecteur de l'Académie FoodEatUp, donne-moi le parcours d'un chef de rang |
| 35.30 s | 5 · Réponses en anglais | En français |
| 39.70 s | Fin |  · tutoriel.foodeatup.com/mcp/sante · Le nombre d'outils servis ·  |

Rendu : `renders/foodeatup-pannes-connecteur-v1.mp4`.

## Publication
Archivée dans la bibliothèque RapidoCMS. **Aucune publication sur les réseaux sans validation humaine de la pièce.**
