# Tutoriel — Créer un produit pour l'étiquetage FoodEatUp

Module **HACCP**, sous-fonctionnalité « Etiqueteuse » (accessible depuis Accueil →
tuile « Etiqueteuse », ou menu Traçabilité → Etiqueteuse). Rush fourni par Michael :
`Ajouter/Créer un produit à sélectionner pour vos étiquettes.mp4`, **64,9 s**,
1920×828, H.264/AAC. Cartes intro/outro fournies (`CRÉER UN PRODUIT POUR
ÉTIQUETAGE.jpg` et la carte CTA générique déjà utilisée sur les autres tutos — même
fichier, hash identique à `foodeatup-produits-tuto/assets/outro.jpg`, réutilisée telle
quelle sans re-upload).

## Ce que montre le rush

1. Accueil (« bonjour, soulayma ») → scroll vers la seconde rangée de tuiles module
   HACCP → clic sur la tuile **Etiqueteuse**.
2. Arrivée sur `Accueil > Etiqueteuse` (liste de produits existants : Farine, Pizza
   margaritta) → clic sur **Ajouter un produit** (bouton orange, en haut à droite).
3. Modale « Ajouter un produit », onglet **Détails produit** :
   - Nom du produit : « Abricot »
   - Marque du produit : « fruiti »
   - Code à barre du produit : « 3760123456789 »
   - Catégorie : « Fruits »
   - Poids/Volume : « 10 »
   - Unité : « kg »
   - Allergène : liste de cases à cocher visible, aucune cochée dans le rush (pas
     pertinent pour un abricot brut)
4. Onglet **Paramètres** :
   - Durée de vie : « 5 » (jours)
   - Alerte DLC : « 2 » (jours avant la DLC)
5. Clic sur **Ajouter** → retour sur la liste : le produit « Abricot » apparaît
   (catégorie Fruits, référence `#00000024`), prêt à être sélectionné pour
   l'impression d'une étiquette.

## Pas de séquence Claude sur cette vidéo

Vérifié dans les outils `mcp__FoodEatUp__*` disponibles : aucun outil ne correspond à
cette action précise. `create_haccp_label` crée directement une **étiquette DLC**
(paramètres : `ingredient_name`, `quantity`, `unit`, `type` Frais/Surgelé/…, `dlc`,
`lot_number`, `temperature`, `storage_location`) — c'est l'étape *suivante* dans
FoodEatUp (impression d'une étiquette pour un lot précis), pas la création de ce
**produit catalogue réutilisable** (marque, code-barres, allergènes, durée de vie,
seuil d'alerte DLC) montrée dans ce rush. `create_product` (menu/carte, avec prix HT
et TVA) ne correspond pas non plus : aucun champ prix ici. Aucun outil MCP n'expose
la création de ce produit-catalogue « Etiqueteuse » tel quel aujourd'hui → pas de
`claudePrompt` inventé, même règle que sur `regler-ses-unites` (ce champ reste absent
côté fiche Lovable, section masquée automatiquement par le template).
**À confirmer avec Michael** : si un outil équivalent existe côté MCP mais n'a pas
été repéré, il pourra être ajouté après coup sans reprendre la vidéo.

## Voix off (8 lignes) — PROJET, à valider avant génération audio

| # | Texte | Ancrage |
|---|---|---|
| N0 | Créer un produit pour l'étiquetage, en quelques clics. | carte d'intro |
| N1 | Depuis l'accueil, ouvrez l'Etiqueteuse, puis cliquez sur Ajouter un produit. | clics Etiqueteuse → Ajouter un produit |
| N2 | Donnez-lui un nom, une marque, et son code-barres si vous en avez un. | nom / marque / code-barre |
| N3 | Choisissez sa catégorie, son poids ou son volume, et l'unité qui va avec. | catégorie / poids / unité |
| N4 | Réglez sa durée de vie et le délai d'alerte avant la DLC. | onglet Paramètres |
| N5 | Cliquez sur Ajouter : votre produit rejoint aussitôt la liste de l'étiqueteuse. | clic Ajouter → succès |
| N6 | Il est maintenant prêt à être sélectionné pour l'impression de vos étiquettes, DLC calculée automatiquement. | bénéfice |
| N7 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | carte de fin (CTA, réutilisable telle quelle depuis `foodeatup-tva-tuto/vo/N8.mp3`) |

N7 réutilisable telle quelle (texte générique identique) — zéro crédit ElevenLabs
supplémentaire si validé sans modification.

## Découpage envisagé (à affiner au montage, après validation du script)

| Seg | Rush (approx.) | Contenu |
|---|---|---|
| intro | carte | CRÉER UN PRODUIT POUR ÉTIQUETAGE |
| A | 0,0 → 6,0 | accueil, scroll, clic tuile Etiqueteuse |
| B | 6,0 → 9,0 | **zoom-punch** clic « Ajouter un produit » |
| C | 9,0 → 21,0 | saisie nom / marque / code-barre |
| D | 21,0 → 48,0 | catégorie / poids / unité |
| E | 48,0 → 57,0 | onglet Paramètres, durée de vie / alerte DLC |
| F | 57,0 → 60,0 | **zoom-punch** clic « Ajouter » |
| G | 60,0 → 64,9 | liste mise à jour, carte « Abricot » visible |
| outro | carte | CTA |

Coordonnées de clic exactes à mesurer par seuillage colorimétrique sur les frames
réelles au moment du montage (`build.py`), pas à l'œil — même méthode que le reste de
la série.

## STOP — validation requise

Conformément à `FOODEATUP-TUTORIELS-WORKFLOW.md` : **ne pas générer la voix off tant
que ce script n'est pas validé par Michael.** Retours possibles : texte des lignes,
durée, présence/absence de la séquence Claude, découpage.

## Statut publication

Non publiée — en attente de validation du script (étape 1/2), puis du montage final
(étape 2/2) avant toute mise en ligne RapidoCMS / LinkedIn / Lovable.
