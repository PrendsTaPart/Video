# Runbook — boucle nocturne « 30 routines » (production autonome)

À CHAQUE réveil de la boucle (message AUTO), produire **UN** épisode puis re-programmer le suivant.

## Étapes (épisode N = `serie-etat.json.episode_courant`)
1. Si N > 30 → **STOP** (ne pas re-programmer). Prévenir Michael : série terminée.
2. **Re-armer tout de suite** le prochain réveil (`send_later` +2 min, même message AUTO) — garantit
   la continuité même si cette itération échoue (N n'avance qu'en cas de succès).
3. Lire l'épisode N dans `scripts/saison-{1,2,3}.md` (hook Mika, VO routine/prompt/cas, CTA rotatif
   `(N-1)%3` → A/B/C, teaser = titre de N+1). Charte : accent indigo `#5A67F2`, overlays BraindCode + `E{N}/30`.
4. Projet : `cp -r serie-30-e01 serie-30-e{NN}` ; nettoyer ; générer 4 VO ElevenLabs (Adam, direct curl
   mp3→wav, retries) : `mika-in`, `routine`, `prompt`, `cas`.
5. **Hook Mika** : chercher dans `mika-assets/MANIFEST.md`. Absent → générer (HeyGen : avatar
   `bd56633302aa4790a8d526fe2ee6b63f`, voice audio=upload wav `audio/x-wav`, bg `#00B140`, dim 1080×1920),
   poller, télécharger → `serie-30-e{NN}/mika/mika-in.mp4`, ajouter au manifeste.
6. **Outro** : réutiliser `mika-assets/raw/cta-{A|B|C}-generique.mp4` selon la rotation → `mika/mika-out.mp4`.
7. `audio_meta.json` (clés frame, mots even-split, bgm null) + `STORYBOARD.md` (3 frames, durées = VO).
8. Frames : 3 HTML verticales (frame 2 prompt = adapter le gabarit terminal ; frames 1 & 3 = contenu de l'épisode).
9. captions.mjs (injecter `--cap-accent #5A67F2`) → assemble-index.mjs → transitions.mjs → vendor gsap →
   `npm run check` (0 erreur) → `npm run render` → `body.mp4`.
10. Montage : `build-episode.sh` (PROJ, EP, ELABEL=E{N}/30, HOOK, OUTRO, TEASER1=DEMAIN, TEASER2=teaser,
    BODY=body.mp4, OUT=deliverable/…mp4). Overlays + BGM + loudnorm -14 inclus.
11. `.gitignore` (renders/ mika/) → commit + push `claude/hyperframes-reels-studio-9f0b63`.
12. Archive CMS : get_file_contents (URL raw fraîche) → `upload_file_tool`.
13. LinkedIn : `create_draft_tool` (linkedin, account 101119080, mediatext, media_url S3, caption hook+corps+teaser+#30routines)
    → `schedule_draft_tool` date = 2026-07-10 + N jours (E1=11/07), heure 08:00:00.
    **TikTok** : si `tiktok_account_id` valide à la publication → 2ᵉ draft tiktok (account 5) ; sinon SKIP + noter.
14. `serie-etat.json` : `episode_courant = N+1`, ajouter à `historique`. Commit + push.
15. Livrer à Michael (bref) : E{N} fait + lien programmé. Continuer (le réveil re-armé en étape 2 fera N+1).

## Garde-fous
- 1 épisode/réveil. Jamais publier direct (drafts programmés, annulables).
- Sur échec (HeyGen/réseau/CMS) : ne PAS incrémenter `episode_courant` → l'épisode sera repris au prochain réveil.
- Rendus HyperFrames = locaux/gratuits. Seul coût = 1 génération HeyGen (hook) par épisode.
