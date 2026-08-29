# ÉPISODE 04 — « LE BRUNCH DES ZOMBIES »

🎬 **Genre** : Film de zombies
🍽️ **Situation** : Le rush du brunch du dimanche à 11 h
⚙️ **Module** : File d'attente + Plan de salle
🎯 **Hook (0–2 s)** : Une tasse qui tremble, un grondement, Michael : « Ils arrivent. »

## Sélecteurs Higgsfield

| Époque | Genre | Lumière | Physique | Objectif | Émotion | Montage |
|---|---|---|---|---|---|---|
| 2020s | horreur | blanche crue de matin, angle frontal | réaliste (foule au ralenti) | 24 mm grand-angle | dread → panique comique | 4 plans |

> Le look du film se règle dans ces sélecteurs : ne le répétez pas dans le texte du prompt.

## SEEDANCE 01 — Ils arrivent

*Restaurant vide, une horde de brunchers avance lentement vers la vitrine*

```text
REF: Michael = @Image 1 (face, hair, build) + @Image 2 (season outfit), keep identical. Location = @Image 3.
FORMAT: 9:16, 10 s, 4 shots, realistic comedy shot like a zombie movie.
SCENE: Sunday morning, empty restaurant, flat white light, total silence. Michael sips a coffee at the bar.
ACTION:
0–2 s: close-up on the coffee cup; it starts to vibrate; a low rumble.
2–5 s: Michael walks to the glass front; outside, a crowd of adults in sunglasses shuffles slowly toward the window, arms half raised, heads down.
5–8 s: hands press against the glass one by one; moaning voices; Michael backs away.
8–10 s: extreme close-up on Michael's face; he stacks two chairs against the door.
DIALOGUE (spoken French, slow and clear, natural lip-sync, no captions): Crowd (moaning): « Brunch… » « Café… » « Œufs… » Michael: « Ils arrivent. »
CAMERA: macro on cup → dolly toward the window → handheld through the glass → extreme close-up.
LIGHT & GRADE: harsh morning white, slightly green shadows, high contrast.
AUDIO: cup rattle, sub rumble, shuffling feet, moans, palms squeaking on glass, chair scrape.
PHYSICS: realistic body weight, no morphing, no sliding feet, correct hands and fingers, no extra limbs. SKIN: preserve Michael's natural skin and features from @Image 1, no smoothing, no plastic look. NO-IP: no brands, no logos, no readable text, no captions or subtitles, no recognizable songs, no real celebrity likeness, no minors. Keep Michael's face, hair, build and outfit identical through the whole clip. Sharp, clean, cinematic render.
```

## SEEDANCE 02 — Dix minutes

*La porte cède, service en accéléré, Michael dos au mur*

```text
REF: Michael = @Image 1 (face, hair, build) + @Image 2 (season outfit), keep identical. Location = @Image 3.
FORMAT: 9:16, 10 s, 4 shots, realistic comedy shot like a zombie movie.
SCENE: The door gives way; the crowd pours in, in slow motion, backlit; Michael silhouetted in the middle.
ACTION:
0–2 s: slow-motion breach, chairs sliding, Michael's hair blown back.
2–5 s: hyper-fast montage: plates of eggs, juice, pancakes flying across tables; Michael weaves between customers.
5–8 s: a customer grabs Michael's arm and moans a question; he answers; she repeats it slowly and shuffles away.
8–10 s: Michael with his back to the wall, breathing hard, looks at the camera and manages a tired smile.
DIALOGUE (spoken French, slow and clear, natural lip-sync, no captions): Customer: « Une table ? » Michael: « Dix minutes. » Customer (slow): « Dix… minutes… » Michael: « Ils ont faim. » (beat) « Moi aussi. »
CAMERA: slow-motion low angle → whip pans and speed ramps → medium two-shot → static close-up.
LIGHT & GRADE: backlit door, white bloom, warm skin, cold background.
AUDIO: door crash, slow-motion roar, fast plate clatter, sizzling, moan, exhausted breath.
PHYSICS: realistic body weight, no morphing, no sliding feet, correct hands and fingers, no extra limbs. SKIN: preserve Michael's natural skin and features from @Image 1, no smoothing, no plastic look. NO-IP: no brands, no logos, no readable text, no captions or subtitles, no recognizable songs, no real celebrity likeness, no minors. Keep Michael's face, hair, build and outfit identical through the whole clip. Sharp, clean, cinematic render.
```

## CLAUDE CODE — 10 s (outro ep04)

**Voix off** : « Le rush du dimanche n'est pas une invasion. FoodEatUp met tout le monde en file et remplit la salle table par table. »

> ⚠️ Cette phrase dépasse la fenêtre de 7 s (2,0 s → 9,0 s) à débit posé.
> **Variante courte proposée** : « Le rush du dimanche n'est pas une invasion. FoodEatUp met tout le monde en file et remplit la salle. »

```text
Tu es motion designer. Crée avec Remotion (React) une composition verticale 1080×1920, 30 fps,
300 images (10 s), export MP4 H.264, fichier ep04-outro.mp4.

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
2–4 s : la foule collée à la vitre se transforme en une liste de groupes : nom, nombre de personnes, attente estimée.
4–7 s : écran File d'attente : un groupe ajouté en un tap → « table prête » envoyé → sur le plan de salle, la table passe de libre à occupée ; la salle se remplit en vert.
7–9 s : cartes : File d'attente · Plan de salle · Tables · Commandes.
Modules affichés en cartes (7–9 s) : File d'attente · Plan de salle · Tables · Commandes
Texte à l'écran : « Le rush arrive. La file est prête. »
Voix off (démarre à 2,0 s, finie avant 9,0 s) : « Le rush du dimanche n'est pas une invasion. FoodEatUp met tout le monde en file et remplit la salle table par table. »
SFX : tick par groupe, notification, whoosh de remplissage, impact final.

RÈGLES : L'animation se comprend sans le son. Texte ≥ 64 px, ≤ 6 mots par écran, zone sûre TikTok/Reels/Shorts (marges 220 px haut, 320 px bas, 120 px côtés). Jamais de faux texte d'interface : uniquement les libellés réels. La voix off démarre à 2,0 s et finit avant 9,0 s. Un SFX par apparition ; motion blur sur les zooms. Rendu premium SaaS, humoristique, moderne, lisible sur smartphone.

SORTIES : ep04-outro.mp4 · ep04-outro-muet.mp4 · ep04-thumb.png
Titre de la miniature : « Le brunch des zombies ».
```

## Contrôle avant publication

- [ ] Michael : même visage, même coiffure, même tenue sur les deux scènes.
- [ ] Aucun texte lisible généré par Seedance (enseigne, ticket, écran, sous-titre).
- [ ] Chaque réplique est compréhensible sans sous-titres.
- [ ] La chute est claire avant la fin de la scène 2 et Michael regarde la caméra.
- [ ] Le clap « COUPEZ ! » arrive à 0,4 s de l'outro.
- [ ] Modules affichés : File d'attente · Plan de salle · Tables · Commandes — libellés réels vérifiés.
- [ ] Logo FoodEatUp intact, centré, seul à l'écran de 9 à 10 s.
- [ ] La vidéo se comprend sans le son.

---
Source : `episodes/` + `saison.json` — fiche générée par `scripts/build.mjs`, ne pas éditer à la main.
