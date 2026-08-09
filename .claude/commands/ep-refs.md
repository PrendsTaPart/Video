---
description: Génère (ou vérifie) les 9 portraits canoniques de la série + 1 planche décor
---

# /ep-refs

Étape 1 du pipeline. Génère une fois pour toutes les portraits canoniques verrouillés de
la série, à partir de `bible/personnages.json` et `bible/01-BIBLE-PERSONNAGES.md`.

## Garde-fous

- **N'appelle jamais le MCP Higgsfield.** Cette commande n'utilise que RapidoCMS.
- **Ne régénère jamais un portrait déjà validé** dans `bible/refs/`. Pour une nouvelle pose,
  repartir du portrait existant via `images_to_image`, jamais de zéro.
- Refuse de s'exécuter si `manifest.json` a déjà `pipeline.ep-refs.status == "done"`
  sans confirmation explicite de l'utilisateur.

## Étapes

1. **Vérification marque (bloquante).**
   - Appeler `get_brand` sur l'id `7` (FoodEatUp).
   - Si `couleur_primaire`, `couleur_fond`, `couleur_texte` ou `logo_url` sont vides/null :
     proposer l'`edit_brand` exact (`#147AFF` / `#0B0B0F` / `#FFFFFF` + URL du logo fournie
     par l'utilisateur) et **attendre validation écrite** avant de continuer.
   - Si le `logo_url` n'est pas connu : **arrête-toi et demande-le**. Ne génère rien.
   - Re-lire `get_brand` pour confirmer après tout `edit_brand`.
   - Mettre à jour `manifest.json.etape_0_marque.status` en conséquence.

2. **Génération des portraits, un par un.**
   - Pour chacun des 9 personnages dans `bible/personnages.json`, construire un prompt
     `generate_image` à partir des `traits_verrouilles` (double-bind : texte + référence
     si une pose antérieure existe).
   - **Montrer chaque rendu à l'utilisateur pour validation avant de l'enregistrer.**
   - Une fois validé, uploader dans la bibliothèque RapidoCMS et sauver la référence
     (URL/ID) dans `bible/refs/`.

3. **Planche décor.** Générer une planche de référence de la cuisine FoodEatUp (décor
   variable de l'épisode 1 — voir `episodes/ep01-la-rentree/02-SCENARIO.md`), même protocole
   de validation.

4. **Mise à jour `manifest.json`** : `pipeline.ep-refs.status = "done"` seulement quand les
   9 portraits + la planche décor sont validés et uploadés.

## Ne fait rien d'autre tant que cette commande n'est pas terminée.
