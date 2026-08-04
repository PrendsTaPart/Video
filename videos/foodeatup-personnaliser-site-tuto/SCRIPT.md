# Tutoriel — Personnaliser son site (éditeur web) FoodEatUp

Catalogue 157 tutoriels : module `site-web-vitrine` (Site Web & Vitrine, 8 vidéos
attendues), vidéo **03 Personnaliser son site (éditeur web)**. Distinct de
`foodeatup-vitrine-tuto` (02 Choisir son Template + publication) : ce tutoriel se
concentre sur l'édition en direct des textes d'un bloc déjà en ligne, sans changer
de template ni republier.

Intrants fournis par Michael : `assets/intro.jpg` (carte "PERSONNALISER TON SITE"),
`assets/outro.jpg` (carte CTA, **identique octet pour octet** à celle déjà utilisée
sur `foodeatup-vitrine-tuto`/`foodeatup-qrcode-tuto` — réutilisée telle quelle),
`assets/screen.mp4` (rush "Éditer son site", 1920x828, 25fps, 37,80s).

## Analyse du rush (frames extraites à 1-10fps, coordonnées mesurées par grille pixel)

| Temps source | Écran | Action |
|---|---|---|
| 0,00 → 4,70 | Templates (bibliothèque) → Éditeur visuel | Arrivée sur le site "GoSushi Démo" en mode édition, bloc Hero visible avec le bouton "modifier hero" |
| 4,70 → 4,95 | — | **clic** sur "modifier hero" (500, 333), taille (145, 45) |
| 4,95 → 29,85 | Panneau "Modifier le bloc" (HERO) | Badge "Levain naturel" → "GoSushi" ; Titre "Sorti du four ce matin." → "Le restaurant le plus proche de vous". Sous-titre et Bouton principal laissés identiques (non touchés) |
| 29,85 → 30,10 | — | **clic** sur "Enregistrer" (1670, 707), taille (220, 50) |
| 30,10 → 37,80 | Site (mode édition) | Panneau fermé, aperçu mis à jour instantanément : badge "GOSUSHI", titre "Le restaurant le plus proche de vous", sous-titre et bouton inchangés |

Le formulaire ne touche que les champs modifiés (fusion partielle) : sous-titre et
bouton restent ceux du template tant qu'on ne les vide/modifie pas — comportement
qui correspond exactement à `mcp__FoodEatUp__update_section` ("fusion partielle,
ex. {title, text}").

## Voix off (8 lignes, durées mesurées après génération ElevenLabs)

| # | Texte | Durée | Offset | Segment |
|---|---|---:|---:|---|
| N0 | Personnaliser votre site FoodEatUp ? Ça se fait en un clic, sans toucher au code. | 4,78 s | 0,30 s | intro |
| N1 | Ouvrez l'Éditeur visuel, puis cliquez sur le bloc que vous voulez modifier — ici, la bannière d'accueil. | 5,75 s | 5,30 s | A + clic B |
| N2 | Changez le badge, le titre et le sous-titre : le texte du template est remplacé par le vôtre, sans toucher au reste. | 6,22 s | 11,27 s | C |
| N3 | Cliquez sur Enregistrer : la mise à jour est visible instantanément sur votre site. | 4,55 s | 18,20 s | clic D |
| N4 | Votre identité de marque reste cohérente, page après page, sans écrire une ligne de code. | 4,96 s | 22,97 s | E |
| N5 | Vous pouvez aussi le faire depuis Claude : copiez ce prompt, remplacez les crochets. | 4,41 s | 28,72 s | claude étages 1+2 (réutilisé) |
| N6 | Collez-le dans la conversation : le contenu de votre site est mis à jour en quelques secondes. | 4,83 s | 33,60 s | claude étage 3 |
| N7 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | 5,02 s | 39,19 s | carte de fin (CTA, réutilisé) |

N5/N7 réutilisés tels quels, octet pour octet, depuis
`foodeatup-vitrine-tuto/vo/N6.mp3` et `N8.mp3` (mêmes textes exacts) plutôt que
régénérés — gagne un aller-retour ElevenLabs. N0-N4 et N6 générés avec la voix
Adam FR (`TGAegA0zNRi8I6nUdq3i`).

## Découpage (durées de sortie mesurées sur le rendu final)

| Seg | Source | Sortie | Contenu |
|---|---|---:|---|
| intro | carte | 2,60 s | PERSONNALISER TON SITE |
| A | 0,00 → 4,70 | 4,60 s | Templates → Éditeur visuel, bloc Hero, "modifier hero" |
| B | 4,70 → 4,95 | 0,90 s | **zoom-punch** sur "modifier hero" (500, 333) taille (145, 45) |
| C | 4,95 → 29,85 | 10,90 s | Badge + Titre édités dans le panneau (×2,3 ralenti vs rush) |
| D | 29,85 → 30,10 | 0,90 s | **zoom-punch** sur "Enregistrer" (1670, 707) taille (220, 50) |
| E | 30,10 → 37,80 | 10,10 s | Aperçu mis à jour, badge/titre visibles en direct (×1,3 ralenti) |
| claude1 | carte générée | 3,00 s | reveal — prompt en gros, fond crème |
| claude2 | carte générée | 2,45 s | confirmation « Copié dans le presse-papiers ! » |
| claude3 | carte générée | 5,70 s | mockup chatbot Claude |
| outro | carte | 6,20 s | CTA |

**Durée totale livrée : 45,04 s.** Segments C et E tournent plus lentement que le
temps réel (rush dense, 37,8 s en tout) pour laisser aux lignes N2/N3/N4 le temps
de se dérouler sans chevaucher la séquence Claude — mêmes principes que
`foodeatup-mouvement-stock-tuto` (segment M) : contenu statique (panneau
d'édition, toast de confirmation), le ralenti ne se voit pas à l'écran. Aucune
dérive imprévue : offsets vérifiés dans les logs `build.py`, chaque ligne reste
dans son segment prévu (N4 se termine à 27,93 s, la séquence Claude commence à
28,52 s).

## Séquence Claude — module partagé

`mcp__FoodEatUp__update_section(establishment_id, section_id, props)` correspond
exactement à l'action montrée : mise à jour partielle des props d'une section
(badge + titre), le reste du bloc n'étant pas touché.

> Modifie le badge en [nouveau badge], le titre en [nouveau titre] et le sous-titre
> en [nouveau sous-titre] de la section [ID de la section] de mon site, pour mon
> établissement FoodEatUp (ID [ID établissement]).

Même texte côté fiche Lovable (`claudePrompt`).

## Animations

Mêmes principes que toute la série : Ken Burns sur les cartes, xfade (0,28 s),
bandeaux d'étape (rendus en `drawtext` `box=1`, pas `drawbox` — voir
`FOODEATUP-TUTORIELS-WORKFLOW.md`, piège corrigé le 2026-08-03), encadré orange
pulsant sur les 2 clics. Pas d'avatar HeyGen sur ce tutoriel (voix ElevenLabs
Adam FR sur toute la narration).

## Statut publication

Livrée et validée le 2026-08-04. Publiée sur Lovable le 2026-08-04 : remplace la
fiche placeholder préexistante `personnaliser-son-site` (module `site-web-vitrine`,
order 3) dans `src/data/tutorials.ts` via `mcp__Lovable__send_message`, `tsgo
--noEmit` OK. Vidéo/vignette hébergées en raw GitHub
(`videos/foodeatup-personnaliser-site-tuto/out/`, branche
`claude/foodeatup-video-tutorial-4qnhnz`) — RapidoCMS non disponible dans cette
session, LinkedIn non demandé.
