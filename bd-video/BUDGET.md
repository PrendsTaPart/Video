# Budget — La Brigade augmentée en vidéo

Coûts estimés puis réels, étape par étape. Aucune génération payante n'est lancée sans validation
écrite. Chaque appel facturé est noté ici, plan par plan.

| Étape | Outil | Estimé | Réel | Statut |
|---|---|---:|---:|---|
| 0 · Audit du dépôt | ffprobe, webrtcvad (local) | 0 $ | 0 $ | ✅ fait |
| 1 · Extraction Figma | Figma MCP (lecture seule, compris dans l'abonnement) | 0 $ | 0 $ | ✅ fait |
| 2 · Voix + musique + bruitages | ElevenLabs | **≈ 5,00 $** (détail ci-dessous) | — | ⏸ en attente de validation |
| 3A · Motion design | HyperFrames local | 0 $ | — | — |
| 3B · Plans hero (≈ 21) | image-to-video ElevenLabs | à chiffrer | — | ⏸ un plan test d'abord |
| 4 · Montage + rendu | HyperFrames local | 0 $ | 0 $ | 🔄 animatique ep01 en cours |
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

## Devis de l'étape 2 (relevé avec `estimate_only`, le 2026-10-02)

Prix constaté : **0,165 $ pour 1 000 caractères** (162 caractères = 162 crédits = 0,027 $), identique en `eleven_v3` et `eleven_multilingual_v2`.

| Poste | Volume | Prix unitaire | Total estimé |
|---|---:|---:|---:|
| Voix (eleven_v3, 1 prise par réplique) | 236 répliques · 17 331 caractères (balises d'intention comprises) | 0,165 $ / 1 000 car. | **2,86 $** |
| Musique (eleven_music_v2_5) | 7 ambiances | 0,30 $ / piste (estimation à durée par défaut) | **2,10 $** |
| Bruitages (eleven_text_to_sound_v2) | 3 (téléphone, friture, écran qui s'allume) | 0,01 $ | **0,03 $** |
| **Total étape 2** | | | **≈ 5,00 $** |

Les échantillons de casting (`audio/casting/`) sont les extraits gratuits fournis par ElevenLabs : 0 $.
Aucune reprise n'est relancée sans accord ; une reprise d'une réplique coûte environ 0,001 à 0,004 $.
