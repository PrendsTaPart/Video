# Livraison — « RapidoCMS & son MCP en 4 minutes » (16:9)

## Fichier final
- `deliverable/rapidocms-mcp-4min.mp4` — **1920×1080**, **2:02** (≤ 4:00), H.264 + AAC, ~11 Mo.
- Rendu **local** (ffmpeg, gratuit) — le `render_video` HeyGen MCP est désactivé en CLI, non utilisé (aucune action payante).

## Contenu (9 chapitres)
Hook (perso-stressé) → Intro **Mika** → Connecter vos réseaux (Instagram via Facebook) →
⭐ **Connecter votre IA (MCP)** : `cms.rapidosoftware.com/mcp` affiché ~17 s + logos **Claude · Mistral · OpenAI** →
Générer & ranger vos visuels → ⭐⭐ Créer & planifier vos posts (date AAAA-MM-JJ · heure HH:MM:SS) →
Campagnes & analyse → Pilotage quotidien → Outro (perso-heureux, CTA démo).
- **4 « Astuces du Chef »** en scènes **chat Claude** (fond sombre, prompt + « ✓ Exécuté par votre IA » + résultat RapidoCMS).
- **Lower-thirds** avec les **familles d'outils MCP réels** (`list_connected_accounts`, `create_draft_tool · schedule_draft_tool`, `create_campagne · ingishts_campagne`, …).

## Fichiers
- `script/analyse-mcp.md` — outils réels du MCP RapidoCMS par famille (7 familles)
- `script/voix-off.md` — script (13 segments, timecodes, [MIKA]/[ÉCRAN]/[ANIMATION CLAUDE])
- `storyboard/storyboard.md` — plan par plan + mapping assets
- `build_rcms.py` — compositeur frames (chapitres + frames Astuce chat + MCP)
- `assemble_rcms.py` — montage (Ken Burns + médaillon Mika + BGM + loudnorm)
- `assets/rapidocms/` (19 assets), `assets-generes/` (2 heroes RapidoCMS)

## Reproduire
```bash
python3 build_rcms.py && python3 assemble_rcms.py   # -> deliverable/rapidocms-mcp-4min.mp4
```

## Specs
- Charte RapidoCMS bleu `#29ABE2`, accents vert/violet · Poppins · VO Adam FR
- URL MCP lisible ~17 s (≥ 6 s requis) · logos Claude/Mistral/OpenAI ensemble (usage neutre « compatible avec »)

## Bonus — 4 shorts verticaux (plan, sans rendu)
1. **Le MCP** — connectez Claude/Mistral/OpenAI à RapidoCMS (URL + logos)
2. **Posts planifiés** — 10 posts, 3 réseaux, 1/jour (Astuce #3 + calendrier)
3. **Campagnes** — regrouper + analyser (Astuce #4 + stats)
4. **Avant / après** — perso-stressé → perso-heureux (hook + outro)
Réutiliser `videos/stories-foodeatup-30j/build_story.py` (médaillon Mika vertical) en pointant sur les assets RapidoCMS.
