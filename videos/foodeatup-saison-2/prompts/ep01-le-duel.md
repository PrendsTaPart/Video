# ÉPISODE 01 — « LE DUEL »

🎬 **Genre** : Western (le duel de midi)
🍽️ **Situation** : Deux clients ont réservé la même table
⚙️ **Module** : Réservations + Plan de salle
🎯 **Hook (0–2 s)** : « C'est ma table. » — « Non. La mienne. »

## Sélecteurs Higgsfield

| Époque | Genre | Lumière | Physique | Objectif | Émotion | Montage |
|---|---|---|---|---|---|---|
| 1960s | western | soleil dur de midi, angle haut | réaliste | anamorphique 40 mm | tension comique | 4 plans |

> Le look du film se règle dans ces sélecteurs : ne le répétez pas dans le texte du prompt.

## SEEDANCE 01 — Midi pile

*Michael serveur, deux clients arrivent par deux portes, même table*

```text
REF: Michael = @Image 1 (face, hair, build) + @Image 2 (season outfit), keep identical. Location = @Image 3 (dining room).
FORMAT: 9:16, 10 s, 4 shots, realistic comedy shot like a western.
SCENE: A French bistro at noon, dust motes in hard sunlight, a wall clock at twelve, a crumpled napkin ball rolling across the floor like tumbleweed. Michael stands alone in the middle of the room as the waiter.
ACTION:
0–2 s: wide low shot, the napkin rolls, the clock ticks, Michael squints into the light.
2–5 s: two adult customers push through two opposite doors in slow motion, walk toward the same table and stop face to face across it.
5–8 s: whip-cuts between extreme close-ups of their eyes and their hands hovering over forks; Michael opens a paper notebook, a drop of sweat, crash zoom on his face.
8–10 s: Michael slowly turns to the camera and freezes.
DIALOGUE (spoken French, slow and clear, natural lip-sync, no captions): Customer A: « C'est ma table. » Customer B: « Non. La mienne. » Michael: « J'ai… réservé deux fois. »
CAMERA: low wide → slow-motion dolly → extreme close-ups → crash zoom → freeze frame.
LIGHT & GRADE: hard midday sun, warm sepia grade, long shadows, fine film grain.
AUDIO: dry wind, a creaking sign, a single guitar note (original), a fly buzzing, tense drone, comic zoom whoosh.
PHYSICS: realistic body weight, no morphing, no sliding feet, correct hands and fingers, no extra limbs. SKIN: preserve Michael's natural skin and features from @Image 1, no smoothing, no plastic look. NO-IP: no brands, no logos, no readable text, no captions or subtitles, no recognizable songs, no real celebrity likeness, no minors. Keep Michael's face, hair, build and outfit identical through the whole clip. Sharp, clean, cinematic render.
```

## SEEDANCE 02 — Table pour trois

*Le duel continue, Michael traîne une deuxième table, les deux clients s'assoient quand même ensemble*

```text
REF: Michael = @Image 1 (face, hair, build) + @Image 2 (season outfit), keep identical. Location = @Image 3.
FORMAT: 9:16, 10 s, 4 shots, realistic comedy shot like a western.
SCENE: Same bistro, same table, the two customers still standing and staring at each other; Michael between them holding a chair like a lion tamer.
ACTION:
0–2 s: close-up on boots shifting on the floor, a fly lands on Michael's nose, he does not move.
2–5 s: Michael proposes, both customers answer at once without looking at him.
5–8 s: speed ramp: Michael drags a second table across the room in a cloud of dust, sets two candles, bows; the two customers sit down at the SAME first table, back to back.
8–10 s: Michael sits between them, bites a breadstick, looks at the camera; whip pan out to a wide shot.
DIALOGUE (spoken French, slow and clear, natural lip-sync, no captions): Michael: « On partage ? » Both customers: « Non. » Michael: « Table pour trois. »
CAMERA: macro on boots → medium on Michael → fast dolly with speed ramp → static wide, whip pan.
LIGHT & GRADE: hard midday sun, warm sepia, dust in the light beam.
AUDIO: table screech, dust whoosh, harmonica sting (original), crunch of the breadstick, clock tick.
PHYSICS: realistic body weight, no morphing, no sliding feet, correct hands and fingers, no extra limbs. SKIN: preserve Michael's natural skin and features from @Image 1, no smoothing, no plastic look. NO-IP: no brands, no logos, no readable text, no captions or subtitles, no recognizable songs, no real celebrity likeness, no minors. Keep Michael's face, hair, build and outfit identical through the whole clip. Sharp, clean, cinematic render.
```

## CLAUDE CODE — 12 s (outro ep01 : 2 s de transition + 10 s d'animation)

**Voix off — transition** (commune aux 30 épisodes, à 2,1 s) : « Cette scène aurait pu être évitée ? »

**Voix off — épisode** (à 4,6 s) : « Deux clients, une table ? Avec FoodEatUp, la réservation vérifie la place avant vous. »

```text
Tu es motion designer. Crée avec Remotion (React) une composition verticale 1080×1920, 30 fps,
300 images (10 s), export MP4 H.264, fichier ep01-outro.mp4.

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
2–4 s : le carnet papier de Michael s'ouvre ; deux noms clignotent en rouge sur le même créneau ; le carnet se dissout en lignes de données.
4–7 s : écran Réservations : un créneau choisi → « disponibilité vérifiée » → la table est assignée en un tap ; sur le plan de salle, la table passe au statut réservé.
7–9 s : cartes reliées : Réservations · Plan de salle · Tables.
Modules affichés en cartes (7–9 s) : Réservations · Plan de salle · Tables
Texte à l'écran : « Une table. Un client. Zéro duel. »
Voix off de l'épisode (démarre à 4,6 s, finie avant 11,0 s) : « Deux clients, une table ? Avec FoodEatUp, la réservation vérifie la place avant vous. »
SFX : tick sur chaque nom, whoosh sur l'assignation, impact final.

RÈGLES : L'animation se comprend sans le son. Texte ≥ 64 px, ≤ 6 mots par écran, zone sûre TikTok/Reels/Shorts (marges 220 px haut, 320 px bas, 120 px côtés). Jamais de faux texte d'interface : uniquement les libellés réels. Deux lignes de voix off : la punchline de transition à 2,1 s, puis la voix de l'épisode à 4,6 s, terminée avant 11,0 s. Un SFX par apparition ; motion blur sur les zooms. Rendu premium SaaS, humoristique, moderne, lisible sur smartphone.

SORTIES : ep01-outro.mp4 · ep01-outro-muet.mp4 · ep01-thumb.png
Titre de la miniature : « Le duel ».
```

## Contrôle avant publication

- [ ] Michael : même visage, même coiffure, même tenue sur les deux scènes.
- [ ] Aucun texte lisible généré par Seedance (enseigne, ticket, écran, sous-titre).
- [ ] Chaque réplique est compréhensible sans sous-titres.
- [ ] La chute est claire avant la fin de la scène 2 et Michael regarde la caméra.
- [ ] Le clap « COUPEZ ! » arrive à 0,4 s de l'outro.
- [ ] Modules affichés : Réservations · Plan de salle · Tables — libellés réels vérifiés.
- [ ] Logo FoodEatUp intact, centré, seul à l'écran de 9 à 10 s.
- [ ] La vidéo se comprend sans le son.

---
Source : `episodes/` + `saison.json` — fiche générée par `scripts/build.mjs`, ne pas éditer à la main.
