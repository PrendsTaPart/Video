# Brand assets — statut PLACEHOLDER

Le kit de marque officiel EatNow (`amine.zip`) envoyé par le client est corrompu — tous ses
fichiers (logo, wordmark, motifs SVG/PNG, `BRAND.md`) sont à 0 octet. En attendant le vrai
fichier, ce dossier contient des reconstructions placeholder :

- **`motif-stamp-placeholder.svg`** — motif "tampon" recréé à partir de l'image de référence
  envoyée par le client (grille 5×5 de carrés arrondis, 17 cases actives, symétrique). Utilisé
  au Frame 6 (clôture) pour le repère EatNow qui se dessine case par case. `currentColor` +
  `data-index` par case pour piloter le stagger d'apparition en GSAP.
- **Wordmark** — pas de fichier séparé : rendu en texte "EatNow" (Geist Bold) directement dans
  `compositions/frames/06-cta.html`, pas d'image.

**À remplacer dès réception du vrai kit de marque** : le motif officiel `06-motifs/svg/motif-06-logo-stamp.svg`
et le wordmark officiel `02-wordmark/svg/` (structure attendue du zip, voir `SCRIPT.md` § Statut assets).
