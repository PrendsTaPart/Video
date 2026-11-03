# Vidéo 26 — Audit GitHub PRONOCLIP

Dépôt `PrendsTaPart/PRONOCLIP`, **public**, lu en lecture seule le 27/10/2026.

## Branches

| Branche | Dernier commit |
|---|---|
| `main` | `fe2041c` Merge pull request #3 (claude/pronoclip-video-plugin-setup-m2outx) |
| `claude/pronoclip-video-plugin-setup-m2outx` | `7a96b9f` Merge pull request #4 from main (13/07/2026) |

PR #1 à #4 fusionnées, d'après l'historique. Les PR ouvertes n'ont pas été listées : le dépôt n'est pas rattaché à la session pour l'API GitHub.

## Plugin `pronoclip-video` 0.4.0 — vérifié

- Manifeste : `.claude-plugin/plugin.json` (auteur BraindCode) et `.claude-plugin/marketplace.json`.
- **5 commandes** : pronoclip-match, pronoclip-routine, pronoclip-daily, pronoclip-cartoon, pronoclip-presentateur.
- **8 skills** : video-pronostic, routine-matchs, studio-cartoon, presentateur-heygen, publication-cms, audio-narration, sequences-match, suivi-rh-daily.
- **4 agents** : scenariste-cartoon, directeur-artistique-cartoon, video-composer, verificateur-legal (bloquant).
- **6 références** : charte, directives légales, prompts des séquences, scripts de narration, storyboard cartoon, template de composition.
- Garde-fous écrits dans le dépôt :
  - HeyGen (~1 crédit/s) et `render_video` sont payants : confirmation explicite obligatoire, jamais dans une routine automatique ;
  - aucun logo de club ni joueur identifiable ;
  - mention « Pronostic — contenu généré par IA » obligatoire.
- Le README indique « Passage en 1.0.0 après validation de la section Recette » : la recette (11 tests) n'est **pas** marquée comme passée.

## Secrets

- Recherche `api_key|token|secret|sk-|Bearer` dans le dépôt : **aucun secret en dur**. Les clés (`HEYGEN_API_KEY`, `ELEVENLABS_API_KEY`) sont lues dans l'environnement.
- Le dépôt étant **public**, ne jamais y verser d'export n8n brut.

## Ce que le dépôt ne contient pas

- Aucun workflow n8n : les WC2026 / PRONO_0 vivent seulement dans l'instance n8n.
- Aucune vidéo produite. La « Recette » n'a pas de sortie archivée.
- Aucun code qui appelle les webhooks n8n : **le plugin et la chaîne n8n ne sont pas reliés dans le code**.
