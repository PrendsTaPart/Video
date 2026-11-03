# Épisode 04 « Le brunch des zombies » — provenance

**Aucune génération Higgsfield n'a été lancée** (règle `CLAUDE.md`). Les deux plans de 10 s
existaient déjà dans la bibliothèque du compte et sont **réutilisés tels quels**.

| Plan | Generation ID Higgsfield | Fichier |
|---|---|---|
| Scène 1 — « Ils arrivent » | `ab380df9-909d-479b-b764-66e8dd6c41fd` | `source/ep04-scene1.mp4` |
| Scène 2 — « Dix minutes » | `96615720-6e6a-4908-a5b6-a83fc85be935` | `source/ep04-scene2.mp4` |
| Scène 2, prise alternative | `3adbbfab-9708-41cf-b0fe-d5416cf69f97` | `source/ep04-scene2-prise-alternative.mp4` |

Sources d'origine : 720×1280, 24 fps, ~10 s, audio AAC 32 kHz (dialogue français et ambiance
générés dans la même passe). Les prompts stockés côté Higgsfield correspondent à la fiche
`prompts/ep04-le-brunch-des-zombies.md`, à une différence près : la référence visage y est passée en
`<<<image_1>>>` (Reference Element) au lieu de `@Image 1`.

## Sorties

| Fichier | Contenu |
|---|---|
| `ep04-le-brunch-des-zombies.mp4` | **Le master** : scène 1 + scène 2 + transition + animation, 1080×1920, 30 fps, 32,1 s |
| `ep04-outro.mp4` | L'outro seul, 12 s, voix off + SFX |
| `ep04-outro-muet.mp4` | L'outro seul, 12 s, SFX uniquement |
| `vo.mp3` | La voix off de l'épisode, normalisée |
| `ep04-thumb.png` | Miniature : le plan figé du début de l'outro + le titre |
| `scene2-last-frame.png` | Dernière image de la scène 2, plaque de départ de l'outro |

## Voix off

| | |
|---|---|
| Voix | **Adam - Instructor** `TGAegA0zNRi8I6nUdq3i`, modèle `eleven_multilingual_v2` |
| Transition (commune aux 30 épisodes) | « Cette scène aurait pu être évitée ? » — prise `sZWCVMCGg2WgpYJb4j3c` (2,04 s), calée à 2,1 s |
| Ligne de l'épisode | « Le rush du dimanche n'est pas une invasion. FoodEatUp met tout le monde en file et remplit la salle table par table. » |
| Prise retenue | `FJ4w50OFQYxItDFhqK04` (6,08 s) |
| Calage | démarre à **4,60 s**, se termine à **10,68 s** (fenêtre : avant 11,0 s) ✅ |

Les prises ElevenLabs sortent très bas : chacune est normalisée à −16 LUFS / −1,5 dBTP.
Le départ de la voix est calculé pour qu'elle finisse avant 11,0 s : 4,60 s par défaut, avancé quand
la prise est longue. L'outro est ensuite calé au niveau de saison (−18,5 LUFS), puis le master normalisé
à −16 LUFS en gain linéaire (loudnorm deux passes), le standard des plateformes.

## Dépôt au catalogue Social FoodEatUp

| | |
|---|---|
| Épisode au catalogue | `EPC04` — série `michael-fait-son-cinema`, saison 2 |
| Pièce | `master` |
| État | **pret** |
| Fichier | https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/michael-fait-son-cinema-EPC04-le-brunch-des-zombies-master |

« pret » s'écrit par un agent, « valide » est un geste humain dans /admin/production. Rien ne se planifie sur les réseaux sans « valide » : aucun outil n'expose cette bascule.

## Calage des SFX dans l'outro (secondes)

`clap` 0,40 · `whoosh` 2,00 (la punchline de transition) · `tick` 4,40 / 4,73 / 5,07
(l'élément clé qui devient des données) · `whoosh` 7,60 (l'action en un tap) · `tick`
9,33 / 9,67 / 10,00 (les cartes modules) · `whoosh` 10,95 + `impact` 11,00 (le logo).

## Reconstruire

```bash
./scripts/monter-episode.sh 04
```

---
Fichier généré par `scripts/sources.mjs` depuis `renders/sources.json`, ne pas éditer à la main.
