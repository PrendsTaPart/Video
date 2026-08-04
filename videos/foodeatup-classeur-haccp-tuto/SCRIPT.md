# Tutoriel — Ouvrir son classeur HACCP (FoodEatUp)

Module **HACCP** (30 vidéos attendues, ceci est la 1ʳᵉ), sous-catégorie proposée
**« Accueil & Historique »** (nom exact du sous-dossier Drive non confirmé — à corriger
si Michael a une convention différente).

Durée livrée : **44,64 s** — H.264 High/yuv420p 1920×828 25fps, AAC 48 kHz stéréo,
faststart. Audio : true peak **-7,0 dBFS** (mesuré sur le MP4 final, cohérent avec le
reste de la série).

Source : `assets/screen.mp4` (1920×828, 25 fps, 19,56 s). Intro `assets/intro.jpg`
("OUVRIR SON CLASSEUR MODULE HACCP", mascotte chef) et outro `assets/outro.jpg`
(carte CTA générique, réutilisée telle quelle) fournis par Michael.

## Statut : produite (2026-08-04). Script et montage exécutés sur autorisation directe
de Michael ("continue", ElevenLabs confirmé disponible, structure + voix + prompt Claude
+ publication explicitement redemandés) — le STOP de validation script/vidéo prévu par
`FOODEATUP-TUTORIELS-WORKFLOW.md` §3/§6 a été levé pour cette vidéo par cette
autorisation. Voix ElevenLabs générée via le connecteur MCP `mcp__ElevenLabs__text_to_speech`
(pas de clé API locale dans cet environnement — le connecteur a servi de substitut
fonctionnellement identique, même voix Adam FR `TGAegA0zNRi8I6nUdq3i`).

## Analyse du screen recording

| t | Écran |
|---:|---|
| 0,0–5,5 s | Tableau de bord StockVisionAI, le curseur remonte vers le menu du haut |
| 5,5–7,5 s | Survol de **HACCP** dans la barre de nav → menu déroulant (Accueil HACCP, Contrôle à réception, Traçabilité, Étiquettes, Production HACCP, Températures, Checklist Hygiène, Plan de nettoyage, Conformité, Documents…) → **clic sur « Accueil HACCP »** (≈ 975, 196) |
| 7,5–10,0 s | Le classeur HACCP s'ouvre : nav dédiée (Accueil / Réception / Traçabilité / Production / Hygiène / Documents / Historique), écran d'accueil « bonjour, dupont jean ! » avec 4 cartes (Températures, Traçabilité, Plan de nettoyage, Production) |
| 10,0–12,3 s | Défilement : grille complète (Contrôle à réception, Checklist Hygiène, Étiqueteuse en plus des 4 précédentes) |
| 12,3–13,5 s | **Clic sur l'onglet « Historique »** (≈ 1390, 139) |
| 13,5–19,5 s | Page « historique haccp 📊 » : cartes par module avec compteurs (0 relevés, 0 éléments, 0 actions, 0 productions…) |

Classeur vide (démo) dans cet enregistrement — assumé volontaire (pas de données à
ajouter avant tournage, aucune remarque contraire reçue).

## Voix off (9 lignes, mesurées)

| # | Texte | Durée | Ancrage |
|---|---|---:|---|
| N0 | Ouvrir votre classeur HACCP sur FoodEatUp ? Un seul clic depuis le menu. | 5,25 s | carte d'intro |
| N1 | Cliquez sur HACCP, puis sur Accueil HACCP pour l'ouvrir. | 4,18 s | avant clic Accueil HACCP |
| N2 | D'un coup d'œil : températures, traçabilité, plan de nettoyage et production. | 4,68 s | écran d'accueil, 4 cartes |
| N3 | Et bien plus : réception, hygiène, étiquettes, documents — tout centralisé. | 5,25 s | scroll grille complète |
| N4 | Direction l'onglet Historique pour retrouver tout ce qui a été enregistré. | 4,55 s | clic Historique |
| N5 | Chaque module y laisse sa trace, prêt pour vos contrôles sanitaires. | 3,79 s | page Historique |
| N6 | Vous pouvez aussi le faire depuis Claude : copiez ce prompt, remplacez les crochets. | 4,26 s | **étage 1+2** (reveal + copié) |
| N7 | Collez-le dans Claude : votre historique HACCP s'affiche aussitôt. | 4,36 s | **étage 3** (mockup chatbot) |
| N8 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | 4,83 s | carte de fin (CTA) — ligne générique de la série |

Voix Adam FR (`TGAegA0zNRi8I6nUdq3i`), ton simple et ludique, cohérent avec le reste de
la série. N1/N3/N5/N6/N7 raccourcies d'un premier jet plus long (calibrage
"mesurer la VO avant de fixer les durées de segment", voir bug ci-dessous) pour éviter
un décalage voix/image en cascade.

## Découpage (segments retimés, offsets réels vérifiés)

| Seg | Source | Sortie | Contenu |
|---|---|---:|---|
| intro | carte | 5,90 s | OUVRIR SON CLASSEUR MODULE HACCP |
| A | 0,20 → 5,30 | 4,20 s | dashboard, curseur remonte vers le menu |
| B | 6,30 → 6,55 | 0,90 s | **zoom-punch** clic « Accueil HACCP » (975, 196) |
| C | 7,60 → 9,80 | 5,30 s | écran d'accueil classeur, 4 cartes |
| D | 9,80 → 12,30 | 6,00 s | scroll grille complète (7 modules) |
| E | 12,30 → 12,55 | 0,90 s | **zoom-punch** clic onglet « Historique » (1390, 139) |
| F | 13,60 → 19,40 | 5,60 s | page Historique, compteurs par module |
| claude1 | carte générée | 2,40 s | reveal — prompt en gros, fond crème |
| claude2 | carte générée | 1,70 s | confirmation « Copié dans le presse-papiers ! » |
| claude3 | carte générée | 3,10 s | mockup chatbot Claude (logo + bulles) |
| outro | carte | 11,13 s (auto-étendue depuis 6,20 s par le mécanisme standard de `build.py`) | CTA |

Offsets réels vérifiés (`offsets:` imprimé par `build.py`) : N0=0.30, N1=5.84, N2=10.48,
N3=15.52, N4=21.18, N5=25.95, N6=29.95, N7=34.43, N8=39.01 — chaque ligne démarre après
la fin de la précédente + GAP (0.22s), aucun chevauchement.

## Bug de synchronisation rencontré et corrigé (même piège que `foodeatup-tva-tuto`)

Premier jet : lignes VO plus longues (N3 6,69s, N6 6,53s, N7 5,51s), segments visuels
dimensionnés trop courts (ex. D à 3,00s) → cascade : chaque ligne débordait sur le
segment suivant, poussant tout en chaîne → sortie 52,12s avec **~15s de carte de fin
silencieuse** avant le début de N8. Corrigé en deux temps : (1) raccourci les lignes les
plus longues (N1/N3/N5/N6/N7, voir tableau VO ci-dessus), (2) recalibré les segments
visuels sur la durée mesurée de la ligne qu'ils portent (A 3,00→4,20s, C 3,60→5,30s, D
3,00→6,00s avec plage source élargie 9,80→12,30, F 4,20→5,60s). Résultat : sortie 44,64s,
extension d'outro ramenée à +4,93s (au lieu de +15s). Toujours un peu de silence en début
de carte CTA (~5,5s) avant N8 — acceptable, pas retouché davantage (rendement décroissant
au vu du temps disponible).

## Séquence Claude — module partagé

Pas de création de donnée visible à l'écran (classeur vide, navigation + consultation
Historique) → pas d'outil MCP `create_*` correspondant. En revanche plusieurs outils de
lecture (`list_haccp_temperatures`, `list_haccp_tracabilite`, `list_cleaning_actions`,
`list_haccp_reception`) couvrent ensemble exactement ce que montre l'onglet Historique —
prompt de consultation légitime (pas inventé) :

> Montre-moi l'historique de mon classeur HACCP (températures, traçabilité, nettoyage,
> production) pour mon établissement FoodEatUp (ID [ID établissement]).

Séquence en 3 temps via `videos/_shared/claude_prompt_sequence.py` (reveal → copié →
mockup chatbot), identique visuellement au reste de la série. Durées locales
`[2.40, 1.70, 3.10]` (vs défaut `[2.20, 1.30, 2.50]`), ajustées à N6=4,26s / N7=4,36s.

## Publication

Voir `LOVABLE-FOODEATUP-DOCS.md` pour la fiche Lovable (`ouvrir-son-classeur-haccp`,
module `haccp`) et l'entrée RapidoCMS/LinkedIn.
