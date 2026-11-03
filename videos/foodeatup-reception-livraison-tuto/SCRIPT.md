# Tutoriel — Ajouter, modifier ou valider une réception livraison (module HACCP)

Intrants fournis par Michael : `VALIDER_UNE_LIVRAISON_MODULE_HACCP.jpg` (carte intro),
carte outro générique (identique aux autres tutos),
`Ajouter_modifier_ou_valider_une_r_ception_livraison.mp4` (screen recording, 1920×828,
25 fps, **54,56 s**).

## Ce que montre le rush

1. **Réception du jour** (0–4s) — liste des réceptions (68 total, 63 en attente,
   1 manuel), bouton « Contrôle à réception ».
2. **Nouvelle réception — étape 1** (4–33s) — date/heure de contrôle, photo du bon de
   livraison, référence (« BL-2026-006 »), fournisseur (« Fournisseur des légumes »),
   catégorie(s) de produits, état de livraison (Conforme/Non conforme), commentaires,
   bouton « Étape suivante ».
3. **Étape 2** (33–38s) — température des produits frais (curseur +/-, 1,5 → 4°C).
4. **Ajouter des produits** (38–41,6s) — modale « Ajouter des produits » (recherche,
   filtres Frais/Surgelé/Sec/Autres), sélection d'un produit (Abricot, qté 1), bouton
   « Valider ».
5. **Récapitulatif et enregistrement** (41,6–44,3s) — liste des produits ajoutés
   (suppression possible), case « Ma réception est terminée », bouton « Enregistrer ».
6. **Confirmation** (44,3–47,5s) — retour sur la liste, toast « Succès ! Réception
   manuelle enregistrée avec succès. », nouvelle carte « Contrôle manuel / Conforme /
   Enregistré ».
7. **Modifier après validation** (47,5–54,56s) — ouverture de la fiche (statut
   « Livrée », fournisseur, référence, date, température), tableau « Produits livrés »,
   menu d'action « … » sur un produit : **Photo DLC / DLC manuelle / Température /
   Scanner produit** — c'est le point « modifier » du titre.

Le rush couvre bien les 3 verbes du titre : **ajouter** (nouvelle réception + produits),
**valider** (Enregistrer → statut Livrée), **modifier** (menu d'action post-validation).

## Outil MCP FoodEatUp correspondant

`mcp__FoodEatUp__create_haccp_reception(establishment_id, date_controle, heure_controle,
etat_livraison, fournisseur_id?, fournisseur_nom?, reference_bl?,
temperature_produits_frais?, non_conformites?, commentaires?, validate?)` — correspond
exactement à l'étape 1+2 du rush (contrôle réception manuel). Le paramètre `validate`
(bool, défaut false) permet même de valider immédiatement, ce qui correspond au bouton
Enregistrer + à l'étape de validation montrée dans le rush.

> Crée une réception HACCP du [date] à [heure] pour le fournisseur [nom fournisseur],
> référence [référence BL], état [conforme/non conforme], température [température]°C,
> pour mon établissement FoodEatUp (ID [ID établissement]).

## Voix off (12 lignes, Adam FR `TGAegA0zNRi8I6nUdq3i`)

| # | Texte | Segment | Note |
|---|---|---|---|
| N0 | Ajoutez, modifiez ou validez vos réceptions de livraison directement depuis FoodEatUp. | intro | — |
| N1 | Depuis Réception du jour, cliquez sur Contrôle à réception pour démarrer une nouvelle réception. | A+B (liste + clic) | — |
| N2 | Indiquez la date, l'heure et prenez en photo le bon de livraison. | C (date/heure/photo) | — |
| N3 | Ajoutez la référence du bon et sélectionnez le fournisseur. | D (référence/fournisseur) | — |
| N4 | Choisissez la catégorie de produits concernée et l'état de la livraison, conforme ou non conforme. | E (catégorie/état) | — |
| N5 | À l'étape suivante, renseignez la température des produits frais. | F+G (clic Étape suivante + température) | — |
| N6 | Ajoutez les produits reçus depuis votre catalogue, puis validez la sélection. | H+I (clic Ajouter produits + modale) | — |
| N7 | Vérifiez le récapitulatif et cliquez sur Enregistrer pour valider la réception. | K+L (récap + clic Enregistrer) | — |
| N8 | Votre réception est enregistrée : vous pouvez encore modifier chaque produit, sa DLC ou sa température si besoin. | M+N (succès + menu modifier) | — |
| N9 | Vous pouvez aussi le faire depuis Claude : copiez ce prompt, remplacez les crochets. | étage 1 (reveal) | **réutilisée** telle quelle depuis `foodeatup-produits-tuto/vo/N6.mp3` (texte générique identique) |
| N10 | Collez-le dans la conversation : votre réception est créée en quelques secondes. | étage 3 (chatbot) | spécifique, générée |
| N11 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | carte de fin (CTA) | **réutilisée** telle quelle depuis `foodeatup-produits-tuto/vo/N8.mp3` |

## Découpage (source 1920×828, 25 fps) — coordonnées mesurées sur les frames réelles

| Seg | Source | Contenu | Bouton (zoom-punch) |
|---|---|---|---|
| intro | carte | AJOUTER MODIFIER OU VALIDER UNE LIVRAISON | — |
| A | 0,30 → 4,00 | Réception du jour (liste) | — |
| B | 4,00 → 4,35 | clic **Contrôle à réception** | (1642, 344), taille (306, 52) |
| C | 4,50 → 10,00 | date/heure + photo bon de livraison | — |
| D | 10,00 → 18,00 | référence + fournisseur | — |
| E | 18,00 → 33,40 | catégorie(s) + état livraison + commentaires | — |
| F | 33,40 → 33,75 | clic **Étape suivante** | (1642, 805), taille (200, 52) |
| G | 33,90 → 38,00 | température produits frais | — |
| H | 38,00 → 38,35 | clic **Ajouter des produits à réception** | (1519, 447), taille (412, 52) |
| I | 38,50 → 41,60 | modale sélection produit + Valider | — |
| K | 41,60 → 43,85 | récapitulatif produits + case terminée | — |
| L | 43,85 → 44,30 | clic **Enregistrer** | (1670, 660), taille (148, 52) |
| M | 44,30 → 47,50 | toast succès + liste + clic nouvelle carte | — |
| N | 47,50 → 54,50 | fiche Livrée + menu action « modifier » | — |
| claude1 | carte générée | reveal — prompt en gros, fond crème | — |
| claude2 | carte générée | confirmation « Copié dans le presse-papiers ! » | — |
| claude3 | carte générée | mockup chatbot Claude | — |
| outro | carte | CTA | — |

Durées de sortie calibrées sur les VO mesurées après génération (règle "segment sur la
VO, pas l'inverse" — voir `FOODEATUP-TUTORIELS-WORKFLOW.md`), pas fixées a priori ici.

## Animations

Mêmes principes que toute la série : Ken Burns sur intro/outro, xfade (0,28 s) entre
tous les segments, `setpts` pour le retiming (jamais `zoompan` sur la vidéo réelle),
zoom-punch (crop fixe centré sur le bouton, ~1.20x) sur les 4 clics d'action listés
ci-dessus. Aucune apostrophe dans les bannières (bug déjà rencontré sur
`foodeatup-ingredients-tuto`).

## Statut

Vidéo demandée par Michael avec instruction explicite de publier une fois le montage
terminé (workflow complet : script → VO → montage → QA → RapidoCMS → Lovable → mise à
jour du dépôt), sans étape de validation intermédiaire séparée cette fois-ci.

## Montage — v1 livrée (2026-08-04)

Durées VO mesurées : N0 4,68 s · N1 5,09 s · N2 3,53 s · N3 2,95 s · N4 5,33 s ·
N5 3,19 s · N6 4,26 s · N7 4,60 s · N8 6,53 s · N9 4,41 s (réutilisée depuis
`foodeatup-produits-tuto/vo/N6.mp3`) · N10 4,18 s · N11 5,02 s (réutilisée depuis
`foodeatup-produits-tuto/vo/N8.mp3`). Segments recalibrés une première fois sur ces
mesures, puis une seconde fois avec une marge supplémentaire (~0,3 s/segment) pour
absorber le GAP inter-lignes après une première passe où la dérive croissait ligne
après ligne (piège déjà documenté dans `FOODEATUP-TUTORIELS-WORKFLOW.md`).

**Sortie** : `out/foodeatup-reception-livraison-tuto-v1.mp4` — **58,88 s**, H.264
1920×828/25fps/yuv420p, AAC 48 kHz stéréo, faststart confirmé. Peak audio final
**-7,24 dBFS**. QA de synchronisation : image extraite au timestamp exact des 12
lignes VO sur le rendu final — toutes tombent sur leur écran/étage prévu (dérive
résiduelle max 2,15 s avant récupération complète sur l'étage Claude, comparable aux
autres tutos de la série).

**Statut : publiée le 2026-08-04** (RapidoCMS + Lovable, sans étape de validation
intermédiaire — instruction explicite de Michael pour cette vidéo). Voir
`LOVABLE-FOODEATUP-DOCS.md` pour l'entrée du tableau de suivi.

## Doublon détecté et résolu (2026-08-04)

En publiant sur Lovable, l'agent a signalé une entrée existante `controler-reception-livraisons`
(« Contrôler à réception de vos livraisons (Module HACCP) ») couvrant le même écran
(Réception du jour → Contrôle à réception → date/heure/photo/référence/fournisseur →
conforme/non conforme, + menu DLC/Température/Scanner) avec sa propre vidéo
(`foodeatup-reception-tuto-v1`, 51 s). Je n'avais pas vérifié l'existant avant de
monter cette vidéo. Question posée à Michael : garder les deux, remplacer l'ancienne,
ou annuler la nouvelle — **réponse : remplacer l'ancienne**. L'entrée
`controler-reception-livraisons` a été supprimée de `src/data/tutorials.ts` (le fichier
vidéo reste dans la bibliothèque RapidoCMS, jamais supprimé — règle standing de
sauvegarde). ⚠️ Chevauchement partiel non résolu : `scanner-ean-et-dlc-reception`
couvre déjà en détail le menu DLC/Température/Scanner avec ses propres
`claudePrompts[]` — cette vidéo n'y touche que dans son dernier segment/N8, à garder
en tête pour la prochaine vidéo réception/HACCP plutôt que d'ajouter un 3e doublon.

**Leçon pour la suite** : avant de monter une nouvelle vidéo, grep les slugs/mots-clés
du sujet dans `src/data/tutorials.ts` (via `mcp__Lovable__read_file` ou
`search_files`) pour repérer un doublon éventuel AVANT de générer la VO et le montage,
pas après publication.
