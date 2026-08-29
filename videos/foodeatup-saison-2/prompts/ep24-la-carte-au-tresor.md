# ÉPISODE 24 — « LA CARTE AU TRÉSOR »

🎬 **Genre** : Film d'aventure (la carte qui s'envole)
🍽️ **Situation** : La commande notée sur une serviette part avec le vent
⚙️ **Module** : Commandes numériques + Écran cuisine
🎯 **Hook (0–2 s)** : « Table six. Deux pizzas. » — rafale, la serviette s'envole : « Attends ! »

## Sélecteurs Higgsfield

| Époque | Genre | Lumière | Physique | Objectif | Émotion | Montage |
|---|---|---|---|---|---|---|
| 2020s | aventure | jour venteux, angle bas | réaliste | 24 mm caméra à l'épaule | poursuite héroïque | 4 plans |

> Le look du film se règle dans ces sélecteurs : ne le répétez pas dans le texte du prompt.

## SEEDANCE 01 — Attends !

*La serviette traverse la rue, la fontaine, un chien l'attrape au vol*

```text
REF: Michael = @Image 1 (face, hair, build) + @Image 2 (season outfit), keep identical. Location = @Image 3 (windy terrace) then a town square with a fountain.
FORMAT: 9:16, 10 s, 4 shots, realistic comedy shot like an adventure movie.
SCENE: Windy terrace; Michael scribbles an order on a paper napkin (abstract scribbles, no readable words).
ACTION:
0–2 s: he repeats the order while writing; a gust rips the napkin from his hand; he shouts.
2–5 s: adventure music; he chases the napkin down the street; it slips between two passers-by, under a parked car, onto a passing bicycle.
5–8 s: the napkin lands on the rim of a fountain; Michael climbs the edge in slow motion, fingertips brushing the paper.
8–10 s: a dog snatches it mid-air and bolts; Michael freezes.
DIALOGUE (spoken French, slow and clear, natural lip-sync, no captions): Michael: « Table six. Deux pizzas. » Michael: « Attends ! » Michael: « Non. »
CAMERA: insert on the napkin → handheld chase tracking → slow-motion low angle at the fountain → freeze on Michael.
LIGHT & GRADE: bright windy daylight, dynamic shadows, slight motion blur.
AUDIO: wind gust, adventure brass (original), footsteps, bicycle bell, fountain splash, dog bark, silence.
PHYSICS: realistic body weight, no morphing, no sliding feet, correct hands and fingers, no extra limbs. SKIN: preserve Michael's natural skin and features from @Image 1, no smoothing, no plastic look. NO-IP: no brands, no logos, no readable text, no captions or subtitles, no recognizable songs, no real celebrity likeness, no minors. Keep Michael's face, hair, build and outfit identical through the whole clip. Sharp, clean, cinematic render.
```

## SEEDANCE 02 — Trois

*Négociation avec le chien, la serviette illisible, le retour héroïque*

```text
REF: Michael = @Image 1 (face, hair, build) + @Image 2 (season outfit), keep identical. Location = town square, then @Image 3.
FORMAT: 9:16, 10 s, 4 shots, realistic comedy shot like an adventure movie.
SCENE: Michael on all fours on the square, face to face with the dog holding the napkin.
ACTION:
0–2 s: standoff with the dog; Michael holds out his hand and asks.
2–5 s: he pulls a piece of bread from his pocket; slow-motion exchange; the dog trots off.
5–8 s: he unfolds the napkin: the ink has run, it is a blue smear; heroic slow-motion walk back into the restaurant, out of breath.
8–10 s: at table six, a customer asks; Michael guesses; the dog trots past the window with another napkin.
DIALOGUE (spoken French, slow and clear, natural lip-sync, no captions): Michael: « Donne. » Customer: « On avait dit deux pizzas ? » Michael: « …trois. »
CAMERA: low two-shot with the dog → macro on the exchange → slow-motion tracking → medium at the table, window in the background.
LIGHT & GRADE: bright daylight, warm interior at the end.
AUDIO: dog panting, bread rustle, slow-motion whoosh, heavy breathing, chair creak, dog nails on pavement.
PHYSICS: realistic body weight, no morphing, no sliding feet, correct hands and fingers, no extra limbs. SKIN: preserve Michael's natural skin and features from @Image 1, no smoothing, no plastic look. NO-IP: no brands, no logos, no readable text, no captions or subtitles, no recognizable songs, no real celebrity likeness, no minors. Keep Michael's face, hair, build and outfit identical through the whole clip. Sharp, clean, cinematic render.
```

## CLAUDE CODE — 10 s (outro ep24)

**Voix off** : « Une commande, ça ne s'envole pas. Avec FoodEatUp, elle part de la table à la cuisine en une seconde. »

```text
Tu es motion designer. Crée avec Remotion (React) une composition verticale 1080×1920, 30 fps,
300 images (10 s), export MP4 H.264, fichier ep24-outro.mp4.

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
2–4 s : la serviette bleue délavée se reconstitue en commande numérique : table, articles, quantités, options.
4–7 s : écran Commandes : prise de commande sur téléphone à la table → envoi en un tap → la commande apparaît sur l'Écran cuisine, rangée par poste.
7–9 s : cartes : Commandes · Écran cuisine · Tables · Postes.
Modules affichés en cartes (7–9 s) : Commandes · Écran cuisine · Tables · Postes
Texte à l'écran : « De la table à la cuisine. Sans serviette. »
Voix off (démarre à 2,0 s, finie avant 9,0 s) : « Une commande, ça ne s'envole pas. Avec FoodEatUp, elle part de la table à la cuisine en une seconde. »
SFX : whoosh d'envoi, ping cuisine, impact final.

RÈGLES : L'animation se comprend sans le son. Texte ≥ 64 px, ≤ 6 mots par écran, zone sûre TikTok/Reels/Shorts (marges 220 px haut, 320 px bas, 120 px côtés). Jamais de faux texte d'interface : uniquement les libellés réels. La voix off démarre à 2,0 s et finit avant 9,0 s. Un SFX par apparition ; motion blur sur les zooms. Rendu premium SaaS, humoristique, moderne, lisible sur smartphone.

SORTIES : ep24-outro.mp4 · ep24-outro-muet.mp4 · ep24-thumb.png
Titre de la miniature : « La carte au trésor ».
```

## Contrôle avant publication

- [ ] Michael : même visage, même coiffure, même tenue sur les deux scènes.
- [ ] Aucun texte lisible généré par Seedance (enseigne, ticket, écran, sous-titre).
- [ ] Chaque réplique est compréhensible sans sous-titres.
- [ ] La chute est claire avant la fin de la scène 2 et Michael regarde la caméra.
- [ ] Le clap « COUPEZ ! » arrive à 0,4 s de l'outro.
- [ ] Modules affichés : Commandes · Écran cuisine · Tables · Postes — libellés réels vérifiés.
- [ ] Logo FoodEatUp intact, centré, seul à l'écran de 9 à 10 s.
- [ ] La vidéo se comprend sans le son.

---
Source : `episodes/` + `saison.json` — fiche générée par `scripts/build.mjs`, ne pas éditer à la main.
