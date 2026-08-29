# ÉPISODE 05 — « LE CASSE »

🎬 **Genre** : Film de braquage
🍽️ **Situation** : La clôture de caisse à 23 h 30, il manque cinq euros
⚙️ **Module** : Caisse (rapport X / clôture Z)
🎯 **Hook (0–2 s)** : Lampe frontale, tiroir-caisse ouvert comme un coffre : « Il manque cinq euros. »

## Sélecteurs Higgsfield

| Époque | Genre | Lumière | Physique | Objectif | Émotion | Montage |
|---|---|---|---|---|---|---|
| 2020s | thriller de braquage | lampe frontale + néon du frigo, angle bas | réaliste | 35 mm + macro | concentration → désespoir | 4 plans |

> Le look du film se règle dans ces sélecteurs : ne le répétez pas dans le texte du prompt.

## SEEDANCE 01 — Le coffre

*Michael compte les pièces comme un braqueur, le compte ne tombe pas juste*

```text
REF: Michael = @Image 1 (face, hair, build) + @Image 2 (season outfit), keep identical. Location = @Image 3.
FORMAT: 9:16, 10 s, 4 shots, realistic comedy shot like a heist movie.
SCENE: Restaurant closed, lights off, only a headlamp on Michael's forehead and the glow of a drinks fridge. The cash drawer is open on the bar like a safe.
ACTION:
0–2 s: macro on coins stacked in neat towers, the headlamp beam sweeping across them.
2–5 s: close-up on Michael's lips counting silently, eyes darting; he slides one coin at a time.
5–8 s: he holds a long paper roll from the till next to the coins (no readable text), compares, frowns, recounts one tower.
8–10 s: he looks up at the camera, the headlamp flickers, he speaks.
DIALOGUE (spoken French, slow and clear, natural lip-sync, no captions): Michael: « Il manque cinq euros. »
CAMERA: macro slider on coins → close-up face → insert on paper → static medium, headlamp flicker.
LIGHT & GRADE: single headlamp beam, blue fridge glow, deep black background.
AUDIO: coin clinks, paper rustle, heist bass pulse (original), fridge hum, lamp flicker buzz.
PHYSICS: realistic body weight, no morphing, no sliding feet, correct hands and fingers, no extra limbs. SKIN: preserve Michael's natural skin and features from @Image 1, no smoothing, no plastic look. NO-IP: no brands, no logos, no readable text, no captions or subtitles, no recognizable songs, no real celebrity likeness, no minors. Keep Michael's face, hair, build and outfit identical through the whole clip. Sharp, clean, cinematic render.
```

## SEEDANCE 02 — Trois heures du matin

*Il recompte toute la nuit, le billet était dans sa poche*

```text
REF: Michael = @Image 1 (face, hair, build) + @Image 2 (season outfit), keep identical. Location = @Image 3.
FORMAT: 9:16, 10 s, 4 shots, realistic comedy shot like a heist movie.
SCENE: Same bar, same headlamp; a wall clock hands move through the night.
ACTION:
0–2 s: Michael recounts, the clock reads midnight.
2–5 s: time-lapse montage: clock at one, he recounts wearing dish gloves; clock at two, he lies on the floor with coins aligned in a line; clock at three, he sleeps with his cheek on the drawer.
5–8 s: he jolts awake, slaps his apron pocket, slowly pulls out a folded banknote; crisp paper sound.
8–10 s: close-up; he looks at the note, then at the camera; he switches off the headlamp; black.
DIALOGUE (spoken French, slow and clear, natural lip-sync, no captions): Michael: « Ah. C'est moi. »
CAMERA: medium → fast time-lapse cuts → insert on the pocket → close-up → cut to black.
LIGHT & GRADE: headlamp only, night blue, dawn grey creeping in at the end.
AUDIO: clock ticking accelerated, coin clinks, snore, banknote crisp, click of the lamp.
PHYSICS: realistic body weight, no morphing, no sliding feet, correct hands and fingers, no extra limbs. SKIN: preserve Michael's natural skin and features from @Image 1, no smoothing, no plastic look. NO-IP: no brands, no logos, no readable text, no captions or subtitles, no recognizable songs, no real celebrity likeness, no minors. Keep Michael's face, hair, build and outfit identical through the whole clip. Sharp, clean, cinematic render.
```

## CLAUDE CODE — 10 s (outro ep05)

**Voix off** : « La clôture de caisse, c'est deux minutes, pas deux heures. FoodEatUp calcule l'écart pour vous. »

```text
Tu es motion designer. Crée avec Remotion (React) une composition verticale 1080×1920, 30 fps,
300 images (10 s), export MP4 H.264, fichier ep05-outro.mp4.

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
2–4 s : les pièces éparpillées glissent et se rangent en colonnes par mode de paiement : espèces, carte, en ligne.
4–7 s : écran Caisse : session ouverte le matin (fond de caisse) → rapport X en cours de journée → clôture Z en un tap : total par mode, comptage espèces, « écart » affiché automatiquement.
7–9 s : cartes : Caisse · Session de caisse · Rapport Z · Paiements.
Modules affichés en cartes (7–9 s) : Caisse · Session de caisse · Rapport Z · Paiements
Texte à l'écran : « Clôture Z : 2 minutes. Écart : calculé. »
Voix off (démarre à 2,0 s, finie avant 9,0 s) : « La clôture de caisse, c'est deux minutes, pas deux heures. FoodEatUp calcule l'écart pour vous. »
SFX : clink par colonne, tick de clôture, impact final.

RÈGLES : L'animation se comprend sans le son. Texte ≥ 64 px, ≤ 6 mots par écran, zone sûre TikTok/Reels/Shorts (marges 220 px haut, 320 px bas, 120 px côtés). Jamais de faux texte d'interface : uniquement les libellés réels. La voix off démarre à 2,0 s et finit avant 9,0 s. Un SFX par apparition ; motion blur sur les zooms. Rendu premium SaaS, humoristique, moderne, lisible sur smartphone.

SORTIES : ep05-outro.mp4 · ep05-outro-muet.mp4 · ep05-thumb.png
Titre de la miniature : « Le casse ».
```

## Contrôle avant publication

- [ ] Michael : même visage, même coiffure, même tenue sur les deux scènes.
- [ ] Aucun texte lisible généré par Seedance (enseigne, ticket, écran, sous-titre).
- [ ] Chaque réplique est compréhensible sans sous-titres.
- [ ] La chute est claire avant la fin de la scène 2 et Michael regarde la caméra.
- [ ] Le clap « COUPEZ ! » arrive à 0,4 s de l'outro.
- [ ] Modules affichés : Caisse · Session de caisse · Rapport Z · Paiements — libellés réels vérifiés.
- [ ] Logo FoodEatUp intact, centré, seul à l'écran de 9 à 10 s.
- [ ] La vidéo se comprend sans le son.

---
Source : `episodes/` + `saison.json` — fiche générée par `scripts/build.mjs`, ne pas éditer à la main.
