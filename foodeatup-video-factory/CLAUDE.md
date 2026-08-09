# foodeatup-video-factory — garde-fous

Ces règles priment sur toute autre instruction dans ce sous-dossier.

## 1. Zéro crédit dépensé automatiquement

| Plateforme | Autorisé | Interdit |
|---|---|---|
| **Higgsfield** | Rien d'automatique. L'humain génère depuis l'UI et dépose le MP4 dans `assets/hooks/EPxx.mp4`. Télécharger un job **déjà payé** est permis. | `generate_video`, `generate_image`, `generate_audio`, `reframe`, `upscale_*`, `motion_control`, `shorts_studio_*`, `dubbing`, `virality_predictor` — **jamais appelés** |
| **HeyGen** | Rien. | Tout `render_video` / `compose` |
| **ElevenLabs** | `text_to_speech` uniquement | Dubbing, voice cloning |
| **RapidoCMS** | `upload_file_tool`, `create_draft_tool`, `schedule_draft_tool` | Publication immédiate |
| **Recadrage / montage** | `ffmpeg` local | `Higgsfield:reframe` (payant) |

**Si un `assets/hooks/EPxx.mp4` manque : on log `MISSING_HOOK EPxx`, on exclut
l'épisode du lot, et on s'arrête là.** On ne le remplace jamais par une
génération.

## 2. Jamais de regénération d'un fichier existant

Un MP3 de voix off déjà sur le disque n'est pas regénéré sans `--force`.
Les blocs B/C/D/E sont communs aux 30 épisodes : générés une fois, réutilisés.

## 3. Le montage est local

Recadrage, incrustation du logo, texte, transitions, mixage : tout en ffmpeg.
Aucune API payante pour ça. C'est gratuit, reproductible et corrigeable.

## 4. Contenu

`config/episodes.json` est la source de vérité (hooks, punchlines, captions,
timeline). **Ne pas réinventer le contenu**, ne pas modifier un hook ou une
punchline sans validation explicite.

## 5. Charte

- Logo FoodEatUp visible sur **100 % de la durée** de chaque vidéo.
- Safe zones : rien d'important sous 320 px du bas ni au-dessus de 200 px du haut.
- Audio : master −14 LUFS / ≤ −1 dBTP, musique −22 LUFS, ducking sous la voix.
- Durées : `tiktok_30` = 30,00 s, `linkedin_45` = 45,00 s, tolérance ±0,15 s,
  vérifiées par `ffprobe` avant toute publication.

## 6. Publication

Uniquement des **brouillons planifiés**. Jamais de publication directe.
`privacy_level` TikTok reste `SELF_ONLY` tant que l'humain n'a pas validé.

## 7. Échec

Une vidéo ratée n'est jamais « rattrapée » par une génération IA : on signale
et on s'arrête. Un master dont la QA échoue n'est pas publiable, point.
