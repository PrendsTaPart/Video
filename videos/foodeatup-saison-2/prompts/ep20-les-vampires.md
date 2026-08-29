# ÉPISODE 20 — « LES VAMPIRES »

🎬 **Genre** : Film de vampires
🍽️ **Situation** : Happy hour — ils sortent quand le soleil se couche
⚙️ **Module** : Happy hours + Boissons
🎯 **Hook (0–2 s)** : Bar vide, Michael astique un verre : « Happy hour. » — silence, une chips tombe.

## Sélecteurs Higgsfield

| Époque | Genre | Lumière | Physique | Objectif | Émotion | Montage |
|---|---|---|---|---|---|---|
| 2020s | horreur gothique | coucher de soleil puis néon bleu, angle bas | réaliste | anamorphique 50 mm | effroi élégant | 4 plans |

> Le look du film se règle dans ces sélecteurs : ne le répétez pas dans le texte du prompt.

## SEEDANCE 01 — Ils sortent la nuit

*Les bureaux se vident au coucher du soleil, l'ail ne marche pas*

```text
REF: Michael = @Image 1 (face, hair, build) + @Image 2 (season outfit), keep identical. Location = @Image 3 (bar).
FORMAT: 9:16, 10 s, 4 shots, realistic comedy shot like a vampire movie.
SCENE: Five o'clock, empty bar, golden light; Michael polishes a glass.
ACTION:
0–2 s: Michael announces the happy hour to nobody; silence; a single crisp falls from a bowl.
2–5 s: time-lapse through the window: the sun sinks, shadows stretch; Michael watches, uneasy.
5–8 s: outside, adults in office suits step out of the buildings in slow motion, ties loosened, eyes fixed on the bar's blinking lamp; Michael whispers.
8–10 s: Michael holds up… a clove of garlic; looks at it; deadpan.
DIALOGUE (spoken French, slow and clear, natural lip-sync, no captions): Michael: « Happy hour. » Michael (whisper): « Ils sortent la nuit. » Michael: « Ça marche pas. »
CAMERA: medium at the bar → window time-lapse → slow-motion low angle on the suits → close-up on the garlic.
LIGHT & GRADE: gold to deep blue dusk, neon rim light, gothic contrast.
AUDIO: glass squeak, crisp drop, organ note (original), slow footsteps, coats swishing, garlic thud.
PHYSICS: realistic body weight, no morphing, no sliding feet, correct hands and fingers, no extra limbs. SKIN: preserve Michael's natural skin and features from @Image 1, no smoothing, no plastic look. NO-IP: no brands, no logos, no readable text, no captions or subtitles, no recognizable songs, no real celebrity likeness, no minors. Keep Michael's face, hair, build and outfit identical through the whole clip. Sharp, clean, cinematic render.
```

## SEEDANCE 02 — Happy hour… fini

*Trente pressions, minuit, la salle vide d'un coup*

```text
REF: Michael = @Image 1 (face, hair, build) + @Image 2 (season outfit), keep identical. Location = @Image 3 (bar).
FORMAT: 9:16, 10 s, 4 shots, realistic comedy shot like a vampire movie.
SCENE: The door opens in a drift of mist; the suits glide in, jackets on their shoulders like capes.
ACTION:
0–2 s: mist, slow entrance, whispered orders.
2–5 s: fast montage: Michael pulls thirty pints, slow motion on overflowing foam, lemon slices flying, a shaker rattling.
5–8 s: the clock strikes midnight: they all vanish at once; the room is empty, glasses everywhere.
8–10 s: Michael alone, hair wild, a glass in hand; he sips; a small sigh.
DIALOGUE (spoken French, slow and clear, natural lip-sync, no captions): Suits (whisper): « Une pinte… » « Deux… » Michael: « Happy hour… fini. »
CAMERA: low wide with mist → speed-ramped bar montage → whip pan to the empty room → close-up, sip.
LIGHT & GRADE: blue neon, foam glowing, midnight black.
AUDIO: mist hiss, whispers, taps hissing, foam, shaker, clock chime, sudden silence, sip, sigh.
PHYSICS: realistic body weight, no morphing, no sliding feet, correct hands and fingers, no extra limbs. SKIN: preserve Michael's natural skin and features from @Image 1, no smoothing, no plastic look. NO-IP: no brands, no logos, no readable text, no captions or subtitles, no recognizable songs, no real celebrity likeness, no minors. Keep Michael's face, hair, build and outfit identical through the whole clip. Sharp, clean, cinematic render.
```

## CLAUDE CODE — 12 s (outro ep20 : 2 s de transition + 10 s d'animation)

**Voix off — transition** (commune aux 30 épisodes, à 2,1 s) : « Cette scène aurait pu être évitée ? »

**Voix off — épisode** (à 4,6 s) : « Le jour, l'heure, la remise, les boissons : tout est réglé d'avance. Quand ils sortent, FoodEatUp est déjà prêt. »

> ⚠️ Cette phrase dépasse la fenêtre de 7 s (2,0 s → 9,0 s) à débit posé.
> **Variante courte proposée** : « Le jour, l'heure, la remise : tout est réglé d'avance. Quand ils sortent, FoodEatUp est prêt. »

```text
Tu es motion designer. Crée avec Remotion (React) une composition verticale 1080×1920, 30 fps,
300 images (10 s), export MP4 H.264, fichier ep20-outro.mp4.

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
2–4 s : l'horloge devient un créneau : jours, heure de début, heure de fin, remise.
4–7 s : écran Happy hours : créneau créé en un tap, périmètre (boissons ou carte), remise appliquée automatiquement en caisse ; le stock Boissons baisse à chaque pinte.
7–9 s : cartes : Happy hours · Boissons · Caisse · Stock.
Modules affichés en cartes (7–9 s) : Happy hours · Boissons · Caisse · Stock
Texte à l'écran : « Happy hour : réglé d'avance. »
Voix off de l'épisode (démarre à 4,6 s, finie avant 11,0 s) : « Le jour, l'heure, la remise, les boissons : tout est réglé d'avance. Quand ils sortent, FoodEatUp est déjà prêt. »
SFX : tick horloge, remise « ding », impact final.

RÈGLES : L'animation se comprend sans le son. Texte ≥ 64 px, ≤ 6 mots par écran, zone sûre TikTok/Reels/Shorts (marges 220 px haut, 320 px bas, 120 px côtés). Jamais de faux texte d'interface : uniquement les libellés réels. Deux lignes de voix off : la punchline de transition à 2,1 s, puis la voix de l'épisode à 4,6 s, terminée avant 11,0 s. Un SFX par apparition ; motion blur sur les zooms. Rendu premium SaaS, humoristique, moderne, lisible sur smartphone.

SORTIES : ep20-outro.mp4 · ep20-outro-muet.mp4 · ep20-thumb.png
Titre de la miniature : « Les vampires ».
```

## Contrôle avant publication

- [ ] Michael : même visage, même coiffure, même tenue sur les deux scènes.
- [ ] Aucun texte lisible généré par Seedance (enseigne, ticket, écran, sous-titre).
- [ ] Chaque réplique est compréhensible sans sous-titres.
- [ ] La chute est claire avant la fin de la scène 2 et Michael regarde la caméra.
- [ ] Le clap « COUPEZ ! » arrive à 0,4 s de l'outro.
- [ ] Modules affichés : Happy hours · Boissons · Caisse · Stock — libellés réels vérifiés.
- [ ] Logo FoodEatUp intact, centré, seul à l'écran de 9 à 10 s.
- [ ] La vidéo se comprend sans le son.

---
Source : `episodes/` + `saison.json` — fiche générée par `scripts/build.mjs`, ne pas éditer à la main.
