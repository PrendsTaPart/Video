# Routine "Série Rapido" — 1 vidéo/jour jusqu'à la fin des 28 épisodes

## PROMPT de routine (à coller dans le déclencheur — session autonome)

```
Tu es le studio vidéo BraindCode. Produis LE PROCHAIN épisode de la série Rapido.

1. Lis videos/rapido-series/LEDGER.md → prends le PREMIER épisode coché [ ] de la FILE.
   Lis sa ligne détaillée dans videos/rapido-series/CALENDAR.md (fil conducteur de la saison,
   skill/tools, prompt Claude à montrer, résultat logiciel). Lis references/rapido-brand.md
   (palette de la saison, logos, mockups, règles de wording « Rapido »).
2. Construis une vidéo TikTok VERTICALE 1080×1920, 5 frames, avec :
   - un HOOK de début à impact (question choc / promesse / chiffre) ;
   - le SKILL en contexte + une frame « avec Claude » : bulle prompt utilisateur (navy) →
     réponse Claude (✓ vert) → puis le RÉSULTAT dans le logiciel (réutiliser le mockup de la saison :
     videos/shared-images/rapido/rapido{rh,cms,crm}-mockup.*) ;
   - un HOOK de fin à impact + logo de la saison + CTA « Découvrir Rapido<App> » ;
   - accent = couleur de la saison (RH violet #7850C0 / CMS bleu #00A8F0 / CRM vert #48A850 /
     Orchestration tri-color), fond #F7F9FC, Poppins+Inter, sous-titres karaoké en bas.
   Réutilise le gabarit d'un projet videos/*-9x16 existant comme modèle technique.
   Génère via RapidoCMS generate_image seulement les visuels manquants, range-les dans shared-images/rapido/.
3. Voix off FR (Adam TGAegA0zNRi8I6nUdq3i, clé studio-video/.env), transcription --language fr,
   audio_meta clés "frame", BGM assets/bgm/track.mp3 @0.18 + SFX.
4. captions.mjs → **recolore l'accent des captions à la couleur de la saison** (injecte
   `--cap-accent`/`--primary` = #7850C0 RH / #00A8F0 CMS / #48A850 CRM dans le bloc
   `<style data-brand-tokens>` de compositions/captions.html) → assemble-index.mjs → vendor gsap local → transitions.mjs inject → lint+inspect
   (0 erreur / 0 layout issue) → render → QA frames ffmpeg (hooks lisibles, prompt+résultat clairs,
   logo/CTA présents, orthographe des marques). Nomme le rendu, commit+push sur
   claude/hyperframes-reels-studio-9f0b63, archive dans RapidoCMS.
5. Publication : create_draft_tool (social_type linkedin, account_id = compte RapidoSoftware 101119107 (RÈGLE ARRÊTÉE), post_type mediatext, media video biblio, media_url = URL S3 de la vidéo,
   caption FR + hashtags jouant sur « Rapido ») → PAR DÉFAUT schedule_draft_tool à la date du jour, post_heure=16:00:00 (publication programmée 16h ; annulable avant dans RapidoCMS). Publication directe seulement si Michael l'a demandé.
6. Coche l'épisode dans LEDGER.md (déplace-le en FAIT avec date + chemin projet), commit+push.
7. Livre à Michael : MP4 + lien du brouillon + épisode traité + prochain épisode de la file.
   Quand la FILE est vide : préviens Michael que la série des 28 est terminée.
```

## Garde-fous
- 1 épisode par run (borne coût/temps). Respecter l'ORDRE de la file (pas de saut).
- QA obligatoire avant l'étape LinkedIn. Publication = brouillon programmé par défaut (jamais direct sans accord).
- Cadence : 1×/jour (voir cron / déclencheur). Durée totale ≈ 28 jours.

## Déclenchement durable
Idem FoodEatUp (voir videos/skill-videos/ROUTINE.md) : le planificateur de chat est éphémère (7 j max).
Pour du permanent : **déclencheur planifié Claude Code (web)** ou **workflow n8n** (skill usine-automatisations)
ou **GitHub Actions**, en lançant le PROMPT ci-dessus une fois par jour.
