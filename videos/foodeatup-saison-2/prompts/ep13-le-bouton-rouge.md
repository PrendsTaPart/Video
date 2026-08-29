# ÉPISODE 13 — « LE BOUTON ROUGE »

🎬 **Genre** : Thriller de salle de contrôle
🍽️ **Situation** : Michael envoie « -50 % ce soir »… à toute la ville
⚙️ **Module** : Campagnes + Segments RFM
🎯 **Hook (0–2 s)** : Une main au-dessus d'un gros bouton rouge : « Envoyer. »

## Sélecteurs Higgsfield

| Époque | Genre | Lumière | Physique | Objectif | Émotion | Montage |
|---|---|---|---|---|---|---|
| 2020s | thriller | écran rouge dans le noir, angle bas | réaliste (scène 1) / hyperbolique (scène 2) | 35 mm | euphorie → panique | 4 plans |

> Le look du film se règle dans ces sélecteurs : ne le répétez pas dans le texte du prompt.

## SEEDANCE 01 — Envoyer

*Le doigt hésite, la ville entière vibre*

```text
REF: Michael = @Image 1 (face, hair, build) + @Image 2 (season outfit), keep identical. Location = @Image 3 (back office corner).
FORMAT: 9:16, 10 s, 4 shots, realistic comedy shot like a control-room thriller.
SCENE: A dark back office, Michael's face lit red by a screen (no readable text), a chunky physical red button on the desk.
ACTION:
0–2 s: Michael announces his offer to himself, hand hovering over the button.
2–5 s: macro on the hesitating finger, a slow alarm pulse; he closes his eyes and presses.
5–8 s: rapid montage across the city: phones buzzing on a café table, in a bus, in a jogger's pocket, on a construction site, in a waiting room.
8–10 s: back to Michael, satisfied smile.
DIALOGUE (spoken French, slow and clear, natural lip-sync, no captions): Michael: « Moins cinquante. Ce soir. » Michael: « Envoyer. » Michael: « Ça va marcher. »
CAMERA: low medium in red light → macro on the finger → five fast cutaways → close-up.
LIGHT & GRADE: red monitor glow, black surroundings, city cutaways in natural light.
AUDIO: alarm pulse, button click with reverb, wave of phone buzzes, distant notification chimes, smug exhale.
PHYSICS: realistic body weight, no morphing, no sliding feet, correct hands and fingers, no extra limbs. SKIN: preserve Michael's natural skin and features from @Image 1, no smoothing, no plastic look. NO-IP: no brands, no logos, no readable text, no captions or subtitles, no recognizable songs, no real celebrity likeness, no minors. Keep Michael's face, hair, build and outfit identical through the whole clip. Sharp, clean, cinematic render.
```

## SEEDANCE 02 — À tout le monde

*Une file de plusieurs centaines de personnes serpente dans le quartier*

```text
REF: Michael = @Image 1 (face, hair, build) + @Image 2 (season outfit), keep identical. Location = @Image 3 (entrance).
FORMAT: 9:16, 10 s, 4 shots, realistic comedy shot like a control-room thriller.
SCENE: Evening; aerial drone view of the restaurant with a queue of hundreds of adults snaking through the neighbourhood.
ACTION:
0–2 s: drone shot over the endless queue.
2–5 s: Michael opens the door, sees the queue, closes it, opens it again slowly.
5–8 s: the customer at the front explains; Michael asks; the customer repeats.
8–10 s: Michael looks at the camera; the crowd surges forward; zoom out.
DIALOGUE (spoken French, slow and clear, natural lip-sync, no captions): Customer: « Vous avez écrit à tout le monde. » Michael: « …à qui ? » Customer: « À tout le monde. » Michael: « Oups. »
CAMERA: drone top-down → medium at the door → two-shot → close-up with fast zoom out.
LIGHT & GRADE: blue hour, warm restaurant light spilling on the queue.
AUDIO: crowd murmur growing, door creak twice, crowd surge, comic sting.
PHYSICS: realistic body weight, no morphing, no sliding feet, correct hands and fingers, no extra limbs. SKIN: preserve Michael's natural skin and features from @Image 1, no smoothing, no plastic look. NO-IP: no brands, no logos, no readable text, no captions or subtitles, no recognizable songs, no real celebrity likeness, no minors. Keep Michael's face, hair, build and outfit identical through the whole clip. Sharp, clean, cinematic render.
```

## CLAUDE CODE — 10 s (outro ep13)

**Voix off** : « Envoyez à la bonne personne, pas à toute la ville. FoodEatUp segmente vos clients et vous montre le retour de chaque campagne. »

> ⚠️ Cette phrase dépasse la fenêtre de 7 s (2,0 s → 9,0 s) à débit posé.
> **Variante courte proposée** : « Envoyez à la bonne personne, pas à toute la ville. FoodEatUp segmente et mesure vos campagnes. »

```text
Tu es motion designer. Crée avec Remotion (React) une composition verticale 1080×1920, 30 fps,
300 images (10 s), export MP4 H.264, fichier ep13-outro.mp4.

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
2–4 s : l'explosion de notifications se replie en quatre groupes de clients : champions, réguliers, à risque, endormis.
4–7 s : écran Campagnes : choix du segment → canal (SMS, email, WhatsApp) → aperçu → confirmation en un tap → statistiques de retour (envoyés, clics, retours en commande).
7–9 s : cartes : Campagnes · Segments RFM · Clients.
Modules affichés en cartes (7–9 s) : Campagnes · Segments RFM · Clients
Texte à l'écran : « La bonne offre. Aux bons clients. »
Voix off (démarre à 2,0 s, finie avant 9,0 s) : « Envoyez à la bonne personne, pas à toute la ville. FoodEatUp segmente vos clients et vous montre le retour de chaque campagne. »
SFX : tick par segment, notification unique, impact final.

RÈGLES : L'animation se comprend sans le son. Texte ≥ 64 px, ≤ 6 mots par écran, zone sûre TikTok/Reels/Shorts (marges 220 px haut, 320 px bas, 120 px côtés). Jamais de faux texte d'interface : uniquement les libellés réels. La voix off démarre à 2,0 s et finit avant 9,0 s. Un SFX par apparition ; motion blur sur les zooms. Rendu premium SaaS, humoristique, moderne, lisible sur smartphone.

SORTIES : ep13-outro.mp4 · ep13-outro-muet.mp4 · ep13-thumb.png
Titre de la miniature : « Le bouton rouge ».
```

## Contrôle avant publication

- [ ] Michael : même visage, même coiffure, même tenue sur les deux scènes.
- [ ] Aucun texte lisible généré par Seedance (enseigne, ticket, écran, sous-titre).
- [ ] Chaque réplique est compréhensible sans sous-titres.
- [ ] La chute est claire avant la fin de la scène 2 et Michael regarde la caméra.
- [ ] Le clap « COUPEZ ! » arrive à 0,4 s de l'outro.
- [ ] Modules affichés : Campagnes · Segments RFM · Clients — libellés réels vérifiés.
- [ ] Logo FoodEatUp intact, centré, seul à l'écran de 9 à 10 s.
- [ ] La vidéo se comprend sans le son.

---
Source : `episodes/` + `saison.json` — fiche générée par `scripts/build.mjs`, ne pas éditer à la main.
