# FoodEatUp — Usine à vidéos promo (30 épisodes)

Kit complet : prompts Higgsfield, scripts voix ElevenLabs, spécification de montage
pour Claude Code, publication RapidoCMS.

---

## Règle absolue : ZÉRO crédit dépensé automatiquement

| Plateforme | Ce qui est autorisé | Ce qui est interdit |
|---|---|---|
| **Higgsfield** | Rien d'automatique. Tu génères toi-même depuis l'UI avec les prompts fournis, puis tu déposes le MP4 dans `assets/hooks/`. Claude Code peut **télécharger** un job déjà payé. | `generate_video`, `generate_image`, `reframe`, `upscale`, `shorts_studio`, `motion_control` — **jamais appelés** |
| **HeyGen** | Rien. Aucune génération vidéo. | Tout `render_video` / `compose` |
| **ElevenLabs** | `text_to_speech` uniquement (voix off) — coût faible, ~1 200 caractères par épisode | Dubbing, voice cloning non demandé |
| **RapidoCMS** | `upload_file_tool`, `create_draft_tool`, `schedule_draft_tool` — gratuits | — |
| **Recadrage 9:16 → 1:1** | `ffmpeg` en local (gratuit) | `Higgsfield:reframe` (payant) |

**Le logo, les incrustations de texte, les transitions et le recadrage se font tous
en ffmpeg local.** C'est gratuit, reproductible et ça évite de repasser par une IA.

---

## Arbitrage de durée

Ton découpage initial totalise 35–45 s, mais tu imposes 30 s max. Deux formats,
mêmes assets :

### Master 30 s — TikTok / Reels / Stories (9:16, 1080×1920)

| Temps | Bloc | Source | Audio |
|---|---|---|---|
| 0.0 → 7.0 | **A — Hook humoristique** (coupe 7 s du clip 10 s) | Higgsfield `assets/hooks/EPxx.mp4` | Son diégétique du clip |
| 7.0 → 9.0 | **B — Sting logo** | `assets/brand/sting-logo.mp4` | Whoosh + VO « FoodEatUp. » |
| 9.0 → 16.5 | **C — Problème** | Motion design / B-roll | VO bloc C |
| 16.5 → 26.0 | **D — Démo produit** | Capture Drive (Module Mon Site) | VO bloc D |
| 26.0 → 30.0 | **E — Closing** | `assets/brand/outro.mp4` | VO bloc E |

### Version longue 45 s — LinkedIn (1:1, 1080×1080)

10 s hook complet · 5 s sting logo · 12 s problème · 13 s démo · 5 s closing.
Générée depuis le même `episodes.json`, variante `linkedin_45`.

---

## Sources d'assets

| Asset | Emplacement | Comment l'obtenir |
|---|---|---|
| 30 clips hook | Higgsfield | Tu génères depuis les prompts du fichier `01` |
| Captures produit | Google Drive `1LpWivm0KEPwX5XhNHiw08426NjT6PXHC` | API Drive — voir mapping ci-dessous |
| Logo FoodEatUp | RapidoCMS (bibliothèque de marque) | `get_brand` + `list_all_files` |
| Voix off | ElevenLabs | `text_to_speech`, fichier `02` |
| Sting logo + outro | À produire une fois | Motion design maison, réutilisé sur les 30 |

### Mapping Drive — captures produit (bloc D)

Le dossier racine contient 14 modules. Pour le bloc D « site web + caisse + KDS +
marketing », les dossiers utiles :

| Bloc démo | Dossier Drive | ID |
|---|---|---|
| Site web IA | `6 - Module Mon Site / 5 - CRÉER UN SITE PAR IA` | `1WZsVdrBvcL2OQiYcRdnBCgzUx6u9J6p9` |
| Caisse POS | `11 - Module Caisse POS & Matériel` | `1nHjH82ig0i-MtQqDmYp131htOSThaPIQ` |
| KDS | `9 - Module KDS` | `1wQAkcP9pY90DLu_sE8GLiI6WYHZuYwq9` |
| Marketing / Iris | `7 - Module Marketing` | `1hBc6Axd0DE2ocTiXXKGlmj1dyagOwKFg` |
| Livraison / HubRise | `12 - Module HubRise & Livraisons` | `19D09dNt_jZSKpcwVCU8Mn1OkMLkY_ojd` |

Structure type d'un dossier feuille : `<Nom du tuto>.mp4` + une vignette `.jpg` +
`page fin vid..jpg`. Exemple vérifié : `Créer son site avec l'IA.mp4`
(ID `1MEMdJJMq2MhQ6H-dU5Nb5ls8ifoqM3U4`, 9,8 Mo).

---

## Charte vidéo (à respecter partout)

- **Logo** : filigrane permanent, coin haut-droit, marge 40 px, hauteur 90 px,
  opacité 85 %. Passe à 100 % et centré pendant le bloc B.
- **Safe zones TikTok/Reels** : rien d'important sous 320 px du bas ni au-dessus
  de 200 px du haut (UI plateforme).
- **Typo hooks** : sans-serif condensée grasse, blanc, contour noir 6 px, ombre
  portée. Hook en 3 mots max par ligne, 2 lignes max.
- **Audio** : master à −14 LUFS, peak −1 dBTP. Musique à −22 LUFS avec ducking
  −8 dB sous la voix.
- **Aucun texte généré par Higgsfield** — les prompts l'interdisent explicitement.
  Tout le texte est incrusté en ffmpeg pour rester lisible et corrigeable.

---

## Ordre d'exécution

1. Tu génères les 30 hooks sur Higgsfield (fichier `01`) → dépose dans `assets/hooks/`
2. Claude Code : `python scripts/01_fetch_assets.py` (Drive + logo RapidoCMS)
3. Claude Code : `python scripts/02_generate_vo.py` (ElevenLabs)
4. Claude Code : `python scripts/03_assemble.py --episode EP01 --format tiktok_30`
5. Claude Code : `python scripts/04_publish_rapidocms.py --episode EP01`

Spécification complète pour Claude Code : fichier `03-CLAUDE-CODE-MONTAGE.md`.
