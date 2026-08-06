# Tutoriel — Placer un client à table (Check-in réservation)

Module `reservation-salle` (Réservations & Plan de salle), site Lovable
FoodEatUp Academy. **Fiche déjà présente sur le site sous le slug
`placer-un-client-a-table` (placeholder "en cours de tournage", order 4,
section "Placement en salle") — ce tutoriel la complète, ne crée pas de
nouvelle entrée.**

Rush fourni : `Ajouter_un_client_a_une_table.mp4` (22,96 s, 1920x828, 25 fps).

## Déroulé du rush (analyse frame par frame)

| t (rush) | Écran |
|---:|---|
| 0-6,6 s | Liste des réservations, la ligne "Jean dupont" (En attente, table T3) |
| 6,6-8 s | Ouverture du menu d'actions (⋮) : Confirmer / **Check-in** / Modifier / No-show / Annuler / Supprimer |
| 8 s | Clic **Check-in** |
| 9,3-10,5 s | Toast « Client installé. Commande sur place CMD-2026-00105 créée. » |
| 10,5 s | Clic **OK** |
| 12,5-15,6 s | Ligne mise à jour : statut **Installée** ; réouverture du menu d'actions (Modifier / Supprimer seulement) |
| 16 s | Clic **Modifier** |
| 16,5-23 s | Modal « Modifier la réservation » : Client, Créneau, Table — optionnel (Toutes / Salle principale / Terrasse). Le rush s'arrête avant la sélection d'une table précise (curseur revient vers la croix de fermeture). |

## Voix off (v1, 8 lignes — voix Adam FR `TGAegA0zNRi8I6nUdq3i`)

| # | Texte | Ancrage |
|---|---|---|
| N0 | Installer un client à sa table sur FoodEatUp ? Quelques clics suffisent. | carte d'intro |
| N1 | Repérez la réservation de votre client dans la liste, puis cliquez sur Check-in pour l'installer directement à sa table. | seg A + clic Check-in |
| N2 | Sa commande sur place est créée automatiquement, en un instant. | toast + clic OK |
| N3 | Le statut passe aussitôt à Installée. Besoin de changer sa table ? | ligne mise à jour + réouverture du menu |
| N4 | Ouvrez Modifier : choisissez la zone et la table, ou laissez FoodEatUp l'assigner automatiquement. | clic Modifier + modal |
| N5 | Vous pouvez aussi le faire depuis Claude : copiez ce prompt, remplacez les crochets. | étage 1+2 — **réutilisée depuis `foodeatup-tva-tuto/vo/N6.mp3`** |
| N6 | Collez-le dans la conversation : votre client est installé en quelques secondes. | étage 3 (mockup chatbot) |
| N7 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | carte de fin — **réutilisée depuis `foodeatup-tva-tuto/vo/N8.mp3`** |

Pas de carte de transition supplémentaire cette fois (sujet unique, pas de
canal alternatif à introduire comme sur `commander-via-site-vocal-qrcode`).

## Découpage prévu

| Seg | Source (rush) | Cible | Contenu |
|---|---|---:|---|
| intro | carte fournie | 4,40 s | PLACER UN CLIENT À TABLE |
| A | 0,30 → 6,60 | 3,40 s | Liste des réservations |
| B | 7,85 → 8,15 | 0,90 s | **zoom-punch** Check-in (1505, 408) |
| C | 9,30 → 10,55 | 1,60 s | Toast "Client installé" |
| D | 10,55 → 10,85 | 0,90 s | **zoom-punch** OK (1232, 102) |
| E | 12,50 → 15,60 | 3,00 s | Statut Installée + réouverture menu |
| F | 15,90 → 16,20 | 0,90 s | **zoom-punch** Modifier (1505, 213) |
| G | 16,50 → 22,90 | 3,60 s | Modal "Modifier la réservation" |
| claude1 | carte générée | 3,00 s | reveal — prompt |
| claude2 | carte générée | 2,30 s | « Copié dans le presse-papiers ! » |
| claude3 | carte générée | 4,60 s | mockup chatbot Claude |
| outro | carte fournie | 6,20 s (extensible) | CTA |

Coordonnées mesurées par grille de pixels sur les frames du rush
(`work/grid_*.png`).

## Séquence Claude — `mcp__Foodeatup__checkin_reservation`

Correspondance exacte et directe : *"Check-in : installe le client (table «
occupée ») et crée la commande sur place."* — paramètres `establishment_id`,
`reservation_id`, `table_id` (optionnel, "si non encore assignée").

**Prompt affiché dans la vidéo et sur la fiche Lovable** :

> Installe le client de la réservation [ID réservation] à la table [ID
> table] pour mon établissement FoodEatUp (ID [ID établissement]).

## Contenu prévu pour la fiche Lovable (remplace le placeholder)

- **howItWorks** : repérer la réservation dans la liste · ouvrir le menu
  d'actions (⋮) et cliquer Check-in · la commande sur place est créée
  automatiquement, statut → Installée · ouvrir Modifier pour changer la
  table (zone + table précise, ou assignation automatique).
- **whatItsFor** : installer un client réservé à sa table en un clic, avec
  sa commande créée automatiquement — sans ressaisie côté service.
- **claudePrompt** : voir ci-dessus (`checkin_reservation`).
- **chefTip** : sur l'intérêt de check-in même sans table pré-assignée
  (FoodEatUp assigne automatiquement) et sur la réassignation via Modifier
  en cas de changement de dernière minute.

## Statut

**v1 livrée.** Script validé par Michael (2026-08-06).

Durée livrée : **38,44 s** — H.264 High/yuv420p 1920x828 25fps, AAC 48 kHz
stéréo, faststart. Audio : true peak **-7,3 dBFS** (mesuré sur le MP4 final).

Offsets VO mesurés (`offsets:` de `build.py`, zéro dérive) :

| # | Offset | Durée |
|---|---:|---:|
| N0 | 0,30 s | 4,00 s |
| N1 | 4,52 s | 6,16 s |
| N2 | 10,90 s | 3,37 s |
| N3 | 14,49 s | 3,47 s |
| N4 | 18,19 s | 5,46 s |
| N5 | 23,87 s | 4,41 s |
| N6 | 28,50 s | 3,89 s |
| N7 | 32,61 s | 5,02 s |

Outro auto-étendue de 6,20 s → 7,99 s pour absorber la fin de N7.

Livrables : `out/foodeatup-placer-un-client-a-table-tuto-v1.mp4` +
`out/thumbnail-youtube.jpg` (recadrage neutre de `assets/intro.jpg`).
