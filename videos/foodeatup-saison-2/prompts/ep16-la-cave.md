# ÉPISODE 16 — « LA CAVE »

🎬 **Genre** : Horreur found footage (caméra de poche, vision nocturne)
🍽️ **Situation** : Chercher une facture fournisseur dans la cave à trois heures du matin
⚙️ **Module** : Factures + Dépenses + Synthèse financière
🎯 **Hook (0–2 s)** : Image verte tremblante, Michael se filme : « Il est trois heures. Je cherche une facture. »

## Sélecteurs Higgsfield

| Époque | Genre | Lumière | Physique | Objectif | Émotion | Montage |
|---|---|---|---|---|---|---|
| 2000s (caméscope) | horreur found footage | vision nocturne + lampe torche | réaliste | grand-angle de caméscope | peur comique | 3 plans (un plan-séquence par scène possible) |

> Le look du film se règle dans ces sélecteurs : ne le répétez pas dans le texte du prompt.

## SEEDANCE 01 — Je cherche une facture

*La caméra descend à la cave, un carton bouge*

```text
REF: Michael = @Image 1 (face, hair, build) + @Image 2 (season outfit), keep identical. Location = a cellar under the restaurant (cardboard boxes, wine racks).
FORMAT: 9:16, 10 s, 3 shots, found-footage horror comedy, handheld camcorder look, night-vision green, timecode-free (no readable overlay).
SCENE: Michael films himself with a small camcorder held at arm's length, whispering; then the cellar stairs; boxes of receipts everywhere.
ACTION:
0–2 s: selfie-style night-vision close-up, Michael whispers his mission.
2–5 s: he goes down the cellar stairs, the torch shakes; a cardboard box moves slightly (a draught); he freezes.
5–8 s: he opens a shoebox: hundreds of receipts; one yellowed invoice flies up in front of the lens; he lets out a small scream.
8–10 s: the camera drops to the floor; we see only his shoes; his voice.
DIALOGUE (spoken French, slow and clear, natural lip-sync, no captions): Michael (whisper): « Il est trois heures. Je cherche une facture. » Michael: « C'est pas celle-là. »
CAMERA: handheld selfie → shaky POV down the stairs → POV into the box → camera falls, tilted floor view.
LIGHT & GRADE: night-vision green with hot torch spots, heavy noise, vignette.
AUDIO: breathing close to the mic, creaking steps, box scrape, paper flutter, small scream, camera clatter.
PHYSICS: realistic body weight, no morphing, no sliding feet, correct hands and fingers, no extra limbs. SKIN: preserve Michael's natural skin and features from @Image 1, no smoothing, no plastic look. NO-IP: no brands, no logos, no readable text, no captions or subtitles, no recognizable songs, no real celebrity likeness, no minors. Keep Michael's face, hair, build and outfit identical through the whole clip. Sharp, clean, cinematic render.
```

## SEEDANCE 02 — Impayée

*Sous une couverture de papiers, il trouve enfin la facture*

```text
REF: Michael = @Image 1 (face, hair, build) + @Image 2 (season outfit), keep identical. Location = same cellar.
FORMAT: 9:16, 10 s, 3 shots, found-footage horror comedy, handheld camcorder look, night-vision green.
SCENE: The camera is picked up from the floor; Michael is now sitting under a blanket of receipts.
ACTION:
0–2 s: the camera lifts, night-vision reveals Michael covered in paper.
2–5 s: fast montage of him reading receipts and discarding them; one sticks to his forehead.
5–8 s: he finds the invoice, holds it up to the lens in triumph; then reads it and his face falls.
8–10 s: the torch dies; black; his voice; a box tumbles.
DIALOGUE (spoken French, slow and clear, natural lip-sync, no captions): Michael: « Poisson… non. Pain… non. » Michael (triumphant, then flat): « …impayée. » Michael (in the dark): « Non. »
CAMERA: handheld lift → jump-cut montage → close-up to lens → cut to black with audio only.
LIGHT & GRADE: night-vision green, torch hot spot, then full black.
AUDIO: paper rustle in bursts, sticky peel, triumphant gasp, torch click off, cardboard tumble.
PHYSICS: realistic body weight, no morphing, no sliding feet, correct hands and fingers, no extra limbs. SKIN: preserve Michael's natural skin and features from @Image 1, no smoothing, no plastic look. NO-IP: no brands, no logos, no readable text, no captions or subtitles, no recognizable songs, no real celebrity likeness, no minors. Keep Michael's face, hair, build and outfit identical through the whole clip. Sharp, clean, cinematic render.
```

## CLAUDE CODE — 12 s (outro ep16 : 2 s de transition + 10 s d'animation)

**Voix off — transition** (commune aux 30 épisodes, à 2,1 s) : « Cette scène aurait pu être évitée ? »

**Voix off — épisode** (à 4,6 s) : « Vos factures ne dorment plus à la cave. FoodEatUp affiche ce qui est payé, ce qui attend, et ce que ça vous coûte. »

> ⚠️ Cette phrase dépasse la fenêtre de 6.4 s (2,0 s → 9,0 s) à débit posé.
> **Variante courte proposée** : « Vos factures ne dorment plus à la cave. FoodEatUp affiche ce qui est payé et ce qui attend. »

```text
Tu es motion designer. Crée avec Remotion (React) une composition verticale 1080×1920, 30 fps,
300 images (10 s), export MP4 H.264, fichier ep16-outro.mp4.

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
2–4 s : la vision nocturne verte passe en pleine lumière ; les tickets deviennent des lignes classées par statut : payée, en attente, impayée.
4–7 s : écran Factures et Dépenses : une facture passe « en attente → payée » en un tap ; la Synthèse financière se met à jour : CA facturé, encaissé, impayés, dépenses.
7–9 s : cartes : Factures · Dépenses · Devis · Synthèse financière.
Modules affichés en cartes (7–9 s) : Factures · Dépenses · Devis · Synthèse financière
Texte à l'écran : « Vos chiffres, en pleine lumière. »
Voix off de l'épisode (démarre à 4,6 s, finie avant 11,0 s) : « Vos factures ne dorment plus à la cave. FoodEatUp affiche ce qui est payé, ce qui attend, et ce que ça vous coûte. »
SFX : interrupteur, tick par statut, impact final.

RÈGLES : L'animation se comprend sans le son. Texte ≥ 64 px, ≤ 6 mots par écran, zone sûre TikTok/Reels/Shorts (marges 220 px haut, 320 px bas, 120 px côtés). Jamais de faux texte d'interface : uniquement les libellés réels. Deux lignes de voix off : la punchline de transition à 2,1 s, puis la voix de l'épisode à 4,6 s, terminée avant 11,0 s. Un SFX par apparition ; motion blur sur les zooms. Rendu premium SaaS, humoristique, moderne, lisible sur smartphone.

SORTIES : ep16-outro.mp4 · ep16-outro-muet.mp4 · ep16-thumb.png
Titre de la miniature : « La cave ».
```

## Contrôle avant publication

- [ ] Michael : même visage, même coiffure, même tenue sur les deux scènes.
- [ ] Aucun texte lisible généré par Seedance (enseigne, ticket, écran, sous-titre).
- [ ] Chaque réplique est compréhensible sans sous-titres.
- [ ] La chute est claire avant la fin de la scène 2 et Michael regarde la caméra.
- [ ] Le clap « COUPEZ ! » arrive à 0,4 s de l'outro.
- [ ] Modules affichés : Factures · Dépenses · Devis · Synthèse financière — libellés réels vérifiés.
- [ ] Logo FoodEatUp intact, centré, seul à l'écran de 9 à 10 s.
- [ ] La vidéo se comprend sans le son.

---
Source : `episodes/` + `saison.json` — fiche générée par `scripts/build.mjs`, ne pas éditer à la main.
