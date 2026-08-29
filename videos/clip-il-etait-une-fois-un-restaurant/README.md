# Clip musical « Il était une fois un restaurant »

Montage vertical sur la chanson Suno du même nom, à partir des **35 plans Higgsfield
existants** de la série `il-etait-une-fois-un-restaurant` (UpEatFood) — aucun plan n'est
regénéré, conformément à la règle du dépôt (`CLAUDE.md`).

```
manifest.json  →  rushes/  →  work/beats.json  →  work/edl.json  →  work/segments/  →  out/
   35 plans       (10 s)       BPM + temps        ordre + coupes      1080×1920         5 fichiers
```

## État : monté

Clip rendu sur la chanson livrée (`chanson.mp3`, 4:30, 90,7 BPM détectés) — voir
[`out/RAPPORT.md`](out/RAPPORT.md) pour l'ordre des plans et les timecodes.

| | |
|---|---|
| Plans montés | 102, tuilant les 270,000 s **à l'image près** |
| Fondus | 5 × 0,3 s, sur les bascules avant ↔ après |
| Exports | 9:16, 1:1, 16:9, teaser 30 s, vignette — tous contrôlés à ffprobe |
| En ligne | https://www.youtube.com/watch?v=Z31TDGNBErs (chaîne FoodEatUp, non répertoriée) |

Les MP4 (355 Mo) ne sont pas versionnés : ils se régénèrent avec

```bash
python3 scripts/run_all.py     # ~15 min sur 4 cœurs
```

après avoir redéposé `chanson.mp3` (le fichier Suno) à la racine du projet. Pour une
autre version de la chanson, rien à changer : les sections sont des poids normalisés sur
la durée réelle du fichier livré.

## Étapes

| Script | Rôle | Sortie |
|---|---|---|
| `00_check_env.py` | ffmpeg, ffprobe, librosa, arborescence | — |
| `01_fetch_rushes.py` | télécharge les 35 plans (idempotent, repli CMS) | `rushes/`, `work/rushes.json` |
| `02_analyze_audio.py` | durée exacte, BPM, grille de temps forts | `work/beats.json` |
| `03_build_edl.py` | l'ordre narratif et l'emplacement des coupes | `work/edl.json` |
| `04_render_segments.py` | découpe, 1080×1920, 30 i/s, étalonnage | `work/segments/` |
| `05_assemble.py` | collage, fondus, chanson, fondu au noir | `out/clip-9x16.mp4` |
| `06_exports.py` | déclinaisons et vignette | `out/clip-1x1.mp4`, `clip-16x9.mp4`, `clip-teaser-30s.mp4`, `vignette.jpg` |
| `07_verify.py` | contrôle ffprobe + rapport | `out/RAPPORT.md` |

Chaque script tourne seul (`python3 scripts/03_build_edl.py`), et `run_all.py --from 03`
reprend en cours de chaîne. Les étapes 01 et 04 sont idempotentes : un rush déjà valide
n'est pas retéléchargé, un plan déjà rendu avec les mêmes paramètres n'est pas refait.

## Le montage

L'ordre narratif est **imposé par le brief**, il ne se déduit pas de la musique ; la
musique décide seulement **où** tombent les coupes.

| Section | Plans | Rythme |
|---|---|---|
| Intro + couplet 1 | `avant-cuisine` **puis** `avant-salle` (EP501→EP509, EP512), EP501 ouvre | 4–6 s, coupes sur les temps faibles |
| Pré-refrains | `avant-bureau` (EP513→EP515) | 3 s |
| Refrains 1 et 2 | `apres-salle` + `apres-bureau` (EP510, EP511, EP516→EP518) | 2 s, coupe sur chaque temps fort |
| Couplet 2 | `avant-client` (EP519→EP521), bascule EP522 sur « quelqu'un a décroché », puis EP523, EP524 | 3–4 s |
| Pont | EP525 seul, ralenti 0,85×, sans coupe | plan long |
| Refrain final | `final` (EP526→EP532), EP533 et EP534 calés sur leurs vers | 1,5 s → 1 s, ça accélère |
| Outro | EP535 jusqu'au bout, puis fondu au noir 1,5 s | plan long |

Réutilisation des plans : jamais deux fois le même consécutivement, et le point d'entrée
dans le rush se décale à chaque réutilisation (`Pool.take`).

### Trois décisions à connaître

1. **Le fondu de 0,3 s tombe sur la bascule avant ↔ après, pas sur chaque changement
   d'acte littéral.** Les refrains alternent salle et bureau tous les deux plans : y
   fondre à chaque fois aurait tué le montage sur les temps forts que le brief demande.
   Le fondu marque donc la bascule que l'étalonnage rend visible (froid → chaud) — 5 à 6
   fondus sur tout le clip. Le plan sortant est rendu 0,3 s plus long, le fondu mange ce
   rab : la timeline musicale ne bouge pas d'une image.
2. **Le pont garde son ralenti 0,85×, et ses trois plans de tête sortent des paroles.**
   Le pont réel dure 28,7 s ; EP525 n'en tient que 11,9 s à 0,85×. Le ralentir à 0,35×
   aurait donné de la bouillie, le combler au hasard aurait cassé le calme du passage.
   Sa tête est donc portée par les plans que les paroles du pont nomment elles-mêmes —
   « vingt heures quinze » (EP530), « vingt heures trente et une, le plat part » (EP531),
   « vingt heures trente-deux, il ne remarque rien » (EP532) — avant EP525 « le même soir,
   quatre fois ». C'est le seul écart au brief, qui supposait un pont plus court.
3. **EP533 et EP534 sont retirés du pool de remplissage du refrain final.** Ils
   n'apparaissent que sur leurs vers (« le Z avant d'éteindre », « sept heures du matin,
   le lendemain ») ; les laisser dans la rotation aurait dilué leur arrivée.

### Calage sur la chanson

Les sections de `song-structure.json` sont des **poids en mesures**, pas des timecodes.
Trois niveaux de calage, du plus fiable au moins fiable :

1. **Les passages calmes**, que la chanson donne sans ambiguïté (`02_analyze_audio.py`
   les mesure sur l'enveloppe RMS lissée) : intro piano seul, pont piano/voix, outro.
   Sur la chanson livrée : intro jusqu'à 19,4 s, pont de 3:03 à 3:31, outro à 4:20.
2. **Les frontières d'arrangement** détectées sur le timbre, l'harmonie et l'énergie
   (`librosa.segment.agglomerative`) : les frontières encore libres y sont attirées, sans
   jamais laisser une section voisine tomber sous 60 % de sa part — sinon deux arêtes
   attirées par le même repère écrasent la section coincée entre elles.
3. **Le prorata des mesures** entre deux points ainsi fixés, puis calage sur le temps fort
   voisin.

Les trois vers repères (`anchors`) sont placés en fraction de leur section. Pour un calage
manuel exact, voir « Si le calage ne tombe pas juste » dans [`SUNO.md`](SUNO.md).

Toutes les frontières sont quantifiées sur la grille d'images (30 i/s) : sans ça, les
arrondis de 107 plans s'additionnent et la fin du montage dérive de la musique.

## Exports (`out/`)

| Fichier | Format | Usage |
|---|---|---|
| `clip-9x16.mp4` | 1080×1920, H.264 CRF 18, AAC 192k | TikTok / Reels / Shorts |
| `clip-1x1.mp4` | 1080×1080, recadrage centré | fil Instagram / Facebook |
| `clip-16x9.mp4` | 1920×1080, plan vertical entier sur fond flouté | YouTube / LinkedIn |
| `clip-teaser-30s.mp4` | 30 s autour du refrain final | teaser |
| `vignette.jpg` | image du plan EP535 | miniature |
| `RAPPORT.md` | ordre des plans, timecodes, contrôles | traçabilité |

### Copies de livraison (`dist/`)

Le master CRF 18 pèse 149 Mo — au-dessus de la limite GitHub de 100 Mo, et au-dessus de ce
que le connecteur YouTube encaisse : un dépôt du fichier 87 Mo est resté bloqué en
« uploading » plus de trente minutes sans message d'erreur, là où la copie 56 Mo est passée
en quelques secondes. D'où deux copies versionnées, qui servent d'URL publique
(`raw.githubusercontent.com`, la même route que les rushes de la série) :

| Fichier | Poids | Usage |
|---|---|---|
| `dist/clip-9x16-livraison.mp4` | 87 Mo, CRF 23 | archive téléchargeable pleine qualité |
| `dist/clip-9x16-web.mp4` | 56 Mo, CRF 26 | ce qui a été déposé sur YouTube |

Les deux restent en 1080×1920. Pour un nouveau dépôt automatisé, viser **≤ 60 Mo**.

Le 16:9 **ne recadre pas** : un recadrage 16:9 dans du 9:16 couperait les visages, le plan
vertical reste donc entier au centre sur un fond flouté tiré de lui-même. Le 1:1, lui, est
un recadrage centré comme demandé au brief ; si un cadrage serré fait passer une tête trop
haut, décaler le `crop` de `06_exports.py` vers le haut (`y=(ih-1080)*0.42`) suffit.

## Rushes

`manifest.json` donne les 35 plans. Source principale : le dépôt de production
(`base + file`). Repli automatique sur la bibliothèque RapidoCMS (`base_cms + cms`, sans
extension mais bien du MP4) pour les 27 plans qui y sont déposés. Les rushes font
720×1280 à 24 i/s, ~10,08 s ; ils sont remontés en 1080×1920 à 30 i/s. Un rush manquant
ou corrompu est signalé et sauté, il ne bloque pas le montage.

Ni `rushes/`, ni `work/`, ni `out/` ne sont versionnés (voir `.gitignore`) : tout se
régénère à partir de `manifest.json` et de la chanson.

## Dépendances

`ffmpeg` / `ffprobe` (obligatoires) et `librosa` + `soundfile` (détection du tempo ;
repli sur `aubio`, puis sur une grille régulière à 92 BPM).

```bash
apt-get install -y ffmpeg
python3 -m pip install librosa soundfile numpy
```
