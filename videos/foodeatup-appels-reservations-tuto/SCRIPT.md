# Tutoriel — Réécouter ses appels et réservations (FoodEatUp)

Deuxième vidéo du module `caroline-ia` (Agent IA Caroline & Salle), catalogue
157 tutoriels : "02 Réécouter ses Appels et réservations" (voir
`videos/CATALOGUE-157-TUTORIELS.md` ligne 88). Premier tutoriel du module à
être produit (le module était à 0/6 au 2026-08-04, voir
`videos/PROGRESSION-157-TUTORIELS.md`). Intro card + rush + outro card fournis
par Michael (upload direct dans la conversation, pas de Drive).

## Ce que montre le rush

Rush 43,0 s, 1920x828, muet (mean_volume -91 dB — pas de son à nettoyer).
Onglet "Appels" (agent vocal Caroline) :

1. **0,3-6,6 s** — Liste des appels : 4 compteurs (Total appels 47,
   Aujourd'hui 0, Commandes générées 2, Durée moyenne 0:53), tableau
   Date/Numéro/Durée/Statut/Intentions/Commande, tous les statuts visibles en
   vert "Réussi".
2. **~6,7 s** — Clic sur "Voir" (première ligne, appel du 05/08 18:58, 1:10).
3. **7,0-17,3 s** — Modale de détail : badge "Réussi", **Résumé** (texte en
   anglais côté produit : commande de couscous/plats tunisiens pour Ali,
   2 couverts, le lendemain soir), **Transcription** complète tour par tour
   Caroline/Client, zone scrollable — l'utilisateur fait défiler le texte
   dans les deux sens pour le lire en entier.
4. **~17,4 s** — Clic sur le "×" de fermeture.
5. **19,0-22,3 s** — Retour à la liste complète.
6. **~22,4 s** — Clic sur le filtre "Statut" (menu déroulant, natif).
7. **24,0-33,0 s** — Cycle à travers plusieurs valeurs du filtre (Manqué,
   Transféré, En cours) : la liste passe à "Aucun appel pour le moment" à
   chaque fois (tous les appels de la démo sont "Réussi"), avec l'aperçu du
   bloc "Comment ça marche" qui pointe en bas de page.
8. **34,0-42,5 s** — Retour au filtre "Tous les statuts" : la liste complète
   réapparaît, état final stable.

Aucun clic n'a d'équivalent direct dans les outils `mcp__FoodEatUp__*`
exposés à cette session (ni `list_calls`, ni `get_call` — seuls des outils de
réservation existent : `list_reservations`, `create_reservation`, etc., qui
ne correspondent pas à l'action filmée ici, consulter l'historique des
appels vocaux). **Aucun `claudePrompt` fabriqué** — conforme à la règle du
paragraphe 3 de `videos/FOODEATUP-TUTORIELS-WORKFLOW.md` ("si non : ne pas
fabriquer de prompt"). La section correspondante reste donc masquée côté
Lovable pour cette fiche.

## Voix off (7 lignes, voix Adam FR `TGAegA0zNRi8I6nUdq3i`)

| # | Texte | Durée | Segment |
|---|---|---:|---|
| N0 | Caroline répond à vos appels. Retrouvez chaque échange directement dans FoodEatUp. | 4,55 s | intro |
| N1 | Nombre d'appels, commandes générées, durée moyenne : tout est résumé en un coup d'œil. | 5,04 s | A — liste + compteurs |
| N2 | Cliquez sur Voir pour rouvrir n'importe quel appel. | 2,87 s | B — punch "Voir" |
| N3 | Vous retrouvez le résumé et la transcription complète, mot pour mot. | 4,00 s | C/D — modale + fermeture |
| N4 | Filtrez les appels par statut : réussi, manqué, transféré ou en cours. | 4,86 s | F/G — punch filtre + cycle |
| N5 | De quoi garder un œil sur chaque échange avec vos clients, sans rien manquer. | 4,26 s | H — retour liste complète |
| N6 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | 5,02 s | carte de fin (CTA, réutilisé tel quel depuis `foodeatup-devis-statuts-tuto/vo/N9.mp3` — texte identique, zéro crédit ElevenLabs dépensé) |

## Boutons mesurés (frames extraites du rush, 1920x828 natif)

- `BTN_VOIR` (1639, 303), taille (58, 35) — pilule "Voir", 1re ligne.
- `BTN_CLOSE` (1278, 95), taille (30, 30) — "×" de la modale.
- `BTN_FILTER` (1238, 147), taille (197, 49) — sélecteur "Statut".

Bandeaux d'étape rendus avec la méthode corrigée (deux `drawtext` en `box=1`,
pas `drawbox` — voir `videos/foodeatup-mouvement-stock-tuto/build.py` et le
paragraphe correspondant de `FOODEATUP-TUTORIELS-WORKFLOW.md`), aucune
apostrophe dans les textes de bandeau.

## Découpage

| Seg | Source | Sortie | Contenu |
|---|---|---:|---|
| intro | carte | 5,00 s | RÉÉCOUTER SES APPELS ET RÉSERVATIONS |
| A | 2,00 → 6,60 | 4,20 s | "1 - Suivez tous vos appels" (liste + compteurs) |
| B | 6,60 → 6,95 | 0,75 s | **zoom-punch** sur "Voir" (1639, 303) |
| C | 7,00 → 17,20 | 6,00 s | "2 - Résumé et transcription" (modale, scroll) |
| D | 17,20 → 17,55 | 0,75 s | **zoom-punch** sur le "×" de fermeture (1278, 95) |
| E | 19,00 → 22,30 | 1,80 s | retour liste (transition, sans bandeau) |
| F | 22,30 → 22,65 | 0,75 s | **zoom-punch** sur le filtre Statut (1238, 147) |
| G | 24,00 → 33,00 | 3,50 s | "3 - Filtrez par statut" (cycle Manqué/Transféré/En cours) |
| H | 34,00 → 42,50 | 3,00 s | "Historique complet, toujours accessible" (liste finale) |
| outro | carte | 6,20 s (auto-étendue si besoin) | CTA |

## Statut publication

Validée par Michael puis publiée le 2026-08-06 :
- RapidoCMS : `foodeatup-appels-reservations-tuto-v1` (vidéo) +
  `foodeatup-appels-reservations-tuto-thumbnail` (vignette), URLs S3 stables.
- Lovable (`src/data/tutorials.ts`, module `caroline-ia`, commit `3cc5d912`) —
  a remplacé un placeholder préexistant du même sujet créé par une autre
  session. Module `caroline-ia` passé de 0/6 à 2/6 (une autre fiche,
  `01 Configurer Caroline`, avait entre-temps été publiée par une session
  concurrente). Pas de `claudePrompt`, conforme à l'analyse ci-dessus.
- `videos/LOVABLE-FOODEATUP-DOCS.md` et `videos/PROGRESSION-157-TUTORIELS.md`
  mis à jour en conséquence.
- LinkedIn FoodEatUp (`68807312`) : brouillon programmé le 2026-09-21 à 07:00
  (post `575`) — prochain créneau libre, le calendrier était complet jusqu'au
  2026-09-20 (2 posts/jour, alimenté par plusieurs sessions en parallèle).
- Facebook FoodEatUp (`201499969703551`) : brouillon créé (`685`) mais
  **programmation refusée** — « date supérieure à la date d'expiration du
  compte » (même blocage que celui déjà documenté dans `RAPPORT-VIDEOS.md`
  au 2026-07-11). Le compte doit être renouvelé par Michael avant de pouvoir
  reprogrammer ce brouillon.
