# Tutoriel — Paramétrer sa TVA FoodEatUp

Module 1 « CONFIGURATION », dossier Drive `5 - vos taux de TVA`.
Durée livrée : **38,2 s** — H.264 High/yuv420p, AAC 48 kHz stéréo, faststart.
Audio : true peak **-7,2 dBFS** (mesuré sur le MP4 final).

**v3 (2026-08-02)** : script voix off amélioré (2 lignes dédiées à la séquence Claude :
une qui explique le prompt, une qui présente l'envoi dans Claude) + retiming complet des
segments A-I pour supprimer un décalage voix/image qui s'était accumulé au fil de la
vidéo (voir §"Bug de synchronisation" plus bas) + séquence Claude migrée vers le module
partagé `videos/_shared/claude_prompt_sequence.py` (même animation chatbot 3 temps que
toute la série, seul le texte du prompt change d'une vidéo à l'autre).

## Voix off (v3, 9 lignes)

| # | Texte | Durée | Ancrage |
|---|---|---:|---|
| N0 | Paramétrer sa TVA sur FoodEatUp ? Quelques secondes suffisent. | 3,79 s | carte d'intro |
| N1 | Cliquez sur Ajouter TVA pour créer votre premier taux. | 2,87 s | clic Ajouter TVA |
| N2 | Donnez-lui un nom clair et son pourcentage, puis validez. | 3,34 s | modal + clic Ajouter |
| N3 | Votre taux apparaît aussitôt, prêt à être appliqué à vos produits. | 3,76 s | liste mise à jour |
| N4 | Besoin de l'ajuster ? Cliquez sur le crayon à tout moment. | 3,29 s | clic crayon |
| N5 | Modifiez le pourcentage et sauvegardez, c'est instantané. | 3,19 s | clic Sauvegarder |
| N6 | Vous pouvez aussi le faire depuis Claude : copiez ce prompt, remplacez les crochets. | 4,41 s | **étage 1+2** (reveal + copié) |
| N7 | Collez-le dans la conversation : votre taux de TVA est créé en secondes. | 4,68 s | **étage 3** (mockup chatbot) |
| N8 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | 5,02 s | carte de fin (CTA) |

N6/N7 remplacent l'ancienne ligne unique N6 ("vous pouvez aussi créer ce taux directement
avec Claude") qui devait porter la narration sur les 3 étages à elle seule — désormais
chaque étage a sa propre ligne, alignée sur ce qu'il montre réellement.

## Découpage (targets retimés v3)

| Seg | Source | Sortie | Contenu |
|---|---|---:|---|
| intro | carte | 4,40 s | PARAMÉTRER SA TVA FOODEATUP |
| A | 0,20 → 1,40 | 2,75 s | liste vide (« Aucune TVA ») |
| B | 1,40 → 1,55 | 0,90 s | **zoom-punch** sur Ajouter TVA (1708, 351) |
| C | 2,00 → 5,90 | 3,25 s | modal, nom + pourcentage (7) |
| D | 6,30 → 6,55 | 0,90 s | **zoom-punch** sur Ajouter / submit (1204, 602) |
| E | 7,00 → 9,00 | 4,30 s | taux créé, visible dans la liste |
| F | 9,30 → 9,55 | 0,90 s | **zoom-punch** sur le crayon d'édition (1489, 537) |
| G | 10,00 → 14,90 | 3,20 s | modification du pourcentage (7 → 8) |
| H | 15,20 → 15,55 | 0,90 s | **zoom-punch** sur Sauvegarder (1172, 602) |
| I | 16,00 → 18,20 | 3,10 s | taux mis à jour (8%) |
| claude1 | carte générée | 3,00 s | reveal — prompt en gros, fond crème |
| claude2 | carte générée | 2,30 s | confirmation « Copié dans le presse-papiers ! » |
| claude3 | carte générée | 5,30 s | mockup chatbot Claude (logo + bulles) |
| outro | carte | 6,20 s | CTA (plus d'auto-extension nécessaire, voir plus bas) |

Seuls les segments "informatifs" (A, C, E, G, I, intro) ont été rallongés ; les 4 beats de
zoom-punch (B, D, F, H) restent à 0,90 s, volontairement courts et percutants.

## Bug de synchronisation voix/image (détecté et corrigé en v3)

En reconstruisant la vidéo avec les 2 nouvelles lignes N6/N7, contrôle des offsets réels
(`offsets:` imprimé par `build.py`) contre les ancrages `S[...]` : l'écart était déjà
présent avant cette passe (mêmes offsets N0-N5 dans la version précédente), mais devenait
flagrant une fois la séquence Claude scindée en deux lignes. Cause : les 6 lignes VO
N0-N5 (≈20,2 s de parole + battements GAP) dépassaient largement le temps visuel disponible
sur les segments intro+A..I (≈15,9 s), et le mécanisme de placement séquentiel
(`off = max(anchor, fin_ligne_précédente + GAP)`) reporte tout le monde en cascade dès
qu'une ligne dépasse. Résultat mesuré avant correction : N4 ("cliquez sur le crayon")
démarrait à 14,95 s alors que le clic sur le crayon (segment F) avait lieu à 10,08 s — la
voix décrivait un clic déjà passé depuis ~5 s, et pire, N6/N7 (la nouvelle séquence Claude)
tombaient respectivement sur le mockup chatbot et sur la carte de sortie au lieu de leurs
propres étages.

Corrigé en retimant les segments non-cliqués (voir tableau ci-dessus) pour que chaque ligne
VO se termine avant l'ancrage de la suivante — calcul fait à la main à partir des durées
mesurées de chaque `.mp3`, en remontant la chaîne depuis N0. Résultat vérifié après
retiming : **zéro écart**, chaque offset réel == son ancrage exact (contrôlé programmatiquement
avec `build.S`), et l'auto-extension de l'outro n'est plus nécessaire (elle absorbait
jusqu'ici tout le décalage cumulé). Confirmé aussi visuellement par extraction de frame aux
timestamps N6 (22,8 s → carte reveal) et N7 (27,8 s → mockup chatbot) : chaque ligne tombe
bien sur son propre étage.

## Séquence Claude — module partagé (2026-08-02)

`mcp__FoodEatUp__create_tva(establishment_id, name, percentage)` existe. La séquence en 3
temps (reveal → copié → mockup chatbot Claude) vit désormais dans
`videos/_shared/claude_prompt_sequence.py`, réutilisée telle quelle sur toute la série —
seuls le texte du prompt (`CLAUDE_PROMPT`) et la réplique de l'assistant
(`CLAUDE_RESPONSE`) sont propres à ce tutoriel. Détail de l'animation et des bugs
`drawtext`/couleur déjà rencontrés et corrigés : voir le docstring du module et
`FOODEATUP-TUTORIELS-WORKFLOW.md` (section "Séquence de fin"). Durées de cette vidéo
(3,00 / 2,30 / 5,30 s) : override local du défaut du module ([2.20, 1.30, 2.50]), choisi
pour laisser à N6/N7 la place de se dérouler sur leur propre étage (règle : mesurer la VO
avant de fixer les durées de segment).

Prompt (identique côté vidéo et côté fiche Lovable `claudePrompt`) :

> Crée un taux de TVA nommé [nom du taux] à [pourcentage]% pour mon établissement
> FoodEatUp (ID [ID établissement]).

## Animations

Mêmes principes que les précédents : Ken Burns sur les cartes, xfade (0,28 s), bandeaux
d'étape, encadré orange pulsant sur les 4 clics. Pas de clip avatar dans ce dossier.

## Statut publication (2026-08-02)

Vidéo livrée à Michael pour validation (règle : plus aucune publication RapidoCMS/
LinkedIn/Lovable sans validation explicite au préalable). En attente de retour avant
upload RapidoCMS (remplacement du draft LinkedIn #543, prévu 2026-08-05 07h) et mise à
jour de la fiche Lovable `parametrer-sa-tva`.
