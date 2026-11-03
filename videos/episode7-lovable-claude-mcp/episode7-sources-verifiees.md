# Épisode 7 — Sources et fonctionnalités vérifiées (27/10/2026, lecture seule)

Aucune modification n'a été faite : pas de `send_message`, pas d'écriture MCP, aucun fichier Lovable changé. Le fichier `.env` des deux projets a été repéré dans la liste des fichiers mais **jamais ouvert**.

## Connecteur Lovable dans Claude (outils réellement disponibles)
| Besoin du brief | Outil | Testé ici |
|---|---|---|
| Lister workspaces et projets | `list_workspaces`, `list_projects` | oui (workspace Braindcode : 135 projets ; plus de 50 workspaces) |
| Ouvrir un projet | `get_project` | oui (2 projets) |
| Lire fichiers et code | `list_files`, `read_file` | oui |
| Historique de développement | `list_edits`, `list_messages` | `list_edits` oui |
| Différences entre versions | `get_diff` | oui (commit 7c5e6c9) |
| Instructions à l'agent Lovable | `send_message` (+ `respond_to_approval`) | **non utilisé** (aucune modification autorisée) |
| Connecteurs MCP | `list_connectors`, `list_custom_connectors`, `add_connector` | non appelés |
| Vérifier les modifications | `get_diff`, `list_edits` | oui |

## BraindCode Plugins — projet Lovable `bc246af9-fd93-4df0-b4ed-8fbddf30647e`
- Nom Lovable « Braindcode plugin », publié, dernier commit `60e4fad`. Marketplace française de plugins Claude Code synchronisée avec GitHub. Stack : TanStack Start + Supabase (migrations drizzle).
- Manifeste `.lovable/mcp/manifest.json` : serveur `rapido-plugins-mcp` v0.12.0 « Rapido Plugins MCP », chemin `/mcp`, auth OAuth (émetteur Supabase du projet).
- **58 outils : 41 en lecture (`readOnlyHint`), 17 en écriture** (`creer_ma_kb`, `ajouter_favori`, `definir_variable`, `planifier_routine`, `marquer_progression`, `installer_routine`, `signaler_ecart_mcp`, `proposer_routine`, `mettre_a_jour_routine`, `enregistrer_execution_routine`, `declarer_mcp`, `enregistrer_kpi`, `enregistrer_kpi_lot`, `definir_kpi`, `rattacher_kpi_routine`, `promouvoir_routine`, `rendre_verdict_routine`).
- Architecture : `src/lib/mcp/index.ts` + `src/lib/mcp/tools/<outil>.ts` (un fichier par outil) + utilitaires (`plugins-utils`, `supabase-user`, `kb-utils`, `routines-utils`, `search-utils`).
- Code lu : `lister_plugins.ts` (paramètres Zod `mcp`, `categorie`, `q`, `seulement_nouveaux` ; `readOnlyHint: true`), `ajouter_favori.ts` (`ctx.isAuthenticated()` sinon « Authentification requise (OAuth). »), `supabase-user.ts` (le jeton de l'utilisateur est transmis à Supabase : la base applique ses droits RLS).
- Historique réel (`list_edits`) : 18/07 « Corrigé outils MCP pour JSON », « Ajouté enrichissement MCP » · 19/07 « Ajouté les 4 outils MCP » (7c5e6c9, v0.6.0 → v0.7.0 : `collections_pour_outil`, `creer_ma_kb`, `prompts_pour_agent`, `prompts_pour_outil`) · 28/07 « Corrigé KB et index MCP » · 31/07 « Ajouté 6 outils MCP » · 23/08 « Ajouté 14 outils MCP lecture », « Ajouté registre MCP en base », « Créé le socle db routines avec RLS » · 24/08 « Ajouté enregistrement MCP » · 10/10 « Implemented MCP widgets », « Corrigé boucle et serveur MCP » · 25/10 « Récupéré les 4 routes MCP ». Un historique plus ancien existe (non parcouru). Les premiers prompts (`list_messages`) n'ont pas été lus : la reconstitution part des messages de commit.

## BraindCode Extensions Hub — projet Lovable `652d74c0-a111-4f76-abd2-15afc1c30ce8`
- Publié (build.braindcode.com), dernier commit `0535c45`. Manifeste : serveur `braindcode-extensions-hub` v1.0.0, chemin `/api/mcp`, OAuth (Supabase).
- **44 outils : 23 en lecture, 21 en écriture** (`reserve_project`, `save_project_spec`, `publish_project`, `register_ai_developer`, `start_prompt_step`, `request_human_validation`… ). C'est le serveur du connecteur « Braindcode Build » de cette session.

## Tests réels (27/10)
1. Lecture via le connecteur authentifié : `lister_plugins {"q":"foodeatup"}` → 11 plugins (foodeatup 1.11.5 · 27 skills · 5 agents ; foodeatup-boucles 0.3.0 ; foodeatup-iris 0.2.0 ; foodeatup-tutoriel 0.2.0 ; rapido-canva 1.0.3 ; rapido-direction 1.1.0 ; rapido-elevenlabs 0.1.1 ; rapido-employe 0.1.0 ; rapido-gmaps 0.5.0 ; rapido-lovable 1.5.2 ; rapido-relation-client 0.2.0).
2. Contrôle de refus : `POST https://plugin.braindcode.com/mcp` sans jeton (initialize, tools/list, tools/call) → **HTTP 401 `{"error":"unauthorized"}`**, en-tête `WWW-Authenticate: Bearer realm="mcp", resource_metadata=".../.well-known/oauth-protected-resource"`. Le transport exige OAuth même pour les outils publics.
3. Fiche `obtenir_plugin rapido-lovable` 1.5.2 : skills `connecteur-mcp-lovable`, `agent-ia-produit`, `site-restaurant`, `usine-a-landing`, `sync-marque-lovable`… ; agent `architecte-lovable` ; hook `garde-lovable` ; serveurs lovable, foodeatup, rapidocms, rapidocrm, rapidorh.

## Technologies affichées (scène 5)
- Lovable (TanStack + Supabase) : Rapido Plugins MCP, BraindCode Build — vérifié par les manifestes.
- Laravel (`laravel/mcp`) : RapidoRH, `Mcp::web('/mcp/rapidorh', RapidoRHServer::class)` — vérifié dans le code lu lors de l'épisode 8.
- Python (FastAPI + FastMCP) : RapidoATS, serveur MCP v2 — d'après le CLAUDE.md du dépôt RapidoATS.
- FoodEatUp, RapidoCRM, RapidoCMS : technologie **non vérifiée**, non affichée.

## Médias
- Portrait : `braindcode-profil.jpg` (photo réelle). Poses : bibliothèque Michael existante.
- Logos officiels : `videos/video-20/assets/logos/logiciels/` (Claude, Lovable, FoodEatUp, RapidoCRM, RapidoCMS, RapidoRH) et BraindCode. Aucun logo redessiné.
- Captures : pages publiées de BraindCode Plugins et Extensions Hub (27/10), dans `captures/`.
- Aucune vidéo Higgsfield générée.

## À signaler
- La note « Mon plugin Vidéo » du brief : non utilisé (chaîne de montage habituelle de la série).
