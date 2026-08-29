# ÉPISODE 21 — « LE GÉNIE »

🎬 **Genre** : Drame du génie des mathématiques (formules sur la vitre)
🍽️ **Situation** : Douze personnes, douze additions séparées, le vin partagé en cinq
⚙️ **Module** : Caisse (note divisée, paiement partiel)
🎯 **Hook (0–2 s)** : « On paie séparément. » — « Bien sûr. »

## Sélecteurs Higgsfield

| Époque | Genre | Lumière | Physique | Objectif | Émotion | Montage |
|---|---|---|---|---|---|---|
| 2020s | drame | fin d'après-midi sur la vitrine, angle latéral | réaliste | 50 mm | obsession | 4 plans |

> Le look du film se règle dans ces sélecteurs : ne le répétez pas dans le texte du prompt.

## SEEDANCE 01 — Et le pain ?

*Michael couvre la vitrine de formules au marqueur*

```text
REF: Michael = @Image 1 (face, hair, build) + @Image 2 (season outfit), keep identical. Location = @Image 3 (window).
FORMAT: 9:16, 10 s, 4 shots, realistic comedy shot like a tormented-genius drama.
SCENE: A table of twelve adults finishing lunch; Michael with a whiteboard marker at the shop window.
ACTION:
0–2 s: a customer announces they pay separately; Michael smiles and agrees.
2–5 s: tormented-genius music; Michael writes columns, fractions and arrows on the window (abstract scribbles, not readable); the camera pulls back: the whole window is covered.
5–8 s: a customer adds the wine shared by five; Michael erases and rewrites; another adds the bread; he erases again.
8–10 s: extreme close-up on his bloodshot eyes; the marker squeaks; someone mentions the coffee.
DIALOGUE (spoken French, slow and clear, natural lip-sync, no captions): Customer: « On paie séparément. » Michael: « Bien sûr. » Customer: « Le vin, en cinq ? » Michael: « Cinq. » Customer: « Et le pain ? » Michael: « Le pain… aussi. » Customer: « Et le café ? »
CAMERA: two-shot → slow pull-back from the window → inserts on erasing → extreme close-up on eyes.
LIGHT & GRADE: warm low sun through the glass, marker lines backlit.
AUDIO: piano motif (original), marker squeaks, sleeve erasing glass, murmurs, a spoon on a cup.
PHYSICS: realistic body weight, no morphing, no sliding feet, correct hands and fingers, no extra limbs. SKIN: preserve Michael's natural skin and features from @Image 1, no smoothing, no plastic look. NO-IP: no brands, no logos, no readable text, no captions or subtitles, no recognizable songs, no real celebrity likeness, no minors. Keep Michael's face, hair, build and outfit identical through the whole clip. Sharp, clean, cinematic render.
```

## SEEDANCE 02 — Je paie pour tout le monde

*Douze moyens de paiement, la dernière phrase qui l'achève*

```text
REF: Michael = @Image 1 (face, hair, build) + @Image 2 (season outfit), keep identical. Location = @Image 3 (window).
FORMAT: 9:16, 10 s, 4 shots, realistic comedy shot like a tormented-genius drama.
SCENE: Dusk; Michael still at the window, marker worn to nothing; the twelve customers queue at the till, each holding something different: coins, a card, a cheque, a folded banknote as a paper plane.
ACTION:
0–2 s: pull-back on the covered window, Michael's shoulders sagging.
2–5 s: he announces amounts in a cracked voice as each customer pays.
5–8 s: the last customer steps up and offers to pay for everyone; silence.
8–10 s: Michael looks at the window, then at the camera, and gently collapses face-down on the table; the marker rolls away.
DIALOGUE (spoken French, slow and clear, natural lip-sync, no captions): Michael: « Vingt-quatre cinquante. » « Dix-huit. » « Trois euros vingt. » Last customer: « Je paie pour tout le monde. »
CAMERA: pull-back → medium on the queue → close-up on the last customer → slow tilt down as Michael collapses.
LIGHT & GRADE: blue dusk outside, warm lamps inside, marker lines catching light.
AUDIO: coins, card beep, cheque tear, paper plane whoosh, silence, soft thud, marker rolling.
PHYSICS: realistic body weight, no morphing, no sliding feet, correct hands and fingers, no extra limbs. SKIN: preserve Michael's natural skin and features from @Image 1, no smoothing, no plastic look. NO-IP: no brands, no logos, no readable text, no captions or subtitles, no recognizable songs, no real celebrity likeness, no minors. Keep Michael's face, hair, build and outfit identical through the whole clip. Sharp, clean, cinematic render.
```

## CLAUDE CODE — 10 s (outro ep21)

**Voix off** : « Douze personnes, une note, zéro migraine. FoodEatUp divise la note par article, par personne ou en parts égales. »

> ⚠️ Cette phrase dépasse la fenêtre de 7 s (2,0 s → 9,0 s) à débit posé.
> **Variante courte proposée** : « Douze personnes, une note, zéro migraine. FoodEatUp divise par article, par personne ou en parts égales. »

```text
Tu es motion designer. Crée avec Remotion (React) une composition verticale 1080×1920, 30 fps,
300 images (10 s), export MP4 H.264, fichier ep21-outro.mp4.

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
2–4 s : la vitrine couverte de formules s'efface d'un coup ; une seule note de table apparaît.
4–7 s : écran Caisse : note de la table → « diviser » : par article, par personne, ou en parts égales ; paiements partiels par plusieurs moyens ; reste dû et rendu affichés.
7–9 s : cartes : Caisse · Paiements · Commandes · Tables.
Modules affichés en cartes (7–9 s) : Caisse · Paiements · Commandes · Tables
Texte à l'écran : « Divisez la note. Pas vos nerfs. »
Voix off (démarre à 2,0 s, finie avant 9,0 s) : « Douze personnes, une note, zéro migraine. FoodEatUp divise la note par article, par personne ou en parts égales. »
SFX : effacement, tick par part, impact final.

RÈGLES : L'animation se comprend sans le son. Texte ≥ 64 px, ≤ 6 mots par écran, zone sûre TikTok/Reels/Shorts (marges 220 px haut, 320 px bas, 120 px côtés). Jamais de faux texte d'interface : uniquement les libellés réels. La voix off démarre à 2,0 s et finit avant 9,0 s. Un SFX par apparition ; motion blur sur les zooms. Rendu premium SaaS, humoristique, moderne, lisible sur smartphone.

SORTIES : ep21-outro.mp4 · ep21-outro-muet.mp4 · ep21-thumb.png
Titre de la miniature : « Le génie ».
```

## Contrôle avant publication

- [ ] Michael : même visage, même coiffure, même tenue sur les deux scènes.
- [ ] Aucun texte lisible généré par Seedance (enseigne, ticket, écran, sous-titre).
- [ ] Chaque réplique est compréhensible sans sous-titres.
- [ ] La chute est claire avant la fin de la scène 2 et Michael regarde la caméra.
- [ ] Le clap « COUPEZ ! » arrive à 0,4 s de l'outro.
- [ ] Modules affichés : Caisse · Paiements · Commandes · Tables — libellés réels vérifiés.
- [ ] Logo FoodEatUp intact, centré, seul à l'écran de 9 à 10 s.
- [ ] La vidéo se comprend sans le son.

---
Source : `episodes/` + `saison.json` — fiche générée par `scripts/build.mjs`, ne pas éditer à la main.
