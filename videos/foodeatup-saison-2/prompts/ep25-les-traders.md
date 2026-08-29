# ÉPISODE 25 — « LES TRADERS »

🎬 **Genre** : Salle des marchés (trois téléphones, panique boursière)
🍽️ **Situation** : Le téléphone qui sonne pendant le rush
⚙️ **Module** : Agent vocal
🎯 **Hook (0–2 s)** : Trois téléphones, un dans chaque main, un sur l'épaule : « Allô ? Oui. Allô ? Oui. »

## Sélecteurs Higgsfield

| Époque | Genre | Lumière | Physique | Objectif | Émotion | Montage |
|---|---|---|---|---|---|---|
| 2020s | thriller financier | néon froid + lampes clignotantes, angle frontal | réaliste | 35 mm | frénésie | 4 plans |

> Le look du film se règle dans ces sélecteurs : ne le répétez pas dans le texte du prompt.

## SEEDANCE 01 — Je vends quoi, là ?

*Michael jongle avec les appels comme un trader*

```text
REF: Michael = @Image 1 (face, hair, build) + @Image 2 (season outfit), keep identical. Location = @Image 3 (counter).
FORMAT: 9:16, 10 s, 4 shots, realistic comedy shot like a trading-floor thriller.
SCENE: Rush hour; Michael behind the counter with three phones: one in each hand, one wedged on his shoulder; blinking lamps behind him like a trading board (no readable text).
ACTION:
0–2 s: he answers two phones at once, rapid fire.
2–5 s: he answers the third; then a wrong number.
5–8 s: all three phones ring together; he juggles them; a customer at the counter raises a hand; the chef shouts from the kitchen.
8–10 s: Michael, a phone at each ear, asks the camera.
DIALOGUE (spoken French, slow and clear, natural lip-sync, no captions): Michael: « Allô ? Oui. Une table pour deux. » « Allô ? Oui. Une pizza. » « Allô ? Non. C'est pas le garage. » Michael: « Je vends quoi, là ? »
CAMERA: fast push-in → alternating close-ups on each phone → wide with the customer and the chef → tight close-up.
LIGHT & GRADE: cold fluorescents, blinking coloured lamps, high energy.
AUDIO: three ringtones layered, ticker-like clicks, chatter, chef shouting, comic sting.
PHYSICS: realistic body weight, no morphing, no sliding feet, correct hands and fingers, no extra limbs. SKIN: preserve Michael's natural skin and features from @Image 1, no smoothing, no plastic look. NO-IP: no brands, no logos, no readable text, no captions or subtitles, no recognizable songs, no real celebrity likeness, no minors. Keep Michael's face, hair, build and outfit identical through the whole clip. Sharp, clean, cinematic render.
```

## SEEDANCE 02 — Elle a sonné

*Il décroche une spatule, puis un tire-bouchon, puis sa chaussure*

```text
REF: Michael = @Image 1 (face, hair, build) + @Image 2 (season outfit), keep identical. Location = @Image 3 (counter).
FORMAT: 9:16, 10 s, 4 shots, realistic comedy shot like a trading-floor thriller.
SCENE: Same counter; the phones keep ringing.
ACTION:
0–2 s: by reflex he picks up… a spatula and answers it.
2–5 s: the chef appears in the doorway and points out the obvious; Michael defends himself.
5–8 s: fast montage: he answers a corkscrew, a salt shaker, his own shoe.
8–10 s: he puts everything down, sits on the floor behind the counter; the real phone rings; he looks at the camera.
DIALOGUE (spoken French, slow and clear, natural lip-sync, no captions): Michael: « Allô ? » Chef: « C'est une spatule. » Michael: « Elle a sonné. » Michael: « Je réponds plus. »
CAMERA: insert on the spatula → two-shot → jump-cut montage → low angle behind the counter, ring.
LIGHT & GRADE: cold fluorescents, warm doorway light on the chef.
AUDIO: ringtone, spatula « hello », shoe squeak, salt shaker rattle, ringtone continues, silence.
PHYSICS: realistic body weight, no morphing, no sliding feet, correct hands and fingers, no extra limbs. SKIN: preserve Michael's natural skin and features from @Image 1, no smoothing, no plastic look. NO-IP: no brands, no logos, no readable text, no captions or subtitles, no recognizable songs, no real celebrity likeness, no minors. Keep Michael's face, hair, build and outfit identical through the whole clip. Sharp, clean, cinematic render.
```

## CLAUDE CODE — 12 s (outro ep25 : 2 s de transition + 10 s d'animation)

**Voix off — transition** (commune aux 30 épisodes, à 2,1 s) : « Cette scène aurait pu être évitée ? »

**Voix off — épisode** (à 4,6 s) : « Le téléphone répond tout seul. L'agent vocal FoodEatUp prend la réservation ou la commande pendant que vous servez. »

> ⚠️ Cette phrase dépasse la fenêtre de 7 s (2,0 s → 9,0 s) à débit posé.
> **Variante courte proposée** : « Le téléphone répond tout seul. L'agent vocal FoodEatUp prend la réservation pendant que vous servez. »

```text
Tu es motion designer. Crée avec Remotion (React) une composition verticale 1080×1920, 30 fps,
300 images (10 s), export MP4 H.264, fichier ep25-outro.mp4.

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
2–4 s : les trois téléphones fusionnent en un seul appel entrant, pris automatiquement.
4–7 s : écran : l'Agent vocal répond → la réservation ou la commande est créée directement (canal « téléphone / agent vocal ») → notification à Michael, qui a les mains libres.
7–9 s : cartes : Agent vocal · Réservations · Commandes · Notifications.
Modules affichés en cartes (7–9 s) : Agent vocal · Réservations · Commandes · Notifications
Texte à l'écran : « Le téléphone répond. Vous servez. »
Voix off de l'épisode (démarre à 4,6 s, finie avant 11,0 s) : « Le téléphone répond tout seul. L'agent vocal FoodEatUp prend la réservation ou la commande pendant que vous servez. »
SFX : sonnerie coupée, tick de création, impact final.

RÈGLES : L'animation se comprend sans le son. Texte ≥ 64 px, ≤ 6 mots par écran, zone sûre TikTok/Reels/Shorts (marges 220 px haut, 320 px bas, 120 px côtés). Jamais de faux texte d'interface : uniquement les libellés réels. Deux lignes de voix off : la punchline de transition à 2,1 s, puis la voix de l'épisode à 4,6 s, terminée avant 11,0 s. Un SFX par apparition ; motion blur sur les zooms. Rendu premium SaaS, humoristique, moderne, lisible sur smartphone.

SORTIES : ep25-outro.mp4 · ep25-outro-muet.mp4 · ep25-thumb.png
Titre de la miniature : « Les traders ».
```

## Contrôle avant publication

- [ ] Michael : même visage, même coiffure, même tenue sur les deux scènes.
- [ ] Aucun texte lisible généré par Seedance (enseigne, ticket, écran, sous-titre).
- [ ] Chaque réplique est compréhensible sans sous-titres.
- [ ] La chute est claire avant la fin de la scène 2 et Michael regarde la caméra.
- [ ] Le clap « COUPEZ ! » arrive à 0,4 s de l'outro.
- [ ] Modules affichés : Agent vocal · Réservations · Commandes · Notifications — libellés réels vérifiés.
- [ ] Logo FoodEatUp intact, centré, seul à l'écran de 9 à 10 s.
- [ ] La vidéo se comprend sans le son.

---
Source : `episodes/` + `saison.json` — fiche générée par `scripts/build.mjs`, ne pas éditer à la main.
