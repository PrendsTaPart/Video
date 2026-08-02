# Tutoriel — Paramétrer sa TVA FoodEatUp

Module 1 « CONFIGURATION », dossier Drive `5 - vos taux de TVA`.
Durée livrée : **32,1 s** — H.264 High/yuv420p, AAC 48 kHz stéréo, faststart.
Audio : true peak **-7,2 dBFS** (mesuré sur le MP4 final).

**v2 (2026-08-02)** : script voix off amélioré + séquence Claude entièrement repensée
en animation chatbot 3 temps (voir §"Séquence Claude" plus bas). Remplace la v1 (carte
statique unique à fond noir).

## Voix off (v2)

| # | Texte | Durée | Placement |
|---|---|---:|---|
| N0 | Paramétrer sa TVA sur FoodEatUp ? Quelques secondes suffisent. | 3,79 s | carte d'intro |
| N1 | Cliquez sur Ajouter TVA pour créer votre premier taux. | 2,87 s | clic Ajouter TVA |
| N2 | Donnez-lui un nom clair et son pourcentage, puis validez. | 3,34 s | modal + clic Ajouter |
| N3 | Votre taux apparaît aussitôt, prêt à être appliqué à vos produits. | 3,76 s | liste mise à jour |
| N4 | Besoin de l'ajuster ? Cliquez sur le crayon à tout moment. | 3,29 s | clic crayon |
| N5 | Modifiez le pourcentage et sauvegardez, c'est instantané. | 3,19 s | clic Sauvegarder |
| N6 | Et vous pouvez faire tout ça directement depuis Claude, en copiant-collant ce prompt. | 4,21 s | séquence Claude (3 étages) |
| N7 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | 5,02 s | carte de fin (CTA) |

## Découpage

| Seg | Source | Sortie | Contenu |
|---|---|---:|---|
| intro | carte | 2,6 s | PARAMÉTRER SA TVA FOODEATUP |
| A | 0,20 → 1,40 | 2,00 s | liste vide (« Aucune TVA ») |
| B | 1,40 → 1,55 | 0,90 s | **zoom-punch** sur Ajouter TVA (1708, 351) |
| C | 2,00 → 5,90 | 2,50 s | modal, nom + pourcentage (7) |
| D | 6,30 → 6,55 | 0,90 s | **zoom-punch** sur Ajouter / submit (1204, 602) |
| E | 7,00 → 9,00 | 2,70 s | taux créé, visible dans la liste |
| F | 9,30 → 9,55 | 0,90 s | **zoom-punch** sur le crayon d'édition (1489, 537) |
| G | 10,00 → 14,90 | 2,90 s | modification du pourcentage (7 → 8) |
| H | 15,20 → 15,55 | 0,90 s | **zoom-punch** sur Sauvegarder (1172, 602) |
| I | 16,00 → 18,20 | 2,10 s | taux mis à jour (8%) |
| claude1 | carte générée | 2,20 s | reveal — prompt en gros, fond crème |
| claude2 | carte générée | 1,30 s | confirmation « Copié dans le presse-papiers ! » |
| claude3 | carte générée | 2,50 s | mockup chatbot Claude (logo + bulles) |
| outro | carte | ~11,0 s (auto-étendue) | CTA |

## Séquence Claude — v2, animation chatbot en 3 temps (remplace la carte statique v1)

`mcp__FoodEatUp__create_tva(establishment_id, name, percentage)` existe. Sur demande de
Michael ("enlève le fond noir et réalise une animation comme un chatbot... ajoute le logo
de Claude et sa charte graphique"), la carte statique unique à fond marine a été
entièrement remplacée par 3 cartes PNG (rendues via PIL, pas ffmpeg drawtext/lavfi)
enchaînées en `slideleft` :

1. **Reveal** (2,20 s) — fond crème FoodEatUp `#FCF9E6`, **aucune boîte noire**. Titre
   « Utilisez cette fonctionnalité avec Claude », prompt affiché en gros dans une carte
   blanche à filet bleu + liseré corail, police Liberation Sans Bold (pas monospace).
2. **Copié** (1,30 s) — même carte, filet vert + badge « check » dessiné à la main (pas un
   glyphe emoji, non fiable selon la police), légende « Copié dans le presse-papiers ! ».
3. **Chatbot Claude** (2,50 s) — mockup d'interface Claude : vrai logo Claude
   (`studio-video/assets/brand/third-party-logos/claude-logo.png`) + « claude.ai » en barre
   du haut, fond `#F0EEE6` (cream propre à l'UI Claude), bulle utilisateur à droite en
   corail `#D97757` (couleur de marque Claude, extraite du logo lui-même — sampling PIL,
   pas devinée) avec le prompt collé, bulle assistant à gauche (avatar rond corail +
   astérisque dessiné) qui commence sa réponse « Bien sûr ! Je crée ce taux de TVA... ».

Prompt (identique côté vidéo et côté fiche Lovable `claudePrompt`) :

> Crée un taux de TVA nommé [nom du taux] à [pourcentage]% pour mon établissement
> FoodEatUp (ID [ID établissement]).

### Bugs rencontrés et corrigés (v1 + v2)

1. **v1 — ligne du milieu disparue.** `[pourcentage]%` contient un `%` isolé — `drawtext`
   l'interprète comme un token d'expansion et abandonne le filtre. N'existe plus en v2 :
   le texte est dessiné avec PIL (glyphes littéraux), pas de parseur d'expansion.
2. **v1 — fond crème viré au kaki.** `color=c=0xFCF9E6` (lavfi) encodé direct puis passé
   dans `xfade` ressortait désaturé. Corrigé en rendant en PNG statique d'abord, passé
   ensuite dans `card()` — même traitement que les cartes intro/outro, couleurs garanties.
   Toujours le cas en v2 (les 3 étages sont des PNG).
3. **v2 — étage « Copié » à moitié noir.** `card()` applique un fondu-au-noir 0,4 s en
   entrée/sortie, pensé pour intro/outro (vrai début/fin de vidéo). Sur un étage court
   (~1 s) situé au milieu du montage, ce fondu se cumule avec le `xfade` des deux côtés
   (0,28 s chacun) : la carte passe le plus clair de son temps à moitié fondue au noir des
   deux côtés à la fois, illisible (vérifié par extraction de frame : pixel de fond
   (176,173,160) au lieu du crème attendu (252,248,229)). Corrigé en ajoutant un paramètre
   `fade=False` à `card()`, utilisé pour les 3 étages Claude (ils n'ont pas besoin de leur
   propre fondu, le `xfade` suffit — même logique que les segments de screen recording).
   Re-vérifié après correction : pixel de fond exact (252,248,229), lisible du début à la
   fin de l'étage.

## Animations

Mêmes principes que les précédents : Ken Burns sur les cartes, xfade (0,28 s), bandeaux
d'étape, encadré orange pulsant sur les 4 clics. Pas de clip avatar dans ce dossier.

## Statut publication (2026-08-02)

Vidéo livrée à Michael pour validation (règle ajoutée le 2026-08-02 : plus aucune
publication RapidoCMS/LinkedIn/Lovable sans validation explicite au préalable). En attente
de retour avant upload RapidoCMS (remplacement du draft LinkedIn #543, prévu 2026-08-05
07h) et mise à jour de la fiche Lovable `parametrer-sa-tva`.
