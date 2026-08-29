# ÉPISODE 30 — « LA CÉRÉMONIE »

🎬 **Genre** : Cérémonie de remise de prix + générique de fin
🍽️ **Situation** : Tout le casting de la saison réuni, Michael ouvre l'enveloppe
⚙️ **Module** : FoodEatUp tout entier
🎯 **Hook (0–2 s)** : Tapis rouge dans le restaurant, roulement de tambour : « Et le gagnant… »

## Sélecteurs Higgsfield

| Époque | Genre | Lumière | Physique | Objectif | Émotion | Montage |
|---|---|---|---|---|---|---|
| 2020s | cérémonie / drame élégant | projecteurs chauds, angle frontal | réaliste | anamorphique 50 mm | émotion sincère et drôle | 4 plans |

> Le look du film se règle dans ces sélecteurs : ne le répétez pas dans le texte du prompt.

## SEEDANCE 01 — Et le gagnant

*L'enveloppe, le casting, le téléphone brandi*

```text
REF: Michael = @Image 1 (face, hair, build) + @Image 2 (season outfit) + a tuxedo jacket over the apron, keep identical. Location = @Image 3.
FORMAT: 9:16, 10 s, 4 shots, realistic comedy shot like an awards ceremony.
SCENE: A red carpet through the dining room, warm spotlights; the season's cast seated as adults in the audience: the chef, a waiter, an influencer with a ring light, a courier with a helmet, a regular in a suit. Michael at a small podium holds a sealed envelope.
ACTION:
0–2 s: drum roll; Michael starts the announcement.
2–5 s: he opens the envelope very slowly; the camera orbits him; the audience leans forward.
5–8 s: he pulls out his phone and holds it up like a trophy (screen blurred, no readable text); the audience erupts.
8–10 s: the chef wipes a tear with a kitchen towel; confetti; Michael thanks his mother.
DIALOGUE (spoken French, slow and clear, natural lip-sync, no captions): Michael: « Et le gagnant… » Michael: « …c'est… lui. » Michael: « Merci maman. »
CAMERA: wide on the red carpet → slow orbit on the envelope → low angle on the raised phone → medium on the chef, confetti.
LIGHT & GRADE: warm golden spotlights, anamorphic flares, confetti sparkle.
AUDIO: drum roll, envelope tear, gasp, applause, sniff, confetti pop, strings (original).
PHYSICS: realistic body weight, no morphing, no sliding feet, correct hands and fingers, no extra limbs. SKIN: preserve Michael's natural skin and features from @Image 1, no smoothing, no plastic look. NO-IP: no brands, no logos, no readable text, no captions or subtitles, no recognizable songs, no real celebrity likeness, no minors. Keep Michael's face, hair, build and outfit identical through the whole clip. Sharp, clean, cinematic render.
```

## SEEDANCE 02 — Coupez

*Générique de fin : le restaurant fonctionne, chacun salue, Michael boit enfin son café*

```text
REF: Michael = @Image 1 (face, hair, build) + @Image 2 (season outfit), keep identical. Location = @Image 3.
FORMAT: 9:16, 10 s, 4 shots, warm realistic comedy shot like an end-credits sequence.
SCENE: The restaurant calm and running perfectly: the chef smiling at the pass, a waiter clocking in with a wave, a customer paying with a nod.
ACTION:
0–2 s: a smooth steadicam pulls back along the dining room; each cast member waves at the camera as it passes.
2–5 s: the camera keeps gliding backwards; soft music.
5–8 s: Michael finally sits, takes a coffee, exhales; the camera continues out through the door into the street.
8–10 s: Michael, tiny in the distance, says one last word to the camera; a clapperboard snaps shut; black.
DIALOGUE (spoken French, slow and clear, natural lip-sync, no captions): Michael (softly): « Coupez. »
CAMERA: one continuous steadicam pull-back with waves → sit-down beat → out the door → clapperboard, cut to black.
LIGHT & GRADE: warm late-afternoon light, gentle glow, soft contrast.
AUDIO: soft piano (original), cups, a distant laugh, the coffee sip, clapperboard snap, silence.
PHYSICS: realistic body weight, no morphing, no sliding feet, correct hands and fingers, no extra limbs. SKIN: preserve Michael's natural skin and features from @Image 1, no smoothing, no plastic look. NO-IP: no brands, no logos, no readable text, no captions or subtitles, no recognizable songs, no real celebrity likeness, no minors. Keep Michael's face, hair, build and outfit identical through the whole clip. Sharp, clean, cinematic render.
```

## CLAUDE CODE — 10 s (outro ep30)

**Voix off** : « Trente films. Un restaurant. Un seul système. FoodEatUp. »

```text
Tu es motion designer. Crée avec Remotion (React) une composition verticale 1080×1920, 30 fps,
300 images (10 s), export MP4 H.264, fichier ep30-outro.mp4.

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

FINAL DE SAISON : le découpage ci-dessous REMPLACE la structure imposée (le clap reste à 0,4 s,
le logo reste seul de 9 à 10 s).

CONTENU DE CET ÉPISODE :
0–2 s : clap « COUPEZ ! » sur la dernière image de la scène 2.
2–4 s : mosaïque des 29 chutes précédentes (une image figée par épisode) en grille verticale qui défile très vite.
4–6 s : chaque image se transforme en données et converge vers le centre.
6–8 s : cartes reliées : Commandes · Réservations · Plan de salle · Écran cuisine · Caisse · Stock · HACCP · Planning · Fidélité · Campagnes · Avis · Synthèse financière.
8–9 s : tout disparaît.
9–10 s : logo FoodEatUp seul, animation finale, signature sous le logo : « Le système qui travaille avec vous. »
Modules affichés en cartes : Commandes · Réservations · Plan de salle · Écran cuisine · Caisse · Stock · HACCP · Planning · Fidélité · Campagnes · Avis · Synthèse financière
Texte à l'écran (6–8 s, au-dessus des cartes) : « Trente films. Un seul système. »
Voix off (démarre à 2,0 s, finie avant 9,0 s) : « Trente films. Un restaurant. Un seul système. FoodEatUp. »
SFX : clap, défilement rapide, convergence, impact propre + petit whoosh, fondu.

RÈGLES : L'animation se comprend sans le son. Texte ≥ 64 px, ≤ 6 mots par écran, zone sûre TikTok/Reels/Shorts (marges 220 px haut, 320 px bas, 120 px côtés). Jamais de faux texte d'interface : uniquement les libellés réels. La voix off démarre à 2,0 s et finit avant 9,0 s. Un SFX par apparition ; motion blur sur les zooms. Rendu premium SaaS, humoristique, moderne, lisible sur smartphone.

SORTIES : ep30-outro.mp4 · ep30-outro-muet.mp4 · ep30-thumb.png
Titre de la miniature : « La cérémonie ».
```

## Contrôle avant publication

- [ ] Michael : même visage, même coiffure, même tenue sur les deux scènes.
- [ ] Aucun texte lisible généré par Seedance (enseigne, ticket, écran, sous-titre).
- [ ] Chaque réplique est compréhensible sans sous-titres.
- [ ] La chute est claire avant la fin de la scène 2 et Michael regarde la caméra.
- [ ] Le clap « COUPEZ ! » arrive à 0,4 s de l'outro.
- [ ] Modules affichés : Commandes · Réservations · Plan de salle · Écran cuisine · Caisse · Stock · HACCP · Planning · Fidélité · Campagnes · Avis · Synthèse financière — libellés réels vérifiés.
- [ ] Logo FoodEatUp intact, centré, seul à l'écran de 9 à 10 s.
- [ ] La vidéo se comprend sans le son.

---
Source : `episodes/` + `saison.json` — fiche générée par `scripts/build.mjs`, ne pas éditer à la main.
