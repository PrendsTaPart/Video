# Tutoriel — Lire ses mouvements de stock FoodEatUp

Module `stockvision-ai`, dossier Drive « Mouvements de stock / Détails / Supprimer ».
Rush source : 24,08 s, 1920x828, 25 fps.
Durée livrée : **46,32 s** — H.264 High/yuv420p, AAC 48 kHz stéréo, faststart
(moov en tête). Audio : true peak **-7,3 dBFS**. Decode 0 erreur.

## Voix off (9 lignes, Adam FR `TGAegA0zNRi8I6nUdq3i`)

| # | Texte | Durée | Ancrage |
|---|---|---:|---|
| N0 | Vos mouvements de stock, c'est l'historique de tout ce qui entre et sort de votre cuisine. | 4,21 s | carte d'intro |
| N1 | Dans Gestion des stocks, chaque ligne indique le produit, la quantité, le motif et la date. | 5,51 s | A (liste) |
| N2 | Ouvrez le menu Action de la ligne, puis cliquez sur Voir détails. | 3,47 s | B + C + D (clics) |
| N3 | La fiche complète s'affiche, avec l'heure exacte de la saisie et l'utilisateur qui l'a faite. | 5,33 s | E (page détail) |
| N4 | Une erreur ? Cliquez sur Supprimer, en haut à droite. | 3,34 s | F + G |
| N5 | Confirmez : la suppression corrige aussi votre stock, votre registre reste toujours juste. | 4,78 s | H + I |
| N6 | Vous pouvez aussi le faire depuis Claude : copiez ce prompt, remplacez les crochets. | 4,41 s | étages 1+2 (**réutilisé** de tva) |
| N7 | Collez-le dans la conversation : votre stock est lu et corrigé en quelques secondes. | 4,60 s | étage 3 |
| N8 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | 5,02 s | carte de fin (**réutilisé** de tva) |

N1 a été regénérée plus courte que la première version (7,05 s → 5,51 s) : la ligne
d'origine énumérait les 7 colonnes du tableau et aurait forcé le segment A (4,05 s de
rush) à tourner à 0,55x. `build.py` imprime `drift vs anchors` et **s'arrête** si une
ligne ne démarre pas sur son ancrage — sortie actuelle : `none -- all lines on their
anchors`.

N6 et N8 sont réutilisés tels quels depuis `foodeatup-tva-tuto/vo/` (lignes génériques).
N7 est spécifique à ce tutoriel — relu avant usage, il nomme bien le stock et pas un
autre objet (piège rencontré sur `foodeatup-fournisseurs-tuto`).

## Déroulé exact du rush (mesuré image par image)

| t source | Événement |
|---:|---|
| 0,0 → 4,5 | Liste « Mouvements de Stock » — 1 ligne : Chocolat / Entrée / 5000 pièce / Réception commande / Carrefour / 23/07/2026 / dupont jean |
| ~4,6 | **clic** menu Action (3 points) → ouverture du menu Voir détails / Modifier / Supprimer |
| ~6,2 | **clic** « Voir détails » |
| 6,9 → 11,3 | Page « Détails du Mouvement » : Informations Générales + Informations Supplémentaires |
| ~11,3 | **clic** « Supprimer » (bouton bordeaux, haut à droite) |
| 11,4 → 15,0 | Modale de confirmation « ...Cette action affectera également le stock. » |
| ~15,0 | **clic** « Confirmer » |
| 15,1 → 24,0 | Retour liste, état vide « Aucun mouvement de stock » |

Bornes modale mesurées par comptage de pixels ambre (bouton Annuler) sur un balayage
à 0,1 s : apparition 11,4 s, disparition 15,1 s.

## Coordonnées des clics (espace source 1920x828, seuillage colorimétrique)

| Bouton | Centre | Taille |
|---|---|---|
| Menu Action (3 points) | (1710, 408) | 40 x 40 |
| « Voir détails » | (1542, 451) | 190 x 40 |
| « Supprimer » (page détail) | (1718, 307) | 155 x 61 |
| « Confirmer » (modale) | (1047, 503) | 153 x 63 |

## Découpage

| Seg | Source | Sortie | Facteur | Contenu |
|---|---|---:|---:|---|
| intro | carte | 5,20 s | — | LIRE SES MOUVEMENTS DE STOCK |
| A | 0,30 → 4,35 | 6,35 s | 0,64x | liste du registre, bandeau « 1 · Le registre des mouvements » |
| B | 4,40 → 4,82 | 1,20 s | 0,35x | **zoom-punch** sur le menu Action (1710, 408) |
| C | 4,88 → 6,00 | 2,45 s | 0,46x | menu ouvert, bandeau « 2 · Voir le détail » |
| D | 6,00 → 6,32 | 1,10 s | 0,29x | **zoom-punch** sur « Voir détails » (1542, 451) |
| E | 6,90 → 11,20 | 6,15 s | 0,70x | page détail, bandeau « Produit, motif, date, utilisateur » |
| F | 11,20 → 11,55 | 0,95 s | 0,37x | **zoom-punch** sur « Supprimer » (1718, 307) |
| G | 11,60 → 14,80 | 3,40 s | 0,94x | modale de confirmation, bandeau « 3 · Confirmez la suppression » |
| H | 14,80 → 15,05 | 0,95 s | 0,26x | **zoom-punch** sur « Confirmer » (1047, 503) |
| I | 15,30 → 24,00 | 4,90 s | 1,78x | toast « Supprimé ! » puis registre vide, bandeau « Registre à jour » |
| claude1 | carte générée | 3,15 s | — | reveal — prompt en gros, fond crème |
| claude2 | carte générée | 2,30 s | — | « Copié dans le presse-papiers ! » |
| claude3 | carte générée | 5,35 s | — | mockup chatbot Claude |
| outro | carte | 6,20 s | — | CTA |

Rush court (24 s) portant ~44 s de narration : la plupart des segments tournent
légèrement sous 1x, ce qui est sans conséquence ici (écrans quasi statiques — un
tableau, une fiche, une modale). Seul le plan de fin (8,7 s d'état vide) est accéléré.

**Dimensionnement des segments** : une ligne VO couvrant les segments X..Z tient si
`somme(target) - n*XF >= ligne + amorce + GAP`. Le terme `n*XF` (recouvrement xfade,
0,28 s par coupe) avait été oublié au premier passage → 2,3 s de dérive accumulée, la
narration finissant sur le mauvais segment. `build.py` refuse désormais de produire un
fichier si `drift` n'est pas nul.

Bandeaux volontairement sans apostrophe — une apostrophe dans `banner()` casse la chaîne
`-vf` de `drawtext` (piège rencontré sur `foodeatup-ingredients-tuto`). Les accents, eux,
passent sans problème, d'où « Voir le détail » et « Registre à jour » écrits normalement.

## Bug corrigé : les bandeaux de toute la série ne s'affichaient qu'à moitié

Le `banner()` hérité dessinait la plaque bleue et le liseré orange avec **`drawbox`**, et
la position `x` était une expression animée en `t` pour l'effet de glissement. Or
**`drawbox` n'expose pas d'horodatage : dans une expression `drawbox`, `t` est l'épaisseur
du trait** — et comme le pipeline passe `t=fill`, `t` vaut un nombre énorme. Les deux
rampes `min(1, max(0, (t-…)/0.32))` saturaient donc à 1 en permanence et
`x = -640 + 700*1 - 700*1 = -640` : la plaque était garée hors champ à chaque image, sur
chaque vidéo. `drawtext`, lui, expose bien `t`, ce qui explique que le **texte** glissait
correctement — d'où des bandeaux réduits à du texte blanc sur fond de page clair, illisible.
Vérifié sur le livrable déjà publié `foodeatup-vitrine-tuto-v1.mp4` : même symptôme.

Correction : la plaque est dessinée par le `box=1` de `drawtext` lui-même (il suit le texte
et partage son `t`), en deux passes — une orange décalée de 14 px à gauche qui dépasse en
liseré, puis la bleue par-dessus. Un seul filtre animé, plus de `drawbox` dans `banner()`.
La plaque épouse maintenant la largeur du texte au lieu d'une largeur fixe de 560 px.

## Séquence Claude — module partagé

Deux outils MCP correspondent à ce que montre le rush, d'où deux prompts (`claudePrompts[]`,
comme sur `saisir-ses-ingredients`) :

1. **Lire le registre** — `list_stocks(establishment_id)` + `list_low_stocks(establishment_id)` :

   > Fais le point sur mon stock FoodEatUp (établissement [ID établissement]) : donne-moi
   > l'état de chaque article et la liste de ceux qui sont en niveau bas.

2. **Corriger une ligne** — `adjust_stock(establishment_id, ..., mode, quantity, motif)`.
   La description de l'outil est explicite : « Chaque ajustement écrit un mouvement tracé »
   — c'est exactement le registre affiché dans la vidéo :

   > Corrige mon stock de [produit ou ingrédient] : mets la quantité à [quantité],
   > motif [motif], pour mon établissement FoodEatUp (ID [ID établissement]).

C'est le prompt 2 qui est affiché dans la vidéo (le geste « corriger le registre » est
celui que montre le rush). Les deux figurent sur la fiche Lovable.

Il n'existe **pas** d'outil MCP de suppression de mouvement — aucun prompt inventé pour
ce geste, conformément à la règle du workflow.

## Statut

Script → VO → montage → livraison. Publication Lovable demandée explicitement par Michael
dans la même consigne que la commande de la vidéo.
