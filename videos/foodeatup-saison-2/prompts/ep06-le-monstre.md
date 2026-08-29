# ÉPISODE 06 — « LE MONSTRE »

🎬 **Genre** : Film de monstre géant
🍽️ **Situation** : Michael a commandé « dix », il reçoit dix palettes d'oignons
⚙️ **Module** : Commandes fournisseurs + Réception
🎯 **Hook (0–2 s)** : Tous les verres tremblent, une ombre géante passe sur la façade.

## Sélecteurs Higgsfield

| Époque | Genre | Lumière | Physique | Objectif | Émotion | Montage |
|---|---|---|---|---|---|---|
| 2020s | film de monstre | matin gris, angle contre-plongée | hyperbolique | 18 mm ultra grand-angle | effroi comique | 4 plans |

> Le look du film se règle dans ces sélecteurs : ne le répétez pas dans le texte du prompt.

## SEEDANCE 01 — Dix palettes

*Le camion recule, la montagne d'oignons descend, Michael la contemple*

```text
REF: Michael = @Image 1 (face, hair, build) + @Image 2 (season outfit), keep identical. Location = @Image 3.
FORMAT: 9:16, 10 s, 4 shots, realistic comedy shot like a giant-monster movie.
SCENE: Quiet morning, Michael arranging glasses behind the bar; outside, a delivery truck reverses with a beeping alarm.
ACTION:
0–2 s: one glass trembles, then all of them; a deep rumble; a giant shadow slides across the window.
2–5 s: Michael steps outside; extreme low angle: a mountain of onion pallets descends from the truck on a lift, towering over him.
5–8 s: an adult courier in a hi-vis vest with a tablet confirms flatly; Michael protests; the courier repeats.
8–10 s: the camera tilts up the onion mountain to the sky; Michael's voice, tiny, from below.
DIALOGUE (spoken French, slow and clear, natural lip-sync, no captions): Courier: « Dix palettes. » Michael: « J'ai dit dix. » Courier: « Dix palettes. » Michael (small): « …oignons. »
CAMERA: macro on glasses → dolly out through the door → extreme low angle → slow tilt up.
LIGHT & GRADE: overcast grey, monster-movie contrast, the truck lights cutting through.
AUDIO: glass rattle, sub-bass rumble, reversing beep, hydraulic lift, onion nets creaking, orchestral sting (original).
PHYSICS: realistic body weight, no morphing, no sliding feet, correct hands and fingers, no extra limbs. SKIN: preserve Michael's natural skin and features from @Image 1, no smoothing, no plastic look. NO-IP: no brands, no logos, no readable text, no captions or subtitles, no recognizable songs, no real celebrity likeness, no minors. Keep Michael's face, hair, build and outfit identical through the whole clip. Sharp, clean, cinematic render.
```

## SEEDANCE 02 — C'est les oignons

*La cuisine ensevelie, Michael gravit la montagne en pleurant*

```text
REF: Michael = @Image 1 (face, hair, build) + @Image 2 (season outfit), keep identical. Location = @Image 4.
FORMAT: 9:16, 10 s, 4 shots, realistic comedy shot like a giant-monster movie.
SCENE: The kitchen buried under nets of onions up to the ceiling.
ACTION:
0–2 s: Michael's hand bursts out of the onions; he surfaces as if swimming.
2–5 s: heroic slow motion: he climbs the onion mountain, onions tumbling down around him, fists in the nets.
5–8 s: at the summit, tears streaming, he faces the camera and denies crying.
8–10 s: another pallet slides in through the kitchen window and stops right next to him; he stares at it.
DIALOGUE (spoken French, slow and clear, natural lip-sync, no captions): Michael: « Je pleure pas. » (sniff) « C'est les oignons. » Michael: « Non. »
CAMERA: insert on the hand → slow-motion low angle climb → close-up at the top → wide as the pallet arrives.
LIGHT & GRADE: kitchen fluorescents, onion skins golden in the light, dramatic contrast.
AUDIO: onions rolling, net creaks, heroic orchestral swell (original), sniff, pallet thud, silence.
PHYSICS: realistic body weight, no morphing, no sliding feet, correct hands and fingers, no extra limbs. SKIN: preserve Michael's natural skin and features from @Image 1, no smoothing, no plastic look. NO-IP: no brands, no logos, no readable text, no captions or subtitles, no recognizable songs, no real celebrity likeness, no minors. Keep Michael's face, hair, build and outfit identical through the whole clip. Sharp, clean, cinematic render.
```

## CLAUDE CODE — 12 s (outro ep06 : 2 s de transition + 10 s d'animation)

**Voix off — transition** (commune aux 30 épisodes, à 2,1 s) : « Cette scène aurait pu être évitée ? »

**Voix off — épisode** (à 4,6 s) : « Dix, c'est dix. FoodEatUp fixe l'unité, la quantité et la date avant que le camion recule. »

```text
Tu es motion designer. Crée avec Remotion (React) une composition verticale 1080×1920, 30 fps,
300 images (10 s), export MP4 H.264, fichier ep06-outro.mp4.

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
2–4 s : la montagne d'oignons se réduit au chiffre « 10 » qui se corrige : 10 kg / 10 pièces / 10 palettes, l'unité juste s'allume.
4–7 s : écran Commandes fournisseurs : ligne produit, quantité, unité, date prévue → à la livraison, Réception en un tap (contrôle à l'arrivée) → le stock se met à jour.
7–9 s : cartes : Fournisseurs · Commandes fournisseurs · Réception · Stock.
Modules affichés en cartes (7–9 s) : Fournisseurs · Commandes fournisseurs · Réception · Stock
Texte à l'écran : « Commandez juste. Recevez juste. »
Voix off de l'épisode (démarre à 4,6 s, finie avant 11,0 s) : « Dix, c'est dix. FoodEatUp fixe l'unité, la quantité et la date avant que le camion recule. »
SFX : tick unité, whoosh réception, impact final.

RÈGLES : L'animation se comprend sans le son. Texte ≥ 64 px, ≤ 6 mots par écran, zone sûre TikTok/Reels/Shorts (marges 220 px haut, 320 px bas, 120 px côtés). Jamais de faux texte d'interface : uniquement les libellés réels. Deux lignes de voix off : la punchline de transition à 2,1 s, puis la voix de l'épisode à 4,6 s, terminée avant 11,0 s. Un SFX par apparition ; motion blur sur les zooms. Rendu premium SaaS, humoristique, moderne, lisible sur smartphone.

SORTIES : ep06-outro.mp4 · ep06-outro-muet.mp4 · ep06-thumb.png
Titre de la miniature : « Le monstre ».
```

## Contrôle avant publication

- [ ] Michael : même visage, même coiffure, même tenue sur les deux scènes.
- [ ] Aucun texte lisible généré par Seedance (enseigne, ticket, écran, sous-titre).
- [ ] Chaque réplique est compréhensible sans sous-titres.
- [ ] La chute est claire avant la fin de la scène 2 et Michael regarde la caméra.
- [ ] Le clap « COUPEZ ! » arrive à 0,4 s de l'outro.
- [ ] Modules affichés : Fournisseurs · Commandes fournisseurs · Réception · Stock — libellés réels vérifiés.
- [ ] Logo FoodEatUp intact, centré, seul à l'écran de 9 à 10 s.
- [ ] La vidéo se comprend sans le son.

---
Source : `episodes/` + `saison.json` — fiche générée par `scripts/build.mjs`, ne pas éditer à la main.
