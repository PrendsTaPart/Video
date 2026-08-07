# STORYBOARD — LA 8 (16:9, 1920×1080, ~61.7s, master)

**Le break et la chute des billes sont une vraie simulation physique** (Matter.js,
`scripts/bake-physics.mjs`), pas une animation scriptée : la bille blanche percute
vraiment le triangle, et chaque bille est empochée un vrai tir à la fois (le plus
facile d'abord), avec de vraies collisions entre elles. La 8 n'est jamais visée —
c'est un obstacle comme un autre, jamais rentrée. Voir `scripts/bake-physics.mjs`
pour le détail ; les durées ci-dessous sont mesurées sur la sortie réelle du
calcul, pas estimées.

Décor unique : table de billard, fond quasi noir, une seule source de lumière au-dessus du
tapis. Feutre bleu profond (`#0E2A4D`→`#12345E`), pas vert — on tire vers le bleu FoodEatUp
(`#1E9BF0`). Style : motion design plat/glossy (cercles CSS avec reflet), pas de rendu
photoréaliste — cohérent avec le reste du studio (`foodeatup-promo`, 100% HTML/CSS/GSAP,
aucune génération vidéo externe).

| Frame | Fichier | Durée | Contenu | VO |
|---|---|---:|---|---|
| 01 | `01-triangle.html` | 0.00 – 14.00s (14s) | Craie (silence, ~3s) → triangle de 15 billes (12 numérotées + la 8 + 3 contours craie) → étiquettes de catégorie (liste fixe à droite) | `assets/voice/01.mp3` (8.78s), part à t=4.0 |
| 02 | `02-break.html` | 14.00 – 21.50s (7.5s) | 2.5s de tension (bille blanche qui respire) puis **LE BREAK réel** : la blanche percute le triangle, physique Matter.js jusqu'à 5.0s | — (sfx seul : impact + roulement) |
| 03 | `03-note.html` | 21.50 – 33.733s (12.233s) | Suite de la simulation : chaque bille (sauf la 8) est empochée un vrai tir à la fois, la plus facile d'abord ; liste + compteur suivent les vrais événements → **540 € – 1 040 €/mois** | `assets/voice/03.mp3` (6.22s), part à t=0.3 |
| 04 | `04-trous.html` | 33.733 – 40.733s (7s) | Le tapis se vide, travelling latéral, on s'arrête sur **3 contours à la craie** vides (OCR factures · Prédiction · Agents IA) — la 8, jamais visée, traîne encore là où la physique l'a laissée | `assets/voice/04.mp3` (4.91s), part à t=0.5 |
| 05 | `05-la8.html` | 40.733 – 47.733s (7s) | La bille **8** revient au centre depuis sa position réelle, tourne lentement ; le noir vire au bleu FoodEatUp ; le tapis devient une grille de dashboard (12 modules) | `assets/voice/05.mp3` (5.04s), part à t=0.5 |
| 06 | `06-cta.html` | 47.733 – 61.733s (14s) | Carton produit (logo, prix) puis fond bleu plein écran + URL comparateur | `assets/voice/06.mp3` (7.34s), part à t=1.0 |

Total mesuré : 14 + 7.5 + 12.233 + 7 + 7 + 14 = **61.733s**.

## Le plan clé : Frame 04

Tout le film accélère jusqu'à la fin du break (t≈22s) puis la chute des billes (t≈22–32s),
puis s'arrête net sur trois contours vides. C'est le silence qui vend, pas le break — garder
un vrai temps mort ici (pas de musique qui remonte avant t≈37s).

## Bandeau mention légale

Affiché en bas d'écran, `LegalBar`, pendant Frame 03 (t 22–32s) et Frame 06 (t 46–60s), 3s
minimum à l'écran à chaque fois :

> Fourchette relevée sur les grilles publiques des éditeurs, juillet 2026. Hors caisse et hors
> paie. Marques citées à titre d'identification. Votre coût réel dépend de vos outils :
> calculez-le sur site.foodeatup.com/comparateur.

## Chiffres autorisés à l'écran

- **540 € – 1 040 €/mois** (Frame 03) — fourchette publique, hors caisse/paie, source à l'écran.
- **12 poches. 177 outils. 1 bille.** (Frame 05) — décompte MCP FoodEatUp.
- **49 €/mois** (Frame 06) — page Tarifs FoodEatUp.

Aucune promesse d'économie chiffrée (jamais « Économisez X €/mois ») — cf. art. L122-1 à
L122-7 du Code de la consommation (publicité comparative FR).

## Casting des billes (triangle, Frame 01)

Rack à 15 emplacements, apex en haut, la **8 au centre géométrique** (rangée du milieu),
3 emplacements du dernier rang laissés en **contour craie** (billes fantômes) :

| Rang | Billes |
|---|---|
| 0 (apex) | 1 — Caisse (jaune) |
| 1 | 2 — Réservation (bleu) · 3 — Agent vocal (rouge) |
| 2 | 4 — Food cost (violet) · **8 — FoodEatUp (noir)** · 5 — HACCP (orange) |
| 3 | 6 — Planning (vert) · 7 — Fidélité (bordeaux) · 9 — Avis (jaune rayé) · 10 — Site (bleu rayé) |
| 4 | 11 — Messages (rouge rayé) · 12 — BI (violet rayé) · 13 👻 OCR factures · 14 👻 Prédiction IA · 15 👻 Agents IA |

Formulation VO obligatoire : les billes fantômes sont **ce que le restaurateur n'a pas**,
jamais présentées comme une absence chez un éditeur nommé (dénigrement interdit).
