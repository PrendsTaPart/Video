# ÉPISODE 22 — « LE POKER »

🎬 **Genre** : Film de casino
🍽️ **Situation** : Le nouveau plat à quatorze euros… qui coûte seize
⚙️ **Module** : Recettes (coût, marge) + Analyse de la carte
🎯 **Hook (0–2 s)** : Lampe verte de table de jeu, le chef pousse une assiette au centre : « Le nouveau plat. Quatorze euros. »

## Sélecteurs Higgsfield

| Époque | Genre | Lumière | Physique | Objectif | Émotion | Montage |
|---|---|---|---|---|---|---|
| 1970s | film de casino | lampe basse verte, angle plongée | réaliste | 85 mm | bluff | 4 plans |

> Le look du film se règle dans ces sélecteurs : ne le répétez pas dans le texte du prompt.

## SEEDANCE 01 — Je suis

*Les tickets de caisse mélangés comme des cartes*

```text
REF: Michael = @Image 1 (face, hair, build) + @Image 2 (season outfit) + a dealer's green visor, keep identical. Location = @Image 3 (back room).
FORMAT: 9:16, 10 s, 4 shots, realistic comedy shot like a casino movie.
SCENE: A back room, a low green lamp over a table, steam like cigar smoke; Michael as the dealer; an adult chef pushes a plate to the centre like a stack of chips.
ACTION:
0–2 s: the chef slides the plate into the light and names the price.
2–5 s: Michael asks the cost; the chef shrugs; Michael shuffles a deck of till receipts like cards.
5–8 s: he turns the receipts over one by one, naming an ingredient; the chef answers vaguely; Michael presses; the chef repeats.
8–10 s: close-up on Michael's poker stare; he pushes a pile of wine corks into the centre.
DIALOGUE (spoken French, slow and clear, natural lip-sync, no captions): Chef: « Le nouveau plat. Quatorze euros. » Michael: « Ça coûte combien ? » Chef: « …aucune idée. » Michael: « Truffe. » Chef: « Un peu. » Michael: « Un peu combien ? » Chef: « Un peu. » Michael: « Je suis. »
CAMERA: top-down on the plate → medium two-shot → macro on the receipt flip → close-up on the stare.
LIGHT & GRADE: green lamp, warm faces, seventies grain, deep shadows.
AUDIO: lamp hum, receipt shuffle, cork clatter, jazz bass (original), a slow exhale.
PHYSICS: realistic body weight, no morphing, no sliding feet, correct hands and fingers, no extra limbs. SKIN: preserve Michael's natural skin and features from @Image 1, no smoothing, no plastic look. NO-IP: no brands, no logos, no readable text, no captions or subtitles, no recognizable songs, no real celebrity likeness, no minors. Keep Michael's face, hair, build and outfit identical through the whole clip. Sharp, clean, cinematic render.
```

## SEEDANCE 02 — On perd deux euros

*Le calcul sur la serviette, l'assiette retournée comme une carte perdante*

```text
REF: Michael = @Image 1 (face, hair, build) + @Image 2 (season outfit) + a dealer's green visor, keep identical. Location = @Image 3 (back room).
FORMAT: 9:16, 10 s, 4 shots, realistic comedy shot like a casino movie.
SCENE: Same table; Michael calculates on a napkin with a pencil.
ACTION:
0–2 s: pencil scratching, the camera slowly orbits the table.
2–5 s: he stops writing; long beat; he states the selling price, then the cost.
5–8 s: the chef defends the dish; Michael agrees flatly; the chef insists.
8–10 s: Michael looks at the camera, turns the plate over like a losing card, adds two words.
DIALOGUE (spoken French, slow and clear, natural lip-sync, no captions): Michael: « Quatorze de vente… seize de coût. » Chef: « Mais il est beau. » Michael: « Il est beau. » Chef: « Très beau. » Michael: « On perd deux euros. » (beat) « Par assiette. »
CAMERA: slow orbit → close-up on the pencil stopping → two-shot → close-up, plate flip.
LIGHT & GRADE: green lamp, smoke curling in the beam.
AUDIO: pencil scratch, silence, jazz sting, plate clink, exhale.
PHYSICS: realistic body weight, no morphing, no sliding feet, correct hands and fingers, no extra limbs. SKIN: preserve Michael's natural skin and features from @Image 1, no smoothing, no plastic look. NO-IP: no brands, no logos, no readable text, no captions or subtitles, no recognizable songs, no real celebrity likeness, no minors. Keep Michael's face, hair, build and outfit identical through the whole clip. Sharp, clean, cinematic render.
```

## CLAUDE CODE — 12 s (outro ep22 : 2 s de transition + 10 s d'animation)

**Voix off — transition** (commune aux 30 épisodes, à 2,1 s) : « Cette scène aurait pu être évitée ? »

**Voix off — épisode** (à 4,6 s) : « Chaque plat a un coût, une marge, un prix juste. FoodEatUp les calcule avant que vous misiez. »

```text
Tu es motion designer. Crée avec Remotion (React) une composition verticale 1080×1920, 30 fps,
300 images (10 s), export MP4 H.264, fichier ep22-outro.mp4.

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
2–4 s : la serviette devient une fiche recette : ingrédients, quantités, prix d'achat.
4–7 s : écran Recettes : coût de revient calculé → marge en pourcentage → prix conseillé ; puis l'Analyse de la carte place le plat dans la matrice popularité × marge.
7–9 s : cartes : Recettes · Ingrédients · Analyse de la carte · Commandes.
Modules affichés en cartes (7–9 s) : Recettes · Ingrédients · Analyse de la carte · Commandes
Texte à l'écran : « Un plat beau. Et rentable. »
Voix off de l'épisode (démarre à 4,6 s, finie avant 11,0 s) : « Chaque plat a un coût, une marge, un prix juste. FoodEatUp les calcule avant que vous misiez. »
SFX : tick par ingrédient, jeton, impact final.

RÈGLES : L'animation se comprend sans le son. Texte ≥ 64 px, ≤ 6 mots par écran, zone sûre TikTok/Reels/Shorts (marges 220 px haut, 320 px bas, 120 px côtés). Jamais de faux texte d'interface : uniquement les libellés réels. Deux lignes de voix off : la punchline de transition à 2,1 s, puis la voix de l'épisode à 4,6 s, terminée avant 11,0 s. Un SFX par apparition ; motion blur sur les zooms. Rendu premium SaaS, humoristique, moderne, lisible sur smartphone.

SORTIES : ep22-outro.mp4 · ep22-outro-muet.mp4 · ep22-thumb.png
Titre de la miniature : « Le poker ».
```

## Contrôle avant publication

- [ ] Michael : même visage, même coiffure, même tenue sur les deux scènes.
- [ ] Aucun texte lisible généré par Seedance (enseigne, ticket, écran, sous-titre).
- [ ] Chaque réplique est compréhensible sans sous-titres.
- [ ] La chute est claire avant la fin de la scène 2 et Michael regarde la caméra.
- [ ] Le clap « COUPEZ ! » arrive à 0,4 s de l'outro.
- [ ] Modules affichés : Recettes · Ingrédients · Analyse de la carte · Commandes — libellés réels vérifiés.
- [ ] Logo FoodEatUp intact, centré, seul à l'écran de 9 à 10 s.
- [ ] La vidéo se comprend sans le son.

---
Source : `episodes/` + `saison.json` — fiche générée par `scripts/build.mjs`, ne pas éditer à la main.
