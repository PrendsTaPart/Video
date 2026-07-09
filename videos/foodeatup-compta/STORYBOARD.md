---
format: 1920x1080
message: "FoodEatUp — votre rentabilité, sous contrôle."
arc: Pain (paperasse compta) → Reveal module → Fonctions → Deux usages Claude (OCR + Devis) → Bénéfice/CTA
audience: restaurateurs et gérants (France) qui gèrent factures, dépenses, food cost et marges
music: calm reassuring corporate underscore, clean and methodical, light and optimistic, subtle
---

## Frame 1 — Le gouffre de la compta

- voiceover: "Les factures fournisseurs qui s'empilent, les dépenses à ressaisir une par une, les food costs qu'on ne calcule jamais vraiment... et les marges, qu'on découvre bien trop tard. La comptabilité d'un restaurant, c'est un vrai gouffre de temps."
- duration: 14.289s
- transition_in: cut
- status: animated
- src: compositions/frames/01-gouffre.html
- type: pain_point
- blueprint: overwhelm-surround
- asset_candidates: public/compta-chaos.png

Image gérant débordé côté droit ; à gauche 4 fiches (factures qui s'empilent, dépenses à ressaisir, food cost jamais calculé, marges trop tard) s'accumulent ; tampon « GOUFFRE DE TEMPS ».

## Frame 2 — Le reveal du module

- voiceover: "FoodEatUp réunit toute votre comptabilité dans un seul module. Factures, fournisseurs, dépenses et food cost, au même endroit."
- duration: 7.367s
- transition_in: crossfade
- status: animated
- src: compositions/frames/02-reveal.html
- type: product_intro
- blueprint: logo-assemble-lockup
- asset_candidates: public/foodeatup-logo-mascot.png

Logo + badge « MODULE COMPTA » + sous-ligne + 3 attributs (Factures, Dépenses, Food cost).

## Frame 3 — Les fonctions du module

- voiceover: "Éditez vos devis et vos factures, suivez vos fournisseurs et vos dépenses, scannez vos factures grâce à l'OCR, et calculez le food cost et la marge de chaque recette. Votre chiffre d'affaires, vos impayés et vos marges, en un coup d'œil."
- duration: 13.453s
- transition_in: crossfade
- status: animated
- src: compositions/frames/03-fonctions.html
- type: feature_showcase
- blueprint: grid-card-assemble
- asset_candidates: public/chef-invoice-tablet.png

Image gérant+tablette côté droit ; à gauche 5 pills (Devis & factures, Fournisseurs, Dépenses & achats, OCR des factures, Food cost & marges) ; puce « CA · impayés · marge en un coup d'œil ».

## Frame 4 — Deux façons avec Claude

- voiceover: "Et tout se pilote aussi avec Claude. Donnez-lui une facture fournisseur : il met à jour le prix de vos ingrédients et recalcule vos marges. Demandez un devis pour un buffet de cinquante personnes : il estime les coûts et le rédige — dans FoodEatUp."
- duration: 13.505s
- transition_in: push-slide LEFT
- status: animated
- src: compositions/frames/04-usages.html
- type: feature_showcase
- blueprint: grid-card-assemble
- asset_candidates: public/chef-claude-assistant.png

Image gérant+assistant IA côté droit ; à gauche deux échanges Claude : OCR facture Metro → prix mis à jour + marge risotto recalculée ; devis buffet 50 pers → coûts estimés + devis créé.

## Frame 5 — Le bénéfice + CTA

- voiceover: "Moins de saisie, des marges enfin maîtrisées, une compta toujours à jour. FoodEatUp — votre rentabilité, sous contrôle."
- duration: 7.105s
- transition_in: push-slide LEFT
- status: animated
- src: compositions/frames/05-cta.html
- type: cta
- blueprint: logo-assemble-lockup
- asset_candidates: public/chef-desk-calm.png ; public/foodeatup-logo-mascot.png

Image gérant serein à son bureau côté gauche ; à droite 3 micro-bénéfices (Zéro ressaisie, Marges maîtrisées, Compta à jour) puis logo + tagline « Votre rentabilité, sous contrôle. » + CTA « Découvrir le module Compta ».

## Video direction

- Format 16:9 (1920×1080). Charte FoodEatUp : fond off-white #F7F9FC, texte navy #1B2A41, accent bleu #1E9BF0, vert #059669 (coches/validations), rouge discret pour impayés/déficit. Poppins (600-800) + Inter, fichiers locaux assets/fonts/.
- Gabarit 60/40 pour F3/F4 (contenu gauche / image droite) ; F2/F5 encadrent avec le lockup logo. Entrées power3.out sans overshoot, reveals calés sur la voix, hold net par frame.
- Les images 3D sur fond blanc (compta-chaos, chef-invoice-tablet, chef-claude-assistant) : posées directement, recadrage objet-contain. chef-desk-calm (fond bureau intégré) : contenue dans un bloc arrondi.
- Transitions : cut (F1) → crossfade (F2, F3) → push-slide LEFT (F4, F5).
- Sous-titres karaoké en bas (caption-skin de marque). Musique assets/bgm/track.mp3 bouclée à 0.18 ; SFX sous la voix.
