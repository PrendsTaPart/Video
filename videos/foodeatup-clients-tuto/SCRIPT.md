# Tutoriel — Gérer ses clients côté ventes FoodEatUp

Deuxième vidéo du module `comptabilite` (Comptabilité & Achats), section
"Fournisseurs & clients" — juste après `gerer-ses-fournisseurs-cote-achats`
(order 1). Fiche déjà présente en placeholder dans `tutorials.ts`
(`gerer-ses-clients-cote-ventes`, vignette déjà hébergée sur le CDN Lovable) :
cette livraison la complète. Durée livrée : **42,32 s** — H.264 High/yuv420p,
AAC 48 kHz stéréo, faststart. Audio : true peak **-7,17 dBFS**. moov avant
mdat (faststart confirmé).

## Ce que montre le rush

Le rush (47,64 s, 1920x828, fourni par Michael sous le nom
`Ajout_et_modificationsSuppression_dun_client.mp4`) montre, depuis "Gestion
des clients" :
1. Clic "Ajouter un nouveau client" → formulaire complet : identité (Jean
   Dupont), coordonnées (email, téléphone), adresse (autocomplétion pays/code
   postal/ville), puis en option date de naissance, genre, TVA, SIRET, canal
   d'acquisition (Instagram) → "Enregistrer le client" → apparaît aussitôt
   dans la liste.
2. Sur une fiche client existante (démo "Jean dupont", distincte de celle
   qu'on vient de créer) : clic "Modifier" → formulaire pré-rempli éditable.
3. Menu "..." de la carte → "Options avancées" : facture/devis par défaut,
   bon de commande, commercial associé, notifications automatiques.
4. Menu "..." → "Voir détails" : panneau latéral avec coordonnées et
   informations générales (TVA, SIRET, ville, pays, date d'ajout).
5. Clic "Supprimer" → modale de confirmation "Supprimer ce client ?" listant
   ce qui sera perdu (facturation, devis/BC/factures, toutes les données) →
   **"Annuler"** — la suppression n'est **pas** confirmée dans le rush, comme
   sur la vidéo jumelle fournisseurs (les données de démo restent intactes).

## Voix off (9 lignes, voix Adam FR `TGAegA0zNRi8I6nUdq3i`, `eleven_multilingual_v2`)

| # | Texte | Durée | Segment |
|---|---|---:|---|
| N0 | Gérer ses clients, aussi vu côté ventes et comptabilité. | 3,19 s | intro |
| N1 | Retrouvez la liste de vos clients, prête à facturer. | 2,77 s | A — liste |
| N2 | Ajoutez un client : identité, coordonnées et adresse, qui se complète automatiquement. | 5,02 s | C1 — montage saisie |
| N3 | En option, précisez sa date de naissance, sa TVA, son SIRET et son canal d'acquisition. | 5,67 s | C2 — détails & facturation |
| N4 | Il apparaît aussitôt dans la liste. | 1,91 s | E — ajouté |
| N5 | Modifiez-le à tout moment, puis choisissez ses options avancées : facture, devis, commercial associé. | 5,85 s | H+I — modifier puis options avancées |
| N6 | Retrouvez sa fiche complète en un clic, avec toutes ses informations. | 3,66 s | J — fiche détaillée |
| N7 | Avant toute suppression, FoodEatUp vous redemande toujours confirmation — une sécurité contre l'erreur irréversible. | 6,40 s | L — modale de suppression |
| N8 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | 5,02 s | carte de fin (CTA, réutilisée telle quelle depuis `foodeatup-fournisseurs-achats-tuto`, 0 crédit ElevenLabs) |

N8 réutilisée tel quel. Drift max ≤2,9 s sur les dernières lignes — l'outro
s'auto-étend (6,20 → 9,01 s) pour caler le CTA, comportement normal déjà
documenté sur la série (`foodeatup-fournisseurs-achats-tuto`).

## Découpage

| Seg | Source | Sortie | Contenu |
|---|---|---:|---|
| intro | carte (`assets/intro.jpg`, fournie par Michael) | 3,20 s | GÉRER SES CLIENTS CÔTÉ VENTES |
| A | 0,20 → 1,90 | 2,60 s | "Gestion des clients", état initial |
| B | 1,90 → 2,20 | 0,80 s | **zoom-punch** "Ajouter un nouveau client" (1601, 183) |
| C1 | 2,20 → 20,00 | 4,80 s | montage accéléré : identité, coordonnées, adresse |
| C2 | 20,00 → 27,80 | 5,40 s | montage : détails & facturation optionnels |
| D | 27,80 → 28,30 | 0,80 s | **zoom-punch** "Enregistrer le client" (1032, 722) |
| E | 28,30 → 29,60 | 1,80 s | client ajouté à la liste |
| G | 36,30 → 36,90 | 0,80 s | **zoom-punch** "Modifier" carte Jean dupont (1621, 648) |
| H | 36,90 → 39,60 | 2,80 s | formulaire de modification |
| I | 42,70 → 44,30 | 3,30 s | modale "Options avancées du client" |
| J | 40,20 → 41,85 | 3,40 s | panneau "Fiche détaillée" |
| K | 45,50 → 45,70 | 0,70 s | **zoom-punch** "Supprimer" carte Jean dupont (1361, 648) |
| L | image fixe (`assets/delete-confirm.jpg`, extraite du rush à 46,2 s) | 5,80 s | modale "Supprimer ce client ?" — **carte statique**, pas de rush étiré (le dialogue n'anime pas, un `setpts` à ce facteur aurait produit un ralenti artificiel non naturel) |
| M | 46,80 → 47,00 | 0,70 s | **zoom-punch** "Annuler" (861, 745) |
| outro | carte (`assets/outro.jpg`, fournie par Michael) | 9,01 s (auto-étendue) | CTA |

Les segments H/I/J/K/L/M sont réordonnés par rapport à l'ordre brut du rush
(qui montre Modifier → Voir détails → Options avancées → Supprimer) pour
coller au texte validé (Modifier+Options avancées → Fiche détaillée →
Suppression) : ce sont 4 actions indépendantes sur la même carte démo, leur
réordonnancement au montage ne change rien à ce qu'elles montrent réellement.
Coordonnées de clic mesurées sur les frames extraites du rush (diff `ffmpeg
fps=5` + frames ciblées), résolution source native 1920x828.

## claudePrompts — cas d'usage

`mcp__FoodEatUp__create_client` / `update_client` / `list_clients` +
`get_client` — schémas vérifiés avant rédaction, les champs correspondent à
ce que montre le rush (nom, prénom, email, num_tel, adresse, code_postal,
ville, pays, numero_tva, siret). Pas d'outil `delete_client` exposé dans les
prompts (cohérent avec le rush qui ne confirme jamais la suppression). 3
`claudePrompts`, calqués sur le jumeau fournisseurs :
1. Créer un client directement (`create_client`).
2. Modifier un client (`update_client`).
3. Vérifier un client avant de facturer (`list_clients` + `get_client`).

## Astuce du chef (Lovable) — capacités non montrées dans ce rush

À la demande de Michael : chaque fiche client alimente aussi les devis, les
factures et le compte fidélité, et sert de base à la segmentation RFM
(clients fidèles / à risque / occasionnels...). Cette base clients — enrichie
automatiquement depuis tous les canaux de vente (site web, QR code à table,
agent vocal) — est aussi le socle des campagnes marketing : SMS, jeux
concours, sondages, pour faire revenir ses clients via le module Marketing,
Fidélité & Iris. Aucune de ces capacités n'est visible dans le rush (qui ne
montre que la fiche client elle-même) : documentées ici plutôt qu'inventées à
l'image, même principe que sur `foodeatup-fournisseurs-achats-tuto`.

## Animations

Mêmes principes que toute la série : Ken Burns sur les cartes, xfade (0,28 s,
`fade` uniquement — même écran d'un bout à l'autre, y compris le saut de
pagination pour retrouver la carte de démo), bandeaux d'étape (rendus en PNG
via PIL puis glissés avec `overlay`, `drawbox` n'évaluant pas `t` sur ffmpeg
6.1.1 — piège documenté dans `FOODEATUP-TUTORIELS-WORKFLOW.md`), encadré
orange pulsant sur les 6 clics. Pas de séquence Claude animée (3
`claudePrompts` texte suffisent, comme sur le jumeau). Pas de clip avatar.

## Statut publication

Montage terminé, checklist de compatibilité passée (H.264 High/yuv420p, AAC
48 kHz stéréo, faststart, peak -7,17 dBFS). **En attente de validation par
Michael avant publication** (règle du workflow) : livré via `SendUserFile`,
commit/push du dossier projet sur la branche
`claude/foodeatup-video-tutorials-qclxxe`. Pas encore uploadé sur
RapidoCMS/LinkedIn ni mis à jour dans `tutorials.ts` — en attente d'un retour
explicite.
