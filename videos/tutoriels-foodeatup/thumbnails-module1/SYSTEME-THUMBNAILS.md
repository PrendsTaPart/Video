# Système Thumbnails YouTube — FoodEatUp · Module 1

« Configuration d'un compte et d'un établissement » (V00 → V13). Une série homogène :
canon de personnage verrouillé + gabarit unique + 14 blocs variables.

## Décisions structurantes
1. **Le texte se pose en post-prod** (Canva/Figma, vraie typo Goodly) — jamais généré. Image = espace vide à gauche réservé au titre.
2. **Titre miniature ≠ titre YouTube** : 1 mot d'accroche + 2-3 mots max (lisible à 168×94 px).
3. **Fond sombre `#0F1A23`** (charte : arrière-plans sombres) → texte blanc + accents bleus autorisés, chef qui ressort.

## Charte
Typo **Goodly** · fond `#0F1A23` · primaire `#007BFF` · halo `#A6D0FF` · fond clair `#FCF9E6`.
Texte couleur uniquement sur fond noir/blanc ; sur fond coloré → noir 100 %. Logo = tête chef clin d'œil + double-O infini, zone protection ½ hauteur, priorité gauche. Motif toque en filigrane.

## Canon chef — VERROUILLÉ
Voir `rapido-kb/traits-personnages.md`. Axes variables : pose · expression · objet · accent lumineux.
Clin d'œil réservé V00 / V13. **Portrait de référence validé : `rapido-kb/personnages.json` → canon-v1.**

## Gabarit (16:9, 1280×720)
Chef dans les **40 % droite**, buste, tourné vers la gauche, œil au tiers supérieur. **55 % gauche = espace
vide** (titre en post-prod). Fond sombre + gradient radial + motif toque 6 % + rim light `#007BFF` + brume `#A6D0FF`.
Objets = hologrammes en verre bleu lumineux `#007BFF`. Aucun texte / logo / QR dans l'image.

Zones post-prod : logo blanc haut-gauche · pastille `MODULE 1 · NN` (`#007BFF`, chiffres noir) · accroche (Goodly Medium `#007BFF`) + titre (Goodly Bold blanc) · bas-droit vide (badge durée).

## Pipeline réel utilisé
1. Portrait canon : `RapidoCMS generate_image` (3 variantes) → **STOP validation** → canon-v1 verrouillé.
2. 14 scènes : `RapidoCMS images_to_image` depuis le portrait canon (garantit la cohérence).
   ⚠️ RapidoCMS sort en **portrait 1024×1536** → reframe 16:9 en post via `reframe.py`
   (canvas sombre + chef à droite + gauche vide + blend feutré).
3. Livraison : `output/thumb-vNN.jpg` (1280×720) + upload biblio RapidoCMS.

## Les 14 blocs (accroche · titre miniature · objet)
| # | Accroche | Titre | Objet hologramme |
|---|---|---|---|
|00|CRÉER|SON COMPTE|panneau formulaire + enveloppe + coche verte + clé (clin d'œil)|
|01|CRÉER|SA BOUTIQUE|devanture de restaurant miniature qui tourne|
|02|CHOISIR|SON ABONNEMENT|3 cartes d'abonnement en arc, la centrale haloée|
|03|REMPLIR|SON PROFIL|carte d'identité entreprise + tampon de validation|
|04|PARAMÉTRER|LA TVA|symboles % en orbite + calculatrice|
|05|AJOUTER|SES FOURNISSEURS|cagette de légumes + camion de livraison|
|06|BRANCHER|SON MCP|constellation de nœuds connectés + prise|
|07|CRÉER|SES CATÉGORIES|dossiers à onglets en grille|
|08|RÉGLER|SES UNITÉS|balance + verre doseur + cuillères|
|09|SAISIR|SES INGRÉDIENTS|ingrédients en lévitation (tomate, basilic, ail, farine, œuf)|
|10|CRÉER|SES PRODUITS|plat dressé sous cloche en verre|
|11|ÉCRIRE|SES RECETTES|livre de recettes ouvert + marqueurs d'étapes|
|12|OUVRIR|SA VITRINE|tablette vitrine en ligne + cloche de notification|
|13|DIFFUSER|SON QR CODE|carré blanc vide (vrai QR en post-prod) + chevalet + flyer vierges|

## Titres YouTube ↔ miniatures : voir §10 de la spec source (gardée en mémoire).
