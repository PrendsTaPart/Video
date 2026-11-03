# Routine "1 skill / jour × 2" — runbook

Objectif : **2 fois par jour (11h30 & 16h30 Paris)**, produire automatiquement une **vidéo TikTok
verticale (1080×1920)** qui explique **un skill du plugin BraindCode** (connecté à un MCP), avec
**un prompt Claude montré à l'écran** et **le résultat dans le logiciel**, puis la **publier sur
LinkedIn FoodEatUp**.

## Ce qui est en place
- **Ledger** : `videos/skill-videos/LEDGER.md` (FILE = à faire, FAIT = produits). Un run = 1 skill.
- **Pipeline vidéo** : identique aux 9x16 déjà livrés (voir n'importe quel `videos/*-9x16/`).
- **LinkedIn** : compte FoodEatUp connecté dans RapidoCMS → `account_id = 68807312` (network linkedin).
- **Voix** : ElevenLabs Adam `TGAegA0zNRi8I6nUdq3i`, clé dans `studio-video/.env` (suivie par git).

## Déclenchement (durable — à activer une fois)
Le planificateur interne d'une session de chat est **éphémère** (meurt avec la session, 7 j max).
Pour du **permanent**, activer UN de ces déclencheurs externes qui relancent ce runbook :
- **Claude Code (web) — déclencheur planifié** sur cet environnement (recommandé : MCP + secrets déjà là).
  Programmer 2 déclencheurs : `30 11 * * *` et `30 16 * * *` (heure de Paris) avec le PROMPT ci-dessous.
- **GitHub Actions** : `.github/workflows/daily-skill-video.yml` (scaffold fourni — voir les TODO secrets).

## PROMPT de routine (à coller tel quel dans le déclencheur — session autonome)

```
Tu es le studio vidéo FoodEatUp. Exécute la routine "1 skill / cas d'usage".

1. Lis videos/skill-videos/LEDGER.md. Prends le PREMIER skill de la section FILE
   (s'il est vide, pioche un skill non encore dans FAIT depuis references/mcp-plugins-video-catalog.md).
2. Construis une vidéo TikTok VERTICALE 1080×1920 sur ce skill, en 5 frames, arc :
   pain → reveal → le skill en action → « et avec Claude » (prompt montré + résultat dans le logiciel)
   → bénéfice/CTA. Réutilise le gabarit d'un projet videos/*-9x16 existant comme modèle
   (frames portrait, captions karaoké en bas, charte off-white #F7F9FC / navy #1B2A41 / bleu #1E9BF0 /
   vert #059669, Poppins+Inter locaux). Réutilise les images de videos/shared-images/ ;
   ne génère de nouveaux visuels via RapidoCMS generate_image que si nécessaire (et copie-les dans shared-images/).
3. Voix off : écris le script, génère la VO (media-use audio.mjs --only tts --provider elevenlabs --lang fr,
   voix TGAegA0zNRi8I6nUdq3i, clé depuis studio-video/.env). Re-transcris en français les lignes à 0 mot
   (npx hyperframes transcribe … --language fr) et fusionne dans audio_meta.json (clés "frame", pas "id").
   Ajoute BGM assets/bgm/track.mp3 @0.18 + quelques SFX.
4. Assemble (product-launch-video scripts : captions.mjs → assemble-index.mjs → remplacer le CDN gsap par
   assets/vendor/gsap.min.js → transitions.mjs inject), lint+inspect (0 erreur / 0 layout issue),
   render, QA en extrayant des frames avec ffmpeg (image en haut, contenu empilé, captions lisibles,
   CTA présent, « FoodEatUp » bien orthographié).
5. Renomme le rendu proprement, commit + push sur la branche claude/hyperframes-reels-studio-9f0b63
   (auteur noreply@anthropic.com / Claude). Archive la vidéo dans RapidoCMS (upload_file_tool depuis
   l'URL brute GitHub) — récupère un token frais juste avant l'upload.
6. Publication LinkedIn FoodEatUp : RapidoCMS create_draft_tool (social_type linkedin, account_id 68807312,
   post_type mediatext, media_type video, media_source biblio, media_url = URL S3 de la vidéo dans la
   bibliothèque, media_caption = accroche FR + 3-5 hashtags). PAR DÉFAUT : ne PAS auto-publier —
   créer un BROUILLON PROGRAMMÉ (schedule_draft_tool à la date du jour, heure 11:30:00 ou 16:30:00)
   pour que Michael valide/annule dans RapidoCMS avant diffusion. (Passer en publication directe seulement
   sur instruction explicite de Michael.)
7. Déplace la ligne du skill de FILE vers FAIT dans LEDGER.md (avec la date), commit + push.
8. Livre à Michael : le MP4 + le lien du brouillon LinkedIn + le skill traité + le prochain de la file.
```

## Sécurité / garde-fous
- **Jamais** de publication directe non validée par défaut : la routine crée un **brouillon programmé**
  (visible et annulable dans RapidoCMS via list_scheduled_posts / cancel_schedules_post) — Michael garde la main.
- Un rendu raté ne doit pas partir : la QA (frames ffmpeg) doit valider avant l'étape LinkedIn.
- Une seule vidéo par run (1 skill), pour borner le coût et le temps.

## Réglages faciles (dis-le simplement en chat)
- Changer les horaires, passer à 1×/jour, ou activer la publication directe automatique.
- Étendre la FILE avec d'autres skills du catalogue.
