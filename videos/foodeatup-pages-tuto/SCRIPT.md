# Tutoriel — Gérer les pages de son site FoodEatUp

Module 3 « SITE WEB & VITRINE », sous-catégorie `04 - Gérer les Pages de son site`
(`videos/CATALOGUE-157-TUTORIELS.md`). Premier tutoriel produit pour ce module
(0/8 publiés avant celui-ci, voir `videos/PROGRESSION-157-TUTORIELS.md`).

Durée livrée : **42,60 s** — H.264 High/yuv420p, AAC 48 kHz stéréo, faststart.
Audio : true peak **-7,2 dBFS** (mesuré sur le MP4 final, `ffmpeg -af astats`).
Decode 0 erreur.

## Voix off (9 lignes, voix Adam FR `TGAegA0zNRi8I6nUdq3i`)

| # | Texte | Durée | Ancrage |
|---|---|---:|---|
| N0 | Gérer les pages de votre site FoodEatUp ? Un clic suffit. | 3,19 s | carte d'intro |
| N1 | Ouvrez l'onglet Pages pour retrouver Accueil, Carte, À propos et Contact. | 4,73 s | clic Pages (menu gauche) |
| N2 | Chaque page affiche son statut, publiée ou brouillon, en un coup d'œil. | 4,18 s | liste des pages (toutes publiées) |
| N3 | Cliquez sur Dépublier pour retirer une page du site sans la supprimer. | 3,60 s | clic Dépublier (Accueil) |
| N4 | Publier la remet en ligne aussitôt, avec toutes ses sections intactes. | 3,79 s | clic Publier (Accueil) |
| N5 | Cliquez sur Voir pour contrôler le rendu, en direct sur votre site. | 3,76 s | clic Voir |
| N6 | Vous pouvez aussi le faire depuis Claude : copiez ce prompt, remplacez les crochets. | 4,41 s | étage 1+2 (reveal + copié) — **réutilisée telle quelle** depuis `foodeatup-tva-tuto/vo/N6.mp3` |
| N7 | Collez-le dans la conversation : votre page est publiée en quelques secondes. | 4,00 s | étage 3 (mockup chatbot) |
| N8 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | 5,02 s | carte de fin (CTA) — **réutilisée telle quelle** depuis `foodeatup-tva-tuto/vo/N8.mp3` |

N6/N8 copiées d'un tutoriel précédent (texte générique de la série, voir
`FOODEATUP-TUTORIELS-WORKFLOW.md`) : gain d'un aller-retour ElevenLabs. N0-N5/N7
générées pour cette vidéo (ElevenLabs, `eleven_multilingual_v2`, `language_code=fr`).

## Analyse du rush (`assets/screen.mp4`, 1920x828, 25 fps, 17,96 s)

Reconstitué par extraction de frames à intervalles réguliers (2 fps, puis
10 fps autour de chaque clic) :
- 0,0 → ~2,9 s : écran Éditeur visuel (menu de gauche visible, pas encore sur Pages)
- ~3,0 s : clic sur **Pages** (menu gauche) → liste des 5 pages (Accueil, Notre
  carte, À propos, Contact, Mentions légales), toutes **Publiée**
- ~7,1 s : clic **Dépublier** (ligne Accueil) → statut passe à **Brouillon**,
  le bouton devient **Publier**
- ~8,6 s : clic **Publier** → retour à **Publiée**
- ~9,5 s : clic **Voir** → ouverture de la page live (Accueil)
- 10,9 → 17,96 s : défilement de la page publiée (hero, carte du jour,
  horaires, pied de page avec lien Mentions légales)

Coordonnées mesurées directement sur les frames (espace source 1920x828) :
- Item **Pages** (menu gauche) : (110, 469)
- Bouton **Dépublier / Publier** (ligne Accueil) : (1791, 338)
- Bouton **Voir** (ligne Accueil) : (1685, 338)

## Découpage

| Seg | Source | Sortie | Contenu |
|---|---|---:|---|
| intro | carte | 3,40 s | GÉRER TES PAGES |
| A | 0,00 → 2,90 | 2,40 s | Éditeur visuel, menu de gauche |
| B | 2,90 → 3,10 | 0,60 s | **zoom-punch** sur Pages (110, 469) |
| C | 3,10 → 7,00 | 8,50 s | liste des 5 pages, toutes publiées (ralenti pour porter N1+N2) |
| D | 7,00 → 7,15 | 0,60 s | **zoom-punch** sur Dépublier (1791, 338) |
| E | 7,15 → 8,50 | 4,00 s | statut Brouillon |
| F | 8,50 → 8,75 | 0,60 s | **zoom-punch** sur Publier (1791, 338) |
| G | 8,75 → 9,50 | 4,20 s | retour à Publiée |
| H | 9,50 → 9,65 | 0,60 s | **zoom-punch** sur Voir (1685, 338) |
| I | 10,90 → 17,96 | 4,20 s | page live, défilement |
| claude1 | carte générée | 3,00 s | reveal — prompt en gros, fond crème |
| claude2 | carte générée | 2,30 s | confirmation « Copié dans le presse-papiers ! » |
| claude3 | carte générée | 5,30 s | mockup chatbot Claude |
| outro | carte | 6,20 s | CTA |

Transition `slideleft` sur les 3 étages Claude (scènes distinctes), `fade`
partout ailleurs (action continue à l'écran). `drift` maximal observé sur les
lignes VO vs leurs ancrages : 2,08 s (N2, après une N1 plus longue que prévu) —
sans conséquence, aucune ligne ne chevauche la suivante (`GAP` 0,22 s respecté).

## Séquence Claude — module partagé

Un seul outil MCP correspond exactement à ce que montre le rush :
`toggle_site_page(establishment_id, page_slug, publish)` — dépublier puis
republier une page, dans l'ordre où le rush le montre. Pas de `add_site_page`
dans ce prompt : le rush ne montre pas l'activation d'une page inactive du
catalogue, seulement le statut publié/brouillon d'une page déjà active.

> Dépublie temporairement la page [nom de la page, ex : Accueil] de mon site
> FoodEatUp (établissement ID [ID établissement]) le temps d'une mise à jour,
> puis republie-la.

Même texte côté fiche Lovable (`claudePrompt`).

## Animations

Mêmes principes que toute la série : Ken Burns sur les cartes, xfade (0,28 s),
bandeaux d'étape, encadré orange pulsant sur les 3 clics. **Bandeaux rendus
avec le `box=1` de `drawtext`** (pas `drawbox` — sur ffmpeg 6.1.1, `drawbox`
n'évalue son `x`/`y` qu'une fois à l'init, un slide animé sur `t` ne bouge
jamais et le bandeau reste hors champ ou statique ; voir les pitfalls dans
`FOODEATUP-TUTORIELS-WORKFLOW.md`). Vérifié visuellement sur les frames
extraites du rendu final : bandeau bicolore orange+bleu bien visible et
lisible à chaque étape.

## Statut publication

Montage terminé, checklist de compatibilité passée (voir ci-dessus). Livré à
Michael pour validation avant publication Lovable/RapidoCMS/LinkedIn (règle du
2026-08-02, `FOODEATUP-TUTORIELS-WORKFLOW.md`).
