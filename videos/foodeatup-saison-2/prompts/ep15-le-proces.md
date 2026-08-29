# ÉPISODE 15 — « LE PROCÈS »

🎬 **Genre** : Film de tribunal
🍽️ **Situation** : Un client conteste le tiramisu sur l'addition
⚙️ **Module** : Commandes par table + Caisse
🎯 **Hook (0–2 s)** : Michael pose une cuillère sur la table : « Pièce numéro un. »

## Sélecteurs Higgsfield

| Époque | Genre | Lumière | Physique | Objectif | Émotion | Montage |
|---|---|---|---|---|---|---|
| 2020s | drame judiciaire | rasante de fenêtre, angle latéral | réaliste | 50 mm | gravité absurde | 4 plans |

> Le look du film se règle dans ces sélecteurs : ne le répétez pas dans le texte du prompt.

## SEEDANCE 01 — Pièce numéro un

*L'addition comme dossier, une trace de cacao comme preuve*

```text
REF: Michael = @Image 1 (face, hair, build) + @Image 2 (season outfit), keep identical. Location = @Image 3.
FORMAT: 9:16, 10 s, 4 shots, realistic comedy shot like a courtroom drama.
SCENE: The dining room lit like a courtroom, low raking light, Michael standing with a bill in hand like a lawyer; an adult customer sits with folded arms; other customers watch like a jury.
ACTION:
0–2 s: Michael places a spoon on the table with ceremony.
2–5 s: he names the dessert; the customer denies everything.
5–8 s: crash zoom on a smear of cocoa on the customer's cheek; Michael points; the customer wipes it off and improvises.
8–10 s: the jury murmurs; Michael repeats the excuse flatly and looks at the camera.
DIALOGUE (spoken French, slow and clear, natural lip-sync, no captions): Michael: « Pièce numéro un. Le tiramisu. » Customer: « J'ai rien mangé. » Michael: « Et ça ? » Customer: « C'est… du café. » Michael: « Du café. »
CAMERA: insert on the spoon → medium on Michael pacing → crash zoom on the cheek → close-up to camera.
LIGHT & GRADE: warm raking light, dark wood tones, dust in the beam.
AUDIO: spoon on wood, courtroom murmur, crash zoom sting, throat clearing, silence.
PHYSICS: realistic body weight, no morphing, no sliding feet, correct hands and fingers, no extra limbs. SKIN: preserve Michael's natural skin and features from @Image 1, no smoothing, no plastic look. NO-IP: no brands, no logos, no readable text, no captions or subtitles, no recognizable songs, no real celebrity likeness, no minors. Keep Michael's face, hair, build and outfit identical through the whole clip. Sharp, clean, cinematic render.
```

## SEEDANCE 02 — Coupable

*L'assiette raclée, le voisin qui secoue la tête, la louche-marteau*

```text
REF: Michael = @Image 1 (face, hair, build) + @Image 2 (season outfit), keep identical. Location = @Image 3.
FORMAT: 9:16, 10 s, 4 shots, realistic comedy shot like a courtroom drama.
SCENE: Same table, same customer, the neighbour at the next table now part of the case.
ACTION:
0–2 s: Michael paces, hands behind his back.
2–5 s: he presents a scraped-clean dessert plate; the customer blames his neighbour; the adult neighbour slowly shakes his head.
5–8 s: Michael bangs a ladle on the table like a gavel; the jury holds its breath.
8–10 s: the customer gives in; Michael delivers the verdict to the camera; the neighbour applauds softly.
DIALOGUE (spoken French, slow and clear, natural lip-sync, no captions): Michael: « Pièce numéro deux. » Customer: « C'est mon voisin. » Customer: « OK. Je paie. » Michael: « Coupable. »
CAMERA: tracking on the pacing → insert on the plate → close-up on the ladle strike → medium, slow clap.
LIGHT & GRADE: warm raking light, dramatic shadows on the wall.
AUDIO: footsteps, plate scrape, ladle bang with reverb, gasp, soft applause.
PHYSICS: realistic body weight, no morphing, no sliding feet, correct hands and fingers, no extra limbs. SKIN: preserve Michael's natural skin and features from @Image 1, no smoothing, no plastic look. NO-IP: no brands, no logos, no readable text, no captions or subtitles, no recognizable songs, no real celebrity likeness, no minors. Keep Michael's face, hair, build and outfit identical through the whole clip. Sharp, clean, cinematic render.
```

## CLAUDE CODE — 10 s (outro ep15)

**Voix off** : « Chaque plat est noté sur la bonne table, à la bonne heure. Avec FoodEatUp, la note parle d'elle-même. »

```text
Tu es motion designer. Crée avec Remotion (React) une composition verticale 1080×1920, 30 fps,
300 images (10 s), export MP4 H.264, fichier ep15-outro.mp4.

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
2–4 s : la cuillère devient une ligne de commande horodatée ; les articles de la table s'empilent proprement.
4–7 s : écran Commandes : la table, ses articles avec l'heure de commande, le total ; un tap → paiement encaissé en caisse.
7–9 s : cartes : Commandes · Tables · Caisse · Paiements.
Modules affichés en cartes (7–9 s) : Commandes · Tables · Caisse · Paiements
Texte à l'écran : « La note est claire. Pas de procès. »
Voix off (démarre à 2,0 s, finie avant 9,0 s) : « Chaque plat est noté sur la bonne table, à la bonne heure. Avec FoodEatUp, la note parle d'elle-même. »
SFX : coup de marteau doux, tick par article, impact final.

RÈGLES : L'animation se comprend sans le son. Texte ≥ 64 px, ≤ 6 mots par écran, zone sûre TikTok/Reels/Shorts (marges 220 px haut, 320 px bas, 120 px côtés). Jamais de faux texte d'interface : uniquement les libellés réels. La voix off démarre à 2,0 s et finit avant 9,0 s. Un SFX par apparition ; motion blur sur les zooms. Rendu premium SaaS, humoristique, moderne, lisible sur smartphone.

SORTIES : ep15-outro.mp4 · ep15-outro-muet.mp4 · ep15-thumb.png
Titre de la miniature : « Le procès ».
```

## Contrôle avant publication

- [ ] Michael : même visage, même coiffure, même tenue sur les deux scènes.
- [ ] Aucun texte lisible généré par Seedance (enseigne, ticket, écran, sous-titre).
- [ ] Chaque réplique est compréhensible sans sous-titres.
- [ ] La chute est claire avant la fin de la scène 2 et Michael regarde la caméra.
- [ ] Le clap « COUPEZ ! » arrive à 0,4 s de l'outro.
- [ ] Modules affichés : Commandes · Tables · Caisse · Paiements — libellés réels vérifiés.
- [ ] Logo FoodEatUp intact, centré, seul à l'écran de 9 à 10 s.
- [ ] La vidéo se comprend sans le son.

---
Source : `episodes/` + `saison.json` — fiche générée par `scripts/build.mjs`, ne pas éditer à la main.
