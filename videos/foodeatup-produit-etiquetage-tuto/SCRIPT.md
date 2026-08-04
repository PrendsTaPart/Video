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

## Statut — script validé par Michael le 2026-08-04

## Voix off (8 lignes) — validée, VO générée (ElevenLabs, voix Adam FR
`TGAegA0zNRi8I6nUdq3i`, `eleven_multilingual_v2`)

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

N7 réutilisé tel quel depuis `foodeatup-tva-tuto/vo/N8.mp3` (CTA générique, texte
identique) — zéro crédit ElevenLabs dépensé sur cette ligne.

## Découpage final (`build.py`)

Coordonnées de clic mesurées par seuillage colorimétrique sur les frames réelles
(script Python, pas à l'œil) : bouton « Ajouter un produit » (1429, 343), bouton
« Ajouter » (soumission modale, 1024, 604).

**Piège rencontré et corrigé** : le premier montage plaçait la fenêtre brute du
zoom-punch B sur 7,60→8,70 s ; or le clic déclenche un scroll de la page en arrière-plan
qui décale le bouton de ~160 px verticalement dans cette fenêtre (page réelle, pas la
modale), désynchronisant le cadrage du zoom. Fenêtre resserrée à 7,45→7,65 s (juste
l'instant du clic, avant le scroll) — vérifié stable par seuillage sur plusieurs frames
avant/après. Le bouton « Ajouter » de la modale, lui, ne bouge pas (overlay fixe,
vérifié stable sur 57,9→58,5 s).

**Piège rencontré et corrigé (2)** : premier calage des durées de segment sur la durée
brute de chaque ligne VO (facteurs de vitesse jusqu'à x5,4) → dérive cumulée jusqu'à
+4,8 s sur les dernières lignes et carte de sortie auto-étendue à 13,7 s de silence
visuel (même bug que documenté sur le tuto unités). Corrigé en redimensionnant les
segments avec une marge (~+0,3 s sur la durée VO), carte de sortie ramenée à une
extension de 7,72 s.

| Seg | Rush (source) | Sortie | Contenu |
|---|---|---:|---|
| intro | carte | 3,00 s | CRÉER UN PRODUIT POUR ÉTIQUETAGE |
| A | 0,20 → 7,45 | 4,50 s | accueil, scroll, clic tuile Etiqueteuse |
| B | 7,45 → 7,65 | 0,90 s | **zoom-punch** clic « Ajouter un produit » (1429, 343) |
| C1 | 9,00 → 24,00 | 4,20 s | nom « Abricot », marque « fruiti », code-barres |
| C2 | 24,00 → 48,00 | 4,68 s | catégorie « Fruits », poids « 10 », unité « kg » |
| C3 | 48,00 → 58,30 | 3,52 s | onglet Paramètres : durée de vie « 5 », alerte DLC « 2 » |
| D | 58,30 → 58,80 | 0,90 s | **zoom-punch** clic « Ajouter » (1024, 604) |
| E | 58,80 → 64,88 | 9,80 s | liste mise à jour, carte « Abricot » (Fruits, #00000024) |
| outro | carte | 7,72 s (auto-étendue) | CTA |

**Durée finale livrée : 37,04 s** — H.264 High/yuv420p 1920×828, AAC 48 kHz stéréo,
faststart (moov avant mdat). Audio : true peak **-7,0 dBFS**. Decode 0 erreur.

## Animations

Mêmes principes que toute la série : Ken Burns sur les cartes, xfade (0,28 s), bandeaux
d'étape (accents restaurés, pas d'apostrophe dans les textes de bandeau — piège déjà
documenté sur `foodeatup-ingredients-tuto`), encadré orange pulsant sur les 2 clics.
Pas de clip avatar dans ce dossier.

## Statut publication

**Montage terminé, non publié.** Script validé par Michael le 2026-08-04. Vidéo montée
livrée pour validation finale (`SendUserFile`) — en attente de retour avant toute mise
en ligne RapidoCMS / LinkedIn / Lovable, conformément à la règle du dépôt
(`FOODEATUP-TUTORIELS-WORKFLOW.md` et `LOVABLE-FOODEATUP-DOCS.md`).
