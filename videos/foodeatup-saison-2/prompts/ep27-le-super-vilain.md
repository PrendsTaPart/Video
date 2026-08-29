# ÉPISODE 27 — « LE SUPER-VILAIN »

🎬 **Genre** : Film de super-vilain (fauteuil tournant, rire, éclair)
🍽️ **Situation** : Trois demandes de congé pour le même samedi, déjà signées
⚙️ **Module** : Congés + Planning
🎯 **Hook (0–2 s)** : Fauteuil qui se retourne lentement, lumière par en dessous : « Samedi. »

## Sélecteurs Higgsfield

| Époque | Genre | Lumière | Physique | Objectif | Émotion | Montage |
|---|---|---|---|---|---|---|
| 2020s | film de super-héros (côté vilain) | contre-plongée dramatique + éclairs, angle bas | réaliste | 35 mm | mégalomanie qui s'effondre | 4 plans |

> Le look du film se règle dans ces sélecteurs : ne le répétez pas dans le texte du prompt.

## SEEDANCE 01 — J'ai déjà signé

*Il lit les trois demandes avec un rire de vilain… qui se casse*

```text
REF: Michael = @Image 1 (face, hair, build) + @Image 2 (season outfit), keep identical. Location = @Image 3 (back office corner).
FORMAT: 9:16, 10 s, 4 shots, realistic comedy shot like a supervillain reveal.
SCENE: A dark office, a swivel chair with its back to the camera, a desk lamp from below; Michael strokes a baguette like a villain's pet.
ACTION:
0–2 s: the chair turns slowly; underlight on Michael's face.
2–5 s: he reads three sheets one after the other with a villain's laugh after each; the laugh cracks on the third.
5–8 s: he counts: three requests, three waiters, the same Saturday; close-up.
8–10 s: he looks at the camera; lightning flashes behind him.
DIALOGUE (spoken French, slow and clear, natural lip-sync, no captions): Michael: « Samedi. » (laugh) « Samedi. » (laugh) « Samedi. » (broken laugh) Michael: « Tout le monde. » Michael: « J'ai déjà signé. »
CAMERA: slow reveal on the chair → close-up on the sheets → extreme close-up → medium with lightning.
LIGHT & GRADE: underlight, cold blue rim, lightning flashes, deep blacks.
AUDIO: chair creak, villain organ (original), paper flips, laugh, laugh, laugh cracking, thunder.
PHYSICS: realistic body weight, no morphing, no sliding feet, correct hands and fingers, no extra limbs. SKIN: preserve Michael's natural skin and features from @Image 1, no smoothing, no plastic look. NO-IP: no brands, no logos, no readable text, no captions or subtitles, no recognizable songs, no real celebrity likeness, no minors. Keep Michael's face, hair, build and outfit identical through the whole clip. Sharp, clean, cinematic render.
```

## SEEDANCE 02 — J'ai validé quoi ?

*Samedi midi, seul, il fait tout, la caméra tourne de plus en plus vite*

```text
REF: Michael = @Image 1 (face, hair, build) + @Image 2 (season outfit), keep identical. Location = @Image 3.
FORMAT: 9:16, 10 s, 4 shots, realistic comedy shot like a supervillain movie.
SCENE: Saturday noon, the restaurant full; Michael alone, sliding on the tiled floor in trainers.
ACTION:
0–2 s: he slides in, takes an order mid-slide.
2–5 s: fast montage: he runs to the kitchen, comes out wearing the chef's hat, serves, takes payment, clears tables; the camera orbits faster and faster.
5–8 s: he stops dead in the middle of the room; everyone looks at him; he smiles; a plate breaks off-screen.
8–10 s: he looks at his hand: three signed leave forms; close-up.
DIALOGUE (spoken French, slow and clear, natural lip-sync, no captions): Michael: « Je gère. » Michael: « J'ai validé quoi ? »
CAMERA: low slide shot → accelerating orbit → sudden static wide → insert on the forms.
LIGHT & GRADE: bright lunch light, saturated, motion blur on the orbit.
AUDIO: floor squeak, accelerating rhythm, plate smash, silence, paper crinkle.
PHYSICS: realistic body weight, no morphing, no sliding feet, correct hands and fingers, no extra limbs. SKIN: preserve Michael's natural skin and features from @Image 1, no smoothing, no plastic look. NO-IP: no brands, no logos, no readable text, no captions or subtitles, no recognizable songs, no real celebrity likeness, no minors. Keep Michael's face, hair, build and outfit identical through the whole clip. Sharp, clean, cinematic render.
```

## CLAUDE CODE — 10 s (outro ep27)

**Voix off** : « Un congé validé, un planning à jour, un samedi couvert. FoodEatUp vous prévient avant que vous signiez. »

```text
Tu es motion designer. Crée avec Remotion (React) une composition verticale 1080×1920, 30 fps,
300 images (10 s), export MP4 H.264, fichier ep27-outro.mp4.

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
2–4 s : les trois feuilles deviennent trois demandes de congé sur le même jour ; une alerte de conflit s'allume.
4–7 s : écran Congés : demande → conflit détecté (trois absents, minimum de service) → validation ou refus en un tap → le Planning de la semaine se réorganise.
7–9 s : cartes : Congés · Planning · Shifts · Employés.
Modules affichés en cartes (7–9 s) : Congés · Planning · Shifts · Employés
Texte à l'écran : « Validez sans vous retrouver seul. »
Voix off (démarre à 2,0 s, finie avant 9,0 s) : « Un congé validé, un planning à jour, un samedi couvert. FoodEatUp vous prévient avant que vous signiez. »
SFX : alerte douce, tick de validation, impact final.

RÈGLES : L'animation se comprend sans le son. Texte ≥ 64 px, ≤ 6 mots par écran, zone sûre TikTok/Reels/Shorts (marges 220 px haut, 320 px bas, 120 px côtés). Jamais de faux texte d'interface : uniquement les libellés réels. La voix off démarre à 2,0 s et finit avant 9,0 s. Un SFX par apparition ; motion blur sur les zooms. Rendu premium SaaS, humoristique, moderne, lisible sur smartphone.

SORTIES : ep27-outro.mp4 · ep27-outro-muet.mp4 · ep27-thumb.png
Titre de la miniature : « Le super-vilain ».
```

## Contrôle avant publication

- [ ] Michael : même visage, même coiffure, même tenue sur les deux scènes.
- [ ] Aucun texte lisible généré par Seedance (enseigne, ticket, écran, sous-titre).
- [ ] Chaque réplique est compréhensible sans sous-titres.
- [ ] La chute est claire avant la fin de la scène 2 et Michael regarde la caméra.
- [ ] Le clap « COUPEZ ! » arrive à 0,4 s de l'outro.
- [ ] Modules affichés : Congés · Planning · Shifts · Employés — libellés réels vérifiés.
- [ ] Logo FoodEatUp intact, centré, seul à l'écran de 9 à 10 s.
- [ ] La vidéo se comprend sans le son.

---
Source : `episodes/` + `saison.json` — fiche générée par `scripts/build.mjs`, ne pas éditer à la main.
