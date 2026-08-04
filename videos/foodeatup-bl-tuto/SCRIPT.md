# Tutoriel — Valider son BL en détail FoodEatUp

Module Lovable `hubrise-livraisons` (HubRise & Livraisons). Durée livrée : **49,3 s** —
H.264 High/yuv420p, AAC 48 kHz stéréo, faststart. Audio : true peak **-7,3 dBFS**.
Decode 0 erreur, moov avant mdat (faststart confirmé).

## Ce que montre le rush

Rush (28,08 s, fourni par Michael, piste audio quasi silencieuse -91dB — pas de
narration native) : liste « Gestion des livraisons » filtrée sur Expédiée →
clic sur Filtrer → sélection du statut Livrée → liste filtrée avec bouton
« Voir le détail » → clic → détail de la commande (fournisseur, mode de
livraison, dates prévue/effective, prix) → scroll vers le tableau « Produits
livrés » (quantité commandée vs reçue + température) et la section Facture.

**Piège rencontré** : le rush scrolle vers le bas jusqu'au tableau (~23,3 →
24,8 s) puis **remonte en haut de page** (~25 s → fin, 28,08 s) avant la fin de
l'enregistrement. Une première passe de montage utilisait par erreur la plage
25,00-28,08 (déjà remontée en haut) pour les segments « quantité/température »
et « facture » — le tableau n'y apparaît plus. Corrigé en pointant ces deux
segments sur la fenêtre réellement scrollée (23,30-24,80 s), repérée en
extrayant des frames à 0,3 s d'intervalle.

## Voix off (9 lignes)

| # | Texte | Durée | Segment |
|---|---|---:|---|
| N0 | Une livraison vient d'arriver ? Voici comment valider son bon de livraison en détail sur FoodEatUp. | 5,43 s | intro |
| N1 | Dans Gestion des livraisons, filtrez par statut : en attente, expédiée ou livrée. | 4,73 s | A + clic B (Filtrer) |
| N2 | Cliquez sur Voir le détail pour ouvrir le bon de livraison d'une commande reçue. | 4,44 s | D (liste filtrée Livrée) |
| N3 | Retrouvez le fournisseur, le mode de livraison, la date prévue et la date effective. | 4,41 s | F (détail, haut de page) |
| N4 | Comparez chaque produit : quantité commandée, quantité reçue et température relevée. | 4,96 s | G1 (tableau Produits livrés) |
| N5 | Ajoutez la facture correspondante pour boucler le suivi comptable de la livraison. | 4,13 s | G2 (section Facture) |
| N6 | Vous pouvez aussi enregistrer ce contrôle depuis Claude : copiez ce prompt, remplacez les crochets. | 5,56 s | étages 1+2 |
| N7 | Collez-le dans la conversation : votre contrôle de réception est enregistré en quelques secondes. | 5,09 s | étage 3 |
| N8 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | 5,02 s | carte de fin (CTA, réutilisée) |

N8 réutilisé tel quel depuis `foodeatup-vitrine-tuto/vo/` (texte générique — zéro
crédit ElevenLabs dépensé). N0-N7 générés via ElevenLabs, voix Adam FR
(`TGAegA0zNRi8I6nUdq3i`), `eleven_multilingual_v2`.

## Découpage

| Seg | Source | Sortie | Contenu |
|---|---|---:|---|
| intro | carte | 2,80 s | VALIDER SON BL EN DÉTAIL |
| A | 0,50 → 9,50 | 4,20 s | liste « Gestion des livraisons », filtre Expédiée |
| B | 9,50 → 11,90 | 0,90 s | **zoom-punch** sur Filtrer (1493, 343) |
| C | 11,90 → 13,40 | 1,30 s | **zoom-punch** sur l'option Livrée (1580, 371) |
| D | 18,50 → 19,90 | 4,60 s | liste filtrée Livrée, boutons Voir le détail |
| E | 19,90 → 20,40 | 0,90 s | **zoom-punch** sur Voir le détail (372, 570) |
| F | 21,50 → 23,30 | 5,00 s | détail commande : fournisseur, mode, dates, prix |
| G1 | 23,30 → 24,10 | 5,80 s | tableau Produits livrés (lait, 6000l/6000l, N/A) |
| G2 | 24,10 → 24,80 | 4,80 s | section Facture (+ Ajouter une facture) |
| claude1 | carte générée | 6,50 s | reveal — prompt en gros, fond crème |
| claude2 | carte générée | 3,00 s | confirmation « Copié dans le presse-papiers ! » |
| claude3 | carte générée | 6,50 s | mockup chatbot Claude |
| outro | carte | 6,20 s | CTA |

Coordonnées des boutons eyeballées sur frames extraites (pas de script de
seuillage colorimétrique cette fois, marge gardée large avec le zoom 1.20x).

## Séquence Claude — module partagé

`mcp__FoodEatUp__create_haccp_reception(establishment_id, date_controle,
heure_controle, etat_livraison, fournisseur_id?, fournisseur_nom?,
reference_bl?, temperature_produits_frais?, commentaires?, validate?)` —
schéma vérifié, correspond exactement à ce que montre le rush (contrôle de
réception HACCP à l'arrivée fournisseur) :

> Crée un contrôle de réception pour le fournisseur [nom du fournisseur],
> référence BL [référence BL], livraison [conforme/non conforme], température
> produits frais [température]°C, pour mon établissement FoodEatUp (ID [ID
> établissement]).

Même texte côté fiche Lovable (`claudePrompt`).

## Animations

Mêmes principes que toute la série : Ken Burns sur les cartes, xfade (0,28 s),
bandeaux d'étape, encadré orange pulsant sur les 3 clics. Pas de clip avatar
dans ce dossier (VO ElevenLabs uniquement, comme `produits-tuto`/`tva-tuto`).

## Statut publication

**Script validé par Michael le 2026-08-03 avant génération voix (STOP
obligatoire respecté).** Montage terminé, checklist de compatibilité passée.
**En attente de validation de la vidéo montée par Michael** (2e STOP
obligatoire, voir `FOODEATUP-TUTORIELS-WORKFLOW.md`) avant toute publication
RapidoCMS / LinkedIn / Lovable.
