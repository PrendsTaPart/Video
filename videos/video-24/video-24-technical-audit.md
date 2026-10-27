# Vidéo 24 — Audit technique de RapidoATS

Dépôt privé `braindcode1/RapidoATS`, branche `main`, commit `9caeb26` (22/10/2026). Audit en lecture seule le 27/10/2026. Aucune donnée de production consultée ni modifiée, aucun workflow exécuté, aucune offre publiée, aucun message envoyé.

## Ce qui a été vérifié dans le code

| Élément | Constat | Dans la vidéo |
|---|---|---|
| Frontend React 18 / Vite / TS / Tailwind / shadcn | Pages BaseRAG, Offres, Candidatures, CandidateProfile, Entretiens, InterviewDetail, EntretienAvatar, Communications, Onboarding, Subscription, VideoStudio… | Interface reconstituée (pas de capture) |
| Statuts des candidatures | `src/pages/Candidatures.tsx` : Nouveau, En analyse, Entretien, En attente, Retenu, Refusé. **« Présélectionné » n'existe pas.** | Les six statuts réels |
| Scoring | `score_final = score_ml × 0,4 + score_llm × 0,6` (CLAUDE.md du dépôt) | Montré comme aide au tri, avec avertissement |
| Serveur MCP (FastMCP) | `backend/app/mcp/server.py` enregistre 11 outils : generate_job, publish_job, promote_job, score_cvs, rank_candidates, schedule_interview, start_avatar_interview, get_report, trigger_onboarding, create_video, get_subscription | 10 outils de la garde |
| Garde MCP | `backend/app/mcp/guard.py`, fail-closed : tenant et rôle déduits de l'identité du canal, outil ou rôle inconnu refusé, écriture (WRITE/EXTERNAL) sans `confirmed` refusée (`confirmation_requise`), journal d'audit | « Chaque écriture attend une confirmation » |
| Plugin Claude Code | `plugins/rapidoats/` : commandes `/rapidoats-screen`, `/rapidoats-interview`, `/rapidoats-hire`, agent `recruiter` | Non démontré (serveur MCP non joignable) |
| Entretiens | LiveKit (`livekit_service.py`, `livekit_agent.py`, `routers/avatar.py`), avatars GLB dans `public/avatars/`, rapports (`routers/report.py`) | « Codé · en test » |
| Tests | 1 098 fonctions `test_` dans 67 fichiers `backend/tests` (non exécutés ici : services externes requis) | — |

## En développement ou non vérifié

- **Publication Indeed/LinkedIn** (`publish_job`) : code présent, aucune publication testée → non présentée comme opérationnelle.
- **Workflows n8n** : le README en décrit neuf et le CLAUDE.md cite `n8n/workflows/*.json`, mais **le dossier `n8n/` n'existe pas dans le dépôt**. Les workflows ne sont pas vérifiables d'ici (connecteur n8n non activé dans cette conversation).
- **RapidoRH** : `RAPIDORH_MODE=pending` empile les embauches dans `rapidorh_sync_queue`, et rien ne draine cette file → onboarding non automatisé.
- **Migrations 023, 027, 028, 029, 030** marquées « à appliquer » dans le CLAUDE.md du dépôt.
- **Pourcentages par module** (M1–M10) du CLAUDE.md : auto-déclarés, non repris dans la vidéo.
- **Application en ligne** `ats.rapidosoftware.com` : injoignable depuis la session, d'où l'absence de captures réelles.

## Points de sécurité à traiter avant toute démonstration

1. **Régression WhatsApp** : la PR #8 (brouillon, ouverte) indique que le dernier commit du formateur `send_email` a retiré les contrôles de sécurité du webhook WhatsApp sur `main`. Le canal WhatsApp n'est pas montré. → Fusionner la PR #8 après revue.
2. **`promote_job` hors de la garde** : l'outil est exposé par `server.py`, mais absent de `TOOL_KINDS` dans `guard.py`. Par conception fail-closed il est refusé via le pont, mais il faut le classer explicitement (EXTERNAL) ou le retirer du serveur.
3. **Biais du scoring** : la composante LLM (GPT-4o) et le modèle ML entraîné sur des données historiques peuvent reproduire des biais. Le score ne doit jamais trier seul. Aucun rejet automatique n'a été trouvé dans l'interface ; le statut « Refusé » est un choix humain.
4. **Données des candidats** : données personnelles (CV) → RLS Supabase par entreprise et tenant déduit de l'identité. Vérifier les politiques RLS en base avant ouverture (non vérifiable ici).
5. **Webhooks sans secret** : `DOCUSIGN_HMAC_KEY` et `WHATSAPP_VERIFY_TOKEN` vides désactivent la vérification (dev uniquement), et `WHATSAPP_APP_SECRET` est obligatoire en prod. À contrôler dans les variables de production.

## Pull requests au 27/10/2026

| PR | Titre | Statut |
|---|---|---|
| #9 | main | brouillon ouvert |
| #8 | fix(security): restore fail-closed WhatsApp controls | brouillon ouvert, **prioritaire** |
| #4 | Ligne de base des tests | brouillon ouvert |
| #3 | Sécurité P1b/P1c | fermée sans fusion |
| #1, #2, #6, #7 | CI, webhook WhatsApp, domaine/proxy | fusionnées |

Aucune PR n'a été fusionnée ni modifiée par cet audit.

## Protection des personnes dans la vidéo

- CV, candidats A–F, offre et score fictifs ; aucun nom réel.
- Le nom de l'étudiante citée dans le CLAUDE.md du dépôt (PFE) n'apparaît pas.
- Aucune clé ni variable secrète à l'écran.
- Logo RapidoATS : aucun fichier officiel trouvé, donc nom écrit en typographie neutre. **À fournir** pour les prochains épisodes.
