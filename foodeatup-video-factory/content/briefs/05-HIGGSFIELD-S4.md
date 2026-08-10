# Saison 4 — 30 prompts Higgsfield (EP91 → EP120)

Série FoodEatUp · hooks humoristiques 10 s · aucun crédit dépensé par Claude Code
Objectif série : 150 épisodes. Après cette saison : **120/150** (reste la saison 5, EP121 → EP150).

---

## 0. Rappel des réglages (identiques aux saisons 1–3)

- **Modèle** : Kling 3.0 (audio natif + multi-plan) ou Seedance 2.5 pour le photoréalisme pur.
- **Format** : 9:16 vertical · 10 s · 1080×1920.
- **Génération** : par toi, depuis l'UI Higgsfield. Claude Code ne lance **aucune** génération.
- **Nommage** : `EP91.mp4` … `EP120.mp4` dans `assets/hooks/`.

**Préfixe technique** (déjà inclus dans les 30 prompts) :
`Vertical 9:16, 10 seconds, photorealistic, cinematic handheld camera, shallow depth of field, natural light, 4K. NO text overlay, NO subtitles, NO watermark, NO logo, NO on-screen captions.`

**Les trois règles qui font que ça se monte tout seul**
1. Aucun texte dans l'image — le hook est incrusté en ffmpeg (corrigeable sans regénérer).
2. Beat comique entre **4,5 s et 6,5 s** — c'est là que tombe la punchline VO.
3. **Deux dernières secondes stables** — le master 30 s coupe à 7 s.

**Deux points de vigilance ajoutés en saison 4**
- **Personnages sous licence** : aucun nom de super-héros, de marque ou de personnage protégé dans un prompt (Higgsfield refuse ou floute, et c'est un risque juridique sur une vidéo commerciale). EP92 utilise donc un **super-héros générique masqué**, costume inventé, aucun logo — l'effet comique est identique et l'asset t'appartient.
- **Épisodes d'actualité** : EP94, EP95, EP96, EP98, EP111, EP113 ont une **date de péremption**. À publier en priorité (voir §3).

---

## 1. Les 30 épisodes en un coup d'œil

Vérifie cette liste contre tes EP49 → EP90 avant de générer : j'ai les saisons 1 et 2 sous les yeux, pas la 3. Si une ligne fait doublon, dis-le-moi et je la remplace.

| # | Titre | Ressort | Module FoodEatUp |
|---|---|---|---|
| EP91 | Le pétard dans le tiramisu | explosion / anniversaire | Réservation & événements |
| EP92 | Le super-héros qui a réservé | parodie / foule | Réservation |
| EP93 | Le chef part à la pêche | absurde | StockVision AI |
| EP94 | Le robot livreur qui double le scooter | actualité | HubRise & Livraisons |
| EP95 | L'éclipse de 13 h 12 | actualité | Service / KDS |
| EP96 | Canicule : le beurre fugueur | actualité | HACCP |
| EP97 | Le mur de tablettes | satire métier | HubRise & Livraisons |
| EP98 | Le robot serveur qui bugge et danse | actualité + trend | Service |
| EP99 | Le répondeur préhistorique | rétro / absurde | Caroline (IA vocale) |
| EP100 | L'influenceur au ring light | satire sociale | Marketing |
| EP101 | POV : thriller comptable | parodie de format | Comptabilité |
| EP102 | L'inspecteur surprise | panique comique | HACCP |
| EP103 | Le car de 40 sans réservation | invasion | Réservation |
| EP104 | Le no-show western | western / vide | Réservation |
| EP105 | Le duel de la dernière table | western | Réservation |
| EP106 | L'addition en quatorze parts | absurde | Caisse POS |
| EP107 | Le magicien de l'addition | magie | Caisse POS |
| EP108 | Le poulpe du pass | absurde animalier | KDS |
| EP109 | Le kombucha qui explose | tendance food | Stock / HACCP |
| EP110 | Le menu 100 % matcha | tendance food | Carte / Mon Site |
| EP111 | L'imprimante 3D qui déraille | actualité tech | Production |
| EP112 | Le casque de réalité augmentée | actualité tech | Mon Site / menu |
| EP113 | Le drone qui se trompe de balcon | actualité | HubRise & Livraisons |
| EP114 | La choré pendant que ça brûle | trend TikTok | Marketing |
| EP115 | Les poules du potager du toit | absurde animalier | StockVision AI |
| EP116 | Le stagiaire et le mur de craie | rétro / absurde | KDS |
| EP117 | Le plat étoilé en dix minutes | challenge viral | Fiches techniques |
| EP118 | La file du brunch | absurde social | Mon Site / Réservation |
| EP119 | La mascotte poulet et le vent | slapstick | Marketing |
| EP120 | La réunion des dix logiciels | absurde / message central | PrediBot |

---

## 2. Les prompts

### EP91 — Le pétard dans le tiramisu

**Prompt**
Vertical 9:16, 10 seconds, photorealistic, cinematic handheld camera, shallow depth of field, warm restaurant lighting, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A waiter carries a birthday tiramisu with a single sparkler candle across a dining room toward a table of guests already clapping. At 5 seconds the sparkler erupts into a full firework fountain, throwing bright sparks up to the ceiling; the guests recoil backwards in unison, one man's paper party hat tilts over his eyes. Final 2 seconds: the waiter stands perfectly still, dessert held level, face completely neutral, sparks still falling around him. Audio: restaurant ambience, scattered applause and a few voices humming happy birthday, a sudden loud fizzing roar of the firework, chairs scraping back, a surprised collective "Oh !", then only fizzing. No music.

**Hook** (0.8 → 3.5 s) : Anniversaire de table 12.
**Punchline VO** (5.0 s) : « Les surprises, c'est bien. Les imprévus, non. »
**Module** : Réservation & événements privés.

---

### EP92 — Le super-héros qui a réservé

**Prompt**
Vertical 9:16, 10 seconds, photorealistic, cinematic handheld camera, sunny terrace, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. IMPORTANT: an entirely generic, invented masked superhero — plain matte green and silver bodysuit, simple blank eye-mask, no emblem, no cape logo, no resemblance to any existing character. He arrives politely at the host stand of a busy restaurant terrace and points at a reservation notebook. At 5 seconds a crowd of thirty excited fans floods in behind him from off-frame, phones raised, filling the entire terrace within two seconds; a single young waiter is swallowed by the crowd, one arm holding a tray above his head like a periscope. Final 2 seconds: the superhero sits alone at a small table in the middle of the chaos, hands folded, waiting patiently. Audio: terrace ambience, a sudden roar of running footsteps and excited shouting, camera shutters, a tray wobbling, a lone waiter's voice saying "Attendez—", then the crowd noise settling into a hum. No music.

**Hook** : Lui, il avait réservé.
**Punchline VO** : « Ses quatre-vingts fans, non. »
**Module** : Réservation / liste d'attente.

---

### EP93 — Le chef part à la pêche

**Prompt**
Vertical 9:16, 10 seconds, photorealistic, cinematic, professional kitchen then window, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A chef opens the fish fridge: it is completely empty except for one sad lemon. He looks at a ticket in his hand, then at the empty fridge, then at the open kitchen window. At 5 seconds he is leaning out of that window in full chef whites and toque, casting a fishing rod into an ornamental carp pond in the courtyard, elbow resting on the sill. Final 2 seconds: the line goes taut, he braces, expression suddenly hopeful and completely serious. Audio: fridge fan hum, a paper ticket rustle, a long resigned exhale, a window latch, the whir of a fishing reel casting, a plop in water, then birdsong and a single reel click. No music.

**Hook** : Rupture de stock, 20 h 15.
**Punchline VO** : « Anticiper, c'est moins sportif. »
**Module** : StockVision AI.

---

### EP94 — Le robot livreur qui double le scooter

**Prompt**
Vertical 9:16, 10 seconds, photorealistic, low-angle street tracking shot, late afternoon light, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A delivery rider on a scooter with an insulated backpack is stuck in slow traffic on a French city street, foot down, visor up, sighing. At 5 seconds a small autonomous six-wheeled delivery robot the size of a suitcase glides smoothly past him in the bike lane, indicator light blinking politely. Final 2 seconds: the rider watches it disappear ahead; the robot stops at a pedestrian crossing and waits, perfectly law-abiding, while he is still stuck. Audio: idling engines, car horns, a resigned human sigh through a helmet, a quiet electric motor whirr and a soft robotic indicator beep, then traffic ambience. No music.

**Hook** : 2026, la livraison change de main.
**Punchline VO** : « Autant que tes commandes arrivent au bon endroit. »
**Module** : HubRise & Livraisons. *(Épisode d'actualité — arrêté du 7 août 2026 sur l'homologation des robots de livraison autonomes en France. À publier vite.)*

---

### EP95 — L'éclipse de 13 h 12

**Prompt**
Vertical 9:16, 10 seconds, photorealistic, wide then slow push-in, bright midday exterior with unusual dimming light, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A packed restaurant terrace at lunch. Every single guest at every table suddenly stops eating, puts on cardboard eclipse glasses and tilts their head straight up in unison, forks frozen mid-air. The light dims to an eerie silver. At 5 seconds a waiter arrives with three hot plates and stands in the middle of the terrace, holding them, looking at forty upturned faces, then up at the sky himself. Final 2 seconds: he lowers the plates onto an empty table, sits down on a spare chair and looks up too. Audio: terrace chatter falling to complete silence, cutlery set down, cardboard glasses rustling, birds going quiet, one child's "waouh", plates clinking softly on a table. No music.

**Hook** : Le service s'est arrêté deux minutes.
**Punchline VO** : « Le reste du temps, il ne devrait jamais s'arrêter. »
**Module** : Service / KDS. *(Actualité : éclipse du 12 août 2026 — publier autour de la date.)*

---

### EP96 — Canicule : le beurre fugueur

**Prompt**
Vertical 9:16, 10 seconds, photorealistic macro then medium, harsh summer light through a kitchen window, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. Close macro on a large block of butter sitting on a stainless pass, a small fan oscillating uselessly beside it. The butter is visibly slumping, then sliding, leaving a glossy trail across the metal. At 5 seconds it slides right off the edge and lands with a wet slap on the tiles; the camera widens to reveal a cook standing in the heat with a wet cloth on his neck, watching it happen without moving. Final 2 seconds: he looks at the fan, then at the camera, sweat on his forehead, completely defeated. Audio: fan motor droning, distant cicadas, a fridge compressor struggling, a slow greasy slide on metal, a wet slap, one long exhale. No music.

**Hook** : 39° en cuisine.
**Punchline VO** : « Une alerte température, et tu sauves la marchandise. »
**Module** : HACCP — relevés de températures.

---

### EP97 — Le mur de tablettes

**Prompt**
Vertical 9:16, 10 seconds, photorealistic, static wide then slow push-in, busy kitchen pass, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. Six different tablets and order terminals are mounted side by side on a shelf above a restaurant pass, each with a different generic interface colour, no readable text, no brand. They start chiming one after another, then all together, faster and faster. A manager stands in front of them holding a spatula, and at 5 seconds begins conducting them like an orchestra, sweeping the spatula in time with the chimes, deadly serious. Final 2 seconds: he stops conducting; every screen falls silent at once; he lowers the spatula slowly. Audio: kitchen ambience, six distinct notification chimes overlapping into a chaotic rhythm, escalating, then an abrupt collective silence and a single drip from a tap. No music.

**Hook** : Six plateformes. Six alertes.
**Punchline VO** : « Une seule commande, un seul écran. »
**Module** : HubRise & Livraisons.

---

### EP98 — Le robot serveur qui bugge et danse

**Prompt**
Vertical 9:16, 10 seconds, photorealistic, medium tracking shot in a modern dining room, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A wheeled humanoid service robot with a tray of drinks rolls smoothly between tables, guests watching, impressed. At 5 seconds it hits a small rug edge, freezes, its head twitches, and it begins performing a jerky, off-beat dance routine with the tray still perfectly level, glasses untouched. Final 2 seconds: it stops mid-pose, one arm up, and its status light turns from blue to red while a waiter walks calmly into frame and takes the tray off it. Audio: restaurant ambience, a smooth servo whirr, a sharp electronic glitch stutter, rhythmic servo clicking like a broken beat, guests laughing, a soft error chime, glass clinking as the tray is lifted. No music.

**Hook** : Ton nouveau serveur, en période d'essai.
**Punchline VO** : « L'IA, c'est utile quand elle sert à quelque chose. »
**Module** : Service.

---

### EP99 — Le répondeur préhistorique

**Prompt**
Vertical 9:16, 10 seconds, photorealistic, tight macro on a cluttered back-office desk, warm lamp light, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A 1990s cassette answering machine sits on a restaurant back-office desk next to a corded phone, its red light blinking furiously. The phone rings; the machine clicks and starts recording. At 5 seconds the little cassette door bursts open and a huge tangle of magnetic tape spills out and keeps unspooling across the desk and onto the floor, while the phone keeps ringing. Final 2 seconds: a hand enters frame, gently closes the office door on the whole mess, leaving the tape still unspooling. Audio: an old phone ringing, a plastic click and cassette whirr, muffled voices leaving messages layered on top of each other, tape unspooling with a papery hiss, a door closing softly, ringing continuing behind it. No music.

**Hook** : Quarante appels pendant le rush.
**Punchline VO** : « Quelqu'un devrait répondre. Ce ne sera pas toi. »
**Module** : Caroline (agent IA vocale).

---

### EP100 — L'influenceur au ring light

**Prompt**
Vertical 9:16, 10 seconds, photorealistic, over-the-shoulder then reverse, restaurant table, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A young man has set up a ring light, a tripod and a small reflector around a single plate of pasta on a restaurant table, and is filming it from twelve different angles, moving the plate, adjusting a basil leaf with tweezers. Steam stops rising from the dish. At 5 seconds he finally takes one bite — and grimaces, because it is stone cold. Final 2 seconds: he pushes the plate away and starts typing on his phone with one finger, expression sour, ring light still glowing on his face. Audio: restaurant ambience, tripod clicks, a phone shutter repeating, a chair adjusting, a small disappointed "mmh", then rapid soft phone typing. No music.

**Hook** : Il a mis vingt minutes à filmer.
**Punchline VO** : « Et deux minutes à te mettre deux étoiles. »
**Module** : Marketing / avis clients.

---

### EP101 — POV : thriller comptable

**Prompt**
Vertical 9:16, 10 seconds, photorealistic, extreme close-ups with dramatic thriller lighting and slow dolly moves, night back office, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. Shot like a psychological thriller: an extreme close-up of a trembling hand pushing a stack of paper invoices; a macro of a calculator key being pressed with enormous tension; a slow tilt up a restaurant owner's face lit from below by a laptop screen, jaw clenched, a bead of sweat. At 5 seconds he presses the equals key, stares at the result, and his shoulders drop three centimetres. Final 2 seconds: he closes the laptop very slowly and sits in the dark, perfectly still. Audio: deep ominous room tone, a clock ticking, paper sliding, one loud calculator click, a heartbeat rising then stopping dead, a laptop lid closing, silence. No music beyond the tension drone.

**Hook** : Rapprochement des caisses. Vendredi soir.
**Punchline VO** : « Ça devrait être une ligne, pas une enquête. »
**Module** : Comptabilité.

---

### EP102 — L'inspecteur surprise

**Prompt**
Vertical 9:16, 10 seconds, photorealistic, fast handheld, professional kitchen, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A person in a plain grey jacket carrying a clipboard walks slowly toward a kitchen's swinging door from the dining room. Cut inside: the entire brigade explodes into hyper-speed motion — containers stacked, a floor mopped, a thermometer plunged into a fridge, a hairnet yanked on, all in three seconds of frantic activity, then everyone freezes in perfect professional poses. At 5 seconds the door opens: it is only a delivery driver asking for a signature. Final 2 seconds: the entire brigade stays frozen in their poses, mop in the air, staring at him. Audio: calm dining room ambience, then an explosion of clattering, running footsteps, fridge doors, a mop slapping tiles, an abrupt total silence, a door creak, a casual "Bonjour, signature ?". No music.

**Hook** : Contrôle surprise. Ou pas.
**Punchline VO** : « Le jour où c'est le vrai, tu ne bouges pas. »
**Module** : HACCP.

---

### EP103 — Le car de 40 sans réservation

**Prompt**
Vertical 9:16, 10 seconds, photorealistic, wide exterior then interior reverse, small village restaurant, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A quiet restaurant with two occupied tables. Through the window, a large coach pulls up and stops with a hiss. At 5 seconds its doors open and forty tourists in matching caps stream out and walk in single file toward the entrance, one of them waving cheerfully. Final 2 seconds: interior shot of a lone waiter behind the bar, holding a single menu, watching the line come through the door, not moving a muscle. Audio: quiet restaurant ambience, a coach air-brake hiss, doors opening, a rising tide of cheerful chatter and footsteps, a bell above the door ringing repeatedly, then one very small "bonjour". No music.

**Hook** : Quarante couverts. Sans prévenir.
**Punchline VO** : « Prévenu, tu aurais dit oui. »
**Module** : Réservation.

---

### EP104 — Le no-show western

**Prompt**
Vertical 9:16, 10 seconds, photorealistic, wide static shot, elegant empty dining room, evening light, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A long table beautifully set for eight — folded napkins, polished glasses, a flower arrangement — completely empty in a silent restaurant. The camera holds. At 5 seconds a dry tumbleweed rolls slowly across the floor in front of the table, from one side of the frame to the other, as if in a western. Final 2 seconds: it comes to rest against a chair leg; a single candle flickers. Audio: deep empty-room reverb, a clock ticking, a faint whistling wind that should not exist indoors, dry rustling as the tumbleweed rolls, then a candle-flame flicker. No music.

**Hook** : Table de huit. 20 h 30.
**Punchline VO** : « Un no-show, ça se prévient. »
**Module** : Réservation.

---

### EP105 — Le duel de la dernière table

**Prompt**
Vertical 9:16, 10 seconds, photorealistic, western-style low-angle close-ups, sunlit terrace, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. Shot like a spaghetti-western standoff: two couples face each other across a restaurant terrace, one single free table between them. Extreme close-ups of narrowed eyes, a hand hovering near a jacket pocket, a bead of sweat, a napkin fluttering like a tumbleweed. At 5 seconds both men draw — their phones — and stab at a booking screen with one thumb, faster and faster. Final 2 seconds: one of them raises his phone in triumph; the other lowers his head; the winner's partner is already sitting down. Audio: terrace ambience, wind, a single suspended note of tension, exaggerated boot-scrape and leather creak, two rapid phone taps, a soft confirmation chime, a chair scraping. No music beyond the tension note.

**Hook** : Dernière table du samedi.
**Punchline VO** : « Le plus rapide gagne. Rends-la réservable en ligne. »
**Module** : Réservation / Mon Site.

---

### EP106 — L'addition en quatorze parts

**Prompt**
Vertical 9:16, 10 seconds, photorealistic, over-the-shoulder then reverse, long dinner table, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A waiter arrives at a long table of fourteen friends with the bill folder. Instantly fourteen hands shoot up holding fourteen bank cards, plus one person waving a handful of coins and another holding out a restaurant voucher. At 5 seconds the waiter is holding the card machine in one hand and a fan of fourteen cards in the other, like a poker hand, blinking. Final 2 seconds: he stares at the camera over the fan of cards, absolutely still, while a fifteenth hand enters frame with another card. Audio: cheerful table chatter, chairs, plastic cards tapping, coins jingling, a terminal beep, a rising confused murmur, then a single beep. No music.

**Hook** : « On peut payer chacun ? »
**Punchline VO** : « Oui. En trois secondes, pas en trente minutes. »
**Module** : Caisse POS.

---

### EP107 — Le magicien de l'addition

**Prompt**
Vertical 9:16, 10 seconds, photorealistic, medium shot, warm bistro lighting, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A guest in a slightly theatrical velvet jacket receives the bill folder, smiles, and makes an elaborate flourish over it with both hands, a napkin draped across the top like a magician. At 5 seconds he whips the napkin away — the folder is completely empty, and a white dove flaps up out of it toward the ceiling. Final 2 seconds: the waiter, unimpressed, calmly places a second identical bill folder on the table and walks away. Audio: bistro ambience, a theatrical fabric whoosh, wing flapping, one impressed gasp from a neighbouring table, then a flat cardboard tap as the second folder lands. No music.

**Hook** : Tout le monde a un tour.
**Punchline VO** : « Ta caisse, elle, ne perd jamais une addition. »
**Module** : Caisse POS.

---

### EP108 — Le poulpe du pass

**Prompt**
Vertical 9:16, 10 seconds, photorealistic, medium shot at a stainless pass, moody kitchen lighting, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A large live octopus sits calmly on the stainless steel pass of a professional kitchen wearing a tiny white chef's toque. Each of its arms holds a different tool — tongs, a squeeze bottle, a whisk, a ticket, a plate, a spoon — and all of them are moving competently at once. At 5 seconds a human chef steps into frame beside it holding two tools, looks at the octopus, then at his own two hands. Final 2 seconds: he sets his tools down and leans on the pass, watching it work, defeated but admiring. Audio: kitchen extractor hum, sizzling, rapid metallic tool clicking layered on itself, a wet suction sound, a spoon set down slowly, one human sigh. No music.

**Hook** : Il te faudrait six bras.
**Punchline VO** : « Ou un seul outil qui fait le reste. »
**Module** : KDS.

---

### EP109 — Le kombucha qui explose

**Prompt**
Vertical 9:16, 10 seconds, photorealistic, macro then medium, shelf of fermentation jars in a cellar, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A shelf of large glass fermentation jars filled with cloudy kombucha and pickles, lids straining. Macro on one lid trembling and bulging. A cook leans in slowly to inspect it, nose close to the glass. At 5 seconds that jar erupts, blasting foam straight up onto the ceiling and across his face and apron. Final 2 seconds: he stands dripping, eyes closed, while on the shelf behind him a second lid starts trembling. Audio: cellar room tone, a gas hiss building inside glass, a wet explosive pop, splattering and dripping, a startled inhale, then a second faint hiss beginning. No music.

**Hook** : Ta cave à ferments.
**Punchline VO** : « Suivie et datée, elle ne t'explose pas à la figure. »
**Module** : Stock / HACCP (DLC & traçabilité).

---

### EP110 — Le menu 100 % matcha

**Prompt**
Vertical 9:16, 10 seconds, photorealistic, top-down then eye-level, bright modern café, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A waiter places a plate in front of a guest: everything on it is vivid green — green latte, green bread, green sauce, a green steak, a green boiled egg. The guest looks at it, looks up at the waiter, looks back down. At 5 seconds he lifts a forkful, sniffs it, and eats it anyway. Final 2 seconds: he gives a small, genuinely surprised nod of approval, and the waiter immediately places a second identical green plate beside the first. Audio: café ambience, an espresso machine, ceramic on wood, a fork clink, a thoughtful chewing pause, a small "hm !", then another plate landing. No music.

**Hook** : Tu suis toutes les tendances.
**Punchline VO** : « Regarde surtout lesquelles se vendent. »
**Module** : Carte & analyse de rentabilité.

---

### EP111 — L'imprimante 3D qui déraille

**Prompt**
Vertical 9:16, 10 seconds, photorealistic macro, clean modern kitchen laboratory, cool light, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A food 3D printer extrudes a neat layer of purée onto a plate with clinical precision, watched by a chef with folded arms. At 5 seconds the nozzle begins moving erratically, extruding an ever-growing chaotic spaghetti tangle that rises off the plate and spills onto the counter, still perfectly smooth and glossy. Final 2 seconds: the chef reaches out and, with total calm, presses a single button; the machine stops, leaving a large edible sculpture of nothing at all. Audio: quiet lab hum, a precise servo whirr, a soft wet extrusion sound, the servo tempo becoming erratic, a rising mechanical whine, a button click, silence. No music.

**Hook** : La cuisine du futur.
**Punchline VO** : « Le futur utile, c'est celui qui te fait gagner du temps. »
**Module** : Production / fiches techniques.

---

### EP112 — Le casque de réalité augmentée

**Prompt**
Vertical 9:16, 10 seconds, photorealistic, medium shot, elegant restaurant, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A guest wearing a sleek generic augmented-reality headset (no brand, no logo) sits at a beautifully set table, reaching out with a fork toward something only he can see. His fork repeatedly stabs the tablecloth thirty centimetres to the left of his actual plate. At 5 seconds he brings the empty fork to his mouth with great satisfaction and chews on nothing. Final 2 seconds: a waiter quietly slides the real plate under his hovering fork; the guest's next stab hits food and he freezes, delighted. Audio: refined restaurant ambience, cutlery clicking on cloth and wood, a faint headset electronic hum, contented chewing, a plate sliding on linen, a soft "ah !". No music.

**Hook** : La carte du futur.
**Punchline VO** : « Ou juste une carte en ligne qui marche. »
**Module** : Mon Site / carte digitale.

---

### EP113 — Le drone qui se trompe de balcon

**Prompt**
Vertical 9:16, 10 seconds, photorealistic, exterior apartment building facade, late afternoon, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A delivery drone carrying a pizza box in a harness descends along an apartment building facade. On the third floor a customer waits on his balcony with both arms raised, ready. At 5 seconds the drone drifts two metres sideways and gently lowers the box onto the neighbour's balcony instead, where an elderly woman is watering her plants. Final 2 seconds: she picks up the box, opens it, looks at the pizza, then across at the customer, and nods once — she is keeping it. Audio: city ambience, rotor buzz rising and falling, a harness servo, a cardboard box settling, a watering can being set down, a very short delighted "oh !", the customer's distant "hé !". No music.

**Hook** : Livraison réussie. Presque.
**Punchline VO** : « Un suivi de commande, et personne ne mange ta pizza. »
**Module** : HubRise & Livraisons.

---

### EP114 — La choré pendant que ça brûle

**Prompt**
Vertical 9:16, 10 seconds, photorealistic, static phone-style frontal shot, professional kitchen, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. Four young kitchen staff line up shoulder to shoulder in front of a phone on a tripod and perform a tight, synchronised dance routine, grinning, fully committed. Behind them, out of focus, a pan on the stove starts smoking, then flames rise gently. At 5 seconds one of them notices in the reflection of a stainless surface but keeps dancing, eyes wide. Final 2 seconds: the routine ends on a pose; all four turn around at once and stare at the burning pan, still in formation. Audio: kitchen ambience, four pairs of shoes on tiles in rhythm, laughing and counting "cinq, six, sept, huit", a growing crackle and a smoke alarm starting to chirp, then silence on the freeze. No music track — rhythm carried by claps and footsteps.

**Hook** : Ton community manager, c'est ta brigade.
**Punchline VO** : « Poste. Mais garde un œil sur le service. »
**Module** : Marketing / réseaux sociaux.

---

### EP115 — Les poules du potager du toit

**Prompt**
Vertical 9:16, 10 seconds, photorealistic, rooftop garden with city skyline, golden hour, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A neat rooftop restaurant vegetable garden with labelled wooden crates of herbs and salad. A chef crouches, harvesting basil into a basket, proud. At 5 seconds a dozen chickens burst out from behind the crates and swarm the beds, scattering leaves and soil, one of them landing directly in his basket. Final 2 seconds: he stands up holding the basket with the chicken sitting comfortably inside it, looking at the camera; the beds behind him are bare. Audio: rooftop wind and distant city traffic, gentle clipping of herbs, a sudden explosion of clucking and flapping, soil scattering, then steady contented clucking. No music.

**Hook** : Circuit court, très court.
**Punchline VO** : « Compte ce qui rentre. Et ce qui sort. »
**Module** : StockVision AI.

---

### EP116 — Le stagiaire et le mur de craie

**Prompt**
Vertical 9:16, 10 seconds, photorealistic, wide shot of a kitchen wall, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A young intern writes orders in chalk directly onto a huge black kitchen wall — abstract marks, tally strokes and arrows only, absolutely no readable words or letters. The wall is already almost entirely covered. He climbs onto a milk crate to reach higher, then onto a chair on top of the crate. At 5 seconds he reaches the ceiling, still writing, chalk dust falling on his shoulders. Final 2 seconds: he looks down at the chef below him, who silently holds up a tablet-sized rectangle of blank white board. Audio: kitchen ambience, chalk squeaking on a wall, a crate scraping, wood creaking under weight, chalk dust settling, one calm cough from below. No music.

**Hook** : Ton système de commandes.
**Punchline VO** : « Il tient sur un mur. Il tiendrait sur un écran. »
**Module** : KDS.

---

### EP117 — Le plat étoilé en dix minutes

**Prompt**
Vertical 9:16, 10 seconds, photorealistic, fast handheld with quick whip-pans, professional kitchen, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A large kitchen timer is slammed onto the counter and a chef explodes into action: pans flying, sauce whisked, tweezers placing garnish, a blowtorch flaring, all in rapid succession, sweat flying. At 5 seconds the timer rings; he slides a stunning, immaculate gourmet plate into frame with both hands. Final 2 seconds: the camera pulls back to reveal the entire kitchen behind him utterly destroyed — every pan used, flour everywhere, a cupboard door hanging open — while he holds the perfect plate. Audio: a mechanical timer ticking loudly, frantic metallic clattering, a blowtorch hiss, plates scraping, an alarm bell ringing, then heavy breathing and one distant pan falling. No music.

**Hook** : Le défi à dix minutes.
**Punchline VO** : « Une fiche technique, et c'est dix minutes tous les jours. »
**Module** : Recettes & fiches techniques.

---

### EP118 — La file du brunch

**Prompt**
Vertical 9:16, 10 seconds, photorealistic, street-level tracking shot along a queue, early morning light, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. The camera tracks slowly along a long pavement queue outside a closed restaurant at dawn. The people are absurdly over-equipped: folding chairs, thermos flasks, a blanket, one small camping tent, a man doing stretches, a woman reading a novel already half finished. At 5 seconds the camera reaches the front of the queue: a man in a sleeping bag is sitting directly against the locked door. Final 2 seconds: a hand inside flips a small sign on the glass; the entire queue stands up at once in a single wave. Audio: quiet dawn street, birds, a thermos unscrewing, a tent zip, pages turning, a sleeping bag rustling, a metallic door bolt, then a collective shuffle of forty people standing up. No music.

**Hook** : Le brunch du dimanche.
**Punchline VO** : « Ils feraient la queue chez toi aussi. Encore faut-il pouvoir réserver. »
**Module** : Mon Site / Réservation.

---

### EP119 — La mascotte poulet et le vent

**Prompt**
Vertical 9:16, 10 seconds, photorealistic, handheld street shot, windy grey daylight, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A person in an oversized generic chicken mascot costume (plain yellow, no brand, no logo) hands out flyers on a pavement outside a restaurant, dancing awkwardly. A strong gust hits: the flyers explode out of their wing in a white cloud and the costume's huge tail acts like a sail, dragging the mascot backwards down the pavement in small hops, arms flailing. At 5 seconds it collides softly with a lamppost and wraps around it. Final 2 seconds: the mascot clings to the lamppost, motionless, as the last flyers drift past its beak. Audio: strong wind gusts, paper flapping and scattering, foam costume squeaking, small running steps, a soft padded thud on metal, one muffled human groan from inside the head. No music.

**Hook** : Ta stratégie d'acquisition.
**Punchline VO** : « Cinq cents tracts, zéro donnée. »
**Module** : Marketing.

---

### EP120 — La réunion des dix logiciels

**Prompt**
Vertical 9:16, 10 seconds, photorealistic, slow dolly along a long table, empty dining room, dramatic evening light, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A restaurant owner sits at the head of a long dining table set for a formal meeting. In each of the ten guest chairs sits an open laptop or tablet instead of a person, each screen showing a different abstract coloured interface with no readable text. He looks around at them expectantly and opens his hands as if to say "so?". At 5 seconds every screen simultaneously plays a different notification chime and then goes to a blank screensaver, one after another, ignoring him completely. Final 2 seconds: he lowers his hands, alone at the head of a table of dark screens, and pours himself a glass of water. Audio: empty room reverb, a chair creak, ten mismatched notification chimes overlapping, fans spinning down one by one, water pouring into a glass, then silence. No music.

**Hook** : Réunion de tes dix logiciels.
**Punchline VO** : « Ils ne se parlent toujours pas. FoodEatUp, si. »
**Module** : PrediBot / message central.

---

## 3. Ordre de publication recommandé

Les épisodes d'actualité se périment ; les autres sont evergreen.

1. **Cette semaine** : EP95 (éclipse du 12 août), EP94 (robots livreurs, arrêté du 7 août), EP96 (canicule).
2. **Août–septembre** : EP98, EP113, EP111, EP112 (vague tech/IA), EP118, EP114.
3. **Evergreen, à répartir** : tous les autres. Garde EP120 pour un temps fort — c'est le plus « pitch ».

Alternance conseillée sur le feed : 1 animal/absurde → 1 satire métier → 1 tech/actualité. Ça évite l'effet catalogue.

---

## 4. Ce que j'ai trouvé dans ton Drive (et comment Claude Code s'en sert)

Le dossier partagé contient **14 modules Academy**, chacun découpé en sous-chapitres de vidéos écran. Ce sont tes assets de démo pour le segment « animation 10-15 s ». IDs à mettre dans la config de Claude Code :

| Module | ID dossier Drive |
|---|---|
| 1 — Configuration (14 vidéos) | `19xTrrkXtWO3yfJqtC3SIlDgpBjSEc4N9` |
| 2 — Équipe & Planning (20 vidéos) | `1wboT7bVjEwxbhpU9Xgz8sRjjqn9XEd7X` |
| 3 — Comptabilité (10 vidéos) | `1KlXihMLILGDrlxDuO2d3VCe1ic-kCAw_` |
| 4 — HACCP (30 vidéos) | `10rqzHFjXbjkGi73uJyjt3XQM92eaIMK_` |
| 5 — StockVision AI (20 vidéos) | `1Ib_pKyJ8_jaFAwtIhkzhtmUU_DCtGSSY` |
| 6 — Mon Site | `1ykcHl2BaY22WlCsBA3DuwXaEMvQZUtMF` |
| 7 — Marketing | `1hBc6Axd0DE2ocTiXXKGlmj1dyagOwKFg` |
| 8 — Service | `1z4li_rdzH8yC7VFoWgOa4yMHbbKIAG29` |
| 9 — KDS | `1wQAkcP9pY90DLu_sE8GLiI6WYHZuYwq9` |
| 10 — Réservation | `1m6WdjC_iNYWO_4U3LmDuOsc-_Y_DrZLu` |
| 11 — Caisse POS & Matériel | `1nHjH82ig0i-MtQqDmYp131htOSThaPIQ` |
| 12 — HubRise & Livraisons | `19D09dNt_jZSKpcwVCU8Mn1OkMLkY_ojd` |
| 13 — Caroline (agent IA vocale) | `1SV1XsT61_cDqoRzD8JxehtRoOpyH5LaA` |
| 14 — PrediBot (agent IA directeur) | `19kYZliyRnKraKVg1zdFrXCocD38VZ2a9` |

La colonne « Module » de chaque épisode indique dans quel dossier piocher le screencast de démo : le hook et la démo racontent alors la même histoire (EP96 canicule → module HACCP, EP103 car de 40 → module Réservation, etc.).

Le module 6 (Mon Site) est celui qui contient « Créer un site par IA » et « Choisir ton template » : c'est la source des 10-15 s « Regarde, en un clic j'ai créé ton site ».

---

## 5. `episodes.json` — bloc saison 4 à coller

```json
[
  { "id": "EP91",  "titre": "Le pétard dans le tiramisu",        "module": "reservation",  "hook": "Anniversaire de table 12.",                 "vo": "Les surprises, c'est bien. Les imprévus, non.",                        "cut_out": 7.0, "actualite": false },
  { "id": "EP92",  "titre": "Le super-héros qui a réservé",       "module": "reservation",  "hook": "Lui, il avait réservé.",                    "vo": "Ses quatre-vingts fans, non.",                                          "cut_out": 7.0, "actualite": false },
  { "id": "EP93",  "titre": "Le chef part à la pêche",            "module": "stockvision",  "hook": "Rupture de stock, 20 h 15.",                "vo": "Anticiper, c'est moins sportif.",                                       "cut_out": 7.0, "actualite": false },
  { "id": "EP94",  "titre": "Le robot livreur",                   "module": "hubrise",      "hook": "2026, la livraison change de main.",        "vo": "Autant que tes commandes arrivent au bon endroit.",                     "cut_out": 7.0, "actualite": true  },
  { "id": "EP95",  "titre": "L'éclipse de 13 h 12",               "module": "service",      "hook": "Le service s'est arrêté deux minutes.",     "vo": "Le reste du temps, il ne devrait jamais s'arrêter.",                    "cut_out": 7.0, "actualite": true  },
  { "id": "EP96",  "titre": "Le beurre fugueur",                  "module": "haccp",        "hook": "39° en cuisine.",                           "vo": "Une alerte température, et tu sauves la marchandise.",                  "cut_out": 7.0, "actualite": true  },
  { "id": "EP97",  "titre": "Le mur de tablettes",                "module": "hubrise",      "hook": "Six plateformes. Six alertes.",             "vo": "Une seule commande, un seul écran.",                                    "cut_out": 7.0, "actualite": false },
  { "id": "EP98",  "titre": "Le robot serveur qui bugge",         "module": "service",      "hook": "Ton nouveau serveur, en période d'essai.",  "vo": "L'IA, c'est utile quand elle sert à quelque chose.",                    "cut_out": 7.0, "actualite": true  },
  { "id": "EP99",  "titre": "Le répondeur préhistorique",         "module": "caroline",     "hook": "Quarante appels pendant le rush.",          "vo": "Quelqu'un devrait répondre. Ce ne sera pas toi.",                       "cut_out": 7.0, "actualite": false },
  { "id": "EP100", "titre": "L'influenceur au ring light",        "module": "marketing",    "hook": "Il a mis vingt minutes à filmer.",          "vo": "Et deux minutes à te mettre deux étoiles.",                             "cut_out": 7.0, "actualite": false },
  { "id": "EP101", "titre": "POV : thriller comptable",           "module": "comptabilite", "hook": "Rapprochement des caisses. Vendredi soir.", "vo": "Ça devrait être une ligne, pas une enquête.",                           "cut_out": 7.0, "actualite": false },
  { "id": "EP102", "titre": "L'inspecteur surprise",              "module": "haccp",        "hook": "Contrôle surprise. Ou pas.",                "vo": "Le jour où c'est le vrai, tu ne bouges pas.",                           "cut_out": 7.0, "actualite": false },
  { "id": "EP103", "titre": "Le car de 40 sans réservation",      "module": "reservation",  "hook": "Quarante couverts. Sans prévenir.",         "vo": "Prévenu, tu aurais dit oui.",                                           "cut_out": 7.0, "actualite": false },
  { "id": "EP104", "titre": "Le no-show western",                 "module": "reservation",  "hook": "Table de huit. 20 h 30.",                   "vo": "Un no-show, ça se prévient.",                                           "cut_out": 7.0, "actualite": false },
  { "id": "EP105", "titre": "Le duel de la dernière table",       "module": "reservation",  "hook": "Dernière table du samedi.",                 "vo": "Le plus rapide gagne. Rends-la réservable en ligne.",                   "cut_out": 7.0, "actualite": false },
  { "id": "EP106", "titre": "L'addition en quatorze parts",       "module": "caisse",       "hook": "« On peut payer chacun ? »",                "vo": "Oui. En trois secondes, pas en trente minutes.",                        "cut_out": 7.0, "actualite": false },
  { "id": "EP107", "titre": "Le magicien de l'addition",          "module": "caisse",       "hook": "Tout le monde a un tour.",                  "vo": "Ta caisse, elle, ne perd jamais une addition.",                         "cut_out": 7.0, "actualite": false },
  { "id": "EP108", "titre": "Le poulpe du pass",                  "module": "kds",          "hook": "Il te faudrait six bras.",                  "vo": "Ou un seul outil qui fait le reste.",                                   "cut_out": 7.0, "actualite": false },
  { "id": "EP109", "titre": "Le kombucha qui explose",            "module": "haccp",        "hook": "Ta cave à ferments.",                       "vo": "Suivie et datée, elle ne t'explose pas à la figure.",                   "cut_out": 7.0, "actualite": false },
  { "id": "EP110", "titre": "Le menu 100 % matcha",               "module": "monsite",      "hook": "Tu suis toutes les tendances.",             "vo": "Regarde surtout lesquelles se vendent.",                                "cut_out": 7.0, "actualite": false },
  { "id": "EP111", "titre": "L'imprimante 3D qui déraille",       "module": "stockvision",  "hook": "La cuisine du futur.",                      "vo": "Le futur utile, c'est celui qui te fait gagner du temps.",              "cut_out": 7.0, "actualite": true  },
  { "id": "EP112", "titre": "Le casque de réalité augmentée",     "module": "monsite",      "hook": "La carte du futur.",                        "vo": "Ou juste une carte en ligne qui marche.",                               "cut_out": 7.0, "actualite": true  },
  { "id": "EP113", "titre": "Le drone qui se trompe de balcon",   "module": "hubrise",      "hook": "Livraison réussie. Presque.",               "vo": "Un suivi de commande, et personne ne mange ta pizza.",                  "cut_out": 7.0, "actualite": true  },
  { "id": "EP114", "titre": "La choré pendant que ça brûle",      "module": "marketing",    "hook": "Ton community manager, c'est ta brigade.",  "vo": "Poste. Mais garde un œil sur le service.",                              "cut_out": 7.0, "actualite": false },
  { "id": "EP115", "titre": "Les poules du potager du toit",      "module": "stockvision",  "hook": "Circuit court, très court.",                "vo": "Compte ce qui rentre. Et ce qui sort.",                                 "cut_out": 7.0, "actualite": false },
  { "id": "EP116", "titre": "Le stagiaire et le mur de craie",    "module": "kds",          "hook": "Ton système de commandes.",                 "vo": "Il tient sur un mur. Il tiendrait sur un écran.",                       "cut_out": 7.0, "actualite": false },
  { "id": "EP117", "titre": "Le plat étoilé en dix minutes",      "module": "stockvision",  "hook": "Le défi à dix minutes.",                    "vo": "Une fiche technique, et c'est dix minutes tous les jours.",             "cut_out": 7.0, "actualite": false },
  { "id": "EP118", "titre": "La file du brunch",                  "module": "monsite",      "hook": "Le brunch du dimanche.",                    "vo": "Ils feraient la queue chez toi aussi. Encore faut-il pouvoir réserver.","cut_out": 7.0, "actualite": false },
  { "id": "EP119", "titre": "La mascotte poulet et le vent",      "module": "marketing",    "hook": "Ta stratégie d'acquisition.",               "vo": "Cinq cents tracts, zéro donnée.",                                       "cut_out": 7.0, "actualite": false },
  { "id": "EP120", "titre": "La réunion des dix logiciels",       "module": "predibot",     "hook": "Réunion de tes dix logiciels.",             "vo": "Ils ne se parlent toujours pas. FoodEatUp, si.",                        "cut_out": 7.0, "actualite": false }
]
```

---

## 6. Direction voix (ElevenLabs)

Même voix off que les saisons précédentes sur les 30 punchlines, pour l'unité de série.

- **Ton** : posé, légèrement amusé, jamais vendeur. La punchline arrive *après* le gag, elle le commente — elle ne le surjoue pas.
- **Débit** : lent. Chaque punchline tient en 2 à 2,5 s ; si le rendu dépasse 2,8 s, raccourcis le texte plutôt que d'accélérer.
- **Réglages** : stability haute (voix stable d'une vidéo à l'autre), style bas, speaker boost activé.
- **Trois exceptions à jouer plus sec** : EP101 (thriller — quasi chuchoté), EP104 (western — une pause avant « ça se prévient »), EP120 (finale — ton neutre, la chute est dans le texte).
- Les répliques diégétiques en français (« Bonjour, signature ? » EP102, « Attendez— » EP92) sont **générées par Higgsfield dans le clip**, pas par ElevenLabs. Si Kling les rate, Claude Code les laisse tomber : elles ne sont pas nécessaires au montage.

---

## 7. Contrôle qualité avant de déposer le MP4

1. Aucun texte, aucun logo, aucune marque visible dans l'image.
2. Beat comique entre 4,5 s et 6,5 s.
3. Deux dernières secondes stables.
4. EP92, EP112, EP119 : vérifie qu'aucun costume/casque ne ressemble à un personnage ou une marque existante. Si oui, régénère avec « plain, invented, no emblem ».
5. Si le beat arrive trop tard mais que le clip est bon : ajuste `cut_out` dans `episodes.json` plutôt que de régénérer.

---

## 8. Pour finir la série (EP121 → EP150)

Il reste 30 épisodes. Trois veines encore inexploitées, si tu veux que je les écrive :
- **Les clients impossibles** : le modificateur infini, le « comme d'habitude » du client jamais venu, l'allergie annoncée au dessert.
- **Les saisons** : réveillon, Saint-Valentin surbookée, rentrée, fête de la musique, premier jour de terrasse.
- **Le point de vue des objets** : la friteuse, le lave-verres, le carnet de réservations qui raconte sa journée.
