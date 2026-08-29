# ÉPISODE 08 — « LE DOCUMENTAIRE »

🎬 **Genre** : Documentaire animalier (voix de narrateur)
🍽️ **Situation** : La cliente influenceuse filme son plat pendant qu'il refroidit
⚙️ **Module** : Avis + Site vitrine + Fidélité
🎯 **Hook (0–2 s)** : Voix de narrateur : « Ici, dans son habitat naturel… » — une cliente et son ring light.

## Sélecteurs Higgsfield

| Époque | Genre | Lumière | Physique | Objectif | Émotion | Montage |
|---|---|---|---|---|---|---|
| 2020s | documentaire | naturelle de fenêtre, angle latéral | réaliste | 135 mm téléobjectif | patience amusée | 4 plans |

> Le look du film se règle dans ces sélecteurs : ne le répétez pas dans le texte du prompt.

## SEEDANCE 01 — Le client qui filme

*Narrateur calme, Michael caché derrière une plante*

```text
REF: Michael = @Image 1 (face, hair, build) + @Image 2 (season outfit), keep identical. Location = @Image 3.
FORMAT: 9:16, 10 s, 4 shots, realistic comedy shot like a wildlife documentary.
SCENE: A window table; an adult influencer with a small ring light on a tripod circles her steaming plate with her phone. Michael crouches behind a large potted plant, peeking through the leaves.
ACTION:
0–2 s: long-lens shot through leaves; the narrator introduces the scene.
2–5 s: she shoots the plate from eight angles; time-lapse: the steam rises, thins, disappears.
5–8 s: she stops, repositions a single fry with two fingers, restarts; Michael whispers.
8–10 s: the narrator concludes; Michael stares into the camera, one slow blink.
DIALOGUE (spoken French, slow and clear, natural lip-sync, no captions): Narrator (calm male voice-over): « Ici, dans son habitat naturel… le client qui filme. » Michael (whisper): « Elle filme encore. » Michael (whisper): « Une frite. » Narrator: « Le serveur attend. »
CAMERA: telephoto through leaves → orbit around the table → macro on the fry → static close-up on Michael.
LIGHT & GRADE: soft daylight, natural colours, gentle vignette.
AUDIO: gentle documentary strings (original), phone shutter, ring light hum, leaves rustling, whisper.
PHYSICS: realistic body weight, no morphing, no sliding feet, correct hands and fingers, no extra limbs. SKIN: preserve Michael's natural skin and features from @Image 1, no smoothing, no plastic look. NO-IP: no brands, no logos, no readable text, no captions or subtitles, no recognizable songs, no real celebrity likeness, no minors. Keep Michael's face, hair, build and outfit identical through the whole clip. Sharp, clean, cinematic render.
```

## SEEDANCE 02 — Le cycle recommence

*C'est froid, elle refilme, Michael apporte un plat neuf… qu'elle refilme*

```text
REF: Michael = @Image 1 (face, hair, build) + @Image 2 (season outfit), keep identical. Location = @Image 3.
FORMAT: 9:16, 10 s, 4 shots, realistic comedy shot like a wildlife documentary.
SCENE: Same table; the influencer finally tastes the food.
ACTION:
0–2 s: she takes one bite, freezes, and states the obvious.
2–5 s: she flips the phone to front camera and films herself complaining; Michael emerges from the plant in slow motion carrying a new steaming plate.
5–8 s: she beams, sets the ring light, films the new plate from eight angles; Michael walks backwards into the plant.
8–10 s: close-up on Michael between two leaves; he speaks to the camera.
DIALOGUE (spoken French, slow and clear, natural lip-sync, no captions): Influencer: « C'est froid. » Narrator: « Et le cycle recommence. » Michael: « J'aurais dû faire biologiste. »
CAMERA: close-up on the bite → handheld front-cam feel → slow-motion tracking with the plate → telephoto through leaves.
LIGHT & GRADE: soft daylight, steam catching the window light.
AUDIO: fork tap, phone tap, slow-motion whoosh, shutter burst, leaves, documentary strings resolve.
PHYSICS: realistic body weight, no morphing, no sliding feet, correct hands and fingers, no extra limbs. SKIN: preserve Michael's natural skin and features from @Image 1, no smoothing, no plastic look. NO-IP: no brands, no logos, no readable text, no captions or subtitles, no recognizable songs, no real celebrity likeness, no minors. Keep Michael's face, hair, build and outfit identical through the whole clip. Sharp, clean, cinematic render.
```

## CLAUDE CODE — 10 s (outro ep08)

**Voix off** : « Vos clients font votre pub. FoodEatUp la récupère : la photo, l'avis, les points de fidélité. »

```text
Tu es motion designer. Crée avec Remotion (React) une composition verticale 1080×1920, 30 fps,
300 images (10 s), export MP4 H.264, fichier ep08-outro.mp4.

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
2–4 s : les huit photos de la cliente s'envolent de son téléphone et se rangent en galerie.
4–7 s : écran : les photos rejoignent la galerie du Site vitrine, son commentaire devient un Avis à modérer en un tap, sa visite crédite des points sur sa fiche Fidélité.
7–9 s : cartes : Site vitrine · Avis · Fidélité · Clients.
Modules affichés en cartes (7–9 s) : Site vitrine · Avis · Fidélité · Clients
Texte à l'écran : « Ils filment. Vous gagnez. »
Voix off (démarre à 2,0 s, finie avant 9,0 s) : « Vos clients font votre pub. FoodEatUp la récupère : la photo, l'avis, les points de fidélité. »
SFX : shutter par photo, ding de points, impact final.

RÈGLES : L'animation se comprend sans le son. Texte ≥ 64 px, ≤ 6 mots par écran, zone sûre TikTok/Reels/Shorts (marges 220 px haut, 320 px bas, 120 px côtés). Jamais de faux texte d'interface : uniquement les libellés réels. La voix off démarre à 2,0 s et finit avant 9,0 s. Un SFX par apparition ; motion blur sur les zooms. Rendu premium SaaS, humoristique, moderne, lisible sur smartphone.

SORTIES : ep08-outro.mp4 · ep08-outro-muet.mp4 · ep08-thumb.png
Titre de la miniature : « Le documentaire ».
```

## Contrôle avant publication

- [ ] Michael : même visage, même coiffure, même tenue sur les deux scènes.
- [ ] Aucun texte lisible généré par Seedance (enseigne, ticket, écran, sous-titre).
- [ ] Chaque réplique est compréhensible sans sous-titres.
- [ ] La chute est claire avant la fin de la scène 2 et Michael regarde la caméra.
- [ ] Le clap « COUPEZ ! » arrive à 0,4 s de l'outro.
- [ ] Modules affichés : Site vitrine · Avis · Fidélité · Clients — libellés réels vérifiés.
- [ ] Logo FoodEatUp intact, centré, seul à l'écran de 9 à 10 s.
- [ ] La vidéo se comprend sans le son.

---
Source : `episodes/` + `saison.json` — fiche générée par `scripts/build.mjs`, ne pas éditer à la main.
