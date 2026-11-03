# Tutoriel — Changer les statuts d'une facture (module Comptabilité & Achats)

Première vidéo du module `comptabilite` (catalogue #6, Comptabilité & Achats).
Durée livrée : **59,48 s** — H.264 High/yuv420p, AAC LC 48 kHz stéréo,
faststart (moov avant mdat confirmé). Audio : max **-7,1 dBFS** / mean
-22,0 dBFS. Decode 0 erreur.

## Ce que montre le rush

Le rush (39,28 s, capture 1920x828 @25fps, pas de chrome navigateur à
rogner) montre le module Comptabilité > Facture : liste des factures
(onglets Facture/Devis/Dépenses, sous-onglets Factures/E-Reporting/Archives
légales, statistiques Total payées/En attente de paiement/Total devis reçu)
→ tableau des factures avec statuts (Brouillon, En attente, Payée) → clic
sur le menu Action (3 points) d'une facture "En attente" → "Visualiser" →
détail de la facture (Informations, Résumé, Historique des statuts,
Informations client, Articles, Actions rapides) → menu "Téléchargements et
options" (Télécharger PDF/Factur-X/UBL, Renvoyer au client, Marquer comme
payée) → clic "Marquer comme payée" → confirmation ("Le statut de cette
facture passera à « Payée »") → succès, statut mis à jour → retour à la
liste, statistiques actualisées (Total payées 1010→1011, En attente
334→333).

## Voix off (9 lignes, voix Adam FR `TGAegA0zNRi8I6nUdq3i`)

| # | Texte | Durée | Segment |
|---|---|---:|---|
| N0 | Comment changer le statut d'une facture dans FoodEatUp ? Voici comment faire, en toute conformité. | 5,43 s | intro |
| N1 | Retrouvez toutes vos factures au même endroit, avec leur statut : brouillon, en attente, ou payée. | 5,69 s | A — liste des factures |
| N2 | Ouvrez une facture pour voir son détail : informations, résumé, et historique des statuts. | 5,04 s | C — détail de la facture |
| N3 | Le menu Téléchargements et options propose aussi de renvoyer la facture, ou de changer son statut. | 5,67 s | E — menu Téléchargements et options |
| N4 | Un clic sur Marquer comme payée, une confirmation, et le statut passe aussitôt à Payée. | 4,68 s | H — statut mis à jour |
| N5 | Les statistiques et la liste des factures se mettent à jour automatiquement. | 4,36 s | I — retour à la liste, stats actualisées |
| N6 | Vous pouvez aussi le faire depuis Claude : copiez ce prompt, remplacez les crochets. | 6,87 s | claude1 — reveal + copied (réutilisé tel quel depuis `foodeatup-conge-employe-tuto`) |
| N7 | Collez-le dans la conversation : le statut de la facture est mis à jour en quelques secondes. | 4,68 s | claude3 — résultat chatbot |
| N8 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | 5,02 s | carte de fin (CTA, réutilisé tel quel depuis `foodeatup-borne-tuto`) |

N6 et N8 réutilisés tels quels (texte générique identique aux tutos
précédents) — zéro crédit ElevenLabs dépensé sur ces deux lignes.

## Découpage

Segments dimensionnés dès le départ à partir des durées VO réellement
mesurées — **dérive nulle dès le premier montage**.

| Seg | Source | Sortie | Contenu |
|---|---|---:|---|
| intro | carte | 6,50 s | CHANGER LES STATUTS D'UNE FACTURE |
| A | 0,20 → 7,00 | 7,00 s | liste des factures, statuts, statistiques |
| B | 7,00 → 7,30 | 0,90 s | **zoom-punch** sur le menu Action (3 points) |
| C | 10,00 → 13,00 | 6,50 s | détail de la facture |
| D | 15,00 → 15,30 | 0,90 s | **zoom-punch** sur "Téléchargements et options" |
| E | 16,00 → 18,50 | 7,00 s | menu options (PDF, Factur-X, UBL, renvoyer, marquer payée) |
| F | 19,00 → 19,30 | 0,90 s | **zoom-punch** sur "Marquer comme payée" |
| G | 20,00 → 21,30 | 0,90 s | **zoom-punch** sur "Confirmer" (modale) |
| H | 21,30 → 25,00 | 6,00 s | succès, statut "Payée" |
| I | 30,00 → 34,00 | 5,00 s | retour à la liste, statistiques actualisées |
| claude1-3 | PNG générés | 6+3+6 s | séquence "Utiliser avec Claude" (reveal / copied / chatbot) |
| outro | carte | 6,20 s | CTA |

Transitions : `fade` sur les enchaînements continus (intro→A, A→B, C→D, E→F,
F→G, claude3→outro), `slideleft` sur les coupures de contexte (B→C, D→E,
G→H, H→I, I→claude1→claude2→claude3).

## Séquence "Utiliser avec Claude"

`mcp__FoodEatUp__update_invoice_status` change le statut d'une facture en
respectant les transitions légales autorisées (DGFiP) : `brouillon`,
`en_attente`, `envoyee`, `acceptee`, `refusee`, `litige`, `payee`,
`annulee`. Le prompt de la vidéo généralise volontairement au-delà du seul
"marquer comme payée" montré à l'écran, pour refléter la richesse réelle de
l'outil :

```
Change le statut de la facture [numéro de facture] vers [nouveau statut :
payée, envoyée, litige…], pour mon établissement FoodEatUp (ID [ID
établissement]).
```

## Animations

Mêmes principes que toute la série : Ken Burns sur les cartes, xfade
(0,28 s), bandeaux d'étape, encadré orange pulsant sur les 4 clics (menu
Action, Téléchargements et options, Marquer comme payée, Confirmer).
Séquence "Utiliser avec Claude" en 3 étages (reveal/copied/chatbot) via
`claude_prompt_sequence.py`, réutilisée telle quelle. Pas de mini-animation
dédiée supplémentaire.

## Astuce du chef — les statuts et leurs usages

L'astuce du chef publiée sur Lovable explique les 8 statuts disponibles et
leur usage légal (DGFiP) : `brouillon` (facture en préparation, non
définitive), `en_attente` (envoyée, en attente de paiement),
`envoyee`/`acceptee`/`refusee` (suivi côté client), `litige` (paiement
contesté, à traiter avant relance), `payee` (soldée), `annulee`
(facture annulée, doit rester tracée — jamais supprimée pour la conformité).

## Statut publication

Montage terminé et checklist de compatibilité passée (H.264 High/yuv420p,
AAC 48 kHz stéréo, faststart, peak -7,1 dBFS, 0 erreur de décodage). Vidéo
et vignette hébergées via URL GitHub raw sur la branche
`claude/foodeatup-tutorial-video-vn7udf`. Lovable : tutoriel
`changer-les-statuts-dune-facture` à ajouter dans `src/data/tutorials.ts`
(module `comptabilite`, subcategory "6 - changer les statuts d'une
facture"), avec `chefTip` et `claudePrompt`. Première vidéo du module
Comptabilité & Achats.
