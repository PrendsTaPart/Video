# R9 — VIDEO-FACTORY (routine quotidienne · série « 30 routines »)

> À installer dans le plugin sous `loop-engine-v2/references/routines/R9-VIDEO-FACTORY.md`
> et à référencer dans le `SKILL.md` de loop-engine-v2 (déclencheurs : « lance R9 »,
> « épisode du jour », « video factory »). Ce fichier est la version de référence de la série.

## Déclenchement (Claude Code ne se réveille pas seul)

**Recommandé — A.** n8n *Schedule Trigger 07:00 Europe/Paris* → nœud *Execute Command* :
`claude -p "Lance R9 VIDEO-FACTORY épisode du jour"` sur la machine/serveur où le plugin
et les MCP sont configurés. Un 2ᵉ workflow n8n à **08:15** vérifie via `list_scheduled_posts`
que les 2 posts du jour existent et alerte sinon.
**B.** cron système : `0 7 * * * cd ~/plugin && claude -p "Lance R9 épisode du jour" >> logs/r9.log`

## Prompt de routine

```
Tu exécutes R9 VIDEO-FACTORY — épisode du jour de la série « 30 routines ».

CONFIG:
- fichier_serie: ./rapido-kb/serie-30-episodes.md (+ scripts/saison-{1,2,3}.md, mika-textes.md)
- etat: ./rapido-kb/serie-etat.json  (episode_courant, historique, budget, pause)
- linkedin_account_id: 101119080 (BraindCode)
- tiktok_account_id: {depuis serie-etat.json — BLOQUANT si null}
- heure_publication: 08:00:00 | budget_rendu_max_jour: {serie-etat.json.budget.plafond_par_jour}
- designSource: blockframe (registre pop, vertical)

GARDE-FOU 0: si serie-etat.json.pause == true OU budget.rendu_autorise == false → STOP + explique.

SENSE:
1. Lis serie-etat.json → épisode N (= date - date_debut + 1). Si N > 30: STOP (série terminée).
2. Charge l'épisode N : ligne de serie-30-episodes.md + script complet (scripts/saison-*.md)
   + textes Mika in/out (mika-textes.md) + CTA rotatif [(N-1) mod 3] + teaser N+1.
3. Vérifie en bibliothèque CMS: mika-e{N}-in et mika-e{N}-out (list_all_files).
   ABSENTS → alerte + tâche RapidoRH urgente + STOP (JAMAIS d'épisode sans Mika).
4. list_prompts: réutilise le prompt visuel gagnant de la série s'il existe.

ACT:
1. Génère le(s) visuel(s) de l'épisode (generate_image, style série 9:16, AUCUN texte incrusté
   — protocole zéro-faute). Au 1er épisode réussi, sauvegarde le prompt gagnant (add_prompt).
2. Narration VO: texte EXACT du script (gabarit 5 blocs déjà rempli) via /hyperframes-media TTS
   (voix série), transcription --language fr, audio_meta clés "frame".
3. compose HyperFrames 9:16 1080×1920 SANS projectId: gabarit fixe 5 blocs (hook Mika / routine /
   prompt machine-à-écrire ≥4s / cas d'usage / hook fin Mika), timecodes calés sur durées audio
   réelles, clips Mika aux positions, sous-titres incrustés (max 6 mots), overlay « E{N}/30 »,
   logo BraindCode discret, musique série -18 dB, 1 SFX/transition.
4. RENDU: render_video SEULEMENT si budget.rendu_autorise==true ET coût ≤ plafond_par_jour ET
   statut draft/completed. Sinon: tâche RH + STOP. Polling get_render_status 30s.

FEED:
1. upload_file_tool (type video) du MP4 final → récup file_url.
2. create_draft_tool ×2 — media_source 'biblio', media_url = file_url, post_type mediatext,
   post_heure '08:00:00', post_date du jour:
   (a) social_type linkedin, account 101119080, copy = hook + 3 lignes + #30routines;
   (b) social_type tiktok, account {tiktok_account_id}, copy courte + hashtags TikTok.
   PIÈGE: les champs media_* sont requis.
3. schedule_draft_tool sur les 2 brouillons.
4. Mets à jour serie-etat.json (episode_courant=N+1, historique[N]={IDs, coût, durée}) + log prompt visuel.

REPORT (bref): épisode N publié 8h (2 liens), coût rendu, cumul budget, teaser N+1, anomalies.
Sur échec à toute étape: tâche RapidoRH priorité haute (projet 29, colonne 95) + notification.
JAMAIS de publication d'un épisode dégradé (sans Mika, sans sous-titres, ou hors charte).
```

## Gouvernance (dérogation encadrée au render payant)

1. **Validation batch avant J1** : 30 scripts + gabarit visuel + pilote E1 rendu & approuvé.
2. **Pré-autorisation budgétaire écrite** dans serie-etat.json (`budget.rendu_autorise=true`,
   plafonds) — la routine s'arrête d'elle-même si dépassement ou hors-gabarit.
3. **Kill switch** : `pause:true` dans serie-etat.json (ou suppression du fichier) stoppe tout.

## Rattrapage d'un épisode raté

Re-run manuel : `Lance R9 épisode N` (met à jour l'historique sans avancer episode_courant si N < courant).
