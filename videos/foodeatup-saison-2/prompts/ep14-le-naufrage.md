# ÉPISODE 14 — « LE NAUFRAGE »

🎬 **Genre** : Film catastrophe maritime
🍽️ **Situation** : Quarante clients en terrasse, orage soudain, douze chaises à l'intérieur
⚙️ **Module** : Plan de salle (zones Terrasse / Salle)
🎯 **Hook (0–2 s)** : « Belle journée. » — une goutte sur le nez.

## Sélecteurs Higgsfield

| Époque | Genre | Lumière | Physique | Objectif | Émotion | Montage |
|---|---|---|---|---|---|---|
| 2020s | catastrophe | soleil puis ciel noir, angle bas | hyperbolique | 24 mm caméra à l'épaule | calme → survie | 4 plans |

> Le look du film se règle dans ces sélecteurs : ne le répétez pas dans le texte du prompt.

## SEEDANCE 01 — Tout le monde à l'intérieur

*Le ciel noircit en deux secondes, les parasols s'envolent*

```text
REF: Michael = @Image 1 (face, hair, build) + @Image 2 (season outfit), keep identical. Location = @Image 3 (terrace side).
FORMAT: 9:16, 10 s, 4 shots, realistic comedy shot like a maritime disaster movie.
SCENE: A sunny terrace full of adult customers, parasols, glasses of rosé; Michael stands like a ship's captain, hands behind his back.
ACTION:
0–2 s: Michael admires the day and speaks; a single raindrop lands on his nose.
2–5 s: time-lapse: the sky turns black in two seconds, thunder, the wind rises.
5–8 s: downpour: parasols lift off, tablecloths fly, a plate floats across the terrace, customers run toward the door like a lifeboat; Michael holds the door open like a hatch, hair plastered.
8–10 s: Michael shouts over the wind.
DIALOGUE (spoken French, slow and clear, natural lip-sync, no captions): Michael: « Belle journée. » Michael (shouting): « Tout le monde à l'intérieur ! »
CAMERA: medium on Michael → sky time-lapse tilt → handheld chaos with rain on the lens → low angle at the door.
LIGHT & GRADE: golden sun turning to storm grey-green, lightning flashes.
AUDIO: seagull, one raindrop, thunder crack, wind roar, rain on tables, parasol flapping, screams of laughter.
PHYSICS: realistic body weight, no morphing, no sliding feet, correct hands and fingers, no extra limbs. SKIN: preserve Michael's natural skin and features from @Image 1, no smoothing, no plastic look. NO-IP: no brands, no logos, no readable text, no captions or subtitles, no recognizable songs, no real celebrity likeness, no minors. Keep Michael's face, hair, build and outfit identical through the whole clip. Sharp, clean, cinematic render.
```

## SEEDANCE 02 — Presque

*Quarante clients trempés, douze chaises, Michael agent de piste*

```text
REF: Michael = @Image 1 (face, hair, build) + @Image 2 (season outfit), keep identical. Location = @Image 3.
FORMAT: 9:16, 10 s, 4 shots, realistic comedy shot like a maritime disaster movie.
SCENE: Inside: forty soaked adult customers, twelve chairs, water on the floor, rain hammering the windows.
ACTION:
0–2 s: wide on the dripping crowd; Michael raises two forks like airport marshalling batons.
2–5 s: he directs traffic: two here, four there; a customer sits on the bar, another on the radiator.
5–8 s: Michael counts heads with his finger in slow motion, asks the room; silence; outside, under an overturned parasol, one customer raises a hand.
8–10 s: Michael, dripping, looks at the camera.
DIALOGUE (spoken French, slow and clear, natural lip-sync, no captions): Michael: « Tout le monde est là ? » Michael: « Presque. »
CAMERA: wide → medium with batons → slow-motion pan across faces → rack focus through the window → close-up.
LIGHT & GRADE: cold storm light, warm lamps inside, wet reflections.
AUDIO: dripping, chair scrapes, batons whoosh, rain against glass, distant thunder, silence, drip.
PHYSICS: realistic body weight, no morphing, no sliding feet, correct hands and fingers, no extra limbs. SKIN: preserve Michael's natural skin and features from @Image 1, no smoothing, no plastic look. NO-IP: no brands, no logos, no readable text, no captions or subtitles, no recognizable songs, no real celebrity likeness, no minors. Keep Michael's face, hair, build and outfit identical through the whole clip. Sharp, clean, cinematic render.
```

## CLAUDE CODE — 10 s (outro ep14)

**Voix off** : « La terrasse ferme, la salle s'organise. Avec le plan de salle FoodEatUp, vous replacez tout le monde en trente secondes. »

> ⚠️ Cette phrase dépasse la fenêtre de 7 s (2,0 s → 9,0 s) à débit posé.
> **Variante courte proposée** : « La terrasse ferme, la salle s'organise. Avec FoodEatUp, vous replacez tout le monde en trente secondes. »

```text
Tu es motion designer. Crée avec Remotion (React) une composition verticale 1080×1920, 30 fps,
300 images (10 s), export MP4 H.264, fichier ep14-outro.mp4.

Entrées dans ./assets :
- logo-foodeatup.svg : logo officiel. Ne jamais le redessiner, le déformer, le recolorer, le rogner.
  Zone de protection = 10 % de sa largeur.
- palette.json : couleurs officielles de la charte FoodEatUp (exportées du CMS). Seules couleurs
  autorisées, aucune couleur inventée.
- scene2-last-frame.png : dernière image de la scène Seedance 2 (extraite avec ffmpeg).
- vo.mp3 : voix off de l'épisode (ElevenLabs, même voix sur toute la saison).
- sfx/ : clap.wav, whoosh.wav, tick.wav, impact.wav.

STRUCTURE IMPOSÉE (identique sur les 30 épisodes — c'est la signature de la saison) :
0–2 s : scene2-last-frame plein écran, léger zoom avant, désaturation progressive ; clap de cinéma qui entre par le bas et claque à 0,4 s (SFX clap) ; texte « COUPEZ ! » ; à 1,6 s « Dans la vraie vie… ».
2–4 s : L'élément clé de la scène se transforme en données (motion blur, particules légères, easing expo-out) — précisé par épisode.
4–7 s : Démonstration du bénéfice : maquette d'écran FoodEatUp en 3D légère (rotation ≤ 8°), micro-animations, action en UN tap, ralenti de 6 images sur le tap.
7–9 s : Les modules concernés apparaissent en cartes reliées par des flux lumineux (libellés réels uniquement).
9–10 s : Tout disparaît ; logo FoodEatUp seul, centré, scale 0,9 → 1 + halo ; signature sous le logo ; SFX impact + whoosh ; fondu.

CONTENU DE CET ÉPISODE :
2–4 s : la terrasse trempée se transforme en zone du plan de salle qui passe en « fermée » ; les groupes deviennent des jetons.
4–7 s : écran Plan de salle : zones Terrasse et Salle ; tables par statut (libre, réservée, occupée) ; un groupe glissé de la terrasse vers une table de salle en un geste.
7–9 s : cartes : Plan de salle · Zones · Tables · Réservations.
Modules affichés en cartes (7–9 s) : Plan de salle · Zones · Tables · Réservations
Texte à l'écran : « Terrasse ou salle : tout le monde a sa place. »
Voix off (démarre à 2,0 s, finie avant 9,0 s) : « La terrasse ferme, la salle s'organise. Avec le plan de salle FoodEatUp, vous replacez tout le monde en trente secondes. »
SFX : goutte, glissement, tick par table, impact final.

RÈGLES : L'animation se comprend sans le son. Texte ≥ 64 px, ≤ 6 mots par écran, zone sûre TikTok/Reels/Shorts (marges 220 px haut, 320 px bas, 120 px côtés). Jamais de faux texte d'interface : uniquement les libellés réels. La voix off démarre à 2,0 s et finit avant 9,0 s. Un SFX par apparition ; motion blur sur les zooms. Rendu premium SaaS, humoristique, moderne, lisible sur smartphone.

SORTIES : ep14-outro.mp4 · ep14-outro-muet.mp4 · ep14-thumb.png
Titre de la miniature : « Le naufrage ».
```

## Contrôle avant publication

- [ ] Michael : même visage, même coiffure, même tenue sur les deux scènes.
- [ ] Aucun texte lisible généré par Seedance (enseigne, ticket, écran, sous-titre).
- [ ] Chaque réplique est compréhensible sans sous-titres.
- [ ] La chute est claire avant la fin de la scène 2 et Michael regarde la caméra.
- [ ] Le clap « COUPEZ ! » arrive à 0,4 s de l'outro.
- [ ] Modules affichés : Plan de salle · Zones · Tables · Réservations — libellés réels vérifiés.
- [ ] Logo FoodEatUp intact, centré, seul à l'écran de 9 à 10 s.
- [ ] La vidéo se comprend sans le son.

---
Source : `episodes/` + `saison.json` — fiche générée par `scripts/build.mjs`, ne pas éditer à la main.
