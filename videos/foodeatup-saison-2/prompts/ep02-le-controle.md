# ÉPISODE 02 — « LE CONTRÔLE »

🎬 **Genre** : Thriller d'interrogatoire
🍽️ **Situation** : Le contrôle d'hygiène demande les relevés de température
⚙️ **Module** : HACCP
🎯 **Hook (0–2 s)** : Une lampe qui balance, une voix calme : « Vos températures ? »

## Sélecteurs Higgsfield

| Époque | Genre | Lumière | Physique | Objectif | Émotion | Montage |
|---|---|---|---|---|---|---|
| 2020s | thriller | lampe nue en plongée, angle bas | réaliste | 50 mm | angoisse contenue | 4 plans |

> Le look du film se règle dans ces sélecteurs : ne le répétez pas dans le texte du prompt.

## SEEDANCE 01 — Quelque part

*Michael interrogé dans sa propre cuisine par un inspecteur de dos*

```text
REF: Michael = @Image 1 (face, hair, build) + @Image 2 (season outfit), keep identical. Location = @Image 4 (kitchen).
FORMAT: 9:16, 10 s, 4 shots, realistic comedy shot like an interrogation thriller.
SCENE: The kitchen in darkness, one bare bulb swinging over a steel table. Michael sits on a stool, hands flat on the table. An adult inspector in a grey jacket stands with his back to camera, holding a clipboard.
ACTION:
0–2 s: the bulb swings, light sweeps across Michael's face, the inspector speaks.
2–5 s: slow push-in on Michael, a clock ticks, sweat on his temple, he answers.
5–8 s: Michael searches his pockets, pulls out a crumpled sticky note, reads it, turns it over, reads the other side.
8–10 s: extreme close-up on Michael's mouth as he whispers; the bulb goes out; black.
DIALOGUE (spoken French, slow and clear, natural lip-sync, no captions): Inspector (calm): « Vos températures ? » Michael: « Elles sont… quelque part. » Michael (whisper): « Hier… je crois. »
CAMERA: swinging light wide → slow push-in → insert on hands → extreme close-up → cut to black.
LIGHT & GRADE: single hard practical, deep shadows, cold desaturated grade.
AUDIO: buzzing bulb, clock tick, pen tapping, paper crumple, low tense drone, electric pop at blackout.
PHYSICS: realistic body weight, no morphing, no sliding feet, correct hands and fingers, no extra limbs. SKIN: preserve Michael's natural skin and features from @Image 1, no smoothing, no plastic look. NO-IP: no brands, no logos, no readable text, no captions or subtitles, no recognizable songs, no real celebrity likeness, no minors. Keep Michael's face, hair, build and outfit identical through the whole clip. Sharp, clean, cinematic render.
```

## SEEDANCE 02 — Dans ma tête

*Des post-its partout, le ventilateur les envoie tous en l'air*

```text
REF: Michael = @Image 1 (face, hair, build) + @Image 2 (season outfit), keep identical. Location = @Image 4.
FORMAT: 9:16, 10 s, 4 shots, realistic comedy shot like an interrogation thriller.
SCENE: Same kitchen, the bulb back on; a cardboard box overflowing with sticky notes now sits in front of Michael.
ACTION:
0–2 s: the bulb flickers on, revealing the box; Michael smiles nervously.
2–5 s: fast montage: Michael finds sticky notes inside the fridge door, under the floor mat, inside the extractor hood, inside his own shoe.
5–8 s: he lays the notes on the table in a row like playing cards, counting them off; the inspector's pen taps faster.
8–10 s: a floor fan switches on, every note lifts into the air in slow motion; Michael stays perfectly still and looks at the camera.
DIALOGUE (spoken French, slow and clear, natural lip-sync, no captions): Michael: « Lundi… mardi… » Michael (to camera): « Je note tout. Dans ma tête. »
CAMERA: flicker reveal → quick inserts → top-down on the table → slow-motion medium shot with notes floating.
LIGHT & GRADE: same bare bulb, cold grade, notes catching the light.
AUDIO: fridge door, hood rattle, shoe squeak, fan spinning up, paper flutter in slow motion, pen click.
PHYSICS: realistic body weight, no morphing, no sliding feet, correct hands and fingers, no extra limbs. SKIN: preserve Michael's natural skin and features from @Image 1, no smoothing, no plastic look. NO-IP: no brands, no logos, no readable text, no captions or subtitles, no recognizable songs, no real celebrity likeness, no minors. Keep Michael's face, hair, build and outfit identical through the whole clip. Sharp, clean, cinematic render.
```

## CLAUDE CODE — 12 s (outro ep02 : 2 s de transition + 10 s d'animation)

**Voix off — transition** (commune aux 30 épisodes, à 2,1 s) : « Cette scène aurait pu être évitée ? »

**Voix off — épisode** (à 4,6 s) : « Le contrôle d'hygiène ? Avec FoodEatUp, chaque relevé est daté, rangé, prêt à montrer. »

```text
Tu es motion designer. Crée avec Remotion (React) une composition verticale 1080×1920, 30 fps,
300 images (10 s), export MP4 H.264, fichier ep02-outro.mp4.

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
2–4 s : les post-its volants se figent, s'alignent en grille, deviennent des lignes horodatées.
4–7 s : écran HACCP : un relevé de température saisi en un tap sur un équipement → historique par jour → « export » d'un rapport en une pression.
7–9 s : cartes : HACCP · Températures · Étiquettes DLC · Traçabilité · Checklist hygiène.
Modules affichés en cartes (7–9 s) : HACCP · Températures · Étiquettes DLC · Traçabilité · Checklist hygiène
Texte à l'écran : « HACCP : tout est noté. Pas dans votre tête. »
Voix off de l'épisode (démarre à 4,6 s, finie avant 11,0 s) : « Le contrôle d'hygiène ? Avec FoodEatUp, chaque relevé est daté, rangé, prêt à montrer. »
SFX : tick par ligne, whoosh d'export, impact final.

RÈGLES : L'animation se comprend sans le son. Texte ≥ 64 px, ≤ 6 mots par écran, zone sûre TikTok/Reels/Shorts (marges 220 px haut, 320 px bas, 120 px côtés). Jamais de faux texte d'interface : uniquement les libellés réels. Deux lignes de voix off : la punchline de transition à 2,1 s, puis la voix de l'épisode à 4,6 s, terminée avant 11,0 s. Un SFX par apparition ; motion blur sur les zooms. Rendu premium SaaS, humoristique, moderne, lisible sur smartphone.

SORTIES : ep02-outro.mp4 · ep02-outro-muet.mp4 · ep02-thumb.png
Titre de la miniature : « Le contrôle ».
```

## Contrôle avant publication

- [ ] Michael : même visage, même coiffure, même tenue sur les deux scènes.
- [ ] Aucun texte lisible généré par Seedance (enseigne, ticket, écran, sous-titre).
- [ ] Chaque réplique est compréhensible sans sous-titres.
- [ ] La chute est claire avant la fin de la scène 2 et Michael regarde la caméra.
- [ ] Le clap « COUPEZ ! » arrive à 0,4 s de l'outro.
- [ ] Modules affichés : HACCP · Températures · Étiquettes DLC · Traçabilité · Checklist hygiène — libellés réels vérifiés.
- [ ] Logo FoodEatUp intact, centré, seul à l'écran de 9 à 10 s.
- [ ] La vidéo se comprend sans le son.

---
Source : `episodes/` + `saison.json` — fiche générée par `scripts/build.mjs`, ne pas éditer à la main.
