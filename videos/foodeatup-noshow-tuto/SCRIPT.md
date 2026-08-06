# Tutoriel — Gérer ses No-shows & modifications

Module `reservation-salle` (catégorie « Agent IA Caroline & Salle »), item **#3/5** du
catalogue.

Durée livrée : **44,12 s** — H.264 High/yuv420p, AAC 48 kHz stéréo, faststart.
Audio : true peak **-7,14 dBFS**. Sans avatar HeyGen. **Avec séquence « cas d'usage +
prompt Claude »** : `mcp__Foodeatup__no_show_reservation(establishment_id,
reservation_id)` existe. Ni la modification de détails de réservation ni la suppression
définitive n'ont d'équivalent MCP (`cancel_reservation` = « Annuler », statut différent
de « Supprimer » qui efface la ligne) — un seul prompt, centré sur le no-show.

## Rush

`assets/screen.mp4` (1920×828, 36,32 s, audio quasi silencieux -91 dB → pas de voix
native) : page **Réservations** de FoodEatUp. Déroulé :
1. Vue d'ensemble de la liste (statuts : En attente, Installée, No-show, Confirmée,
   Terminée, Annulée).
2. Menu « ... » sur la ligne « Jean dupont » (t≈6s) → clic **Modifier** (t≈8,2s) →
   modale d'édition (nom, téléphone, email, date, heure, couverts) puis sélection de
   table (Toutes / Salle principale / Terrasse, T3/T4/T6/T7/T1).
3. Menu « ... » réouvert (t≈24-28s) → clic **No-show** → le statut de la ligne passe à
   « No-show » (t≈29s).
4. Menu réouvert, réduit à Modifier/Supprimer (le statut No-show retire les actions non
   pertinentes) → survol **Supprimer** → boîte de dialogue de confirmation « Supprimer
   la réservation de jean dupont ? » (OK/Annuler) — capturée dans le montage, bonus non
   anticipé au script initial.

## Voix off (8 lignes, voix Adam FR `TGAegA0zNRi8I6nUdq3i`)

Script validé par l'utilisateur avant génération.

| # | Texte | Durée | Ancrage |
|---|---|---:|---|
| N0 | Modifier, marquer no-show ou supprimer une réservation ? Tout se passe au même endroit. | 5,20 s | carte d'intro |
| N1 | Depuis Réservations, ouvrez le menu à trois points sur la ligne concernée. | 4,13 s | clic sur « ... » (seg B/C/D) |
| N2 | Cliquez sur Modifier pour changer l'horaire, le nombre de couverts ou la table. | 4,21 s | modale d'édition (seg E/F) |
| N3 | Le client ne s'est pas présenté ? Cliquez sur No-show pour libérer la table. | 4,21 s | menu réouvert + clic No-show (seg G/H) |
| N4 | Une réservation à supprimer définitivement ? Le même menu propose aussi cette option. | 4,68 s | statut mis à jour + menu réduit + survol Supprimer (seg I/J/K) |
| N5 | Vous pouvez aussi marquer un no-show depuis Claude : copiez ce prompt, remplacez les crochets. | 4,78 s | séquence Claude — reveal + copié |
| N6 | Collez-le dans la conversation : la table est libérée en quelques secondes. | 4,02 s | séquence Claude — mockup chatbot |
| N7 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | 4,96 s | carte de fin (CTA, réutilisée telle quelle) |

## Découpage

| Seg | Source | Sortie | Contenu |
|---|---|---:|---|
| intro | carte | 5,70 s | GÉRER & NO-SHOWS (image fournie) |
| A | 0,00 → 1,50 | 1,80 s | Vue d'ensemble « Réservations » |
| B | 5,80 → 6,30 | 1,00 s | **zoom-punch** sur « ... » (1617, 165) |
| C | 6,30 → 7,90 | 2,30 s | Menu ouvert (6 actions) |
| D | 8,00 → 8,50 | 1,40 s | **zoom-punch** sur « Modifier » (1440, 307) |
| E | 8,50 → 11,00 | 2,90 s | Modale d'édition — champs client/créneau |
| F | 13,00 → 15,50 | 2,80 s | Modale — sélection de table |
| G | 24,00 → 27,50 | 3,30 s | Menu réouvert (6 actions) |
| H | 27,50 → 28,70 | 2,10 s | **zoom-punch** sur « No-show » (1440, 347) |
| I | 29,00 → 29,80 | 1,00 s | Statut mis à jour (badge No-show) |
| J | 30,00 → 31,00 | 1,50 s | Menu réduit (Modifier/Supprimer) |
| K | 33,00 → 34,50 | 3,90 s | **zoom-punch** sur « Supprimer » (1440, 252) + confirmation |
| claude1 | carte générée | 2,90 s | reveal — prompt en gros, fond crème |
| claude2 | carte générée | 3,30 s | confirmation « Copié dans le presse-papiers ! » |
| claude3 | carte générée | 4,90 s | mockup chatbot Claude |
| outro | carte | 6,49 s | CTA |

Coordonnées mesurées par extraction de frames plein-format (1920×828) et crops PIL
autour de chaque clic. `drift vs anchors` final : uniquement N2 à 0,34 s (négligeable),
tous les autres à 0.

Prompt Claude (identique côté vidéo et côté fiche Lovable `claudePrompt`) :

> Marque comme no-show la réservation de [nom du client] (ID [ID réservation]) pour mon
> établissement FoodEatUp (ID [ID établissement]).

## Pièges rencontrés

- **Dérive voix/image importante au premier montage** (jusqu'à 3,65 s sur les stages
  Claude) : les cibles initiales des segments informatifs (E/F, G/H, I/J/K, stages
  Claude) étaient calées trop près de la durée mesurée des lignes VO correspondantes,
  sans marge pour le `GAP` séquentiel — dès qu'une ligne dépassait légèrement son
  segment, le décalage se répercutait en cascade sur toutes les lignes suivantes.
  Corrigé en augmentant les cibles de chaque groupe de segments avec une marge
  (~0,7-0,9 s) au-dessus de la durée VO mesurée, plutôt que de viser l'égalité stricte.
- Le rush contient une boîte de dialogue de confirmation de suppression non identifiée
  lors du premier repérage à 1 fps (visible seulement en extrayant des frames à 2 fps
  autour de t=33-35s) — capturée par chance dans la fenêtre du segment K, résultat
  bonus cohérent avec le sujet de la vidéo.

## Statut publication

**Validée par l'utilisateur le 2026-08-06**, montage terminé. Livrée pour information
puis publication autorisée par l'utilisateur (« tu peux publier »).
