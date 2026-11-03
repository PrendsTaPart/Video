# Livraison — « FoodEatUp, le tutoriel complet en 5 minutes » (16:9)

## Fichier final
- `deliverable/foodeatup-tutoriel-5min.mp4`
- **1920×1080**, **4:25** (≤ 5:00), H.264 + AAC, ~23 Mo.
- Rendu **local** (pipeline ffmpeg, gratuit) — le render HeyGen MCP (`render_video`, payant) est **désactivé en CLI** et n'a pas été utilisé.

## Contenu
9 chapitres (Intro → 7 phases → Outro), avatar **Mika** en médaillon à l'ouverture de chaque phase,
écrans produit avec **Ken Burns**, illustrations **RapidoCMS**, sous-titres/lower-thirds, BGM + `loudnorm I=-14`.
- Slogan : **« Une infinité de solutions pour gérer votre restaurant »** (intro, bumpers, outro).
- **Chapitre 3 (MCP)** : `https://foodeatup.com/api/mcp` + connecteurs **Claude · Mistral · OpenAI · WhatsApp**.

## Voix off
ElevenLabs Adam FR (`TGAegA0zNRi8I6nUdq3i`, `eleven_multilingual_v2`) — 27 segments réutilisés (`audio/s00…s99.mp3`).

## Reproduire
```bash
python3 build_fe169.py       # frames 1920x1080 -> frames/
python3 assemble_fe169.py    # clips + Ken Burns + avatar + BGM -> deliverable/
# (si le lien MCP change : éditer build_fe169.py puis python3 finalize_s31.py)
```

## Livrables du dossier
- `script/voix-off.md` — script (9 chapitres, timecodes, [MIKA]/[ÉCRAN])
- `storyboard/storyboard.md` — storyboard plan par plan + mapping captures
- `assets-manifest.md` — source · usage · timecode de chaque asset
- `shorts-plan.md` — **bonus** : plan de 7 shorts verticaux (1 par phase), sans rendu
- `assets-generes/` (9 visuels RapidoCMS), `assets/screens/foodeatup/` (20 captures), `assets/logo/`, `assets/avatar/`
- Librairie réutilisable indexée dans `assets/screens/foodeatup/README.md` (racine dépôt)

## Notes
- Substitutions visuelles (pas de capture fidèle) : étape 14 (DLC) → `p6.jpg`, étape 17 (devis) → `ajouter-client.png`. Voir `assets-manifest.md`.
- Assets FoodEatUp conservés et indexés pour réutilisation (mini-stories Insta/TikTok).
