# Tutoriel — Contrôler à réception de vos livraisons (Module HACCP)

Dossier Drive / module « Hygiène & HACCP ». Rush fourni : `Contrôle_a_réception_de_vos_livraison.mp4`
(1920x828, 25fps, 34,80 s). Intro fournie : `CONTRÔLER À RÉCEPTION DE LIVRAISON.jpg`.
Outro CTA générique (réutilisée telle quelle).

Pas d'avatar sur ce rush — VO ElevenLabs (Adam FR, `TGAegA0zNRi8I6nUdq3i`) sur toute la vidéo.

## Déroulé observé dans le rush (analyse frame-by-frame, 1fps + zooms)

| t≈ | Écran |
|---|---|
| 0-2s | « Réception du jour » : grille de commandes (64 Total, 0 Contrôlé(s), 60 En attente), bouton « Contrôle à réception » en haut à droite |
| 2-6,5s | Ouverture d'une commande livrée (`#CMD-20260615104456-109 · louay`) : Fournisseur, Référence, Statut « Livrée », Date, Température, table « Produits livrés » (Farine de blé T55, 200kg commandé / 199kg reçu) |
| 6,5-6,85s | Clic sur le menu **« … »** de la ligne produit |
| 6,85-14s | Modale **Photo DLC** (prendre une photo / importer depuis la galerie, date DLC optionnelle) |
| 14-18s | Modale **DLC manuelle** (date limite de consommation) |
| 18-21,5s | Modale **Température** (stepper, ex. +4,0°C) |
| 21,5-26,5s | Modale **Scanner produit** (ouverture caméra, cadre de scan code-barres) |
| 26,5-28,6s | Retour au détail de la commande |
| 28,6-28,95s | Clic sur **« Contrôle à réception »** (bouton bleu, en haut à droite) |
| 28,95-34,8s | Formulaire **« Nouvelle réception »** : Date de contrôle / Heure de contrôle, Bon de livraison (photo), Référence (pré-remplie), Fournisseur ; en scrollant : tags de catégories produits, **État de livraison** (Conforme ✓), Commentaires, boutons Annuler / Étape suivante |

Le même composant modale (Nom/Type-like) sert pour les 4 actions produit (Photo DLC / DLC
manuelle / Température / Scanner produit) — ce sont des annotations au niveau de la ligne
produit, distinctes du formulaire global « Contrôle à réception ».

## Voix off (9 lignes)

| # | Texte | Segment | Notes |
|---|---|---|---|
| N0 | Contrôler une livraison à réception ? FoodEatUp centralise tout, produit par produit. | intro + A | accroche |
| N1 | Ouvrez une commande livrée pour voir son détail : fournisseur, référence et produits reçus. | B | |
| N2 | Sur un produit, ouvrez le menu Action pour photographier la DLC, la saisir manuellement, noter la température ou scanner le code-barres. | C(clic)+D+E+F+G | couvre les 4 sous-actions produit |
| N3 | Prêt à valider ? Cliquez sur « Contrôle à réception ». | H+I(clic) | |
| N4 | Renseignez la date, l'heure, une photo du bon de livraison et le fournisseur. | J1 | |
| N5 | Indiquez l'état de la livraison — conforme ou non conforme — ajoutez un commentaire, puis passez à l'étape suivante. | J2 | |
| N6 | Vous pouvez aussi le faire depuis Claude : copiez ce prompt, remplacez les crochets. | séquence Claude étages 1+2 | **réutilisée telle quelle** (identique aux autres tutos) |
| N7 | Collez-le dans la conversation : votre contrôle à réception est enregistré en quelques secondes. | séquence Claude étage 3 | spécifique à ce tuto |
| N8 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | carte de fin (CTA) | **réutilisée telle quelle** |

## Séquence Claude — outil MCP correspondant

`create_haccp_reception(establishment_id, date_controle, heure_controle, etat_livraison,
fournisseur_nom, reference_bl, temperature_produits_frais, commentaires, validate)`
correspond exactement au formulaire « Nouvelle réception » montré dans le rush (seule action
de cette vidéo qui a un outil MCP dédié — les 4 actions produit Photo DLC / DLC manuelle /
Température / Scanner produit n'ont pas d'équivalent MCP, donc pas de prompt pour elles).

> Enregistre un contrôle à réception pour la commande [référence BL] du fournisseur [nom du
> fournisseur], livraison [conforme / non conforme], le [date] à [heure], pour mon
> établissement FoodEatUp (ID [ID établissement]).

Même texte côté fiche Lovable (`claudePrompt`).

## Statut build (2026-08-04)

Durée livrée : **50,72 s**. Checklist de compatibilité passée : H.264 High/yuv420p,
AAC LC 48 kHz stéréo, faststart (moov avant mdat), 0 erreur de décodage, true peak
**-7,16 dBFS**. Offsets VO calculés sans dérive (`drift: none -- all lines on their
anchors`).

## Fiche Lovable

- **slug** : `controler-reception-livraisons`
- **title** : Contrôler à réception de vos livraisons (Module HACCP)
- **moduleSlug** : `haccp`
- **subcategory** : Contrôle à réception : produits, DLC, température, conformité
- **whatItsFor** : Contrôler chaque livraison au moment où elle arrive — DLC, température et
  conformité produit par produit — puis valider un contrôle à réception complet, daté et
  horodaté, sans registre papier.
- **chefTip** : Les actions rapides sur chaque produit (Photo DLC, DLC manuelle, Température,
  Scanner produit) sont indépendantes du contrôle global : vous pouvez les utiliser au fil de
  la réception, produit par produit, avant même d'ouvrir le formulaire « Contrôle à réception ».
  Et si un produit pose problème, choisissez "Non conforme" dans le formulaire plutôt que de
  valider par réflexe — c'est ce statut qui déclenche votre traçabilité des non-conformités
  fournisseur, à réutiliser lors du prochain arbitrage avec ce fournisseur.
- **chefTipAvatar** : `michael-chef-mascot.jpg`

## Statut

Vidéo montée et publiée à la demande de Michael (workflow complet demandé dans le même
message : montage, VO, séquence Claude, publication Lovable, mise à jour du dépôt).
