# Saison 3 — 30 prompts Higgsfield (EP61 → EP90)
## Une vidéo = une fonctionnalité FoodEatUp

Réglages identiques aux saisons 1 et 2 : **Kling 3.0** (audio natif) ou
**Seedance 2.5**, 9:16, 10 s, 1080×1920. Générés depuis l'UI Higgsfield, déposés
dans `assets/hooks/EP61.mp4` … `EP90.mp4`. Aucun texte dans l'image.

---

## Ce qui change par rapport aux saisons 1 et 2

Les deux premières saisons partageaient un **bloc D générique** (site → caisse →
KDS → marketing). La saison 3 le remplace par un **bloc D spécifique à la
fonctionnalité**, tiré du tutoriel Académy correspondant.

Le montage devient donc :

| Bloc | 30 s | Contenu |
|---|---|---|
| A | 0 → 7 s | Gag Higgsfield (le problème, sans logiciel) |
| B | 7 → 9 s | Sting logo |
| C | 9 → 15 s | **Nouveau texte court, propre à l'épisode** (voir colonne VO C) |
| D | 15 → 26 s | **Capture du tutoriel Drive de la fonctionnalité** |
| E | 26 → 30 s | Closing (inchangé, `vo/common/E-closing-30.mp3`) |

Le bloc C commun (« dix logiciels, mille euros ») disparaît en saison 3 : chaque
épisode a sa propre ligne de 6 s. C'est plus long à produire côté voix, mais
c'est ce qui transforme une série de gags en série de démos.

**Conséquence pour Claude Code** : `episodes.json` gagne deux champs par
épisode — `feature_drive_folder_id` et `vo_c_text`. Le reste du pipeline est
inchangé.

---

## EP61 — Le badge introuvable

> Vertical 9:16, 10 seconds, photorealistic, cinematic handheld camera, shallow depth of field, natural light, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. Early morning at a restaurant staff entrance. A young employee taps a supermarket loyalty card against the door reader. Nothing. He tries a metro pass. Nothing. He tries his wrapped sandwich. At 5 seconds the door opens on its own because a colleague pushes it from inside, and he walks in holding the sandwich against the reader. Final 2 seconds: the reader blinks red, alone, as the door closes. Audio: quiet street ambience, three flat error beeps, plastic tapping on a reader, a door hinge, a colleague's mumbled "Bonjour", then one last error beep. No music.

**Hook** : `Ton système de pointage.`
**Punchline VO** : « Un badge, un QR code, un code PIN. Point. »
**VO bloc C** : « Chaque employé pointe avec un badge NFC, un QR code de boutique ou son code PIN. L'heure d'arrivée est enregistrée, pas discutée. »

**Fonctionnalité** : pointage employé — badge NFC, QR code boutique, borne code PIN
**Drive** : Module 2 › `8- Configuration et génération du QR code par boutique` (`1tu_HLStTS54V-GCm6SgNFNbjqVQodyeS`) · `10- Commande de carte NFC personnalisée` (`1JaigGqCPAzM44n1bmCAj4pKQx6cfQvl7`) · `11- Borne d'accueil des employés` (`1b_d7I_15WX1Jbv-iwbifUXHjxvjYxLQL`)
**MCP** : `list_attendances`

---

## EP62 — La photo de pointage

> Vertical 9:16, 10 seconds, photorealistic, front-on framing as if from a tablet camera, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. An employee stands in front of a wall-mounted tablet at the staff entrance, taking his clock-in photo. He tries a neutral face, then a serious face, then a slight smile, then a full grin, adjusting his hair between each. At 5 seconds he settles on an intensely dramatic, chin-lifted expression. Final 2 seconds: he holds it perfectly still, absolutely committed. Audio: staff room ambience, a soft camera shutter repeated five times, fabric rustling, one satisfied exhale. No music.

**Hook** : `« Je te jure, j'étais là à 8 h. »`
**Punchline VO** : « Photo, heure, poste. Le débat est clos. »
**VO bloc C** : « Chaque pointage garde une empreinte photo et l'heure exacte. Entrées, sorties, pauses. Tout est dans l'historique. »

**Fonctionnalité** : pointage avec empreinte photo, gestion des pauses
**Drive** : Module 2 › `15- Gestion des pauses, pointage entrée et sortie et empreinte photo` (`1cMGeDtBYtJdS4iu_yWQQrQ5RcbCnl38_`) · `12- Historique des pointages` (`165Pq4ZXw8IGWVge3kACbiiLJ162oDYij`)
**MCP** : `list_attendances`

---

## EP63 — Le post-it perdu

> Vertical 9:16, 10 seconds, photorealistic, office corridor, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. An employee writes carefully on a yellow sticky note, presses it firmly onto the manager's office door, and walks away satisfied. The camera stays on the door. At 5 seconds the note peels off in slow motion, drifts sideways and slides down the gap behind a radiator. Final 2 seconds: the empty door, one corner of yellow just visible behind the radiator grille. Audio: corridor ambience, pen on paper, a sticky note pressed to wood, footsteps leaving, a faint paper slide, a metallic radiator tick. No music.

**Hook** : `Ta demande de congé.`
**Punchline VO** : « Demandée, reçue, validée. Sans papier. »
**VO bloc C** : « L'employé pose sa demande d'absence depuis son espace. Tu valides ou tu refuses, et le planning se met à jour tout seul. »

**Fonctionnalité** : demandes de congé et d'absence
**Drive** : Module 2 › `17- Demande d'absence ou de congé de l'employé` (`1Y_WxNxLa301L_2rhVS2zjpi2CqqrS5iw`)
**MCP** : `list_leaves`, `approve_leave`, `reject_leave`

---

## EP64 — Le planning au marqueur

> Vertical 9:16, 10 seconds, photorealistic, staff room, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A whiteboard weekly rota covered in layers of crossings-out, arrows, magnets and three different marker colours. A manager studies it, then adds a strip of masking tape over one section and writes a new name on the tape. At 5 seconds a magnet gives way and half the paper slips sideways. Final 2 seconds: he presses it back with one finger and holds it there, looking at the camera. Audio: staff room ambience, squeaky marker on whiteboard, tape tearing, a magnet clattering to the floor, one long exhale. No music.

**Hook** : `Le planning de la semaine.`
**Punchline VO** : « Par employé ou par poste. Imprimable. À jour. »
**VO bloc C** : « Le planning se construit par employé ou par poste de travail. Tu l'affiches, tu l'imprimes, et le coût de la semaine se calcule au fur et à mesure. »

**Fonctionnalité** : planning équipe par employé ou par poste
**Drive** : Module 2 › `6- Affichage et impression du planning Équipe` (`1sLZB_zcuk_uL3BpFvj63LdU2W_7oKU-X`) · `4- Configuration des horaires` (`1LH1Yc5W_TjOZlRh3yalK5FGLesAKKNA4`)
**MCP** : `list_plannings`, `create_shift`, `update_employee_schedule`

---

## EP65 — Le stagiaire au bureau

> Vertical 9:16, 10 seconds, photorealistic, back office, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A very young intern sits in the manager's oversized leather chair, feet up on the desk, slowly spinning, holding the manager's coffee mug. He opens a drawer, looks inside, nods approvingly. At 5 seconds the office door opens off-frame; he freezes mid-spin, feet still on the desk. Final 2 seconds: he is standing perfectly straight beside the chair, mug behind his back. Audio: office ambience, a chair spinning and creaking, a drawer sliding, a door handle turning, an abrupt scramble, then silence. No music.

**Hook** : `Qui a accès à quoi ?`
**Punchline VO** : « Chaque rôle voit exactement ce qu'il doit voir. »
**VO bloc C** : « Tu définis les rôles et les permissions. Chaque employé ouvre une interface d'accueil adaptée à son poste, et rien de plus. »

**Fonctionnalité** : rôles, permissions et interfaces par poste
**Drive** : Module 2 › `1- Configuration des rôles et permissions` (`1l1uyfbTUhGHdrBTNHpSmzeHf551e7byp`) · `14- Interface d'accueil des employés selon les rôles` (`1OM_9b9btI1TWGGpf13I46fNhszDKAoSJ`)
**MCP** : `create_employee`, `update_employee`, `get_employee`

---

## EP66 — Le grille-pain qui ne répond pas

> Vertical 9:16, 10 seconds, photorealistic, professional kitchen, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A cook, hands covered in flour, leans toward a stainless-steel toaster on the counter and speaks to it clearly, waiting for an answer. Nothing. He speaks again, louder, more articulately. At 5 seconds the toaster ejects two slices of toast violently. He takes this as a response and nods. Final 2 seconds: he goes back to work, satisfied, having received his answer. Audio: kitchen ambience, a muffled human question, a pause, a second louder question, a metallic toaster spring-pop, one accepting "Ah, d'accord." No music.

**Hook** : `Ta cuisine n'a personne à qui parler.`
**Punchline VO** : « Jarvis répond, lui. Et il note. »
**VO bloc C** : « Jarvis, c'est l'assistant vocal de ton équipe en cuisine. On lui parle, il enregistre les températures, les tâches, les productions. Les mains restent sales, les données restent propres. »

**Fonctionnalité** : Jarvis, assistant vocal employé
**Drive** : Module 2 › `5- Configuration de Jarvis et son jeton` (`1ZBn-9i0IRMEMiSK3bWLgAATmHbHVvgn8`) · `9- Code PIN employé pour l'accès à Jarvis` (`1m40kS9oWTWYWVSwpv3eaCKj_wSsqHGZx`)
**MCP** : `add_temperature`, `assign_task`

---

## EP67 — Le thermomètre humain

> Vertical 9:16, 10 seconds, photorealistic, kitchen fridge close-up, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A chef opens a fridge door, holds his bare hand inside for exactly two seconds, withdraws it, and gives a confident single nod as if a precise measurement has been taken. He writes nothing down. At 5 seconds he repeats the procedure on the freezer, this time with two fingers, and nods even more confidently. Final 2 seconds: he closes the door and walks away, hands in pockets, entirely satisfied with his data collection. Audio: fridge seal opening and closing, compressor hum, kitchen ambience, one decisive "Hm." repeated twice. No music.

**Hook** : `Ton relevé de température.`
**Punchline VO** : « Un vrai relevé, horodaté, par équipement. »
**VO bloc C** : « Chaque frigo, chaque congélateur, chaque chambre froide est déclaré. Le relevé est horodaté, associé à l'équipement, et l'historique se remplit tout seul. »

**Fonctionnalité** : relevés de température HACCP par équipement
**Drive** : Module 4 › `2- Ajouter, supprimer, modifier un équipement` (`1WQDVmCZUct__2ovbFBELmewN_Vp-GkHw`) · `3- Enregistrer une température` (`1ohzkWaC6hB6wEa2ow1gOtoLWz_zjd5_O`) · `4- Historique de mes températures` (`1KUT3iph-lFxoLX4iKKUEv9Vx9lGDqh2z`)
**MCP** : `create_equipment`, `add_temperature`, `list_haccp_temperatures`

---

## EP68 — Le second avis

> Vertical 9:16, 10 seconds, photorealistic, kitchen close-up, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A cook opens a large tub of cream and sniffs it long and deeply, eyes narrowed in genuine scientific concentration. He sniffs again. Uncertain, he holds it out toward a colleague. The colleague sniffs, makes exactly the same face, and hands it back without a word. At 5 seconds a third cook enters frame, sniffs, and shrugs. Final 2 seconds: all three stand in a small circle staring at the tub, nobody deciding. Audio: kitchen ambience, deep deliberate sniffing, plastic lid flexing, a noncommittal grunt, a shrug of fabric, silence. No music.

**Hook** : `Le test scientifique du nez.`
**Punchline VO** : « Une étiquette DLC, et plus personne ne renifle. »
**VO bloc C** : « Tu imprimes une étiquette de stockage ou de vente avec sa date limite. Le doute disparaît, et l'historique des étiquettes reste consultable. »

**Fonctionnalité** : étiquettes DLC, impression stockage et vente
**Drive** : Module 4 › `18- Imprimer une étiquette de vente ou de stockage` (`1fK8_rGPJyN1_He5Vo2n6qgO9hKeOBwyT`) · `19- Historique de mes étiquettes` (`1XD1uzS3j0spECOnYWqpLwhL3tG1D9IT9`)
**MCP** : `create_haccp_label`, `list_haccp_labels`

---

## EP69 — Le livreur fantôme

> Vertical 9:16, 10 seconds, photorealistic, restaurant back door, morning, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A delivery driver stacks fifteen boxes and crates against the back door with impressive speed, drops a crumpled delivery note on top, and is already jogging back to his van before anyone appears. At 5 seconds the kitchen door opens and a cook steps out holding a pen, looking at an empty street. Final 2 seconds: the van pulls away in the background; the cook looks down at the tower of unchecked boxes. Audio: crates thudding on concrete, fast footsteps, a van door sliding shut, an engine pulling away, a kitchen door creak, then street quiet. No music.

**Hook** : `« Tu as vérifié la livraison ? »`
**Punchline VO** : « Température, DLC, code EAN. En scannant. »
**VO bloc C** : « À la réception, tu scannes le code EAN, tu saisis la température, tu poses la DLC. Le contrôle est tracé, et le stock se met à jour dans la foulée. »

**Fonctionnalité** : contrôle à réception, scan EAN, températures de livraison
**Drive** : Module 4 › `25- Contrôle à réception de vos livraisons` (`1gZmtvcVR5A6PnBuwf01gFFDioWJ5EQ_V`) · `27- Modifier la température, scanner un code EAN, ajouter une DLC` (`1CI_lxNpvFjd42ol04ITlU5wxbsXCJf6u`)
**MCP** : `create_haccp_reception`, `list_haccp_reception`, `adjust_stock`

---

## EP70 — La dalle propre

> Vertical 9:16, 10 seconds, photorealistic, high angle then low angle, kitchen floor, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. An employee mops a single floor tile with extraordinary dedication, back and forth, until it gleams. The camera pulls back slowly to reveal the entire rest of the kitchen floor untouched and grimy. At 6 seconds he steps back to admire his one perfect tile, hands on hips. Final 2 seconds: he takes a photo of that single tile with his phone. Audio: kitchen ambience, wet mop strokes on tile, a bucket handle clank, a phone camera shutter, one proud sigh. No music.

**Hook** : `« C'est fait. »`
**Punchline VO** : « Photo analysée par l'IA. Rapport objectif. »
**VO bloc C** : « Tu paramètres ton plan de nettoyage par zone et par poste. L'équipe photographie, l'IA analyse et sort un rapport de nettoyage. Fini le déclaratif. »

**Fonctionnalité** : plan de nettoyage et analyse photo par IA
**Drive** : Module 4 › `10- Ajouter et paramétrer un plan de nettoyage` (`12L7F6QWg_Dnl8l0fdP20J-CVOxA6iOJD`) · `29- Prendre une photo et faire analyser par l'IA` (`1_LgMACeuDcqWvVL5ArOIZYbJ0iZcrrO5`)
**MCP** : `create_cleaning_zone`, `record_cleaning_action`, `list_cleaning_actions`

---

## EP71 — La liste à l'envers

> Vertical 9:16, 10 seconds, photorealistic, kitchen corridor, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A cook ticks boxes on a paper checklist at high speed without ever looking at the sheet, walking down a corridor. Tick, tick, tick, tick. At 5 seconds he reaches the end, signs it with a flourish, and pins it to the wall. Final 2 seconds: the camera holds on the sheet, which is pinned completely upside down. Audio: brisk footsteps, rapid pen ticking on paper, a satisfied hum, a pin pushing into a corkboard, then corridor quiet. No music.

**Hook** : `La check-list du soir.`
**Punchline VO** : « Cochée, horodatée, signée par qui l'a faite. »
**VO bloc C** : « Tu crées tes check-lists hygiène une fois. Chaque validation est enregistrée avec l'heure et la personne. Le contrôle de conformité devient une trace, pas une promesse. »

**Fonctionnalité** : check-lists hygiène et contrôles de conformité
**Drive** : Module 4 › `22- Créer une check-list hygiène` (`15CwOKunwpcys81_j-rwf0W2bLfghvsXv`) · `23- Réaliser des contrôles de conformité` (`14aDxJMZU_ZnneMXrv0ucr2B1cpKJnAWl`) · `24- Historique des check-lists` (`1-IBldJ7iAzA2aeVJXv8ZsJwUOPnTt2F6`)
**MCP** : `create_hygiene_checklist`, `create_hygiene_checklist_validation`, `list_hygiene_checklists`

---

## EP72 — Le classeur

> Vertical 9:16, 10 seconds, photorealistic, restaurant office, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A health inspector in a jacket stands waiting with a clipboard. The manager hauls an enormous overstuffed ring binder onto the desk between them. He opens it. At 5 seconds the rings give way and several hundred loose pages fan out across the desk and floor in slow motion. Final 2 seconds: the two men look at each other over a desk covered in paper; the inspector clicks his pen once. Audio: office ambience, a heavy binder thud, metal rings snapping open, a long paper cascade, one pen click, total silence. No music.

**Hook** : `Contrôle sanitaire. Ce matin.`
**Punchline VO** : « Tout l'historique HACCP, exporté en un clic. »
**VO bloc C** : « Températures, traçabilité, nettoyage, réceptions, check-lists : tout l'historique HACCP est là, filtrable par période et exportable. Le contrôle dure dix minutes. »

**Fonctionnalité** : export de l'historique HACCP complet
**Drive** : Module 4 › `30- Retrouver et exporter les historiques du module HACCP` (`1zW01WAMfEsT4x62i4D1nwm4BCb3cYM_e`) · `1- Accueil et historique` (`14eutFL8vuT8ImEadyltp1UBs15KWmEZ_`)
**MCP** : `list_haccp_temperatures`, `list_haccp_tracabilite`, `list_haccp_reception`, `list_cleaning_actions`

---

## EP73 — Pile ou face

> Vertical 9:16, 10 seconds, photorealistic, bakery kitchen at dawn, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A chef stands in front of empty bread racks holding a coin. He flips it, catches it on the back of his hand, looks at it, and writes a number on an order pad. Unsatisfied, he flips again. At 5 seconds he flips a third time, misses the catch, and the coin rolls under a rack. Final 2 seconds: he writes a number anyway, without the coin. Audio: quiet early-morning kitchen, a coin ringing off a thumb, a slap on skin, pen on paper, a coin rolling on tiles, then silence. No music.

**Hook** : `Combien tu commandes pour samedi ?`
**Punchline VO** : « Tes ventes le savent. Demande-leur. »
**VO bloc C** : « À partir de tes ventes réelles et de tes productions passées, la prédiction te dit quoi commander et en quelle quantité. Tu arbitres, tu ne devines plus. »

**Fonctionnalité** : prédiction des commandes StockVision AI
**Drive** : Module 5 › `3- Ma carte, prédictions des commandes en fonction de vos ventes et production` (`107h7JIXDFCD5cjyF90tiOZT2LSkFSjFj`)
**MCP** : `list_top_productions`, `list_low_stocks`, `list_production_alerts`

---

## EP74 — La liste oubliée

> Vertical 9:16, 10 seconds, photorealistic, wholesale market aisle, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A restaurateur stands still in the middle of a busy wholesale market aisle, patting every pocket of his jacket, then his trousers, then his jacket again. He looks at his empty hands. At 5 seconds he turns a full slow circle on the spot, trolley beside him, surrounded by produce, remembering nothing. Final 2 seconds: he picks up one random cabbage and looks at it as if it might help. Audio: busy market ambience, forklift beeps, fabric patting, a trolley wheel squeak, one hopeless "Bon…", crowd murmur. No music.

**Hook** : `Tu as oublié la liste.`
**Punchline VO** : « Elle se construit toute seule. Et elle part au fournisseur. »
**VO bloc C** : « La liste de courses se remplit depuis tes productions planifiées et tes stocks bas. Tu la valides, elle part directement au bon fournisseur. »

**Fonctionnalité** : liste de courses et commande fournisseur
**Drive** : Module 5 › `4- Liste des courses, ajouter, modifier, supprimer` (`1wOLOfH054cLrfHRx_GmGlKxrfW10cHhb`) · `5- Commander et envoyer ma liste au fournisseur` (`18dlgcwepziokEkkpTQFu1-ifGJ5ajOYB`)
**MCP** : `list_low_stocks`, `create_supplier_order`, `list_suppliers`

---

## EP75 — La facture dans la poche

> Vertical 9:16, 10 seconds, photorealistic, macro on a stainless counter, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A hand pulls a heavily crumpled paper invoice out of an apron pocket and unfolds it on a counter, smoothing it flat with the side of the hand. The paper is stained with oil and sauce, and one corner is torn away. At 5 seconds the hand rotates it ninety degrees, trying to find a readable angle. Final 2 seconds: the paper slowly re-folds itself back into its crumpled shape on its own. Audio: paper crackling and unfolding, a hand smoothing paper on steel, kitchen ambience, one defeated exhale, a soft paper rustle as it curls back. No music.

**Hook** : `Ta facture fournisseur.`
**Punchline VO** : « Photographie-la. Les prix se mettent à jour seuls. »
**VO bloc C** : « Tu prends la facture en photo. L'analyse lit les lignes, met à jour tes prix d'achat et range la dépense au bon endroit. Tu n'as rien ressaisi. »

**Fonctionnalité** : OCR facture livraison et mise à jour des prix d'achat
**Drive** : Module 5 › `9- Livraisons, ajouter une facture, OCR, analyse et mise à jour des prix` (`1zh3uaf2PRqTdZsddSpupoSIkpMbvsAzJ`) · `10- Ajout des factures dans mes dépenses` (`1KNKei8JIJOYZMnPFPF-ukF9iJYdbqgGd`)
**MCP** : `create_expense`, `list_deliveries`, `update_ingredient`

---

## EP76 — Le recomptage

> Vertical 9:16, 10 seconds, photorealistic, walk-in fridge, cold light, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A chef counts vacuum-packed steaks on a shelf out loud, pointing at each one. He reaches the end, frowns, and starts again from the beginning. Second count gives a different number. He starts a third time, now moving each pack physically to the other side of the shelf as he counts. At 6 seconds a colleague walks past and takes one. Final 2 seconds: the chef finishes his count, satisfied, unaware. Audio: cold room compressor drone, vacuum plastic crinkling, murmured counting in French, footsteps passing, plastic rustle, then counting continuing. No music.

**Hook** : `Ton inventaire du mardi.`
**Punchline VO** : « La production sort les ingrédients du stock. Automatiquement. »
**VO bloc C** : « Quand tu valides une production, avec sa quantité et sa température, les ingrédients sortent du stock tout seuls. Le stock reflète la réalité, pas ton souvenir. »

**Fonctionnalité** : validation de production et sortie de stock automatique
**Drive** : Module 5 › `12- Production, valider une production, quantité, température, note` (`1JCRKsZ3Hk50JI9_Cn_WVknci92yTuwEb`) · `15- Sortie des ingrédients du stock` (`1R39Whn8WiAr8zxH7Yb1Ive7L2FMxYvvx`)
**MCP** : `create_production_plan`, `validate_production`, `get_production_ingredients`

---

## EP77 — Le devis sur le set de table

> Vertical 9:16, 10 seconds, photorealistic, restaurant table, warm light, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A restaurant owner sits across from a couple planning a wedding. Having no notepad, he writes numbers on a paper placemat, then continues onto a second placemat, then onto a napkin. At 5 seconds he slides all three across the table toward them as a formal proposal. Final 2 seconds: the bride picks up the napkin, turns it over, and finds a coffee ring on the total. Audio: restaurant ambience, pen scratching on textured paper, paper sliding on wood, a polite "Voilà !", one uncertain "Ah.", cutlery in the background. No music.

**Hook** : `Ton devis pour le mariage de samedi.`
**Punchline VO** : « Devis, envoi, acceptation, facture. Une seule chaîne. »
**VO bloc C** : « Tu crées le devis avec ses lignes, tu l'envoies, tu suis son statut. Une fois accepté, il devient une facture sans que tu ressaisisses quoi que ce soit. »

**Fonctionnalité** : devis, statuts et bascule en facture
**Drive** : Module 3 › `3- Créer un devis` (`1vEqEBl6EYPfsXAsDkHKMKjMCFs845eQH`) · `4- Changer les statuts d'un devis` (`1tQ4Blwv-Tjz4E10rKILtkQAUjin1qtLI`) · `5- Créer une facture` (`1026gmGm615P9PAOfk4CUGaxRava0Nm6k`)
**MCP** : `create_quote`, `update_quote_status`, `create_invoice`, `update_invoice_status`

---

## EP78 — La boîte à chaussures

> Vertical 9:16, 10 seconds, photorealistic, accountant's office, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A restaurateur places a shoebox on an accountant's desk and lifts the lid. It is packed to the brim with crumpled receipts and invoices, some folded, some torn. The accountant looks into the box for a long moment without moving. At 5 seconds a single receipt escapes and drifts to the floor. Final 2 seconds: the accountant slowly puts the lid back on and slides the box six centimetres to one side. Audio: quiet office ambience, cardboard lid lifting, dense paper settling, a clock ticking, a single sheet fluttering to the floor, a cardboard slide on wood. No music.

**Hook** : `Ta comptabilité annuelle.`
**Punchline VO** : « Chaque dépense rattachée à sa livraison. Toute l'année. »
**VO bloc C** : « Chaque dépense fournisseur est enregistrée avec ses montants et rattachée à la livraison correspondante. En fin d'année, il n'y a rien à reconstituer. »

**Fonctionnalité** : dépenses fournisseurs et archivage relié aux livraisons
**Drive** : Module 3 › `7- Mes dépenses fournisseur` (`1xexncFtORGZ5oL8c-ojAAItWUz6lT_pQ`) · `8- Archivage de mes dépenses et connexion aux livraisons` (`1LKE7TtSjPJRnWVF_4-Tt89KmnudV-dcY`)
**MCP** : `create_expense`, `list_expenses`, `finance_summary`

---

## EP79 — Les quatorze cartes

> Vertical 9:16, 10 seconds, photorealistic, café counter close-up, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A customer at a counter pulls a thick stack of paper loyalty cards from his wallet and fans them out like a poker hand. He searches through them one by one, checking the stamps. Every card is partially stamped; none is complete. At 6 seconds he finds one with nine stamps out of ten, holds it up hopefully, then reads the expiry date and lowers it. Final 2 seconds: he puts them all back and pays normally. Audio: café ambience, espresso machine, cards shuffling and flicking, a hopeful "Ah !", a disappointed "Ah.", a card slipping back into a wallet. No music.

**Hook** : `Ton programme de fidélité.`
**Punchline VO** : « Un compte, tous les canaux, zéro carton. »
**VO bloc C** : « Les points se cumulent quel que soit le canal : sur place, en ligne, en livraison. Le client voit son solde et sa prochaine récompense, et toi tu vois qui revient. »

**Fonctionnalité** : fidélité multi-canal, récompenses et vue client
**Drive** : Module 7 › `12- Booster la fidélité` (`1QgM4jgAXdh1G1-Ke0ncugZvAdQ3ldkbZ`) · `13- Gérer les récompenses` (`1y3QFdo1j1Gl0vIWHt4Hd10c2MvMCy0dw`) · `19- Fidélité multi-canal` (`1A6UKoeqxb2RoILPCxBPs84iy-EWeIKNZ`) · `20- Vue client fidélité` (`18JE8aUMjo0tFGD_V1NFNfxW3svy9EIl9`)
**MCP** : `get_loyalty_program`, `get_loyalty_account`, `upsert_loyalty_reward`, `validate_redemption`

---

## EP80 — Le tiroir vide

> Vertical 9:16, 10 seconds, photorealistic, bar counter before opening, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A manager pulls open a cash drawer at the start of service. It is completely empty. He closes it, opens it again as if that might help, then blows into it the way one blows into an old game cartridge. At 5 seconds he checks under the counter, behind the till, and inside an empty mug. Final 2 seconds: he stands holding the empty drawer, looking off toward the front door where a first customer is arriving. Audio: cash drawer mechanism sliding twice, a hollow blow into plastic, hands patting under a counter, a ceramic mug lifted and set down, a shop door bell. No music.

**Hook** : `Ouverture. Fond de caisse : ?`
**Punchline VO** : « Fond déclaré, opérateur identifié, service ouvert. »
**VO bloc C** : « Tu ouvres ta session de caisse avec un fond initial et un opérateur. À partir de là, chaque encaissement est rattaché à quelqu'un. »

**Fonctionnalité** : ouverture de session de caisse et fond initial
**Drive** : Module 11 › `2- Ouvrir son fond de caisse en début de service` (`11BEZbZC9xgir-TYps_Ag-dBUXjq4o04e`) · `1- Configurer sa caisse POS, TPE et ticket` (`1hQ5RgiSyb2DGfkP_EIQ3mwWzVQOQBcOc`)
**MCP** : `open_pos_session`, `get_pos_session`

---

## EP81 — Huit calculatrices

> Vertical 9:16, 10 seconds, photorealistic, restaurant table, evening, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. Eight friends around a finished dinner table, each holding a phone calculator, all talking at once and pointing at different items on a single shared bill. One person has a pen and is drawing a diagram on the receipt. At 6 seconds someone puts a twenty-euro note down and everyone stops to look at it. Final 2 seconds: the waiter stands beside the table, terminal in hand, waiting with infinite patience. Audio: overlapping animated French chatter, phone keypad taps, a pen on paper, a banknote laid on wood, then a sudden collective silence. No music.

**Hook** : `« On peut séparer ? »`
**Punchline VO** : « Oui. Par personne, par article, par montant. »
**VO bloc C** : « Une addition, plusieurs paiements. Tu encaisses par personne ou par article, en espèces avec le rendu monnaie calculé, ou par carte. Le reste dû s'affiche à chaque étape. »

**Fonctionnalité** : addition séparée et paiements multiples
**Drive** : Module 11 › `5- Séparer une addition, multi-paiement` (`1SeLJel_btaKEnvS8W3s6u8C0-ZnjaB4t`) · `3- Encaisser une commande comptoir et table` (`1FfRiDgDtAi_ERE7oTv9yfgbkjPQRwK-T`)
**MCP** : `record_pos_payment`, `list_pos_payments`

---

## EP82 — Le centime

> Vertical 9:16, 10 seconds, photorealistic, night, closed restaurant, single overhead lamp, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. Two in the morning. A manager recounts a small pile of coins for what is clearly the fifth time, lips moving. He checks the till, lifts the drawer insert, looks underneath, shakes it. At 6 seconds he finds nothing and writes a figure on a pad. Final 2 seconds: he stares at the pad, then holds up a single one-cent coin between two fingers, defeated by it. Audio: empty restaurant reverb, coins being counted, a drawer insert lifted and dropped, a chair creak, one long breath, a single coin set on wood. No music.

**Hook** : `Il manque un centime.`
**Punchline VO** : « Le Z calcule l'écart. Toi, tu rentres chez toi. »
**VO bloc C** : « À la clôture, tu comptes tes espèces, l'écart se calcule tout seul et le rapport Z sort avec le chiffre d'affaires, les modes de paiement et la TVA. L'historique des écarts reste consultable. »

**Fonctionnalité** : clôture Z et suivi des écarts de caisse
**Drive** : Module 11 › `6- Clôturer sa caisse, le Z de caisse` (`1ht1CI-2jBkP6DdhvMdT3xVCPbzrwUU3m`) · `7- Suivre les écarts de caisse, historique` (`1XpLa01_iscSfjrfA8GkM2uEuHdDZIw4d`)
**MCP** : `close_pos_session`, `get_pos_report`

---

## EP83 — Le cri dans le vide

> Vertical 9:16, 10 seconds, photorealistic, busy professional kitchen, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A head chef at the pass shouts an order across the kitchen. Nobody reacts — the extraction hood is roaring, a mixer is running, two cooks have their backs turned. He shouts again, louder, cupping his hands. Still nothing. At 6 seconds he simply walks the plate over himself. Final 2 seconds: the moment he leaves the pass, three cooks all turn around at once and look at the empty spot where he was. Audio: overwhelming kitchen noise, extractor roar, a mixer, two muffled shouted orders swallowed by the noise, footsteps, then the noise continuing. No music.

**Hook** : `« J'AI DIT DEUX BURGERS ! »`
**Punchline VO** : « Chaque poste voit ses plats. Sans crier. »
**VO bloc C** : « Tu crées tes postes de cuisine, et chaque écran n'affiche que ses plats. En attente, en cours, prêt. La charge de chaque poste est visible d'un coup d'œil. »

**Fonctionnalité** : postes KDS et vue cuisine par poste
**Drive** : Module 9 › `1- Créer tes postes KDS` (`1NU0o445gOk4pdMf4uimNPOts3XIcR7LO`) · `2- Vue KDS par poste` (`1L83RmygIEnYQwa2ELdR7viJODqI764wD`) · `3- Gérer le KDS en direct` (`1RnmeyK_4aYgVpGKKNdPOrClzmpHw9Ljg`)
**MCP** : `update_kds_item_status`, `get_station_load`

---

## EP84 — Le QR code scotché

> Vertical 9:16, 10 seconds, photorealistic, restaurant table close-up, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A customer holds a phone over a QR code taped to a restaurant table. The code is torn across one corner and covered in three overlapping layers of yellowed sticky tape. He moves the phone closer, then further, then tilts it, then tilts the whole table slightly. At 6 seconds he gives up and looks around for a waiter. Final 2 seconds: the phone camera finally focuses — on a reflection of the ceiling light. Audio: restaurant ambience, a phone scan failure buzz repeated three times, tape crinkling, a table leg scraping, an impatient tap on the screen. No music.

**Hook** : `Commander à table.`
**Punchline VO** : « Un plan de salle, un QR par table. Ça marche. »
**VO bloc C** : « Tu dessines ton plan de salle, chaque table reçoit son QR code. Le client commande depuis sa place, et la commande part directement en cuisine. »

**Fonctionnalité** : plan de salle et commande par QR code à table
**Drive** : Module 13 › `3- Dessiner son plan de salle, QR code à table` (`1Y_TFKokdQ6-x54EmTehizW9rApt_jn75`) · Module 10 › `5- Commander par QR code` (`1z8q4btyT2yAqNIenhuvwtssyCvK2Qk9S`)
**MCP** : `create_zone`, `create_table`, `floor_plan_status`, `list_orders`

---

## EP85 — Le ballon qui se dégonfle

> Vertical 9:16, 10 seconds, photorealistic, restaurant interior, warm evening light, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A table set for eight, immaculate, with a small "Réservé" card and a helium balloon tied to a chair. Nobody is there. The camera holds, then pushes in very slowly. At 6 seconds the balloon, losing helium, sinks gently until it rests on the tablecloth. Final 2 seconds: a waiter enters frame at the far side of the room, looks at the table, and turns off one of the lights above it. Audio: quiet restaurant ambience, distant chatter from other tables, a faint balloon string rubbing on fabric, a light switch click, then quiet. No music.

**Hook** : `Table de 8. 20 h 30. Personne.`
**Punchline VO** : « No-show marqué, table libérée, soirée sauvée. »
**VO bloc C** : « Tu confirmes tes réservations, tu marques les no-shows, et la table se libère immédiatement pour la file d'attente. Une place vide ne reste pas vide. »

**Fonctionnalité** : réservations, confirmation, no-shows et libération de table
**Drive** : Module 10 › `3- Gérer et no-shows` (`11I5195HrUUPsZVqectjWhfM9f-EEo1y5`) · `1- Réservations du jour` (`1L_ewdqi9eYPYPMdzLIL-Rj3JwvEzTJQm`) · `4- Placer un client à table` (`1OPt9xLWcJHMHt-LCOM4gAfWP-I0MeaC8`)
**MCP** : `list_reservations`, `confirm_reservation`, `no_show_reservation`, `seat_waitlist`

---

## EP86 — Le téléphone que personne ne prend

> Vertical 9:16, 10 seconds, photorealistic, kitchen and pass during full service, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A wall phone rings in a restaurant at peak service. One by one, every person in frame looks at it and then looks away: a cook with both hands in a pan, a waiter with a full tray, a dishwasher with wet arms up to the elbows. At 6 seconds the ringing stops on its own. Final 2 seconds: everyone relaxes visibly — and it starts ringing again. Audio: busy service noise, an insistent landline ring cutting through it, sizzling, plates, the ring stopping, one collective exhale, then the ring restarting. No music.

**Hook** : `Trois appels manqués pendant le coup de feu.`
**Punchline VO** : « Caroline décroche. Et elle prend la réservation. »
**VO bloc C** : « Caroline répond au téléphone à ta place, prend les réservations et les commandes. Tu réécoutes les appels quand tu veux, et rien ne se perd pendant le service. »

**Fonctionnalité** : Caroline, agent IA vocale au téléphone
**Drive** : Module 13 › `1- Configurer Caroline, voix et prompts` (`1GqODoJqsP5RS8ePzb-CAwfjfSIfQ0F0n`) · `2- Réécouter ses appels et réservations` (`1AHUIPfLkUOE3P2-YjfbyggJdrsa3olRA`)
**MCP** : `list_orders` (canal agent vocal), `create_reservation`, `reservation_availability`

---

## EP87 — Les trois tablettes

> Vertical 9:16, 10 seconds, photorealistic, takeaway counter, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. Three different delivery-platform tablets sit propped side by side on a counter. They all start chiming at once, each with a different tone, each screen flashing a different colour. A single employee reaches for all three at the same time with two hands. At 6 seconds a fourth device — a phone — starts ringing beside them. Final 2 seconds: he stands with one tablet in each hand and the third one held against his chest with his chin. Audio: three distinct order-notification chimes overlapping and repeating, a phone ringtone joining, plastic tablets clacking, one desperate inhale. No music.

**Hook** : `Trois plateformes. Trois écrans.`
**Punchline VO** : « Une seule cuisine. Un seul flux. »
**VO bloc C** : « Uber Eats, Deliveroo, ta caisse tierce : tout remonte via HubRise dans un seul flux de commandes. Un écran, une file, une cuisine. »

**Fonctionnalité** : centralisation des commandes livraison via HubRise
**Drive** : Module 12 › `2- Relier Uber Eats et Deliveroo via HubRise` (`109Fn97h2rydpDX7zeHt_EFzKtZIbFa-k`) · `4- Centraliser les commandes, flux livraison` (`1Qt_omsrE2w9UqlhhlfkhwJaCjeL_ddow`)
**MCP** : `get_hubrise_status`, `list_orders`, `list_delivery_zones`

---

## EP88 — Une étoile

> Vertical 9:16, 10 seconds, photorealistic, tight portrait, restaurant back office, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. Close-up on a restaurant owner's face lit by his phone screen, smiling as he scrolls. The smile holds, then falters, then collapses entirely into a flat stare. He scrolls back up and reads the same thing again. At 6 seconds he lowers the phone slowly to the desk, screen down. Final 2 seconds: he picks it up and reads it a third time. Audio: quiet office, a finger swiping glass, a small amused hum that stops abruptly, a long silence, a phone set face-down on wood, then picked up again. No music.

**Hook** : `Un avis. Publié il y a six jours.`
**Punchline VO** : « Vu, répondu, traité. Le jour même. »
**VO bloc C** : « Tes avis Google et ceux de ton site arrivent au même endroit. Tu les modères, tu réponds, et tu vois ta note évoluer sans avoir à surveiller cinq plateformes. »

**Fonctionnalité** : centralisation, modération et réponse aux avis
**Drive** : Module 7 › `1- Débloquer les avis` (`1qKR-8QOFNaR5OIbNYKodlUB1Qmgr1CLW`) · `2- Synchro Google Avis` (`1hUQ9X4Cw75sFsyF4L8QOoxPDEGLb_8bs`) · `3- Répondre aux avis` (`1ZXZeT7GyPTkQT95XNGu8svx6OI1aUgNA`)
**MCP** : `list_reviews`, `reply_review`, `moderate_review`

---

## EP89 — Le bocal presque vide

> Vertical 9:16, 10 seconds, photorealistic, restaurant entrance counter, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A large glass jar sits on a counter beside a handwritten sign, intended for a prize draw. Inside there is exactly one folded slip of paper. The camera pushes in slowly on the single slip. At 6 seconds a hand reaches in, takes the slip out, unfolds it, and reads it. Final 2 seconds: the same hand refolds it and puts it back in the empty jar. Audio: entrance ambience, a door opening in the background, glass resonance as a hand reaches in, paper unfolding, a beat of silence, paper dropped back into glass. No music.

**Hook** : `Ton jeu concours.`
**Punchline VO** : `QR code, roue cadeaux, gagnants tracés.`
**VO bloc C** : « Tu lances ton jeu, tu diffuses le QR code, les clients jouent et laissent leurs coordonnées. Tu vois les lancers, les lots gagnés et les leads captés. »

**Fonctionnalité** : jeux concours, roue cadeaux et capture de leads
**Drive** : Module 7 › `14- Lancer un jeu concours` (`1XtJqFuUhRUQ8k1nkH7PUm_mHdy2LnT88`) · `15- QR code jeu concours` (`16BjIiFxzy9771SnWawxx0uq6jJRjgOUY`) · `16- Gagnants et historique` (`1oMHPLFz1qnx9UQlSOuieA5z1FsQ3pB2V`)
**MCP** : `list_wheel_games`, `get_wheel_stats`, `list_site_leads`

---

## EP90 — Le marc de café

> Vertical 9:16, 10 seconds, photorealistic, dim restaurant office, single warm lamp, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A restaurant manager sits alone at a desk, tilting an empty espresso cup and studying the coffee grounds inside with intense concentration, as if reading a forecast. He rotates the cup slowly, tilts his head, then nods once at something only he can see. At 6 seconds he writes a single number on a sheet of paper and underlines it twice. Final 2 seconds: he looks up at the camera with total conviction. Audio: quiet office, a clock ticking, ceramic rotating on a wooden desk, a pen underlining twice, one confident "Voilà." No music.

**Hook** : `Ta prévision pour samedi.`
**Punchline VO** : « PrediBot lit tes données. Pas ton café. »
**VO bloc C** : « PrediBot lit ton activité réelle et te sort tes prévisions, tes priorités et ce qui va coincer. Tu lui parles, il répond avec tes chiffres. »

**Fonctionnalité** : PrediBot, agent IA directeur
**Drive** : Module 14 › `1- Lire ses prévisions PrediBot` (`19KbPaohx3zwWwsG4Ud3KfJU9WlqeqIoE`) · `3- Parler à PrediBot avec nos prompts` (`10__yAAWsF5AzYJFvViRjWlSYTzIlIyBQ`)
**MCP** : `get_daily_brief`, `finance_summary`, `list_production_alerts`

---

## Tableau de couverture

| Module Académy | Épisodes |
|---|---|
| 2 — Équipe & Planning | EP61, EP62, EP63, EP64, EP65, EP66 |
| 4 — HACCP | EP67, EP68, EP69, EP70, EP71, EP72 |
| 5 — StockVision AI | EP73, EP74, EP75, EP76 |
| 3 — Comptabilité | EP77, EP78 |
| 7 — Marketing | EP79, EP88, EP89 |
| 11 — Caisse POS | EP80, EP81, EP82 |
| 9 — KDS | EP83 |
| 10 + 13 — Réservation & Caroline | EP84, EP85, EP86 |
| 12 — HubRise | EP87 |
| 14 — PrediBot | EP90 |

Le module 1 (Configuration) et le module 6 (Mon Site) ne sont pas repris ici :
ils ont déjà servi de bloc démo générique sur les saisons 1 et 2.

---

## Note de production

Le bloc D de la saison 3 se coupe dans le tutoriel Académy déjà tourné — donc
**aucun tournage supplémentaire**. Mais ces tutos durent plusieurs minutes et
montrent une interface dense. Deux règles pour que ça tienne en 11 s :

1. **Zoom, pas recadrage centré.** Cible la zone où l'action se produit (le
   bouton, le champ qui se remplit, la ligne qui change de statut), pas le centre
   de l'écran. Note le point d'entrée dans `config/demo_cuts.json`.
2. **Une seule action par vidéo.** Si le tuto montre créer *puis* modifier *puis*
   consulter l'historique, garde la création. Le reste, c'est la vidéo suivante.

Si un tutoriel n'existe pas encore pour une fonctionnalité listée ici, l'épisode
attend — ne le remplace pas par une capture d'un module voisin.
