# ÉPISODE 10 — « LA BOUCLE »

🎬 **Genre** : Boucle temporelle
🍽️ **Situation** : Chaque matin, Michael recompte le stock à la main, et le chiffre change
⚙️ **Module** : Stock
🎯 **Hook (0–2 s)** : Réveil à six heures, Michael compte les bouteilles du doigt… puis le réveil sonne à nouveau.

## Sélecteurs Higgsfield

| Époque | Genre | Lumière | Physique | Objectif | Émotion | Montage |
|---|---|---|---|---|---|---|
| 2020s | comédie fantastique | néon de réserve, angle frontal | réaliste | 35 mm | lassitude croissante | 4 plans |

> Le look du film se règle dans ces sélecteurs : ne le répétez pas dans le texte du prompt.

## SEEDANCE 01 — Encore ?

*Même réveil, même geste, jamais le même chiffre*

```text
REF: Michael = @Image 1 (face, hair, build) + @Image 2 (season outfit), keep identical. Location = @Image 4 (storeroom side).
FORMAT: 9:16, 10 s, 4 shots, realistic comedy shot like a time-loop movie.
SCENE: A storeroom shelf lined with identical bottles; an alarm clock on a crate; Michael with a pencil and a paper pad.
ACTION:
0–2 s: the alarm rings, Michael sits up from a nap on a flour sack and starts counting bottles with his finger.
2–5 s: he counts out loud, writes a number.
5–8 s: hard cut: the alarm rings again, same posture, same bottles, he counts again and gets a different number; hard cut: alarm again, another number.
8–10 s: he turns very slowly toward the camera.
DIALOGUE (spoken French, slow and clear, natural lip-sync, no captions): Michael: « Un, deux, trois… douze. » Michael: « …onze ? » Michael: « …quinze ?! » Michael: « Encore ? »
CAMERA: medium → insert on the finger counting → three identical jump-cuts → slow turn into close-up.
LIGHT & GRADE: flat fluorescent, slightly green, identical framing on every loop.
AUDIO: same alarm ring three times, pencil scratch, bottle clink, a comic bass note on the turn.
PHYSICS: realistic body weight, no morphing, no sliding feet, correct hands and fingers, no extra limbs. SKIN: preserve Michael's natural skin and features from @Image 1, no smoothing, no plastic look. NO-IP: no brands, no logos, no readable text, no captions or subtitles, no recognizable songs, no real celebrity likeness, no minors. Keep Michael's face, hair, build and outfit identical through the whole clip. Sharp, clean, cinematic render.
```

## SEEDANCE 02 — Je sors pas

*Il essaie de casser la boucle, le mur redevient propre*

```text
REF: Michael = @Image 1 (face, hair, build) + @Image 2 (season outfit), keep identical. Location = @Image 4 (storeroom side).
FORMAT: 9:16, 10 s, 4 shots, realistic comedy shot like a time-loop movie.
SCENE: Same storeroom, same shelf, same alarm clock.
ACTION:
0–2 s: Michael counts the bottles backwards, then counts while hopping on one foot.
2–5 s: he writes a big number on the wall with a marker (unreadable scribble); hard cut: the alarm rings, the wall is clean, he stares at it.
5–8 s: he slides down and sits on the floor, resigned; a bottle rolls off the shelf and stops against his shoe.
8–10 s: he looks at the bottle, then at the camera; the alarm rings again.
DIALOGUE (spoken French, slow and clear, natural lip-sync, no captions): Michael: « Je sors pas. » Michael: « Treize. »
CAMERA: medium with hop → insert on the marker → match-cut to clean wall → low angle on the floor, bottle rolls in.
LIGHT & GRADE: flat fluorescent, faint dawn light through a vent at the end.
AUDIO: hop thuds, marker squeak, alarm, bottle rolling, alarm again, silence.
PHYSICS: realistic body weight, no morphing, no sliding feet, correct hands and fingers, no extra limbs. SKIN: preserve Michael's natural skin and features from @Image 1, no smoothing, no plastic look. NO-IP: no brands, no logos, no readable text, no captions or subtitles, no recognizable songs, no real celebrity likeness, no minors. Keep Michael's face, hair, build and outfit identical through the whole clip. Sharp, clean, cinematic render.
```

## CLAUDE CODE — 12 s (outro ep10 : 2 s de transition + 10 s d'animation)

**Voix off — transition** (commune aux 30 épisodes, à 2,1 s) : « Cette scène aurait pu être évitée ? »

**Voix off — épisode** (à 4,6 s) : « Comptez une fois. FoodEatUp compte le reste, à chaque vente, à chaque livraison. »

```text
Tu es motion designer. Crée avec Remotion (React) une composition verticale 1080×1920, 30 fps,
300 images (10 s), export MP4 H.264, fichier ep10-outro.mp4.

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
2–4 s : le réveil se fige ; les bouteilles se rangent en une ligne de stock : quantité, seuil, niveau.
4–7 s : écran Stock : une vente encaissée → le stock baisse tout seul ; une réception validée → il remonte ; sous le seuil, une alerte « stock bas » s'allume.
7–9 s : cartes : Stock · Ingrédients · Réception · Notifications.
Modules affichés en cartes (7–9 s) : Stock · Ingrédients · Réception · Notifications
Texte à l'écran : « Le stock se compte tout seul. »
Voix off de l'épisode (démarre à 4,6 s, finie avant 11,0 s) : « Comptez une fois. FoodEatUp compte le reste, à chaque vente, à chaque livraison. »
SFX : tick par mouvement, alerte douce, impact final.

RÈGLES : L'animation se comprend sans le son. Texte ≥ 64 px, ≤ 6 mots par écran, zone sûre TikTok/Reels/Shorts (marges 220 px haut, 320 px bas, 120 px côtés). Jamais de faux texte d'interface : uniquement les libellés réels. Deux lignes de voix off : la punchline de transition à 2,1 s, puis la voix de l'épisode à 4,6 s, terminée avant 11,0 s. Un SFX par apparition ; motion blur sur les zooms. Rendu premium SaaS, humoristique, moderne, lisible sur smartphone.

SORTIES : ep10-outro.mp4 · ep10-outro-muet.mp4 · ep10-thumb.png
Titre de la miniature : « La boucle ».
```

## Contrôle avant publication

- [ ] Michael : même visage, même coiffure, même tenue sur les deux scènes.
- [ ] Aucun texte lisible généré par Seedance (enseigne, ticket, écran, sous-titre).
- [ ] Chaque réplique est compréhensible sans sous-titres.
- [ ] La chute est claire avant la fin de la scène 2 et Michael regarde la caméra.
- [ ] Le clap « COUPEZ ! » arrive à 0,4 s de l'outro.
- [ ] Modules affichés : Stock · Ingrédients · Réception · Notifications — libellés réels vérifiés.
- [ ] Logo FoodEatUp intact, centré, seul à l'écran de 9 à 10 s.
- [ ] La vidéo se comprend sans le son.

---
Source : `episodes/` + `saison.json` — fiche générée par `scripts/build.mjs`, ne pas éditer à la main.
