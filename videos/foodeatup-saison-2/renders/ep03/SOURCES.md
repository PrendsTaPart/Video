# Épisode 03 « Le critique » — provenance

**Aucune génération Higgsfield n'a été lancée** (règle `CLAUDE.md`). Les deux plans de 10 s
existaient déjà dans la bibliothèque du compte et sont **réutilisés tels quels**.

| Plan | Generation ID Higgsfield | Fichier |
|---|---|---|
| Scène 1 — « C'est lui » | `d0ff89f7-dbf5-41fa-9ff9-343789f6807f` | `source/ep03-scene1.mp4` |
| Scène 2 — « Une étoile » | `11191050-3916-467e-a1d2-e086182e0a31` | `source/ep03-scene2.mp4` |

Sources d'origine : 720×1280, 24 fps, ~10 s, audio AAC 32 kHz (dialogue français et ambiance
générés dans la même passe). Les prompts stockés côté Higgsfield correspondent à la fiche
`prompts/ep03-le-critique.md`, à une différence près : la référence visage y est passée en
`<<<image_1>>>` (Reference Element) au lieu de `@Image 1`.

## Sorties

| Fichier | Contenu |
|---|---|
| `ep03-le-critique.mp4` | **Le master** : scène 1 + scène 2 + transition + animation, 1080×1920, 30 fps, 32,1 s |
| `ep03-outro.mp4` | L'outro seul, 12 s, voix off + SFX |
| `ep03-outro-muet.mp4` | L'outro seul, 12 s, SFX uniquement |
| `vo.mp3` | La voix off de l'épisode, normalisée |
| `ep03-thumb.png` | Miniature : le plan figé du début de l'outro + le titre |
| `scene2-last-frame.png` | Dernière image de la scène 2, plaque de départ de l'outro |

## Voix off

| | |
|---|---|
| Voix | **Adam - Instructor** `TGAegA0zNRi8I6nUdq3i`, modèle `eleven_multilingual_v2` |
| Transition (commune aux 30 épisodes) | « Cette scène aurait pu être évitée ? » — prise `sZWCVMCGg2WgpYJb4j3c` (2,04 s), calée à 2,1 s |
| Ligne de l'épisode | « Le vrai critique, c'est chaque client. FoodEatUp réunit tous vos avis et vous aide à répondre. » |
| Prise retenue | `YLcYEbeoxV6bkVVbakaT` (5,39 s) |
| Calage | démarre à **4,60 s**, se termine à **9,99 s** (fenêtre : avant 11,0 s) ✅ |

Les prises ElevenLabs sortent très bas : chacune est normalisée à −16 LUFS / −1,5 dBTP.
L'outro est ensuite calé au niveau de saison (−18,5 LUFS), puis le master entier est normalisé
à −16 LUFS en gain linéaire (loudnorm deux passes), le standard des plateformes.

## Calage des SFX dans l'outro (secondes)

`clap` 0,40 · `whoosh` 2,00 (la punchline de transition) · `tick` 4,40 / 4,73 / 5,07
(l'élément clé qui devient des données) · `whoosh` 7,60 (l'action en un tap) · `tick`
9,33 / 9,67 / 10,00 (les cartes modules) · `whoosh` 10,95 + `impact` 11,00 (le logo).

## Reconstruire

```bash
./scripts/monter-episode.sh 03
```

---
Fichier généré par `scripts/sources.mjs` depuis `renders/sources.json`, ne pas éditer à la main.
