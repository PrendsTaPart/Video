# Brand assets

Le vrai kit de marque EatNow a été reçu le 2026-08-05 (`amine.zip`, `eatnow-brand-assets/`) après
deux envois précédents corrompus (fichiers à 0 octet). Les assets officiels utilisés dans cette
composition vivent dans `official/` :

- **`official/BRAND.md`** — charte complète (couleurs, typo, motif, voix). Référence faisant foi.
- **`official/tokens.json`** — tokens couleurs (Ink/Paper/Navy/Beige + neutres + fonctionnels).
- **`official/brandmark-paper.svg`** / **`brandmark-ink.svg`** — le repère (grille 5×5, 17 points,
  symétrie 4 côtés) — inliné directement dans `compositions/frames/06-cta.html` (rects individuels
  avec `data-index` pour le stagger d'apparition case par case).
- **`official/wordmark-paper.svg`** / **`wordmark-ink.svg`** — le wordmark "EatNow" (tracé vectoriel
  réel, Geist Bold) — inliné dans `compositions/frames/06-cta.html`.
- **`official/motif-06-logo-stamp.svg`** — exemple d'usage du repère en tampon (coin de carte) ;
  non utilisé directement dans cette vidéo, gardé pour référence.

Le motif que j'avais recréé à partir de l'image de référence envoyée par le client correspondait
exactement à la grille officielle (même disposition des 17 points) — aucune reprise structurelle
n'a été nécessaire pour le Frame 6, seul le SVG source a été remplacé par le vrai fichier.

**Polices** : Geist (400/500/700) et Fraunces italic (300, avec `font-variation-settings: "opsz" 144,
"SOFT" 100, "WONK" 1` et `letter-spacing: -0.03em` selon `official/BRAND.md` § 3) — vendorées dans
`../fonts/` depuis Google Fonts (fichiers statiques ; les axes variables SOFT/WONK/opsz ne sont pas
pilotables via l'API `css2` de Google pour un fichier statique — approximation acceptée pour cette
vidéo, la police variable complète n'a pas été poursuivie).
