# Budget — La Brigade augmentée en vidéo

Coûts estimés puis réels, étape par étape. Aucune génération payante n'est lancée sans validation
écrite. Chaque appel facturé est noté ici, plan par plan.

| Étape | Outil | Estimé | Réel | Statut |
|---|---|---:|---:|---|
| 0 · Audit du dépôt | ffprobe, webrtcvad (local) | 0 $ | 0 $ | ✅ fait |
| 1 · Extraction Figma | Figma MCP (lecture seule, compris dans l'abonnement) | 0 $ | 0 $ | ✅ fait |
| 2 · Voix + musique + bruitages | ElevenLabs | **≈ 5,00 $** (détail ci-dessous) | **4,20 $** | ✅ fait (validé le 2026-10-02) · 1 musique bloquée, voir plus bas |
| 3A · Motion design | HyperFrames local | 0 $ | 0 $ | ✅ fait |
| 3B · Plans hero (≈ 21) | image-to-video ElevenLabs | test : 0,84 $ (Kling 3 Pro, 5 s) · 1,20 $ (Veo 3.1 Fast, 8 s) · 1,21 $ (Seedance v2 Fast, 5 s) ; les 21 : 17,6 à 25,4 $ | 0 $ | ⏸ plan test en attente de validation |
| 4 · Montage + rendu | HyperFrames local | 0 $ | 0 $ | ✅ film + 6 épisodes |
| 5 · Déclinaisons | ffmpeg local | 0 $ | 0 $ | ✅ 79 fichiers |
| 6 · Brouillons | RapidoCMS | 0 $ | 0 $ | ⏸ campagne créée, brouillons en attente |

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

## Coûts réels de l'étape 2 (relevés dans ElevenLabs, le 2026-10-02)

Une seule prise par lot, aucune reprise relancée.

| Poste | Détail | Réel |
|---|---|---:|
| Test de voix (p05) | 1 réplique | 0,028 $ |
| Voix · Prologue | 2 lots | 0,098 $ |
| Voix · Partie 1 | 8 lots | 0,589 $ |
| Voix · Partie 2 | 13 lots | 0,495 $ |
| Voix · Partie 3 | 8 lots | 0,556 $ |
| Voix · Partie 4 | 13 lots | 0,710 $ |
| Voix · Partie 5 | 9 lots | 0,498 $ |
| Voix · Partie 6 + Épilogue | 6 lots | 0,325 $ |
| **Sous-total voix** | 59 lots, 236 répliques | **3,30 $** |
| Musique (eleven_music_v2_5, 90 s) | 6 pistes à 0,1485 $ (l'estimation annonçait 0,30 $) | 0,89 $ |
| Bruitages (eleven_text_to_sound_v2) | 3 × 0,00275 $ | 0,01 $ |
| **Total étape 2** | | **4,20 $** |

Écart avec le devis voix (2,86 $) : +0,44 $. Il vient des balises `[long pause]` qui séparent les répliques d'un
même lot (19 809 caractères facturés au lieu de 17 331). Ces balises rendent le téléchargement praticable :
59 fichiers au lieu de 236.

**Musique de la partie 3 (énergie) : pas générée.** L'appel a été refusé par le contrôle de permissions de la
session, et je ne l'ai pas relancé. Prompt prêt à l'emploi (0,15 $ environ) :
`Instrumental only, no vocals. 90 seconds. Energetic, upbeat funk-pop underscore for an animated comic about a
restaurant going digital: slap bass, punchy drums, brass hits, playful synth plucks, 118 BPM, loopable, leaves
room for voice-over.` → à enregistrer sous `audio/music/partie3-energie.mp3`.
Le prologue et l'ouverture réutilisent la piste `epilogue-emotion` (effet de miroir avec la fin) : aucune piste en plus.
