# La Brigade augmentée — de la BD au film vertical

La bande dessinée « La Brigade augmentée » (88 pages, Figma) transformée en film vertical TikTok,
en 6 épisodes et en déclinaisons réseaux. Travail par étapes, sur la branche `feat/bd-video`.

| Étape | État | Livrables |
|---|---|---|
| 0 · Audit du dépôt | ✅ | [`AUDIT.md`](AUDIT.md), [`assets/catalog.json`](assets/catalog.json) |
| 1 · Extraction Figma | ✅ | [`storyboard.json`](storyboard.json), `panels/`, `pages/`, `cast/`, `assets/logos/`, [`figma/extraction.json`](figma/extraction.json) |
| 2 · Script, voix, musique | ✅ (musique partie 3 manquante, voir BUDGET) | [`script.md`](script.md), [`voices.json`](voices.json), `audio/vo/` (236 répliques), `audio/music/`, `audio/sfx/` |
| 3A · Motion design | ✅ | Ken Burns, bulles animées, cartouches, transitions de BD : `montage/*/index.html` |
| 3B · Plans hero IA | ⏸ plan test en attente de validation | [`veo3_prompts.md`](veo3_prompts.md) (21 prompts) |
| 4 · Montage et rendu | ✅ | `montage/<film\|epNN>/`, `renders/film/`, `renders/episodes/` |
| 5 · Déclinaisons | ✅ | [`declinaisons.md`](declinaisons.md), `renders/tiktok/`, `instagram/`, `facebook/`, `linkedin/`, `bonus/` |
| 6 · RapidoCMS | ⏸ campagne créée, brouillons en attente (comptes et hébergement à confirmer) | [`calendrier.csv`](calendrier.csv) |

Coûts réels, poste par poste : [`BUDGET.md`](BUDGET.md) (étape 2 : 4,20 $ ; tout le reste a tourné en local, 0 $).

## Ce qui a été produit

- **Film complet** 9:16, 1080×1920, 30 fps, ~23 min : les 88 pages dans l'ordre, carton « À suivre… » entre les parties.
- **6 épisodes** (Prologue + Partie 1, Partie 2 … Partie 6 + Épilogue), 3 à 4 min chacun : accroche de 2 s, carton,
  plans du storyboard avec voix, bulles, musique et bruitages, fin « Une seule saisie, pas dix · Testez FoodEatUp ».
- **Déclinaisons** coupées dans les épisodes : stories 15 s, reels 60–90 s, stories « personnage du jour » et « citation »,
  LinkedIn 60–120 s en 9:16 et 4:5, séries bonus « personnages » (10 s × 14) et « une case, une fonction » (15 s × 16).
  Liste complète : [`declinaisons.md`](declinaisons.md).
- **Son** : 16 voix ElevenLabs existantes (aucune voix clonée), une prise par réplique ; musique baissée sous la voix
  (sidechain) ; niveau final −14 LUFS.

Règles tenues : aucun logo inventé (logos réels de Figma uniquement), aucun chiffre hors BD, aucune clé dans le dépôt,
rien de publié ni de programmé.

## Où sont les vidéos

Les 79 vidéos finales sont dans le dépôt, en **Git LFS** (`bd-video/renders/`). Le dépôt est public : chaque fichier a un
lien de téléchargement direct, utilisable aussi par RapidoCMS (`upload_file_tool`).

- Dossier sur GitHub : https://github.com/PrendsTaPart/Video/tree/feat/bd-video/bd-video/renders
- Film complet : https://media.githubusercontent.com/media/PrendsTaPart/Video/feat/bd-video/bd-video/renders/film/film.mp4
- Épisodes : https://media.githubusercontent.com/media/PrendsTaPart/Video/feat/bd-video/bd-video/renders/episodes/ep01.mp4 … `ep06.mp4`
- Déclinaisons : même préfixe `https://media.githubusercontent.com/media/PrendsTaPart/Video/feat/bd-video/bd-video/renders/` + le chemin indiqué dans [`declinaisons.md`](declinaisons.md)

Les rendus muets intermédiaires (`*-video.mp4`) et les aperçus (`previews/`) restent hors Git.

## Relancer

```bash
# Étape 0 — inventaire des médias du dépôt
pip install webrtcvad-wheels && python3 bd-video/scripts/audit_media.py

# Étape 1 — Figma (URLs temporaires de download_assets sur l'entrée standard : « page NN <url> » / « raw <url> »)
bd-video/scripts/fetch_figma_assets.sh < urls.txt
python3 bd-video/scripts/build_panels.py
python3 bd-video/scripts/build_storyboard.py

# Étape 2 — script et voix
python3 bd-video/scripts/build_script.py        # script.md, voices.json, audio/vo_manifest.json
python3 bd-video/scripts/vo_batches.py plan      # 59 lots ElevenLabs (partie × voix)
#   … génération ElevenLabs (vo_sessions.json garde les sessions), lots bruts dans audio/vo_raw/
pip install faster-whisper
python3 bd-video/scripts/vo_batches.py split     # une réplique par fichier, alignement Whisper

# Étape 4 — montage et rendu (HyperFrames local, Chrome headless)
python3 bd-video/scripts/build_montage.py all    # montage/<nom>/index.html + timeline.json
export HYPERFRAMES_BROWSER_PATH=$(ls -d /opt/pw-browsers/chromium_headless_shell-*/*/headless_shell | head -1)
bash bd-video/scripts/render_all.sh ep01 ep02 ep03 ep04 ep05 ep06 film   # rendu + mixage −14 LUFS + aperçu 720p

# Étape 5 — déclinaisons
python3 bd-video/scripts/declinaisons.py all
python3 bd-video/scripts/declinaisons.py bonus
python3 bd-video/scripts/declinaisons.py inventaire   # réécrit declinaisons.md

# Étape 6 — calendrier proposé (rien n'est programmé)
python3 bd-video/scripts/calendrier.py
```

`mix_audio.py` peut se relancer seul sur un rendu muet : `python3 bd-video/scripts/mix_audio.py ep03 renders/episodes/ep03-video.mp4 renders/episodes/ep03.mp4`
(par exemple après avoir ajouté `audio/music/partie3-energie.mp3`).

## Contenu du dossier

| Chemin | Contenu |
|---|---|
| `storyboard.json` | 290 plans dans l'ordre de lecture : page, case, partie, image, type (`recit` / `bulle` / `titre`), personnage, voix, texte, pastille, `hero` |
| `panels/`, `pages/`, `cast/` | Dessins d'origine sans texte (152), pages entières (88), portraits et pastilles |
| `assets/logos/`, `assets/fonts/` | Logos réels repris de la BD ; Bangers et Comic Neue en local |
| `audio/vo/`, `audio/vo_raw/` | Répliques découpées (236) et lots bruts ElevenLabs avec leur transcription Whisper |
| `montage/<nom>/` | Compositions HyperFrames (`index.html`) et `timeline.json` (départ de chaque plan) |
| `scripts/` | Tous les outils ci-dessus |

Fichier source : https://www.figma.com/design/izfLEauBeeBnTcTt9tOAMm (page « Guide A4 — Formation caisse »).
