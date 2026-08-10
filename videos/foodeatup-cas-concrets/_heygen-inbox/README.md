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

## Lot du 2026-08-10 (2e) — 4 clips uniques sur 5 déposés

Le premier fichier déposé (`443910d1-…854954`) était **byte-identique à `gen-5`**
(md5 `61059782…`) : le clip 05 re-téléchargé. Deuxième doublon en deux lots.

| Fichier | Durée | Attribution |
|---|---|---|
| `gen-7_1786326858026.mp4` | 9,83 s | ❓ à confirmer |
| `gen-8_1786326862531.mp4` | 9,54 s | ❓ à confirmer |
| `gen-9_1786326864985.mp4` | 8,34 s | **08 — Imprimer son planning par poste** (voir analyse) |
| `gen-10_1786326872362.mp4` | 9,64 s | ❓ à confirmer |

Contrôle qualité : les 4 sont conformes — avatar seul, plan unique, fond clair + tablier
FoodEatUp, aucun template ni incrustation.

## Analyse de la voix — ce qu'elle permet et ne permet pas

Demandé par Michael avant montage. La transcription automatique est impossible ici (modèles
Whisper sur `huggingface.co`, Vosk sur `alphacephei.com` : les deux bloqués par la politique
réseau — testé). L'analyse s'est donc faite sur deux mesures acoustiques, calibrées sur les
6 clips dont le script est connu.

**1. Structure des pauses — inexploitable.** L'idée était de compter les fins de phrase.
Mesuré au seuil −30 dB / 0,22 s sur les 6 clips connus :

| Clip | Script | Phrases dans le script | Pauses internes mesurées |
|---|---|---|---|
| gen-1 | 01 | 2 | 2 |
| gen-2 | 02 | 2 | 5 |
| gen-3 | 03 | 2 | **0** |
| gen-4 | 04 | 3 | 3 |
| gen-5 | 05 | 2 | 1 |
| gen-6 | 06 | 3 | 4 |

L'avatar ne marque pas ses fins de phrase de façon fiable : `gen-3` enchaîne sans aucune
pause détectable malgré un point. Le nombre de pauses ne dit donc rien du script.

**2. Durée / débit — partiellement exploitable.** Débit mesuré sur les 6 clips connus :
**3,05 mots/seconde** (écart-type 0,25 ; de 2,63 à 3,35). Prédiction pour les scripts
suivants, et confrontation :

| Script | Mots | Durée prédite | Clip qui colle |
|---|---|---|---|
| 07 Contrat & salaire | 29 | ~9,5 s | gen-7, gen-8 ou gen-10 |
| 08 Planning par poste | 26 | ~8,5 s | **gen-9 (8,34 s)** |
| 09 Assigner les tâches | 29 | ~9,5 s | gen-7, gen-8 ou gen-10 |
| 10 QR code de pointage | 29 | ~9,5 s | gen-7, gen-8 ou gen-10 |
| 11 Jarvis | 31 | ~10,2 s | gen-7 (9,83 s) plutôt |

**Conclusion honnête** : seul `gen-9` est identifiable — c'est le seul script court de la
série (26 mots), et le seul clip nettement plus bref. Les trois autres font tous 29 à 31
mots et tombent dans la marge de bruit du débit : les départager reviendrait à tirer au sort,
et une erreur mettrait l'avatar en train de parler d'autre chose que le logiciel affiché.

## ✅ Comment supprimer le problème définitivement

Mettre le numéro du script dans le nom du fichier au moment de l'export HeyGen :
`07.mp4`, `08.mp4`, `09.mp4`… Le montage devient alors entièrement automatique, sans
confirmation ni risque d'inversion — et les doublons se repèrent tout seuls.
