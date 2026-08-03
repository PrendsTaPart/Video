# Tutoriel — Tenir sa liste de courses FoodEatUp

Module StockVisionAI, écran « Liste des courses ». Rush unique et continu
(60,28 s) : ajout d'un produit (lait, 5000 l, fournisseur Laiterie du Cap
Bon) → modification de sa quantité (5000 → 6000) → suppression (la liste
revient à son état initial : 9 produit(s) / 2 fournisseur(s) / 355 245,00 €).

## Voix off (9 lignes)

| # | Texte | Durée | Segment | Origine |
|---|---|---:|---|---|
| N0 | Tenir votre liste de courses à jour dans FoodEatUp, c'est très simple. | 3,66 s | intro + A | ElevenLabs Adam |
| N1 | Cliquez sur Ajouter produit, choisissez l'article, sa quantité et son fournisseur. | 4,49 s | C — remplissage du formulaire d'ajout | Piper (fallback, voir note) |
| N2 | Besoin de corriger une quantité ? Cliquez sur le crayon. | 3,71 s | E/F — clic sur le crayon (édition) | Piper |
| N3 | Modifiez le chiffre et validez : le stock est mis à jour aussitôt. | 4,02 s | G/H — édition de la quantité | Piper |
| N4 | Un produit à retirer ? La corbeille le supprime en un clic. | 3,87 s | I/J/K/L — suppression | Piper |
| N5 | Votre liste reste toujours juste, prête à être commandée à vos fournisseurs. | 4,31 s | M — bénéfice | Piper |
| N6 | Vous pouvez aussi le faire depuis Claude : copiez ce prompt, remplacez les crochets. | 4,41 s | étages 1+2 (réutilisé) | ElevenLabs Adam (réutilisé) |
| N7 | Collez-le dans la conversation : votre commande fournisseur est prête en quelques secondes. | 4,36 s | étage 3 | Piper |
| N8 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | 5,02 s | carte de fin (CTA, réutilisé) | ElevenLabs Adam (réutilisé) |

**Note importante — voix mixte sur cette vidéo.** Le quota ElevenLabs du
compte s'est épuisé en cours de production (35 crédits restants, 56 à 91
requis par ligne — confirmé après échec de deux appels, y compris avec le
modèle `eleven_flash_v2_5`, moins coûteux). N0/N6/N8 sont de la vraie voix
Adam FR ElevenLabs (N6/N8 réutilisés tels quels depuis
`foodeatup-produits-tuto/vo/`, N0 généré avant l'épuisement du quota). Faute
de crédits, **N1 à N5 et N7 ont été générés en secours avec Piper**
(`fr_FR-upmc-medium`, moteur neuronal local hors-ligne, voix masculine
française) — qualité correcte mais **perceptiblement différente** du grain
Adam habituel de la série. À régénérer en Adam ElevenLabs dès que le quota du
compte est reconstitué, pour une voix homogène sur toute la vidéo.

## Découpage

| Seg | Source | Sortie | Contenu |
|---|---|---:|---|
| intro | carte | 2,60 s | TENIR SA LISTE DE COURSES |
| A | 0,50 → 3,00 | 2,60 s | liste initiale (9 produit(s), 2 fournisseur(s), 355 245,00 €) |
| B | 3,00 → 3,35 | 0,90 s | **zoom-punch** sur + Ajouter produit (1456, 492) |
| C | 6,00 → 33,10 | 4,40 s | formulaire : « lait » (produit existant), quantité 5000, unité l, fournisseur → Laiterie du Cap Bon |
| D | 33,10 → 33,45 | 0,90 s | **zoom-punch** sur Ajouter (modal, 1035, 683) |
| E | 34,00 → 38,60 | 2,30 s | toast « Ajouté ! » + liste rafraîchie (Laiterie du Cap Bon / Lait) |
| F | 38,60 → 38,95 | 0,90 s | **zoom-punch** sur le crayon (554, 296) |
| G | 39,50 → 46,10 | 3,10 s | modale Modifier lait : quantité 5000 → 6000 |
| H | 46,10 → 46,45 | 0,90 s | **zoom-punch** sur Modifier (872, 607) |
| I | 47,00 → 52,60 | 2,60 s | toast « Modifié ! » + liste (coût 4 800,00 €) |
| J | 52,60 → 52,95 | 0,90 s | **zoom-punch** sur la corbeille (594, 297) |
| K | 53,50 → 54,30 | 1,10 s | dialogue « Supprimer ce produit ? » |
| L | 54,30 → 54,65 | 0,90 s | **zoom-punch** sur Supprimer (872, 553) |
| M | 55,00 → 59,50 | 3,00 s | toast « Supprimé ! » + liste revenue à l'état initial |
| claude1 | carte générée | 2,60 s | reveal — prompt en gros, fond crème |
| claude2 | carte générée | 2,00 s | confirmation « Copié dans le presse-papiers ! » |
| claude3 | carte générée | 5,00 s | mockup chatbot Claude |
| outro | carte | 6,20 s (auto-étendue si besoin) | CTA |

Coordonnées mesurées par seuillage colorimétrique sur les frames réelles
(boutons bleu `#1B6DF3` et rouge de confirmation) ; icônes crayon/corbeille
recoupées visuellement sur les mêmes frames (bounding boxes des boutons
adjacents cohérentes à quelques px près avec l'estimation visuelle).

## Séquence Claude — module partagé

`mcp__FoodEatUp__create_supplier_order(establishment_id, fournisseur_id,
items[{ingredient_id, quantity, unit}], date_prevue?, note?)` est l'outil qui
correspond le mieux à ce que montre le rush : construire une liste de
courses par fournisseur puis la transformer en commande — la suite logique
de l'ajout/édition montré à l'écran.

> Crée une commande fournisseur pour [nom fournisseur] avec [quantité]
> [unité] de [produit], pour mon établissement FoodEatUp (ID [ID
> établissement]).

Même texte côté fiche Lovable (`claudePrompt`).

## Animations

Mêmes principes que toute la série : Ken Burns sur les cartes, xfade
(0,28 s), bandeaux d'étape (pas d'apostrophe), encadré orange pulsant sur les
6 clics (3 icônes d'accès + leurs 3 boutons de soumission/confirmation). Pas
de clip avatar dans ce dossier.

## Statut publication

Vidéo montée et poussée sur la branche de travail. Session ayant reçu
instruction explicite de publier (site Lovable FoodEatUp Academy) sans
étape de validation manuelle intermédiaire — dérogation à la règle standing
« ne pas publier sans retour explicite de Michael » (voir
`LOVABLE-FOODEATUP-DOCS.md`), documentée ici pour traçabilité. Signaler à
Michael la voix Piper mixte (N1-N5, N7) pour arbitrage sur une regénération
ElevenLabs ultérieure.
