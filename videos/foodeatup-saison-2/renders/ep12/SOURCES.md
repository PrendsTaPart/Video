# Épisode 12 « Le casting » — provenance

**Aucune génération Higgsfield n'a été lancée** (règle `CLAUDE.md`). Les deux plans de 10 s
existaient déjà dans la bibliothèque du compte et sont **réutilisés tels quels**.

| Plan | Generation ID Higgsfield | Fichier |
|---|---|---|
| Scène 1 — « Suivant » | `2f1f2533-00ce-4bc1-aa7f-bb3e2a50d22e` | `source/ep12-scene1.mp4` |
| Scène 2 — « Y'a personne » | `d6533af5-f81b-4872-850c-2670deb5cc80` | `source/ep12-scene2.mp4` |

> ⚠️ Tenue de saison rompue entre les deux scènes : Michael porte la toque, la veste blanche et le tablier FoodEatUp en scène 1, mais une chemise puis une veste sombres, sans toque, en scène 2. La checklist de saison l'interdit — la scène 2 est à regénérer avant validation. L'épisode n'est pas déposé au catalogue pour cette raison.

Sources d'origine : 720×1280, 24 fps, ~10 s, audio AAC 32 kHz (dialogue français et ambiance
générés dans la même passe). Les prompts stockés côté Higgsfield correspondent à la fiche
`prompts/ep12-le-casting.md`, à une différence près : la référence visage y est passée en
`<<<image_1>>>` (Reference Element) au lieu de `@Image 1`.

## Sorties

| Fichier | Contenu |
|---|---|
| `ep12-le-casting.mp4` | **Le master** : scène 1 + scène 2 + transition + animation, 1080×1920, 30 fps, 32,1 s |
| `ep12-outro.mp4` | L'outro seul, 12 s, voix off + SFX |
| `ep12-outro-muet.mp4` | L'outro seul, 12 s, SFX uniquement |
| `vo.mp3` | La voix off de l'épisode, normalisée |
| `ep12-thumb.png` | Miniature : le plan figé du début de l'outro + le titre |
| `scene2-last-frame.png` | Dernière image de la scène 2, plaque de départ de l'outro |

## Voix off

| | |
|---|---|
| Voix | **Adam - Instructor** `TGAegA0zNRi8I6nUdq3i`, modèle `eleven_multilingual_v2` |
| Transition (commune aux 30 épisodes) | « Cette scène aurait pu être évitée ? » — prise `sZWCVMCGg2WgpYJb4j3c` (2,04 s), calée à 2,1 s |
| Ligne de l'épisode | « Une offre, des candidatures classées, un statut par personne. Recruter sans courir après les CV. » |
| Prise retenue | `kzEB3wToSJBmojcYmDGC` (5,8 s) |
| Calage | démarre à **4,60 s**, se termine à **10,40 s** (fenêtre : avant 11,0 s) ✅ |

Les prises ElevenLabs sortent très bas : chacune est normalisée à −16 LUFS / −1,5 dBTP.
Le départ de la voix est calculé pour qu'elle finisse avant 11,0 s : 4,60 s par défaut, avancé quand
la prise est longue. L'outro est ensuite calé au niveau de saison (−18,5 LUFS), puis le master normalisé
à −16 LUFS en gain linéaire (loudnorm deux passes), le standard des plateformes.

## Calage des SFX dans l'outro (secondes)

`clap` 0,40 · `whoosh` 2,00 (la punchline de transition) · `tick` 4,40 / 4,73 / 5,07
(l'élément clé qui devient des données) · `whoosh` 7,60 (l'action en un tap) · `tick`
9,33 / 9,67 / 10,00 (les cartes modules) · `whoosh` 10,95 + `impact` 11,00 (le logo).

## Reconstruire

```bash
./scripts/monter-episode.sh 12
```

---
Fichier généré par `scripts/sources.mjs` depuis `renders/sources.json`, ne pas éditer à la main.
