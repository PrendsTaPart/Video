# Boîte de réception — clips HeyGen à identifier

Clips reçus de Michael, en attente d'attribution à un script de
`../SCRIPTS-HEYGEN-30.md`. Une fois identifiés, ils partent dans
`../vNN-<slug>/assets/heygen/resultat.mp4`.

## Lot du 2026-08-09 (4 clips uniques)

Nommés par **ordre de génération** (le nombre dans le nom de fichier HeyGen est un
timestamp epoch en millisecondes — c'est le seul indice d'ordre disponible).

| Fichier | Durée | Généré à | Apparence avatar |
|---|---|---|---|
| `gen-1_1786317231351.mp4` | 10,22 s | 23:13:51 | fond clair + tablier FoodEatUp |
| `gen-2_1786317254794.mp4` | 12,14 s | 23:14:14 | ⚠️ fond gris-vert + veste à boutons, **sans tablier** |
| `gen-3_1786317280068.mp4` | 9,24 s | 23:14:40 | fond clair + tablier FoodEatUp |
| `gen-4_1786317311124.mp4` | 9,24 s | 23:15:11 | fond clair + tablier FoodEatUp |

Un cinquième fichier avait été déposé mais c'était `gen-4` en double (md5 identique) —
non conservé.

## Contrôle qualité : ✅ tous conformes

Vérifié image par image (`qa-contact-sheet.jpg`, 3 instants par clip) : **avatar seul,
plan unique, aucun template, aucun sous-titre ni logo incrusté**, l'avatar parle du début
à la fin. C'est bien le mode d'export demandé — l'erreur des deux premières tentatives de
la vidéo 1 ne s'est pas reproduite.

## ⚠️ Deux points à trancher avant montage

**1. Quel script correspond à quel clip ?**
Pas identifiable automatiquement : les clips n'ont aucune métadonnée de titre, et la
transcription locale est impossible ici (les modèles Whisper sont hébergés sur
huggingface.co, bloqué par la politique réseau de cette session — vérifié, 403 au CONNECT).
Attribuer au hasard produirait des vidéos où l'avatar parle d'autre chose que le logiciel
affiché, donc l'attribution doit être confirmée par Michael.

**2. `gen-2` n'a pas la même apparence que les autres.**
Fond gris-vert et veste à boutons sans tablier FoodEatUp, là où les trois autres — et le
clip déjà monté dans `../v01-fidelite/assets/heygen/resultat.mp4` — ont un fond clair et
le tablier siglé. Sur une série publiée à un rythme régulier, cette rupture se remarquera.
À refaire dans la même apparence que les autres, sauf si c'est voulu.

## Lot du 2026-08-10 (2 clips uniques sur 3 déposés)

| Fichier | Durée | Attribution |
|---|---|---|
| `gen-5_1786325920661.mp4` | 9,35 s | script **05** — Brancher son MCP sur Claude |
| `gen-6_1786325937242.mp4` | 9,47 s | script **06** — Ajouter ses employés |

Le troisième fichier déposé (`1c9ae6e9-…958033`) était **byte-identique à `gen-3`**
(md5 `b9b097ff…`) : c'est le clip 03 re-téléchargé, pas une nouvelle génération. Supprimé.

Comme il a été déposé en dernier alors que les deux précédents suivaient l'ordre 05 puis 06,
il occupait la place du **script 07 (Établir un contrat et son salaire)** — celui-là reste
donc à générer.

## Normalisation audio

Les clips HeyGen sortent à ~−17 dB de moyenne, les voix off ElevenLabs à ~−30 dB. Toutes les
voix sont donc passées au `loudnorm I=-16:TP=-1.5:LRA=11` avant montage
(`../motion/assets/audio/norm/vo-avatar-genN.mp3`). Sans ça, le spectateur doit monter le son
au début de la vidéo puis le baisser à l'arrivée de l'avatar.
