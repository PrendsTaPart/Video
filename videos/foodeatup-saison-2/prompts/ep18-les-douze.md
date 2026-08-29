# ÉPISODE 18 — « LES DOUZE »

🎬 **Genre** : Comédie de mariage / grande famille
🍽️ **Situation** : « On sera douze » = douze familles
⚙️ **Module** : Événements privés
🎯 **Hook (0–2 s)** : Michael au téléphone : « On sera douze ? Parfait. »

## Sélecteurs Higgsfield

| Époque | Genre | Lumière | Physique | Objectif | Émotion | Montage |
|---|---|---|---|---|---|---|
| 2020s | comédie familiale | chaleureuse de fête, angle frontal | hyperbolique (scène 2) | 35 mm | sourire figé | 4 plans |

> Le look du film se règle dans ces sélecteurs : ne le répétez pas dans le texte du prompt.

## SEEDANCE 01 — Douze familles

*La porte s'ouvre et n'arrête plus de laisser entrer du monde*

```text
REF: Michael = @Image 1 (face, hair, build) + @Image 2 (season outfit), keep identical. Location = @Image 3.
FORMAT: 9:16, 10 s, 4 shots, realistic comedy shot like a big-family wedding comedy.
SCENE: Michael on the phone, smiling; then the front door on Saturday: a family enters with balloons, a tiered cake on a trolley, an accordion, and keeps entering.
ACTION:
0–2 s: Michael hangs up, pleased with himself.
2–5 s: endless lateral tracking shot along the entering crowd: balloons, cake trolley, accordion player, cousins, cousins, cousins.
5–8 s: Michael counts on his fingers, passes ten, loses count; the adult organiser explains.
8–10 s: close-up on Michael's frozen smile.
DIALOGUE (spoken French, slow and clear, natural lip-sync, no captions): Michael: « On sera douze ? Parfait. » Organiser: « On est douze. » Michael: « Douze ? » Organiser: « Douze… familles. » Michael: « Parfait. »
CAMERA: medium on the phone → long lateral tracking → close-up on fingers → close-up on the smile.
LIGHT & GRADE: warm festive light, balloons in saturated colours.
AUDIO: phone click, door bell ringing again and again, accordion (original tune), chatter, cake trolley wheels.
PHYSICS: realistic body weight, no morphing, no sliding feet, correct hands and fingers, no extra limbs. SKIN: preserve Michael's natural skin and features from @Image 1, no smoothing, no plastic look. NO-IP: no brands, no logos, no readable text, no captions or subtitles, no recognizable songs, no real celebrity likeness, no minors. Keep Michael's face, hair, build and outfit identical through the whole clip. Sharp, clean, cinematic render.
```

## SEEDANCE 02 — Pardon

*Bancs, tables collées jusqu'au trottoir, Michael souffle les bougies par réflexe*

```text
REF: Michael = @Image 1 (face, hair, build) + @Image 2 (season outfit), keep identical. Location = @Image 3.
FORMAT: 9:16, 10 s, 4 shots, realistic comedy shot like a big-family wedding comedy.
SCENE: Chairs borrowed from everywhere; Michael carries a bench over his head.
ACTION:
0–2 s: Michael with the bench, weaving through balloons.
2–5 s: fast montage: tablecloths, two tables pushed together, three, eight, out onto the pavement; the accordion plays.
5–8 s: the tiered cake with lit candles is wheeled straight to Michael; the whole family sings off-screen.
8–10 s: alone in front of the candles, Michael blows them out by reflex; silence; he apologises to the camera.
DIALOGUE (spoken French, slow and clear, natural lip-sync, no captions): Michael: « Pardon. »
CAMERA: low angle on the bench → time-lapse montage → dolly with the cake → close-up on the blow, silence.
LIGHT & GRADE: warm festive light, candle glow on Michael's face.
AUDIO: bench creak, tables scraping, accordion, off-screen singing (original), candle blow, record-scratch silence.
PHYSICS: realistic body weight, no morphing, no sliding feet, correct hands and fingers, no extra limbs. SKIN: preserve Michael's natural skin and features from @Image 1, no smoothing, no plastic look. NO-IP: no brands, no logos, no readable text, no captions or subtitles, no recognizable songs, no real celebrity likeness, no minors. Keep Michael's face, hair, build and outfit identical through the whole clip. Sharp, clean, cinematic render.
```

## CLAUDE CODE — 10 s (outro ep18)

**Voix off** : « Douze ou cinquante, tout est écrit : la demande, le devis, la salle, la facture. FoodEatUp gère vos privatisations de bout en bout. »

> ⚠️ Cette phrase dépasse la fenêtre de 7 s (2,0 s → 9,0 s) à débit posé.
> **Variante courte proposée** : « Douze ou cinquante : la demande, le devis, la salle, la facture. FoodEatUp gère vos privatisations. »

```text
Tu es motion designer. Crée avec Remotion (React) une composition verticale 1080×1920, 30 fps,
300 images (10 s), export MP4 H.264, fichier ep18-outro.mp4.

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
2–4 s : les bougies deviennent une demande d'événement : date, nombre de personnes, budget.
4–7 s : écran Événements privés : demande « nouvelle → devis → gagnée » ; devis envoyé en un tap ; tables réservées sur le plan de salle ; facture générée.
7–9 s : cartes : Événements privés · Devis · Réservations · Factures.
Modules affichés en cartes (7–9 s) : Événements privés · Devis · Réservations · Factures
Texte à l'écran : « Privatisation : tout est écrit. »
Voix off (démarre à 2,0 s, finie avant 9,0 s) : « Douze ou cinquante, tout est écrit : la demande, le devis, la salle, la facture. FoodEatUp gère vos privatisations de bout en bout. »
SFX : souffle de bougie, tick par étape, impact final.

RÈGLES : L'animation se comprend sans le son. Texte ≥ 64 px, ≤ 6 mots par écran, zone sûre TikTok/Reels/Shorts (marges 220 px haut, 320 px bas, 120 px côtés). Jamais de faux texte d'interface : uniquement les libellés réels. La voix off démarre à 2,0 s et finit avant 9,0 s. Un SFX par apparition ; motion blur sur les zooms. Rendu premium SaaS, humoristique, moderne, lisible sur smartphone.

SORTIES : ep18-outro.mp4 · ep18-outro-muet.mp4 · ep18-thumb.png
Titre de la miniature : « Les douze ».
```

## Contrôle avant publication

- [ ] Michael : même visage, même coiffure, même tenue sur les deux scènes.
- [ ] Aucun texte lisible généré par Seedance (enseigne, ticket, écran, sous-titre).
- [ ] Chaque réplique est compréhensible sans sous-titres.
- [ ] La chute est claire avant la fin de la scène 2 et Michael regarde la caméra.
- [ ] Le clap « COUPEZ ! » arrive à 0,4 s de l'outro.
- [ ] Modules affichés : Événements privés · Devis · Réservations · Factures — libellés réels vérifiés.
- [ ] Logo FoodEatUp intact, centré, seul à l'écran de 9 à 10 s.
- [ ] La vidéo se comprend sans le son.

---
Source : `episodes/` + `saison.json` — fiche générée par `scripts/build.mjs`, ne pas éditer à la main.
