---
description: Récupère les chiffres réels FoodEatUp pour les variables {{CA_MOIS}}, {{COUVERTS}}, {{RUPTURES_EVITEES}}
---

# /ep-data

Étape 2 du pipeline. Lecture seule sur le MCP FoodEatUp.

## Garde-fou (bloquant)

Refuse de s'exécuter si `manifest.json.pipeline.ep-refs.status != "done"`.

## Étapes

1. Appeler en lecture seule :
   - `finance_summary` → `{{CA_MOIS}}`
   - `get_daily_brief` → contexte / `{{COUVERTS}}`
   - `list_low_stocks` → `{{RUPTURES_EVITEES}}`
2. **Zéro chiffre inventé.** Toute variable non résolue devient `"__SUPPRIMER__"` — jamais
   une estimation. Un chiffre non sourcé dans une communication commerciale française est
   une pratique commerciale trompeuse (art. L.121-2 du Code de la consommation).
3. Écrire les valeurs (ou `"__SUPPRIMER__"`) dans `manifest.json.pipeline.ep-data.variables`.
4. Lister explicitement à l'utilisateur les cartons qui seront supprimés du motion design
   faute de donnée sourcée.
5. Mettre à jour `manifest.json.pipeline.ep-data.status = "done"`.
