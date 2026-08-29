# ÉPISODE 23 — « LA MÉMOIRE »

🎬 **Genre** : Thriller amnésique (post-its et flèches)
🍽️ **Situation** : L'habitué dit « Comme d'habitude » et Michael ne sait plus
⚙️ **Module** : Clients + Fidélité
🎯 **Hook (0–2 s)** : « Comme d'habitude. » — « Bien sûr. » (sourire figé dès qu'il se retourne)

## Sélecteurs Higgsfield

| Époque | Genre | Lumière | Physique | Objectif | Émotion | Montage |
|---|---|---|---|---|---|---|
| 2020s | thriller psychologique | froide de comptoir, angle latéral | réaliste | 50 mm | panique intérieure | 4 plans |

> Le look du film se règle dans ces sélecteurs : ne le répétez pas dans le texte du prompt.

## SEEDANCE 01 — D'habitude

*Un comptoir couvert de post-its avec des visages dessinés*

```text
REF: Michael = @Image 1 (face, hair, build) + @Image 2 (season outfit), keep identical. Location = @Image 3 (counter).
FORMAT: 9:16, 10 s, 4 shots, realistic comedy shot like an amnesia thriller.
SCENE: An adult regular sits at the counter and orders without looking up; behind the counter, dozens of sticky notes with hand-drawn faces and arrows (no readable words).
ACTION:
0–2 s: the regular orders; Michael agrees, turns around, and his smile freezes.
2–5 s: reverse shot: the wall of sticky notes; Michael scans them frantically, finger moving from face to face; none match.
5–8 s: he discreetly turns back and studies the customer from several angles while the camera orbits; the customer reads a newspaper.
8–10 s: Michael whispers to the camera.
DIALOGUE (spoken French, slow and clear, natural lip-sync, no captions): Regular: « Comme d'habitude. » Michael: « Bien sûr. » Michael (whisper): « Je sais pas c'est quoi, d'habitude. »
CAMERA: two-shot → reverse on the wall with rack focus → orbit around the customer → close-up whisper.
LIGHT & GRADE: cool counter light, sticky notes in muted colours, shallow depth of field.
AUDIO: newspaper rustle, thriller pulse (original), paper flicks, orbit whoosh, whisper.
PHYSICS: realistic body weight, no morphing, no sliding feet, correct hands and fingers, no extra limbs. SKIN: preserve Michael's natural skin and features from @Image 1, no smoothing, no plastic look. NO-IP: no brands, no logos, no readable text, no captions or subtitles, no recognizable songs, no real celebrity likeness, no minors. Keep Michael's face, hair, build and outfit identical through the whole clip. Sharp, clean, cinematic render.
```

## SEEDANCE 02 — Une omelette

*Trois plats, un café, une soupe, un dessert… la table déborde*

```text
REF: Michael = @Image 1 (face, hair, build) + @Image 2 (season outfit), keep identical. Location = @Image 3 (counter).
FORMAT: 9:16, 10 s, 4 shots, realistic comedy shot like an amnesia thriller.
SCENE: Same counter, same regular; Michael arrives with three different dishes and a coffee.
ACTION:
0–2 s: he sets the plates around the customer, watching his face.
2–5 s: the customer shakes his head; Michael insists it is close; he adds a soup, a dessert, a juice; the counter overflows.
5–8 s: the customer finally says the word; Michael repeats it and writes it on the palm of his hand.
8–10 s: the customer takes the dessert anyway; Michael shows his palm to the camera.
DIALOGUE (spoken French, slow and clear, natural lip-sync, no captions): Regular: « C'est pas ça. » Michael: « C'est… presque ça. » Regular: « Une omelette. » Michael: « …une omelette. » Michael (showing his palm): « D'habitude, c'est ça. »
CAMERA: medium → top-down on the overflowing counter → close-up on the palm → medium, dessert taken.
LIGHT & GRADE: cool counter light, plates colourful against the wood.
AUDIO: plates set down one by one, spoon clink, pen on skin, fork into the dessert.
PHYSICS: realistic body weight, no morphing, no sliding feet, correct hands and fingers, no extra limbs. SKIN: preserve Michael's natural skin and features from @Image 1, no smoothing, no plastic look. NO-IP: no brands, no logos, no readable text, no captions or subtitles, no recognizable songs, no real celebrity likeness, no minors. Keep Michael's face, hair, build and outfit identical through the whole clip. Sharp, clean, cinematic render.
```

## CLAUDE CODE — 12 s (outro ep23 : 2 s de transition + 10 s d'animation)

**Voix off — transition** (commune aux 30 épisodes, à 2,1 s) : « Cette scène aurait pu être évitée ? »

**Voix off — épisode** (à 4,6 s) : « Ses habitudes, vous les connaissez, même sans mémoire. FoodEatUp garde l'historique, les préférences et la fidélité de chaque client. »

> ⚠️ Cette phrase dépasse la fenêtre de 6.4 s (2,0 s → 9,0 s) à débit posé.
> **Variante courte proposée** : « Même sans mémoire, vous connaissez ses habitudes. FoodEatUp garde l'historique et la fidélité. »

```text
Tu es motion designer. Crée avec Remotion (React) une composition verticale 1080×1920, 30 fps,
300 images (10 s), export MP4 H.264, fichier ep23-outro.mp4.

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
2–4 s : les post-its aux visages dessinés se transforment en fiches clients avec leur historique.
4–7 s : écran Clients : fiche du client → dernières commandes, plat préféré, dernière visite → solde de points Fidélité et récompense disponible ; un tap : « comme d'habitude » part en commande.
7–9 s : cartes : Clients · Fidélité · Commandes · Récompenses.
Modules affichés en cartes (7–9 s) : Clients · Fidélité · Commandes · Récompenses
Texte à l'écran : « Comme d'habitude. Vraiment. »
Voix off de l'épisode (démarre à 4,6 s, finie avant 11,0 s) : « Ses habitudes, vous les connaissez, même sans mémoire. FoodEatUp garde l'historique, les préférences et la fidélité de chaque client. »
SFX : tick par fiche, ding de points, impact final.

RÈGLES : L'animation se comprend sans le son. Texte ≥ 64 px, ≤ 6 mots par écran, zone sûre TikTok/Reels/Shorts (marges 220 px haut, 320 px bas, 120 px côtés). Jamais de faux texte d'interface : uniquement les libellés réels. Deux lignes de voix off : la punchline de transition à 2,1 s, puis la voix de l'épisode à 4,6 s, terminée avant 11,0 s. Un SFX par apparition ; motion blur sur les zooms. Rendu premium SaaS, humoristique, moderne, lisible sur smartphone.

SORTIES : ep23-outro.mp4 · ep23-outro-muet.mp4 · ep23-thumb.png
Titre de la miniature : « La mémoire ».
```

## Contrôle avant publication

- [ ] Michael : même visage, même coiffure, même tenue sur les deux scènes.
- [ ] Aucun texte lisible généré par Seedance (enseigne, ticket, écran, sous-titre).
- [ ] Chaque réplique est compréhensible sans sous-titres.
- [ ] La chute est claire avant la fin de la scène 2 et Michael regarde la caméra.
- [ ] Le clap « COUPEZ ! » arrive à 0,4 s de l'outro.
- [ ] Modules affichés : Clients · Fidélité · Commandes · Récompenses — libellés réels vérifiés.
- [ ] Logo FoodEatUp intact, centré, seul à l'écran de 9 à 10 s.
- [ ] La vidéo se comprend sans le son.

---
Source : `episodes/` + `saison.json` — fiche générée par `scripts/build.mjs`, ne pas éditer à la main.
