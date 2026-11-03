# ÉPISODE 07 — « LA BOMBE »

🎬 **Genre** : Film de démineurs
🍽️ **Situation** : Une cliente allergique, deux sauces, un chef absent
⚙️ **Module** : Recettes + Allergènes
🎯 **Hook (0–2 s)** : « Je suis allergique aux noix. » — « Bien sûr. » (le sourire tombe dès qu'il se retourne)

## Sélecteurs Higgsfield

| Époque | Genre | Lumière | Physique | Objectif | Émotion | Montage |
|---|---|---|---|---|---|---|
| 2020s | thriller d'action | néon cuisine froid, angle frontal | réaliste | macro 100 mm | panique silencieuse | 4 plans |

> Le look du film se règle dans ces sélecteurs : ne le répétez pas dans le texte du prompt.

## SEEDANCE 01 — Laquelle ?

*Deux bols, un chrono qui bipe, Michael avec une pince comme un démineur*

```text
REF: Michael = @Image 1 (face, hair, build) + @Image 2 (season outfit), keep identical. Locations = @Image 3 then @Image 4.
FORMAT: 9:16, 10 s, 4 shots, realistic comedy shot like a bomb-defusal thriller.
SCENE: Dining room, an adult customer calmly speaks to Michael; then the kitchen: the chef's hat hangs on a hook, the chef is gone; two sauce bowls on the pass, one red, one green; a kitchen timer ticking.
ACTION:
0–2 s: the customer states her allergy; Michael smiles, turns around, and the smile drops instantly.
2–5 s: kitchen: Michael grips a pair of tongs, sweat beads in macro, the timer beeps.
5–8 s: rapid alternating close-ups: red bowl, green bowl, red, green, Michael's eyes.
8–10 s: extreme close-up on the tongs hovering; the timer beeps faster; Michael speaks.
DIALOGUE (spoken French, slow and clear, natural lip-sync, no captions): Customer: « Je suis allergique aux noix. » Michael: « Bien sûr. » Michael: « C'est laquelle ? »
CAMERA: medium two-shot → whip to kitchen → macro inserts → extreme close-up.
LIGHT & GRADE: cold kitchen fluorescents, red and green bowls saturated, blue shadows.
AUDIO: timer tick, beeps accelerating, tense pulse (original), sweat drop, tongs click.
PHYSICS: realistic body weight, no morphing, no sliding feet, correct hands and fingers, no extra limbs. SKIN: preserve Michael's natural skin and features from @Image 1, no smoothing, no plastic look. NO-IP: no brands, no logos, no readable text, no captions or subtitles, no recognizable songs, no real celebrity likeness, no minors. Keep Michael's face, hair, build and outfit identical through the whole clip. Sharp, clean, cinematic render.
```

## SEEDANCE 02 — C'est sûr

*Le chef ne répond pas, Michael sert du pain et de l'eau*

```text
REF: Michael = @Image 1 (face, hair, build) + @Image 2 (season outfit), keep identical. Locations = @Image 4 then @Image 3.
FORMAT: 9:16, 10 s, 4 shots, realistic comedy shot like a bomb-defusal thriller.
SCENE: Same kitchen, then the customer's table.
ACTION:
0–2 s: Michael phones the chef, listens to the ringing tone, no answer.
2–5 s: he sniffs the red sauce, nothing; sniffs the green sauce and squints; turns over a stained, blurred recipe card he cannot read.
5–8 s: the tongs approach the red bowl, stop a centimetre away; he puts the tongs down and exhales.
8–10 s: dining room: he serves the customer a perfectly clean plate with bread and a glass of water; the timer stops.
DIALOGUE (spoken French, slow and clear, natural lip-sync, no captions): Customer: « C'est tout ? » Michael: « C'est sûr. »
CAMERA: close-up on phone → macro on the sniff → extreme close-up on tongs → medium at the table, timer click.
LIGHT & GRADE: cold kitchen, then warm dining light on the clean plate.
AUDIO: ringing tone, sniff, card flip, tongs down, heartbeat stops, plate set down, timer click.
PHYSICS: realistic body weight, no morphing, no sliding feet, correct hands and fingers, no extra limbs. SKIN: preserve Michael's natural skin and features from @Image 1, no smoothing, no plastic look. NO-IP: no brands, no logos, no readable text, no captions or subtitles, no recognizable songs, no real celebrity likeness, no minors. Keep Michael's face, hair, build and outfit identical through the whole clip. Sharp, clean, cinematic render.
```

## CLAUDE CODE — 12 s (outro ep07 : 2 s de transition + 10 s d'animation)

**Voix off — transition** (commune aux 30 épisodes, à 2,1 s) : « Cette scène aurait pu être évitée ? »

**Voix off — épisode** (à 4,6 s) : « Un allergène, ça se sait avant de servir. FoodEatUp l'affiche sur chaque recette et sur votre site. »

```text
Tu es motion designer. Crée avec Remotion (React) une composition verticale 1080×1920, 30 fps,
300 images (10 s), export MP4 H.264, fichier ep07-outro.mp4.

Entrées dans ./assets :
- logo-foodeatup.svg : logo officiel. Ne jamais le redessiner, le déformer, le recolorer, le rogner.
  Zone de protection = 10 % de sa largeur.
- palette.json : couleurs officielles de la charte FoodEatUp (exportées du CMS). Seules couleurs
  autorisées, aucune couleur inventée.
- scene2-last-frame.png : dernière image de la scène Seedance 2 (extraite avec ffmpeg).
- vo.mp3 : voix off de l'épisode (ElevenLabs, même voix sur toute la saison).
- sfx/ : clap.wav, whoosh.wav, tick.wav, impact.wav.

STRUCTURE IMPOSÉE (identique sur les 30 épisodes — c'est la signature de la saison) :
0–2 s : scene2-last-frame plein écran, léger zoom avant, désaturation progressive ; clap de cinéma qui entre par le bas et claque à 0,4 s (SFX clap) ; texte « COUPEZ ! ».
2–4 s : TRANSITION (identique sur les 30 épisodes) : sur le plan figé, la punchline « Cette scène aurait pu être évitée ? » à l'écran et en voix off (calée à 2,1 s) ; puis « Dans la vraie vie… » et fondu vers l'animation.
4–6 s : L'élément clé de la scène se transforme en données (motion blur, particules légères, easing expo-out) — précisé par épisode.
6–9 s : Démonstration du bénéfice : maquette d'écran FoodEatUp en 3D légère (rotation ≤ 8°), micro-animations, action en UN tap, ralenti de 6 images sur le tap.
9–11 s : Les modules concernés apparaissent en cartes reliées par des flux lumineux (libellés réels uniquement).
11–12 s : Tout disparaît ; logo FoodEatUp seul, centré, scale 0,9 → 1 + halo ; signature sous le logo ; SFX impact + whoosh ; fondu.

TRANSITION (identique sur les 30 épisodes, ne pas la réinventer) :
Texte à l'écran de 2,0 à 3,8 s, sur le plan figé qui finit de se désaturer : « Cette scène aurait pu être évitée ? »
Voix off de la transition calée à 2,1 s — une seule prise ElevenLabs sert les 30 épisodes.
Puis « Dans la vraie vie… » à 3,6 s et fondu vers l'animation à 3,9 s.

CONTENU DE CET ÉPISODE :
2–4 s : les deux bols se déplient en deux fiches recette ; les ingrédients défilent ligne par ligne ; une ligne s'allume avec une icône allergène.
4–7 s : écran Recettes : ingrédients, quantités, allergènes signalés sur le plat → la page Allergènes du site vitrine s'active en un tap.
7–9 s : cartes : Recettes · Ingrédients · Site vitrine · Pages.
Modules affichés en cartes (7–9 s) : Recettes · Ingrédients · Site vitrine · Pages
Texte à l'écran : « Allergènes : visibles avant. Pas après. »
Voix off de l'épisode (démarre à 4,6 s, finie avant 11,0 s) : « Un allergène, ça se sait avant de servir. FoodEatUp l'affiche sur chaque recette et sur votre site. »
SFX : tick par ligne, alerte douce, impact final.

RÈGLES : L'animation se comprend sans le son. Texte ≥ 64 px, ≤ 6 mots par écran, zone sûre TikTok/Reels/Shorts (marges 220 px haut, 320 px bas, 120 px côtés). Jamais de faux texte d'interface : uniquement les libellés réels. Deux lignes de voix off : la punchline de transition à 2,1 s, puis la voix de l'épisode à 4,6 s, terminée avant 11,0 s. Un SFX par apparition ; motion blur sur les zooms. Rendu premium SaaS, humoristique, moderne, lisible sur smartphone.

SORTIES : ep07-outro.mp4 · ep07-outro-muet.mp4 · ep07-thumb.png
Titre de la miniature : « La bombe ».
```

## Contrôle avant publication

- [ ] Michael : même visage, même coiffure, même tenue sur les deux scènes.
- [ ] Aucun texte lisible généré par Seedance (enseigne, ticket, écran, sous-titre).
- [ ] Chaque réplique est compréhensible sans sous-titres.
- [ ] La chute est claire avant la fin de la scène 2 et Michael regarde la caméra.
- [ ] Le clap « COUPEZ ! » arrive à 0,4 s de l'outro.
- [ ] Modules affichés : Recettes · Ingrédients · Site vitrine · Pages — libellés réels vérifiés.
- [ ] Logo FoodEatUp intact, centré, seul à l'écran de 9 à 10 s.
- [ ] La vidéo se comprend sans le son.

---
Source : `episodes/` + `saison.json` — fiche générée par `scripts/build.mjs`, ne pas éditer à la main.
