---
format: 1080x1080
duration: 24s
message: "Un agent qui répond et réserve."
arc: Le manque (personne ne décroche) → la conversation réelle → la preuve de compétence → la réservation qui se prend → l'intégration dans le système → la marque + CTA
audience: restaurateurs qui perdent des réservations le soir/le week-end faute de pouvoir répondre au téléphone/WhatsApp pendant le service
mode: autonomous
declination: 1080x1920 (9:16) — même storyboard, cf. table "Aspect-ratio" en fin de fichier
fps: 24
music: aucune — son design seul (notification douce, whoosh subtils sur les transitions de carte), jamais bruyant
voiceover: aucun — texte à l'écran uniquement (UI de chat + cartons Fraunces italic)
---

## Frame 1 — Personne n'a décroché

- scene: Surface Ink pleine page, champ de points 8px dense en fond (respiration lente). La ligne "Personne n'a décroché." se révèle seule, mot à mot, centrée.
- on_screen_text: "Personne n'a décroché."
- duration: 3s
- timecode: 0-3s
- transition_in: fade from black
- status: animated
- src: compositions/frames/01-ouverture.html
- type: hook
- persuasion: tension immédiate — la douleur nommée avant la solution
- beat: manque, silence
- asset_candidates: motif de points recréé en CSS (grille 8px, opacité faible, Ink sur Ink)
- motion: blueprint `titlecard-reveal` (posture: Adapt) — breather/landing beat, un mouvement restreint puis hold ; composé avec les rules `waterfall-entry` (reveal mot à mot de la ligne Fraunces) et `sine-wave-loop` (respiration lente du champ de points)

narrativeRole: Planter la douleur — un appel/message resté sans réponse — avant de montrer la solution.
keyMessage: Sans réponse, il n'y a pas de réservation.

Scene 1 (0.0–0.6s): fond Ink pur, champ de points 8px qui fade in très légèrement (respiration, pas d'animation de mouvement).
Scene 2 (0.6–2.4s): la ligne "Personne n'a décroché." apparaît en Fraunces italic, Paper, reveal mot à mot (stagger léger, sans overshoot) — seule au centre, grande échelle.
Scene 3 (2.4–3.0s): hold net, aucun mouvement — le silence est le message.

## Frame 2 — Le téléphone monte

- scene: Le téléphone (mockup) monte depuis le bas sur fond Paper avec une ombre douce. En-tête du fil : "Le Comptoir · Agent IA · en ligne". Première bulle client en vert WhatsApp entre par le bas.
- on_screen_text: en-tête "Le Comptoir · Agent IA · en ligne" ; bulle client "Bonsoir, vous avez une terrasse ? Ouvert dimanche soir ?"
- duration: 4s
- timecode: 3-7s
- transition_in: cut sur fond qui change (Ink → Paper)
- status: animated
- src: compositions/frames/02-telephone.html
- type: setup
- persuasion: crédibilité — c'est un vrai fil WhatsApp, pas une maquette abstraite
- beat: bascule, entrée en matière
- asset_candidates: mockup téléphone (composant CSS, style sobre, pas de skin iOS/Android trop marqué), icône "en ligne" (point vert petit format, toléré car statut système WhatsApp)
- motion: compose (aucun blueprint entier ne convient à une scène aussi courte) — rules `spring-pop-entrance` (montée du téléphone, arrivée de la bulle client) et `waterfall-entry` (en-tête du fil qui se pose)

narrativeRole: Poser le contexte réel — un client écrit sur WhatsApp au restaurant, un agent est en ligne.
keyMessage: La conversation se passe sur le vrai WhatsApp du restaurant.

Scene 1 (0.0–1.2s): fond Paper, le téléphone (silhouette sobre, ombre douce Ink 8%) monte depuis le bas (slide + settle power3, sans overshoot), ancré bas-centre.
Scene 2 (1.2–2.2s): l'en-tête du fil se pose en haut de l'écran du téléphone : "Le Comptoir" (Geist Bold) · "Agent IA · en ligne" (label, point vert statut).
Scene 3 (2.2–4.0s): la bulle client (vert WhatsApp officiel, coin arrondi côté gauche) spring-pop depuis le bas : "Bonsoir, vous avez une terrasse ? Ouvert dimanche soir ?" — SEULE zone verte de tout le plan.

## Frame 3 — L'agent répond

- scene: Indicateur "écrit…" puis la bulle de réponse de l'agent apparaît (surface Paper/Beige, PAS verte — c'est l'agent EatNow, pas le client). Un repère Navy glisse depuis le côté : "Depuis votre base de connaissances".
- on_screen_text: bulle agent "Grande terrasse côté jardin, service dimanche jusqu'à 23h." ; repère "Depuis votre base de connaissances"
- duration: 4s
- timecode: 7-11s
- transition_in: crossfade
- status: animated
- src: compositions/frames/03-reponse.html
- type: proof
- persuasion: preuve de compétence — l'agent connaît vraiment le restaurant (le repère cite la source)
- beat: confiance qui s'installe
- asset_candidates: aucun nouvel asset — réutilise le mockup téléphone du plan 2 (continuité du même fil)
- motion: blueprint `agent-progress-theater` (posture: Adapt) — theater d'état de travail (typing → réponse → repère) ; composé avec les rules `sine-wave-loop` (points "···" qui pulsent) et `spring-pop-entrance` (bulle agent, pill repère Navy)

narrativeRole: Montrer que l'agent répond avec une vraie information du restaurant, pas un script générique.
keyMessage: L'agent répond avec les vraies infos du restaurant (terrasse, horaires), pas une réponse robotique.

Scene 1 (0.0–1.0s): trois points "···" (indicateur de frappe) pulsent dans une bulle neutre Beige, sous la bulle client du plan précédent (le fil continue, pas de cut de contexte).
Scene 2 (1.0–2.6s): la bulle agent remplace les points — spring-pop, fond Beige/Paper (PAS vert) : "Grande terrasse côté jardin, service dimanche jusqu'à 23h."
Scene 3 (2.6–4.0s): un petit repère Navy (pill, icône base de connaissances) glisse depuis le bord droit et se verrouille à côté de la bulle agent : "Depuis votre base de connaissances" — settle sans overshoot.

## Frame 4 — La réservation se prend

- scene: Le client demande la table, l'agent confirme dans le fil ; puis la carte de réservation se plie/déploie depuis le bas du téléphone (surface Paper) avec une pastille verte "Confirmé".
- on_screen_text: carte "4 couverts · dimanche 20h30 · terrasse · table 12" ; pastille "Confirmé"
- duration: 5s
- timecode: 11-16s
- transition_in: crossfade (continuité du fil)
- status: animated
- src: compositions/frames/04-reservation.html
- type: conversion
- persuasion: la conversation devient un acte concret — c'est le pivot du film
- beat: résolution, satisfaction
- asset_candidates: aucun nouvel asset — carte de réservation en composant CSS (fold/déploiement)
- motion: compose — rules `anchored-layout-expand` (conteneur ancré qui se déploie sur un axe, la carte se plie/déploie depuis le bas) et `spring-pop-entrance` (pastille "Confirmé")

narrativeRole: Montrer le moment exact où la conversation devient une réservation ferme.
keyMessage: La demande de table est traitée et confirmée dans le même fil, sans intervention humaine.

Scene 1 (0.0–1.5s): dernier échange bref dans le fil (bulle client "demande la table" / bulle agent "confirme" — texte court, illisible en détail, le focus visuel bascule déjà vers la carte).
Scene 2 (1.5–3.5s): la carte de réservation se DÉPLIE depuis le bas du téléphone (effet de pliage — fold-out CSS 3D léger, surface Paper, coins arrondis, ombre douce) : "4 couverts · dimanche 20h30 · terrasse · table 12" (Geist Bold pour les valeurs).
Scene 3 (3.5–5.0s): la pastille "Confirmé" (vert `#3D7A58`, distinct du vert WhatsApp) spring-pop dans le coin de la carte ; hold net.

## Frame 5 — Ça tombe dans le carnet

- scene: La carte de réservation glisse le long d'une ligne Navy, sort du cadre du téléphone, et atterrit dans un plan de salle réel (le carnet EatNow). Les icônes des canaux (WhatsApp · Google · Instagram · site) convergent vers le même point d'entrée.
- on_screen_text: "Et ça tombe dans votre carnet, avec toutes les autres." (Fraunces italic)
- duration: 4s
- timecode: 16-20s
- transition_in: push/glisse le long de la ligne Navy (pas un cut — la carte EST la transition)
- status: animated
- src: compositions/frames/05-carnet.html
- type: system_proof
- persuasion: preuve d'intégration — ce n'est pas un canal isolé, tout converge au même endroit
- beat: soulagement, vue d'ensemble
- asset_candidates: mini plan de salle (grille de tables simplifiée, style EatNow), 4 icônes de canaux (WhatsApp, Google, Instagram, site — pictogrammes simples ligne Navy/Ink, PAS les couleurs de marque tierces sauf le vert WhatsApp déjà vu au plan 2)
- motion: compose — rule `svg-path-draw` (ligne Navy qui se dessine, `stroke-dashoffset`) + `center-outward-expansion` inversée (les 4 icônes de canaux convergent vers le centre au lieu d'en sortir)

narrativeRole: Prouver que cette réservation WhatsApp n'est pas un silo — elle rejoint toutes les autres réservations, tous canaux confondus.
keyMessage: Toutes les réservations (WhatsApp, Google, Instagram, site) atterrissent au même endroit dans EatNow.

Scene 1 (0.0–1.2s): la carte de réservation quitte le cadre du téléphone, guidée par une ligne Navy fine qui se dessine (draw-on, pas instantanée).
Scene 2 (1.2–2.6s): la ligne traverse l'écran, la carte rétrécit progressivement en approchant du plan de salle (perspective/scale-down cohérent, pas de saut).
Scene 3 (2.6–4.0s): la carte se pose sur la table 12 du plan de salle ; les 4 icônes de canaux convergent en même temps vers ce même point (fan-in symétrique, settle ensemble) ; la ligne Fraunces italic apparaît en overlay bas : "Et ça tombe dans votre carnet, avec toutes les autres."

## Frame 6 — Un agent qui répond et réserve

- scene: Retour à la surface Ink pleine page (bouclage avec le plan 1). Le repère EatNow (mark) se dessine trait par trait, le wordmark se pose dessous, puis le CTA et les preuves apparaissent.
- on_screen_text: "Un agent qui répond et réserve." · CTA "Demander une démo →" · preuves "24/7 · 0% commission"
- duration: 4s
- timecode: 20-24s
- transition_in: cut retour Ink (bouclage visuel avec le plan 1)
- status: animated  # PLACEHOLDER logo/wordmark en attendant le vrai kit de marque, voir SCRIPT.md § Statut assets
- src: compositions/frames/06-cta.html
- type: cta
- persuasion: clôture mémorable + preuve chiffrée + appel à l'action direct
- beat: résolution, mémorabilité
- asset_candidates: wordmark texte "EatNow" (Geist Bold, PLACEHOLDER), motif tampon recréé depuis l'image de référence (grille de carrés arrondis qui apparaissent un à un, PLACEHOLDER)
- motion: blueprint `logo-assemble-lockup` (posture: Adapt — le repère s'auto-dessine case par case au lieu d'un outline SVG classique) ; composé avec les rules `svg-path-draw`-like stagger (cases qui apparaissent une à une, index-dérivé) et `spring-pop-entrance` (wordmark, CTA pill)

narrativeRole: Refermer la boucle ouverte au plan 1 (le silence devient la marque qui répond) et convertir.
keyMessage: EatNow répond et réserve à la place de l'équipe, 24/7, sans commission.

Scene 1 (0.0–0.8s): fond Ink, champ de points identique au plan 1 (boucle visuelle volontaire).
Scene 2 (0.8–2.0s): le repère EatNow (motif tampon — grille de carrés arrondis) se dessine case par case, staggered, PAS toutes en même temps (cf. image de référence client).
Scene 3 (2.0–2.8s): le wordmark "EatNow" (Geist Bold, Paper) se verrouille sous le repère ; la ligne "Un agent qui répond et réserve." apparaît en dessous.
Scene 4 (2.8–4.0s): le CTA pill "Demander une démo →" spring-pop, avec "24/7" et "0% commission" en micro-attributs de part et d'autre ; hold final net — dernier frame de la vidéo.

### Carton générique (si un 7e temps est ajouté hors durée du film, ou en fin de hold du plan 6)
    EatNow — le système de réservation tout-en-un pour les restaurants.
    Demander une démo →
    Contact : wa.me/33651240020 · eat-now.io/solutions/reservation-whatsapp

---

## Video direction

- **Palette stricte** : Ink `#141210` (plans 1, 6) · Navy `#10386B` (repères, lignes de connexion) · Beige `#DDD6C6` (bulle agent, surfaces secondaires) · Paper `#FAF8F2` (téléphone, cartes, texte sur Ink) · Confirmé `#3D7A58` (pastille uniquement). **Le vert WhatsApp officiel n'apparaît que dans la bulle client des plans 2 et 4** — jamais ailleurs, jamais comme accent de marque.
- **Typo** : Geist Bold pour tous les titres/labels/UI (tracking −0.04em) · Fraunces italic réservée aux 2 lignes émotionnelles (plans 1 et 5) — jamais pour de l'UI ou des labels.
- **Motif** : champ de points 8px en fond, densité qui varie par surface (dense sur Ink, quasi invisible sur Paper) — jamais décoratif au point de nuire à la lisibilité du texte.
- **Registre** : sobre, retenu, jamais "waouh" — le calme EST la promesse (un agent qui gère sans bruit). Entrées `power3.out` sans overshoot sur les éléments UI ; le seul `spring-pop` net est réservé aux moments de preuve (bulle client qui arrive, pastille Confirmé, repère EatNow).
- **Continuité de fil** : les plans 2, 3, 4 sont un seul fil de conversation continu — pas de cut dur entre eux, toujours crossfade ou continuité directe du même mockup téléphone.
- **Rythme des transitions** : fade (P1) → cut (P1→P2, bouclage inverse en P6) → crossfade (P2→P3→P4) → glisse-le-long-de-la-ligne (P4→P5, la carte EST la transition) → cut retour Ink (P5→P6).
- **Son** : notification douce sur l'arrivée de chaque bulle (P2, P3), whoosh subtil sur le pliage de la carte (P4) et sur la glissade le long de la ligne Navy (P5), signal calme sur le dessin du repère (P6). Jamais de musique identifiée dans le brief — à confirmer avec le client avant rendu si un lit sonore est souhaité.
- **Sous-titres** : le brief demande une variante "avec" et "sans" sous-titres — ici il n'y a pas de voix off, donc "sous-titres" = la répétition texte du contenu déjà affiché à l'écran (accessibilité), pas un rail karaoké classique. À clarifier avec le client si besoin d'un vrai texte alternatif screen-reader plutôt qu'un rail visuel redondant.

## Aspect-ratio (1:1 → 9:16)

| Plan | 1:1 (master) | 9:16 (déclinaison) |
|---|---|---|
| P1 — Ouverture | ligne centrée, grande échelle | identique, ligne réduite pour tenir en largeur |
| P2-P4 — Téléphone/fil | mockup centré ~70% largeur | mockup élargi ~85% largeur, occupe plus de hauteur |
| P5 — Carnet | ligne Navy diagonale courte | ligne Navy verticale, plan de salle en bas de cadre |
| P6 — CTA | repère + wordmark + CTA empilés centrés | identique, empilement vertical déjà naturel |

## Points à valider avant rendu final

1. **Recevoir le vrai kit de marque** (zip non corrompu) pour remplacer le wordmark et le motif tampon placeholder.
2. **Vendorer Geist Bold et Fraunces italic** dans `assets/fonts/` (aucune des deux n'est actuellement dans le repo).
3. **Confirmer l'absence de musique** — le brief ne mentionne que du son design, à valider que c'est un choix assumé et pas un oubli.
4. **Valider le mockup téléphone** — style sobre à définir (pas de skin OS trop marqué) pour rester neutre marque.
