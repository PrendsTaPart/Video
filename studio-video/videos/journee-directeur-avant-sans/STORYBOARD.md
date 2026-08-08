---
format: 1920x1080
duration: 80s
message: "Sept logiciels qui ne se parlent pas coûtent plus cher — en temps et en argent — que le problème qu'ils étaient censés résoudre."
arc: story-explainer
audience: restaurateurs / gérants indépendants — public marketing FoodEatUp
mode: autonomous
music: none
---

## Video direction

**Palette system** (from `frame.md`, roles as hand-corrected in Step 2 — see `BRIEF.md`): `bg-primary` `#EDEEF0` is the ground on every frame except Frame 8. `text-primary` `#3A3F45` (anthracite) is every piece of reading text. `line` `#8A9099` (gray) is decoration only — hairlines, the broken-line motif, tab-bar chrome, dashed connectors — **never** text. `accent`/`text-secondary` (muted anthracite, `rgba(58,63,69,0.70)`) is chrome labels and secondary text. `alert` `#D64545` (red) is reserved **exclusively** for the friction grammar: crosses, empty-state marks, the loss counter, the refrain numerals — never a default UI color. Frame 8 is the one exception in the whole film: full charter break to FoodEatUp marine `#1B2A41` + white + the real brand blue logo.

**Motion grammar + reveal model** — `power3` long-tail settle on every entrance (`fromTo`, never a CSS starting state); no `back.out` / `bounce.out` / `elastic.out` anywhere. Every frame reveals its pieces on their spoken cue (word timings are in each frame's packet) — nothing sits on screen before the VO reaches it, and Frame 3 / Frame 5 especially spread their reveals across the full duration rather than resolving early. A silent frame (Frame 8) paces to the beat instead of the VO, same discipline. During a hold, the only sanctioned aliveness is a low-amplitude **subtle jitter** (`sine-wave-loop`) — no breathing, no drifting camera, no back-half pan/push.

**Rhythm / held-frame allocation** — Frame 3 (TabChaos) is the sustained-motion centerpiece: it never fully stops until its last ~2s. Frame 6 (the refrain) is the deliberate stillness peak of the film — a ~3.5s dead-still hold on "deux.", the longest held beat in the whole piece, landing the refrain by contrast against five busier frames before it. Frame 7 closes calm and held. Frame 8 is two restrained title beats, mostly still — the exhale after Frame 6/7.

**Negative list** — no FoodEatUp color or logo anywhere except Frame 8. No real browser chrome, no OS window controls, no favicons, no real spreadsheet grid styling — every "software" surface in Frames 2-4 is deliberately flat and generic (gray hairline rectangles only), never a reconstruction of an identifiable product. No green checkmarks anywhere in the film — friction is always a red cross / an empty outlined box / a gray "?". No bouncy easing, ever. No lazy breathing, no back-half camera drift or push. No infinite/looping motion. No single-figure price — only the "350–900 €/mois" range. The broken-line motif never resolves into one continuous joined line, in any frame, at any time (Frame 8 is a different visual language entirely and carries no broken-line requirement). No `sfx:` cues are named on any frame — HeyGen's SFX/BGM catalog is unavailable in this environment (see `BRIEF.md` Step 0); a "desynchronized overlapping notifications" bed was the brief's ideal but is undocumented-as-missing rather than faked with an invented placeholder tone.

**Continuity** — Frames 2, 3, and 4 share one visual stage: a generic workstation ground with the same 7-tab bar anchored top-of-frame (built once in Frame 1, echoed faintly in Frame 2, fully active in Frame 3, faintly echoed again in Frame 4) so the three read as one continuous morning rather than three unrelated slides. Frames 2→3→4 share the `push-slide LEFT` transition for this reason (chronological progression); Frame 1 opens on `cut` (mandatory, no prior frame); Frame 5→6 uses `crossfade` (a layer/atmosphere shift into the climax); Frame 6→7 uses `cut` (echoing the refrain's own internal hard-cut signature); Frame 7→8 uses `cut` (the deliberate, total palette break into the brand world).

---

## Frame 1 — Sept heures

- scene: la salle est vide et sombre ; sept onglets de navigateur génériques apparaissent en haut du cadre, un par un, puis une ligne de mots de passe et une pile de factures d'abonnement
- voiceover: "Sept heures. La salle est vide. Mes écrans, eux, sont déjà pleins. Sept onglets ouverts. Sept mots de passe. Sept factures d'abonnement — chaque mois."
- duration: 11.546s
- transition_in: cut
- status: animated
- src: compositions/frames/01-sept-heures.html
- type: hook
- persuasion: Contraste (salle vide / écrans pleins) + énumération martelée ("sept")
- beat: reconnaissance résignée
- blueprint: kinetic-type-beats (Adapt)
- focal: le compte "Sept" qui revient trois fois (heures / onglets / factures)
- roles: numéral "7"/tab-row/invoice-stack = foreground subject (successif) · ligne brisée basse = background · dots de mots de passe = supporting

narrativeRole: Ouvre sur le contraste entre le calme du restaurant et la charge invisible des outils — pose l'énigme numérique avant le service.
keyMessage: Avant même d'ouvrir, le gérant jongle déjà avec sept logiciels.

Adapt: on garde la structure "beats de type" de `kinetic-type-beats` (chaque "Sept" est son propre beat) mais on l'habille d'éléments d'interface génériques (tab-row, dots, factures) plutôt que de texte pur — la ligne brisée du système "sans" sert de fond continu.

Scene 1 (0.0–1.0s): canvas nu, fond `bg-primary` seul ; un unique segment de ligne grise bas dans le cadre (la ligne brisée, immobile). Rien d'autre — on attend "Sept".
Scene 2 (1.0–2.3s, cue "Sept heures. La salle est vide."): un numéral anthracite "7H" spring-pop (power3, pas de rebond) en haut à gauche, discret ; un petit label "la salle est vide" apparaît en per-word staggered reveal juste dessous.
Scene 3 (2.3–4.7s, cue "Mes écrans, eux, sont déjà pleins."): une grappe de rectangles plats génériques ("écrans", sans chrome, sans favicon) glisse depuis la droite et occupe les deux tiers droits du cadre — layer-reveal, un rectangle toutes les 2-3 mots.
Scene 4 (4.7–7.6s, cue "Sept onglets ouverts. Sept mots de passe."): une rangée de 7 onglets génériques (rectangles fins gris, un seul actif en soulignement anthracite) se construit de gauche à droite au rythme du mot "Sept" (cluster→outward expansion) ; une rangée de 7 points (mots de passe) apparaît dessous en sync avec "mots de passe".
Scene 5 (7.6–10.53s, cue "Sept factures d'abonnement — chaque mois."): une pile de cartes plates ("factures") s'évase en bas à droite, un petit label "× 7" en value-scaled counter atterrit à côté.
Scene 6 (10.53–11.546s): hold — tout se fige ; seul un jitter discret anime la rangée d'onglets. Sortie = transition harnais (cut) vers Frame 2.

## Frame 2 — Deux logiciels qui s'ignorent

- scene: deux panneaux génériques face à face (un "logiciel de stock", une "caisse"), reliés par un connecteur en pointillés qui n'aboutit jamais ; un point d'interrogation rouge clignote au milieu du vide
- voiceover: "Mon logiciel de stock ne sait pas ce que ma caisse a vendu hier soir. Les deux ne se parlent pas. Alors je fais le pont. À la main."
- duration: 8.333s
- transition_in: push-slide LEFT
- status: animated
- src: compositions/frames/02-deux-logiciels.html
- type: pain_point
- persuasion: Chaîne causale rompue (A ne mène pas à B) + concrétisation du "pont" à venir
- beat: friction et perplexité
- blueprint: comparison-split (Adapt)
- focal: le connecteur en pointillés qui échoue + le "?" rouge dans le vide
- roles: panneau "logiciel de stock" (gauche) / panneau "caisse" (droite) = foreground subject pair · connecteur pointillé = supporting · "?" rouge = foreground subject (climax du frame) · rangée d'onglets (écho très faible, continuité de plateau) = background

narrativeRole: Nomme la friction concrète et centrale du film — deux outils cloisonnés qui devraient parler la même langue — et prépare le geste montré au Frame 3.
keyMessage: Le stock et la caisse ne communiquent pas ; c'est lui qui fait le lien.

Adapt: on garde le tilt mirroré d'entrée de `comparison-split` (les deux panneaux arrivent en miroir depuis les bords opposés) ; au lieu du badge-pill qui ponctue chaque carte, c'est un connecteur qui échoue au milieu, et le "pop" final est un "?" rouge dans le vide plutôt qu'un badge de validation.

Scene 1 (0.0–1.0s, cue "Mon logiciel"): canvas nu, écho très faible (8% opacité) de la rangée d'onglets de Frame 1 tout en haut (continuité de plateau) ; le panneau gauche "mon logiciel de stock" (rectangle hairline, label générique, icône boîte abstraite) glisse depuis le bord gauche avec un tilt 3D qui s'aplatit (signature comparison-split, settle amorti, sans rebond).
Scene 2 (1.0–3.81s, cue "de stock ne sait pas ce que ma caisse a vendu hier soir."): le panneau droit "ma caisse" (icône ticket abstraite) entre en miroir depuis la droite, même mécanique de tilt-settle, sur son propre mot.
Scene 3 (3.81–5.31s, cue "Les deux ne se parlent pas."): un connecteur pointillé gris se dessine lui-même (SVG self-draw) d'un panneau à l'autre — il s'arrête net avant le milieu, un espace visible ne se referme jamais.
Scene 4 (5.31–7.13s, cue "Alors je fais le pont. À la main."): un "?" rouge (`alert`) spring-pop (power3, petite échelle, pas de rebond) exactement dans l'espace où le connecteur échoue — seul élément rouge du frame.
Scene 5 (7.13–8.33s): hold — panneaux, connecteur et "?" figés ; jitter discret sur le "?" uniquement. Sortie push-slide LEFT vers Frame 3.

## Frame 3 — TabChaos (le pont à la main)

- scene: LE plan clé — sept onglets génériques en haut d'un même poste de travail ; un curseur fait l'aller-retour entre un onglet et un tableur au centre, recopiant un chiffre à chaque passage, au moins 3 allers-retours à un rythme de ~1,2s
- voiceover: "Tous les lundis. J'ouvre l'onglet du stock. Je note un chiffre. Je change d'onglet. Je le recopie dans un tableur. Encore. Et encore."
- duration: 14.028s
- transition_in: push-slide LEFT
- status: animated
- src: compositions/frames/03-tabchaos.html
- type: feature_showcase
- persuasion: Démonstration (le mécanisme tourne devant nous) + balisage ("j'ouvre… je note… je recopie… encore")
- beat: lassitude tranquille, presque mécanique
- blueprint: cursor-ui-demo (Adapt)
- focal: le curseur + le chiffre qu'il transporte
- roles: rangée de 7 onglets (haut) = background/chrome · grille "tableur" générique (bas, cellules plates grises, aucun style de tableur réel) = foreground subject · curseur + chiffre transporté = foreground subject (hero) · pastilles de comptage (I / II / III) = supporting

narrativeRole: LE plan signature du film — montre littéralement le "pont à la main" nommé au Frame 2 : un rituel manuel, répétitif, hebdomadaire, qui devrait être automatique.
keyMessage: Ce qu'un logiciel unique ferait en un instant, il le refait à la main, chaque lundi.

Adapt: on garde la mécanique "curseur pilote une UI reconstruite" de `cursor-ui-demo`, mais l'UI reconstruite est délibérément générique (aucun chrome de navigateur réel, aucune grille de tableur identifiable) et le geste n'est jamais productif — c'est une recopie manuelle en boucle, pas un workflow qui "marche bien". Le premier aller-retour est lent et démonstratif (la phrase le décrit en détail) ; les deux suivants ("Encore.", "Et encore.") sont compressés à ~1,2s pour matérialiser le rythme exact demandé par le brief.

Scene 1 (0.0–1.58s, cue "Tous les lundis."): même plateau que Frame 2 mais complet — rangée de 7 onglets active en haut, grille "tableur" plate au centre-bas, curseur immobile posé sur l'onglet 1. Un label "chaque lundi" apparaît en haut à gauche, per-word.
Scene 2 (1.58–4.01s, cue "J'ouvre l'onglet du stock."): le curseur (flèche plate générique, aucun style OS) se déplace et clique l'onglet 1 (cursor-click-ripple, ripple minuscule) — l'onglet s'active (soulignement anthracite, jamais de couleur de marque) et son panneau révèle un chiffre en gras anthracite (ex. "128"), entrée `fromTo`, sans rebond.
Scene 3 (4.01–5.77s, cue "Je note un chiffre."): un cercle fin `alert` (rouge, usage restreint et intentionnel — "voici le chiffre à retenir") se dessine autour du chiffre puis s'efface, laissant le chiffre en anthracite normal.
Scene 4 (5.77–7.57s, cue "Je change d'onglet."): le curseur traverse le cadre vers la grille "tableur" ; l'onglet 1 se désactive (le soulignement s'éloigne avec lui).
Scene 5 (7.57–10.31s, cue "Je le recopie dans un tableur."): le chiffre se tape lui-même caractère par caractère dans une cellule surlignée de la grille (type-on avec caret) ; une pastille de comptage "I" apparaît en bas à droite (supporting, couleur `line`) — fin de l'aller-retour n°1.
Scene 6 (10.31–11.04s, cue "Encore."): aller-retour n°2, compressé (~0,73s pour le geste complet, cadence proche de 1,2s avec le suivant) : le curseur revient d'un coup sur l'onglet 1 (hard-cut / flash sur le nouveau chiffre affiché), pastille "II" apparaît.
Scene 7 (11.10–12.02s, cue "Et encore."): aller-retour n°3, même cadence rapide ~1,2s : curseur → onglet 1 (nouveau chiffre en flash) → grille (le chiffre se tape), pastille "III" apparaît — trois pastilles visibles au total, ≥ 3 allers-retours conformes au brief.
Scene 8 (12.02–14.028s): hold — les trois pastilles et le dernier chiffre recopié restent figés ; les 6 autres onglets, jamais touchés, restent silencieux en arrière-plan (la preuve visuelle qu'un seul onglet sert vraiment). Jitter discret sur le curseur uniquement. Sortie push-slide LEFT vers Frame 4.

## Frame 4 — La commande au flair

- scene: même poste de travail générique (le bandeau d'onglets reste en haut, cohérence de plateau avec Frame 3) ; un message type SMS générique se tape lettre par lettre sur un fond neutre, sans aucun graphique de prévision — juste un cadre vide marqué d'un "?" gris là où une courbe devrait être
- voiceover: "La commande fournisseur, je la passe au flair. Par SMS. À sept heures. Pas de prévision. Pas de données croisées. Juste l'habitude."
- duration: 10.031s
- transition_in: push-slide LEFT
- status: animated
- src: compositions/frames/04-commande-flair.html
- type: feature_showcase
- persuasion: Concrétisation + contre-exemple (l'absence de prévision, l'absence de croisement de données)
- beat: résignation pragmatique
- blueprint: typewriter-reveal (Adapt)
- focal: le message générique qui se tape + le cadre de prévision vide
- roles: bulle de message générique (gauche) = foreground subject · cadre vide + "?" gris (droite) = foreground subject (climax du frame, en `line`, pas en `alert` — c'est une absence, pas une alerte) · rangée d'onglets (écho faible) = background

narrativeRole: Étend la même cause racine (les outils cloisonnés) à une deuxième décision quotidienne — la commande fournisseur se fait sans aucune donnée croisée.
keyMessage: Sans outils reliés, même une commande se décide à l'instinct, pas aux chiffres.

Adapt: la mécanique de `typewriter-reveal` (une ligne se tape comme un humain le ferait) porte le message générique ; on ajoute un second élément (le cadre de prévision vide) que le blueprint de base n'a pas, pour porter la seconde moitié de la phrase — reveals toujours cadencés au VO, jamais les deux au même instant.

Scene 1 (0.0–1.0s): fond neutre, écho très faible de la rangée d'onglets en haut ; contour de bulle de message générique vide au centre-gauche, caret clignotant, en attente.
Scene 2 (1.0–3.15s, cue "La commande fournisseur, je la passe au flair."): le texte se tape caractère par caractère dans la bulle (type-on avec caret).
Scene 3 (3.15–4.71s, cue "Par SMS. À sept heures."): un petit horodatage générique apparaît sous la bulle (supporting, anthracite atténué) — renforce "aucune identité d'appli, juste un message".
Scene 4 (4.71–7.53s, cue "Pas de prévision. Pas de données croisées."): un rectangle en pointillés (un graphique qui n'existe pas) apparaît à droite, 40% de la largeur — d'abord le contour ("Pas de prévision"), puis un grand "?" gris centré à l'intérieur qui spring-pop (power3) sur "données croisées".
Scene 5 (7.53–8.73s, cue "Juste l'habitude."): la bulle et le cadre vide reçoivent chacun un très fin trait `alert` en soulignement (discret, pas un accent dominant) — comme deux éléments "non vérifiés".
Scene 6 (8.73–10.031s): hold — tout se fige ; jitter discret sur le "?" uniquement. Sortie push-slide LEFT vers Frame 5.

## Frame 5 — Le compteur de pertes

- scene: un compteur de pertes construit sous nos yeux — 7 abonnements, un nombre de doubles saisies qui grimpe, des minutes perdues qui s'accumulent, puis une fourchette de coût (jamais un chiffre unique) ; tous les chiffres en rouge d'alerte sur fond neutre, ligne brisée en fond qui ne se referme jamais
- voiceover: "Sept abonnements à payer. Des doubles saisies, chaque semaine. Des minutes qui s'accumulent. Et un coût que je ne connais qu'en fourchette : entre 350 et 900 euros par mois."
- duration: 12.069s
- transition_in: crossfade
- status: animated
- src: compositions/frames/05-compteur-pertes.html
- type: social_proof
- persuasion: Preuve statistique + règle de trois (abonnements / doubles saisies / minutes) + fourchette plutôt que chiffre unique (rigueur, pas de prix attribué à un tiers)
- beat: malaise qui monte
- blueprint: dataviz-countup (Reproduce)
- focal: le compteur de pertes (empilement de 3 stats + la fourchette finale)
- roles: 3 lignes de stat (abonnements / doubles saisies / minutes) = foreground subject · chip de fourchette "350–900 €/mois" = foreground subject (climax) · ligne brisée basse = background

narrativeRole: Chiffre l'addition invisible des frames précédents — transforme la friction ressentie en un fait mesurable qui prépare le refrain.
keyMessage: La désynchronisation a un coût réel, et personne ne le voit tant qu'il n'est pas compté.

Reproduce: le compteur remplit exactement le rôle du count-up/ring de `dataviz-countup` — un empilement de stats traversé jusqu'à un chiffre-hero, ici la fourchette finale plutôt qu'un chiffre unique (contrainte du brief).

Scene 1 (0.0–1.59s, cue "Sept abonnements à payer."): fond nu, fin segment de ligne brisée bas (background, motif filé). Une première ligne de stat entre en haut : "7" (`alert`, value-scaled counter, montée rapide 0→7) + label "abonnements" en anthracite.
Scene 2 (1.59–3.77s, cue "Des doubles saisies, chaque semaine."): une deuxième ligne de stat révèle dessous — un compteur qui grimpe (stat-bars-and-fills) jusqu'à une valeur modeste illustrative, label "doubles saisies / semaine".
Scene 3 (3.77–5.53s, cue "Des minutes qui s'accumulent."): une troisième ligne de stat révèle, un value-scaled counter qui continue de grimper (suggère l'accumulation continue), label "minutes perdues / semaine".
Scene 4 (5.53–8.22s, cue "Et un coût que je ne connais qu'en fourchette :"): les trois lignes se compressent légèrement vers le haut (la mise en page évolue) pour faire de la place ; un contour de chip vide se dessine lui-même (SVG self-draw) en bas, en attente.
Scene 5 (8.22–10.27s, cue "entre 350 et 900 euros par mois."): "350" et "900" atterrissent ensemble dans le chip (jamais l'un sans l'autre), bordure et texte en `alert` rouge, label "€ / mois" en dessous en anthracite atténué — le climax du compteur.
Scene 6 (10.27–12.069s): hold — l'empilement complet des stats + le chip de fourchette restent visibles ensemble (l'addition assemblée) ; jitter discret sur le chip uniquement. Sortie crossfade vers Frame 6.

## Frame 6 — Le refrain

- scene: cadre nu, un seul mot à la fois ; "7" énorme qui se fige puis, sur un cut sec, devient "2" — plus rien d'autre à l'écran
- voiceover: "Le pire ? Je paie sept abonnements. Mon équipe en utilise deux."
- duration: 7.576s
- transition_in: cut
- status: animated
- src: compositions/frames/06-refrain.html
- type: branding
- persuasion: Distillation (compresser tout le film en une ligne) — le refrain de la série
- beat: ironie plate, conviction
- blueprint: kinetic-type-beats (Reproduce)
- focal: le "7" qui devient "2"
- roles: numéral géant = foreground subject unique · rien d'autre à l'écran — le vide autour du chiffre EST le message

narrativeRole: Le refrain de toute la série "SANS FoodEatUp" — une ligne qui condense en une phrase tout ce que les frames précédents viennent de montrer.
keyMessage: Sept abonnements payés ; deux réellement utilisés — l'absurdité chiffrée d'un seul coup.

Reproduce: le "in-place token cycle" de `kinetic-type-beats` EST le mécanisme de ce frame — une position fixe, un seul slot qui change (7 → 2) par cut sec, jamais par fondu. C'est le frame le plus immobile du film — la tenue de ~3,5s sur "deux." est délibérée.

Scene 1 (0.0–0.68s, cue "Le pire ?"): canvas totalement vide. Un petit label anthracite "le pire ?" apparaît en haut, discret, per-word.
Scene 2 (0.68–2.32s, cue "Je paie sept abonnements."): un "7" géant (`alert`, dominant, centré ~0,42×hauteur) spring-pop (power3, sans rebond) — seul élément hero du cadre ; un label "abonnements payés" reste tranquille dessous en anthracite.
Scene 3 (2.32–4.08s, cue "Mon équipe en utilise deux."): le "7" hard-cut (flash word-swap, LA signature du blueprint — un cut instantané, jamais un fondu) vers "2", même position, même échelle, toujours `alert` ; le label bascule au même instant vers "réellement utilisés" (in-place token cycle synchrone).
Scene 4 (4.08–7.576s): hold total — le "2" et son label restent figés ~3,5s, la tenue la plus longue du film (délibérée — c'est le moment où le film demande au spectateur de s'asseoir avec le chiffre). Jitter à peine perceptible au maximum. Aucun panoramique, aucune dérive. Sortie cut vers Frame 7 (fait écho au hard-cut interne du frame).

## Frame 7 — Le vrai chiffre

- scene: cadre calme, presque vide ; la ligne brisée du début revient une dernière fois, toujours discontinue, ne se referme jamais ; une phrase se pose au centre et tient
- voiceover: "Le vrai chiffre du mois ? Je ne le saurai que dans six semaines. Le temps que quelqu'un, quelque part, recopie tout ça à la main."
- duration: 10.919s
- transition_in: crossfade
- status: animated
- src: compositions/frames/07-vrai-chiffre.html
- type: cta
- persuasion: Rappel (renoue avec le "je ne sais pas" du Frame 1-2) + généralisation
- beat: clarté résignée
- blueprint: titlecard-reveal (Reproduce)
- focal: la phrase de clôture (3 lignes)
- roles: les 3 lignes de texte = foreground subject · ligne brisée = background (dernière apparition du film)

narrativeRole: Referme le film sur l'absurdité du système plutôt que sur une solution — la dernière image du monde "SANS", juste avant la bascule de marque.
keyMessage: Sans données reliées, le vrai coût du mois reste inconnu bien après qu'il compte.

Reproduce: `titlecard-reveal` EST le calme du breather — un seul mouvement restreint (slide-up crossfade) répété pour chacune des 3 lignes, puis une tenue immobile.

Scene 1 (0.0–1.53s, cue "Le vrai chiffre du mois ?"): la ligne brisée (dernière apparition, toujours discontinue) est visible, immobile, en fond. Une première ligne de texte glisse/fond vers le haut (slide-up crossfade), centrée ~0,42×hauteur.
Scene 2 (1.53–3.74s, cue "Je ne le saurai que dans six semaines."): une deuxième ligne révèle sous la première (per-word staggered reveal, même mouvement restreint) — "six semaines" reçoit un très léger surcroît de graisse (jamais de couleur) pour l'emphase.
Scene 3 (3.74–7.42s, cue "Le temps que quelqu'un, quelque part, recopie tout ça à la main."): une troisième ligne, plus petite, révèle sous les deux premières — écho direct de "à la main" (Frame 3).
Scene 4 (7.42–10.919s): hold — les 3 lignes + la ligne brisée restent figées ~3,5s. Jitter discret uniquement. Dernier frame du monde "sans" — sortie crossfade vers la rupture de palette du Frame 8.

## Frame 8 — Carte de marque

- scene: SEUL moment où la charte FoodEatUp réapparaît — fond marine plein cadre, glow ambiant ; le texte "Avec FoodEatUp, une seule application." se pose, puis une VRAIE capture du tableau de bord FoodEatUp (en couleur, `productions-dashboard.png`) apparaît comme preuve concrète, puis "Et si c'est encore trop, vous parlez à Jarvis." apparaît sous elle ; le logo FoodEatUp (public/foodeatup-logo.png) clôt le cadre
- voiceover:
- duration: 5s
- transition_in: cut
- status: animated
- src: compositions/frames/08-carte-marque.html
- type: branding
- persuasion: Contraste (sept outils → une seule application) + preuve concrète (vraie capture produit) + adresse directe
- beat: résolution calme
- blueprint: titlecard-reveal (Reproduce, chain compressée en un seul frame)
- focal: les deux lignes de la carte + la capture produit + le logo
- roles: ligne 1 / capture produit / ligne 2 = foreground subject successif · logo FoodEatUp = foreground subject (résolution finale) · glow ambiant + fond marine plein cadre = background
- asset_candidates: public/foodeatup-logo.png — logo horizontal FoodEatUp (mascotte bleue, fond transparent), réservé exclusivement à cette carte finale ; public/foodeatup-product-dashboard.png — vraie capture d'écran du tableau de bord "Mes productions" (assets/brand/product-screenshots/productions-dashboard.png), réservée exclusivement à cette carte finale, ajoutée suite au retour utilisateur post-rendu (voir BRIEF.md)

narrativeRole: Bascule hors du monde "SANS" — seul cadre de tout le film où la marque, sa couleur, son nom ET son vrai produit sont autorisés à apparaître.
keyMessage: Une seule application, bien réelle, remplace les sept ; et au-delà, un assistant (Jarvis) reste disponible.

Reproduce (silencieux — cadencé au battement, pas au VO, cf. `visual-design.md` sur les frames muets) : `titlecard-reveal` tourne ici comme une chaîne de cartes compressée en UN seul frame (2-3 cartes normalement séparées, ici 2 beats de texte + 1 beat de logo, seams internes en cut dur) plutôt que sur plusieurs frames distincts — cohérent avec le catalogue de coupes internes (`cut-catalog.md`).

Scene 1 (0.0–0.3s): cut dur depuis le monde anthracite-sur-blanc de Frame 7 vers un fond marine `#1B2A41` plein cadre, totalement vide un instant — la rupture de palette EST l'impact.
Scene 2 (0.3–1.8s): ligne 1 "Avec FoodEatUp, une seule application." glisse/fond vers le haut en blanc, centrée ~0,42×hauteur (mouvement restreint, power3).
Scene 3 (1.8–3.3s): ligne 2 "Et si c'est encore trop, vous parlez à Jarvis." révèle sous la ligne 1, même mouvement, au battement.
Scene 4 (3.3–5.0s): le logo FoodEatUp (`public/foodeatup-logo.png`) se pose sous les deux lignes (spring-pop discret, power3, sans rebond) et tout tient jusqu'à la fin — seul vrai exit du film (frame final).
