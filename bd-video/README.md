# La Brigade augmentée — de la BD au film vertical

La bande dessinée « La Brigade augmentée » (88 pages, Figma) transformée en film vertical TikTok,
en épisodes et en déclinaisons réseaux. Travail par étapes, sur la branche `feat/bd-video`.

| Étape | État | Livrables |
|---|---|---|
| 0 · Audit du dépôt | ✅ | [`AUDIT.md`](AUDIT.md), [`assets/catalog.json`](assets/catalog.json) |
| 1 · Extraction Figma | ✅ | [`storyboard.json`](storyboard.json), `panels/`, `pages/`, `cast/`, `assets/logos/`, [`figma/extraction.json`](figma/extraction.json) |
| 2 · Script et voix | ⏳ | `script.md`, `voices.json`, `audio/` |
| 3 · Animation | — | `veo3_prompts.md` |
| 4 · Montage | — | `renders/` |
| 5 · Déclinaisons | — | `declinaisons.md` |
| 6 · Brouillons RapidoCMS | — | `calendrier.csv` |

Coûts : [`BUDGET.md`](BUDGET.md).

## Ce que contient le dossier

| Chemin | Contenu |
|---|---|
| `storyboard.json` | 290 plans dans l'ordre de lecture : page, case, partie, épisode, image, type (`recit` / `bulle` / `titre`), personnage, voix, texte, pastille, `hero`, durée estimée |
| `panels/pXX-cN.{jpg,png}` | Dessins d'origine sans texte (152), tels qu'importés dans Figma : 880×1320 (portrait) pour les parties 1–2, 1376×768 (paysage) pour les parties 3–6. `panels/index.json` relie chaque fichier à son nœud Figma |
| `pages/pXX.png` | Les 88 pages entières (794×1123), pour les plans « feuilletage » |
| `cast/<id>.png` | Portraits ronds des 12 personnages à visage (416 px), plus les pastilles à initiale des rôles secondaires ; `cast/source/` garde les portraits d'origine non recadrés |
| `assets/logos/` | Logos réels repris de la BD (FoodEatUp, Claude, OpenAI, Mistral, Plani't) : à utiliser tels quels |
| `figma/extraction.json` | Texte brut extrait de Figma (récitatifs, bulles, pastilles, titres, cartes) avec les nœuds et les imageHash |

Images et audio sont suivis par **Git LFS** (`.gitattributes` à la racine).

## Relancer

```bash
# Étape 0 — inventaire des médias du dépôt
pip install webrtcvad-wheels && python3 bd-video/scripts/audit_media.py

# Étape 1 — après avoir récupéré les URLs temporaires des outils Figma (download_assets) :
#   lignes « page NN <url> » et « raw <url> » sur l'entrée standard
bd-video/scripts/fetch_figma_assets.sh < urls.txt
python3 bd-video/scripts/build_panels.py      # range figma/cache → panels/
python3 bd-video/scripts/build_storyboard.py  # extraction.json → storyboard.json
```

Le texte vient de `use_figma` en lecture seule, avec [`scripts/figma_extract.js`](scripts/figma_extract.js) ; le résultat est
`figma/extraction.json`. L'imageHash Figma est le SHA-1 du fichier d'origine : c'est ce qui relie
chaque image téléchargée à sa case.

Fichier source : https://www.figma.com/design/izfLEauBeeBnTcTt9tOAMm (page « Guide A4 — Formation caisse »).
