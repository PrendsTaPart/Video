# ÉPISODE 26 — « LE DÉTECTIVE »

🎬 **Genre** : Film noir (noir et blanc, stores vénitiens, voix off intérieure)
🍽️ **Situation** : Qui a nettoyé la hotte ?
⚙️ **Module** : Plan de nettoyage + Checklist hygiène
🎯 **Hook (0–2 s)** : Noir et blanc, voix off : « Il était vingt-trois heures. La hotte était sale. »

## Sélecteurs Higgsfield

| Époque | Genre | Lumière | Physique | Objectif | Émotion | Montage |
|---|---|---|---|---|---|---|
| 1960s + noir et blanc | film noir | stores vénitiens, angle latéral dur | réaliste | 40 mm | soupçon | 4 plans |

> Le look du film se règle dans ces sélecteurs : ne le répétez pas dans le texte du prompt.

## SEEDANCE 01 — Qui a nettoyé la hotte ?

*L'équipe alignée contre le mur, tout le monde pointe le voisin*

```text
REF: Michael = @Image 1 (face, hair, build) + @Image 2 (season outfit) + a trench coat and a fedora over the apron, keep identical. Location = @Image 4.
FORMAT: 9:16, 10 s, 4 shots, black-and-white comedy shot like a film noir.
SCENE: The kitchen at night in black and white, venetian-blind shadows across the steel; Michael in a trench coat and fedora over his apron; his own voice as inner narration.
ACTION:
0–2 s: Michael examines the extractor hood with a magnifying glass; inner voice-over sets the scene.
2–5 s: he runs a finger along the hood: black; he stares at his finger.
5–8 s: three adults line up against the wall: the chef, a waiter, the dishwasher; Michael asks the question; all three point at their neighbour at the same time.
8–10 s: the dishwasher slowly turns his finger toward Michael; close-up on Michael.
DIALOGUE (spoken French, slow and clear, natural lip-sync, no captions): Michael (voice-over): « Il était vingt-trois heures. La hotte était sale. » Michael: « Quelqu'un ment. » Michael: « Qui a nettoyé la hotte ? » Michael: « Moi ? »
CAMERA: macro through the magnifying glass → insert on the finger → wide lineup → slow push-in on Michael.
LIGHT & GRADE: high-contrast black and white, hard slats of light, smoke haze.
AUDIO: muted trumpet (original), dripping tap, finger squeak on steel, three shirts rustling as they point, sting.
PHYSICS: realistic body weight, no morphing, no sliding feet, correct hands and fingers, no extra limbs. SKIN: preserve Michael's natural skin and features from @Image 1, no smoothing, no plastic look. NO-IP: no brands, no logos, no readable text, no captions or subtitles, no recognizable songs, no real celebrity likeness, no minors. Keep Michael's face, hair, build and outfit identical through the whole clip. Sharp, clean, cinematic render.
```

## SEEDANCE 02 — Le coupable, c'était moi

*Le planning jauni au mur, sa propre photo sur la case du lundi*

```text
REF: Michael = @Image 1 (face, hair, build) + @Image 2 (season outfit) + a trench coat and a fedora, keep identical. Location = @Image 4.
FORMAT: 9:16, 10 s, 4 shots, black-and-white comedy shot like a film noir.
SCENE: Michael walks through the kitchen under falling steam like indoor rain; inner narration.
ACTION:
0–2 s: he walks slowly, collar up, steam drifting.
2–5 s: he finds a yellowed paper schedule pinned to the wall; he blows off the dust.
5–8 s: the camera zooms into one square of the grid: a small ID photo of Michael pinned there (no readable text); narration.
8–10 s: he slowly removes his hat, looks at the camera; fade to black.
DIALOGUE (spoken French, slow and clear, natural lip-sync, no captions): Michael (voice-over): « Je cherchais un coupable. » Michael (voice-over): « Lundi. Hotte. » Michael: « Ah. » Michael (voice-over): « Le coupable, c'était moi. »
CAMERA: tracking through steam → insert on the paper → slow zoom into the photo → close-up, fade out.
LIGHT & GRADE: black and white, steam catching the slats of light, soft fade.
AUDIO: footsteps with reverb, dust blow, paper crackle, trumpet resolve, silence.
PHYSICS: realistic body weight, no morphing, no sliding feet, correct hands and fingers, no extra limbs. SKIN: preserve Michael's natural skin and features from @Image 1, no smoothing, no plastic look. NO-IP: no brands, no logos, no readable text, no captions or subtitles, no recognizable songs, no real celebrity likeness, no minors. Keep Michael's face, hair, build and outfit identical through the whole clip. Sharp, clean, cinematic render.
```

## CLAUDE CODE — 12 s (outro ep26 : 2 s de transition + 10 s d'animation)

**Voix off — transition** (commune aux 30 épisodes, à 2,1 s) : « Cette scène aurait pu être évitée ? »

**Voix off — épisode** (à 4,6 s) : « Qui, quoi, quand : c'est écrit. Le plan de nettoyage FoodEatUp enregistre chaque action, pas besoin de détective. »

> ⚠️ Cette phrase dépasse la fenêtre de 6.4 s (2,0 s → 9,0 s) à débit posé.
> **Variante courte proposée** : « Qui, quoi, quand : c'est écrit. Le plan de nettoyage FoodEatUp enregistre chaque action. »

```text
Tu es motion designer. Crée avec Remotion (React) une composition verticale 1080×1920, 30 fps,
300 images (10 s), export MP4 H.264, fichier ep26-outro.mp4.

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
2–4 s : le planning jauni passe du noir et blanc à la couleur et devient une grille de zones et de postes.
4–7 s : écran Plan de nettoyage : zone → poste → fréquence ; une action de nettoyage enregistrée en un tap avec qui et quand ; la Checklist hygiène du jour se valide.
7–9 s : cartes : Plan de nettoyage · Checklist hygiène · HACCP · Employés.
Modules affichés en cartes (7–9 s) : Plan de nettoyage · Checklist hygiène · HACCP · Employés
Texte à l'écran : « Qui a nettoyé ? C'est écrit. »
Voix off de l'épisode (démarre à 4,6 s, finie avant 11,0 s) : « Qui, quoi, quand : c'est écrit. Le plan de nettoyage FoodEatUp enregistre chaque action, pas besoin de détective. »
SFX : passage couleur, tick par action, impact final.

RÈGLES : L'animation se comprend sans le son. Texte ≥ 64 px, ≤ 6 mots par écran, zone sûre TikTok/Reels/Shorts (marges 220 px haut, 320 px bas, 120 px côtés). Jamais de faux texte d'interface : uniquement les libellés réels. Deux lignes de voix off : la punchline de transition à 2,1 s, puis la voix de l'épisode à 4,6 s, terminée avant 11,0 s. Un SFX par apparition ; motion blur sur les zooms. Rendu premium SaaS, humoristique, moderne, lisible sur smartphone.

SORTIES : ep26-outro.mp4 · ep26-outro-muet.mp4 · ep26-thumb.png
Titre de la miniature : « Le détective ».
```

## Contrôle avant publication

- [ ] Michael : même visage, même coiffure, même tenue sur les deux scènes.
- [ ] Aucun texte lisible généré par Seedance (enseigne, ticket, écran, sous-titre).
- [ ] Chaque réplique est compréhensible sans sous-titres.
- [ ] La chute est claire avant la fin de la scène 2 et Michael regarde la caméra.
- [ ] Le clap « COUPEZ ! » arrive à 0,4 s de l'outro.
- [ ] Modules affichés : Plan de nettoyage · Checklist hygiène · HACCP · Employés — libellés réels vérifiés.
- [ ] Logo FoodEatUp intact, centré, seul à l'écran de 9 à 10 s.
- [ ] La vidéo se comprend sans le son.

---
Source : `episodes/` + `saison.json` — fiche générée par `scripts/build.mjs`, ne pas éditer à la main.
