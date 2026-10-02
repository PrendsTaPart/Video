# Budget — La Brigade augmentée en vidéo

Coûts estimés puis réels, étape par étape. Aucune génération payante n'est lancée sans validation
écrite. Chaque appel facturé est noté ici, plan par plan.

| Étape | Outil | Estimé | Réel | Statut |
|---|---|---:|---:|---|
| 0 · Audit du dépôt | ffprobe, webrtcvad (local) | 0 $ | 0 $ | ✅ fait |
| 1 · Extraction Figma | Figma MCP (lecture seule, compris dans l'abonnement) | 0 $ | 0 $ | ✅ fait |
| 2 · Voix + musique + bruitages | ElevenLabs | à chiffrer (`estimate_only`) | — | ⏸ en attente de validation |
| 3A · Motion design | HyperFrames local | 0 $ | — | — |
| 3B · Plans hero (≈ 21) | image-to-video ElevenLabs | à chiffrer | — | ⏸ un plan test d'abord |
| 4 · Montage + rendu | HyperFrames local | 0 $ | — | — |
| 6 · Brouillons | RapidoCMS | 0 $ | — | — |

## Volumes connus après l'étape 1 (pour chiffrer l'étape 2)

| Élément | Volume |
|---|---:|
| Plans du storyboard | 290 (100 récitatifs, 136 bulles, 54 titres) |
| Texte à dire (récitatifs + bulles) | 14 973 caractères, 236 répliques |
| Durée voix estimée | ≈ 20 min (débit ~14 caractères/s) |
| Voix distinctes | 8 personnages, 4 agents IA, l'assistant IA, 11 rôles secondaires |
| Ambiances musicales | 7 (une par partie + épilogue) |
| Bruitages à créer | 2 (téléphone, friture isolée), les autres existent dans le dépôt |
| Plans hero | 21 cases |

Les 54 titres (couverture, cartes personnages, titres de partie, fermeture) sont prévus à l'écran sans voix.
S'il faut les faire lire par le narrateur, il faut compter environ 6 200 caractères de plus.
