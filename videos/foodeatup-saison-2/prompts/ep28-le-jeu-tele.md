# ÉPISODE 28 — « LE JEU TÉLÉ »

🎬 **Genre** : Jeu télévisé (animateur, roue, applaudissements)
🍽️ **Situation** : La roue cadeaux s'emballe, trente desserts à faire
⚙️ **Module** : Fidélité + Roue cadeaux
🎯 **Hook (0–2 s)** : Lumières de plateau, un poivrier en guise de micro : « Faites tourner la roue ! »

## Sélecteurs Higgsfield

| Époque | Genre | Lumière | Physique | Objectif | Émotion | Montage |
|---|---|---|---|---|---|---|
| 2020s | divertissement télé | projecteurs colorés, angle frontal | hyperbolique | 24 mm | euphorie → gêne | 4 plans |

> Le look du film se règle dans ces sélecteurs : ne le répétez pas dans le texte du prompt.

## SEEDANCE 01 — Faites tourner la roue

*La salle entière veut jouer, la roue s'envole comme un frisbee*

```text
REF: Michael = @Image 1 (face, hair, build) + @Image 2 (season outfit), keep identical. Location = @Image 3 (bar).
FORMAT: 9:16, 10 s, 4 shots, realistic comedy shot like a TV game show.
SCENE: Game-show lights over the bar, a colourful prize wheel on the counter, Michael as host holding a pepper grinder like a microphone.
ACTION:
0–2 s: Michael invites the room to play; applause.
2–5 s: an adult customer spins; tick-tick-tick; the wheel stops; Michael announces a dessert; cheers.
5–8 s: the whole room stands up at once; a queue forms at the wheel; it spins faster and faster.
8–10 s: the wheel detaches and flies across the room like a frisbee in slow motion; Michael watches it go.
DIALOGUE (spoken French, slow and clear, natural lip-sync, no captions): Michael: « Faites tourner la roue ! » Michael: « Un dessert ! » Michael: « Oh. »
CAMERA: wide with lights → close-up on the wheel ticking → wide on the crowd rising → slow-motion tracking on the flying wheel.
LIGHT & GRADE: saturated coloured spotlights, glitter, TV sheen.
AUDIO: game-show jingle (original), wheel ticking, applause, crowd surge, whoosh, distant crash.
PHYSICS: realistic body weight, no morphing, no sliding feet, correct hands and fingers, no extra limbs. SKIN: preserve Michael's natural skin and features from @Image 1, no smoothing, no plastic look. NO-IP: no brands, no logos, no readable text, no captions or subtitles, no recognizable songs, no real celebrity likeness, no minors. Keep Michael's face, hair, build and outfit identical through the whole clip. Sharp, clean, cinematic render.
```

## SEEDANCE 02 — Trente

*La roue plantée dans le mur, le chef devant trente coupes*

```text
REF: Michael = @Image 1 (face, hair, build) + @Image 2 (season outfit), keep identical. Location = @Image 4.
FORMAT: 9:16, 10 s, 4 shots, realistic comedy shot like a TV game show gone wrong.
SCENE: The wheel stuck in the wall; then the kitchen: an adult chef facing thirty empty dessert glasses.
ACTION:
0–2 s: Michael looks at the wheel embedded in the wall.
2–5 s: kitchen: the chef states the number; Michael minimises; the chef repeats.
5–8 s: fast montage: Michael helps, whipped cream everywhere, slow motion on a falling cherry.
8–10 s: Michael, cream on his nose, looks at the camera.
DIALOGUE (spoken French, slow and clear, natural lip-sync, no captions): Chef: « Trente. » Michael: « C'était pour le fun. » Chef: « Trente. » Michael: « Le stock aussi, il joue. »
CAMERA: insert on the wheel → two-shot → speed-ramped montage with a slow-motion cherry → close-up.
LIGHT & GRADE: bar lights, then cold kitchen light, cream bright white.
AUDIO: wall creak, silence, whipped cream siphon, cherry plop in slow motion, sigh.
PHYSICS: realistic body weight, no morphing, no sliding feet, correct hands and fingers, no extra limbs. SKIN: preserve Michael's natural skin and features from @Image 1, no smoothing, no plastic look. NO-IP: no brands, no logos, no readable text, no captions or subtitles, no recognizable songs, no real celebrity likeness, no minors. Keep Michael's face, hair, build and outfit identical through the whole clip. Sharp, clean, cinematic render.
```

## CLAUDE CODE — 10 s (outro ep28)

**Voix off** : « La roue tourne, les lots sont limités, le stock suit. La fidélité FoodEatUp, c'est du jeu avec des règles. »

> ⚠️ Cette phrase dépasse la fenêtre de 7 s (2,0 s → 9,0 s) à débit posé.
> **Variante courte proposée** : « La roue tourne, les lots sont limités, le stock suit. La fidélité FoodEatUp, c'est réglé. »

```text
Tu es motion designer. Crée avec Remotion (React) une composition verticale 1080×1920, 30 fps,
300 images (10 s), export MP4 H.264, fichier ep28-outro.mp4.

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
2–4 s : la roue plantée dans le mur se redresse en roue numérique avec des lots définis et un nombre de lancers.
4–7 s : écran Fidélité : programme actif, points par visite, récompenses (plat réel à 0 €, quantité limitée), Roue cadeaux en ligne avec ses lots et ses leads ; un bon gagné est validé en salle en un tap.
7–9 s : cartes : Fidélité · Récompenses · Roue cadeaux · Bons · Stock.
Modules affichés en cartes (7–9 s) : Fidélité · Récompenses · Roue cadeaux · Bons · Stock
Texte à l'écran : « La roue tourne. Le stock suit. »
Voix off (démarre à 2,0 s, finie avant 9,0 s) : « La roue tourne, les lots sont limités, le stock suit. La fidélité FoodEatUp, c'est du jeu avec des règles. »
SFX : tick de roue, ding de gain, impact final.

RÈGLES : L'animation se comprend sans le son. Texte ≥ 64 px, ≤ 6 mots par écran, zone sûre TikTok/Reels/Shorts (marges 220 px haut, 320 px bas, 120 px côtés). Jamais de faux texte d'interface : uniquement les libellés réels. La voix off démarre à 2,0 s et finit avant 9,0 s. Un SFX par apparition ; motion blur sur les zooms. Rendu premium SaaS, humoristique, moderne, lisible sur smartphone.

SORTIES : ep28-outro.mp4 · ep28-outro-muet.mp4 · ep28-thumb.png
Titre de la miniature : « Le jeu télé ».
```

## Contrôle avant publication

- [ ] Michael : même visage, même coiffure, même tenue sur les deux scènes.
- [ ] Aucun texte lisible généré par Seedance (enseigne, ticket, écran, sous-titre).
- [ ] Chaque réplique est compréhensible sans sous-titres.
- [ ] La chute est claire avant la fin de la scène 2 et Michael regarde la caméra.
- [ ] Le clap « COUPEZ ! » arrive à 0,4 s de l'outro.
- [ ] Modules affichés : Fidélité · Récompenses · Roue cadeaux · Bons · Stock — libellés réels vérifiés.
- [ ] Logo FoodEatUp intact, centré, seul à l'écran de 9 à 10 s.
- [ ] La vidéo se comprend sans le son.

---
Source : `episodes/` + `saison.json` — fiche générée par `scripts/build.mjs`, ne pas éditer à la main.
