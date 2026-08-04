# Tutoriel — Commander et envoyer sa liste de courses au fournisseur

Module StockVision AI. Durée livrée : **47,68 s** — H.264 High/yuv420p, AAC 48 kHz
stéréo, faststart. Audio : true peak **-7,2 dBFS**.

## Voix off (9 lignes)

| # | Texte | Durée | Ancrage |
|---|---|---:|---|
| N0 | Envoyer sa commande au fournisseur, ça prend quelques secondes sur FoodEatUp. | 4,02 s | carte d'intro |
| N1 | Votre liste de courses regroupe tous vos produits par fournisseur, avec le total et les urgences. | 5,56 s | état liste |
| N2 | Cliquez sur Commander pour passer toutes vos commandes fournisseurs en un seul clic. | 4,08 s | clic Commander + modale |
| N3 | Vous préférez les prévenir par email ? Cliquez sur Email : chaque fournisseur reçoit sa propre liste. | 5,80 s | clic Email + détail |
| N4 | Choisissez la date de livraison souhaitée, puis envoyez à tous vos fournisseurs en un clic. | 4,73 s | clic Envoyer à tous + modale date |
| N5 | Fini les appels et les oublis : vos fournisseurs reçoivent la bonne quantité, au bon moment. | 5,20 s | bénéfice |
| N6 *(réutilisé depuis foodeatup-fournisseurs-tuto)* | Vous pouvez aussi le faire depuis Claude : copiez ce prompt, remplacez les crochets. | 4,41 s | étage 1+2 Claude |
| N7 | Collez-le dans la conversation : votre commande fournisseur est créée en quelques secondes. | 4,49 s | étage 3 Claude |
| N8 *(réutilisé depuis foodeatup-fournisseurs-tuto)* | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | 5,02 s | carte de fin (CTA) |

## Découpage

| Seg | Source | Sortie | Contenu |
|---|---|---:|---|
| intro | carte | 4,70 s | ENVOYER SA COMMANDE AU FOURNISSEUR |
| A | 0,20 → 3,90 | 6,10 s | Liste des courses : 469 produits / 23 fournisseurs, groupés par fournisseur |
| B | 3,90 → 4,15 | 0,90 s | **zoom-punch** sur Commander (23) (1687, 194) |
| C | 5,60 → 6,10 | 4,00 s | Modale « Commander tous les produits ? » (469 produits / 23 fournisseurs) |
| D | 12,20 → 12,45 | 0,90 s | **zoom-punch** sur Email (1457, 352) |
| E | 12,80 → 16,20 | 5,70 s | Détail par fournisseur : produit / quantité / unité |
| F | 17,60 → 17,85 | 0,90 s | **zoom-punch** sur Envoyer à tous les fournisseurs (1596, 181) |
| G | 18,00 → 21,00 | 4,65 s | Modale date/heure de livraison souhaitée |
| H | 24,40 → 24,65 | 0,90 s | **zoom-punch** sur Envoyer à tous (22) (860, 643) |
| I | 26,00 → 29,00 | 5,10 s | Retour à la page email, fournisseurs prévenus |
| claude1 | carte générée | 3,00 s | reveal — prompt en gros, fond crème |
| claude2 | carte générée | 2,30 s | confirmation « Copié dans le presse-papiers ! » |
| claude3 | carte générée | 5,30 s | mockup chatbot Claude |
| outro | carte | 6,20 s | CTA |

Coordonnées mesurées par seuillage colorimétrique sur les frames réelles (script Python
PIL, pas à l'œil — voir `build.py`). **Piège rencontré et corrigé pendant cette passe** :
la mise en page se décale verticalement entre le début du rush (boutons Email/Commander
à y≈194) et t≈12 s (mêmes boutons à y≈352, barre de chargement/skeleton supplémentaire
au-dessus de la nav) — un premier zoom-punch sur Email réutilisait par erreur la
coordonnée mesurée à t≈4 s et tombait sur une zone vide ; corrigé en mesurant chaque
bouton à l'instant réel de son clic. Un premier zoom-punch sur Commander (23) était
lui-même tombé sur « Vider la liste » (mauvaise lecture de coordonnée à l'œil) —
corrigé en systématisant la mesure par bbox colorimétrique.

Le clic de confirmation dans la modale « Commander tous les produits ? » (segment C)
n'a pas de zoom-punch : le rush ne montre pas clairement un clic confirmé sur
« Commander tout » avant la fermeture de la modale (probablement « Annuler », la liste
reste inchangée à 469 produits) — pas de clic asserté qui ne serait pas réellement
visible à l'écran.

## Séquence Claude — module partagé

`mcp__FoodEatUp__create_supplier_order(establishment_id, fournisseur_id, items[], date_prevue, note)`
existe — schéma vérifié avant rédaction du prompt.

> Crée une commande auprès de mon fournisseur [nom du fournisseur] avec les produits
> [liste des produits et quantités], livraison prévue le [date de livraison], pour mon
> établissement FoodEatUp (ID [ID établissement]).

Même texte côté fiche Lovable (`claudePrompt`).

## Animations

Mêmes principes que toute la série : Ken Burns sur les cartes, xfade (0,28 s), bandeaux
d'étape, encadré orange pulsant sur les 4 clics. Pas de clip avatar dans ce dossier.

## Statut publication

Validée par l'utilisateur ("tu peux publier"). RapidoCMS + LinkedIn + Lovable en cours.
