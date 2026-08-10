# Prompt & spécification Claude Code — dépôt `foodeatup-video-factory`

Colle la section « PROMPT À DONNER À CLAUDE CODE » telle quelle. Le reste du
fichier est la spec de référence à déposer dans le dépôt.

---

# PROMPT À DONNER À CLAUDE CODE

> Tu construis et exploites `foodeatup-video-factory`, une usine à vidéos promo
> pour FoodEatUp (TikTok, Instagram Reels, LinkedIn).
>
> **Contraintes non négociables :**
> 1. **Tu n'appelles JAMAIS un outil Higgsfield qui génère du média** —
>    `generate_video`, `generate_image`, `generate_audio`, `reframe`, `upscale_*`,
>    `motion_control`, `shorts_studio_*`, `dubbing`, `virality_predictor`.
>    Les clips hook sont fournis par l'humain dans `assets/hooks/EPxx.mp4`.
>    Si un fichier manque, tu t'arrêtes et tu le signales. Tu ne le remplaces pas
>    par une génération.
> 2. **Tu n'appelles aucun outil HeyGen.** Aucune génération d'avatar.
> 3. **ElevenLabs uniquement pour `text_to_speech`**, et uniquement si le fichier
>    MP3 cible n'existe pas déjà sur le disque. Jamais de regénération d'un
>    fichier existant sans `--force`.
> 4. **Tout le montage se fait en ffmpeg local** : recadrage, incrustation du
>    logo, texte, transitions, mixage. Aucune API payante pour ça.
> 5. **Le logo FoodEatUp apparaît sur 100 % de la durée de chaque vidéo.**
> 6. **Durée** : `tiktok_30` = 30,00 s exactement. `linkedin_45` = 45,00 s.
>    Tolérance ±0,15 s. Tu vérifies avec `ffprobe` avant de publier.
>
> **Sources de vérité :** `config/episodes.json` (fourni) pour la timeline, les
> hooks, les punchlines et les captions. Ne réinvente pas le contenu.
>
> **Pipeline :** fetch assets → génère les VO manquantes → assemble → contrôle
> qualité → upload public → brouillon RapidoCMS → planification.
>
> Commence par lire `SPEC.md`, crée l'arborescence, puis implémente les scripts
> dans l'ordre 01 → 04. Teste sur EP01 uniquement avant de traiter le lot.

---

## Arborescence

```
foodeatup-video-factory/
├── CLAUDE.md                 # garde-fous (copie de la section ci-dessus)
├── SPEC.md                   # ce document
├── config/
│   ├── episodes.json         # fourni
│   ├── voices.json           # rempli au 1er run
│   └── secrets.env           # gitignored
├── assets/
│   ├── hooks/EP01.mp4 … EP30.mp4      # DÉPOSÉS PAR L'HUMAIN
│   ├── brand/
│   │   ├── logo-foodeatup.png         # fond transparent, ≥ 400 px de haut
│   │   ├── sting-logo.mp4             # 5 s, réutilisé, tronqué à 2 s en 30 s
│   │   └── outro.mp4                  # 5 s, CTA
│   ├── demo/                          # captures produit tirées du Drive
│   └── music/bed.mp3                  # libre de droits, une seule piste
├── vo/
│   ├── common/                        # 7 fichiers, générés une fois
│   └── punch/EP01.mp3 … EP30.mp3
├── build/                             # intermédiaires, jetables
├── out/                               # livrables finaux
└── scripts/
    ├── 01_fetch_assets.py
    ├── 02_generate_vo.py
    ├── 03_assemble.py
    ├── 04_publish_rapidocms.py
    └── lib/ff.py
```

---

## Étape 1 — `01_fetch_assets.py`

**Logo** : via le MCP RapidoCMS, `get_brand` puis `list_all_files` pour trouver le
logo officiel FoodEatUp. Télécharge-le dans `assets/brand/logo-foodeatup.png`.
S'il n'a pas de fond transparent, applique `colorkey` en ffmpeg plutôt que de le
regénérer par IA.

**Captures produit** : via le MCP Google Drive, `search_files` avec
`parentId = '<folder_id>'` sur les dossiers listés dans `episodes.json →
drive.demo_clips`, puis `download_file_content` (base64) → `assets/demo/`.

Le bloc D a besoin de **4 sous-plans de ~2,4 s** :
`site_web` → `caisse_pos` → `kds` → `marketing`. Découpe automatiquement le
segment le plus lisible de chaque tuto :

```bash
# extrait 2.4 s à partir d'un point donné, sans réencodage lourd
ffmpeg -ss 00:00:12.0 -i "assets/demo/site_web_raw.mp4" -t 2.4 \
  -vf "scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,fps=30" \
  -c:v libx264 -crf 18 -preset medium -an "build/demo_site.mp4"
```

Les captures d'écran sont en 16:9 : le `crop` central coupe les bords. Préfère un
**zoom sur la zone d'action** (le bouton cliqué, la carte qui se génère) plutôt
qu'un recadrage centré aveugle. Note le point d'entrée retenu dans
`config/demo_cuts.json` pour être reproductible.

**Garde-fou** : si un fichier `assets/hooks/EPxx.mp4` est absent, log
`MISSING_HOOK EPxx` et exclus l'épisode du lot. Ne génère rien.

---

## Étape 2 — `02_generate_vo.py`

1. Lit `config/voices.json`. S'il est vide, appelle la liste des voix ElevenLabs,
   propose 3 voix françaises et demande à l'humain de choisir. N'invente pas d'ID.
2. Pour chaque texte de `02-VOIX-ELEVENLABS.md` : si le MP3 existe déjà → skip.
3. Après génération, `ffprobe` la durée. Si écart > 8 % de la cible, regénère avec
   `speed` +0.05 (max 2 tentatives, plafond 1.15). Au-delà, log un avertissement
   et laisse l'assemblage étirer le plan vidéo.
4. Normalise chaque VO : `ffmpeg -i in.mp3 -af "loudnorm=I=-16:TP=-1.5:LRA=11" out.mp3`

---

## Étape 3 — `03_assemble.py`

### 3.1 Normalisation de tous les segments

Tous les segments passent par le même profil avant concaténation — c'est ce qui
permet d'utiliser le démuxeur `concat` sans artefacts :

```bash
ffmpeg -i "$IN" \
  -vf "scale=${W}:${H}:force_original_aspect_ratio=increase,crop=${W}:${H},fps=30,format=yuv420p" \
  -c:v libx264 -profile:v high -level 4.1 -crf 18 -preset medium \
  -c:a aac -b:a 192k -ar 48000 -ac 2 \
  -video_track_timescale 30000 "build/norm_$NAME.mp4"
```

Un segment sans piste audio reçoit un silence :
`-f lavfi -i anullsrc=r=48000:cl=stereo -shortest`

### 3.2 Coupe des blocs à la durée exacte

Chaque bloc est coupé à la seconde près depuis `episodes.json → formats.*.blocks`.
Le hook (bloc A) est coupé à 7,0 s pour le master 30 s — vérifie que le beat
comique tombe avant. Si `cut_out` est renseigné dans l'épisode, utilise-le.

### 3.3 Incrustation du hook (texte)

En ASS plutôt qu'en `drawtext` : le rendu du contour est meilleur et le texte est
modifiable sans recompilation de filtre.

```
[V4+ Styles]
Style: Hook,Anton,96,&H00FFFFFF,&H00000000,&H00000000,&H80000000,-1,0,0,0,100,100,0,0,1,6,3,5,80,80,700,1
```

- Position : centre, à 700 px du bas → hors des safe zones TikTok.
- Apparition à `hook_text_in_s`, disparition à `hook_text_out_s`, fondu 0,2 s.
- Découpe à 3 mots par ligne, 2 lignes max. Si le hook dépasse 6 mots, réduis la
  taille à 82 plutôt que d'ajouter une 3e ligne.

### 3.4 Logo permanent

```bash
ffmpeg -i "build/concat.mp4" -i "assets/brand/logo-foodeatup.png" \
  -filter_complex "[1:v]scale=-1:90,format=rgba,colorchannelmixer=aa=0.85[lg];[0:v][lg]overlay=W-w-40:60:format=auto" \
  -c:v libx264 -crf 18 -preset medium -c:a copy "build/logo.mp4"
```

Pendant le bloc B (sting), passe le logo à pleine opacité et centré : applique
l'overlay avec une expression `enable='between(t,7,9)'` sur une seconde instance
centrée, et désactive l'instance coin sur le même intervalle.

### 3.5 Mixage audio

Quatre pistes : son diégétique du hook, VO commune, punchline, lit musical.

```bash
ffmpeg -i video.mp4 -i vo_track.wav -i music.mp3 \
  -filter_complex "\
    [2:a]volume=-8dB,aloop=loop=-1:size=2e9,atrim=0:30[bed];\
    [bed][1:a]sidechaincompress=threshold=0.05:ratio=8:attack=20:release=300[ducked];\
    [0:a]volume=0.9[diag];\
    [diag][ducked][1:a]amix=inputs=3:duration=first:dropout_transition=0[mixed];\
    [mixed]loudnorm=I=-14:TP=-1.0:LRA=9[out]" \
  -map 0:v -map "[out]" -c:v copy -c:a aac -b:a 192k "out/EP01_tiktok_30.mp4"
```

Le `sidechaincompress` baisse la musique dès que la voix parle. Sans ça, la VO
est mangée sur les enceintes de téléphone.

### 3.6 Version LinkedIn 1:1

Générée depuis le **même master vertical**, recadrage centre :

```bash
ffmpeg -i "out/EP01_tiktok_30.mp4" \
  -vf "crop=1080:1080:0:420,fps=30" -c:v libx264 -crf 18 -c:a copy \
  "out/EP01_linkedin_45.mp4"
```

Attention : le hook incrusté à 700 px du bas sort du cadre 1:1. Pour LinkedIn,
réassemble depuis les segments avec un style ASS dédié (`MarginV: 180`) plutôt que
de recadrer le master.

---

## Étape 4 — Contrôle qualité automatique

Avant toute publication, `03_assemble.py` vérifie et bloque si un test échoue :

| Test | Commande | Seuil |
|---|---|---|
| Durée | `ffprobe -show_entries format=duration` | 30,00 ± 0,15 s |
| Résolution | `ffprobe -show_streams` | 1080×1920 (ou 1080×1080) |
| Loudness | `ffmpeg -af loudnorm=print_format=json -f null -` | −14 ±1 LUFS, TP ≤ −1 dBTP |
| Logo présent | extraction frame à 1 s, 15 s, 29 s + comparaison de zone | 3/3 |
| Pas de frame noire finale | frame à `durée−0.1 s` | luminance moyenne > 12 |
| Audio non muet | `astats` | RMS > −50 dB |

---

## Étape 5 — `04_publish_rapidocms.py`

### 5.1 Le MP4 doit être accessible par une URL publique

`upload_file_tool` prend un `file_url` public — il ne lit pas le disque local.
Chaîne à respecter :

1. Upload du MP4 sur Google Drive via le MCP Drive (`create_file`), dans un
   dossier dédié `FoodEatUp — Vidéos promo`.
2. Rendre le fichier lisible par lien (`get_file_permissions` pour vérifier ; si
   l'API MCP ne permet pas de modifier la permission, prévoir le dossier
   pré-partagé « tous les utilisateurs disposant du lien »).
3. Construire l'URL de téléchargement direct :
   `https://drive.google.com/uc?export=download&id=<FILE_ID>`
4. `RapidoCMS:upload_file_tool(file_url=<cette URL>, name="EP01_tiktok_30", type="video")`

Si l'URL Drive est refusée par RapidoCMS (redirection d'antivirus sur les gros
fichiers), bascule sur un hébergement statique maîtrisé et documente-le. **Ne
contourne pas en régénérant la vidéo ailleurs.**

### 5.2 Création des brouillons

Récupère les IDs de comptes avec `RapidoCMS:list_connected_accounts`, puis un
brouillon par réseau :

```python
RapidoCMS.create_draft_tool(
    account_id      = accounts["instagram"],
    social_type     = "instagram",
    post_name       = "EP01 — Le chien qui te regarde",
    post_type       = "mediatext",
    media_type      = "video",
    media_source    = "biblio",
    media_url       = public_url,
    media_caption   = caption + "\n\n" + hashtags["instagram"],
)
```

- `tiktok` et `instagram` → master `tiktok_30`
- `linkedin` → `linkedin_45`
- `facebook` → master `tiktok_30`, caption Instagram

### 5.3 Planification

`schedule_draft_tool(draft_id=..., post_date="Y-m-d", post_heure="H-i-s")`.
Attention au format `H-i-s` avec des tirets, pas des deux-points.

Cadence conseillée : 3 publications par semaine et par réseau, décalées de 2 h
entre réseaux pour ne pas poster le même contenu au même instant partout.
Les 30 épisodes couvrent ainsi ~10 semaines.

Pour TikTok, `privacy_level` par défaut est `SELF_ONLY` — passe-le explicitement à
`PUBLIC_TO_EVERYONE` seulement si l'humain l'a validé, et mets `your_brand=true`
(contenu promotionnel de sa propre activité).

---

## Journalisation

Chaque run écrit `build/run_<timestamp>.json` avec, par épisode : fichiers
sources utilisés, durées mesurées, résultat de chaque test QA, IDs de brouillon
RapidoCMS, date planifiée. C'est ce qui permet de rejouer ou d'auditer sans
reconstruire le raisonnement.

## Ce qu'il ne faut pas faire

- Ne pas « améliorer » une vidéo ratée par une génération IA. Signaler et
  s'arrêter.
- Ne pas modifier les hooks ou punchlines de `episodes.json` sans validation.
- Ne pas publier directement : uniquement des **brouillons planifiés**.
- Ne pas empiler les transitions. Coupe franche entre A et B, fondu au blanc
  0,25 s entre D et E, rien d'autre.
