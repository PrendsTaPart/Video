# Clip musical « Il était une fois un restaurant »

Montage vertical sur la chanson Suno du même nom, à partir des **35 plans Higgsfield
existants** de la série `il-etait-une-fois-un-restaurant` (UpEatFood) — aucun plan n'est
regénéré, conformément à la règle du dépôt (`CLAUDE.md`).

```
manifest.json  →  rushes/  →  work/beats.json  →  work/edl.json  →  work/segments/  →  out/
   35 plans       (10 s)       BPM + temps        ordre + coupes      1080×1920         5 fichiers
```

## Ce qui manque pour rendre le clip

**La chanson.** Générer le morceau sur Suno avec le prompt et les paroles de
[`SUNO.md`](SUNO.md), déposer le fichier ici sous le nom `chanson.mp4` (ou `chanson.mp3`),
puis :

```bash
python3 scripts/run_all.py
```

Tout le reste est prêt : les 35 rushes se téléchargent tout seuls, le montage se
construit sur la grille de temps détectée dans le fichier livré, quelle que soit sa durée.

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
2. **Le pont fait 4 mesures, pas 8.** EP525 dure 10,08 s ; à 0,85× il couvre 11,9 s. Un
   pont de 8 mesures (≈ 21 s) aurait imposé un 0,48×, c'est-à-dire de la bouillie. Le
   brief dit « ralenti 0,85× », donc c'est la section qui cède.
3. **EP533 et EP534 sont retirés du pool de remplissage du refrain final.** Ils
   n'apparaissent que sur leurs vers (« le Z avant d'éteindre », « sept heures du matin,
   le lendemain ») ; les laisser dans la rotation aurait dilué leur arrivée.

### Calage sur la chanson

Les sections de `song-structure.json` sont des **poids en mesures**, pas des timecodes :
normalisés sur la durée réelle du fichier livré, puis chaque frontière est ramenée sur le
temps fort le plus proche. Les trois vers repères (`anchors`) sont placés en fraction de
leur section. Pour un calage manuel exact, voir « Si le calage ne tombe pas juste » dans
[`SUNO.md`](SUNO.md).

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

Le 16:9 **ne recadre pas** : un recadrage 16:9 dans du 9:16 couperait les visages, le plan
vertical reste donc entier au centre sur un fond flouté tiré de lui-même.

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
