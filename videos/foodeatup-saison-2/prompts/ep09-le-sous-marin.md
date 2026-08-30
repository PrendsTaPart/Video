# ÉPISODE 09 — « LE SOUS-MARIN »

🎬 **Genre** : Film de sous-marin (silence, sonar)
🍽️ **Situation** : Le coup de feu en cuisine, chaque ticket est un « ping »
⚙️ **Module** : Écran cuisine
🎯 **Hook (0–2 s)** : Cuisine en lumière rouge, une goutte tombe, un ping de sonar : « Silence. Une commande. »

## Sélecteurs Higgsfield

| Époque | Genre | Lumière | Physique | Objectif | Émotion | Montage |
|---|---|---|---|---|---|---|
| 2020s | thriller de sous-marin | rouge d'alerte + pratiques, angle bas | réaliste | 35 mm | tension chuchotée | 4 plans |

> Le look du film se règle dans ces sélecteurs : ne le répétez pas dans le texte du prompt.

## SEEDANCE 01 — Ping

*Tout le monde immobile, l'imprimante à tickets devient un sonar*

```text
REF: Michael = @Image 1 (face, hair, build) + @Image 2 (season outfit), keep identical. Location = @Image 4.
FORMAT: 9:16, 10 s, 4 shots, realistic comedy shot like a submarine thriller.
SCENE: The kitchen bathed in red emergency light, water dripping from a tap into a pot, the whole team frozen mid-gesture; an adult chef in a white apron beside Michael.
ACTION:
0–2 s: a drop falls, a sonar ping echoes, Michael raises a finger for silence and whispers.
2–5 s: the chef whispers back; Michael presses his ear against the ticket printer like a hull and reports; the chef lifts a ladle slowly like a periscope.
5–8 s: ping. ping. ping-ping-ping; tickets shoot out of the printer in a burst and curl to the floor.
8–10 s: Michael's eyes go wide; close-up.
DIALOGUE (spoken French, slow and clear, natural lip-sync, no captions): Michael (whisper): « Silence. Une commande. » Chef (whisper): « Où ? » Michael (whisper): « Table quatre. Deux burgers. » Michael: « Ça fait beaucoup de ping. »
CAMERA: macro on the drop → low medium two-shot → insert on the printer → close-up.
LIGHT & GRADE: deep red emergency light, steel reflections, black shadows.
AUDIO: water drop, sonar ping, hull creak, whispers, printer burst, rising tension.
PHYSICS: realistic body weight, no morphing, no sliding feet, correct hands and fingers, no extra limbs. SKIN: preserve Michael's natural skin and features from @Image 1, no smoothing, no plastic look. NO-IP: no brands, no logos, no readable text, no captions or subtitles, no recognizable songs, no real celebrity likeness, no minors. Keep Michael's face, hair, build and outfit identical through the whole clip. Sharp, clean, cinematic render.
```

## SEEDANCE 02 — On remonte

*Alarme rouge, la porte s'ouvre sur la lumière blanche de la salle*

```text
REF: Michael = @Image 1 (face, hair, build) + @Image 2 (season outfit), keep identical. Locations = @Image 4 then @Image 3.
FORMAT: 9:16, 10 s, 4 shots, realistic comedy shot like a submarine thriller.
SCENE: Same kitchen; a rotating red alarm light; tickets now paper the wall; the team whispers loudly in panic.
ACTION:
0–2 s: rotating alarm sweep, tickets everywhere, whispered panic.
2–5 s: Michael shouts in a whisper and turns the sink tap like a valve; steam jets from the pots.
5–8 s: the kitchen door swings open onto the dining room: blinding white light, the roar of the room; Michael squints like a sailor after months at sea.
8–10 s: he looks at the camera, deadpan; the door swings shut on him.
DIALOGUE (spoken French, slow and clear, natural lip-sync, no captions): Michael (loud whisper): « On remonte ! » Michael: « Je préfère le sous-marin. »
CAMERA: rotating light wide → insert on the valve → dolly through the door into white bloom → close-up, door closes.
LIGHT & GRADE: red alarm inside, overexposed white outside, hard cut in colour temperature.
AUDIO: klaxon muted, valve squeak, steam hiss, room noise burst, door thump, silence.
PHYSICS: realistic body weight, no morphing, no sliding feet, correct hands and fingers, no extra limbs. SKIN: preserve Michael's natural skin and features from @Image 1, no smoothing, no plastic look. NO-IP: no brands, no logos, no readable text, no captions or subtitles, no recognizable songs, no real celebrity likeness, no minors. Keep Michael's face, hair, build and outfit identical through the whole clip. Sharp, clean, cinematic render.
```

## CLAUDE CODE — 12 s (outro ep09 : 2 s de transition + 10 s d'animation)

**Voix off — transition** (commune aux 30 épisodes, à 2,1 s) : « Cette scène aurait pu être évitée ? »

**Voix off — épisode** (à 4,6 s) : « Chaque plat, chaque poste, chaque minute : l'écran cuisine FoodEatUp remplace les tickets et le ping. »

```text
Tu es motion designer. Crée avec Remotion (React) une composition verticale 1080×1920, 30 fps,
300 images (10 s), export MP4 H.264, fichier ep09-outro.mp4.

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
2–4 s : les tickets papier collés au mur se détachent, se redressent et deviennent des cartes de commande numériques.
4–7 s : écran Écran cuisine : les plats répartis par poste (froid, chaud, passe) ; un plat passe « en attente → en cours → prêt » en un tap ; la charge de chaque poste s'affiche.
7–9 s : cartes : Écran cuisine · Postes · Commandes · Tables.
Modules affichés en cartes (7–9 s) : Écran cuisine · Postes · Commandes · Tables
Texte à l'écran : « Écran cuisine : chaque plat, chaque poste. »
Voix off de l'épisode (démarre à 4,6 s, finie avant 11,0 s) : « Chaque plat, chaque poste, chaque minute : l'écran cuisine FoodEatUp remplace les tickets et le ping. »
SFX : ping doux par carte, tick par statut, impact final.

RÈGLES : L'animation se comprend sans le son. Texte ≥ 64 px, ≤ 6 mots par écran, zone sûre TikTok/Reels/Shorts (marges 220 px haut, 320 px bas, 120 px côtés). Jamais de faux texte d'interface : uniquement les libellés réels. Deux lignes de voix off : la punchline de transition à 2,1 s, puis la voix de l'épisode à 4,6 s, terminée avant 11,0 s. Un SFX par apparition ; motion blur sur les zooms. Rendu premium SaaS, humoristique, moderne, lisible sur smartphone.

SORTIES : ep09-outro.mp4 · ep09-outro-muet.mp4 · ep09-thumb.png
Titre de la miniature : « Le sous-marin ».
```

## Contrôle avant publication

- [ ] Michael : même visage, même coiffure, même tenue sur les deux scènes.
- [ ] Aucun texte lisible généré par Seedance (enseigne, ticket, écran, sous-titre).
- [ ] Chaque réplique est compréhensible sans sous-titres.
- [ ] La chute est claire avant la fin de la scène 2 et Michael regarde la caméra.
- [ ] Le clap « COUPEZ ! » arrive à 0,4 s de l'outro.
- [ ] Modules affichés : Écran cuisine · Postes · Commandes · Tables — libellés réels vérifiés.
- [ ] Logo FoodEatUp intact, centré, seul à l'écran de 9 à 10 s.
- [ ] La vidéo se comprend sans le son.

---
Source : `episodes/` + `saison.json` — fiche générée par `scripts/build.mjs`, ne pas éditer à la main.
