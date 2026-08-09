# foodeatup-video-factory

Usine à vidéos promo FoodEatUp : 30 épisodes, deux formats, montage 100 % local.

- **`tiktok_30`** — 1080×1920, 30,00 s → TikTok, Instagram, Facebook
- **`linkedin_45`** — 1080×1080, 45,00 s → LinkedIn

Lire **`CLAUDE.md`** (garde-fous) puis **`SPEC.md`** (spécification de montage).

---

## Pipeline

```bash
python scripts/00_build_brand_clips.py                       # sting / problème / outro
python scripts/01_fetch_assets.py --format tiktok_30         # inventaire + sous-plans démo
python scripts/02_generate_vo.py                             # voix off ElevenLabs
python scripts/03_assemble.py --episode EP01 --format tiktok_30
python scripts/04_publish_rapidocms.py --episode EP01        # plan de brouillons planifiés
```

Aucune dépendance Python hors stdlib. Il faut `ffmpeg` / `ffprobe` sur le PATH.

### Ce que les scripts font — et ne font pas

Google Drive, RapidoCMS et (sans clé API) ElevenLabs sont exposés en **MCP**,
donc côté agent. Les scripts ne passent pas ces appels : ils écrivent le travail
à faire dans `build/`, avec les identifiants et arguments exacts.

| Fichier produit | À qui il s'adresse |
|---|---|
| `build/assets_report.json` | ce qui manque, avec le code (`MISSING_HOOK`, `NEED_MCP_DRIVE`, …) |
| `build/vo_jobs.json` | les `text_to_speech` restant à passer |
| `build/publish_plan_<EP>.json` | la suite d'appels RapidoCMS / Drive, dans l'ordre |
| `build/run_<horodatage>_<EP>_<format>.json` | journal d'un assemblage : sources, durées, QA, verdict |

Avec `ELEVENLABS_API_KEY` (dans l'environnement ou `config/secrets.env`),
l'étape 02 se fait toute seule en HTTP.

---

## Arborescence

```
config/
  episodes.json      source de vérité : timeline, hooks, punchlines, captions
  voices.json        voix ElevenLabs retenue (voice_id JAMAIS inventé)
  demo_cuts.json     points d'entrée des sous-plans démo — figés, éditables
assets/
  hooks/EPxx.mp4     DÉPOSÉS PAR L'HUMAIN depuis Higgsfield
  brand/             logos + clips de marque (générés par le script 00)
  demo/*_raw.mp4     tutos produit bruts (Drive)
  music/bed.mp3      lit musical
  fonts/             Anton (typo des hooks)
vo/common vo/punch   voix off
build/               intermédiaires jetables + journaux
out/                 masters livrables
```

## Assets de marque

Les trois logos officiels sont versionnés dans `assets/brand/` :

| Fichier | Usage |
|---|---|
| `logo-foodeatup.png` | pastille bleue, texte blanc — **filigrane permanent** (le fond plein reste lisible sur n'importe quel plan) |
| `logo-foodeatup-mascot.png` | logo horizontal à mascotte, fond transparent |
| `mark-eight.png` | pictogramme seul — animé dans le sting |

`00_build_brand_clips.py` fabrique **en ffmpeg** trois masters réutilisés par les
30 épisodes, à partir de ces PNG. Aucune génération IA :

| Clip | Durée | Contenu |
|---|---|---|
| `sting-logo.mp4` | 5,0 s | pictogramme qui rebondit, puis le logo |
| `probleme.mp4` | 12,0 s | « DIX LOGICIELS » · 10 tuiles isolées · « 1 000 € PAR MOIS » · « ET AUCUN NE SE PARLE » |
| `outro.mp4` | 5,0 s | logo + « Avant, pendant, après le service. » + CTA |

Ils sont composés dans le **carré central 1080×1080** (y ∈ [420, 1500]) pour que
le recadrage 1:1 LinkedIn ne coupe rien, et leurs beats sont calés pour rester
lisibles une fois tronqués à la durée du master 30 s.

## État

- ✅ scripts 00 → 04, testés de bout en bout
- ✅ QA 7 tests, bloquante
- ✅ voix off : **Olivier** (`rgFgMEXfdGwXCYio7I0J`, voix française native déjà
  utilisée dans `hero-video/`) — 7 blocs communs + punchlines, normalisés
- ⏳ hooks : **8/30** récupérés depuis Higgsfield
  (EP01, EP02, EP03, EP04, EP06, EP09, EP10, EP11 ; une 2ᵉ prise d'EP04 est
  rangée dans `assets/hooks/alt/`)
- ⏳ bloc D : les sous-plans `kds` et `marketing` sont des **substituts** pris
  dans les captures du dépôt — les vrais tutos sont sur le Drive, IDs notés dans
  `config/demo_cuts.json`

### Mapping hook ↔ épisode

Établi à partir des prompts Higgsfield eux-mêmes, pas d'une hypothèse sur
l'image : `9b79bede` (scooter + dos d'âne) est EP11, tandis que `b5d50c1e`
(skateboard) est EP02 — les deux montrent un livreur qui tombe.
