# ÉPISODE 11 — « LA VAR »

🎬 **Genre** : Retransmission sportive (photo-finish, assistance vidéo)
🍽️ **Situation** : Le serveur arrive une seconde après le début de son shift
⚙️ **Module** : Pointages + Planning
🎯 **Hook (0–2 s)** : Un serveur court dans la rue au ralenti extrême, voix de commentateur : « Il arrive… il arrive… »

## Sélecteurs Higgsfield

| Époque | Genre | Lumière | Physique | Objectif | Émotion | Montage |
|---|---|---|---|---|---|---|
| 2020s | sport | stade / jour, angle bas | réaliste (ralenti haute vitesse) | 200 mm téléobjectif | suspense sportif | 4 plans |

> Le look du film se règle dans ces sélecteurs : ne le répétez pas dans le texte du prompt.

## SEEDANCE 01 — Une seconde

*Michael arbitre avec un sifflet, freeze frame sur la ligne d'arrivée*

```text
REF: Michael = @Image 1 (face, hair, build) + @Image 2 (season outfit) + a referee whistle, keep identical. Location = @Image 3 (entrance).
FORMAT: 9:16, 10 s, 4 shots, realistic comedy shot like a live sports broadcast.
SCENE: The restaurant entrance framed like a finish line; a wall clock just before twelve; Michael stands in the doorway with a whistle in his mouth.
ACTION:
0–2 s: an adult waiter in service clothes sprints down the street in extreme slow motion, overtaking a passer-by with a dog; sports commentator voice-over.
2–5 s: he crosses the doorway, sweat drops in slow motion; freeze frame like a photo-finish; the clock's second hand ticks just past twelve.
5–8 s: Michael blows the whistle and holds up one finger; the waiter protests.
8–10 s: Michael repeats, deadpan, close-up.
DIALOGUE (spoken French, slow and clear, natural lip-sync, no captions): Commentator: « Il arrive… il arrive… » Michael: « Une seconde. » Waiter: « Une seconde ?! » Michael: « Une seconde. »
CAMERA: telephoto slow-motion tracking → freeze frame → medium two-shot → close-up.
LIGHT & GRADE: bright daylight, punchy broadcast contrast, slight sharpening.
AUDIO: crowd roar under the commentary, slow-motion heartbeat, whistle, freeze-frame click.
PHYSICS: realistic body weight, no morphing, no sliding feet, correct hands and fingers, no extra limbs. SKIN: preserve Michael's natural skin and features from @Image 1, no smoothing, no plastic look. NO-IP: no brands, no logos, no readable text, no captions or subtitles, no recognizable songs, no real celebrity likeness, no minors. Keep Michael's face, hair, build and outfit identical through the whole clip. Sharp, clean, cinematic render.
```

## SEEDANCE 02 — C'est bon

*Le ralenti sous trois angles, verdict, célébration à genoux*

```text
REF: Michael = @Image 1 (face, hair, build) + @Image 2 (season outfit) + a referee whistle, keep identical. Location = @Image 3.
FORMAT: 9:16, 10 s, 4 shots, realistic comedy shot like a live sports broadcast.
SCENE: Michael in front of a small blurred screen on the bar (no readable content), drawing a rectangle in the air with his fingers like a video review.
ACTION:
0–2 s: Michael draws the rectangle gesture; the waiter waits, hands on hips.
2–5 s: replay of the doorway crossing from three angles in slow motion, the shoe touching the doormat; commentator whispers.
5–8 s: Michael stares at the screen for a long beat, turns to the waiter; suspense.
8–10 s: Michael taps his wrist and gives the verdict; the waiter slides on his knees across the floor in celebration; Michael raises both arms.
DIALOGUE (spoken French, slow and clear, natural lip-sync, no captions): Commentator: « C'est serré ! » Michael: « C'est bon. » Commentator: « Quel service ! »
CAMERA: medium on the gesture → three-angle replay inserts → close-up on Michael → wide on the knee slide.
LIGHT & GRADE: bright daylight, broadcast look, replay slightly cooler.
AUDIO: replay whoosh, crowd hush, whistle, crowd explosion, knee slide squeak.
PHYSICS: realistic body weight, no morphing, no sliding feet, correct hands and fingers, no extra limbs. SKIN: preserve Michael's natural skin and features from @Image 1, no smoothing, no plastic look. NO-IP: no brands, no logos, no readable text, no captions or subtitles, no recognizable songs, no real celebrity likeness, no minors. Keep Michael's face, hair, build and outfit identical through the whole clip. Sharp, clean, cinematic render.
```

## CLAUDE CODE — 12 s (outro ep11 : 2 s de transition + 10 s d'animation)

**Voix off — transition** (commune aux 30 épisodes, à 2,1 s) : « Cette scène aurait pu être évitée ? »

**Voix off — épisode** (à 4,6 s) : « Les heures, on ne les discute plus, on les voit. Pointage, planning et contrat au même endroit. »

```text
Tu es motion designer. Crée avec Remotion (React) une composition verticale 1080×1920, 30 fps,
300 images (10 s), export MP4 H.264, fichier ep11-outro.mp4.

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
2–4 s : l'image figée du photo-finish se transforme en une ligne de pointage : heure d'arrivée, heure prévue, écart.
4–7 s : écran Pointages : arrivée enregistrée en un tap → comparée au shift du Planning → heures de la semaine cumulées → contrat lié.
7–9 s : cartes : Pointages · Planning · Shifts · Contrats.
Modules affichés en cartes (7–9 s) : Pointages · Planning · Shifts · Contrats
Texte à l'écran : « Pointage : la vérité à la seconde. »
Voix off de l'épisode (démarre à 4,6 s, finie avant 11,0 s) : « Les heures, on ne les discute plus, on les voit. Pointage, planning et contrat au même endroit. »
SFX : sifflet court, tick, impact final.

RÈGLES : L'animation se comprend sans le son. Texte ≥ 64 px, ≤ 6 mots par écran, zone sûre TikTok/Reels/Shorts (marges 220 px haut, 320 px bas, 120 px côtés). Jamais de faux texte d'interface : uniquement les libellés réels. Deux lignes de voix off : la punchline de transition à 2,1 s, puis la voix de l'épisode à 4,6 s, terminée avant 11,0 s. Un SFX par apparition ; motion blur sur les zooms. Rendu premium SaaS, humoristique, moderne, lisible sur smartphone.

SORTIES : ep11-outro.mp4 · ep11-outro-muet.mp4 · ep11-thumb.png
Titre de la miniature : « La VAR ».
```

## Contrôle avant publication

- [ ] Michael : même visage, même coiffure, même tenue sur les deux scènes.
- [ ] Aucun texte lisible généré par Seedance (enseigne, ticket, écran, sous-titre).
- [ ] Chaque réplique est compréhensible sans sous-titres.
- [ ] La chute est claire avant la fin de la scène 2 et Michael regarde la caméra.
- [ ] Le clap « COUPEZ ! » arrive à 0,4 s de l'outro.
- [ ] Modules affichés : Pointages · Planning · Shifts · Contrats — libellés réels vérifiés.
- [ ] Logo FoodEatUp intact, centré, seul à l'écran de 9 à 10 s.
- [ ] La vidéo se comprend sans le son.

---
Source : `episodes/` + `saison.json` — fiche générée par `scripts/build.mjs`, ne pas éditer à la main.
