# Tutoriel — Retrouver l'historique de ses productions (module HACCP)

Module 4 — HACCP, onglet **Historique > Production**. Durée du rush : **16,48 s** —
H.264 (Main)/yuv420p, AAC 48 kHz stéréo, 1920×828, 25 fps. Piste audio silencieuse
(peak -inf dBFS, pas de voix native) — voix off entièrement ElevenLabs, comme le
reste de la série. Decode 0 erreur.

## Ce que montre le rush

Le rush part de la page **« historique haccp »** (4 cartes : Températures,
Traçabilité, Plan de nettoyage, **Production** — 14 productions), clique sur la
carte **Production**, puis montre le tableau de bord **Historique > Productions** :

- 6 indicateurs en tête : Productions réalisées (205), Portions produites (8438),
  Efficacité moyenne (100.5%), Plats produits (12), Recettes produites (193),
  Portions planifiées (8394) ;
- un graphique **« Tendance des 6 derniers mois »** (barres mensuelles) ;
- une barre de recherche (« Rechercher un plat ou recette »), un filtre
  **« Tous (plats + recettes) »**, un sélecteur de **Période** et un bouton
  **Exporter CSV** ;
- une liste défilante de chaque plat/recette avec badge Plat/Recette, nombre de
  productions, portions, % d'efficacité et date/heure de la dernière production
  (Brik à l'œuf tunisien, Dragon Roll, Plateau Découverte, Salmon Maki, Burrata
  crémeuse, Couscous royal d'été, Bananes flambées, Accras de Morue Créoles...).

À confirmer avec Michael : le **nom exact du sous-dossier Drive** correspondant
(module HACCP, sous-catégorie Historique/Production) pour le champ `subcategory`
côté Lovable — non déductible du rush seul.

## Voix off (9 lignes) — validée par Michael, générée

| # | Texte | Durée | Segment |
|---|---|---:|---|
| N0 | Retrouvez l'historique de toutes vos productions FoodEatUp, en un coup d'œil. | 3,94 s | intro |
| N1 | Depuis Historique, cliquez sur Production pour ouvrir le suivi. | 3,24 s | A + clic |
| N2 | Productions réalisées, portions produites, efficacité moyenne : tout est calculé automatiquement. | 5,75 s | C — KPIs |
| N3 | La tendance des 6 derniers mois vous montre l'évolution de votre activité. | 3,84 s | D — graphique |
| N4 | Recherchez un plat, filtrez par période et exportez tout en CSV en un clic. | 4,73 s | E — liste + outils |
| N5 | De quoi repérer vos best-sellers et ajuster vos prochaines productions. | 3,60 s | E — bénéfice (même écran) |
| N6 | Vous pouvez aussi le faire depuis Claude : copiez ce prompt, remplacez les crochets. | 4,41 s | claude1+2 (réutilisé) |
| N7 | Collez-le dans la conversation : votre historique de production s'affiche en quelques secondes. | 4,62 s | claude3 |
| N8 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | 5,02 s | carte de fin (CTA, réutilisé) |

N6/N8 réutilisés tels quels depuis `foodeatup-tva-tuto/vo/` (texte identique,
zéro crédit ElevenLabs dépensé dessus). N0-N5 et N7 générés (voix Adam FR
`TGAegA0zNRi8I6nUdq3i`, `eleven_multilingual_v2`).

## Découpage — tel que monté

| Seg | Source | Sortie | Contenu |
|---|---|---:|---|
| intro | carte | 3,20 s | RETROUVER SES PRODUCTIONS HISTORIQUE |
| A | 0,00 → 4,10 | 4,20 s | page « historique haccp », 4 cartes, survol de Production |
| clic | 4,10 → 4,40 | 0,90 s | **zoom-punch** sur la carte Production (1620, 657) |
| C | 5,20 → 7,20 | 9,50 s | 6 indicateurs (KPIs) du tableau de bord |
| D | 7,20 → 9,50 | 4,50 s | graphique « Tendance des 6 derniers mois » |
| E | 9,50 → 16,40 | 9,50 s | recherche / filtre Période / Exporter CSV + liste des plats-recettes (scroll) |
| claude1 | carte générée | 6,00 s | reveal — prompt en gros, fond crème |
| claude2 | carte générée | 3,00 s | confirmation « Copié dans le presse-papiers ! » |
| claude3 | carte générée | 6,00 s | mockup chatbot Claude |
| outro | carte | 6,20 s | CTA |

Coordonnées de clic mesurées par seuillage colorimétrique sur le contour bleu
de la carte (`RGB 27,109,243`, identique au reste de la charte) sur la frame
brute à t=0,75 s : carte « Production » centrée en **(1620, 657)**, taille
**506×264**.

Premier passage de montage avec des segments C/D/E trop courts (6,00 s pour
C) : N2 (5,75 s, la ligne la plus longue) débordait de ~2,7 s sur le segment
D suivant — la narration des KPIs continuait à jouer alors que le graphique
était déjà à l'écran. Corrigé en élargissant C à 9,50 s (règle du pipeline :
mesurer la durée réelle de chaque ligne de VO avant de fixer les durées de
segment, pas après — cf. bug identique documenté sur `foodeatup-tva-tuto`).
Après correction : plus aucun décalage sur N3/N4/N6/N7/N8 ; seuls N2 (2,68 s,
absorbé dans son propre segment élargi) et N5 (0,65 s, même segment E que
N4) dérivent encore, sans conséquence car ils ne débordent pas sur un autre
contenu visuel. Vérifié par extraction de frames aux timestamps clés.

## Séquence Claude — module partagé

Correspondance MCP trouvée : `mcp__FoodEatUp__list_top_productions(establishment_id,
days?)` — « Liste les plats/recettes les plus produits sur une période. » C'est
un outil de lecture seule, cohérent avec cet écran (aucune action de création
n'apparaît dans le rush).

> Montre-moi l'historique des productions des [nombre] derniers jours pour mon
> établissement FoodEatUp (ID [ID établissement]).

Même texte côté fiche Lovable (`claudePrompt`).

## Animations

Mêmes principes que toute la série : Ken Burns sur les cartes, xfade (0,28 s),
bandeaux d'étape, encadré orange pulsant sur le clic (un seul clic dans ce
rush, pas de formulaire à remplir — écran de consultation uniquement). Pas de
clip avatar dans ce dossier.

## Rendu final

`out/foodeatup-historique-productions-tuto-v1.mp4` — **50,64 s**, H.264
High/yuv420p, 1920×828, 25 fps, AAC 48 kHz stéréo, +faststart (moov avant
mdat confirmé). Decode 0 erreur. Peak audio **-7,16 dBFS** (marge saine sous
le limiteur -alimiter=0.6, ~-4,4 dBFS). Vignette `out/thumbnail-youtube.jpg`
(1280×720, recadrage de la carte d'intro).

## Statut

**Publiée** (2026-08-04). Script validé par Michael → VO générée (ElevenLabs)
→ montage → vidéo livrée pour validation (`SendUserFile`) → Michael a
confirmé → publication :

- Upload RapidoCMS (vidéo + vignette = carte d'intro) via `upload_file_tool`,
  en pointant les URL GitHub raw des fichiers poussés sur cette branche
  (`videos/foodeatup-historique-productions-tuto/out/...mp4` et
  `assets/intro.jpg`) — S3 : `foodeatup-historique-productions-tuto-v1` /
  `-thumbnail`.
- Entrée ajoutée dans `src/data/tutorials.ts` (module `haccp`, slug
  `retrouver-historique-productions`) via `mcp__Lovable__send_message`,
  commit `0d0021f`, typecheck OK.
- Site redéployé (`mcp__Lovable__deploy_project`) →
  https://foodeatup-guide-star.lovable.app
- Pas de créneau LinkedIn programmé dans cette session (aucune rotation
  demandée par Michael) — à faire séparément si souhaité.

Point signalé à Michael avant publication : une entrée voisine existait déjà
sur le site (`tracer-ses-productions-historique`, écran "Mes productions"
par statut) — vérifié que les deux documentent des écrans différents avant
d'ajouter celle-ci, gardées distinctes.

Point signalé séparément à Michael : sa demande mentionne une série de
**157 vidéos**, mais la mémoire du dépôt (`FAISABILITE-SERIE-TUTORIELS.md`,
`LOVABLE-FOODEATUP-DOCS.md`) documente un périmètre de **91-92 vidéos** (94
annoncées, 92 dossiers Drive réels, 91 avec rush complet), dont 10 déjà
publiées + 1 (« Ouvrir sa vitrine en ligne ») livrée et en attente de
validation. Écart à clarifier avant de mettre à jour un quelconque suivi
« 157 vidéos » dans le dépôt — pas de nombre inventé.
