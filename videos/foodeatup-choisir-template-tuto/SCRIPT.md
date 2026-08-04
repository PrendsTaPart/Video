# Tutoriel — Choisir son template (Mon Site)

Module « Site Web & Vitrine » (nouveau, catalogue 157 tutoriels), fiche Lovable déjà en
place : `choisir-son-template` (`subcategory: "02 · Template & design"`, `order: 2`) —
placeholder à remplir, pas une nouvelle entrée à créer.

Assets fournis par Michael : `CHOISIR_TON_TEMPLATE.jpg` (carte intro), `page_fin_vid..jpg`
(carte outro CTA générique, déjà vue sur d'autres tutos), `Choisir_un_template.mp4`
(screen recording 1920x828, 36,33 s, page Studio > Site Web > Templates).

## Déroulé observé dans le rush

1. Page Templates (bibliothèque de 13 templates métiers, filtrables par catégorie).
2. Clic sur le filtre catégorie « Boulangerie » → liste réduite à 1 résultat (Au Fournil Doré).
3. Clic sur « Aperçu » → ouvre un aperçu grandeur nature du site dans un nouvel onglet
   (hero, carte/menu, horaires) — **rien n'est publié**, bandeau d'avertissement en haut.
4. Retour sur l'onglet Studio (filtre revenu sur "Tous").
5. Clic sur « Utiliser » sur la carte « Au Fournil Doré ».
6. **Modale de confirmation** : "Appliquer « Au Fournil Doré » ? Le site actuel sera
   remplacé (une version est sauvegardée)." boutons OK / Annuler.
7. Clic OK → toast de confirmation « Template « Au Fournil Doré » appliqué. ».

Correspondance MCP FoodEatUp exacte : `apply_site_template(establishment_id, slug,
confirm)` — le paramètre `confirm: true` (avec résumé du changement au restaurateur)
reproduit très précisément la modale de confirmation vue dans le rush. `list_site_templates`
couvre l'étape 1 (bibliothèque). Séquence Claude à ajouter en fin de vidéo (règle du
2026-08-02).

## Voix off (9 lignes, voix Adam FR `TGAegA0zNRi8I6nUdq3i`)

| # | Texte | Ancrage | Source |
|---|---|---|---|
| N0 | Choisir le template de votre site FoodEatUp, c'est transformer votre vitrine en quelques secondes. | carte d'intro | à générer |
| N1 | Filtrez la bibliothèque de templates par type d'établissement pour trouver votre style. | clic filtre « Boulangerie » | à générer |
| N2 | Cliquez sur Aperçu pour visualiser le template en conditions réelles, sans rien publier. | clic Aperçu + preview | à générer |
| N3 | Le template vous plaît ? Cliquez sur Utiliser. | clic Utiliser | à générer |
| N4 | Confirmez l'application : une sauvegarde de votre site actuel est conservée automatiquement. | modale de confirmation | à générer |
| N5 | Votre site est transformé instantanément, prêt à personnaliser. | toast « Template appliqué » | à générer |
| N6 | Vous pouvez aussi le faire depuis Claude : copiez ce prompt, remplacez les crochets. | étage 1+2 (reveal + copié) | **réutilisée telle quelle** de `foodeatup-tva-tuto/vo/N6.mp3` (ligne générique, règle du 2026-08-02) |
| N7 | Collez-le dans la conversation : votre nouveau template est appliqué en quelques secondes. | étage 3 (mockup chatbot) | à générer (spécifique à ce tuto, jamais réutilisable) |
| N8 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | carte de fin (CTA) | **réutilisée telle quelle** de `foodeatup-tva-tuto/vo/N8.mp3` (CTA générique) |

## Découpage prévu (targets à recaler sur la durée réelle des .mp3 avant montage)

| Seg | Source | Contenu |
|---|---|---|
| intro | carte | CHOISIR TON TEMPLATE |
| A | 0,30 → 3,00 | bibliothèque de templates, vue d'ensemble |
| B | ~11,2 → ~11,7 | **zoom-punch** filtre « Boulangerie » |
| C | ~11,7 → ~12,6 | résultat filtré (1 template) |
| D | ~13,0 → ~13,5 | **zoom-punch** bouton « Aperçu » |
| E | ~15,0 → ~19,0 | aperçu grandeur nature (hero, carte, horaires) |
| F | ~21,5 → ~26,5 | retour Studio, bibliothèque |
| G | ~29,6 → ~30,4 | **zoom-punch** bouton « Utiliser » |
| H | ~30,9 → ~32,3 | modale de confirmation + **zoom-punch** OK |
| I | ~33,0 → ~36,3 | toast « Template appliqué » |
| claude1 | carte générée | reveal — prompt en gros, fond crème |
| claude2 | carte générée | confirmation « Copié dans le presse-papiers ! » |
| claude3 | carte générée | mockup chatbot Claude |
| outro | carte | CTA |

Coordonnées boutons (espace source 1920x828, mesurées par crop) : filtre « Boulangerie »
≈ (565, 305) taille ≈ (170, 40) · bouton « Aperçu » ≈ (500, 612) taille ≈ (170, 55) ·
bouton « Utiliser » ≈ (725, 622) taille ≈ (230, 55) · bouton « OK » (modale) ≈ (1090, 125)
taille ≈ (120, 60). **À revérifier par crop fin pendant le montage**, comme pour tous les
tutos précédents — tolérance du zoom-punch (~1.20x) large sur ces tailles.

## Séquence Claude — module partagé

`videos/_shared/claude_prompt_sequence.py`, mêmes fonctions que le reste de la série.

Prompt (identique côté vidéo et côté fiche Lovable `claudePrompt`) :

> Applique le template [nom du template, ex: Au Fournil Doré] à mon site FoodEatUp
> (établissement [ID établissement]).

## Statut (2026-08-04)

**Montée.** Durée livrée : **42,36 s** — H.264 High/yuv420p, AAC 48 kHz stéréo, faststart
(moov avant mdat vérifié). Audio : true peak **-7,26 dBFS** (mesuré sur le MP4 final,
cohérent avec le reste de la série).

Bug rencontré et corrigé pendant le montage : le `banner()` copié tel quel depuis
`foodeatup-abonnement-tuto`/`foodeatup-tva-tuto` utilisait deux `drawbox` avec un `x`
animé en fonction de `t` pour le filet orange et la plaque bleue — exactement le piège
documenté dans `FOODEATUP-TUTORIELS-WORKFLOW.md` (`drawbox` n'évalue `x`/`y`/`w`/`h`
qu'une fois sur cet ffmpeg 6.1.1, donc la plaque ne s'affichait jamais, seul le texte
blanc glissait, illisible sur l'UI claire). Corrigé en reprenant le `banner()` fixé de
`videos/foodeatup-mouvement-stock-tuto/build.py` (plaque = `box=1` de `drawtext`, qui lui
évalue bien `t` par frame). Vérifié visuellement par extraction de frames après coup :
bandeaux, zoom-punch (filtre, Aperçu, Utiliser, OK) et séquence Claude tous lisibles et
correctement positionnés.

Deux passes de retiming des segments A-J (mesurer chaque VO avant de fixer les durées de
segment, règle déjà en place) pour que les clics (filtre, Aperçu, Utiliser, OK) tombent
pendant leur ligne VO associée plutôt qu'après — écart résiduel plus faible en début de
vidéo (filtre/aperçu/utiliser bien synchronisés) qu'en fin (confirmation + séquence
Claude, lignes plus longues que leur segment visuel, glissement absorbé par l'outro
auto-étendu comme sur le reste de la série).

Livrables : `out/foodeatup-choisir-template-tuto-v1.mp4` (42,36 s),
`out/thumbnail-youtube.jpg` (1280x720, depuis `assets/intro.jpg`, aucun recadrage
créatif).

**Prochaines étapes** : livraison à Michael pour validation (règle STOP), puis
publication (RapidoCMS — connecteur indisponible dans cette session, URL GitHub raw en
attendant — + fiche Lovable `choisir-son-template` déjà en place à remplir + mise à jour
des tableaux de suivi).
