/**
 * FoodEatUp — prépare les 150 dossiers épisode sur le Drive de production.
 *
 * Généré par scripts/gen-drive-script.py. Ne pas éditer à la main : régénérer.
 *
 * INSTALLATION
 *   1. script.google.com > Nouveau projet, colle ce fichier
 *   2. Exécute creerTout()
 *   3. Apps Script coupe à 6 minutes : relance creerTout() jusqu'à voir
 *      "TERMINE". Le script reprend exactement où il s'est arrêté.
 *      (ou lance planifier() une fois : un déclencheur horaire finit seul)
 *
 * IDEMPOTENT : relançable sans risque, rien n'est jamais recréé ni écrasé.
 *
 * Pour repartir de zéro sur la progression (sans supprimer les dossiers) :
 *   reinitialiserProgression()
 */

var SAISONS = {
  "1": "18jxNDHRiDI2FzQL8o8CwQoyD_Cm4c8tk",
  "2": "1IBJRoG-B_QR4DC9zqB-gpNLuMzmsCKx4",
  "3": "14jzeohNZyYN1yE5r_3uUKxiEiVDCQdE3",
  "4": "1NfI08kX5E_H2ZmUWAyKgJoNznCwLYxXf",
  "5": "1qx68w5c91hbwESu-LIJD6EZiumL-Zszc"
};

var SOUS_DOSSIERS = ['01-PROMPTS', '02-ASSETS', '03-RESEAUX', '04-MASTERS', '05-ACADEMY'];

var LIMITE_MS = 4.5 * 60 * 1000;  // on s'arrête avant le couperet des 6 minutes

var EP = [
 {
  "id": "EP001",
  "n": 1,
  "t": "Le chien qui te regarde",
  "mod": "Service",
  "ch": "1 - Commandes multi-canaux",
  "drive": "1z4li_rdzH8yC7VFoWgOa4yMHbbKIAG29",
  "hook": "Lui aussi attend ta commande.",
  "punch": "Sauf que lui, il est patient. Tes clients, non.",
  "heygen": "Ici, toutes tes commandes arrivent au même endroit : la salle, le téléphone, le site, la livraison. Une seule file, dans l'ordre d'arrivée. Plus personne n'attend parce qu'on a oublié un ticket.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic, cinematic handheld camera, shallow depth of field, natural light, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A golden retriever sits under a bistro table on a sunlit restaurant terrace, staring up with huge pleading eyes at a plate of fries, head tilting slowly. At 5 seconds a hand reaches for the plate and the dog instantly snatches one fry and freezes mid-chew, guilty, looking straight into the camera. Hold the frozen guilty stare for the final 2 seconds. Audio: quiet terrace ambience, cutlery clinking, distant chatter, a soft whine from the dog, a sharp comedic record-scratch at the moment of the snatch, then silence on the freeze. No music."
 },
 {
  "id": "EP002",
  "n": 2,
  "t": "La chute en skateboard",
  "mod": "Service",
  "ch": "3 - Envoi direct cuisine",
  "drive": "1z4li_rdzH8yC7VFoWgOa4yMHbbKIAG29",
  "hook": "Ton service du samedi soir.",
  "punch": "Ça finit toujours par terre.",
  "heygen": "Tu prends la commande à table, elle part en cuisine dans la seconde. Pas de carnet, pas d'aller-retour, pas de ticket perdu entre la salle et le pass.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic, cinematic handheld camera, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A young man in an apron rides a skateboard down a city street holding a stack of takeaway boxes. He looks confident, smiles at the camera. At 5 seconds the front wheel hits a small crack, he loses balance in slow motion and the boxes fly upward in a slow arc. Final 2 seconds: he lies flat on the pavement, one box lands perfectly upright next to his head. Audio: skateboard wheels rumbling on asphalt, city ambience, a comedic slow-motion whoosh during the fall, a cardboard thud, then a single dry cricket chirp. No music."
 },
 {
  "id": "EP003",
  "n": 3,
  "t": "Le plat dans la piscine",
  "mod": "StockVision",
  "ch": "1 - Ma carte",
  "drive": "1Ib_pKyJ8_jaFAwtIhkzhtmUU_DCtGSSY",
  "hook": "Ta marge, en ce moment.",
  "punch": "Elle coule. On va la repêcher.",
  "heygen": "Chaque plat de ta carte a son coût matière calculé depuis tes ingrédients. Tu vois ta marge réelle, plat par plat, avant même de fixer ton prix.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic, macro-to-wide cinematic, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. Extreme slow motion: a beautifully plated gourmet dish on a white ceramic plate falls into a bright turquoise swimming pool. Sauce and garnish disperse in blooming underwater clouds, the plate sinks slowly toward the tiled bottom. Camera follows the plate down through the water. Final 2 seconds: the plate rests on the pool floor, sunlight rippling over it. Audio: a heavy underwater plunge, muffled bubbling, distant poolside ambience above the surface, a low descending comedic slide-whistle during the sink. No music."
 },
 {
  "id": "EP004",
  "n": 4,
  "t": "Le chat sur la caisse",
  "mod": "Caisse POS",
  "ch": "1 - Configurer sa caisse",
  "drive": "1nHjH82ig0i-MtQqDmYp131htOSThaPIQ",
  "hook": "Ton nouveau responsable de caisse.",
  "punch": "Il gère mieux que ton logiciel actuel.",
  "heygen": "Ta caisse se configure en quelques minutes : TPE, ticket, moyens de paiement. Elle est reliée à ta carte et à ta cuisine, pas posée à côté.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic, locked-off camera then slow push-in, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A grey tabby cat sits squarely on top of a restaurant POS touchscreen terminal, tail flicking, completely unbothered. A hand enters frame trying to gently move it; the cat presses one paw down on the screen and holds eye contact with the camera. Final 2 seconds: the cat lies down fully across the terminal, closing its eyes. Audio: kitchen ambience, a receipt printer chattering, three rapid electronic beeps as the paw presses the screen, a smug cat chirp. No music."
 },
 {
  "id": "EP005",
  "n": 5,
  "t": "Le serveur qui glisse",
  "mod": "Configuration",
  "ch": "vue d'ensemble",
  "drive": "19xTrrkXtWO3yfJqtC3SIlDgpBjSEc4N9",
  "hook": "Trois logiciels. Deux mains.",
  "punch": "Un seul outil, ça change tout.",
  "heygen": "Un seul paramétrage : ta carte, tes zones, tes tables, ta TVA. Tout le reste s'appuie dessus. Tu ne ressaisis jamais deux fois la même information.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic, cinematic tracking shot, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A waiter walks fast through a busy dining room balancing three plates on one arm and a phone wedged against his shoulder. At 5 seconds he steps on a wet patch, one leg slides forward, he does a full split while somehow keeping every plate perfectly level above his head. Final 2 seconds: frozen in the split, plates immaculate, a proud exhausted grin. Audio: busy restaurant ambience, a rubber-sole squeak, a comedic cartoon slip sound, scattered applause from unseen diners. No music."
 },
 {
  "id": "EP006",
  "n": 6,
  "t": "La pizza frisbee",
  "mod": "StockVision",
  "ch": "17 - Ajouter et modifier un mouvement",
  "drive": "1Ib_pKyJ8_jaFAwtIhkzhtmUU_DCtGSSY",
  "hook": "Ta pizza part plus vite que ton stock.",
  "punch": "Enfin… c'était avant.",
  "heygen": "Tu envoies un plat, le stock bouge tout seul. Chaque sortie est tracée, avec la quantité et l'heure. Tu sais ce qu'il te reste sans compter les cartons.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic, dynamic camera whip-pan, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A pizzaiolo pulls a steaming margherita from a wood-fired oven with a peel. The flick is too strong: the pizza launches off the peel and sails across the kitchen like a frisbee, spinning in slow motion, cheese stretching. Final 2 seconds: it lands perfectly flat inside an open takeaway box on the counter. The pizzaiolo stares, then slowly nods once. Audio: roaring oven fire, a whooshing spin as the pizza flies, a soft cardboard landing thump, one impressed whistle. No music."
 },
 {
  "id": "EP007",
  "n": 7,
  "t": "La mamie qui goûte",
  "mod": "Marketing",
  "ch": "3 - Répondre aux avis",
  "drive": "1hBc6Axd0DE2ocTiXXKGlmj1dyagOwKFg",
  "hook": "Le seul avis client qui compte.",
  "punch": "Les quatre cents autres, on s'en occupe.",
  "heygen": "Tes avis Google remontent ici. Tu réponds depuis FoodEatUp, l'IA te propose une réponse dans ton ton, tu valides. Le client voit que tu l'as lu.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic, warm close-up, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. Close-up of an elderly French woman at a bistro table, spoon halfway to her mouth. She tastes, pauses, eyes widening dramatically. At 5 seconds she slams the table gently, points at the plate and gives an enormous exaggerated thumbs up straight to camera, nodding hard. Final 2 seconds: she goes back to eating, ignoring the camera completely. Audio: cosy bistro ambience, a soft spoon clink, her voice saying warmly in French \"Ah ça, c'est bon !\", a light table thump. No music."
 },
 {
  "id": "EP008",
  "n": 8,
  "t": "La pile de tickets",
  "mod": "Comptabilité",
  "ch": "facturation",
  "drive": "1KlXihMLILGDrlxDuO2d3VCe1ic-kCAw_",
  "hook": "Fin de mois. Encore.",
  "punch": "Et si la compta se faisait toute seule ?",
  "heygen": "Chaque commande génère sa facture. Tu retrouves le facturé, l'encaissé et les impayés dans le même écran. La fin de mois devient une lecture, pas une reconstitution.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic, slow push-in, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A restaurant manager sits at a cluttered back-office desk. A thermal receipt printer beside him keeps printing without stopping; the paper roll has already coiled into a huge pile on the floor. He watches it, resigned, then slowly lowers his forehead onto the desk. Final 2 seconds: the printer is still going, the paper now reaching his chair. Audio: relentless thermal printer chattering that never stops, a fluorescent light hum, a long defeated human sigh. No music."
 },
 {
  "id": "EP009",
  "n": 9,
  "t": "Le pigeon voleur",
  "mod": "Caisse POS",
  "ch": "7 - Suivre les écarts de caisse",
  "drive": "1nHjH82ig0i-MtQqDmYp131htOSThaPIQ",
  "hook": "Il y a toujours quelqu'un qui prend ta marge.",
  "punch": "Ton abonnement logiciel, par exemple.",
  "heygen": "À chaque clôture, l'écart entre le théorique et le compté s'affiche. Tu vois quel service dérape et de combien. Ce qui se mesure s'arrête.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic, handheld street-level, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A paper cone of fries sits on a café terrace table in the sun. A pigeon lands on the edge of the table and edges sideways toward it with absurd confidence. At 5 seconds it grabs a single fry and takes off. Final 2 seconds: the empty spot on the table, one feather drifting down in slow motion. Audio: terrace ambience, pigeon wing flaps, an exaggerated theft-movie sting as it grabs the fry, then a soft feather-drop silence. No music."
 },
 {
  "id": "EP010",
  "n": 10,
  "t": "Le flambage raté",
  "mod": "PrediBot",
  "ch": "1 - Lire ses prévisions",
  "drive": "19kYZliyRnKraKVg1zdFrXCocD38VZ2a9",
  "hook": "Toi, devant ta facture logicielle.",
  "punch": "Mille euros par mois. Pour dix outils qui ne se parlent pas.",
  "heygen": "Un écran, le matin : ton chiffre d'affaires prévu, ta fréquentation, tes points de tension. C'est ton point du jour, sans ouvrir dix onglets.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic, cinematic kitchen lighting, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A chef flambés a pan of prawns; the flame erupts far higher than expected, filling the top of the frame. He recoils. Final 2 seconds: he turns to camera with slightly singed eyebrows and a completely blank expression, a wisp of smoke rising from his hat. Audio: gas burner, a loud whoosh of igniting alcohol, a startled French \"Oh !\", then only the quiet crackle of the pan. No music."
 },
 {
  "id": "EP011",
  "n": 11,
  "t": "Le livreur et le dos d'âne",
  "mod": "HubRise",
  "ch": "1 - Connecter son HubRise",
  "drive": "19D09dNt_jZSKpcwVCU8Mn1OkMLkY_ojd",
  "hook": "Ta livraison sans intégration.",
  "punch": "Avec, tout arrive à bon port.",
  "heygen": "Tu connectes HubRise une fois. Tes plateformes de livraison envoient leurs commandes directement dans FoodEatUp. Plus de tablette à surveiller dans un coin.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic, low-angle tracking, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A delivery rider on a scooter with a large insulated backpack rides down a suburban street. At 5 seconds he hits a speed bump he clearly did not see; the backpack lid flips open and three wrapped burgers launch into the air in slow motion. Final 2 seconds: the rider has stopped, one foot down, watching a burger land softly in a hedge. Audio: scooter engine, a metallic bump and rattle, a slow-motion whoosh, a leafy rustle on landing, then engine idling. No music."
 },
 {
  "id": "EP012",
  "n": 12,
  "t": "Le client qui attend",
  "mod": "KDS",
  "ch": "3 - Gérer le KDS en direct",
  "drive": "1wQAkcP9pY90DLu_sE8GLiI6WYHZuYwq9",
  "hook": "Temps d'attente : « on regarde ».",
  "punch": "Avec un KDS, il regarde son plat arriver.",
  "heygen": "Le KDS affiche chaque plat, son poste et son temps d'attente. Le client ne regarde plus la cuisine : il regarde son plat arriver.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic, locked-off camera, timelapse effect, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A man sits alone at a restaurant table with an empty plate in front of him, looking politely toward the kitchen. Time accelerates around him: light shifts from day to evening, other tables fill and empty, and his stubble visibly grows into a full beard. Final 2 seconds: he is fully bearded, still smiling politely, still waiting. Audio: restaurant ambience speeding up and slowing down, a ticking clock rising in the mix, a single small stomach growl at the end. No music."
 },
 {
  "id": "EP013",
  "n": 13,
  "t": "L'avalanche de notifications",
  "mod": "PrediBot",
  "ch": "3 - Parler à PrediBot",
  "drive": "19kYZliyRnKraKVg1zdFrXCocD38VZ2a9",
  "hook": "Dix logiciels. Dix notifications.",
  "punch": "Un seul, ça suffisait.",
  "heygen": "Tu poses ta question en français : combien j'ai fait hier, qu'est-ce qui manque demain. PrediBot lit tes vraies données et te répond. Une seule interface, pas dix.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic, macro then wide, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. Macro shot of a smartphone lying on a stainless-steel kitchen pass. It buzzes once, then faster and faster until it vibrates itself across the metal surface. At 5 seconds it buzzes so hard it walks off the edge. Final 2 seconds: it lies face-down on the floor, still buzzing, a cook's shoe stepping carefully around it. Audio: escalating phone vibration on metal, layered notification chimes stacking into chaos, a clatter as it falls, then muffled buzzing from the floor. No music."
 },
 {
  "id": "EP014",
  "n": 14,
  "t": "Le raton laveur",
  "mod": "StockVision",
  "ch": "16 - Mouvements de stock",
  "drive": "1Ib_pKyJ8_jaFAwtIhkzhtmUU_DCtGSSY",
  "hook": "Ton gaspillage alimentaire.",
  "punch": "Lui au moins, il sait ce qu'il y a en stock.",
  "heygen": "Chaque entrée, chaque sortie, chaque perte est enregistrée. Tu vois ce qui part sans être vendu. Le gaspillage devient une ligne, donc un problème réglable.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic, night, security-camera framing then cinematic, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. Night, behind a restaurant. A raccoon carefully lifts the lid of a large bin, climbs half inside, and emerges holding an entire untouched baguette. It freezes when a light clicks on. Final 2 seconds: it stares directly into the camera, baguette in both paws, absolutely unashamed. Audio: night ambience, crickets, a metallic bin lid clang, plastic rustling, a small raccoon chitter, a light switch click. No music."
 },
 {
  "id": "EP015",
  "n": 15,
  "t": "La tour d'assiettes",
  "mod": "Configuration",
  "ch": "référentiels",
  "drive": "19xTrrkXtWO3yfJqtC3SIlDgpBjSEc4N9",
  "hook": "Ta gestion actuelle.",
  "punch": "Une pièce bouge, tout s'écroule.",
  "heygen": "Tes catégories, ta TVA, tes zones, tes équipements : tout est posé une fois, proprement. Quand une pièce bouge, le reste ne s'écroule pas.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic, static wide then slow zoom, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A dishwasher in a commercial kitchen stacks clean plates into a tower far too tall, adding one more with great care. The tower sways. At 5 seconds he removes a single plate from near the bottom and the entire stack collapses in slow motion. Final 2 seconds: he stands amid the wreckage holding the one plate he took, intact. Audio: kitchen ambience, ceramic clinking, a rising creak as the tower sways, a massive ceramic crash, then total silence except a dripping tap. No music."
 },
 {
  "id": "EP016",
  "n": 16,
  "t": "Le geyser à café",
  "mod": "Comptabilité",
  "ch": "dépenses",
  "drive": "1KlXihMLILGDrlxDuO2d3VCe1ic-kCAw_",
  "hook": "Tes coûts, ce trimestre.",
  "punch": "On va refermer le robinet.",
  "heygen": "Tu enregistres tes achats fournisseurs avec le détail des lignes. Tes dépenses du mois s'additionnent toutes seules, en face de ton chiffre d'affaires.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic, close-up then wide, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A professional espresso machine begins to hiss abnormally. The barista taps it once. At 5 seconds a jet of steam and coffee erupts vertically from the group head, hitting the ceiling. Final 2 seconds: the barista stands completely still, drenched, holding an empty cup at arm's length under the spray. Audio: espresso machine hiss building into a pressurised roar, splattering liquid, dripping ceiling, then a single calm cup-on-saucer clink. No music."
 },
 {
  "id": "EP017",
  "n": 17,
  "t": "Le ninja de la frite",
  "mod": "StockVision",
  "ch": "19 - Création d'un rapport",
  "drive": "1Ib_pKyJ8_jaFAwtIhkzhtmUU_DCtGSSY",
  "hook": "Personne ne touche à ta dernière frite.",
  "punch": "Ni à ta marge.",
  "heygen": "Tu génères ton rapport par module en un clic : ventes, stock, production. L'historique est gardé. Tu compares ce mois-ci avec le mois dernier, pas avec ton souvenir.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic, cinematic slow motion, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. Two people share a basket of fries at a diner table; one fry remains. An adult hand moves toward it in slow motion. From the bottom of the frame a small child's hand shoots in and takes it with impossible speed. Final 2 seconds: the adult's hand closes on empty air; a child chews contentedly at the edge of frame. Audio: diner ambience, a dramatic slow-motion low drone, a sharp martial-arts whoosh at the snatch, a crunchy bite, one satisfied hum. No music."
 },
 {
  "id": "EP018",
  "n": 18,
  "t": "Le serveur Baywatch",
  "mod": "Service",
  "ch": "2 - Site, vocal et QR code",
  "drive": "1z4li_rdzH8yC7VFoWgOa4yMHbbKIAG29",
  "hook": "Le rush de vingt heures.",
  "punch": "Sauve ton service, pas ton dos.",
  "heygen": "Pendant le rush, tes clients commandent seuls : par QR à table, par le site, par l'agent vocal. Ton équipe sert, elle ne court plus.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic, slow motion, golden hour, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. Extreme slow motion of a waiter running across a packed restaurant terrace holding a tray of drinks perfectly steady, apron and hair flowing dramatically, sunset backlight, deeply serious expression. He weaves between tables like a lifeguard on a beach. Final 2 seconds: he arrives, places the tray down, and is instantly out of breath in real time. Audio: heroic slow-motion breathing and heartbeat, glassware chiming softly, ambience, then a sudden snap back to normal speed with heavy panting. No music."
 },
 {
  "id": "EP019",
  "n": 19,
  "t": "Le burger qui rebondit",
  "mod": "StockVision",
  "ch": "3 - Prédictions des commandes",
  "drive": "1Ib_pKyJ8_jaFAwtIhkzhtmUU_DCtGSSY",
  "hook": "Ton chiffre d'affaires, sans outil.",
  "punch": "Ça rebondit rarement tout seul.",
  "heygen": "FoodEatUp regarde tes ventes passées et te dit quoi produire demain. Ton chiffre d'affaires ne dépend plus de ton intuition du lundi matin.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic, extreme slow motion macro, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A double cheeseburger falls in extreme slow motion toward a kitchen floor. Sesame seeds detach and float. It hits, compresses, and improbably bounces once, layers separating mid-air. Final 2 seconds: it lands fully deconstructed, each ingredient in a neat row, as if plated on purpose. Audio: a low slow-motion whoosh, a soft wet impact, a comedic boing on the bounce, then a delicate settling sound. No music."
 },
 {
  "id": "EP020",
  "n": 20,
  "t": "Le chien qui a réservé",
  "mod": "Réservation",
  "ch": "2 - Ajouter une réservation",
  "drive": "1m6WdjC_iNYWO_4U3LmDuOsc-_Y_DrZLu",
  "hook": "Lui, il a réservé.",
  "punch": "Tes vrais clients aussi devraient pouvoir.",
  "heygen": "Tu ajoutes une réservation en dix secondes, la table libre est proposée automatiquement. Et tes clients peuvent le faire eux-mêmes, depuis ton site.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic, warm restaurant lighting, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A large dog sits upright on a chair at a set restaurant table, a napkin tucked into its collar, front paws resting on the tablecloth, waiting with immense dignity. A waiter approaches with a menu and offers it. Final 2 seconds: the dog looks at the menu, then straight at the camera, and lets out one small impatient huff. Audio: cosy restaurant ambience, gentle chatter, cutlery, a paper menu rustle, one deep dog huff. No music."
 },
 {
  "id": "EP021",
  "n": 21,
  "t": "Chef contre imprimante",
  "mod": "KDS",
  "ch": "1 - Créer tes postes KDS",
  "drive": "1wQAkcP9pY90DLu_sE8GLiI6WYHZuYwq9",
  "hook": "Le vrai ennemi du service.",
  "punch": "Un KDS, et le combat s'arrête.",
  "heygen": "Tu crées tes postes : chaud, froid, dessert. Chaque plat part au bon écran. Plus d'imprimante à secouer au milieu du service.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic, handheld kitchen, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A chef at the pass fights with a jammed ticket printer, pulling a crumpled strip of paper that keeps tearing. He shakes it, opens the lid, closes it, hits it once with the flat of his hand. At 5 seconds it prints an enormous unbroken ribbon of tickets straight onto the floor. Final 2 seconds: he stands holding the ribbon with both hands, expressionless. Audio: busy kitchen, printer grinding and jamming, plastic lid snapping, a frustrated French \"Allez !\", then continuous printing. No music."
 },
 {
  "id": "EP022",
  "n": 22,
  "t": "La facture qui fait pleurer",
  "mod": "PrediBot",
  "ch": "2 - Marketplace de prompts",
  "drive": "19kYZliyRnKraKVg1zdFrXCocD38VZ2a9",
  "hook": "Mille euros par mois.",
  "punch": "Pour dix logiciels qui ne se parlent même pas.",
  "heygen": "Tout est déjà là : caisse, stock, planning, marketing, HACCP. Un seul abonnement, une seule base de données. Tes outils arrêtent de s'ignorer.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic, moody desk lamp lighting, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A restaurant owner sits alone at night in the empty dining room with a laptop and a thick stack of invoices. He flips through them faster and faster, expression collapsing. At 5 seconds he stops, stares at one page, and slowly slides down until only his eyes are above the table edge. Final 2 seconds: just his eyes, the invoice held up beside them. Audio: empty room reverb, paper flipping accelerating, a chair creak, a long shaky exhale, a clock ticking. No music."
 },
 {
  "id": "EP023",
  "n": 23,
  "t": "L'aspirateur robot",
  "mod": "Marketing",
  "ch": "24 - Calendrier IA avec Iris",
  "drive": "1hBc6Axd0DE2ocTiXXKGlmj1dyagOwKFg",
  "hook": "Ton automatisation actuelle.",
  "punch": "Automatiser, oui. Mais bien.",
  "heygen": "Iris regarde ton exploitation et te propose quoi publier, et pourquoi. Tu valides ou tu refuses. L'automatisation te sert, elle ne t'échappe pas.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic, low floor-level camera, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A robot vacuum glides across a restaurant floor and catches the corner of a long tablecloth. It keeps going with total determination, dragging the cloth and everything on the table behind it in slow motion — glasses, cutlery, a vase. Final 2 seconds: the robot arrives at its dock, tablecloth and all, and its status light turns green. Audio: soft robot motor hum, fabric dragging, escalating glass and cutlery clatter, then a cheerful electronic docking chime. No music."
 },
 {
  "id": "EP024",
  "n": 24,
  "t": "La mouette braqueuse",
  "mod": "Mon Site",
  "ch": "5 - Créer un site par IA",
  "drive": "1ykcHl2BaY22WlCsBA3DuwXaEMvQZUtMF",
  "hook": "Encore une commission en moins.",
  "punch": "Récupère tes commandes en direct.",
  "heygen": "Ton site de commande est créé par l'IA depuis ta carte. Tes clients commandent en direct, chez toi. Zéro commission sur ces commandes-là.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic, seaside daylight, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A seaside restaurant terrace. A tray of fried fish and lemon sits on a table by the railing. A seagull swoops in from off-frame in a single confident dive, grabs the whole fish and pulls up. Final 2 seconds: the seagull perched on the railing with the fish, staring at the diners, wind ruffling its feathers. Audio: waves and sea wind, terrace chatter, a loud seagull cry, wing beats, a startled human gasp. No music."
 },
 {
  "id": "EP025",
  "n": 25,
  "t": "Le mixeur sans couvercle",
  "mod": "Marketing",
  "ch": "6 - Campagne 100 % IA",
  "drive": "1hBc6Axd0DE2ocTiXXKGlmj1dyagOwKFg",
  "hook": "Quand tu lances une promo sans données.",
  "punch": "Ça éclabousse. Et rarement toi.",
  "heygen": "Tu ne lances plus une promo au hasard. FoodEatUp te propose la campagne depuis tes vraies données clients : qui cibler, avec quelle offre, quel jour.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic, kitchen close-up, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A cook pours bright orange soup into a professional blender and, without noticing the missing lid, presses the highest setting. At 5 seconds soup erupts upward and outward, coating the wall, the ceiling and the cook. Final 2 seconds: he switches it off, wipes one eye clear with a finger, and looks at the camera. Audio: blender motor screaming to full speed, wet splattering, dripping, an abrupt switch-off click, then a single drip. No music."
 },
 {
  "id": "EP026",
  "n": 26,
  "t": "Le ballon qui explose",
  "mod": "StockVision",
  "ch": "5 - Envoyer sa liste de courses au fournisseur",
  "drive": "1Ib_pKyJ8_jaFAwtIhkzhtmUU_DCtGSSY",
  "hook": "Ton stock avant le week-end.",
  "punch": "Prévois, au lieu de subir.",
  "heygen": "Ta liste de courses se construit depuis ta production prévue. Tu l'envoies au fournisseur depuis l'écran. Le week-end se prépare le mercredi.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic macro, studio lighting on a stainless kitchen counter, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A red balloon is being inflated far past its limit next to a neat pyramid of fresh vegetables. The rubber stretches thin and translucent, trembling. Extreme slow motion at 5 seconds as it bursts, fragments peeling outward. Final 2 seconds: the vegetable pyramid stands untouched, a shred of red rubber draped over the top tomato. Audio: rubber stretching creak rising in pitch, a sharp burst, then quiet room tone. No music."
 },
 {
  "id": "EP027",
  "n": 27,
  "t": "Le chat et le verre",
  "mod": "Caisse POS",
  "ch": "6 - Clôturer sa caisse, le Z",
  "drive": "1nHjH82ig0i-MtQqDmYp131htOSThaPIQ",
  "hook": "Ta trésorerie, chaque lundi.",
  "punch": "Il suffit d'un truc mal placé.",
  "heygen": "Ton Z de caisse en un bouton : le compté, le théorique, l'écart, les moyens de paiement. Tu sais où tu en es tous les lundis matin.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic, locked-off close-up, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A black cat sits on a bar counter beside a full wine glass. It makes prolonged eye contact with the camera, then extends one paw and pushes the glass millimetre by millimetre toward the edge. At 6 seconds the glass tips over the edge. Final 2 seconds: the cat looks down at the floor, then back at the camera, entirely satisfied. Audio: quiet bar ambience, faint glass sliding on wood, a glass shattering off-frame, then one soft meow. No music."
 },
 {
  "id": "EP028",
  "n": 28,
  "t": "Le tapis à sushis fou",
  "mod": "HubRise",
  "ch": "4 - Centraliser les commandes",
  "drive": "19D09dNt_jZSKpcwVCU8Mn1OkMLkY_ojd",
  "hook": "Tes commandes en ligne, un vendredi.",
  "punch": "Tout arrive. Nulle part.",
  "heygen": "Uber Eats, Deliveroo, ton site, le comptoir : tout tombe dans la même file. Un vendredi soir, tu regardes un écran, pas quatre.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic, side tracking shot along the belt, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A conveyor-belt sushi restaurant. The belt slowly accelerates beyond normal speed; plates begin to blur past seated diners who turn their heads to follow. At 6 seconds plates start flying off the end of the belt one after another. Final 2 seconds: a diner calmly catches one out of the air with chopsticks without looking. Audio: mechanical belt hum rising in pitch, ceramic rattling, plates clattering off the end, a single clean chopstick click on the catch. No music."
 },
 {
  "id": "EP029",
  "n": 29,
  "t": "Les douze assiettes",
  "mod": "PrediBot",
  "ch": "1 - Lire ses prévisions",
  "drive": "19kYZliyRnKraKVg1zdFrXCocD38VZ2a9",
  "hook": "Toi, gérant, en 2026.",
  "punch": "Personne ne devrait travailler comme ça.",
  "heygen": "Le brief du jour te dit ce qui compte avant que ça te tombe dessus : les réservations, les productions, les alertes. Tu diriges au lieu de courir.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic, slow orbit around the subject, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A restaurant manager stands in a dining room with plates balanced everywhere — both forearms, one on his head, one in each hand, one wedged under his chin — while a phone rings in his apron pocket. He looks at the pocket, then at the camera, unable to move at all. Final 2 seconds: the phone keeps ringing; he closes his eyes. Audio: restaurant ambience, faint ceramic wobble, a phone ringing insistently from inside fabric, one long resigned breath. No music."
 },
 {
  "id": "EP030",
  "n": 30,
  "t": "Le pingouin en cuisine",
  "mod": "Configuration",
  "ch": "Academy",
  "drive": "19xTrrkXtWO3yfJqtC3SIlDgpBjSEc4N9",
  "hook": "Le nouveau, jour 1.",
  "punch": "Forme-le en un clic avec l'Académy.",
  "heygen": "Le nouveau se forme tout seul : chaque module a ses vidéos, dans l'ordre. Tu ne réexpliques plus la caisse à chaque embauche.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic, wide kitchen shot, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A penguin waddles into a professional restaurant kitchen wearing a tiny white apron. It steps onto a freshly mopped tile floor, immediately loses traction and slides the entire length of the kitchen on its belly, passing surprised cooks. Final 2 seconds: it stops against the base of a fridge, stands up, and shakes itself off with dignity. Audio: kitchen ambience, a wet tile squeak, a long comedic slide whoosh, a soft thud against the fridge, one penguin squawk. No music."
 },
 {
  "id": "EP031",
  "n": 31,
  "t": "L'avalanche de tupperware",
  "mod": "HACCP",
  "ch": "étiquettes DLC",
  "drive": "10rqzHFjXbjkGi73uJyjt3XQM92eaIMK_",
  "hook": "C'est quoi, ça ?",
  "punch": "Sans DLC tracées, personne ne sait.",
  "heygen": "Tu crées ton étiquette DLC en trois secondes, avec le produit, la date et l'agent. Plus personne n'ouvre un bac en se demandant ce que c'est.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic, cinematic handheld camera, shallow depth of field, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A cook opens the door of a tall stainless-steel restaurant fridge. For a beat nothing happens. At 5 seconds an avalanche of unlabelled plastic containers pours out onto the floor in slow motion, lids separating mid-air. Final 2 seconds: he stands ankle-deep in containers, holding the fridge door handle, staring at the camera. Audio: fridge seal sucking open, compressor hum, escalating plastic clattering, a lid spinning to a stop on the tiles, then silence. No music."
 },
 {
  "id": "EP032",
  "n": 32,
  "t": "La sauce trop forte",
  "mod": "StockVision",
  "ch": "1 - Ma carte, fiche recette",
  "drive": "1Ib_pKyJ8_jaFAwtIhkzhtmUU_DCtGSSY",
  "hook": "Ta recette « au feeling ».",
  "punch": "Une fiche technique, et c'est pareil tous les jours.",
  "heygen": "Ta recette est enregistrée : ingrédients, quantités, étapes. Le plat sort pareil que ce soit toi ou ton commis. Et son coût est calculé.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic, tight close-up, warm kitchen light, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A chef tastes his own sauce from a wooden spoon with total confidence. His expression holds for two seconds, then cracks: eyes watering, face reddening, breathing through the mouth. At 5 seconds he grabs a jug of water and drinks straight from it. Final 2 seconds: he lowers the jug, gives a thumbs up to the camera, eyes still streaming. Audio: kitchen ambience, a spoon tap, sharp inhaling through teeth, gulping, a strangled French \"Ça va, ça va\", then a small cough. No music."
 },
 {
  "id": "EP033",
  "n": 33,
  "t": "Le rôti disparu",
  "mod": "StockVision",
  "ch": "16 - Mouvements de stock",
  "drive": "1Ib_pKyJ8_jaFAwtIhkzhtmUU_DCtGSSY",
  "hook": "Tu as tout préparé. Presque.",
  "punch": "Ce qui n'est pas suivi finit par disparaître.",
  "heygen": "Ce qui n'est pas suivi disparaît. Ici chaque produit a son niveau, son seuil et son historique. Tu vois le trou avant le service, pas après.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic, warm dining room, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A long banquet table, beautifully set, a whole roast on a platter at the centre. Everyone has turned away to look off-frame. A large dog rises silently from under the table, takes the entire roast off the platter and disappears back down. At 5 seconds the guests turn back to an empty platter. Final 2 seconds: a slow tilt down to the dog under the table, roast between its paws, mid-bite. Audio: banquet chatter and cutlery, a soft platter scrape, chatter stopping abruptly, then contented chewing from below. No music."
 },
 {
  "id": "EP034",
  "n": 34,
  "t": "Le bouchon rebelle",
  "mod": "Configuration",
  "ch": "process",
  "drive": "19xTrrkXtWO3yfJqtC3SIlDgpBjSEc4N9",
  "hook": "Chaque service, une improvisation.",
  "punch": "Ça marche. Jusqu'au jour où ça ne marche plus.",
  "heygen": "Tes procédures sont dans l'outil, pas dans ta tête. Le service ne dépend plus de qui est là ce soir.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic, cinematic medium shot, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A waiter presents a bottle of wine tableside and works the corkscrew with growing effort, bracing the bottle against his hip. At 5 seconds the cork releases explosively and rockets upward out of frame; he keeps the polite smile. Final 2 seconds: a distant clink off-screen, the cork drops back down and lands in a guest's empty glass. The waiter nods once as if it was intentional. Audio: restaurant ambience, corkscrew creaking, a loud pop, a whoosh upward, a small ceiling tap, a glass clink, one guest laugh. No music."
 },
 {
  "id": "EP035",
  "n": 35,
  "t": "Le parasol fugitif",
  "mod": "PrediBot",
  "ch": "1 - Lire ses prévisions",
  "drive": "19kYZliyRnKraKVg1zdFrXCocD38VZ2a9",
  "hook": "Ta terrasse, un jour de vent.",
  "punch": "Certaines choses se prévoient.",
  "heygen": "Prévisions de fréquentation, météo, événements du quartier : PrediBot te dit à quoi ressemble ton service avant qu'il commence.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic, windy daylight, handheld chase, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A gust of wind lifts a large terrace parasol out of its base. A restaurant owner in an apron sprints after it down the pavement as it rolls and bounces ahead of him, always just out of reach. At 5 seconds he dives for it and misses. Final 2 seconds: he lies on the pavement, watching the parasol wedge itself politely into a bike rack twenty metres away. Audio: strong wind, fabric snapping, running footsteps, a scrape of metal on concrete, heavy breathing, a metallic clang on landing. No music."
 },
 {
  "id": "EP036",
  "n": 36,
  "t": "L'addition",
  "mod": "PrediBot",
  "ch": "2 - Un seul abonnement",
  "drive": "19kYZliyRnKraKVg1zdFrXCocD38VZ2a9",
  "hook": "Toi, devant tes abonnements.",
  "punch": "Additionne-les. Vraiment.",
  "heygen": "Additionne tes abonnements actuels. Ici, la caisse, le stock, le planning, la compta et le marketing sont dans le même outil, sur la même base.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic, moody restaurant lighting, slow push-in, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A man opens a leather bill folder at a restaurant table. He reads. He blinks. He removes his glasses, cleans them slowly on his napkin, puts them back on and reads again. Final 2 seconds: he closes the folder very gently, as if it were fragile, and stares into the middle distance. Audio: quiet restaurant ambience, leather creaking, a napkin rustle, one long slow exhale, distant glassware. No music."
 },
 {
  "id": "EP037",
  "n": 37,
  "t": "Le dormeur debout",
  "mod": "Équipe & Planning",
  "ch": "créer un shift",
  "drive": "1wboT7bVjEwxbhpU9Xgz8sRjjqn9XEd7X",
  "hook": "Fermeture. Troisième soir d'affilée.",
  "punch": "Un planning bien fait, ça se voit sur les visages.",
  "heygen": "Tu construis le planning de la semaine par glisser-déposer, avec le coût qui s'affiche en direct. Tes équipes savent, et toi aussi.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic, static wide, late-night restaurant, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. Closing time in an empty dining room, chairs on tables. A young employee stands leaning on a broom handle, completely asleep upright, swaying very slightly. At 5 seconds the broom slips a few centimetres; he jolts awake, sweeps three energetic strokes, then goes still again. Final 2 seconds: asleep on the broom once more. Audio: empty room reverb, a fridge hum, faint street noise, a broom bristle scrape, a startled inhale, then quiet breathing. No music."
 },
 {
  "id": "EP038",
  "n": 38,
  "t": "Le chariot fou",
  "mod": "StockVision",
  "ch": "4 - Ma liste de courses",
  "drive": "1Ib_pKyJ8_jaFAwtIhkzhtmUU_DCtGSSY",
  "hook": "Le réappro du lundi.",
  "punch": "Commander à l'instinct, ça finit toujours en course.",
  "heygen": "Ta commande fournisseur se construit depuis tes stocks bas et ta production prévue. Tu ne commandes plus à l'instinct dans les rayons.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic, tracking shot in a cash-and-carry warehouse, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A restaurateur pushes an overloaded flatbed trolley down a wholesale aisle. It gains speed on a slight slope, one wheel shuddering. He jogs, then runs, then lets go. At 5 seconds the trolley glides on alone in slow motion between the racks. Final 2 seconds: it stops itself perfectly against a pallet of tomatoes, nothing falls, and he raises both arms in silent victory. Audio: warehouse ambience, a rattling wheel rising in pitch, running footsteps, a soft cardboard bump, a distant forklift beeping. No music."
 },
 {
  "id": "EP039",
  "n": 39,
  "t": "Le ballon dans la soupe",
  "mod": "Réservation",
  "ch": "3 - Gérer et no-shows",
  "drive": "1m6WdjC_iNYWO_4U3LmDuOsc-_Y_DrZLu",
  "hook": "L'imprévu du service.",
  "punch": "Il y en aura d'autres. Autant être prêt.",
  "heygen": "L'imprévu, tu ne l'évites pas. Mais tu vois en direct l'état de ta salle, tes retards et tes annulations, et tu réattribues en un geste.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic, sunny terrace, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. Diners eat calmly on a street terrace. From off-frame a football arcs into shot in slow motion and lands squarely in a bowl of soup, sending an orange splash upward across the table. Final 2 seconds: total stillness, soup dripping off the edge of the table, everyone frozen mid-gesture, one child's face appearing at the terrace railing. Audio: terrace ambience, a distant kick, a whooshing arc, a wet heavy splash, dripping, then complete silence. No music."
 },
 {
  "id": "EP040",
  "n": 40,
  "t": "La chèvre au potager",
  "mod": "StockVision",
  "ch": "17 - Ajouter un mouvement",
  "drive": "1Ib_pKyJ8_jaFAwtIhkzhtmUU_DCtGSSY",
  "hook": "Ton stock de basilic.",
  "punch": "Ce qui n'est pas compté disparaît toujours.",
  "heygen": "Tu comptes une fois, l'outil compte ensuite. Chaque sortie d'ingrédient est déduite de ton stock, plat par plat.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic, golden hour, garden setting, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A small restaurant herb garden in neat labelled rows. A goat wanders calmly into frame and begins eating an entire row of basil with great efficiency. At 5 seconds a chef appears at the back door and freezes. Final 2 seconds: the goat looks up, a wooden plant label sticking out of its mouth, chewing without breaking eye contact. Audio: birdsong, gentle chewing, a wooden door creak, a sharp human intake of breath, one goat bleat. No music."
 },
 {
  "id": "EP041",
  "n": 41,
  "t": "Le poulet fugueur",
  "mod": "StockVision",
  "ch": "15 - Sortie des ingrédients de la production",
  "drive": "1Ib_pKyJ8_jaFAwtIhkzhtmUU_DCtGSSY",
  "hook": "Ton contrôle des portions.",
  "punch": "Ce qui part au sol, tu le paies quand même.",
  "heygen": "La production sort exactement les quantités prévues de ton stock. Ce qui tombe au sol, tu le vois dans l'écart. Et ce qui se voit se corrige.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic, kitchen close-up on a carving board, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A chef carves a glistening roast chicken with a long knife. On the third stroke the whole bird slides off the board in slow motion, skates across the stainless counter and drops off the far edge. Final 2 seconds: the chef is still holding the knife exactly where the chicken used to be, not yet looking down. Audio: knife on bone, a greasy slide across metal, a soft floor thud, kitchen extractor hum, one beat of silence. No music."
 },
 {
  "id": "EP042",
  "n": 42,
  "t": "La nappe et le vent",
  "mod": "Marketing",
  "ch": "21 - MCP RapidoCMS et Iris",
  "drive": "1hBc6Axd0DE2ocTiXXKGlmj1dyagOwKFg",
  "hook": "Tout faire seul.",
  "punch": "À un moment, il faut être aidé.",
  "heygen": "Tu n'as pas à tout faire seul. Iris prépare tes contenus, PrediBot surveille tes chiffres, tu gardes la validation.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic, windy outdoor terrace, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A waiter tries to fold a huge white tablecloth alone in the wind. Each time he brings two corners together, a gust inflates the cloth like a sail and wraps it around him. At 5 seconds he disappears completely inside the fabric. Final 2 seconds: a person-shaped white ghost stands motionless on the terrace, one hand emerging to give a thumbs up. Audio: wind gusts, fabric snapping loudly, muffled human grunting from inside the cloth, a chair scraping. No music."
 },
 {
  "id": "EP043",
  "n": 43,
  "t": "L'écureuil et le croissant",
  "mod": "Caisse POS",
  "ch": "4 - Remises et avoirs",
  "drive": "1nHjH82ig0i-MtQqDmYp131htOSThaPIQ",
  "hook": "Petit vol. Tous les jours.",
  "punch": "Mis bout à bout, ça fait ta marge.",
  "heygen": "Chaque remise et chaque avoir est tracé, avec qui l'a fait et pourquoi. Les petits gestes ne mangent plus ta marge en silence.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic, morning park-side café, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A croissant sits on a small saucer beside a coffee on an outdoor café table. A squirrel climbs the table leg, assesses the croissant, and takes it with both paws — it is almost as big as the squirrel. At 5 seconds it drags the croissant off the table and struggles up a nearby tree trunk with it. Final 2 seconds: the squirrel on a branch, croissant held triumphantly, flakes raining down. Audio: morning birdsong, a ceramic saucer tick, tiny claws on wood and bark, a bakery-flake rustle, a distant espresso machine. No music."
 },
 {
  "id": "EP044",
  "n": 44,
  "t": "Les six stylos",
  "mod": "Réservation",
  "ch": "5 - Commander par QR code",
  "drive": "1m6WdjC_iNYWO_4U3LmDuOsc-_Y_DrZLu",
  "hook": "Prendre la commande en 2026.",
  "punch": "La commande devrait partir en cuisine toute seule.",
  "heygen": "Le client scanne, commande, la cuisine reçoit. Ton serveur passe son temps en salle, pas à recopier des lignes sur un carnet.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic, over-the-shoulder at a dining table, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A waiter stands at a table with a notepad, ready to take an order. His pen does not write. He shakes it, scribbles, tries another from his apron, then another, then another, scribbling harder each time on the corner of the pad. At 5 seconds he has five dead pens lined up on the table. Final 2 seconds: he pulls out a sixth, it works, and the guests have already put their menus down and are looking at him. Audio: restaurant ambience, pen scribbling on paper, plastic pens clicking and tapping the table, one polite guest cough. No music."
 },
 {
  "id": "EP045",
  "n": 45,
  "t": "La chambre froide",
  "mod": "StockVision",
  "ch": "18 - Statistiques par module",
  "drive": "1Ib_pKyJ8_jaFAwtIhkzhtmUU_DCtGSSY",
  "hook": "Personne ne sait où tu es.",
  "punch": "Ton restaurant non plus ne devrait pas être une boîte noire.",
  "heygen": "Ton restaurant arrête d'être une boîte noire : ventes, marges, fréquentation, stock, module par module, sur la période que tu choisis.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic, cold blue interior light, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. Interior of a walk-in cold room. A cook is checking shelves when the heavy insulated door swings slowly shut behind him. He turns, pushes the handle, nothing. At 5 seconds he knocks politely, then harder, breath visible in the cold air. Final 2 seconds: he sits down on an upturned crate, resigned, and starts eating a cherry tomato from the shelf. Audio: refrigeration unit droning, a heavy door thud and latch click, knuckles on metal, breathing in cold air, a small crunch. No music."
 },
 {
  "id": "EP046",
  "n": 46,
  "t": "Le sel",
  "mod": "StockVision",
  "ch": "20 - Agent IA et suggestions",
  "drive": "1Ib_pKyJ8_jaFAwtIhkzhtmUU_DCtGSSY",
  "hook": "Un détail. Un service perdu.",
  "punch": "Les petites erreurs coûtent cher quand personne ne les voit.",
  "heygen": "L'IA remonte ce que tu n'as pas le temps de voir : un coût qui monte, un plat qui décroche, un stock qui dort. Le petit détail devient visible.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic, extreme slow-motion macro, dramatic side light, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. Macro slow motion of a hand seasoning a pan with a pinch of salt, grains falling in a beautiful arc. The shot widens slightly: the lid of the salt cellar has come off entirely and the whole contents are pouring into the pan in the same slow, elegant arc. Final 2 seconds: the empty cellar, a white mound in the pan, and a hand frozen mid-gesture. Audio: gentle sizzling, a delicate granular patter that becomes a heavy pour, a hollow plastic clatter as the lid lands, then sizzling alone. No music."
 },
 {
  "id": "EP047",
  "n": 47,
  "t": "Le camion dans la ruelle",
  "mod": "HACCP",
  "ch": "contrôle à réception",
  "drive": "10rqzHFjXbjkGi73uJyjt3XQM92eaIMK_",
  "hook": "La livraison de 7 h.",
  "punch": "Réceptionner, contrôler, tracer. Sans y penser.",
  "heygen": "À la livraison, tu contrôles la température, tu prends la photo, c'est tracé. Sept heures du matin, et ta conformité est déjà faite.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic, high-angle then street level, narrow European alley, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A delivery truck reverses into an alley barely wider than itself, mirrors folding against the walls. A cook stands behind it waving both arms with increasing energy and decreasing accuracy. At 5 seconds the truck stops with the bumper one centimetre from a stack of crates. Final 2 seconds: the cook gives an enthusiastic double thumbs up; the driver's arm emerges from the window with a single flat thumbs up. Audio: diesel engine, reversing beeper, tyre scrub on cobbles, a shouted French \"Encore ! Encore ! Stop !\", a hiss of air brakes. No music."
 },
 {
  "id": "EP048",
  "n": 48,
  "t": "La pyramide de sucre",
  "mod": "Configuration",
  "ch": "paramétrage initial",
  "drive": "19xTrrkXtWO3yfJqtC3SIlDgpBjSEc4N9",
  "hook": "Ce que tu construis chaque jour.",
  "punch": "Un système fragile finit toujours par tomber.",
  "heygen": "Tu poses ta base une fois : établissement, TVA, zones, équipements. Tout le reste de FoodEatUp s'appuie dessus sans que tu y reviennes.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic, café table close-up, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A child builds a tall precarious pyramid out of sugar sachets on a café table while the adults talk off-frame. The camera pushes in slowly as the structure grows to an improbable height. At 6 seconds an adult's elbow enters frame and clips it; the pyramid collapses in slow motion. Final 2 seconds: the child looks at the camera with genuine devastation, one sachet still balanced on a finger. Audio: café ambience, tiny paper sachets sliding, a soft cardboard collapse, one small disappointed sigh, a spoon in a cup. No music."
 },
 {
  "id": "EP049",
  "n": 49,
  "t": "Le chien du pass",
  "mod": "HACCP",
  "ch": "Relevé de température",
  "drive": "10rqzHFjXbjkGi73uJyjt3XQM92eaIMK_",
  "hook": "Il envoie plus vite que ton pass.",
  "punch": "Un KDS, et la cuisine avance toute seule.",
  "heygen": "Tu relèves tes frigos depuis ton téléphone. La mesure est datée, signée, archivée. Un contrôle, et tu sors trois mois d'historique en un clic.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic, kitchen pass, warm service light, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A dog sits at the kitchen pass, exactly where a chef would stand, front paws on the counter. It looks at a plate, then raises one paw and rings the service bell decisively. A waiter appears, takes the plate, and leaves. At 5 seconds the dog rings the bell twice more, faster. Final 2 seconds: it stares down the empty pass, waiting for the next plate, entirely professional. Audio: kitchen ambience, a crisp service bell ding, hurried footsteps, plates, two more bell dings, one impatient dog huff. No music."
 },
 {
  "id": "EP050",
  "n": 50,
  "t": "La casserole brûlante",
  "mod": "HACCP",
  "ch": "Équipements",
  "drive": "10rqzHFjXbjkGi73uJyjt3XQM92eaIMK_",
  "hook": "Apprendre sur le tas.",
  "punch": "Il y a plus rapide pour former quelqu'un.",
  "heygen": "Chaque frigo, chaque chambre froide est déclaré avec ses seuils. Hors zone, tu es alerté. Tu sauves la marchandise avant de la jeter.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic, handheld kitchen, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A cook grabs a pan handle bare-handed, instantly regrets it, and juggles the pan between his hands in a rapid improvised dance while trying not to spill the contents. At 5 seconds he manages to drop it onto the counter, upright, without losing a single thing inside. Final 2 seconds: he stands very still, both hands pressed against his own earlobes, staring at the pan. Audio: sizzling, a sharp metallic clang, fast shuffling feet, a sucked-in French \"Ah ah ah !\", a heavy pan settling on steel. No music."
 },
 {
  "id": "EP051",
  "n": 51,
  "t": "La mousse",
  "mod": "HACCP",
  "ch": "Étiquettes DLC",
  "drive": "10rqzHFjXbjkGi73uJyjt3XQM92eaIMK_",
  "hook": "Un mauvais réglage. Une seule fois.",
  "punch": "Les process, ça évite ça.",
  "heygen": "Étiquette produite, date de fabrication, DLC calculée. Ton bac étiqueté n'est plus un pari.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic, dishwashing area, cool light, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A commercial dishwasher hums. A slow column of white foam begins to rise from its seams, then from underneath, spreading across the floor. A kitchen porter watches it approach his shoes without moving. At 6 seconds the foam reaches his knees. Final 2 seconds: only his head and shoulders are visible above a sea of foam; he blows a small tuft off his nose. Audio: dishwasher hum, wet bubbling and hissing foam, squeaking rubber boots, a single blown puff of air. No music."
 },
 {
  "id": "EP052",
  "n": 52,
  "t": "Le tablier coincé",
  "mod": "HACCP",
  "ch": "Traçabilité",
  "drive": "10rqzHFjXbjkGi73uJyjt3XQM92eaIMK_",
  "hook": "Encore un truc qui te retient.",
  "punch": "Enlève-les tous, un par un.",
  "heygen": "Chaque lot reçu est rattaché à ce que tu produis. En cas de rappel, tu remontes la chaîne en quelques secondes.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic, kitchen corridor, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A chef strides purposefully out of the kitchen carrying two plates. His apron string catches in the swinging door behind him. He is yanked to a dead stop mid-stride, plates still perfectly level. At 5 seconds he calmly reverses two steps, unhooks the string without putting the plates down, and continues. Final 2 seconds: he walks off, dignity fully intact, as the door swings behind him. Audio: kitchen ambience, brisk footsteps, a fabric snap and door creak, one abrupt stop, then footsteps resuming at the exact same rhythm. No music."
 },
 {
  "id": "EP053",
  "n": 53,
  "t": "La file et la salle vide",
  "mod": "HACCP",
  "ch": "Réception fournisseur",
  "drive": "10rqzHFjXbjkGi73uJyjt3XQM92eaIMK_",
  "hook": "Complet dehors. Vide dedans.",
  "punch": "Ta salle et ta file devraient se parler.",
  "heygen": "Contrôle à réception : température, aspect, quantité, non-conformités. Tout part dans le dossier HACCP tout seul.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic, street level then interior, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A long queue of people waits patiently outside a restaurant door on the pavement. The camera moves past them, through the doorway, and reveals a completely empty dining room with every table free and one waiter standing alone. At 6 seconds the waiter notices the camera and shrugs. Final 2 seconds: back outside, the queue has grown by three people. Audio: street ambience, murmuring queue, a door chime on entry, sudden interior quiet with a faint fridge hum, one shrugging exhale. No music."
 },
 {
  "id": "EP054",
  "n": 54,
  "t": "Le pois",
  "mod": "HACCP",
  "ch": "Plan de nettoyage",
  "drive": "10rqzHFjXbjkGi73uJyjt3XQM92eaIMK_",
  "hook": "Ton prix ne raconte pas ton coût.",
  "punch": "Marge réelle par plat. Ça change les décisions.",
  "heygen": "Tes zones et tes postes de nettoyage sont listés. Qui a fait quoi, quand, c'est enregistré. Le plan de nettoyage vit vraiment.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic, fine-dining table, dramatic spotlight, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A waiter places a large silver cloche in front of a hungry-looking guest and lifts it with a theatrical flourish. Steam curls upward. In the centre of an enormous white plate sits one single pea, immaculately placed. At 6 seconds the guest looks up at the waiter, who nods proudly. Final 2 seconds: the guest looks back at the pea, then at the camera. Audio: refined dining ambience, a soft cloche lift and metallic ring, a delicate steam hiss, a long silence, one quiet stomach rumble. No music."
 },
 {
  "id": "EP055",
  "n": 55,
  "t": "Le ventilateur",
  "mod": "HACCP",
  "ch": "Checklists hygiène",
  "drive": "10rqzHFjXbjkGi73uJyjt3XQM92eaIMK_",
  "hook": "Ta compta, au format papier.",
  "punch": "Scanne. Classe. Oublie.",
  "heygen": "Tu crées ta checklist une fois, l'équipe la valide chaque jour. Ce qui est coché est daté et signé.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic, back office, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A manager sits at a paper-covered desk in a hot back office and switches on a floor fan for relief. He closes his eyes with pleasure for two seconds. At 5 seconds every invoice, ticket and delivery note on the desk lifts into the air at once and swirls around the room in slow motion. Final 2 seconds: the room is full of drifting paper; he has not opened his eyes, still enjoying the breeze. Audio: fan motor spinning up, a hot room's stillness, an escalating paper flutter, sheets slapping walls, one contented sigh. No music."
 },
 {
  "id": "EP056",
  "n": 56,
  "t": "Le passager clandestin",
  "mod": "HACCP",
  "ch": "Historique",
  "drive": "10rqzHFjXbjkGi73uJyjt3XQM92eaIMK_",
  "hook": "Il y a toujours un truc en trop.",
  "punch": "Ou en moins. Et tu le vois trop tard.",
  "heygen": "Tes relevés, tes réceptions et tes validations sont conservés. Le jour du contrôle, tu ne cherches rien.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic, street level, delivery scene, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A delivery rider unzips a large insulated backpack on the pavement to check an order. A cat's head pops out from between the food bags, blinking in the daylight. The rider stares. At 5 seconds the cat settles back down comfortably among the bags. Final 2 seconds: the rider slowly zips the bag half-closed, leaving the cat's head out, and rides off. Audio: street ambience, a zip opening, a single questioning meow, a long human pause, purring, a scooter starting up. No music."
 },
 {
  "id": "EP057",
  "n": 57,
  "t": "Les pièces",
  "mod": "HACCP",
  "ch": "Alertes",
  "drive": "10rqzHFjXbjkGi73uJyjt3XQM92eaIMK_",
  "hook": "La clôture de caisse.",
  "punch": "Un Z propre, en une minute.",
  "heygen": "Une température hors seuil déclenche une alerte immédiate. Tu réagis pendant le service, pas le lendemain.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic, close-up at a bar counter at night, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A manager counts coins into stacks on a bar counter, tongue between teeth, deeply focused. He reaches for the last stack and knocks the whole arrangement over. Coins spread across the counter and cascade off the edge in slow motion, rolling in every direction across the floor. Final 2 seconds: one coin rolls a long way alone, wobbles, and settles flat. Audio: quiet closed bar, coins clinking into stacks, a sudden metallic cascade, coins rolling and spinning on tiles, a final wobble and flat clack. No music."
 },
 {
  "id": "EP058",
  "n": 58,
  "t": "Les bougies",
  "mod": "HACCP",
  "ch": "Rôles",
  "drive": "10rqzHFjXbjkGi73uJyjt3XQM92eaIMK_",
  "hook": "L'anniversaire de la table 12.",
  "punch": "Anticiper, c'est aussi ça, le service.",
  "heygen": "Chaque agent signe ses propres relevés. La responsabilité est claire, sans paperasse supplémentaire.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic, dim restaurant, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A waiter carries a birthday cake crowned with far too many sparkling candles through a darkened dining room, guests turning to look. At 5 seconds a ceiling smoke detector begins flashing directly above him. Final 2 seconds: the sprinkler has not gone off, but every guest is looking up at the ceiling instead of the cake, and the waiter closes his eyes. Audio: murmured happy-birthday singing, crackling sparklers, a shrill smoke alarm cutting through everything, chairs scraping, then the alarm alone. No music."
 },
 {
  "id": "EP059",
  "n": 59,
  "t": "L'ardoise",
  "mod": "HACCP",
  "ch": "Non-conformité",
  "drive": "10rqzHFjXbjkGi73uJyjt3XQM92eaIMK_",
  "hook": "Ta com', chaque matin.",
  "punch": "Il y a plus solide qu'une ardoise.",
  "heygen": "Tu déclares une non-conformité, tu notes l'action corrective. C'est exactement ce qu'on te demandera de prouver.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic, windy pavement outside a bistro, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A restaurant owner sets a wooden A-frame chalkboard sign on the pavement. The wind knocks it flat immediately. He stands it up again, angles it differently — it falls again. At 5 seconds he props it with a stone, steps back to admire it, and it falls a third time. Final 2 seconds: he sits down on the kerb next to the fallen sign and simply holds it upright with one hand. Audio: gusty wind, wood clattering on pavement, chalk scraping, a resigned French \"Bon.\", street traffic. No music."
 },
 {
  "id": "EP060",
  "n": 60,
  "t": "Le poulpe multitâche",
  "mod": "HACCP",
  "ch": "Congélation",
  "drive": "10rqzHFjXbjkGi73uJyjt3XQM92eaIMK_",
  "hook": "Ce qu'on te demande d'être.",
  "punch": "Ou alors, un seul outil fait le reste.",
  "heygen": "Tu enregistres une mise en congélation avec sa date et sa quantité. Plus de sac sans nom au fond du bac.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic, surreal but grounded, professional kitchen, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A large octopus sits in a stainless-steel sink in a working kitchen, calmly operating eight things at once with its arms: stirring a pot, flipping a pan, wiping a counter, ringing the service bell, holding a knife, plating, adjusting a burner and answering a wall phone. Human cooks work around it without reacting. Final 2 seconds: it pauses every arm simultaneously and turns one eye toward the camera. Audio: full busy kitchen soundscape layered dense — sizzling, bell, phone ringing, chopping, extractor — then all of it stopping at once for the final beat. No music."
 },
 {
  "id": "EP061",
  "n": 61,
  "t": "Le badge introuvable",
  "mod": "HACCP",
  "ch": "Rapport HACCP",
  "drive": "10rqzHFjXbjkGi73uJyjt3XQM92eaIMK_",
  "hook": "Ton système de pointage.",
  "punch": "Un badge, un QR code, un code PIN. Point.",
  "heygen": "Tu édites ton dossier de conformité sur la période de ton choix, prêt à présenter.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic, cinematic handheld camera, shallow depth of field, natural light, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. Early morning at a restaurant staff entrance. A young employee taps a supermarket loyalty card against the door reader. Nothing. He tries a metro pass. Nothing. He tries his wrapped sandwich. At 5 seconds the door opens on its own because a colleague pushes it from inside, and he walks in holding the sandwich against the reader. Final 2 seconds: the reader blinks red, alone, as the door closes. Audio: quiet street ambience, three flat error beeps, plastic tapping on a reader, a door hinge, a colleague's mumbled \"Bonjour\", then one last error beep. No music."
 },
 {
  "id": "EP062",
  "n": 62,
  "t": "La photo de pointage",
  "mod": "HACCP",
  "ch": "Routine du jour",
  "drive": "10rqzHFjXbjkGi73uJyjt3XQM92eaIMK_",
  "hook": "Je te jure, j'étais là à 8 h.",
  "punch": "Photo, heure, poste. Le débat est clos.",
  "heygen": "La conformité devient une routine de deux minutes par service, au lieu d'un dimanche de rattrapage.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic, front-on framing as if from a tablet camera, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. An employee stands in front of a wall-mounted tablet at the staff entrance, taking his clock-in photo. He tries a neutral face, then a serious face, then a slight smile, then a full grin, adjusting his hair between each. At 5 seconds he settles on an intensely dramatic, chin-lifted expression. Final 2 seconds: he holds it perfectly still, absolutely committed. Audio: staff room ambience, a soft camera shutter repeated five times, fabric rustling, one satisfied exhale. No music."
 },
 {
  "id": "EP063",
  "n": 63,
  "t": "Le post-it perdu",
  "mod": "Équipe & Planning",
  "ch": "Créer un employé",
  "drive": "1wboT7bVjEwxbhpU9Xgz8sRjjqn9XEd7X",
  "hook": "Ta demande de congé.",
  "punch": "Demandée, reçue, validée. Sans papier.",
  "heygen": "Tu crées ta fiche employé avec son rôle et ses horaires. Elle alimente le planning, les pointages et la paie.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic, office corridor, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. An employee writes carefully on a yellow sticky note, presses it firmly onto the manager's office door, and walks away satisfied. The camera stays on the door. At 5 seconds the note peels off in slow motion, drifts sideways and slides down the gap behind a radiator. Final 2 seconds: the empty door, one corner of yellow just visible behind the radiator grille. Audio: corridor ambience, pen on paper, a sticky note pressed to wood, footsteps leaving, a faint paper slide, a metallic radiator tick. No music."
 },
 {
  "id": "EP064",
  "n": 64,
  "t": "Le planning au marqueur",
  "mod": "Équipe & Planning",
  "ch": "Planning semaine",
  "drive": "1wboT7bVjEwxbhpU9Xgz8sRjjqn9XEd7X",
  "hook": "Le planning de la semaine.",
  "punch": "Par employé ou par poste. Imprimable. À jour.",
  "heygen": "Le planning se construit en glisser-déposer, avec le coût de la semaine qui s'affiche pendant que tu poses les shifts.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic, staff room, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A whiteboard weekly rota covered in layers of crossings-out, arrows, magnets and three different marker colours. A manager studies it, then adds a strip of masking tape over one section and writes a new name on the tape. At 5 seconds a magnet gives way and half the paper slips sideways. Final 2 seconds: he presses it back with one finger and holds it there, looking at the camera. Audio: staff room ambience, squeaky marker on whiteboard, tape tearing, a magnet clattering to the floor, one long exhale. No music."
 },
 {
  "id": "EP065",
  "n": 65,
  "t": "Le stagiaire au bureau",
  "mod": "Équipe & Planning",
  "ch": "Pointages",
  "drive": "1wboT7bVjEwxbhpU9Xgz8sRjjqn9XEd7X",
  "hook": "Qui a accès à quoi ?",
  "punch": "Chaque rôle voit exactement ce qu'il doit voir.",
  "heygen": "Les heures réelles sont pointées. Tu compares le prévu et le réalisé, sans discussion de fin de mois.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic, back office, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A very young intern sits in the manager's oversized leather chair, feet up on the desk, slowly spinning, holding the manager's coffee mug. He opens a drawer, looks inside, nods approvingly. At 5 seconds the office door opens off-frame; he freezes mid-spin, feet still on the desk. Final 2 seconds: he is standing perfectly straight beside the chair, mug behind his back. Audio: office ambience, a chair spinning and creaking, a drawer sliding, a door handle turning, an abrupt scramble, then silence. No music."
 },
 {
  "id": "EP066",
  "n": 66,
  "t": "Le grille-pain qui ne répond pas",
  "mod": "Équipe & Planning",
  "ch": "Congés",
  "drive": "1wboT7bVjEwxbhpU9Xgz8sRjjqn9XEd7X",
  "hook": "Ta cuisine n'a personne à qui parler.",
  "punch": "Jarvis répond, lui. Et il note.",
  "heygen": "Une demande de congé arrive, tu valides ou tu refuses depuis l'écran. Le planning se met à jour tout seul.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic, professional kitchen, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A cook, hands covered in flour, leans toward a stainless-steel toaster on the counter and speaks to it clearly, waiting for an answer. Nothing. He speaks again, louder, more articulately. At 5 seconds the toaster ejects two slices of toast violently. He takes this as a response and nods. Final 2 seconds: he goes back to work, satisfied, having received his answer. Audio: kitchen ambience, a muffled human question, a pause, a second louder question, a metallic toaster spring-pop, one accepting \"Ah, d'accord.\" No music."
 },
 {
  "id": "EP067",
  "n": 67,
  "t": "Le thermomètre humain",
  "mod": "Équipe & Planning",
  "ch": "Contrats",
  "drive": "1wboT7bVjEwxbhpU9Xgz8sRjjqn9XEd7X",
  "hook": "Ton relevé de température.",
  "punch": "Un vrai relevé, horodaté, par équipement.",
  "heygen": "Contrats et documents employés sont rangés au même endroit, avec leurs échéances.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic, kitchen fridge close-up, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A chef opens a fridge door, holds his bare hand inside for exactly two seconds, withdraws it, and gives a confident single nod as if a precise measurement has been taken. He writes nothing down. At 5 seconds he repeats the procedure on the freezer, this time with two fingers, and nods even more confidently. Final 2 seconds: he closes the door and walks away, hands in pockets, entirely satisfied with his data collection. Audio: fridge seal opening and closing, compressor hum, kitchen ambience, one decisive \"Hm.\" repeated twice. No music."
 },
 {
  "id": "EP068",
  "n": 68,
  "t": "Le second avis",
  "mod": "Équipe & Planning",
  "ch": "Coût du travail",
  "drive": "1wboT7bVjEwxbhpU9Xgz8sRjjqn9XEd7X",
  "hook": "Le test scientifique du nez.",
  "punch": "Une étiquette DLC, et plus personne ne renifle.",
  "heygen": "Ton coût de personnel s'affiche en face de ton chiffre d'affaires prévu. Tu ajustes avant, pas après.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic, kitchen close-up, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A cook opens a large tub of cream and sniffs it long and deeply, eyes narrowed in genuine scientific concentration. He sniffs again. Uncertain, he holds it out toward a colleague. The colleague sniffs, makes exactly the same face, and hands it back without a word. At 5 seconds a third cook enters frame, sniffs, and shrugs. Final 2 seconds: all three stand in a small circle staring at the tub, nobody deciding. Audio: kitchen ambience, deep deliberate sniffing, plastic lid flexing, a noncommittal grunt, a shrug of fabric, silence. No music."
 },
 {
  "id": "EP069",
  "n": 69,
  "t": "Le livreur fantôme",
  "mod": "Équipe & Planning",
  "ch": "Recrutement",
  "drive": "1wboT7bVjEwxbhpU9Xgz8sRjjqn9XEd7X",
  "hook": "Tu as vérifié la livraison ?",
  "punch": "Température, DLC, code EAN. En scannant.",
  "heygen": "Tu publies ton offre, tu suis les candidatures par statut, tu décides. Le recrutement arrête de traîner sur ton téléphone.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic, restaurant back door, morning, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A delivery driver stacks fifteen boxes and crates against the back door with impressive speed, drops a crumpled delivery note on top, and is already jogging back to his van before anyone appears. At 5 seconds the kitchen door opens and a cook steps out holding a pen, looking at an empty street. Final 2 seconds: the van pulls away in the background; the cook looks down at the tower of unchecked boxes. Audio: crates thudding on concrete, fast footsteps, a van door sliding shut, an engine pulling away, a kitchen door creak, then street quiet. No music."
 },
 {
  "id": "EP070",
  "n": 70,
  "t": "La dalle propre",
  "mod": "Équipe & Planning",
  "ch": "Onboarding",
  "drive": "1wboT7bVjEwxbhpU9Xgz8sRjjqn9XEd7X",
  "hook": "C'est fait.",
  "punch": "Photo analysée par l'IA. Rapport objectif.",
  "heygen": "Le nouveau arrive avec son accès, son planning et ses vidéos de formation. Jour un, il est utile.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic, high angle then low angle, kitchen floor, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. An employee mops a single floor tile with extraordinary dedication, back and forth, until it gleams. The camera pulls back slowly to reveal the entire rest of the kitchen floor untouched and grimy. At 6 seconds he steps back to admire his one perfect tile, hands on hips. Final 2 seconds: he takes a photo of that single tile with his phone. Audio: kitchen ambience, wet mop strokes on tile, a bucket handle clank, a phone camera shutter, one proud sigh. No music."
 },
 {
  "id": "EP071",
  "n": 71,
  "t": "La liste à l'envers",
  "mod": "Équipe & Planning",
  "ch": "Multi-postes",
  "drive": "1wboT7bVjEwxbhpU9Xgz8sRjjqn9XEd7X",
  "hook": "La check-list du soir.",
  "punch": "Cochée, horodatée, signée par qui l'a faite.",
  "heygen": "Tu affectes tes équipes par poste et par zone. Chacun sait où il est attendu ce soir.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic, kitchen corridor, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A cook ticks boxes on a paper checklist at high speed without ever looking at the sheet, walking down a corridor. Tick, tick, tick, tick. At 5 seconds he reaches the end, signs it with a flourish, and pins it to the wall. Final 2 seconds: the camera holds on the sheet, which is pinned completely upside down. Audio: brisk footsteps, rapid pen ticking on paper, a satisfied hum, a pin pushing into a corkboard, then corridor quiet. No music."
 },
 {
  "id": "EP072",
  "n": 72,
  "t": "Le classeur",
  "mod": "Équipe & Planning",
  "ch": "Absences",
  "drive": "1wboT7bVjEwxbhpU9Xgz8sRjjqn9XEd7X",
  "hook": "Contrôle sanitaire. Ce matin.",
  "punch": "Tout l'historique HACCP, exporté en un clic.",
  "heygen": "Une absence, et tu vois immédiatement quel service est découvert. Tu remplaces avant l'ouverture.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic, restaurant office, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A health inspector in a jacket stands waiting with a clipboard. The manager hauls an enormous overstuffed ring binder onto the desk between them. He opens it. At 5 seconds the rings give way and several hundred loose pages fan out across the desk and floor in slow motion. Final 2 seconds: the two men look at each other over a desk covered in paper; the inspector clicks his pen once. Audio: office ambience, a heavy binder thud, metal rings snapping open, a long paper cascade, one pen click, total silence. No music."
 },
 {
  "id": "EP073",
  "n": 73,
  "t": "Pile ou face",
  "mod": "Configuration",
  "ch": "Établissement",
  "drive": "19xTrrkXtWO3yfJqtC3SIlDgpBjSEc4N9",
  "hook": "Combien tu commandes pour samedi ?",
  "punch": "Tes ventes le savent. Demande-leur.",
  "heygen": "Tu paramètres ton établissement une fois : horaires, coordonnées, TVA. Tout FoodEatUp s'appuie dessus.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic, bakery kitchen at dawn, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A chef stands in front of empty bread racks holding a coin. He flips it, catches it on the back of his hand, looks at it, and writes a number on an order pad. Unsatisfied, he flips again. At 5 seconds he flips a third time, misses the catch, and the coin rolls under a rack. Final 2 seconds: he writes a number anyway, without the coin. Audio: quiet early-morning kitchen, a coin ringing off a thumb, a slap on skin, pen on paper, a coin rolling on tiles, then silence. No music."
 },
 {
  "id": "EP074",
  "n": 74,
  "t": "La liste oubliée",
  "mod": "Configuration",
  "ch": "Catégories",
  "drive": "19xTrrkXtWO3yfJqtC3SIlDgpBjSEc4N9",
  "hook": "Tu as oublié la liste.",
  "punch": "Elle se construit toute seule. Et elle part au fournisseur.",
  "heygen": "Tes catégories de produits, d'ingrédients et de recettes structurent tout le reste. Cinq minutes qui t'en font gagner cent.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic, wholesale market aisle, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A restaurateur stands still in the middle of a busy wholesale market aisle, patting every pocket of his jacket, then his trousers, then his jacket again. He looks at his empty hands. At 5 seconds he turns a full slow circle on the spot, trolley beside him, surrounded by produce, remembering nothing. Final 2 seconds: he picks up one random cabbage and looks at it as if it might help. Audio: busy market ambience, forklift beeps, fabric patting, a trolley wheel squeak, one hopeless \"Bon…\", crowd murmur. No music."
 },
 {
  "id": "EP075",
  "n": 75,
  "t": "La facture dans la poche",
  "mod": "Configuration",
  "ch": "TVA",
  "drive": "19xTrrkXtWO3yfJqtC3SIlDgpBjSEc4N9",
  "hook": "Ta facture fournisseur.",
  "punch": "Photographie-la. Les prix se mettent à jour seuls.",
  "heygen": "Tes taux de TVA sont posés une fois, appliqués partout : caisse, factures, comptabilité.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic, macro on a stainless counter, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A hand pulls a heavily crumpled paper invoice out of an apron pocket and unfolds it on a counter, smoothing it flat with the side of the hand. The paper is stained with oil and sauce, and one corner is torn away. At 5 seconds the hand rotates it ninety degrees, trying to find a readable angle. Final 2 seconds: the paper slowly re-folds itself back into its crumpled shape on its own. Audio: paper crackling and unfolding, a hand smoothing paper on steel, kitchen ambience, one defeated exhale, a soft paper rustle as it curls back. No music."
 },
 {
  "id": "EP076",
  "n": 76,
  "t": "Le recomptage",
  "mod": "Configuration",
  "ch": "Zones et tables",
  "drive": "19xTrrkXtWO3yfJqtC3SIlDgpBjSEc4N9",
  "hook": "Ton inventaire du mardi.",
  "punch": "La production sort les ingrédients du stock. Automatiquement.",
  "heygen": "Tu dessines ta salle : zones, tables, capacités. Ton plan de salle devient vivant pendant le service.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic, walk-in fridge, cold light, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A chef counts vacuum-packed steaks on a shelf out loud, pointing at each one. He reaches the end, frowns, and starts again from the beginning. Second count gives a different number. He starts a third time, now moving each pack physically to the other side of the shelf as he counts. At 6 seconds a colleague walks past and takes one. Final 2 seconds: the chef finishes his count, satisfied, unaware. Audio: cold room compressor drone, vacuum plastic crinkling, murmured counting in French, footsteps passing, plastic rustle, then counting continuing. No music."
 },
 {
  "id": "EP077",
  "n": 77,
  "t": "Le devis sur le set de table",
  "mod": "Configuration",
  "ch": "Équipements",
  "drive": "19xTrrkXtWO3yfJqtC3SIlDgpBjSEc4N9",
  "hook": "Ton devis pour le mariage de samedi.",
  "punch": "Devis, envoi, acceptation, facture. Une seule chaîne.",
  "heygen": "Tu déclares tes équipements et leurs seuils. Ils remontent ensuite dans ton suivi HACCP.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic, restaurant table, warm light, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A restaurant owner sits across from a couple planning a wedding. Having no notepad, he writes numbers on a paper placemat, then continues onto a second placemat, then onto a napkin. At 5 seconds he slides all three across the table toward them as a formal proposal. Final 2 seconds: the bride picks up the napkin, turns it over, and finds a coffee ring on the total. Audio: restaurant ambience, pen scratching on textured paper, paper sliding on wood, a polite \"Voilà !\", one uncertain \"Ah.\", cutlery in the background. No music."
 },
 {
  "id": "EP078",
  "n": 78,
  "t": "La boîte à chaussures",
  "mod": "Configuration",
  "ch": "Utilisateurs",
  "drive": "19xTrrkXtWO3yfJqtC3SIlDgpBjSEc4N9",
  "hook": "Ta comptabilité annuelle.",
  "punch": "Chaque dépense rattachée à sa livraison. Toute l'année.",
  "heygen": "Chaque membre de l'équipe a son accès et ses droits. Tout le monde ne voit pas la compta.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic, accountant's office, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A restaurateur places a shoebox on an accountant's desk and lifts the lid. It is packed to the brim with crumpled receipts and invoices, some folded, some torn. The accountant looks into the box for a long moment without moving. At 5 seconds a single receipt escapes and drifts to the floor. Final 2 seconds: the accountant slowly puts the lid back on and slides the box six centimetres to one side. Audio: quiet office ambience, cardboard lid lifting, dense paper settling, a clock ticking, a single sheet fluttering to the floor, a cardboard slide on wood. No music."
 },
 {
  "id": "EP079",
  "n": 79,
  "t": "Les quatorze cartes",
  "mod": "Configuration",
  "ch": "Import de carte",
  "drive": "19xTrrkXtWO3yfJqtC3SIlDgpBjSEc4N9",
  "hook": "Ton programme de fidélité.",
  "punch": "Un compte, tous les canaux, zéro carton.",
  "heygen": "Tu importes ta carte entière en un appel : catégories, sous-catégories, plats, prix.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic, café counter close-up, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A customer at a counter pulls a thick stack of paper loyalty cards from his wallet and fans them out like a poker hand. He searches through them one by one, checking the stamps. Every card is partially stamped; none is complete. At 6 seconds he finds one with nine stamps out of ten, holds it up hopefully, then reads the expiry date and lowers it. Final 2 seconds: he puts them all back and pays normally. Audio: café ambience, espresso machine, cards shuffling and flicking, a hopeful \"Ah !\", a disappointed \"Ah.\", a card slipping back into a wallet. No music."
 },
 {
  "id": "EP080",
  "n": 80,
  "t": "Le tiroir vide",
  "mod": "Configuration",
  "ch": "Abonnement",
  "drive": "19xTrrkXtWO3yfJqtC3SIlDgpBjSEc4N9",
  "hook": "Ouverture. Fond de caisse : ?",
  "punch": "Fond déclaré, opérateur identifié, service ouvert.",
  "heygen": "Tu vois ton plan, tes options actives et ce que tu consommes. Aucune ligne surprise en fin de mois.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic, bar counter before opening, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A manager pulls open a cash drawer at the start of service. It is completely empty. He closes it, opens it again as if that might help, then blows into it the way one blows into an old game cartridge. At 5 seconds he checks under the counter, behind the till, and inside an empty mug. Final 2 seconds: he stands holding the empty drawer, looking off toward the front door where a first customer is arriving. Audio: cash drawer mechanism sliding twice, a hollow blow into plastic, hands patting under a counter, a ceramic mug lifted and set down, a shop door bell. No music."
 },
 {
  "id": "EP081",
  "n": 81,
  "t": "Huit calculatrices",
  "mod": "Comptabilité",
  "ch": "Factures",
  "drive": "1KlXihMLILGDrlxDuO2d3VCe1ic-kCAw_",
  "hook": "On peut séparer ?",
  "punch": "Oui. Par personne, par article, par montant.",
  "heygen": "Chaque commande produit sa facture, numérotée et conforme. Tu ne la ressaisis nulle part.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic, restaurant table, evening, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. Eight friends around a finished dinner table, each holding a phone calculator, all talking at once and pointing at different items on a single shared bill. One person has a pen and is drawing a diagram on the receipt. At 6 seconds someone puts a twenty-euro note down and everyone stops to look at it. Final 2 seconds: the waiter stands beside the table, terminal in hand, waiting with infinite patience. Audio: overlapping animated French chatter, phone keypad taps, a pen on paper, a banknote laid on wood, then a sudden collective silence. No music."
 },
 {
  "id": "EP082",
  "n": 82,
  "t": "Le centime",
  "mod": "Comptabilité",
  "ch": "Devis",
  "drive": "1KlXihMLILGDrlxDuO2d3VCe1ic-kCAw_",
  "hook": "Il manque un centime.",
  "punch": "Le Z calcule l'écart. Toi, tu rentres chez toi.",
  "heygen": "Un devis pour un groupe se crée en deux minutes et se transforme en commande quand il est accepté.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic, night, closed restaurant, single overhead lamp, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. Two in the morning. A manager recounts a small pile of coins for what is clearly the fifth time, lips moving. He checks the till, lifts the drawer insert, looks underneath, shakes it. At 6 seconds he finds nothing and writes a figure on a pad. Final 2 seconds: he stares at the pad, then holds up a single one-cent coin between two fingers, defeated by it. Audio: empty restaurant reverb, coins being counted, a drawer insert lifted and dropped, a chair creak, one long breath, a single coin set on wood. No music."
 },
 {
  "id": "EP083",
  "n": 83,
  "t": "Le cri dans le vide",
  "mod": "Comptabilité",
  "ch": "Impayés",
  "drive": "1KlXihMLILGDrlxDuO2d3VCe1ic-kCAw_",
  "hook": "J'AI DIT DEUX BURGERS !",
  "punch": "Chaque poste voit ses plats. Sans crier.",
  "heygen": "Tu vois ce qui est facturé, encaissé, et ce qui traîne. Les relances arrêtent d'être un jeu de mémoire.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic, busy professional kitchen, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A head chef at the pass shouts an order across the kitchen. Nobody reacts — the extraction hood is roaring, a mixer is running, two cooks have their backs turned. He shouts again, louder, cupping his hands. Still nothing. At 6 seconds he simply walks the plate over himself. Final 2 seconds: the moment he leaves the pass, three cooks all turn around at once and look at the empty spot where he was. Audio: overwhelming kitchen noise, extractor roar, a mixer, two muffled shouted orders swallowed by the noise, footsteps, then the noise continuing. No music."
 },
 {
  "id": "EP084",
  "n": 84,
  "t": "Le QR code scotché",
  "mod": "Comptabilité",
  "ch": "Dépenses",
  "drive": "1KlXihMLILGDrlxDuO2d3VCe1ic-kCAw_",
  "hook": "Commander à table.",
  "punch": "Un plan de salle, un QR par table. Ça marche.",
  "heygen": "Tu photographies la facture fournisseur, elle rentre dans tes dépenses avec ses lignes et son montant.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic, restaurant table close-up, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A customer holds a phone over a QR code taped to a restaurant table. The code is torn across one corner and covered in three overlapping layers of yellowed sticky tape. He moves the phone closer, then further, then tilts it, then tilts the whole table slightly. At 6 seconds he gives up and looks around for a waiter. Final 2 seconds: the phone camera finally focuses — on a reflection of the ceiling light. Audio: restaurant ambience, a phone scan failure buzz repeated three times, tape crinkling, a table leg scraping, an impatient tap on the screen. No music."
 },
 {
  "id": "EP085",
  "n": 85,
  "t": "Le ballon qui se dégonfle",
  "mod": "Comptabilité",
  "ch": "Synthèse",
  "drive": "1KlXihMLILGDrlxDuO2d3VCe1ic-kCAw_",
  "hook": "Table de 8. 20 h 30. Personne.",
  "punch": "No-show marqué, table libérée, soirée sauvée.",
  "heygen": "Chiffre d'affaires, dépenses, impayés, marge : la synthèse du mois tient sur un écran.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic, restaurant interior, warm evening light, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A table set for eight, immaculate, with a small \"Réservé\" card and a helium balloon tied to a chair. Nobody is there. The camera holds, then pushes in very slowly. At 6 seconds the balloon, losing helium, sinks gently until it rests on the tablecloth. Final 2 seconds: a waiter enters frame at the far side of the room, looks at the table, and turns off one of the lights above it. Audio: quiet restaurant ambience, distant chatter from other tables, a faint balloon string rubbing on fabric, a light switch click, then quiet. No music."
 },
 {
  "id": "EP086",
  "n": 86,
  "t": "Le téléphone que personne ne prend",
  "mod": "Comptabilité",
  "ch": "Export comptable",
  "drive": "1KlXihMLILGDrlxDuO2d3VCe1ic-kCAw_",
  "hook": "Trois appels manqués pendant le coup de feu.",
  "punch": "Caroline décroche. Et elle prend la réservation.",
  "heygen": "Tu envoies à ton comptable un export propre. Le dimanche soir redevient un dimanche soir.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic, kitchen and pass during full service, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A wall phone rings in a restaurant at peak service. One by one, every person in frame looks at it and then looks away: a cook with both hands in a pan, a waiter with a full tray, a dishwasher with wet arms up to the elbows. At 6 seconds the ringing stops on its own. Final 2 seconds: everyone relaxes visibly — and it starts ringing again. Audio: busy service noise, an insistent landline ring cutting through it, sizzling, plates, the ring stopping, one collective exhale, then the ring restarting. No music."
 },
 {
  "id": "EP087",
  "n": 87,
  "t": "Les trois tablettes",
  "mod": "Mon Site",
  "ch": "Éditeur",
  "drive": "1ykcHl2BaY22WlCsBA3DuwXaEMvQZUtMF",
  "hook": "Trois plateformes. Trois écrans.",
  "punch": "Une seule cuisine. Un seul flux.",
  "heygen": "Tu actives l'éditeur, tu choisis ton template, ton site est en ligne le jour même, aux couleurs de ta maison.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic, takeaway counter, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. Three different delivery-platform tablets sit propped side by side on a counter. They all start chiming at once, each with a different tone, each screen flashing a different colour. A single employee reaches for all three at the same time with two hands. At 6 seconds a fourth device — a phone — starts ringing beside them. Final 2 seconds: he stands with one tablet in each hand and the third one held against his chest with his chin. Audio: three distinct order-notification chimes overlapping and repeating, a phone ringtone joining, plastic tablets clacking, one desperate inhale. No music."
 },
 {
  "id": "EP088",
  "n": 88,
  "t": "Une étoile",
  "mod": "Mon Site",
  "ch": "Pages",
  "drive": "1ykcHl2BaY22WlCsBA3DuwXaEMvQZUtMF",
  "hook": "Un avis. Publié il y a six jours.",
  "punch": "Vu, répondu, traité. Le jour même.",
  "heygen": "Tu ajoutes tes pages : carte, avis, allergènes, recrutement. Elles se publient quand tu le décides.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic, tight portrait, restaurant back office, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. Close-up on a restaurant owner's face lit by his phone screen, smiling as he scrolls. The smile holds, then falters, then collapses entirely into a flat stare. He scrolls back up and reads the same thing again. At 6 seconds he lowers the phone slowly to the desk, screen down. Final 2 seconds: he picks it up and reads it a third time. Audio: quiet office, a finger swiping glass, a small amused hum that stops abruptly, a long silence, a phone set face-down on wood, then picked up again. No music."
 },
 {
  "id": "EP089",
  "n": 89,
  "t": "Le bocal presque vide",
  "mod": "Mon Site",
  "ch": "Domaine",
  "drive": "1ykcHl2BaY22WlCsBA3DuwXaEMvQZUtMF",
  "hook": "Ton jeu concours.",
  "punch": "QR code, roue cadeaux, gagnants tracés.",
  "heygen": "Tu branches ton nom de domaine. Tes clients arrivent chez toi, pas sur une plateforme.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic, restaurant entrance counter, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A large glass jar sits on a counter beside a handwritten sign, intended for a prize draw. Inside there is exactly one folded slip of paper. The camera pushes in slowly on the single slip. At 6 seconds a hand reaches in, takes the slip out, unfolds it, and reads it. Final 2 seconds: the same hand refolds it and puts it back in the empty jar. Audio: entrance ambience, a door opening in the background, glass resonance as a hand reaches in, paper unfolding, a beat of silence, paper dropped back into glass. No music."
 },
 {
  "id": "EP090",
  "n": 90,
  "t": "Le marc de café",
  "mod": "Mon Site",
  "ch": "Leads du site",
  "drive": "1ykcHl2BaY22WlCsBA3DuwXaEMvQZUtMF",
  "hook": "Ta prévision pour samedi.",
  "punch": "PrediBot lit tes données. Pas ton café.",
  "heygen": "Chaque demande de privatisation ou de contact devient un lead dans ton fichier client.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic, dim restaurant office, single warm lamp, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A restaurant manager sits alone at a desk, tilting an empty espresso cup and studying the coffee grounds inside with intense concentration, as if reading a forecast. He rotates the cup slowly, tilts his head, then nods once at something only he can see. At 6 seconds he writes a single number on a sheet of paper and underlines it twice. Final 2 seconds: he looks up at the camera with total conviction. Audio: quiet office, a clock ticking, ceramic rotating on a wooden desk, a pen underlining twice, one confident \"Voilà.\" No music."
 },
 {
  "id": "EP091",
  "n": 91,
  "t": "Le pétard dans le tiramisu",
  "mod": "Réservation",
  "ch": "2 - Ajouter une réservation",
  "drive": "1m6WdjC_iNYWO_4U3LmDuOsc-_Y_DrZLu",
  "hook": "Anniversaire de table 12.",
  "punch": "Les surprises, c'est bien. Les imprévus, non.",
  "heygen": "L'anniversaire est noté à la réservation, avec le nombre de couverts et la demande spéciale. La cuisine et la salle le savent avant que le client arrive.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic, cinematic handheld camera, shallow depth of field, warm restaurant lighting, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A waiter carries a birthday tiramisu with a single sparkler candle across a dining room toward a table of guests already clapping. At 5 seconds the sparkler erupts into a full firework fountain, throwing bright sparks up to the ceiling; the guests recoil backwards in unison, one man's paper party hat tilts over his eyes. Final 2 seconds: the waiter stands perfectly still, dessert held level, face completely neutral, sparks still falling around him. Audio: restaurant ambience, scattered applause and a few voices humming happy birthday, a sudden loud fizzing roar of the firework, chairs scraping back, a surprised collective \"Oh !\", then only fizzing. No music."
 },
 {
  "id": "EP092",
  "n": 92,
  "t": "Le super-héros qui a réservé",
  "mod": "Réservation",
  "ch": "3 - Gérer et no-shows",
  "drive": "1m6WdjC_iNYWO_4U3LmDuOsc-_Y_DrZLu",
  "hook": "Lui, il avait réservé.",
  "punch": "Ses quatre-vingts fans, non.",
  "heygen": "Quatre-vingts personnes d'un coup, ça se voit venir. Tu ouvres ou tu fermes tes créneaux en direct, et la liste d'attente prend le relais.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic, cinematic handheld camera, sunny terrace, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. IMPORTANT: an entirely generic, invented masked superhero — plain matte green and silver bodysuit, simple blank eye-mask, no emblem, no cape logo, no resemblance to any existing character. He arrives politely at the host stand of a busy restaurant terrace and points at a reservation notebook. At 5 seconds a crowd of thirty excited fans floods in behind him from off-frame, phones raised, filling the entire terrace within two seconds; a single young waiter is swallowed by the crowd, one arm holding a tray above his head like a periscope. Final 2 seconds: the superhero sits alone at a small table in the middle of the chaos, hands folded, waiting patiently. Audio: terrace ambience, a sudden roar of running footsteps and excited shouting, camera shutters, a tray wobbling, a lone waiter's voice saying \"Attendez—\", then the crowd noise settling into a hum. No music."
 },
 {
  "id": "EP093",
  "n": 93,
  "t": "Le chef part à la pêche",
  "mod": "StockVision",
  "ch": "3 - Prédictions des commandes",
  "drive": "1Ib_pKyJ8_jaFAwtIhkzhtmUU_DCtGSSY",
  "hook": "Rupture de stock, 20 h 15.",
  "punch": "Anticiper, c'est moins sportif.",
  "heygen": "FoodEatUp prévoit tes ventes de poisson à partir de ton historique. Tu commandes la bonne quantité le mardi, pas la canne à pêche le samedi.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic, cinematic, professional kitchen then window, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A chef opens the fish fridge: it is completely empty except for one sad lemon. He looks at a ticket in his hand, then at the empty fridge, then at the open kitchen window. At 5 seconds he is leaning out of that window in full chef whites and toque, casting a fishing rod into an ornamental carp pond in the courtyard, elbow resting on the sill. Final 2 seconds: the line goes taut, he braces, expression suddenly hopeful and completely serious. Audio: fridge fan hum, a paper ticket rustle, a long resigned exhale, a window latch, the whir of a fishing reel casting, a plop in water, then birdsong and a single reel click. No music."
 },
 {
  "id": "EP094",
  "n": 94,
  "t": "Le robot livreur qui double le scooter",
  "mod": "HubRise",
  "ch": "4 - Centraliser les commandes",
  "drive": "19D09dNt_jZSKpcwVCU8Mn1OkMLkY_ojd",
  "hook": "2026, la livraison change de main.",
  "punch": "Autant que tes commandes arrivent au bon endroit.",
  "heygen": "Peu importe qui livre. Tes commandes arrivent dans la même file, avec la bonne adresse et le bon statut, jusqu'à la remise au client.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic, low-angle street tracking shot, late afternoon light, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A delivery rider on a scooter with an insulated backpack is stuck in slow traffic on a French city street, foot down, visor up, sighing. At 5 seconds a small autonomous six-wheeled delivery robot the size of a suitcase glides smoothly past him in the bike lane, indicator light blinking politely. Final 2 seconds: the rider watches it disappear ahead; the robot stops at a pedestrian crossing and waits, perfectly law-abiding, while he is still stuck. Audio: idling engines, car horns, a resigned human sigh through a helmet, a quiet electric motor whirr and a soft robotic indicator beep, then traffic ambience. No music."
 },
 {
  "id": "EP095",
  "n": 95,
  "t": "L'éclipse de 13 h 12",
  "mod": "KDS",
  "ch": "3 - Gérer le KDS en direct",
  "drive": "1wQAkcP9pY90DLu_sE8GLiI6WYHZuYwq9",
  "hook": "Le service s'est arrêté deux minutes.",
  "punch": "Le reste du temps, il ne devrait jamais s'arrêter.",
  "heygen": "Sur le KDS, chaque plat a son chrono. Tu vois ce qui traîne au moment où ça traîne, et tu relances le bon poste.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic, wide then slow push-in, bright midday exterior with unusual dimming light, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A packed restaurant terrace at lunch. Every single guest at every table suddenly stops eating, puts on cardboard eclipse glasses and tilts their head straight up in unison, forks frozen mid-air. The light dims to an eerie silver. At 5 seconds a waiter arrives with three hot plates and stands in the middle of the terrace, holding them, looking at forty upturned faces, then up at the sky himself. Final 2 seconds: he lowers the plates onto an empty table, sits down on a spare chair and looks up too. Audio: terrace chatter falling to complete silence, cutlery set down, cardboard glasses rustling, birds going quiet, one child's \"waouh\", plates clinking softly on a table. No music."
 },
 {
  "id": "EP096",
  "n": 96,
  "t": "Canicule : le beurre fugueur",
  "mod": "HACCP",
  "ch": "relevé de température",
  "drive": "10rqzHFjXbjkGi73uJyjt3XQM92eaIMK_",
  "hook": "39° en cuisine.",
  "punch": "Une alerte température, et tu sauves la marchandise.",
  "heygen": "Trente-neuf degrés en cuisine, ton frigo souffre. Le relevé hors seuil te prévient tout de suite. Tu sauves la marchandise.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic macro then medium, harsh summer light through a kitchen window, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. Close macro on a large block of butter sitting on a stainless pass, a small fan oscillating uselessly beside it. The butter is visibly slumping, then sliding, leaving a glossy trail across the metal. At 5 seconds it slides right off the edge and lands with a wet slap on the tiles; the camera widens to reveal a cook standing in the heat with a wet cloth on his neck, watching it happen without moving. Final 2 seconds: he looks at the fan, then at the camera, sweat on his forehead, completely defeated. Audio: fan motor droning, distant cicadas, a fridge compressor struggling, a slow greasy slide on metal, a wet slap, one long exhale. No music."
 },
 {
  "id": "EP097",
  "n": 97,
  "t": "Le mur de tablettes",
  "mod": "HubRise",
  "ch": "2 - Relier Uber Eats et Deliveroo",
  "drive": "19D09dNt_jZSKpcwVCU8Mn1OkMLkY_ojd",
  "hook": "Six plateformes. Six alertes.",
  "punch": "Une seule commande, un seul écran.",
  "heygen": "Tes plateformes envoient tout dans FoodEatUp. Six alertes deviennent une file de commandes. La tablette murale, tu peux la ranger.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic, static wide then slow push-in, busy kitchen pass, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. Six different tablets and order terminals are mounted side by side on a shelf above a restaurant pass, each with a different generic interface colour, no readable text, no brand. They start chiming one after another, then all together, faster and faster. A manager stands in front of them holding a spatula, and at 5 seconds begins conducting them like an orchestra, sweeping the spatula in time with the chimes, deadly serious. Final 2 seconds: he stops conducting; every screen falls silent at once; he lowers the spatula slowly. Audio: kitchen ambience, six distinct notification chimes overlapping into a chaotic rhythm, escalating, then an abrupt collective silence and a single drip from a tap. No music."
 },
 {
  "id": "EP098",
  "n": 98,
  "t": "Le robot serveur qui bugge et danse",
  "mod": "Service",
  "ch": "1 - Commandes multi-canaux",
  "drive": "1z4li_rdzH8yC7VFoWgOa4yMHbbKIAG29",
  "hook": "Ton nouveau serveur, en période d'essai.",
  "punch": "L'IA, c'est utile quand elle sert à quelque chose.",
  "heygen": "L'intelligence utile, c'est celle qui range tes commandes, pas celle qui danse. Ici, chaque canal alimente le même service.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic, medium tracking shot in a modern dining room, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A wheeled humanoid service robot with a tray of drinks rolls smoothly between tables, guests watching, impressed. At 5 seconds it hits a small rug edge, freezes, its head twitches, and it begins performing a jerky, off-beat dance routine with the tray still perfectly level, glasses untouched. Final 2 seconds: it stops mid-pose, one arm up, and its status light turns from blue to red while a waiter walks calmly into frame and takes the tray off it. Audio: restaurant ambience, a smooth servo whirr, a sharp electronic glitch stutter, rhythmic servo clicking like a broken beat, guests laughing, a soft error chime, glass clinking as the tray is lifted. No music."
 },
 {
  "id": "EP099",
  "n": 99,
  "t": "Le répondeur préhistorique",
  "mod": "Caroline",
  "ch": "1 - Configurer voix et prompts",
  "drive": "1SV1XsT61_cDqoRzD8JxehtRoOpyH5LaA",
  "hook": "Quarante appels pendant le rush.",
  "punch": "Quelqu'un devrait répondre. Ce ne sera pas toi.",
  "heygen": "Caroline répond au téléphone pendant ton rush. Elle prend la réservation, la note, et te la remonte. Aucun appel ne tombe dans le vide.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic, tight macro on a cluttered back-office desk, warm lamp light, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A 1990s cassette answering machine sits on a restaurant back-office desk next to a corded phone, its red light blinking furiously. The phone rings; the machine clicks and starts recording. At 5 seconds the little cassette door bursts open and a huge tangle of magnetic tape spills out and keeps unspooling across the desk and onto the floor, while the phone keeps ringing. Final 2 seconds: a hand enters frame, gently closes the office door on the whole mess, leaving the tape still unspooling. Audio: an old phone ringing, a plastic click and cassette whirr, muffled voices leaving messages layered on top of each other, tape unspooling with a papery hiss, a door closing softly, ringing continuing behind it. No music."
 },
 {
  "id": "EP100",
  "n": 100,
  "t": "L'influenceur au ring light",
  "mod": "Marketing",
  "ch": "1 - Débloquer les avis",
  "drive": "1hBc6Axd0DE2ocTiXXKGlmj1dyagOwKFg",
  "hook": "Il a mis vingt minutes à filmer.",
  "punch": "Et deux minutes à te mettre deux étoiles.",
  "heygen": "Tes avis remontent au même endroit, site et Google. Tu réponds à celui qui t'a mis deux étoiles avant qu'il devienne ta vitrine.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic, over-the-shoulder then reverse, restaurant table, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A young man has set up a ring light, a tripod and a small reflector around a single plate of pasta on a restaurant table, and is filming it from twelve different angles, moving the plate, adjusting a basil leaf with tweezers. Steam stops rising from the dish. At 5 seconds he finally takes one bite — and grimaces, because it is stone cold. Final 2 seconds: he pushes the plate away and starts typing on his phone with one finger, expression sour, ring light still glowing on his face. Audio: restaurant ambience, tripod clicks, a phone shutter repeating, a chair adjusting, a small disappointed \"mmh\", then rapid soft phone typing. No music."
 },
 {
  "id": "EP101",
  "n": 101,
  "t": "POV : thriller comptable",
  "mod": "Caisse POS",
  "ch": "6 - Clôturer sa caisse",
  "drive": "1nHjH82ig0i-MtQqDmYp131htOSThaPIQ",
  "hook": "Rapprochement des caisses. Vendredi soir.",
  "punch": "Ça devrait être une ligne, pas une enquête.",
  "heygen": "La clôture, c'est un bouton. Le détail par moyen de paiement, la TVA, l'écart : tout est là, sans calculatrice ni suspense.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic, extreme close-ups with dramatic thriller lighting and slow dolly moves, night back office, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. Shot like a psychological thriller: an extreme close-up of a trembling hand pushing a stack of paper invoices; a macro of a calculator key being pressed with enormous tension; a slow tilt up a restaurant owner's face lit from below by a laptop screen, jaw clenched, a bead of sweat. At 5 seconds he presses the equals key, stares at the result, and his shoulders drop three centimetres. Final 2 seconds: he closes the laptop very slowly and sits in the dark, perfectly still. Audio: deep ominous room tone, a clock ticking, paper sliding, one loud calculator click, a heartbeat rising then stopping dead, a laptop lid closing, silence. No music beyond the tension drone."
 },
 {
  "id": "EP102",
  "n": 102,
  "t": "L'inspecteur surprise",
  "mod": "HACCP",
  "ch": "checklists hygiène",
  "drive": "10rqzHFjXbjkGi73uJyjt3XQM92eaIMK_",
  "hook": "Contrôle surprise. Ou pas.",
  "punch": "Le jour où c'est le vrai, tu ne bouges pas.",
  "heygen": "Ta checklist est validée chaque jour par ton équipe. Le jour du vrai contrôle, tu ouvres l'historique et tu ne bouges pas.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic, fast handheld, professional kitchen, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A person in a plain grey jacket carrying a clipboard walks slowly toward a kitchen's swinging door from the dining room. Cut inside: the entire brigade explodes into hyper-speed motion — containers stacked, a floor mopped, a thermometer plunged into a fridge, a hairnet yanked on, all in three seconds of frantic activity, then everyone freezes in perfect professional poses. At 5 seconds the door opens: it is only a delivery driver asking for a signature. Final 2 seconds: the entire brigade stays frozen in their poses, mop in the air, staring at him. Audio: calm dining room ambience, then an explosion of clattering, running footsteps, fridge doors, a mop slapping tiles, an abrupt total silence, a door creak, a casual \"Bonjour, signature ?\". No music."
 },
 {
  "id": "EP103",
  "n": 103,
  "t": "Le car de 40 sans réservation",
  "mod": "Réservation",
  "ch": "1 - Réservations du jour",
  "drive": "1m6WdjC_iNYWO_4U3LmDuOsc-_Y_DrZLu",
  "hook": "Quarante couverts. Sans prévenir.",
  "punch": "Prévenu, tu aurais dit oui.",
  "heygen": "Un groupe qui arrive, tu vérifies la disponibilité réelle en trois secondes : tables libres, horaires, capacité. Tu dis oui en connaissance de cause.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic, wide exterior then interior reverse, small village restaurant, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A quiet restaurant with two occupied tables. Through the window, a large coach pulls up and stops with a hiss. At 5 seconds its doors open and forty tourists in matching caps stream out and walk in single file toward the entrance, one of them waving cheerfully. Final 2 seconds: interior shot of a lone waiter behind the bar, holding a single menu, watching the line come through the door, not moving a muscle. Audio: quiet restaurant ambience, a coach air-brake hiss, doors opening, a rising tide of cheerful chatter and footsteps, a bell above the door ringing repeatedly, then one very small \"bonjour\". No music."
 },
 {
  "id": "EP104",
  "n": 104,
  "t": "Le no-show western",
  "mod": "Réservation",
  "ch": "3 - Gérer et no-shows",
  "drive": "1m6WdjC_iNYWO_4U3LmDuOsc-_Y_DrZLu",
  "hook": "Table de huit. 20 h 30.",
  "punch": "Un no-show, ça se prévient.",
  "heygen": "Tu marques le no-show, la table se libère immédiatement et repart à la vente. Le client, lui, garde son historique.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic, wide static shot, elegant empty dining room, evening light, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A long table beautifully set for eight — folded napkins, polished glasses, a flower arrangement — completely empty in a silent restaurant. The camera holds. At 5 seconds a dry tumbleweed rolls slowly across the floor in front of the table, from one side of the frame to the other, as if in a western. Final 2 seconds: it comes to rest against a chair leg; a single candle flickers. Audio: deep empty-room reverb, a clock ticking, a faint whistling wind that should not exist indoors, dry rustling as the tumbleweed rolls, then a candle-flame flicker. No music."
 },
 {
  "id": "EP105",
  "n": 105,
  "t": "Le duel de la dernière table",
  "mod": "Mon Site",
  "ch": "6 - Réservations et horaires",
  "drive": "1ykcHl2BaY22WlCsBA3DuwXaEMvQZUtMF",
  "hook": "Dernière table du samedi.",
  "punch": "Le plus rapide gagne. Rends-la réservable en ligne.",
  "heygen": "Tes créneaux sont réservables en ligne, en direct, avec tes vraies disponibilités. Le premier qui réserve a la table.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic, western-style low-angle close-ups, sunlit terrace, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. Shot like a spaghetti-western standoff: two couples face each other across a restaurant terrace, one single free table between them. Extreme close-ups of narrowed eyes, a hand hovering near a jacket pocket, a bead of sweat, a napkin fluttering like a tumbleweed. At 5 seconds both men draw — their phones — and stab at a booking screen with one thumb, faster and faster. Final 2 seconds: one of them raises his phone in triumph; the other lowers his head; the winner's partner is already sitting down. Audio: terrace ambience, wind, a single suspended note of tension, exaggerated boot-scrape and leather creak, two rapid phone taps, a soft confirmation chime, a chair scraping. No music beyond the tension note."
 },
 {
  "id": "EP106",
  "n": 106,
  "t": "L'addition en quatorze parts",
  "mod": "Caisse POS",
  "ch": "5 - Séparer une addition",
  "drive": "1nHjH82ig0i-MtQqDmYp131htOSThaPIQ",
  "hook": "On peut payer chacun ?",
  "punch": "Oui. En trois secondes, pas en trente minutes.",
  "heygen": "Quatorze parts, quatorze cartes : tu découpes l'addition depuis l'écran, chacun paie ce qu'il doit, le reste dû s'affiche en direct.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic, over-the-shoulder then reverse, long dinner table, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A waiter arrives at a long table of fourteen friends with the bill folder. Instantly fourteen hands shoot up holding fourteen bank cards, plus one person waving a handful of coins and another holding out a restaurant voucher. At 5 seconds the waiter is holding the card machine in one hand and a fan of fourteen cards in the other, like a poker hand, blinking. Final 2 seconds: he stares at the camera over the fan of cards, absolutely still, while a fifteenth hand enters frame with another card. Audio: cheerful table chatter, chairs, plastic cards tapping, coins jingling, a terminal beep, a rising confused murmur, then a single beep. No music."
 },
 {
  "id": "EP107",
  "n": 107,
  "t": "Le magicien de l'addition",
  "mod": "Caisse POS",
  "ch": "3 - Encaisser une commande",
  "drive": "1nHjH82ig0i-MtQqDmYp131htOSThaPIQ",
  "hook": "Tout le monde a un tour.",
  "punch": "Ta caisse, elle, ne perd jamais une addition.",
  "heygen": "L'addition est rattachée à la table dès la commande. Elle ne se perd pas, elle ne s'oublie pas, elle ne disparaît pas.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic, medium shot, warm bistro lighting, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A guest in a slightly theatrical velvet jacket receives the bill folder, smiles, and makes an elaborate flourish over it with both hands, a napkin draped across the top like a magician. At 5 seconds he whips the napkin away — the folder is completely empty, and a white dove flaps up out of it toward the ceiling. Final 2 seconds: the waiter, unimpressed, calmly places a second identical bill folder on the table and walks away. Audio: bistro ambience, a theatrical fabric whoosh, wing flapping, one impressed gasp from a neighbouring table, then a flat cardboard tap as the second folder lands. No music."
 },
 {
  "id": "EP108",
  "n": 108,
  "t": "Le poulpe du pass",
  "mod": "KDS",
  "ch": "2 - Vue KDS par poste",
  "drive": "1wQAkcP9pY90DLu_sE8GLiI6WYHZuYwq9",
  "hook": "Il te faudrait six bras.",
  "punch": "Ou un seul outil qui fait le reste.",
  "heygen": "Chaque poste voit ce qui le concerne, et seulement ça. Tu n'as pas besoin de six bras, tu as besoin de six écrans qui parlent entre eux.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic, medium shot at a stainless pass, moody kitchen lighting, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A large live octopus sits calmly on the stainless steel pass of a professional kitchen wearing a tiny white chef's toque. Each of its arms holds a different tool — tongs, a squeeze bottle, a whisk, a ticket, a plate, a spoon — and all of them are moving competently at once. At 5 seconds a human chef steps into frame beside it holding two tools, looks at the octopus, then at his own two hands. Final 2 seconds: he sets his tools down and leans on the pass, watching it work, defeated but admiring. Audio: kitchen extractor hum, sizzling, rapid metallic tool clicking layered on itself, a wet suction sound, a spoon set down slowly, one human sigh. No music."
 },
 {
  "id": "EP109",
  "n": 109,
  "t": "Le kombucha qui explose",
  "mod": "HACCP",
  "ch": "traçabilité",
  "drive": "10rqzHFjXbjkGi73uJyjt3XQM92eaIMK_",
  "hook": "Ta cave à ferments.",
  "punch": "Suivie et datée, elle ne t'explose pas à la figure.",
  "heygen": "Chaque production est datée, tracée, rattachée à son lot. Ce qui fermente en cave n'est plus une surprise.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic, macro then medium, shelf of fermentation jars in a cellar, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A shelf of large glass fermentation jars filled with cloudy kombucha and pickles, lids straining. Macro on one lid trembling and bulging. A cook leans in slowly to inspect it, nose close to the glass. At 5 seconds that jar erupts, blasting foam straight up onto the ceiling and across his face and apron. Final 2 seconds: he stands dripping, eyes closed, while on the shelf behind him a second lid starts trembling. Audio: cellar room tone, a gas hiss building inside glass, a wet explosive pop, splattering and dripping, a startled inhale, then a second faint hiss beginning. No music."
 },
 {
  "id": "EP110",
  "n": 110,
  "t": "Le menu 100 % matcha",
  "mod": "StockVision",
  "ch": "18 - Statistiques par module",
  "drive": "1Ib_pKyJ8_jaFAwtIhkzhtmUU_DCtGSSY",
  "hook": "Tu suis toutes les tendances.",
  "punch": "Regarde surtout lesquelles se vendent.",
  "heygen": "La tendance, tu la testes. Tu regardes ce que ce plat rapporte vraiment, et tu décides de le garder ou pas sur des chiffres.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic, top-down then eye-level, bright modern café, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A waiter places a plate in front of a guest: everything on it is vivid green — green latte, green bread, green sauce, a green steak, a green boiled egg. The guest looks at it, looks up at the waiter, looks back down. At 5 seconds he lifts a forkful, sniffs it, and eats it anyway. Final 2 seconds: he gives a small, genuinely surprised nod of approval, and the waiter immediately places a second identical green plate beside the first. Audio: café ambience, an espresso machine, ceramic on wood, a fork clink, a thoughtful chewing pause, a small \"hm !\", then another plate landing. No music."
 },
 {
  "id": "EP111",
  "n": 111,
  "t": "L'imprimante 3D qui déraille",
  "mod": "StockVision",
  "ch": "12 - Valider une production",
  "drive": "1Ib_pKyJ8_jaFAwtIhkzhtmUU_DCtGSSY",
  "hook": "La cuisine du futur.",
  "punch": "Le futur utile, c'est celui qui te fait gagner du temps.",
  "heygen": "La production planifiée sort ses ingrédients du stock, sa quantité est validée, sa traçabilité écrite. Le gain de temps est là, pas dans le gadget.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic macro, clean modern kitchen laboratory, cool light, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A food 3D printer extrudes a neat layer of purée onto a plate with clinical precision, watched by a chef with folded arms. At 5 seconds the nozzle begins moving erratically, extruding an ever-growing chaotic spaghetti tangle that rises off the plate and spills onto the counter, still perfectly smooth and glossy. Final 2 seconds: the chef reaches out and, with total calm, presses a single button; the machine stops, leaving a large edible sculpture of nothing at all. Audio: quiet lab hum, a precise servo whirr, a soft wet extrusion sound, the servo tempo becoming erratic, a rising mechanical whine, a button click, silence. No music."
 },
 {
  "id": "EP112",
  "n": 112,
  "t": "Le casque de réalité augmentée",
  "mod": "Mon Site",
  "ch": "2 - Choisir ton template",
  "drive": "1ykcHl2BaY22WlCsBA3DuwXaEMvQZUtMF",
  "hook": "La carte du futur.",
  "punch": "Ou juste une carte en ligne qui marche.",
  "heygen": "Ta carte en ligne, propre, à jour, consultable par QR à table. Pas de casque, pas d'appli à installer.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic, medium shot, elegant restaurant, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A guest wearing a sleek generic augmented-reality headset (no brand, no logo) sits at a beautifully set table, reaching out with a fork toward something only he can see. His fork repeatedly stabs the tablecloth thirty centimetres to the left of his actual plate. At 5 seconds he brings the empty fork to his mouth with great satisfaction and chews on nothing. Final 2 seconds: a waiter quietly slides the real plate under his hovering fork; the guest's next stab hits food and he freezes, delighted. Audio: refined restaurant ambience, cutlery clicking on cloth and wood, a faint headset electronic hum, contented chewing, a plate sliding on linen, a soft \"ah !\". No music."
 },
 {
  "id": "EP113",
  "n": 113,
  "t": "Le drone qui se trompe de balcon",
  "mod": "HubRise",
  "ch": "4 - Centraliser les commandes",
  "drive": "19D09dNt_jZSKpcwVCU8Mn1OkMLkY_ojd",
  "hook": "Livraison réussie. Presque.",
  "punch": "Un suivi de commande, et personne ne mange ta pizza.",
  "heygen": "Le suivi de commande affiche l'état en direct, de la prise à la remise. Tu sais toujours où est la commande et chez qui.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic, exterior apartment building facade, late afternoon, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A delivery drone carrying a pizza box in a harness descends along an apartment building facade. On the third floor a customer waits on his balcony with both arms raised, ready. At 5 seconds the drone drifts two metres sideways and gently lowers the box onto the neighbour's balcony instead, where an elderly woman is watering her plants. Final 2 seconds: she picks up the box, opens it, looks at the pizza, then across at the customer, and nods once — she is keeping it. Audio: city ambience, rotor buzz rising and falling, a harness servo, a cardboard box settling, a watering can being set down, a very short delighted \"oh !\", the customer's distant \"hé !\". No music."
 },
 {
  "id": "EP114",
  "n": 114,
  "t": "La choré pendant que ça brûle",
  "mod": "Marketing",
  "ch": "5 - Lancer une campagne",
  "drive": "1hBc6Axd0DE2ocTiXXKGlmj1dyagOwKFg",
  "hook": "Ton community manager, c'est ta brigade.",
  "punch": "Poste. Mais garde un œil sur le service.",
  "heygen": "Ce que ton équipe filme, tu peux l'exploiter : campagne, segment, envoi, résultats. Publier, oui — mesurer, encore mieux.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic, static phone-style frontal shot, professional kitchen, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. Four young kitchen staff line up shoulder to shoulder in front of a phone on a tripod and perform a tight, synchronised dance routine, grinning, fully committed. Behind them, out of focus, a pan on the stove starts smoking, then flames rise gently. At 5 seconds one of them notices in the reflection of a stainless surface but keeps dancing, eyes wide. Final 2 seconds: the routine ends on a pose; all four turn around at once and stare at the burning pan, still in formation. Audio: kitchen ambience, four pairs of shoes on tiles in rhythm, laughing and counting \"cinq, six, sept, huit\", a growing crackle and a smoke alarm starting to chirp, then silence on the freeze. No music track — rhythm carried by claps and footsteps."
 },
 {
  "id": "EP115",
  "n": 115,
  "t": "Les poules du potager du toit",
  "mod": "StockVision",
  "ch": "16 - Mouvements de stock",
  "drive": "1Ib_pKyJ8_jaFAwtIhkzhtmUU_DCtGSSY",
  "hook": "Circuit court, très court.",
  "punch": "Compte ce qui rentre. Et ce qui sort.",
  "heygen": "Ce qui rentre, ce qui sort, ce qui se perd. Circuit court ou pas, la quantité doit être comptée.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic, rooftop garden with city skyline, golden hour, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A neat rooftop restaurant vegetable garden with labelled wooden crates of herbs and salad. A chef crouches, harvesting basil into a basket, proud. At 5 seconds a dozen chickens burst out from behind the crates and swarm the beds, scattering leaves and soil, one of them landing directly in his basket. Final 2 seconds: he stands up holding the basket with the chicken sitting comfortably inside it, looking at the camera; the beds behind him are bare. Audio: rooftop wind and distant city traffic, gentle clipping of herbs, a sudden explosion of clucking and flapping, soil scattering, then steady contented clucking. No music."
 },
 {
  "id": "EP116",
  "n": 116,
  "t": "Le stagiaire et le mur de craie",
  "mod": "KDS",
  "ch": "1 - Créer tes postes KDS",
  "drive": "1wQAkcP9pY90DLu_sE8GLiI6WYHZuYwq9",
  "hook": "Ton système de commandes.",
  "punch": "Il tient sur un mur. Il tiendrait sur un écran.",
  "heygen": "Tes commandes tiennent sur un écran, pas sur un mur. Chaque poste voit les siennes, dans l'ordre, avec son temps.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic, wide shot of a kitchen wall, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A young intern writes orders in chalk directly onto a huge black kitchen wall — abstract marks, tally strokes and arrows only, absolutely no readable words or letters. The wall is already almost entirely covered. He climbs onto a milk crate to reach higher, then onto a chair on top of the crate. At 5 seconds he reaches the ceiling, still writing, chalk dust falling on his shoulders. Final 2 seconds: he looks down at the chef below him, who silently holds up a tablet-sized rectangle of blank white board. Audio: kitchen ambience, chalk squeaking on a wall, a crate scraping, wood creaking under weight, chalk dust settling, one calm cough from below. No music."
 },
 {
  "id": "EP117",
  "n": 117,
  "t": "Le plat étoilé en dix minutes",
  "mod": "StockVision",
  "ch": "1 - Ma carte, fiche recette",
  "drive": "1Ib_pKyJ8_jaFAwtIhkzhtmUU_DCtGSSY",
  "hook": "Le défi à dix minutes.",
  "punch": "Une fiche technique, et c'est dix minutes tous les jours.",
  "heygen": "La fiche technique fixe les quantités, les étapes et le coût. Le plat sort en dix minutes, tous les jours, par n'importe qui de ta brigade.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic, fast handheld with quick whip-pans, professional kitchen, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A large kitchen timer is slammed onto the counter and a chef explodes into action: pans flying, sauce whisked, tweezers placing garnish, a blowtorch flaring, all in rapid succession, sweat flying. At 5 seconds the timer rings; he slides a stunning, immaculate gourmet plate into frame with both hands. Final 2 seconds: the camera pulls back to reveal the entire kitchen behind him utterly destroyed — every pan used, flour everywhere, a cupboard door hanging open — while he holds the perfect plate. Audio: a mechanical timer ticking loudly, frantic metallic clattering, a blowtorch hiss, plates scraping, an alarm bell ringing, then heavy breathing and one distant pan falling. No music."
 },
 {
  "id": "EP118",
  "n": 118,
  "t": "La file du brunch",
  "mod": "Mon Site",
  "ch": "5 - Créer un site par IA",
  "drive": "1ykcHl2BaY22WlCsBA3DuwXaEMvQZUtMF",
  "hook": "Le brunch du dimanche.",
  "punch": "Ils feraient la queue chez toi aussi. Encore faut-il pouvoir réserver.",
  "heygen": "Ton site de réservation et de commande est prêt en un clic, depuis ta carte. La file d'attente devient un carnet plein.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic, street-level tracking shot along a queue, early morning light, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. The camera tracks slowly along a long pavement queue outside a closed restaurant at dawn. The people are absurdly over-equipped: folding chairs, thermos flasks, a blanket, one small camping tent, a man doing stretches, a woman reading a novel already half finished. At 5 seconds the camera reaches the front of the queue: a man in a sleeping bag is sitting directly against the locked door. Final 2 seconds: a hand inside flips a small sign on the glass; the entire queue stands up at once in a single wave. Audio: quiet dawn street, birds, a thermos unscrewing, a tent zip, pages turning, a sleeping bag rustling, a metallic door bolt, then a collective shuffle of forty people standing up. No music."
 },
 {
  "id": "EP119",
  "n": 119,
  "t": "La mascotte poulet et le vent",
  "mod": "Marketing",
  "ch": "9 - Ciblage et consentement",
  "drive": "1hBc6Axd0DE2ocTiXXKGlmj1dyagOwKFg",
  "hook": "Ta stratégie d'acquisition.",
  "punch": "Cinq cents tracts, zéro donnée.",
  "heygen": "Cinq cents tracts, zéro donnée. Ici, chaque client capté entre dans ton fichier, avec son consentement, et devient une campagne.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic, handheld street shot, windy grey daylight, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A person in an oversized generic chicken mascot costume (plain yellow, no brand, no logo) hands out flyers on a pavement outside a restaurant, dancing awkwardly. A strong gust hits: the flyers explode out of their wing in a white cloud and the costume's huge tail acts like a sail, dragging the mascot backwards down the pavement in small hops, arms flailing. At 5 seconds it collides softly with a lamppost and wraps around it. Final 2 seconds: the mascot clings to the lamppost, motionless, as the last flyers drift past its beak. Audio: strong wind gusts, paper flapping and scattering, foam costume squeaking, small running steps, a soft padded thud on metal, one muffled human groan from inside the head. No music."
 },
 {
  "id": "EP120",
  "n": 120,
  "t": "La réunion des dix logiciels",
  "mod": "PrediBot",
  "ch": "1 - Lire ses prévisions",
  "drive": "19kYZliyRnKraKVg1zdFrXCocD38VZ2a9",
  "hook": "Réunion de tes dix logiciels.",
  "punch": "Ils ne se parlent toujours pas. FoodEatUp, si.",
  "heygen": "Une base, un écran, une équipe. Ta caisse, ta cuisine, ton stock et ton marketing lisent les mêmes données. Ils finissent enfin par se parler.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic, slow dolly along a long table, empty dining room, dramatic evening light, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A restaurant owner sits at the head of a long dining table set for a formal meeting. In each of the ten guest chairs sits an open laptop or tablet instead of a person, each screen showing a different abstract coloured interface with no readable text. He looks around at them expectantly and opens his hands as if to say \"so?\". At 5 seconds every screen simultaneously plays a different notification chime and then goes to a blank screensaver, one after another, ignoring him completely. Final 2 seconds: he lowers his hands, alone at the head of a table of dark screens, and pours himself a glass of water. Audio: empty room reverb, a chair creak, ten mismatched notification chimes overlapping, fans spinning down one by one, water pouring into a glass, then silence. No music."
 },
 {
  "id": "EP121",
  "n": 121,
  "t": "Le modificateur infini",
  "mod": "Service",
  "ch": "3 - Envoi direct cuisine",
  "drive": "1z4li_rdzH8yC7VFoWgOa4yMHbbKIAG29",
  "hook": "Alors, sans oignon, mais…",
  "punch": "Une commande complexe, ça se saisit. Pas ça se subit.",
  "heygen": "Les modifications se saisissent sur la commande : sans oignon, cuisson, allergie. Elles partent en cuisine avec le plat, écrites noir sur blanc.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic, cinematic handheld camera, warm restaurant lighting, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A guest sits at a table talking continuously, one finger raised, listing endless modifications with total calm. Opposite him a waiter writes in a small notepad; he fills a page, flips it, fills another, flips again, then pulls a second notepad from his apron, then a third. At 5 seconds the guest pauses, holds up his index finger again and clearly starts a new sentence. Final 2 seconds: the waiter stops writing, looks straight into the camera with three open notepads fanned in his hand, expressionless. Audio: restaurant ambience, a calm continuous French voice listing things without pause, rapid pen scratching, pages flipping faster and faster, an apron rustle, then only the voice continuing. No music."
 },
 {
  "id": "EP122",
  "n": 122,
  "t": "« Comme d'habitude »",
  "mod": "Marketing",
  "ch": "20 - Vue client fidélité",
  "drive": "1hBc6Axd0DE2ocTiXXKGlmj1dyagOwKFg",
  "hook": "Il dit « comme d'habitude ».",
  "punch": "Ton fichier client saurait, lui.",
  "heygen": "La fiche client te dit qui il est, ce qu'il commande et quand il est venu la dernière fois. « Comme d'habitude » devient une information, pas un bluff.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic, medium two-shot at a bar counter, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A confident regular-looking man leans on the counter, taps it twice and gestures broadly as if to say \"the usual\". The owner behind the bar smiles warmly, nods — and behind the smile his eyes flick left, then right, in visible panic, because he has never seen this man in his life. At 5 seconds he seizes a random plate from the pass and sets it down with enormous confidence. Final 2 seconds: the customer looks at the plate, then up at him, deeply moved, and puts a hand on his heart. Audio: bar ambience, two knuckle taps on wood, a glass clinking, a slightly too-loud \"Mais bien sûr !\", a plate landing firmly, then a small emotional sniff. No music."
 },
 {
  "id": "EP123",
  "n": 123,
  "t": "Le végétarien du dessert",
  "mod": "StockVision",
  "ch": "1 - Ma carte, allergènes",
  "drive": "1Ib_pKyJ8_jaFAwtIhkzhtmUU_DCtGSSY",
  "hook": "Il annonce ça au dessert.",
  "punch": "Les régimes et les allergènes, ça se note à la réservation.",
  "heygen": "Les allergènes et les régimes sont portés par ta carte et par la réservation. L'info arrive en cuisine avant l'entrée, pas au dessert.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic, medium shot at a bistro table, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A guest finishes an enormous rare steak, scraping the plate clean, visibly delighted. The waiter arrives to clear it and offers the dessert menu. At 5 seconds the guest raises a polite hand and points to something on the menu while gesturing \"no\" over his own empty steak plate, explaining seriously that he is vegetarian. Final 2 seconds: the waiter looks down at the bare steak bone on the plate, then back at the guest, then at the camera. Audio: bistro ambience, cutlery on porcelain, a satisfied exhale, a plate being lifted, a calm explanatory French voice, then a single fork clink and silence. No music."
 },
 {
  "id": "EP124",
  "n": 124,
  "t": "La table qui ne part jamais",
  "mod": "Caisse POS",
  "ch": "6 - Clôturer sa caisse",
  "drive": "1nHjH82ig0i-MtQqDmYp131htOSThaPIQ",
  "hook": "Il est minuit dix.",
  "punch": "Le service a une fin. Ton logiciel devrait le savoir.",
  "heygen": "Le service a une fin : tu clôtures, tu comptes, tu archives. L'écran te dit quand la journée est vraiment finie.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic, wide static shot of a dining room at closing time, dim light, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. Every chair in the restaurant is upside down on its table, the floor is being mopped, one waiter counts the till, another stacks the last crates — except for one single table in the middle where two friends sit chatting animatedly, entirely unaware. At 5 seconds a vacuum cleaner is switched on and passes directly around their feet; they lift their legs without interrupting the conversation. Final 2 seconds: one of them turns and raises two fingers, ordering two more coffees. Audio: empty room reverb, chairs scraping onto tables, a mop, a till drawer, a vacuum roaring to life, two voices talking straight through it all, then a cheerful \"deux cafés !\". No music."
 },
 {
  "id": "EP125",
  "n": 125,
  "t": "Le client qui refait le plan de salle",
  "mod": "Caroline",
  "ch": "3 - Dessiner son plan de salle",
  "drive": "1SV1XsT61_cDqoRzD8JxehtRoOpyH5LaA",
  "hook": "Je serais mieux là, non ?",
  "punch": "Ton plan de salle, c'est toi qui le décides.",
  "heygen": "Ton plan de salle est le tien : zones, tables, capacités, blocages. Tu places, tu bloques, tu libères en un geste.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic, wide shot of a sunny terrace, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A guest arrives, tests a chair, shakes his head, and begins moving his table — a metre to the left, then out from under the awning, then further, dragging it steadily while a waiter follows behind him holding two menus and saying nothing. At 5 seconds the guest is dragging the table off the terrace and onto the pavement, past the planters. Final 2 seconds: the table now stands in the middle of the street; he sits down, perfectly content, and the waiter calmly places the menu in front of him as a bus indicator blinks behind. Audio: terrace ambience, metal table legs scraping on stone then asphalt, a chair being tested, the waiter's footsteps, distant traffic, a bus air-brake hiss, then a menu landing on metal. No music."
 },
 {
  "id": "EP126",
  "n": 126,
  "t": "Six fourchettes, une salade",
  "mod": "Caisse POS",
  "ch": "5 - Séparer une addition",
  "drive": "1nHjH82ig0i-MtQqDmYp131htOSThaPIQ",
  "hook": "On partage, c'est plus convivial.",
  "punch": "Partage l'assiette. Pas l'addition, elle se divise toute seule.",
  "heygen": "Tu partages l'addition par article ou par personne. Ce qui reste dû s'affiche en direct. Personne ne recompte à la main.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic, top-down then eye-level, restaurant table, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. Top-down shot of one single modest salad placed in the centre of a table set for six. A beat of stillness. At 5 seconds six forks strike the bowl simultaneously from six directions, colliding, retreating, striking again in a fencing flurry. Final 2 seconds: the bowl is empty and spotless; six hands rest politely on the table as if nothing happened. Audio: restaurant ambience, a plate set down, one second of total silence, then a rapid storm of metal-on-ceramic clattering like a swordfight, a last scrape, then calm chatter resuming. No music."
 },
 {
  "id": "EP127",
  "n": 127,
  "t": "Réveillon, 23 h 58",
  "mod": "Réservation",
  "ch": "1 - Réservations du jour",
  "drive": "1m6WdjC_iNYWO_4U3LmDuOsc-_Y_DrZLu",
  "hook": "Bonne année à tout le monde.",
  "punch": "Sauf à celui qui gère les deux cents couverts.",
  "heygen": "Deux cents couverts un 31 décembre, ça se pilote : arrivées échelonnées, tables assignées, cuisine prévenue. La soirée reste une fête.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic, wide shot of a packed festive dining room, warm golden light, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A full New Year's Eve dining room, paper hats, streamers, everyone standing and counting down with raised glasses toward a clock. Behind them, a single waiter moves through the crowd carrying a tray with fourteen glasses, weaving with impossible precision. At 5 seconds confetti cannons fire; the entire room erupts, arms up, kisses, chaos — and the waiter is buried in falling confetti, tray still perfectly level above his head. Final 2 seconds: the room celebrates around him; he stands motionless in the middle, covered in confetti, tray untouched, eyes closed. Audio: a crowd counting down in French, a huge cheer, confetti cannon pops, party horns, glasses clinking, then the cheering settling behind one long exhale. No music."
 },
 {
  "id": "EP128",
  "n": 128,
  "t": "Saint-Valentin surbookée",
  "mod": "Réservation",
  "ch": "4 - Placer un client à table",
  "drive": "1m6WdjC_iNYWO_4U3LmDuOsc-_Y_DrZLu",
  "hook": "Trente couverts en plus, ça rentre.",
  "punch": "Ça rentre. La question, c'est si ça revient.",
  "heygen": "Tu places tes clients selon la vraie capacité de ta salle. Serrer, ça se décide — ça ne se subit pas un soir de Saint-Valentin.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic, medium shot, romantic candlelit restaurant, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. Tables for two crammed so close together that they touch. A couple gaze into each other's eyes over a candle — and fifteen centimetres away, another couple does exactly the same, sharing the same candle. At 5 seconds a man reaches for his partner's hand and takes the hand of the woman at the next table instead; both couples freeze. Final 2 seconds: he releases it, all four look straight ahead, and the two women simultaneously sip their wine without a word. Audio: intimate restaurant ambience, murmured conversations layered too close together, cutlery, a small startled inhale, four seconds of dense awkward silence, two glasses being set down. No music."
 },
 {
  "id": "EP129",
  "n": 129,
  "t": "Premier jour de terrasse, 4 degrés",
  "mod": "Caroline",
  "ch": "4 - Gérer ses tables",
  "drive": "1SV1XsT61_cDqoRzD8JxehtRoOpyH5LaA",
  "hook": "Premier rayon de soleil de l'année.",
  "punch": "Ta terrasse ouvre. Ton service doit suivre.",
  "heygen": "Tu ouvres ta terrasse dans le logiciel : tables ajoutées, capacité mise à jour, réservations ouvertes dessus. Le premier rayon de soleil est rentable.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic, wide exterior, pale early-spring sunlight, visible breath in the air, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A restaurant terrace on the first sunny day of March. Every single outdoor table is full — of people in thick winter coats, scarves, woolly hats and gloves, holding cutlery with gloved hands, faces tilted toward the weak sun with beatific expressions. Inside, through the window, the empty warm dining room is visible. At 5 seconds a waiter comes out and offers a blanket to a guest, who waves it away without opening his eyes. Final 2 seconds: the waiter drapes it on him anyway and goes back in; the guest smiles, still sunbathing at four degrees. Audio: street ambience, wind, the clink of cutlery muffled by gloves, chattering teeth, a blanket unfolding, a contented sigh. No music."
 },
 {
  "id": "EP130",
  "n": 130,
  "t": "Fête de la musique",
  "mod": "Marketing",
  "ch": "7 - Ton agenda marketing",
  "drive": "1hBc6Axd0DE2ocTiXXKGlmj1dyagOwKFg",
  "hook": "21 juin. Devant ta porte.",
  "punch": "Autant que les gens sachent que tu es ouvert.",
  "heygen": "Ton agenda marketing connaît les temps forts de ton quartier. Tu prépares l'événement avant qu'il soit devant ta porte.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic, handheld exterior evening, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A drummer has set up a full drum kit directly in front of a restaurant's entrance door, blocking it completely, and plays with enormous enthusiasm. Diners inside press their faces to the window. At 5 seconds a waiter tries to get out with two plates, waits for a gap, and finally climbs carefully over the bass drum, plates held high. Final 2 seconds: he lands on the other side, serves an outdoor table with total dignity, and the drummer gives him an approving nod without stopping. Audio: enthusiastic live drumming, street crowd noise, a door pushing against a cymbal stand, a plate wobble, a cymbal crash as he climbs over, then the drumming continuing. No music beyond the drums."
 },
 {
  "id": "EP131",
  "n": 131,
  "t": "Rentrée : tout le monde est encore en vacances",
  "mod": "Équipe & Planning",
  "ch": "planning de la semaine",
  "drive": "1wboT7bVjEwxbhpU9Xgz8sRjjqn9XEd7X",
  "hook": "1er septembre. Deux absents.",
  "punch": "Un planning, ça se prépare avant la rentrée.",
  "heygen": "Tu construis la semaine de rentrée en amont : shifts posés, congés validés, coût affiché. Le premier septembre, tu n'es pas seul en cuisine.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic, wide shot of a large professional kitchen, harsh morning light, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A huge kitchen built for a brigade of eight, completely empty except for one chef standing alone at the pass. He looks left at four empty stations, right at three more. At 5 seconds a printer spits out a long ribbon of tickets; he looks at it, rolls up both sleeves, and moves to the first station. Final 2 seconds: a fast series of micro-cuts of him at four different stations in four different postures, ending back at the pass, plating. Audio: extractor hood hum, footsteps echoing in an empty kitchen, a printer chattering, sleeves rolling, then a rapid rhythmic burst of pans, tap, knife and plate sounds. No music."
 },
 {
  "id": "EP132",
  "n": 132,
  "t": "Le 15 août, seul ouvert",
  "mod": "Mon Site",
  "ch": "6 - Réservations et horaires",
  "drive": "1ykcHl2BaY22WlCsBA3DuwXaEMvQZUtMF",
  "hook": "Tout le quartier est fermé.",
  "punch": "Sauf toi. Encore faut-il qu'on te trouve en ligne.",
  "heygen": "Tes horaires d'ouverture sont à jour partout : site, réservation, Google. Quand tout le quartier ferme, on te trouve.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic, wide street shot, hot empty city, midday sun, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A deserted French city street in August: every shop shutter closed, heat haze rising from the asphalt, not a single person. The camera pans slowly. At 5 seconds it reaches one single open restaurant — and a queue of eighty people snaking down the pavement and around the corner, fans, hats, patience. Final 2 seconds: the owner steps into the doorway, looks at the queue, and slowly rolls up his sleeves. Audio: cicadas, distant traffic, absolute street emptiness, then a rising wall of crowd murmur as the camera reaches the queue, a door chime, fabric of sleeves rolling. No music."
 },
 {
  "id": "EP133",
  "n": 133,
  "t": "Le but à la 90e",
  "mod": "Caisse POS",
  "ch": "3 - Encaisser une commande",
  "drive": "1nHjH82ig0i-MtQqDmYp131htOSThaPIQ",
  "hook": "Une minute pour encaisser trois tournées.",
  "punch": "Ta caisse doit tenir le rythme.",
  "heygen": "Trois tournées en une minute : tu encaisses au comptoir ou à table, TPE relié, ticket envoyé. Ta caisse tient le rythme du match.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic, medium wide shot of a packed sports bar, screen glow, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A crowded bar watching a football match on a large screen (screen shows only abstract green blur, no readable broadcast). A waiter crosses the room with a tray of eight full beers. At 5 seconds the entire room explodes upward in a goal celebration, arms flying; the waiter is lifted off his feet by the surge, the tray launched vertically, beers suspended in slow motion. Final 2 seconds: he lands back on his feet, catches the empty tray, and every glass has landed upright on a nearby table in a perfect row. Audio: tense crowd murmur, a sudden roaring cheer, chairs falling, a slow-motion whoosh, glass bases landing on wood one after another, then a single collective gasp. No music."
 },
 {
  "id": "EP134",
  "n": 134,
  "t": "POV : la friteuse",
  "mod": "HACCP",
  "ch": "relevé de température",
  "drive": "10rqzHFjXbjkGi73uJyjt3XQM92eaIMK_",
  "hook": "Sept heures de service. Vue d'en bas.",
  "punch": "Elle aussi a une température à respecter.",
  "heygen": "L'huile et les frigos ont leurs seuils. Le relevé se fait en dix secondes, il est daté et gardé. Ta friteuse aussi a une conformité.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic, extreme low-angle POV from inside a deep fryer basket looking up, heat shimmer, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. The camera is inside a fryer looking up at the ceiling of a kitchen. A hand lowers a basket of fries directly toward the lens; bubbles erupt and fill the frame; the basket rises, drains, disappears. This repeats faster and faster — three times, four, five — hands and baskets flashing past. At 5 seconds a wristwatch on one of the arms shows the movement blurring. Final 2 seconds: the surface goes perfectly still, oil calm, a single bubble rising, the kitchen light steady above. Audio: a deep sustained roar of boiling oil, violent bubbling on each immersion, metal basket clanging on the rim, muffled kitchen shouting above, then a slow calming simmer and one last bubble. No music."
 },
 {
  "id": "EP135",
  "n": 135,
  "t": "POV : le carnet de réservations",
  "mod": "Réservation",
  "ch": "1 - Réservations du jour",
  "drive": "1m6WdjC_iNYWO_4U3LmDuOsc-_Y_DrZLu",
  "hook": "Toutes tes réservations du soir.",
  "punch": "Sur du papier. Vraiment ?",
  "heygen": "Tes réservations du soir sont ici, pas sur un carnet taché de café : contact, couverts, table, historique. Rien ne s'efface.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic, top-down macro POV of an open paper reservation book on a host stand, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. The camera looks straight down at an open paper booking book covered in handwriting rendered as illegible ink marks, crossings-out and arrows only — absolutely no readable words. Hands enter and leave: writing, crossing out, writing again, a coffee cup lands and leaves a brown ring, a page is torn slightly, a pen leaks. At 5 seconds a hand knocks the coffee over completely and a wave of liquid floods the page. Final 2 seconds: a hand blots it with a napkin; the ink is gone, only a brown smear remains where the evening's bookings were. Audio: host stand ambience, pen scratching, pages turning, a phone ringing repeatedly in the background, a ceramic cup landing, liquid spilling, paper absorbing, one very quiet \"non\". No music."
 },
 {
  "id": "EP136",
  "n": 136,
  "t": "POV : le lave-verres",
  "mod": "Service",
  "ch": "1 - Commandes multi-canaux",
  "drive": "1z4li_rdzH8yC7VFoWgOa4yMHbbKIAG29",
  "hook": "Deux minutes par cycle. Quatre-vingts cycles.",
  "punch": "Le service, c'est ça aussi.",
  "heygen": "Le service, c'est cent gestes invisibles. FoodEatUp en enregistre la trace pour que tu saches où part vraiment ton temps.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic POV from inside a commercial glasswasher looking out through the racks, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. The camera sits among upturned glasses inside a professional glasswasher. A hand slides in one more rack, then the door drops and everything goes dark blue. At 5 seconds the cycle starts: jets of water hit the lens from every direction, steam floods the frame, the whole world becomes a hurricane. Final 2 seconds: sudden stop, total calm, steam clearing, the door lifts and a hand reaches straight in and takes one glass. Audio: glass racks rattling, a heavy door dropping, a pump priming, violent spraying water and steam roar filling everything, an abrupt mechanical stop, dripping, a door mechanism, one glass squeaking. No music."
 },
 {
  "id": "EP137",
  "n": 137,
  "t": "POV : la machine à café",
  "mod": "Caisse POS",
  "ch": "3 - Encaisser une commande",
  "drive": "1nHjH82ig0i-MtQqDmYp131htOSThaPIQ",
  "hook": "Deux cent quarante cafés. Aujourd'hui.",
  "punch": "Combien encaissés ? Tu es sûr ?",
  "heygen": "Deux cent quarante cafés, deux cent quarante lignes encaissées. Tu compares le vendu et l'encaissé, à l'unité près.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic macro POV from behind the group head of an espresso machine, looking out at the bar, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. The camera looks out from inside the machine as a portafilter is locked in with a twist, a cup slides underneath, dark espresso streams past the lens. The cup leaves, another arrives, a hand wipes the lens area with a cloth. This accelerates: cup, cup, cup, faster and faster, hands blurring. At 5 seconds a hand slams the portafilter in slightly too hard and the whole frame shakes. Final 2 seconds: everything stops; one lone cup sits under the spout, and a hand appears and slowly turns the machine's switch off. Audio: a portafilter twist-lock, pump whirr, espresso pouring, cups clinking on saucers, steam wand shrieking, the tempo rising into chaos, a metallic slam, then a click and a long fading hiss. No music."
 },
 {
  "id": "EP138",
  "n": 138,
  "t": "POV : l'assiette, du pass à la table",
  "mod": "KDS",
  "ch": "3 - Gérer le KDS en direct",
  "drive": "1wQAkcP9pY90DLu_sE8GLiI6WYHZuYwq9",
  "hook": "Quarante-cinq secondes de vie.",
  "punch": "Chaque assiette compte. Compte-les.",
  "heygen": "De l'envoi au pass, chaque plat a son statut et son chrono. Tu comptes tes assiettes, tu ne les devines pas.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic first-person POV of a plate being carried through a restaurant, smooth gimbal motion, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. The camera IS the plate: it is lifted from the pass under a heat lamp, tilts, and travels fast through a kitchen — past a chef shouting, past flames, through swinging doors, through a crowded dining room, ducking under one arm, past a child's face that lights up. At 5 seconds the journey nearly ends in a collision with another waiter; both spin and continue. Final 2 seconds: the plate lands gently on a table and a guest leans into frame from above, delighted, fork already in hand. Audio: kitchen roar and shouting, a heat lamp buzz, swinging doors, ambient chatter swelling as it enters the dining room, a near-miss gasp, cloth brushing, then a plate settling on wood and one \"ah, merci !\". No music."
 },
 {
  "id": "EP139",
  "n": 139,
  "t": "Le rush, film de guerre",
  "mod": "KDS",
  "ch": "2 - Vue KDS par poste",
  "drive": "1wQAkcP9pY90DLu_sE8GLiI6WYHZuYwq9",
  "hook": "20 h 30. Le coup de feu.",
  "punch": "Sois équipé, pas héroïque.",
  "heygen": "Pendant le coup de feu, tu vois la charge de chaque poste. Tu envoies où il y a de la place. Être équipé, c'est ça.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic, shot like an epic war film: slow motion, heavy smoke, dramatic backlight, low heroic angles, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A professional kitchen at full rush filmed as a battlefield: steam rolling like battle smoke, sparks from a flambé, cooks moving in slow motion with grim determined faces, one carrying a stack of plates like ammunition, another wiping his brow with a forearm. The head chef stands at the pass surveying it all like a general, jaw set. At 5 seconds he raises one hand and everything freezes — every cook mid-motion. Final 2 seconds: he lowers his hand and points at the pass; the freeze breaks and all of them move at once. Audio: a low cinematic rumble, slowed-down clattering and shouting, a heartbeat, a whoosh of flame, total silence on the freeze, then a single sharp \"Service !\" and the noise returning at full volume. No music beyond the rumble."
 },
 {
  "id": "EP140",
  "n": 140,
  "t": "Le braquage du frigo",
  "mod": "StockVision",
  "ch": "16 - Mouvements de stock",
  "drive": "1Ib_pKyJ8_jaFAwtIhkzhtmUU_DCtGSSY",
  "hook": "Ton inventaire, la nuit.",
  "punch": "Ce qui disparaît finit toujours par se voir.",
  "heygen": "L'inventaire est daté, signé, comparé au théorique. Ce qui disparaît la nuit finit toujours par apparaître dans l'écart.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic, shot like a heist movie: darkness, tight close-ups, tense framing, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. Night in a closed restaurant kitchen. Three cooks in black, faces lit from below, execute a heist: one picks the walk-in fridge lock, one watches the door with a mirror, one crawls under an imaginary laser grid rendered as thin red light beams from a security sensor. At 5 seconds the crawler reaches the prize and lifts it with two hands, reverent and slow: a single small pot of crème dessert. Final 2 seconds: all three stare at it in silence; one of them slowly starts clapping. Audio: deep tense silence, a lock picking click, breathing held, a fridge seal cracking open, a soft electronic sensor beep, a plastic pot lifting, then three slow claps. No music beyond a low tension pulse."
 },
 {
  "id": "EP141",
  "n": 141,
  "t": "Cuisine, cockpit spatial",
  "mod": "PrediBot",
  "ch": "3 - Parler à PrediBot",
  "drive": "19kYZliyRnKraKVg1zdFrXCocD38VZ2a9",
  "hook": "Table 6 depuis 22 minutes.",
  "punch": "Un pilote automatique, ça existe aussi en cuisine.",
  "heygen": "Tu demandes, PrediBot répond avec tes vraies données : la table en attente, la production à lancer, l'alerte à traiter. Le pilote automatique existe.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic, shot like a sci-fi spacecraft cockpit: red emergency lighting, tight framing, steam venting, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A professional kitchen lit entirely by pulsing red emergency light, steam venting from a pan like a hull breach. Two cooks work at their stations like astronauts under alarm, one gripping an overhead rail, the other counting down on his fingers with fierce concentration. At 5 seconds he slams his palm onto the pass — and a perfectly plated dish slides forward into the light, mission accomplished. Final 2 seconds: the red light snaps back to normal warm kitchen light; both exhale; one gives a small thumbs up. Audio: a pulsing alarm klaxon, hissing steam vents, tense breathing, a countdown in French \"trois, deux, un\", a palm slam, a plate sliding on steel, then the alarm cutting out and normal kitchen ambience returning. No music."
 },
 {
  "id": "EP142",
  "n": 142,
  "t": "Duel à la spatule",
  "mod": "Équipe & Planning",
  "ch": "affectation des postes",
  "drive": "1wboT7bVjEwxbhpU9Xgz8sRjjqn9XEd7X",
  "hook": "Qui envoie le plat du jour.",
  "punch": "Répartis les postes avant le service, pas pendant.",
  "heygen": "Les postes sont répartis avant le service, pas pendant. Chacun sait ce qu'il envoie, personne ne dégaine sa spatule pour le savoir.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic, western duel framing, golden hour light streaming through a kitchen door, long shadows, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. Two cooks face each other down the length of a kitchen aisle, backlit by the setting sun through an open door, aprons flapping slightly like dusters. Extreme close-ups: narrowed eyes, a hand hovering over an apron pocket, a bead of sweat, a bay leaf tumbling across the floor like a tumbleweed. At 5 seconds both draw — spatulas — and freeze, pointed at each other. Final 2 seconds: they hold the standoff for one long beat, then both turn in unison and use the spatulas to plate two dishes side by side, perfectly synchronised. Audio: a single sustained tension note, wind, boots on tiles, a dry leaf skittering, two sharp fabric draws, a beat of silence, then two spatulas scraping pans in perfect time. No music beyond the tension note."
 },
 {
  "id": "EP143",
  "n": 143,
  "t": "La commande de 200 pièces",
  "mod": "Comptabilité",
  "ch": "devis",
  "drive": "1KlXihMLILGDrlxDuO2d3VCe1ic-kCAw_",
  "hook": "Une seule commande.",
  "punch": "Deux cents parts. Anticipe-les.",
  "heygen": "Deux cents parts, ça commence par un devis : quantités, prix, marge. Il se transforme en commande, puis en facture, sans ressaisie.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic, disaster-movie framing: slow push-in, dust in the light, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A calm kitchen. A ticket printer begins to print. It does not stop. The ribbon of paper grows past the pass, along the counter, across the floor, out through the swinging doors, and keeps going. Two cooks follow the paper with their eyes, then start walking beside it as it travels. At 5 seconds one of them picks up the end of the ribbon and holds it up: it stretches the entire length of the kitchen behind him. Final 2 seconds: the printer is still going; a third cook silently removes his apron and hangs it on a hook. Audio: quiet kitchen, a printer starting, chattering relentlessly and growing louder, footsteps following it, paper dragging on tiles, a printer that will not stop, then an apron string untying. No music."
 },
 {
  "id": "EP144",
  "n": 144,
  "t": "Le procès du steak trop cuit",
  "mod": "Marketing",
  "ch": "3 - Répondre aux avis",
  "drive": "1hBc6Axd0DE2ocTiXXKGlmj1dyagOwKFg",
  "hook": "Un avis une étoile.",
  "punch": "Réponds-y avant qu'il fasse jurisprudence.",
  "heygen": "Un avis une étoile, tu le vois tout de suite et tu réponds depuis l'outil. Une réponse rapide vaut mieux qu'un long procès.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic, shot like a courtroom drama: solemn wooden interior, dramatic overhead light, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A solemn courtroom. In the witness stand, elevated and alone under a single spotlight, sits a plate with one very overcooked steak on it. A serious man in a robe points at it accusingly; the jury of twelve leans forward as one. At 5 seconds a chef in whites stands in the defendant's box and lowers his head. Final 2 seconds: an overhead shot of the plate alone in the spotlight, absolute silence in the room. Audio: courtroom reverb, a low murmur, footsteps on wood, an accusing French voice saying one word \"Cuit.\", a collective gasp from the jury, a gavel strike, then silence. No music."
 },
 {
  "id": "EP145",
  "n": 145,
  "t": "Documentaire animalier : le gérant",
  "mod": "PrediBot",
  "ch": "1 - Lire ses prévisions",
  "drive": "19kYZliyRnKraKVg1zdFrXCocD38VZ2a9",
  "hook": "Le gérant, dans son habitat naturel.",
  "punch": "Espèce en voie d'épuisement.",
  "heygen": "Ton point du jour en un écran : ce qui arrive, ce qui manque, ce qui coince. L'espèce « gérant épuisé » n'est pas obligée de survivre comme ça.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic, shot like a nature documentary: long lens, foliage framing the edges of the shot, patient observational camera, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. Filmed from behind a potted plant in a restaurant, as if observing a rare animal in the wild: a restaurant manager in his natural habitat, moving between the bar, a laptop and the pass, marking his territory by straightening a chair, drinking coffee standing up in one gulp. At 5 seconds he freezes mid-motion, sensing he is being watched, and turns his head slowly toward the camera. Final 2 seconds: he stares directly into the lens through the leaves, motionless, then goes back to work. Audio: soft foliage rustle, distant restaurant ambience recorded at a distance as if through a long lens, a coffee cup, a chair scraping, a beat of held silence when he turns, then ambience resuming. No music."
 },
 {
  "id": "EP146",
  "n": 146,
  "t": "Quarante bougies et les sprinklers",
  "mod": "Comptabilité",
  "ch": "événements privés",
  "drive": "1KlXihMLILGDrlxDuO2d3VCe1ic-kCAw_",
  "hook": "Quarante bougies. Une seule mauvaise idée.",
  "punch": "Les gros événements, ça se prépare en amont.",
  "heygen": "Un événement, c'est une demande, un devis, une réservation et une facture. Enchaînés. Rien ne se prépare la veille au soir.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic, wide shot of a private dining room, warm party lighting, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A large birthday cake carrying an absurd number of lit candles is carried into a private room full of clapping guests; the flame is genuinely large. At 5 seconds a ceiling smoke detector chirps and the room's sprinklers activate, releasing a fine indoor rain over everyone. Final 2 seconds: the guests are soaked and laughing, arms raised, the birthday guest blows out the last surviving candle in the downpour, and the waiter stands at the edge of the frame holding a tray over his own head like an umbrella. Audio: applause and singing, a strong candle-flame roar, a smoke alarm chirping then blaring, water bursting from sprinklers, screams turning into laughter, a single candle being blown out, water drumming on a metal tray. No music."
 },
 {
  "id": "EP147",
  "n": 147,
  "t": "Le gâteau à cinq étages",
  "mod": "Comptabilité",
  "ch": "facture et devis",
  "drive": "1KlXihMLILGDrlxDuO2d3VCe1ic-kCAw_",
  "hook": "Douze mille euros de prestation.",
  "punch": "Sur un devis, pas sur un post-it.",
  "heygen": "Douze mille euros de prestation ne tiennent pas sur un post-it. Devis signé, acompte suivi, facture éditée : tout est dans le dossier.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic, extreme slow motion, elegant wedding venue, soft light, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. Two waiters carry an enormous five-tier wedding cake between them across a crowded room in extreme slow motion. Their arms tremble, sweat on a temple, the top tier wobbling gently. Guests turn to watch, hands over mouths. At 5 seconds one waiter's shoe slips two centimetres on the polished floor; the whole cake leans, the top tier tips — and he catches it flat with his forehead, holding it there. Final 2 seconds: they continue walking, cake intact, one man still balancing the top tier on his forehead, expression of absolute serenity. Audio: refined venue ambience, a collective inhale from the guests, slow-motion low rumble, a shoe squeak, a soft frosting contact sound, a suspended silence, then scattered relieved applause. No music."
 },
 {
  "id": "EP148",
  "n": 148,
  "t": "Le sumo de la place de livraison",
  "mod": "HubRise",
  "ch": "3 - Synchro caisse tierce",
  "drive": "19D09dNt_jZSKpcwVCU8Mn1OkMLkY_ojd",
  "hook": "Trois plateformes. Une place.",
  "punch": "Centralise les commandes, pas les embouteillages.",
  "heygen": "Trois plateformes, une seule file. Les commandes arrivent centralisées, avec leur horaire de retrait. Tes livreurs ne se croisent plus au même moment.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic, low-angle street shot, morning delivery time, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. Two delivery drivers in insulated backpacks arrive at the same narrow loading spot in front of a restaurant at the same second. They dismount, face each other, and adopt exaggerated sumo stances, stamping one foot each on the pavement, backpacks bulging. At 5 seconds they charge and collide chest to chest, backpacks compressing, neither moving an inch. Final 2 seconds: a third driver calmly parks his scooter in the free spot behind them and walks past into the restaurant with his bag. Audio: street ambience, two scooter engines cutting out, boots stamping, a comedic drum-like thud on impact, insulated fabric compressing, grunting, then a third small engine, a kickstand click and a door chime. No music."
 },
 {
  "id": "EP149",
  "n": 149,
  "t": "Le flash mob de la salle",
  "mod": "Marketing",
  "ch": "5 - Lancer une campagne",
  "drive": "1hBc6Axd0DE2ocTiXXKGlmj1dyagOwKFg",
  "hook": "Ta salle a un truc que personne d'autre n'a.",
  "punch": "Fais-le savoir.",
  "heygen": "Ta salle a quelque chose d'unique : fais-le savoir. Campagne créée, segment choisi, résultats mesurés, CA attribué.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic, wide shot of a full dining room, warm evening light, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A completely normal, busy restaurant dinner service. One guest stands up and begins a small rhythmic movement. Two others join. At 5 seconds every single person in the room — guests, waiters, a cook who appears in the kitchen doorway — is performing a tight synchronised routine, napkins waving, chairs pushed back, in perfect unison. Final 2 seconds: they all sit down at exactly the same moment and resume eating as if nothing happened; one lone waiter stands frozen in the middle holding a tray, the only one who did not know. Audio: normal restaurant ambience, one chair pushing back, then dozens of feet finding a rhythm on the floor, clapping and cutlery used as percussion building to a peak, an abrupt collective stop, chairs sliding in, then normal chatter resuming. No music track — rhythm built from claps, feet and cutlery."
 },
 {
  "id": "EP150",
  "n": 150,
  "t": "Le salut final",
  "mod": "PrediBot",
  "ch": "1 - Lire ses prévisions",
  "drive": "19kYZliyRnKraKVg1zdFrXCocD38VZ2a9",
  "hook": "Cent cinquante épisodes.",
  "punch": "Une seule promesse : ton restaurant, avant, pendant et après le service.",
  "heygen": "Cent cinquante épisodes pour dire une chose : ton restaurant tient dans un seul outil, avant, pendant et après ton service. Le reste, c'est du bruit.",
  "hf": "Vertical 9:16, 10 seconds, photorealistic, cinematic slow dolly back, warm golden restaurant lighting, theatrical curtain-call framing, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A restaurant dining room arranged like a theatre stage after a show. In one long line facing the camera stand, side by side: a chef in whites, two waiters, a dishwasher, a delivery rider holding his helmet — and among them, perfectly calm, a golden retriever sitting upright, a penguin in a tiny apron, a goat, a person in an oversized plain yellow chicken mascot costume, and a wheeled service robot. At 5 seconds the whole line bows in unison, humans and animals alike, the robot tilting forward on its base. Final 2 seconds: they straighten up together and hold, looking straight into the camera, the restaurant glowing behind them. Audio: a full room of applause and whistling, chairs, one dog bark, one penguin squawk, one goat bleat, a servo whirr as the robot bows, then the applause continuing over a held silence from the line. No music."
 }
];

function saisonDe(n) {
  if (n <= 30) return 1;
  if (n <= 60) return 2;
  if (n <= 90) return 3;
  if (n <= 120) return 4;
  return 5;
}

function creerTout() {
  var debut = new Date().getTime();
  var props = PropertiesService.getScriptProperties();
  var depart = parseInt(props.getProperty('curseur') || '0', 10);
  var faits = 0;

  for (var i = depart; i < EP.length; i++) {
    if (new Date().getTime() - debut > LIMITE_MS) {
      props.setProperty('curseur', String(i));
      Logger.log('Pause a l index ' + i + ' (' + EP[i].id + '). ' +
                 faits + ' episodes traites. Relance creerTout().');
      return;
    }
    creerEpisode(EP[i]);
    faits++;
  }

  props.setProperty('curseur', String(EP.length));
  Logger.log('TERMINE — ' + EP.length + ' episodes en place.');
  retirerDeclencheurs();
}

function creerEpisode(e) {
  var parent = DriveApp.getFolderById(SAISONS[saisonDe(e.n)]);
  var nom = e.id + ' - ' + e.t;

  var it = parent.getFoldersByName(nom);
  var dossier = it.hasNext() ? it.next() : parent.createFolder(nom);

  var sous = {};
  for (var i = 0; i < SOUS_DOSSIERS.length; i++) {
    sous[SOUS_DOSSIERS[i]] = sousDossier(dossier, SOUS_DOSSIERS[i]);
  }

  fichier(dossier, '00-FICHE-EPISODE-' + e.id + '.md', fiche(e));
  fichier(sous['01-PROMPTS'], '01-HIGGSFIELD-' + e.id + '.md', promptHiggsfield(e));
  fichier(sous['01-PROMPTS'], '02-HEYGEN-' + e.id + '.md', promptHeygen(e));
  fichier(sous['01-PROMPTS'], '03-ELEVENLABS-' + e.id + '.md', promptElevenlabs(e));
  fichier(sous['05-ACADEMY'], 'FICHE-ACADEMY-' + e.id + '.md', ficheAcademy(e));

  raccourci(sous['02-ASSETS'].getId(), e.drive, 'TUTO SOURCE - ' + e.mod);
}

function sousDossier(parent, nom) {
  var it = parent.getFoldersByName(nom);
  return it.hasNext() ? it.next() : parent.createFolder(nom);
}

/** N'ecrase jamais un fichier existant : l'humain a pu l'annoter. */
function fichier(dossier, nom, contenu) {
  if (dossier.getFilesByName(nom).hasNext()) return;
  dossier.createFile(nom, contenu, MimeType.PLAIN_TEXT);
}

function raccourci(parentId, cibleId, nom) {
  try {
    var parent = DriveApp.getFolderById(parentId);
    if (parent.getFilesByName(nom).hasNext()) return;
    Drive.Files.create({
      name: nom,
      mimeType: 'application/vnd.google-apps.shortcut',
      parents: [parentId],
      shortcutDetails: { targetId: cibleId }
    }, null, { supportsAllDrives: true });
  } catch (err) {
    Logger.log('Raccourci impossible (' + nom + ') : ' + err);
  }
}

function fiche(e) {
  return '# ' + e.id + ' — ' + e.t + '\n\n' +
    '| | |\n|---|---|\n' +
    '| Saison | ' + saisonDe(e.n) + ' |\n' +
    '| Module | ' + e.mod + ' |\n' +
    '| Chapitre | ' + e.ch + ' |\n' +
    '| Tuto source | https://drive.google.com/drive/folders/' + e.drive + ' |\n\n' +
    '## Les trois fichiers a deposer dans 02-ASSETS\n\n' +
    '| Fichier | Ce que c est | Contrainte |\n|---|---|---|\n' +
    '| `' + e.id + '_hook.mp4` | clip Higgsfield 10 s | 9:16, AUCUN texte dans l image, chute a 5,0 s |\n' +
    '| `' + e.id + '_avatar.mp4` | segment HeyGen | 10 s (max 12), avec audio, sans musique, sans sous-titres |\n' +
    '| `' + e.id + '_soft.mp4` | extrait du tuto | 10 s ; sinon Claude Code le decoupe a la source |\n\n' +
    'Nommage strict : trois chiffres. Sans le zero, Drive trie EP1, EP10, EP100, EP11.\n\n' +
    '## Les textes de l episode\n\n' +
    '**Hook incruste (0,8 -> 3,5 s)**\n\n> ' + e.hook + '\n\n' +
    '**Punchline VO (5,0 s)**\n\n> ' + e.punch + '\n\n' +
    '**Script HeyGen (16,0 -> 26,0 s)**\n\n> ' + e.heygen + '\n\n' +
    '## Etat\n\n' +
    '- [ ] hook depose\n- [ ] avatar depose\n- [ ] extrait tuto\n' +
    '- [ ] punchline generee\n- [ ] master monte\n- [ ] brouillons CMS crees\n';
}

function promptHiggsfield(e) {
  return '# Prompt Higgsfield — ' + e.id + '\n\n' +
    'A generer TOI-MEME depuis l interface Higgsfield. Claude Code ne lance\n' +
    'aucune generation. Telecharge le resultat en `' + e.id + '_hook.mp4`\n' +
    'dans 02-ASSETS.\n\n' +
    'Modele conseille : Kling 3.0 (audio natif) ou Seedance 2.5.\n' +
    'Format 9:16 · 1080x1920 · 10 s.\n\n' +
    '## Prompt\n\n```\n' + e.hf + '\n```\n\n' +
    '## Ce qui est verifie a la reception\n\n' +
    '- aucun texte, sous-titre, filigrane ni logo dans l image\n' +
    '- la chute comique tombe a 5,0 s (c est la que la punchline arrive)\n' +
    '- les 2 dernieres secondes tiennent le plan fige\n' +
    '- premiere frame non noire : elle devient la vignette sur les 5 reseaux\n';
}

function promptHeygen(e) {
  return '# Prompt HeyGen — ' + e.id + '\n\n' +
    'Segment D du master (16,0 -> 26,0 s). L avatar est en haut, le logiciel en bas.\n' +
    'L avatar parle avec sa voix HeyGen. AUCUNE voix ElevenLabs sur ce segment.\n\n' +
    '## A coller dans HeyGen\n\n```\n' +
    'Avatar : [ton avatar FoodEatUp]\n' +
    'Format : 9:16 · 1080x1920 · duree cible 10 s (max 12 s)\n' +
    'Cadrage : plan poitrine, avatar centre dans le tiers superieur, regard camera\n' +
    'Fond : uni charte FoodEatUp\n' +
    'Voix : voix FR de l avatar, debit pose, ton direct, tutoiement\n' +
    'Musique : AUCUNE (le montage gere l audio)\n' +
    'Sous-titres HeyGen : DESACTIVES (burn-in fait au montage)\n' +
    'Gestes : naturels, une seule main, pas de pointage vers le bas du cadre\n' +
    'Script : « ' + e.heygen + ' »\n```\n\n' +
    '## Le screencast qui va dessous\n\n' +
    e.mod + ' > ' + e.ch + '\n' +
    'https://drive.google.com/drive/folders/' + e.drive + '\n';
}

function promptElevenlabs(e) {
  return '# Voix ElevenLabs — ' + e.id + '\n\n' +
    'Seule la punchline est propre a cet episode. Les trois VO fixes (VO_A, VO_B,\n' +
    'VO_C) sont generees une fois pour les 150 et vivent dans _COMMUN.\n\n' +
    '## Punchline — ' + e.id + '_punchline.mp3\n\n' +
    '```\n' + e.punch + '\n```\n\n' +
    'Cible 2,0 a 2,5 s, plafond 2,8 s. Si le rendu depasse, RACCOURCIR LE TEXTE.\n' +
    'Ne jamais accelerer l audio : une VO acceleree s entend.\n\n' +
    '## Reglages figes sur les 153 fichiers\n\n' +
    'stability 0.55 · similarity_boost 0.80 · style 0.15 · speaker_boost true\n' +
    'eleven_multilingual_v2 · mp3_44100_128\n';
}

function ficheAcademy(e) {
  return '# Fiche Academy — ' + e.id + ' ' + e.t + '\n\n' +
    '**Module** ' + e.mod + ' — **Chapitre** ' + e.ch + '\n\n' +
    '## Ce que l episode montre\n\n' + e.heygen + '\n\n' +
    '## Tutoriel complet\n\n' +
    'https://drive.google.com/drive/folders/' + e.drive + '\n';
}

/** Declencheur horaire : laisse le script finir tout seul. */
function planifier() {
  retirerDeclencheurs();
  ScriptApp.newTrigger('creerTout').timeBased().everyMinutes(10).create();
  Logger.log('Declencheur pose. Il se retirera au TERMINE.');
}

function retirerDeclencheurs() {
  var t = ScriptApp.getProjectTriggers();
  for (var i = 0; i < t.length; i++) {
    if (t[i].getHandlerFunction() === 'creerTout') ScriptApp.deleteTrigger(t[i]);
  }
}

function reinitialiserProgression() {
  PropertiesService.getScriptProperties().deleteProperty('curseur');
  Logger.log('Progression remise a zero.');
}
