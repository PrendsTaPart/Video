# ÉPISODE 17 — « LE ROUND »

🎬 **Genre** : Film de boxe (montage d'entraînement)
🍽️ **Situation** : Trois cents crêpes pour demain matin
⚙️ **Module** : Production
🎯 **Hook (0–2 s)** : Le chef, dos au mur comme un coach : « Trois cents crêpes. »

## Sélecteurs Higgsfield

| Époque | Genre | Lumière | Physique | Objectif | Émotion | Montage |
|---|---|---|---|---|---|---|
| 2020s | film de sport | aube dorée à travers la cuisine, angle latéral | réaliste | 35 mm caméra à l'épaule | détermination | 4 plans |

> Le look du film se règle dans ces sélecteurs : ne le répétez pas dans le texte du prompt.

## SEEDANCE 01 — Encore

*Montage d'entraînement à la poêle, sac de farine dans l'escalier*

```text
REF: Michael = @Image 1 (face, hair, build) + @Image 2 (season outfit) + a hoodie over the apron, keep identical. Location = @Image 4.
FORMAT: 9:16, 10 s, 4 shots, realistic comedy shot like a boxing training montage.
SCENE: Kitchen at dawn, golden light through the window; Michael in a hoodie over his apron holding a pan; an adult chef leans against the wall like a coach.
ACTION:
0–2 s: the chef announces the number; Michael repeats it, the chef repeats it.
2–5 s: training montage: Michael flips pancakes faster and faster, runs up the service stairs carrying a flour sack, does push-ups on the pass, skips rope with a kitchen towel.
5–8 s: one pancake sticks to the ceiling, another lands in the extractor hood; the coach blows a whistle.
8–10 s: close-up: Michael sweating, killer stare, one word.
DIALOGUE (spoken French, slow and clear, natural lip-sync, no captions): Chef: « Trois cents crêpes. » Michael: « Trois cents ? » Chef: « Trois cents. » Michael: « Encore. »
CAMERA: two-shot → fast-cut montage with speed ramps → tilt up to the ceiling → close-up.
LIGHT & GRADE: golden dawn, sweat highlights, warm grade with grain.
AUDIO: triumphant brass (original), pan flips, stair stomps, rope whipping, pancake splat, whistle.
PHYSICS: realistic body weight, no morphing, no sliding feet, correct hands and fingers, no extra limbs. SKIN: preserve Michael's natural skin and features from @Image 1, no smoothing, no plastic look. NO-IP: no brands, no logos, no readable text, no captions or subtitles, no recognizable songs, no real celebrity likeness, no minors. Keep Michael's face, hair, build and outfit identical through the whole clip. Sharp, clean, cinematic render.
```

## SEEDANCE 02 — Il en manque une

*La dernière crêpe monte, monte… et retombe sur sa tête*

```text
REF: Michael = @Image 1 (face, hair, build) + @Image 2 (season outfit) + a hoodie over the apron, keep identical. Location = @Image 4.
FORMAT: 9:16, 10 s, 4 shots, realistic comedy shot like a boxing final round.
SCENE: Same kitchen, a tower of pancakes on the pass; the chef holds up a hand like a referee.
ACTION:
0–2 s: the chef announces the count; Michael sets his stance.
2–5 s: he flips the last pancake in slow motion; it rises and rises; the camera follows it up; it falls… onto his head.
5–8 s: he stands still with the pancake as a hat; a bell rings; the chef lifts Michael's arm like a winner.
8–10 s: Michael, under the pancake, looks at the camera.
DIALOGUE (spoken French, slow and clear, natural lip-sync, no captions): Chef: « Deux cent quatre-vingt-dix-neuf. » Michael: « Il en manque une. »
CAMERA: medium → slow-motion tilt following the pancake → static medium for the landing → close-up.
LIGHT & GRADE: golden dawn, the pancake backlit as it rises.
AUDIO: crowd hush, slow-motion whoosh, soft splat, boxing bell, small cheer, silence.
PHYSICS: realistic body weight, no morphing, no sliding feet, correct hands and fingers, no extra limbs. SKIN: preserve Michael's natural skin and features from @Image 1, no smoothing, no plastic look. NO-IP: no brands, no logos, no readable text, no captions or subtitles, no recognizable songs, no real celebrity likeness, no minors. Keep Michael's face, hair, build and outfit identical through the whole clip. Sharp, clean, cinematic render.
```

## CLAUDE CODE — 12 s (outro ep17 : 2 s de transition + 10 s d'animation)

**Voix off — transition** (commune aux 30 épisodes, à 2,1 s) : « Cette scène aurait pu être évitée ? »

**Voix off — épisode** (à 4,6 s) : « Trois cents crêpes, c'est un plan de production. FoodEatUp calcule les ingrédients, prévient ce qui manque et met le stock à jour. »

> ⚠️ Cette phrase dépasse la fenêtre de 7 s (2,0 s → 9,0 s) à débit posé.
> **Variante courte proposée** : « Trois cents crêpes, c'est un plan de production. FoodEatUp calcule les ingrédients et suit le stock. »

```text
Tu es motion designer. Crée avec Remotion (React) une composition verticale 1080×1920, 30 fps,
300 images (10 s), export MP4 H.264, fichier ep17-outro.mp4.

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
2–4 s : la crêpe sur la tête de Michael devient un plan de production : quoi, combien, quand.
4–7 s : écran Production : recette choisie × quantité → ingrédients nécessaires calculés (farine, œufs, lait) avec les manquants signalés → validation en un tap → le stock se met à jour.
7–9 s : cartes : Production · Recettes · Ingrédients · Alertes production.
Modules affichés en cartes (7–9 s) : Production · Recettes · Ingrédients · Alertes production
Texte à l'écran : « Planifiez. Produisez. Le stock suit. »
Voix off de l'épisode (démarre à 4,6 s, finie avant 11,0 s) : « Trois cents crêpes, c'est un plan de production. FoodEatUp calcule les ingrédients, prévient ce qui manque et met le stock à jour. »
SFX : cloche courte, tick par ingrédient, impact final.

RÈGLES : L'animation se comprend sans le son. Texte ≥ 64 px, ≤ 6 mots par écran, zone sûre TikTok/Reels/Shorts (marges 220 px haut, 320 px bas, 120 px côtés). Jamais de faux texte d'interface : uniquement les libellés réels. Deux lignes de voix off : la punchline de transition à 2,1 s, puis la voix de l'épisode à 4,6 s, terminée avant 11,0 s. Un SFX par apparition ; motion blur sur les zooms. Rendu premium SaaS, humoristique, moderne, lisible sur smartphone.

SORTIES : ep17-outro.mp4 · ep17-outro-muet.mp4 · ep17-thumb.png
Titre de la miniature : « Le round ».
```

## Contrôle avant publication

- [ ] Michael : même visage, même coiffure, même tenue sur les deux scènes.
- [ ] Aucun texte lisible généré par Seedance (enseigne, ticket, écran, sous-titre).
- [ ] Chaque réplique est compréhensible sans sous-titres.
- [ ] La chute est claire avant la fin de la scène 2 et Michael regarde la caméra.
- [ ] Le clap « COUPEZ ! » arrive à 0,4 s de l'outro.
- [ ] Modules affichés : Production · Recettes · Ingrédients · Alertes production — libellés réels vérifiés.
- [ ] Logo FoodEatUp intact, centré, seul à l'écran de 9 à 10 s.
- [ ] La vidéo se comprend sans le son.

---
Source : `episodes/` + `saison.json` — fiche générée par `scripts/build.mjs`, ne pas éditer à la main.
