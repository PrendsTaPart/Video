# Tutoriel — Ajouter une réservation (module Table)

Module « Agent IA Caroline & Salle » (catégorie `caroline-reservation`), sous-module
**Réservations & Plan de salle** (`reservation-salle`, sous-catégorie « 02 · Créer &
modifier », `order: 2` — catalogue : 6b. Réservations Salle — 02 Ajouter une réservation
(module table)).

Rush unique et continu (65,86 s, 1920x828, 25 fps) fourni par Michael : page Réservations
(vue Plan de salle + File d'attente, puis bascule sur la liste "Réservations" avec ses
compteurs Total/En attente/Aujourd'hui/À venir) → clic sur « + Nouvelle réservation » →
modale « Nouvelle réservation » : nom « jean dupont », téléphone, email « jean@contact.fr »,
date 12/08/2026, heure 06:07 PM, couverts 4 → sélection d'une table (filtre « Salle
principale », table T4 choisie manuellement plutôt que l'assignation Auto) → clic sur
« Créer la réservation » → retour à la liste : la réservation de Jean Dupont apparaît en
statut « En attente » (Total 10→11, En attente 0→1, À venir 0→1) → menu d'actions ouvert sur
la ligne (Confirmer / Check-in / Modifier / No-show / Annuler / Supprimer).

## Outil MCP FoodEatUp correspondant

`mcp__FoodEatUp__create_reservation(establishment_id, customer_name, party_size, date,
time, customer_phone?, customer_email?, table_id?, zone?, notes?)` — correspond exactement
à l'action montrée à l'écran (nom, couverts, date, heure, table optionnelle). Séquence
Claude ajoutée en fin de vidéo (template partagé `videos/_shared/claude_prompt_sequence.py`,
même gabarit que le reste de la série).

## Voix off (10 lignes) — ElevenLabs Adam Instructor (`TGAegA0zNRi8I6nUdq3i`)

| # | Texte | Durée | Placement |
|---|---|---:|---|
| N0 | Ajouter une réservation dans FoodEatUp, ça se fait en quelques clics. | 3,79 s | carte d'intro |
| N1 | Depuis Réservations, cliquez sur Nouvelle réservation. | 2,82 s | A1/A2/B — vue d'ensemble + clic |
| N2 | Renseignez le nom du client, son téléphone et son email. | 3,11 s | C — coordonnées client |
| N3 | Choisissez la date, l'heure et le nombre de couverts. | 2,82 s | D — créneau |
| N4 | FoodEatUp propose les tables disponibles : laissez l'assignation automatique, ou choisissez-en une précisément. | 6,09 s | E/F — sélection de table |
| N5 | Cliquez sur Créer la réservation : elle apparaît aussitôt dans votre liste, en attente de confirmation. | 5,20 s | G/H — clic + résultat |
| N6 | Confirmez-la, installez le client, ou gérez un no-show, directement depuis le menu d'actions. | 5,43 s | I — menu d'actions |
| N7 | Vous pouvez aussi le faire depuis Claude : copiez ce prompt, remplacez les crochets. | 4,26 s | étages 1+2 (reveal + copié) |
| N8 | Collez-le dans la conversation : votre réservation est créée en quelques secondes. | 4,13 s | étage 3 (chatbot) |
| N9 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | 5,02 s | carte de fin (CTA, réutilisé) |

N9 réutilisé tel quel (octet-identique, copié depuis `foodeatup-fiche-plat-tuto/vo/N8.mp3`)
— texte générique, zéro crédit ElevenLabs dépensé. N0-N8 générés fraîchement, voix Adam
Instructor FR.

## Découpage

| Seg | Source | Sortie | Contenu |
|---|---|---:|---|
| intro | carte | 4,20 s | AJOUTER UNE RÉSERVATION |
| A1 | 0,30 → 4,00 | 2,00 s | Plan de salle, tables et file d'attente |
| A2 | 4,60 → 8,00 | 1,80 s | **slideleft** — liste Réservations, compteurs |
| B | 8,00 → 8,35 | 0,90 s | **zoom-punch** sur « + Nouvelle réservation » (1638, 310) |
| C | 9,00 → 24,00 | 3,60 s | **slideleft** — modale : nom, téléphone, email |
| D | 32,00 → 40,50 | 3,20 s | date 12/08/2026, heure 06:07 PM |
| E | 44,00 → 48,50 | 2,00 s | couverts 4, filtre « Salle principale », tables dispo |
| F | 51,50 → 52,00 | 0,90 s | **zoom-punch** sur la table T4 (965, 465) |
| G | 52,00 → 52,35 | 0,90 s | **zoom-punch** sur « Créer la réservation » (1026, 745) |
| H | 56,00 → 60,50 | 3,20 s | retour liste : Jean Dupont, statut « En attente » |
| I | 62,00 → 65,86 | 3,40 s | **zoom-punch** sur le menu d'actions (1633, 480), options affichées |
| claude1 | carte générée | 2,60 s | reveal — prompt en gros, fond crème |
| claude2 | carte générée | 2,20 s | confirmation « Copié dans le presse-papiers ! » |
| claude3 | carte générée | 6,00 s | mockup chatbot Claude |
| outro | carte | 5,60 s (auto-étendue si besoin) | CTA |

Coupes volontaires : **8,35 → 9,00 s** (ouverture de la modale, rien à montrer),
**24,00 → 32,00 s** (fin de saisie email, temps mort), **40,50 → 44,00 s** (défilement vers
Couverts, temps mort), **48,50 → 51,50 s** (défilement du panneau tables, redondant) et
**52,35 → 56,00 s** (état "Enregistrement…", chargement). Coordonnées mesurées visuellement
sur les frames réelles (`ffmpeg -ss t -frames:v 1`), cross-vérifiées sur plusieurs frames
voisines (tolérance ±15 px), même méthode que le reste de la série.

## Séquence Claude

> Crée une réservation pour [nom du client], [nombre de couverts] couverts, le [date] à
> [heure], pour mon établissement FoodEatUp (ID [ID établissement]).

Correspond 1:1 aux champs de la modale « Nouvelle réservation » (nom, couverts, date,
heure) ; la table reste optionnelle côté MCP comme côté produit (assignation automatique si
omise).

## Animations

Mêmes principes que toute la série : Ken Burns sur les cartes, xfade (0,28 s), bandeaux
d'étape (accents, pas d'apostrophe), encadré orange pulsant sur les 3 clics (Nouvelle
réservation, table T4, Créer la réservation) + 1 sur le menu d'actions. Pas de clip avatar
dans ce dossier (voix ElevenLabs de bout en bout).

## Cas d'usage / astuce du chef (pour la fiche Lovable)

- **Comment ça marche** : Réservations → + Nouvelle réservation → nom, téléphone, email du
  client → date, heure, nombre de couverts → laisser l'assignation automatique ou choisir une
  table précise → Créer la réservation. La réservation apparaît en statut « En attente ».
- **À quoi ça sert** : centraliser toutes les réservations (site, téléphone, sur place) dans
  un même plan de salle, avec assignation de table automatique ou manuelle selon vos zones
  (Salle principale, Terrasse...).
- **Astuce du chef** : dès qu'un client arrive, confirmez sa réservation ou installez-le
  directement (Check-in) depuis le menu d'actions de la ligne — sans ressaisir ses
  informations. Un no-show se déclare en un clic pour garder l'historique propre et libérer
  la table.

## Statut publication

Vidéo montée et publiée directement sur instruction explicite reçue de publier la vidéo une
fois le montage terminé, en gardant la structure comment-ça-marche / astuce du chef / cas
d'usage (même dérogation documentée que sur `foodeatup-kds-poste-tuto` et
`foodeatup-fiche-plat-tuto`) — livrée à l'utilisateur via `SendUserFile` en parallèle de la
publication.
