# Avatar RapidoCMS Académie

Assets de l'avatar 3D et de sa stack de synchro labiale, pour les pastilles
présentateur des tutoriels RapidoCMS (`videos/academie-rapidocms/`).

## Contenu

| Fichier | Origine | Rôle |
|---|---|---|
| `rapido-avatar.glb` | dépôt Lovable `academie-rapido-spark` (36,4 Mo, glTF 2) | le modèle 3D animé dans three.js |
| `assistante-still.png` | idem | image fixe de secours |
| `decor-bureau.jpg` | idem | fond décor bureau pour l'incrustation |
| `lib/*.ts` | `academie-rapido-spark/src/lib/` — **copiés tels quels, ne pas réécrire** | stack lipsync |
| `poses/*.png` | photos fournies par Michael (session studio du 2026-08-28) | poses du présentateur pour vignettes et cartons |

## Stack lipsync (`lib/`)

- `fr-phonemes.ts` — graphème → phonème français → visème.
- `audio-visemes.ts` — timings de visèmes à partir du texte + audio.
- `lipsync-engine.ts` — seul point d'écriture sur les morphs de la bouche
  (la piste de visèmes décide de la forme, l'audio ne module que l'amplitude).
- `lipsync-timing.ts` — alignement temporel.
- `face-idle.ts` — micro-mouvements d'attente (clignements, respiration).
- `avatar-tuning.ts`, `poses.ts` — réglages et catalogue de poses.

Les imports `@/assets/poses/*.asset.json` de `poses.ts` référencent le CDN
Lovable ; dans ce dépôt, utiliser directement les PNG de `poses/`.

## Poses disponibles (`poses/`)

`accueil` (mains jointes, cravate) · `bras-ouverts` · `casque` (support, pouce
levé) · `checklist` (porte-bloc) · `decouverte` (main levée, enthousiaste) ·
`dossier` · `laptop` · `pointe-droite` · `pointe-gauche` · `presente-paume` ·
`reflexion` (main au menton) · `stop` · `telephone` · `victoire` (poing levé).

Fond blanc uniforme 1024×1024, prêtes pour détourage (`_cutout` du pipeline
`videos/planit-academy/academie.py`).
