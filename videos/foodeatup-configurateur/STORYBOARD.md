---
format: 1920x1080
message: "Le Configurateur — votre restaurant, installé en une conversation."
arc: Pain (page blanche) → Reveal agent → L'agent installe tout → Résultat dans FoodEatUp → Bénéfice/CTA
audience: nouveaux restaurateurs qui démarrent sur FoodEatUp, débordés par le paramétrage initial
music: calm reassuring corporate underscore, clean and methodical, light and optimistic, subtle
---

## Frame 1 — La page blanche

- voiceover: "Nouveau sur FoodEatUp, tout est à configurer : la carte, les zones et les tables, l'équipe, la TVA, les fournisseurs... Démarrer de zéro sur un nouvel outil, ça peut vite prendre des heures."
- duration: 10.762s
- transition_in: cut
- status: animated
- src: compositions/frames/01-blanche.html
- type: pain_point
- blueprint: overwhelm-surround
- asset_candidates: public/setup-blank.png

Image gérant devant un écran vide côté droit ; à gauche 4 fiches vides à configurer (carte, zones & tables, équipe, TVA & fournisseurs) ; tampon « DES HEURES ».

## Frame 2 — Le reveal de l'agent

- voiceover: "Voici le Configurateur, l'agent qui installe votre restaurant à votre place. Vous parlez, il paramètre."
- duration: 5.616s
- transition_in: crossfade
- status: animated
- src: compositions/frames/02-reveal.html
- type: product_intro
- blueprint: logo-assemble-lockup
- asset_candidates: public/configurateur-agent.png ; public/foodeatup-logo-mascot.png

Image agent robot côté droit ; à gauche eyebrow, logo, badge « Configurateur », sous-ligne « vous parlez, il paramètre ».

## Frame 3 — L'agent installe tout

- voiceover: "Dites simplement : installe mon restaurant. Il crée votre carte et vos catégories, dessine vos zones et vos tables, ajoute votre équipe et ses contrats, règle la TVA et vos fournisseurs — et vous confirmez à chaque étape."
- duration: 11.833s
- transition_in: crossfade
- status: animated
- src: compositions/frames/03-installe.html
- type: feature_showcase
- blueprint: grid-card-assemble
- asset_candidates: (commande + checklist d'installation, pas d'image)

Bulle commande « Installe mon restaurant » puis checklist qui se coche étape par étape : Carte & catégories, Zones & tables, Équipe & contrats, TVA & fournisseurs, Confirmation à chaque étape.

## Frame 4 — Tout est prêt dans FoodEatUp

- voiceover: "Et tout est prêt dans FoodEatUp : votre carte en ligne, votre plan de salle, votre équipe, et même votre premier relevé HACCP. En quelques minutes, au lieu de quelques jours."
- duration: 10.344s
- transition_in: push-slide LEFT
- status: animated
- src: compositions/frames/04-pret.html
- type: feature_showcase
- blueprint: grid-card-assemble
- asset_candidates: (fenêtre FoodEatUp, pas d'image)

Fenêtre FoodEatUp « Établissement prêt » : 4 cartes (Carte en ligne · 32 plats ; Plan de salle · 3 zones, 18 tables ; Équipe · 6 membres ; HACCP · 1er relevé).

## Frame 5 — Le bénéfice + CTA

- voiceover: "De zéro à prêt à servir, sans paramétrage manuel. Le Configurateur — votre restaurant, installé en une conversation."
- duration: 6.818s
- transition_in: push-slide LEFT
- status: animated
- src: compositions/frames/05-cta.html
- type: cta
- blueprint: logo-assemble-lockup
- asset_candidates: public/equipe-tablette.png ; public/foodeatup-logo-mascot.png

Image équipe prête côté gauche ; à droite 3 micro-bénéfices (De zéro à prêt, Zéro paramétrage manuel, En quelques minutes) puis logo + tagline « Votre restaurant, installé en une conversation. » + CTA « Découvrir le Configurateur ».

## Video direction

- Format 16:9 (1920×1080). Charte FoodEatUp : fond off-white #F7F9FC, texte navy #1B2A41, accent bleu #1E9BF0, vert #059669 (coches). Poppins (600-800) + Inter, fichiers locaux assets/fonts/.
- Gabarit 60/40 (contenu gauche / image droite) pour F1/F2 ; F3 = commande + checklist ; F4 = fenêtre app ; F5 = image gauche + lockup droite.
- Images 3D sur fond blanc posées directement (contain). Entrées power3.out sans overshoot, reveals calés sur la voix, hold net.
- Transitions : cut (F1) → crossfade (F2, F3) → push-slide LEFT (F4, F5). Sous-titres karaoké en bas. Musique assets/bgm/track.mp3 à 0.18 ; SFX sous la voix.
