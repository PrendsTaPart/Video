# Tutoriel — Créer sa fiche plat pour production FoodEatUp

Module HACCP, écran « Production » → « + Créer un plat ». Rush unique et continu
(87,44 s) : depuis l'accueil, ouverture du module Production, création d'un plat
« Pizza margaritta » avec son ingrédient (Farine, 0,5 g), sa date/heure de
production, sa durée de vie, la quantité à produire (10) et une photo, puis
validation — le plat apparaît aussitôt dans la liste avec son prix et ses
allergènes détectés.

## Voix off (9 lignes) — toutes ElevenLabs Adam (quota reconstitué)

| # | Texte | Durée | Segment |
|---|---|---:|---|
| N0 | Créer une fiche plat pour la production, ça se fait en quelques clics. | 3,47 s | intro + A/B |
| N1 | Direction Production, puis Créer un plat : donnez-lui un nom, comme Pizza margaritta. | 5,02 s | D/E — ouverture + nom |
| N2 | Ajoutez ses ingrédients : recherchez, sélectionnez, et précisez la quantité de chacun. | 4,96 s | F — ingrédients |
| N3 | Renseignez la date de production, la durée de vie et la quantité à produire. | 3,94 s | G — quantités et dates |
| N4 | Une photo du plat termine la fiche, utile pour votre équipe en cuisine. | 4,18 s | H — photo |
| N5 | Cliquez sur Créer la production : votre plat est prêt, tracé et planifié. | 4,68 s | I/J — validation + résultat |
| N6 | Vous pouvez aussi le faire depuis Claude : copiez ce prompt, remplacez les crochets. | 4,41 s | étages 1+2 (réutilisé) |
| N7 | Collez-le dans la conversation : votre plat est créé et sa production planifiée en quelques secondes. | 5,38 s | étage 3 |
| N8 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | 5,02 s | carte de fin (CTA, réutilisé) |

N6/N8 réutilisés tels quels (octet-identiques) depuis `foodeatup-produits-tuto/vo/`
— texte générique, zéro crédit ElevenLabs dépensé. N0/N1/N2/N3/N4/N5/N7 générés
fraîchement (quota ElevenLabs reconstitué depuis le tutoriel précédent, voix
Adam Instructor `TGAegA0zNRi8I6nUdq3i`).

## Découpage

| Seg | Source | Sortie | Contenu |
|---|---|---:|---|
| intro | carte | 2,60 s | CRÉER SA FICHE PLAT POUR PRODUCTION |
| A | 0,50 → 4,00 | 2,20 s | accueil, tuiles rapides (Températures/Traçabilité/Plan de nettoyage/Production) |
| B | 4,00 → 4,35 | 0,90 s | **zoom-punch** sur la tuile Production (1556, 660) |
| C | 4,60 → 8,00 | 2,00 s | page « Production haccp », état vide |
| D | 8,00 → 8,35 | 0,90 s | **zoom-punch** sur + Créer un plat (1697, 313) |
| E | 8,60 → 28,00 | 5,00 s | modale : nom « Pizza margaritta », catégorie |
| F | 28,00 → 40,00 | 5,60 s | recherche d'ingrédient « fa » → sélection Farine |
| G | 40,00 → 68,00 | 5,50 s | quantité ingrédient 1 → 0,5 ; date/heure ; durée de vie 2 → 1 ; quantité produite 1 → 10 |
| H | 68,00 → 77,00 | 5,00 s | ajout photo « Pizza.jpg » |
| I | 78,30 → 78,65 | 0,90 s | **zoom-punch** sur Créer la production (1024, 765) |
| J | 78,65 → 87,44 | 4,60 s | plat créé : carte « Pizza margaritta », 12,00 €, allergène Gluten |
| claude1 | carte générée | 2,60 s | reveal — prompt en gros, fond crème |
| claude2 | carte générée | 2,20 s | confirmation « Copié dans le presse-papiers ! » |
| claude3 | carte générée | 6,00 s | mockup chatbot Claude |
| outro | carte | 6,20 s (auto-étendue si besoin) | CTA |

Coordonnées mesurées visuellement sur les frames réelles (boutons à contour, pas
de remplissage plein — seuillage colorimétrique peu fiable ici), validées par
comparaison croisée sur plusieurs frames successives (tolérance ±15 px, sans
impact sur un zoom-punch à ×1,20).

## Séquence Claude — module partagé

Le rush combine deux actions qui, côté MCP, correspondent à deux outils
distincts : `mcp__FoodEatUp__create_recipe(establishment_id, name, ingredients[],
...)` pour le plat et ses ingrédients, puis `mcp__FoodEatUp__create_production_plan
(establishment_id, item_id, planned_quantity, planned_date, planned_time)` pour
planifier sa production — exactement l'enchaînement montré à l'écran (créer le
plat avec sa recette, puis lui donner une date/quantité de production). Prompt
combiné pour la vidéo (une seule séquence Claude par vidéo) :

> Crée la recette [nom du plat] avec [quantité] [unité] de [ingrédient] pour mon
> établissement FoodEatUp (ID [ID établissement]), puis planifie sa production de
> [quantité produite] portions pour le [date] à [heure].

Côté fiche Lovable, `claudePrompts[]` propose les deux étapes séparément (plus
lisible pour un premier usage) en plus du prompt combiné.

## Animations

Mêmes principes que toute la série : Ken Burns sur les cartes, xfade (0,28 s),
bandeaux d'étape (accents, pas d'apostrophe), encadré orange pulsant sur les 3
clics (tuile Production, + Créer un plat, Créer la production). Pas de clip
avatar dans ce dossier.

## Statut publication

Vidéo montée et publiée directement (instruction explicite reçue de publier sur
Lovable en gardant la structure comment-ça-marche / astuce du chef / cas d'usage,
sans étape de validation manuelle intermédiaire — même dérogation documentée que
sur `foodeatup-liste-courses-tuto`).
