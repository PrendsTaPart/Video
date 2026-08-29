# ÉPISODE 12 — « LE CASTING »

🎬 **Genre** : Émission de casting
🍽️ **Situation** : Recruter un serveur
⚙️ **Module** : Recrutement
🎯 **Hook (0–2 s)** : Projecteur, table de jury, Michael seul : « Suivant. »

## Sélecteurs Higgsfield

| Époque | Genre | Lumière | Physique | Objectif | Émotion | Montage |
|---|---|---|---|---|---|---|
| 2020s | télé-crochet | projecteur de scène, angle frontal | hyperbolique (scène 2) | 50 mm | découragement comique | 4 plans |

> Le look du film se règle dans ces sélecteurs : ne le répétez pas dans le texte du prompt.

## SEEDANCE 01 — Suivant

*Trois candidats, trois catastrophes*

```text
REF: Michael = @Image 1 (face, hair, build) + @Image 2 (season outfit), keep identical. Location = @Image 3.
FORMAT: 9:16, 10 s, 4 shots, realistic comedy shot like a TV talent show.
SCENE: The dining room turned into a stage: one spotlight, a long jury table with three chairs, two of them empty; Michael alone behind the table with a pen.
ACTION:
0–2 s: spotlight snaps on; Michael clicks his pen.
2–5 s: adult candidate one juggles three plates; close-up on Michael impressed; off-screen crash of breaking plates; Michael reacts.
5–8 s: adult candidate two states her only condition; Michael reacts; candidate three talks extremely fast, inaudible, with a huge smile.
8–10 s: Michael turns to the camera, expressionless.
DIALOGUE (spoken French, slow and clear, natural lip-sync, no captions): Michael: « Suivant. » Candidate two: « Je travaille pas le week-end. » Michael: « Suivant. » Michael (to camera): « Suivant. »
CAMERA: spotlight wide → medium on the juggling → close-up on Michael → close-up to camera.
LIGHT & GRADE: theatrical spotlight, dark surroundings, warm key.
AUDIO: spotlight clunk, pen click, plates smashing off-screen, TV show sting (original), fast mumbling.
PHYSICS: realistic body weight, no morphing, no sliding feet, correct hands and fingers, no extra limbs. SKIN: preserve Michael's natural skin and features from @Image 1, no smoothing, no plastic look. NO-IP: no brands, no logos, no readable text, no captions or subtitles, no recognizable songs, no real celebrity likeness, no minors. Keep Michael's face, hair, build and outfit identical through the whole clip. Sharp, clean, cinematic render.
```

## SEEDANCE 02 — Y'a personne

*Une file jusqu'au bout de la rue, les CV s'envolent*

```text
REF: Michael = @Image 1 (face, hair, build) + @Image 2 (season outfit), keep identical. Location = @Image 3.
FORMAT: 9:16, 10 s, 4 shots, realistic comedy shot like a TV talent show.
SCENE: Wide shot: a line of adult candidates stretching out of the door and around the block; inside, a stack of paper CVs as tall as Michael.
ACTION:
0–2 s: the endless line, Michael peeks out and sighs.
2–5 s: he carries the giant paper stack; he sneezes.
5–8 s: the door opens, a gust of wind: the CVs fly out into the street in slow motion; the candidates chase the papers.
8–10 s: Michael stands alone with one CV stuck to his face; he peels it off and speaks to the camera.
DIALOGUE (spoken French, slow and clear, natural lip-sync, no captions): Michael: « Y'a personne. » (looks at the line) « Y'a trop de monde. »
CAMERA: wide street shot → medium on the stack → slow-motion paper storm → close-up.
LIGHT & GRADE: daylight, papers white against a grey street.
AUDIO: crowd murmur, sneeze, wind gust, paper storm flutter, running footsteps, peel sound.
PHYSICS: realistic body weight, no morphing, no sliding feet, correct hands and fingers, no extra limbs. SKIN: preserve Michael's natural skin and features from @Image 1, no smoothing, no plastic look. NO-IP: no brands, no logos, no readable text, no captions or subtitles, no recognizable songs, no real celebrity likeness, no minors. Keep Michael's face, hair, build and outfit identical through the whole clip. Sharp, clean, cinematic render.
```

## CLAUDE CODE — 10 s (outro ep12)

**Voix off** : « Une offre, des candidatures classées, un statut par personne. Recruter sans courir après les CV. »

```text
Tu es motion designer. Crée avec Remotion (React) une composition verticale 1080×1920, 30 fps,
300 images (10 s), export MP4 H.264, fichier ep12-outro.mp4.

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
2–4 s : les CV volants se rassemblent en une offre d'emploi publiée (poste, salaire affiché) et une liste de candidatures.
4–7 s : écran Recrutement : une candidature passe « nouvelle → entretien → retenue » en un tap ; la personne retenue devient un Employé.
7–9 s : cartes : Recrutement · Offres d'emploi · Candidatures · Employés.
Modules affichés en cartes (7–9 s) : Recrutement · Offres d'emploi · Candidatures · Employés
Texte à l'écran : « Recrutez. Sans chasser les CV. »
Voix off (démarre à 2,0 s, finie avant 9,0 s) : « Une offre, des candidatures classées, un statut par personne. Recruter sans courir après les CV. »
SFX : tick par candidature, whoosh de statut, impact final.

RÈGLES : L'animation se comprend sans le son. Texte ≥ 64 px, ≤ 6 mots par écran, zone sûre TikTok/Reels/Shorts (marges 220 px haut, 320 px bas, 120 px côtés). Jamais de faux texte d'interface : uniquement les libellés réels. La voix off démarre à 2,0 s et finit avant 9,0 s. Un SFX par apparition ; motion blur sur les zooms. Rendu premium SaaS, humoristique, moderne, lisible sur smartphone.

SORTIES : ep12-outro.mp4 · ep12-outro-muet.mp4 · ep12-thumb.png
Titre de la miniature : « Le casting ».
```

## Contrôle avant publication

- [ ] Michael : même visage, même coiffure, même tenue sur les deux scènes.
- [ ] Aucun texte lisible généré par Seedance (enseigne, ticket, écran, sous-titre).
- [ ] Chaque réplique est compréhensible sans sous-titres.
- [ ] La chute est claire avant la fin de la scène 2 et Michael regarde la caméra.
- [ ] Le clap « COUPEZ ! » arrive à 0,4 s de l'outro.
- [ ] Modules affichés : Recrutement · Offres d'emploi · Candidatures · Employés — libellés réels vérifiés.
- [ ] Logo FoodEatUp intact, centré, seul à l'écran de 9 à 10 s.
- [ ] La vidéo se comprend sans le son.

---
Source : `episodes/` + `saison.json` — fiche générée par `scripts/build.mjs`, ne pas éditer à la main.
