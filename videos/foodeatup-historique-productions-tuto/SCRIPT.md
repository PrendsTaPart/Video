# Tutoriel — Retrouver l'historique de ses productions (module HACCP)

Module 4 — HACCP, onglet **Historique > Production**. Durée du rush : **16,48 s** —
H.264 (Main)/yuv420p, AAC 48 kHz stéréo, 1920×828, 25 fps. Piste audio silencieuse
(peak -inf dBFS, pas de voix native) — voix off entièrement ElevenLabs, comme le
reste de la série. Decode 0 erreur.

## Ce que montre le rush

Le rush part de la page **« historique haccp »** (4 cartes : Températures,
Traçabilité, Plan de nettoyage, **Production** — 14 productions), clique sur la
carte **Production**, puis montre le tableau de bord **Historique > Productions** :

- 6 indicateurs en tête : Productions réalisées (205), Portions produites (8438),
  Efficacité moyenne (100.5%), Plats produits (12), Recettes produites (193),
  Portions planifiées (8394) ;
- un graphique **« Tendance des 6 derniers mois »** (barres mensuelles) ;
- une barre de recherche (« Rechercher un plat ou recette »), un filtre
  **« Tous (plats + recettes) »**, un sélecteur de **Période** et un bouton
  **Exporter CSV** ;
- une liste défilante de chaque plat/recette avec badge Plat/Recette, nombre de
  productions, portions, % d'efficacité et date/heure de la dernière production
  (Brik à l'œuf tunisien, Dragon Roll, Plateau Découverte, Salmon Maki, Burrata
  crémeuse, Couscous royal d'été, Bananes flambées, Accras de Morue Créoles...).

À confirmer avec Michael : le **nom exact du sous-dossier Drive** correspondant
(module HACCP, sous-catégorie Historique/Production) pour le champ `subcategory`
côté Lovable — non déductible du rush seul.

## Voix off (9 lignes) — proposition, à valider avant génération ElevenLabs

| # | Texte | Segment |
|---|---|---|
| N0 | Retrouvez l'historique de toutes vos productions FoodEatUp, en un coup d'œil. | intro |
| N1 | Depuis Historique, cliquez sur Production pour ouvrir le suivi. | A + clic B |
| N2 | Productions réalisées, portions produites, efficacité moyenne : tout est calculé automatiquement. | C — KPIs |
| N3 | La tendance des 6 derniers mois vous montre l'évolution de votre activité. | D — graphique |
| N4 | Recherchez un plat, filtrez par période et exportez tout en CSV en un clic. | E — liste + outils |
| N5 | De quoi repérer vos best-sellers et ajuster vos prochaines productions. | F — bénéfice |
| N6 | Vous pouvez aussi le faire depuis Claude : copiez ce prompt, remplacez les crochets. | étages 1+2 (réutilisé) |
| N7 | Collez-le dans la conversation : votre historique de production s'affiche en quelques secondes. | étage 3 |
| N8 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | carte de fin (CTA, réutilisé) |

N6/N8 réutilisables tels quels depuis `foodeatup-tva-tuto/vo/` (texte générique,
zéro crédit ElevenLabs à dépenser dessus). N0-N5 et N7 sont nouvelles lignes à
générer (voix Adam FR `TGAegA0zNRi8I6nUdq3i`, `eleven_multilingual_v2`).

## Découpage — estimation avant montage (à recaler sur la durée réelle des VO)

| Seg | Source | Contenu |
|---|---|---|
| intro | carte | RETROUVER SES PRODUCTIONS HISTORIQUE |
| A | 0,00 → 4,30 | page « historique haccp », 4 cartes, survol de Production |
| clic | 4,30 → 4,60 | **zoom-punch** sur la carte Production (≈1556, 610) |
| C | 4,60 → 6,60 | 6 indicateurs (KPIs) du tableau de bord |
| D | 6,60 → 9,50 | graphique « Tendance des 6 derniers mois » |
| E | 9,50 → 16,48 | recherche / filtre Période / Exporter CSV + liste des plats-recettes (scroll) |
| claude1 | carte générée | reveal — prompt en gros, fond crème |
| claude2 | carte générée | confirmation « Copié dans le presse-papiers ! » |
| claude3 | carte générée | mockup chatbot Claude |
| outro | carte | CTA |

Coordonnées de clic estimées par lecture visuelle des frames (survol carte
Production entre t≈4,0 s et t≈4,7 s dans le rush) — à confirmer par seuillage
colorimétrique au moment du montage, comme sur le reste de la série.

## Séquence Claude — module partagé

Correspondance MCP trouvée : `mcp__FoodEatUp__list_top_productions(establishment_id,
days?)` — « Liste les plats/recettes les plus produits sur une période. » C'est
un outil de lecture seule, cohérent avec cet écran (aucune action de création
n'apparaît dans le rush).

> Montre-moi l'historique des productions des [nombre] derniers jours pour mon
> établissement FoodEatUp (ID [ID établissement]).

Même texte côté fiche Lovable (`claudePrompt`).

## Animations

Mêmes principes que toute la série : Ken Burns sur les cartes, xfade (0,28 s),
bandeaux d'étape, encadré orange pulsant sur le clic (un seul clic dans ce
rush, pas de formulaire à remplir — écran de consultation uniquement). Pas de
clip avatar dans ce dossier.

## Statut

**Script proposé, en attente de validation de Michael — STOP obligatoire avant
génération audio ElevenLabs**, conformément à `FOODEATUP-TUTORIELS-WORKFLOW.md`
(étape 3). Ne pas générer la VO, monter, publier sur RapidoCMS/LinkedIn/Lovable
tant que ce script n'est pas confirmé (ou ajusté selon retour).

Point à signaler séparément à Michael : sa demande mentionne une série de
**157 vidéos**, mais la mémoire du dépôt (`FAISABILITE-SERIE-TUTORIELS.md`,
`LOVABLE-FOODEATUP-DOCS.md`) documente un périmètre de **91-92 vidéos** (94
annoncées, 92 dossiers Drive réels, 91 avec rush complet), dont 10 déjà
publiées + 1 (« Ouvrir sa vitrine en ligne ») livrée et en attente de
validation. Écart à clarifier avant de mettre à jour un quelconque suivi
« 157 vidéos » dans le dépôt — pas de nombre inventé.
