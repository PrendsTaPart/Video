# Vidéo 26 — Architecture PRONOCLIP

## Aujourd'hui : deux modules complémentaires, non reliés automatiquement

**Module A — chaîne n8n (instance BraindCode)**
API-Football → PRONO_0 (matchs du jour) → WC2026_1 (agent Gemini, pronostic structuré) → WC2026_2 (prompts + images début/fin) → WC2026_3 (vidéo, détail non vérifié). En complément : WC2026_4 (effectifs, hebdomadaire) et W10 (cotes). W6, W7 et W8 sont inactifs.

**Module B — plugin Claude Code `pronoclip-video` 0.4.0 (dépôt)**
Commande `/pronoclip-cartoon` : scénariste → directeur artistique (generate_image RapidoCMS) → compositeur (HyperFrames, rendu local) → vérificateur légal (bloquant). Puis `publication-cms` (brouillons RapidoCMS) et `suivi-rh-daily` (tâches et dailies RapidoRH).

**Liaison A ↔ B** : aucune dans le code du dépôt. La vidéo la présente comme « à construire ».

## Architecture cible proposée

```
API-Football → n8n PRONO_0 → n8n WC2026_1 (Gemini)
      → [à construire] JSON du pronostic déposé dans RapidoRH (tâche du match)
      → Claude Code /pronoclip-cartoon (lit la tâche) → HyperFrames (local)
      → vérificateur légal → RapidoCMS brouillon → validation humaine → publication
      → /pronoclip-daily → RapidoRH
```

Garde-fous :

- aucun service payant (HeyGen, render_video) sans OUI explicite ;
- aucune publication automatique ;
- aucun pari ;
- probabilités affichées comme « non calibrées » tant qu'elles n'ont pas été validées sur des résultats historiques.
