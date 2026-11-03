# Vidéo 26 — Audit n8n (vérifié le 27/10/2026)

Lecture seule via le connecteur N8n (instance n8n.braindcode.com). Aucun workflow n'a été exécuté, modifié ni publié.

## 1. Workflows actifs

| Workflow | ID | Nœuds | Exécutions conservées | Constat |
|---|---|---|---|---|
| PRONO_0_Fixtures_Today | E3ZXA8HpZpHZDQHx | 6 | 0 | Webhook POST → API-Football (1 appel, filtre des ligues dans le workflow, plan gratuit) → liste numérotée |
| WC2026_1_Match_Prediction | UmRn6ULKA64C7MVN | 14 | 0 | Fixture → H2H (10 derniers) → stats domicile/extérieur → effectifs → agent Gemini → JSON → déclenche WC2026_2. **`season=2026&league=1` codés en dur** (Coupe du monde uniquement) |
| WC2026_2_Frame_Generator | oHewWw1ENJCYZYLe | — | 0 | actif, déclenché par WC2026_1 |
| WC2026_3_Video_Generator | Dp4WiZpSjan5A6IV | — | non lisible | **actif mais fermé au MCP** : contenu et coûts non vérifiables. Une variante « vercel » (pikHvksov4OQf2sV) est inactive |
| WC2026_4_Squad_Sync | E3EweIRCb131vNeE | — | 1 (erreur) | **En erreur** le 26/10 : l'URL utilise `$env.APP_URL`, or `$env` est bloqué sur l'instance → « Invalid URL » |
| W10 — Pre-Match Odds Snapshot | UFFE4AMu0WySoHyQ | — | 192 | **Fonctionne** : succès toutes les heures (dernier 27/10 08:00 UTC) |

## 2. Workflows inactifs

W6 — Auto Publish RapidoCMS (HhXt2cuPxhKmOLcQ), W7 — Video Assembly Worker (LXoQ5jpQb71aI92q), W8 — Viral Trend Watcher (yayEz3y4Y9Fpck1u) : **inactifs**, conforme à la vidéo.

## 3. Fonctionnalités testées

Rien n'a été déclenché pour la vidéo. **Aucune exécution n'est conservée** pour PRONO_0, WC2026_1 et WC2026_2, ce qui peut aussi venir des réglages de rétention. Aucune exécution n'est montrée comme réelle.

## 4. Connexions réellement opérationnelles

- W10 (cotes) tourne toutes les heures.
- La chaîne PRONO_0 → WC2026_1 → WC2026_2 → WC2026_3 est câblée par webhooks internes, sans preuve d'exécution récente.
- Aucune liaison avec le plugin Claude Code `pronoclip-video`.

## 5. À terminer / corriger

- **🔴 Clé API-Football en clair** dans 6 nœuds HTTP de WC2026_1 **et dans une note (sticky note)** du workflow. **À faire tourner immédiatement**, puis à déplacer dans un credential n8n. La clé n'est reproduite nulle part dans ce dépôt.
- **🔴 Webhooks sans authentification** : `fixtures-today` (PRONO_0) et `wc2026-predict` (WC2026_1). N'importe qui connaissant l'URL peut consommer le quota API-Football et Gemini. Ajouter une authentification par en-tête.
- **WC2026_4** : remplacer `$env.*` par des credentials ou des valeurs de configuration.
- **WC2026_1** : paramétrer la saison et la compétition.
- **WC2026_3** : ouvrir l'accès MCP (lecture) pour l'auditer.
