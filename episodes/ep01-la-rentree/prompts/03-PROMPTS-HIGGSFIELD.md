# 03 — PROMPTS HIGGSFIELD
## Épisode 1 « La Rentrée »

> Rappel du CLAUDE.md : **Claude Code n'appelle jamais le MCP Higgsfield.** Ces prompts sont
> à copier-coller manuellement dans l'interface Higgsfield par vous, avec Seedance.

---

## Rappel du double-bind (voir `bible/01-BIBLE-PERSONNAGES.md`)

Pour chaque plan avec un personnage :
1. **Joindre le(s) portrait(s) canonique(s) comme référence(s), en premier**, avant le texte
   du prompt. Fichiers dans `bible/refs/` (déjà validés et uploadés dans RapidoCMS le
   2026-08-09) :
   - Tom → `bible/refs/tom.jpg`
   - Mama Batata → `bible/refs/batata.jpg`
   - Rott-K → `bible/refs/rottk.jpg`
   - Brocoli → `bible/refs/brocoli.jpg`
   - Oignon → `bible/refs/oignon.jpg`
   - Ail → `bible/refs/ail.jpg`
   - Firase → `bible/refs/firase.jpg`
   - Betterave → `bible/refs/betterave.jpg`
   - Don Citrone → `bible/refs/citrone.jpg`
   - Décor cuisine (tous les plans) → `bible/refs/decor-cuisine-ep01.jpg`
2. **Redécrire le personnage en texte** dans le prompt (traits verrouillés ci-dessous,
   copiés depuis `bible/personnages.json`) — ne pas se fier à la seule image de référence.
3. **Ne jamais régénérer un portrait canonique.** Pour une nouvelle pose de personnage
   (hors vidéo), repartir du fichier `bible/refs/*.jpg` via `images_to_image`.
4. Format natif **9:16**, style cohérent avec les portraits (cartoon/3D, mêmes proportions
   enfant ~6 ans, mains à 4 doigts).

---

## BLOC A — HOOK (10 s) — `sources/A_hook.mp4`

### Plan 1 (0–5 s)

**Contexte scénario :** Cuisine morte, premier matin de septembre. Housses de protection sur
le pass, un néon qui clignote, calendrier bloqué sur juillet, herbes fanées, cagettes
fournisseur non ouvertes contre la porte de service. Tom, seul au centre, fixe l'objectif,
impassible. Il tire lentement la housse du pass — un nuage de poussière monte dans les rais
de lumière. Il ne cligne pas des yeux. Derrière lui, hors focus, quelque chose de métallique
tombe.

**Références à joindre (dans cet ordre) :** `bible/refs/tom.jpg`, `bible/refs/decor-cuisine-ep01.jpg`

**Prompt :**
```
Reference images attached: character reference for TOM (a ripe tomato mascot character)
and environment reference for the kitchen set. Match both exactly.

9:16 vertical shot, static locked-off camera, professional restaurant kitchen, dawn light
through windows, cold early-morning atmosphere, first day of September. A dust-cover sheet
drapes over the pass/counter, a neon light fixture flickers intermittently, a wall calendar
is stuck on July, dried wilted herbs sit in a jar, unopened supplier delivery crates are
stacked against a closed service door.

TOM (matching reference): a ripe tomato character, deep red glossy skin with soft
subsurface-scattering glow, green five-leaf calyx on top, large expressive cartoon eyes
with brown irises, thin rectangular black-framed glasses, white baseball cap worn
backwards, open white chef jacket with rolled-up sleeves, thin cartoon limbs, four-fingered
hands, proportioned like a small child relative to the kitchen. Standing alone, centered in
frame, staring directly into the camera lens, expression completely still and unblinking.
He slowly pulls the dust-cover sheet off the pass counter with both hands — a cloud of dust
rises and catches in the light beams from the window. He does not blink throughout the
shot. Behind him, slightly out of focus, something metallic falls and clatters (implied,
not the focus of the shot).

Mood: eerie stillness, deadpan, quiet dread before chaos. Muted cold-blue dawn light mixed
with warm copper undertones from the kitchen fixtures. Clean 3D-cartoon animation style
matching the character reference exactly. No text on screen, no logos, no photorealistic
human faces, no third-party brand names.
```

### Plan 2 (5–10 s)

**Contexte scénario :** Whip-pan à gauche puis retour sec sur Tom en gros plan. Il lève un
doigt. Derrière lui la cuisine explose : cagettes qui basculent, alarme, silhouettes qui
courent en panique.

**Références à joindre :** `bible/refs/tom.jpg`, `bible/refs/decor-cuisine-ep01.jpg`

**Prompt :**
```
Reference images attached: character reference for TOM and environment reference for the
kitchen set. Match both exactly. Continuation of the previous shot, same kitchen, same
character design.

9:16 vertical shot. Fast whip-pan to the left, then a sharp snap-back whip-pan landing on a
close-up of TOM's face and upper body. TOM (matching reference: ripe tomato character, deep
red glossy skin, green five-leaf calyx, large brown cartoon eyes, thin black rectangular
glasses, white backwards baseball cap, open white chef jacket, thin cartoon limbs,
four-fingered hands) raises one finger in the air, a small deliberate gesture right before
he's about to say or decide something — his signature pose.

Behind him, out of focus but clearly legible, the kitchen erupts into chaos: stacked
delivery crates topple over, a kitchen alarm light starts flashing, blurred silhouettes of
other characters run past in a panic. Motion blur on the background chaos, sharp focus on
TOM's face.

Mood: comic tension breaking into chaos, energetic camera whip, contrast between TOM's calm
composure and the escalating disaster behind him. Clean 3D-cartoon animation style matching
the character reference exactly. No text on screen, no logos, no photorealistic human
faces, no third-party brand names.
```

---

## BLOC B — CORPS (15 s) — `sources/B_corps.mp4`

### Plan 1 (10–12 s)

**Contexte scénario :** Plan large de la cuisine en pleine panique. Ail & Oignon franchissent
la porte de service avec des cagettes manifestement fausses, Oignon agitant un bon de
livraison chiffonné. Betterave traverse le cadre en trottinette, plateau vide (gag visuel
de fond).

**Références à joindre :** `bible/refs/oignon.jpg`, `bible/refs/ail.jpg`, `bible/refs/betterave.jpg`, `bible/refs/decor-cuisine-ep01.jpg`

**Prompt :**
```
Reference images attached: character references for OIGNON, AIL, and BETTERAVE, plus the
kitchen environment reference. Match all exactly.

9:16 vertical shot, wide shot of the kitchen in full panic mode, same kitchen set as
previous shots. OIGNON (matching reference: tall yellow-orange onion bulb, tall green
sprouting shoots, permanently furrowed grumpy eyebrows, scruffy brown fanny-pack, yellow
high-visibility safety vest) and AIL (matching reference: small pearly-white garlic bulb,
mischievous face, rosy cheeks, notably smaller than Oignon, same fanny-pack and safety
vest) burst through the service door carrying obviously fake/mismatched delivery crates —
wrong labels, wrong contents visible. OIGNON is waving a crumpled delivery receipt in one
hand, visibly annoyed. AIL and OIGNON must stay at least 50cm apart from each other at all
times in frame — never touching or adjacent.

In the background, BETTERAVE (matching reference: small purple-red teardrop-shaped
beetroot, very small in scale, on a kick scooter, holding an empty serving tray) speeds
across the frame from right to left as a background sight gag, weaving through the chaos.

Mood: loud, chaotic, comic overload — multiple small disasters happening at once in a
single wide shot. Warm-copper kitchen lighting. Clean 3D-cartoon animation style matching
the character references exactly. No text on screen, no logos, no photorealistic human
faces, no third-party brand names.
```

### Plan 2 (12–14,5 s)

**Contexte scénario :** Mama Batata, sac à main au bras, téléphone coincé à l'oreille, tient
trois torchons et un classeur ; un planning mural vide se décroche derrière elle et tombe.

**Références à joindre :** `bible/refs/batata.jpg`, `bible/refs/decor-cuisine-ep01.jpg`

**Prompt :**
```
Reference image attached: character reference for MAMA BATATA, plus the kitchen environment
reference. Match both exactly.

9:16 vertical shot, medium shot in the kitchen. MAMA BATATA (matching reference: elongated
potato character, matte beige-gold skin, small visible tuber "eyes", soft eyes with light
under-eye circles, handbag on her arm even in the kitchen, phone wedged between shoulder
and cheek, burgundy bistro apron with a kitchen towel at the waist) is visibly multitasking
— she holds three folded kitchen towels and a binder/folder in her arms, never setting
anything down, moving briskly through frame while talking on the phone. Harried but warm
expression.

Behind her, an empty wall-mounted planning board comes loose from the wall and falls,
clattering to the floor — she doesn't notice, too busy juggling everything she's carrying.

Mood: frantic multitasking, comic overload, warm-copper kitchen lighting. Clean 3D-cartoon
animation style matching the character reference exactly. No text on screen, no logos, no
photorealistic human faces, no third-party brand names.
```

### Plan 3 (14,5–17 s)

**Contexte scénario :** Rott-K ouvre une chambre froide : un souffle de vapeur froide, elle
recule d'un pas, tourne lentement la tête vers l'objectif une demi-seconde, puis referme la
porte.

**Références à joindre :** `bible/refs/rottk.jpg`, `bible/refs/decor-cuisine-ep01.jpg`

**Prompt :**
```
Reference image attached: character reference for ROTT-K, plus the kitchen environment
reference. Match both exactly.

9:16 vertical shot, medium shot near a walk-in cold room / fridge door in the kitchen.
ROTT-K (matching reference: vivid orange carrot character, bushy green leafy fronds on top,
half-lidded skeptical eyes, long bohemian wooden bead necklace, temperature probe in a
breast pocket plus a small notepad, short white hygiene lab coat) opens the cold-room door.
A visible cold-fog breath of vapor billows out. She takes one step back, reacting to
whatever she sees inside (not shown to camera). She slowly turns her head toward the camera
lens for exactly half a second — a knowing, slightly dry, disapproving look directly at the
viewer — then closes the door again.

Mood: dry deadpan comedy, cold blue lighting from the fridge contrasted with the warm
kitchen behind her. Clean 3D-cartoon animation style matching the character reference
exactly. No text on screen, no logos, no photorealistic human faces, no third-party brand
names.
```

### Plan 4 (17–20 s)

**Contexte scénario :** Firase filme tout au selfie stick en tournant sur elle-même,
radieuse, pendant que tout s'effondre autour. Don Citrone entre en salle, regarde sa montre,
ressort.

**Références à joindre :** `bible/refs/firase.jpg`, `bible/refs/citrone.jpg`, `bible/refs/decor-cuisine-ep01.jpg`

**Prompt :**
```
Reference images attached: character references for FIRASE and DON CITRONE, plus the
kitchen/dining environment reference. Match all exactly.

9:16 vertical shot. FIRASE (matching reference: glossy red strawberry character, visible
yellow akene seeds, green leafy collar, smartphone on a selfie stick always extended toward
the camera first, pale pink cropped jacket, hair barrette) spins slowly in place in the
middle of the kitchen, beaming and delighted, filming herself on her selfie-stick phone —
completely oblivious to the chaos and destruction happening all around her in the
background (crates toppling, panic, motion blur).

In a separate beat within the same shot (or immediately following), DON CITRONE (matching
reference: bright yellow lemon character, plump rounded body, two green leaves, wristwatch
he keeps glancing at) walks into the dining room, checks his watch with visible impatience,
then turns around and walks back out without waiting.

Mood: comic obliviousness contrasted with mounting chaos, bright energetic lighting on
Firase, colder more neutral lighting in the dining room for Don Citrone's beat. Clean
3D-cartoon animation style matching the character references exactly. No text on screen,
no logos, no photorealistic human faces, no third-party brand names.
```

### Plan 5 (20–25 s) — LE RETOURNEMENT (plan le plus important du bloc)

**Contexte scénario :** Tout le monde se fige. Contre-plongée lente sur Brocoli, immobile au
fond, tablette à deux mains, le visage éclairé en bleu `#147AFF`. Elle lève les yeux. Le
chaos s'arrête. Tom traverse le cadre, prend la tablette. La lumière bleue se répand sur le
pass en cuivre — le chaud et le froid se rencontrent. Dernier plan : la brigade entière,
alignée, immobile, éclairée bleu.

**Références à joindre :** `bible/refs/brocoli.jpg`, `bible/refs/tom.jpg`, `bible/refs/decor-cuisine-ep01.jpg` (+ idéalement les autres portraits pour le plan de groupe final : `batata.jpg`, `rottk.jpg`, `oignon.jpg`, `ail.jpg`, `firase.jpg`, `betterave.jpg`, `citrone.jpg`)

**Prompt :**
```
Reference images attached: character references for BROCOLI, TOM, and the full cast, plus
the kitchen environment reference. Match all exactly.

9:16 vertical shot. The chaos suddenly freezes — every character in frame stops moving
mid-action, holding their pose. Slow low-angle push-in (contre-plongée) on BROCOLI
(matching reference: green broccoli character, dense floweret head, pale-green stem,
calm large eyes with very few blinks, blue #147AFF over-ear headphones around the neck,
holding a tablet with both hands, plain grey hoodie with hood down), standing perfectly
still at the back of the kitchen, the tablet screen glowing vivid blue #147AFF and casting
that blue light across her face and the surrounding area. She slowly looks up from the
tablet toward camera. The chaos around her stays completely frozen.

TOM (matching reference: ripe tomato character, as described in earlier shots) walks
calmly through the frame and takes the tablet from her hands. As he does, the blue glow
spreads outward across the copper-toned kitchen pass counter — a visible meeting point
between warm copper light and cold blue light.

Final beat of the shot: the entire brigade (all characters, matching their references) is
now aligned in a row, standing completely still, all lit in the same blue #147AFF glow.

Mood: the pivotal tonal shift of the episode — from loud chaos to sudden calm and clarity.
This is the most important shot of the sequence; the blue/copper light contrast must be
clearly visible. Clean 3D-cartoon animation style matching all character references
exactly. No text on screen, no logos, no photorealistic human faces, no third-party brand
names.
```

---

## Variante 24 s (si Seedance 2.5 actif sur votre compte)

Seedance 2.0 plafonne le Bloc B à 15 s. Si votre compte Higgsfield a bien Seedance 2.5
actif, vous pouvez étendre le Bloc B à 24 s en insérant un plan supplémentaire entre le
Plan 4 (Firase/Don Citrone, 17–20 s) et le Plan 5 (le retournement) :

**Plan bonus (20–23 s, avant le retournement) — suggestion :** un plan de transition qui
laisse le chaos monter encore un cran avant la bascule — par exemple Mama Batata qui lâche
enfin un objet (rupture de sa signature de jeu, pour souligner que la situation devient
intenable), ou un plan large qui montre tous les personnages en même temps juste avant le
gel. Ce plan n'est pas scénarisé dans le doc 02 — à valider avec vous avant de l'écrire en
prompt définitif, puisqu'il ajoute du contenu narratif non prévu à l'origine.

Le Plan 5 (retournement) glisserait alors de 20–25 s à 23–29 s, et le Bloc C démarrerait à
29 s au lieu de 25 s (motion design à raccourcir de 15 s à 11 s en conséquence, ou`
`remotion/src/OutroEp01.tsx` à ajuster).

**Non prioritaire** tant que la version 15 s (Seedance 2.0, structure ci-dessus) n'est pas
validée — c'est elle qui « tourne partout » quel que soit votre compte.

---

## Checklist de recette (avant d'accepter un rendu)

Un rendu qui rate **un seul** point ci-dessous est refusé — on ne « fait pas avec », on
régénère (jamais depuis zéro pour les personnages : repartir des références validées).

### Pour chaque plan
- [ ] Chaque personnage à l'écran correspond aux traits verrouillés de `bible/personnages.json`
      (couleur, accessoires, tenue, proportions) — pas d'hallucination du modèle
- [ ] Format 9:16 respecté, pas de recadrage/déformation
- [ ] Aucun visage humain photoréaliste
- [ ] Aucune marque tierce visible (logos fournisseurs, concurrents, autre)
- [ ] Aucun nom de film/studio/réalisateur/artiste vivant halluciné dans le rendu
- [ ] Aucun chiffre de performance affiché à l'écran
- [ ] Aucune allégation santé

### Points spécifiques par plan
- [ ] **Plan A1** — Tom ne cligne pas des yeux ; nuage de poussière visible ; néon qui clignote
- [ ] **Plan A2** — whip-pan net (pas de flou de transition mal exécuté) ; doigt levé de Tom bien visible
- [ ] **Plan B1** — Ail et Oignon jamais à moins de 50 cm l'un de l'autre ; Betterave traverse bien de **droite à gauche**
- [ ] **Plan B2** — Batata tient bien 3 objets + téléphone, ne pose rien
- [ ] **Plan B3** — Rott-K regarde la caméra une demi-seconde **après** la réaction, pas avant/pendant
- [ ] **Plan B4** — le smartphone de Firase entre dans le cadre avant elle
- [ ] **Plan B5 (retournement)** — le contraste bleu `#147AFF` / cuivre chaud est net et lisible ; Brocoli reste immobile jusqu'à ce qu'elle lève les yeux ; le gel du chaos est clairement lisible (pas un simple ralenti)

### Cohérence inter-plans
- [ ] Le décor (cuisine) reste visuellement cohérent d'un plan à l'autre (mêmes housses,
      même néon, même calendrier) — utiliser systématiquement `bible/refs/decor-cuisine-ep01.jpg`
      comme référence
- [ ] Les personnages gardent la même échelle relative entre les plans (ex. Ail toujours
      moitié de la taille d'Oignon, Betterave toujours très petite)

---

## Interdits absolus (rappel — voir bible)

- ❌ Aucun nom de film, studio d'animation, réalisateur ou artiste vivant
- ❌ Aucune marque tierce visible (logos de fournisseurs, concurrents)
- ❌ Aucun visage humain photoréaliste
- ❌ Aucun chiffre de performance non sourcé à l'écran
- ❌ Aucune allégation santé (on est en B2B logiciel, pas en nutrition)
