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
- ✅ QA 7 tests, bloquante — **56 masters, 56 publiables**
- ✅ voix off **Olivier** (`rgFgMEXfdGwXCYio7I0J`) : blocs communs, 28 punchlines
  et **28 pitchs de démo**, un par épisode, tous normalisés
- ✅ **28 épisodes sur 30** montés en TikTok 30 s ET LinkedIn 1:1 45 s
- ✅ 28 plans de publication prêts dans `build/publish_plan_EPxx.json`
- ⏳ **EP24** (la mouette braqueuse) et **EP28** (le tapis à sushis fou) :
  séquences Higgsfield à générer
- ⏳ publication : rien n'est envoyé, TikTok reste en `SELF_ONLY`

### Une démo par épisode

Chaque épisode a **sa** capture logiciel et **son** pitch de voix off, écrits
dans `episodes.json` (`demo_capture`, `demo_vo`). Le bloc D montre 4 moments du
même tutoriel. 30 captures distinctes : aucun épisode ne partage sa démo.

### Cadence de publication

3 posts par semaine et par réseau (lundi / mercredi / vendredi), 2 h d'écart
entre réseaux. Départ au 17/08/2026, EP30 tombe le 23/10 — soit ~10 semaines.
