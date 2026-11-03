# Tutoriel — Consulter ses productions en cours (HACCP)

Rush fourni par Michael : `Retrouver_toutes_vos_production.mp4`, 26,6 s, 1920x828, 25 fps.
Module **HACCP** (30 vidéos attendues, aucune encore publiée à ce jour — voir
`FAISABILITE-SERIE-TUTORIELS.md` et le tableau "Tutoriels publiés" de
`LOVABLE-FOODEATUP-DOCS.md`, qui ne compte pour l'instant que les 10 vidéos du module
Configuration).

## Déroulé du rush (analyse frame par frame)

| t | Écran |
|---:|---|
| 0,0–6,0 s | Page « Production haccp » : barre de recherche, bouton « + Créer un plat », carte du plat « Uuuu » (10,00 €, date de production 23/07/2026 12:00, allergènes : aucun), boutons **Éditer** / **Ingrédients** |
| ~6,0 s | Clic **Éditer** (bouton ~x=241,y=587 espace source 1920x828) |
| 6,0–16,0 s | Modale « Modifier le plat et la production » : liste ingrédients (tomates, 1 kg), date/heure de production, durée de vie (2 jours) ; scroll vers nom du plat, catégorie (Desserts), prix de vente (10 €), TVA (Consommation immédiate — 10 %) |
| ~16,0 s | Fermeture modale, clic **Ingrédients** (bouton ~x=506,y=587) |
| 16,5–26,6 s | Modale de suivi ingrédients : alerte « 1 ingrédient(s) manquant(s) en stock », bouton **Tout ajouter aux courses**, tableau (ingrédient, quantité, stock, statut, DLC, n° de lot), bouton **Courses** par ligne, bouton **Créer étiquette HACCP** |

## Correspondance outils MCP FoodEatUp

- **`list_production_plans(establishment_id, start_date?, end_date?, status?)`** — l'action
  titre de la vidéo (« Consulter ses productions en cours »).
- `get_production_ingredients(establishment_id, production_id)` — correspond à la modale
  « Ingrédients » (stock/DLC/manquants), montrée dans le rush mais secondaire au propos
  principal (comme les tutoriels avec `claudePrompts[]` à 2 entrées).

## Script voix off proposé (9 lignes, voix Adam FR `TGAegA0zNRi8I6nUdq3i`)

**⚠️ STOP validation — ne pas générer l'audio avant accord de Michael (règle du
`FOODEATUP-TUTORIELS-WORKFLOW.md`).**

| # | Texte | Segment prévu |
|---|---|---|
| N0 | Envie de savoir où en sont vos productions ? FoodEatUp vous montre tout, en un coup d'œil. | intro |
| N1 | Retrouvez la liste de vos plats en préparation, avec leur date de production et leurs allergènes. | A — liste |
| N2 | Cliquez sur Éditer pour ajuster les ingrédients, la date, l'heure ou la durée de vie. | clic Éditer + modale |
| N3 | Cliquez sur Ingrédients pour vérifier votre stock, la DLC et le numéro de lot de chaque produit. | clic Ingrédients + modale |
| N4 | Un ingrédient manque ? Ajoutez-le directement à vos courses, ou créez l'étiquette HACCP en un clic. | alerte + boutons |
| N5 | Résultat : vous suivez chaque production et sa traçabilité HACCP en temps réel, sans rien oublier. | bénéfice |
| N6 | Vous pouvez aussi le faire depuis Claude : copiez ce prompt, remplacez les crochets. | étages Claude 1+2 (réutilisable tel quel) |
| N7 | Collez-le dans la conversation : vos productions en cours s'affichent aussitôt. | étage Claude 3 |
| N8 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | carte de fin (CTA, réutilisable tel quel) |

N6 et N8 peuvent être réutilisés tels quels (mp3 déjà généré, ex. `foodeatup-produits-tuto/vo/N6.mp3` et `N8.mp3`) — zéro crédit ElevenLabs supplémentaire pour ces deux lignes.

## Prompt Claude proposé (`claudePrompt`)

```
Affiche mes productions en cours pour mon établissement FoodEatUp (ID [ID établissement]), du [date début] au [date fin].
```

Optionnel, en second exemple (`claudePrompts[]`, comme sur `saisir-ses-ingredients` / `creer-ses-produits`) :

```
Donne-moi le détail des ingrédients (stock, DLC, manquants) pour la production [ID production] de mon établissement FoodEatUp (ID [ID établissement]).
```

## Fiche Lovable proposée

- slug : `consulter-ses-productions-en-cours`
- moduleSlug : `haccp`
- subcategory : « 14 - Retrouver toutes vos production » (nom exact du sous-dossier
  Drive, module 4 HACCP — confirmé le 2026-08-04, voir ré-audit ci-dessous ; le titre
  affiché à l'écran/sur le site reste « Consulter ses productions en cours »,
  celui de la carte d'intro fournie)
- howItWorks : à partir des lignes N1-N4 ci-dessus (à l'impératif)
- whatItsFor : suivi HACCP en temps réel de toutes les productions du restaurant, sans
  ressaisie, avec alerte stock et traçabilité (DLC, lot)

## Ré-audit Drive (2026-08-04) — le mystère des 157 vidéos partiellement résolu

L'audit du 2026-08-02 (`FAISABILITE-SERIE-TUTORIELS.md`) ne portait que sur 5 modules
(94 annoncés / 92 dossiers). Revérification le 2026-08-04 : **5 nouveaux modules ont été
ajoutés dans le Drive le 2026-08-03** (Mon Site, Marketing, Service, KDS, Réservation),
et les 2 dossiers manquants du module 1 (Configuration) ont été comblés entretemps.

| Module | Dossiers (2026-08-04) |
|---|---:|
| 1 — Configuration | 14 (complet, les 2 trous du 2026-08-02 sont comblés) |
| 2 — Équipe & Planning | 20 |
| 3 — Comptabilité | 10 |
| 4 — HACCP | 30 |
| 5 — StockVision AI | 20 |
| 6 — Mon Site | 8 |
| 7 — Marketing | 24 |
| 8 — Service | 3 |
| 9 — KDS | 3 |
| 10 — Réservation | 5 |
| **Total** | **137** |

**137, pas encore 157** (écart de 20) — mais très au-dessus des 92 du dernier audit. Le
suivi GitHub (`videos/SUIVI-VIDEOS.md`) est mis à jour avec ce chiffre vérifié aujourd'hui,
l'écart à 157 est documenté comme point ouvert (nouveaux dossiers encore à venir, et/ou
déclinaisons 9x16 non comptées dans cette arborescence — hypothèse déjà posée le
2026-08-02, toujours pas tranchée).

## Statut

**Validé par Michael le 2026-08-04.** Audio ElevenLabs généré (voix Adam FR), montage v1
livré et validé. Publication en cours : Lovable (module `haccp`) + suivi GitHub.
RapidoCMS non disponible dans cette session (connecteur non installé pour cet
espace de travail) — vidéo et vignette servies depuis GitHub raw
(`claude/foodeatup-video-tutorials-u4ljhv`) en attendant que RapidoCMS soit reconnecté ;
LinkedIn non programmé pour cette raison.
