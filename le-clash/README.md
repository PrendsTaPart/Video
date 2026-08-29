# LE CLASH — clip musical 9:16

*Deux cuisines, une rue.* Clip du morceau **« LE CLASH »** — drill FR × R&B, **144 BPM**, la mineur.
Le montage suit **les paroles**, pas une chronologie de série : aucun numéro d'épisode, aucun titre
de saison, aucune mention de série à l'écran.

## Livrables (`dist/`)

| Fichier | Format | Contenu |
|---|---|---|
| `clash-master-9x16.mp4` | 1080×1920, 30 fps | le clip complet, 3 min 22,9 |
| `clash-tiktok-15s.mp4` | 1080×1920, 30 fps | 15,9 s — amorce EP083 + EP142 puis le refrain 1 |
| `clash-paysage-16x9.mp4` | 1280×720, 30 fps | recadrage large, split-screen en gauche/droite |
| `clash-proxy-9x16.mp4` | 540×960 | proxy de validation du rythme |
| `affiche-le-clash.jpg` | 1080×1620 | l'affiche du film |
| `shotlist.json` | — | la timeline effective, plan par plan |

## Comment c'est monté

### 1. La grille
Tempo mesuré sur la piste par autocorrélation puis peigne d'onsets : **144,00 BPM exactement**
(et non 142 comme demandé à Suno), phase 0,404 s, mesure de 1,667 s. Aucune dérive sur les
202,92 s — vérifié par tranches de 20 s. **Toute coupe tombe sur un temps ou un contretemps.**

### 2. L'alignement sur les paroles
Transcription mot à mot (faster-whisper `medium`, français), puis **alignement Needleman-Wunsch**
du texte officiel de `lyrics.txt` sur la transcription — l'argot fait échouer Whisper, les paroles
font foi. 56 lignes sur 58 alignées mot pour mot ; les deux lignes parlées de l'outro ont été
recalées sur une passe de transcription isolée.

Frontières de sections obtenues :

| Section | Début | Fin |
|---|---|---|
| intro (instrumentale) | 0,00 | 12,49 |
| couplet 1 | 12,49 | 66,24 |
| refrain 1 | 66,24 | 86,24 |
| couplet 2 | 86,24 | 126,64 |
| pont | 126,64 | 153,15 |
| couplet 3 | 153,15 | 173,32 |
| refrain final | 173,32 | 189,74 |
| outro | 189,74 | 202,92 |

### 3. Les plans — 87 sources, 221 coupes, aucun visuel deux fois
- **44 plans** du catalogue Social FoodEatUp, URL obtenues plan par plan via
  `obtenir_sources_montage` (jamais devinées : deux conventions coexistent, bucket S3 RapidoCMS
  et GitHub raw video-factory).
- **43 plans** de la bibliothèque Higgsfield déjà générée dans ce dépôt
  (`instagram-stories/assets/video/hf2/`, `hero-video/assets/video/`) — aucune génération nouvelle,
  conformément à la règle du dépôt.

Chaque source est découpée en fenêtres qui ne se recouvrent pas, et **chaque fenêtre n'est
consommée qu'une seule fois** : le compteur de réemploi est à zéro. L'attribution tourne en
round-robin, donc deux coupes consécutives ne viennent jamais de la même source.

### 4. Les deux grammaires
| | côté qui subit | côté qui tient |
|---|---|---|
| étalonnage | `saturation=0,72 contrast=1,15`, virage froid, vignette | `saturation=1,12 contrast=1,02`, virage chaud |
| caméra | micro-tremblement 2 px | parfaitement stable |
| coupes | 0,42 à 0,63 s, parfois sur le contretemps | 1,25 à 1,67 s, sur les temps forts |
| transition | coupe sèche | fondu d'entrée de 4 images |
| sous-titres | légèrement tremblants | stables |

### 5. Les moments écrits
- **Couplet 1** — un plan par punchline, EP015 (la tour d'assiettes) joué **en entier** sur les
  10 dernières secondes : l'écroulement finit pile sur le premier temps du refrain.
- **Refrain 1** — split-screen horizontal, trait crème 4 px, les deux moitiés désynchronisées
  (haut en coupes courtes, bas en coupes longues). Sur « y'en a un qui court derrière » la moitié
  haute **fige en noir et blanc** ; sur « y'en a un qui a d'l'avance » la moitié basse **s'ouvre en
  plein cadre**.
- **Couplet 2** — EP141 est le plan le plus long du clip (2,08 s).
- **Pont** — EP142 **sans coupe**, calé pour que le dégainé des spatules tombe sur « Ils ont sorti
  les spatules » (gel 0,6 s + flash blanc 2 images) et le dressage sur « la même assiette ».
  **Aucun sous-titre, aucune incrustation, pas même le logo**, sur tout le pont.
- **Couplet 3** — le split se referme et disparaît sur « c'est toi contre ton lundi ».
- **Refrain final** — alternance des deux grammaires à chaque temps.
- **Outro** — image figée sur les deux assiettes dressées, puis **animation du logo FoodEatUp**
  (« UN FILM PRODUIT PAR » → la marque → le logotype → FOODEATUP.COM).

### 6. Le son
Piste Suno + nappe d'ambiance d'origine des plans « subit » à **−22 dB** (imprimante, cris,
vaisselle), audio coupé net sur les plans « tient », ambiance du pont remontée à **−8 dB**.
Master normalisé : **−14,00 LUFS, TP −1,65 dBTP**.

## Contrôles passés

- master : 1080×1920, 30 fps CFR, **6 088 images exactement**, 202,93 s, 33,3 Mo
- tiktok : 1080×1920, 478 images, 15,93 s, 3,0 Mo
- paysage : 1280×720, 6 088 images, 202,93 s, 21,4 Mo
- audio : −14,00 LUFS / TP −1,65 dBTP
- grille : 0 coupe hors temps ou contretemps
- sources : 0 réemploi de fenêtre visuelle

## Écarts assumés par rapport au brief

1. **Le tempo est 144, pas 142.** La grille est celle de la piste réelle.
2. **L'intro parlée n'existe pas dans ce rendu Suno** — aucune voix détectée avant 12,5 s. Le
   carton « 20:15 » et l'amorce EP083 + EP142 sont conservés, sans les répliques.
3. **Pas de coupure musicale sur le pont** : la piste est un mixage stéréo, isoler la note tenue
   demanderait une séparation de stems. Le gel et le flash sont conservés.
4. **Fondu d'entrée de 4 images** côté « tient » plutôt qu'un fondu enchaîné : un enchaîné
   décalerait les coupes hors de la grille, ce que le brief interdit par ailleurs.
5. **CRF 28** au lieu de 18, à la demande (« compresse au maximum ») : 33 Mo pour 3 min 23.
   Repasser en qualité master = `OUT_CRF=18`.
6. **Rendu par tranches** (7 pour le master) : ouvrir les 223 entrées d'un coup en 1080p fait
   tomber ffmpeg sur un OOM. Chaque tranche a son propre `filter_complex`, les tranches sont
   ensuite concaténées **sans réencodage** et l'audio est muxé en une passe — donc toujours
   un seul encodage vidéo par livrable.

## Reproduire

```bash
python3 scripts/tempo.py        # tempo réel
python3 scripts/grid.py         # grille et downbeats
python3 scripts/transcribe.py   # transcription mot à mot
python3 scripts/align.py        # alignement des paroles
python3 scripts/build.py        # → shotlist.json
python3 scripts/subs.py         # → sous-titres karaoké
python3 scripts/ambience.py     # → nappe d'ambiance + master audio
python3 scripts/brand.py        # → affiche + sting logo
python3 scripts/derivees.py     # → shotlist tiktok + sous-titres dérivés
OUT_FILE=dist/clash-master-9x16.mp4 CHUNKS=7 TAG=m python3 scripts/render_chunks.py
```

`sources/`, `sources-local/` et `work/` ne sont pas versionnés : ils se régénèrent.
