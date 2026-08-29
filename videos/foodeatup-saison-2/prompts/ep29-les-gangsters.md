# ÉPISODE 29 — « LES GANGSTERS »

🎬 **Genre** : Film de gangsters (lumière tamisée, chuchotements, respect)
🍽️ **Situation** : L'habitué qui dit « Mets ça sur ma note » depuis six mois
⚙️ **Module** : Ardoises
🎯 **Hook (0–2 s)** : Un client en costume se penche : « Mets ça sur ma note. »

## Sélecteurs Higgsfield

| Époque | Genre | Lumière | Physique | Objectif | Émotion | Montage |
|---|---|---|---|---|---|---|
| 1970s | film de gangsters | tamisée ambrée, angle bas | hyperbolique (scène 2) | 50 mm | respect craintif | 4 plans |

> Le look du film se règle dans ces sélecteurs : ne le répétez pas dans le texte du prompt.

## SEEDANCE 01 — Sur ma note

*Le mur de petits papiers derrière le comptoir*

```text
REF: Michael = @Image 1 (face, hair, build) + @Image 2 (season outfit), keep identical. Location = @Image 3 (counter).
FORMAT: 9:16, 10 s, 4 shots, realistic comedy shot like a seventies gangster movie.
SCENE: Dim amber light; an adult regular in a suit leans toward Michael at the counter and speaks low.
ACTION:
0–2 s: the regular gives his instruction; Michael nods respectfully.
2–5 s: the camera glides behind the counter: a wall covered with small paper slips, each with a drawn moustache symbol (no readable words), months of them.
5–8 s: montage, day after day: the same line, Michael pins one slip, two, ten; the wall overflows.
8–10 s: Michael whispers to the camera.
DIALOGUE (spoken French, slow and clear, natural lip-sync, no captions): Regular: « Mets ça sur ma note. » Michael: « Bien sûr. » Regular (repeated in the montage): « Sur ma note. » Michael (whisper): « Il paie quand ? »
CAMERA: close two-shot → glide behind the counter → jump-cut montage on the wall → close-up whisper.
LIGHT & GRADE: amber practicals, seventies grain, deep brown shadows.
AUDIO: low mandolin (original), pin pushes, paper rustle, ice in a glass, whisper.
PHYSICS: realistic body weight, no morphing, no sliding feet, correct hands and fingers, no extra limbs. SKIN: preserve Michael's natural skin and features from @Image 1, no smoothing, no plastic look. NO-IP: no brands, no logos, no readable text, no captions or subtitles, no recognizable songs, no real celebrity likeness, no minors. Keep Michael's face, hair, build and outfit identical through the whole clip. Sharp, clean, cinematic render.
```

## SEEDANCE 02 — Tu prends les chèques ?

*Le rouleau de caisse traverse la salle et descend la rue*

```text
REF: Michael = @Image 1 (face, hair, build) + @Image 2 (season outfit), keep identical. Location = @Image 3.
FORMAT: 9:16, 10 s, 4 shots, realistic comedy shot like a seventies gangster movie.
SCENE: One evening the regular returns, jovial, and asks for his total.
ACTION:
0–2 s: the regular asks; Michael reaches for the till roll.
2–5 s: he unrolls the paper: it crosses the room, passes the door and rolls down the street in slow motion.
5–8 s: the regular follows the paper with his eyes, very slowly; both react with the same syllable.
8–10 s: the regular pulls out a chequebook; Michael looks at the camera as the roll flutters in the wind.
DIALOGUE (spoken French, slow and clear, natural lip-sync, no captions): Regular: « Je dois combien ? » Regular: « Ah. » Michael: « Ah. » Regular: « Tu prends les chèques ? »
CAMERA: two-shot → tracking along the unrolling paper out the door → slow pan on the regular's face → close-up on Michael.
LIGHT & GRADE: amber interior, blue street at dusk, paper glowing in the doorway.
AUDIO: paper unrolling endlessly, street ambience, silence, chequebook flap, wind on paper.
PHYSICS: realistic body weight, no morphing, no sliding feet, correct hands and fingers, no extra limbs. SKIN: preserve Michael's natural skin and features from @Image 1, no smoothing, no plastic look. NO-IP: no brands, no logos, no readable text, no captions or subtitles, no recognizable songs, no real celebrity likeness, no minors. Keep Michael's face, hair, build and outfit identical through the whole clip. Sharp, clean, cinematic render.
```

## CLAUDE CODE — 12 s (outro ep29 : 2 s de transition + 10 s d'animation)

**Voix off — transition** (commune aux 30 épisodes, à 2,1 s) : « Cette scène aurait pu être évitée ? »

**Voix off — épisode** (à 4,6 s) : « L'ardoise est numérique : elle ne s'oublie pas, elle ne s'envole pas. Solde, historique, règlement, dans FoodEatUp. »

> ⚠️ Cette phrase dépasse la fenêtre de 7 s (2,0 s → 9,0 s) à débit posé.
> **Variante courte proposée** : « L'ardoise est numérique : elle ne s'oublie pas. Solde, historique, règlement, dans FoodEatUp. »

```text
Tu es motion designer. Crée avec Remotion (React) une composition verticale 1080×1920, 30 fps,
300 images (10 s), export MP4 H.264, fichier ep29-outro.mp4.

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
2–4 s : le mur de papiers se replie en une seule fiche ardoise avec un solde dû.
4–7 s : écran Ardoises : client, solde dû, historique des consommations, statut ; règlement partiel ou total encaissé en caisse en un tap.
7–9 s : cartes : Ardoises · Caisse · Clients · Paiements.
Modules affichés en cartes (7–9 s) : Ardoises · Caisse · Clients · Paiements
Texte à l'écran : « L'ardoise ne s'oublie plus. »
Voix off de l'épisode (démarre à 4,6 s, finie avant 11,0 s) : « L'ardoise est numérique : elle ne s'oublie pas, elle ne s'envole pas. Solde, historique, règlement, dans FoodEatUp. »
SFX : papier qui se replie, tick de règlement, impact final.

RÈGLES : L'animation se comprend sans le son. Texte ≥ 64 px, ≤ 6 mots par écran, zone sûre TikTok/Reels/Shorts (marges 220 px haut, 320 px bas, 120 px côtés). Jamais de faux texte d'interface : uniquement les libellés réels. Deux lignes de voix off : la punchline de transition à 2,1 s, puis la voix de l'épisode à 4,6 s, terminée avant 11,0 s. Un SFX par apparition ; motion blur sur les zooms. Rendu premium SaaS, humoristique, moderne, lisible sur smartphone.

SORTIES : ep29-outro.mp4 · ep29-outro-muet.mp4 · ep29-thumb.png
Titre de la miniature : « Les gangsters ».
```

## Contrôle avant publication

- [ ] Michael : même visage, même coiffure, même tenue sur les deux scènes.
- [ ] Aucun texte lisible généré par Seedance (enseigne, ticket, écran, sous-titre).
- [ ] Chaque réplique est compréhensible sans sous-titres.
- [ ] La chute est claire avant la fin de la scène 2 et Michael regarde la caméra.
- [ ] Le clap « COUPEZ ! » arrive à 0,4 s de l'outro.
- [ ] Modules affichés : Ardoises · Caisse · Clients · Paiements — libellés réels vérifiés.
- [ ] Logo FoodEatUp intact, centré, seul à l'écran de 9 à 10 s.
- [ ] La vidéo se comprend sans le son.

---
Source : `episodes/` + `saison.json` — fiche générée par `scripts/build.mjs`, ne pas éditer à la main.
