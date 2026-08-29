# ÉPISODE 19 — « LA COURSE-POURSUITE »

🎬 **Genre** : Film de course-poursuite / road movie
🍽️ **Situation** : Le livreur tourne à droite trois fois et finit dans un champ
⚙️ **Module** : Livraison (zones)
🎯 **Hook (0–2 s)** : Caméra embarquée sur le scooter, voix GPS : « Tournez à droite. »

## Sélecteurs Higgsfield

| Époque | Genre | Lumière | Physique | Objectif | Émotion | Montage |
|---|---|---|---|---|---|---|
| 2020s | action / poursuite | jour couvert puis pluie, angle embarqué | réaliste | ultra grand-angle type caméra d'action | adrénaline → dépit | 4 plans |

> Le look du film se règle dans ces sélecteurs : ne le répétez pas dans le texte du prompt.

## SEEDANCE 01 — C'est pas ici

*Trois virages à droite, une vache*

```text
REF: Michael = @Image 1 (face, hair, build) + @Image 2 (season outfit) + a delivery helmet, keep identical. Location = city streets then a country lane.
FORMAT: 9:16, 10 s, 4 shots, realistic comedy shot like a chase movie.
SCENE: Michael on a delivery scooter with an insulated bag, chase music, action-camera mounted on the handlebar; a calm female GPS voice.
ACTION:
0–2 s: handlebar POV, the GPS gives an instruction, Michael turns right into an alley.
2–5 s: the GPS repeats; he turns right onto a dirt track; the GPS repeats; he turns right again.
5–8 s: he brakes in front of a field; a cow looks at him; the GPS announces arrival.
8–10 s: rain begins; Michael lifts his visor and asks the camera.
DIALOGUE (spoken French, slow and clear, natural lip-sync, no captions): GPS: « Tournez à droite. » (x3) GPS: « Vous êtes arrivé. » Michael: « C'est pas ici. » Michael: « Elle est où, la rue ? »
CAMERA: handlebar POV → low tracking on the wheel → wide on the field with the cow → close-up through the visor.
LIGHT & GRADE: flat grey daylight, mud and green, rain drops on the lens.
AUDIO: chase drums (original), scooter engine, GPS voice, gravel, a cow, first rain.
PHYSICS: realistic body weight, no morphing, no sliding feet, correct hands and fingers, no extra limbs. SKIN: preserve Michael's natural skin and features from @Image 1, no smoothing, no plastic look. NO-IP: no brands, no logos, no readable text, no captions or subtitles, no recognizable songs, no real celebrity likeness, no minors. Keep Michael's face, hair, build and outfit identical through the whole clip. Sharp, clean, cinematic render.
```

## SEEDANCE 02 — Trente kilomètres

*La pizza livrée à la mauvaise famille, ravie*

```text
REF: Michael = @Image 1 (face, hair, build) + @Image 2 (season outfit) + a delivery helmet, keep identical. Location = suburban street in the rain.
FORMAT: 9:16, 10 s, 4 shots, realistic comedy shot like a chase movie.
SCENE: Michael soaked on the scooter, phone ringing in the rain.
ACTION:
0–2 s: he answers under the rain; the customer's voice crackles.
2–5 s: fast montage: a bridge, the same roundabout three times, an industrial zone, a market; the pizza box goes soggy.
5–8 s: he finally rings at a house; an adult couple opens, delighted, takes the pizza; Michael asks; they answer and close the door.
8–10 s: Michael, dripping, faces the camera; the phone rings again.
DIALOGUE (spoken French, slow and clear, natural lip-sync, no captions): Customer (phone): « Elle est où, ma pizza ? » Michael: « Elle arrive. » Couple: « Une pizza ! » Michael: « C'est pas vous ? » Couple: « Non. Merci ! » Michael: « Trente kilomètres. »
CAMERA: close-up on the phone → speed-ramped montage → medium at the door → close-up, ring.
LIGHT & GRADE: rain-soaked blue-grey, warm doorway light.
AUDIO: rain, phone crackle, engine, roundabout loop whoosh, doorbell, door slam, ringtone.
PHYSICS: realistic body weight, no morphing, no sliding feet, correct hands and fingers, no extra limbs. SKIN: preserve Michael's natural skin and features from @Image 1, no smoothing, no plastic look. NO-IP: no brands, no logos, no readable text, no captions or subtitles, no recognizable songs, no real celebrity likeness, no minors. Keep Michael's face, hair, build and outfit identical through the whole clip. Sharp, clean, cinematic render.
```

## CLAUDE CODE — 10 s (outro ep19)

**Voix off** : « Livrez là où vous livrez, pas plus loin. FoodEatUp définit vos zones, vos frais, et suit chaque commande. »

```text
Tu es motion designer. Crée avec Remotion (React) une composition verticale 1080×1920, 30 fps,
300 images (10 s), export MP4 H.264, fichier ep19-outro.mp4.

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
2–4 s : le trajet en spaghetti du scooter se redresse en une carte avec des zones colorées.
4–7 s : écran Livraison : zones par codes postaux, frais et minimum de commande par zone ; une commande hors zone est refusée automatiquement ; une commande en zone passe « en préparation → en livraison → livrée ».
7–9 s : cartes : Livraison · Zones de livraison · Commandes.
Modules affichés en cartes (7–9 s) : Livraison · Zones de livraison · Commandes
Texte à l'écran : « Vos zones. Vos règles. Vos livraisons. »
Voix off (démarre à 2,0 s, finie avant 9,0 s) : « Livrez là où vous livrez, pas plus loin. FoodEatUp définit vos zones, vos frais, et suit chaque commande. »
SFX : tick par zone, notification livrée, impact final.

RÈGLES : L'animation se comprend sans le son. Texte ≥ 64 px, ≤ 6 mots par écran, zone sûre TikTok/Reels/Shorts (marges 220 px haut, 320 px bas, 120 px côtés). Jamais de faux texte d'interface : uniquement les libellés réels. La voix off démarre à 2,0 s et finit avant 9,0 s. Un SFX par apparition ; motion blur sur les zooms. Rendu premium SaaS, humoristique, moderne, lisible sur smartphone.

SORTIES : ep19-outro.mp4 · ep19-outro-muet.mp4 · ep19-thumb.png
Titre de la miniature : « La course-poursuite ».
```

## Contrôle avant publication

- [ ] Michael : même visage, même coiffure, même tenue sur les deux scènes.
- [ ] Aucun texte lisible généré par Seedance (enseigne, ticket, écran, sous-titre).
- [ ] Chaque réplique est compréhensible sans sous-titres.
- [ ] La chute est claire avant la fin de la scène 2 et Michael regarde la caméra.
- [ ] Le clap « COUPEZ ! » arrive à 0,4 s de l'outro.
- [ ] Modules affichés : Livraison · Zones de livraison · Commandes — libellés réels vérifiés.
- [ ] Logo FoodEatUp intact, centré, seul à l'écran de 9 à 10 s.
- [ ] La vidéo se comprend sans le son.

---
Source : `episodes/` + `saison.json` — fiche générée par `scripts/build.mjs`, ne pas éditer à la main.
