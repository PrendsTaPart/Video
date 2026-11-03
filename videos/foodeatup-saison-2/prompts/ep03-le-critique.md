# ÉPISODE 03 — « LE CRITIQUE »

🎬 **Genre** : Film d'espionnage (paranoïa)
🍽️ **Situation** : Le critique anonyme est dans la salle… ou pas
⚙️ **Module** : Avis
🎯 **Hook (0–2 s)** : Michael observe la salle à travers une passoire : « Il est là. »

## Sélecteurs Higgsfield

| Époque | Genre | Lumière | Physique | Objectif | Émotion | Montage |
|---|---|---|---|---|---|---|
| 2020s | espionnage | contrastée, angle latéral | réaliste | 85 mm téléobjectif | suspicion | 4 plans |

> Le look du film se règle dans ces sélecteurs : ne le répétez pas dans le texte du prompt.

## SEEDANCE 01 — C'est lui

*Tout le monde est suspect, Michael sert le chapeau avec révérence*

```text
REF: Michael = @Image 1 (face, hair, build) + @Image 2 (season outfit), keep identical. Location = @Image 3.
FORMAT: 9:16, 10 s, 4 shots, realistic comedy shot like a spy thriller.
SCENE: A full dining room at lunch. Michael crouches behind the bar and looks at the room through a metal colander held like binoculars.
ACTION:
0–2 s: colander POV with round holes, Michael whispers.
2–5 s: hidden-camera style snap zooms on three adult customers: a woman writing in a notebook, a man photographing his plate, a man alone in a hat; Michael names each one.
5–8 s: Michael serves the man in the hat with an exaggerated bow, straightens the fork by a millimetre, blows on the glass.
8–10 s: the man looks up and asks something simple; Michael sprints away in slow motion.
DIALOGUE (spoken French, slow and clear, natural lip-sync, no captions): Michael (whisper): « Il est là. » Michael: « C'est lui. Non. Elle. Le chapeau ! » Man in hat: « Le sel ? » Michael: « Tout de suite. »
CAMERA: colander POV → three snap zooms → medium on the bow → slow-motion tracking as he runs.
LIGHT & GRADE: contrasty window light, teal shadows, warm highlights.
AUDIO: spy bass line (original), camera shutter clicks, glass hum, whispered lines, slow-motion whoosh.
PHYSICS: realistic body weight, no morphing, no sliding feet, correct hands and fingers, no extra limbs. SKIN: preserve Michael's natural skin and features from @Image 1, no smoothing, no plastic look. NO-IP: no brands, no logos, no readable text, no captions or subtitles, no recognizable songs, no real celebrity likeness, no minors. Keep Michael's face, hair, build and outfit identical through the whole clip. Sharp, clean, cinematic render.
```

## SEEDANCE 02 — Une étoile

*Le vrai critique était le livreur qui attendait dehors*

```text
REF: Michael = @Image 1 (face, hair, build) + @Image 2 (season outfit), keep identical. Location = @Image 3.
FORMAT: 9:16, 10 s, 4 shots, realistic comedy shot like a spy thriller.
SCENE: End of service, chairs on tables, Michael leaning on the bar, exhausted and proud, phone in hand.
ACTION:
0–2 s: Michael exhales and smiles at the room.
2–5 s: his phone buzzes; a blurred notification with a single star glows on the screen (no readable text); his smile freezes.
5–8 s: ultra-fast flashback: an adult courier with a bike helmet waiting at the glass door for a long time, checking his watch, while Michael bows in the background.
8–10 s: back to Michael; he drops the colander; crash zoom.
DIALOGUE (spoken French, slow and clear, natural lip-sync, no captions): Michael: « C'était parfait. » Michael: « Une étoile. » (beat) « Le livreur. »
CAMERA: medium → insert on phone → jump-cut flashback in handheld → crash zoom on face.
LIGHT & GRADE: evening practicals, warm bar light, flashback slightly desaturated.
AUDIO: phone buzz, heartbeat, rewind sound for the flashback, colander clang, sting.
PHYSICS: realistic body weight, no morphing, no sliding feet, correct hands and fingers, no extra limbs. SKIN: preserve Michael's natural skin and features from @Image 1, no smoothing, no plastic look. NO-IP: no brands, no logos, no readable text, no captions or subtitles, no recognizable songs, no real celebrity likeness, no minors. Keep Michael's face, hair, build and outfit identical through the whole clip. Sharp, clean, cinematic render.
```

## CLAUDE CODE — 12 s (outro ep03 : 2 s de transition + 10 s d'animation)

**Voix off — transition** (commune aux 30 épisodes, à 2,1 s) : « Cette scène aurait pu être évitée ? »

**Voix off — épisode** (à 4,6 s) : « Le vrai critique, c'est chaque client. FoodEatUp réunit tous vos avis et vous aide à répondre. »

```text
Tu es motion designer. Crée avec Remotion (React) une composition verticale 1080×1920, 30 fps,
300 images (10 s), export MP4 H.264, fichier ep03-outro.mp4.

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
2–4 s : la notification de Michael se multiplie en dizaines d'étoiles qui se rangent en liste.
4–7 s : écran Avis : avis du site et de Google au même endroit, note, statut ; une réponse s'écrit en un tap ; l'avis passe en « répondu ».
7–9 s : cartes : Avis · Clients · Site vitrine.
Modules affichés en cartes (7–9 s) : Avis · Clients · Site vitrine
Texte à l'écran : « Tous les avis. Une réponse. »
Voix off de l'épisode (démarre à 4,6 s, finie avant 11,0 s) : « Le vrai critique, c'est chaque client. FoodEatUp réunit tous vos avis et vous aide à répondre. »
SFX : ding par étoile, whoosh de réponse, impact final.

RÈGLES : L'animation se comprend sans le son. Texte ≥ 64 px, ≤ 6 mots par écran, zone sûre TikTok/Reels/Shorts (marges 220 px haut, 320 px bas, 120 px côtés). Jamais de faux texte d'interface : uniquement les libellés réels. Deux lignes de voix off : la punchline de transition à 2,1 s, puis la voix de l'épisode à 4,6 s, terminée avant 11,0 s. Un SFX par apparition ; motion blur sur les zooms. Rendu premium SaaS, humoristique, moderne, lisible sur smartphone.

SORTIES : ep03-outro.mp4 · ep03-outro-muet.mp4 · ep03-thumb.png
Titre de la miniature : « Le critique ».
```

## Contrôle avant publication

- [ ] Michael : même visage, même coiffure, même tenue sur les deux scènes.
- [ ] Aucun texte lisible généré par Seedance (enseigne, ticket, écran, sous-titre).
- [ ] Chaque réplique est compréhensible sans sous-titres.
- [ ] La chute est claire avant la fin de la scène 2 et Michael regarde la caméra.
- [ ] Le clap « COUPEZ ! » arrive à 0,4 s de l'outro.
- [ ] Modules affichés : Avis · Clients · Site vitrine — libellés réels vérifiés.
- [ ] Logo FoodEatUp intact, centré, seul à l'écran de 9 à 10 s.
- [ ] La vidéo se comprend sans le son.

---
Source : `episodes/` + `saison.json` — fiche générée par `scripts/build.mjs`, ne pas éditer à la main.
