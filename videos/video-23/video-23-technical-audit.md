# Vidéo 23 · Audit technique RapidoMeet (27/10/2026)

## Sources

- `braindcode1/Rapidomeet`, branche `main`, commit `494aa22` (01/09/2026, « refresh the developer hand-off — 83 %, 85 tests »). Le dépôt contient à la fois le frontend React/Vite **et** le serveur Express (`src/index.ts`, `src/transcribe.ts`, `src/extract.ts`, `src/router.ts`, `src/mcp-server/`), plus `services/whisper-engine` (Python) et `services/Twilio-ingestor`. Aucun dépôt `openclaw-server` séparé n'a été consulté.
- PR, au 27/10 : **#1, #3 et #4 ouvertes en brouillon, non fusionnées** ; #2 « Rapido meet system » fusionnée le 30/07.
- Docs du dépôt : `ARCHITECTURE.md`, `docs/RESTE-A-FAIRE-*.md`, `docs/MCP.md`.
- Application : `app.rapidomeet.io` ne répond pas (aucun déploiement accessible). Les images de la vidéo sont les visuels du site (`src/assets/screenshots/*.png`), avec des données fictives (« Client TechCorp »).

## Capacités

| Capacité | État |
|---|---|
| Authentification Supabase, workspaces | opérationnelle dans le code (bloc Authentification 100 % selon la doc) |
| Connexion Google Calendar (OAuth), agenda | partielle (Agenda 53 % ; événements créés via OpenClaw) |
| Préparation de l'ordre du jour, contexte métier (RAG) | **prévue** : « aucun embedding aujourd'hui, l'UI laisse croire le contraire » |
| Enregistrement audio (vumètre), import de fichier | implémenté |
| Transcription | implémentée, **deux chaînes concurrentes** : Express (Groq Whisper large-v3, découpage, repli faster-whisper local) et edge function Gemini (plafond de 8 000 tokens). La doc demande de trancher. Transcription live : 58 % |
| Résumé, décisions, tâches (responsable, échéance, citation source), prospects | implémenté : Gemini 2.0 Flash, sortie validée par des schémas Zod |
| Tableau des tâches (Kanban), actions groupées | implémenté (Tâches 85 %) |
| Validation humaine | implémentée : les écritures CRM et CMS passent en `awaiting_confirmation`, et l'utilisateur confirme ou refuse |
| RapidoCRM | outils mappés : contact, entreprise, opportunité, modèles, journal d'activité. L'audit PR #3 note **12 outils CRM sur 38 non mappés** |
| RapidoCMS | outils `cms_*` (création, planification) avec validation |
| RapidoRH | **lecture seule** (`rh_list_*`, `rh_get_*`) ; aucune création de tâche |
| Telegram (confirmations), client OpenClaw, expiration des actions | **à moitié livrés** (P4 de l'audit) |
| Envoi du rapport par email et WhatsApp (MCP) | outils présents sur `main` ; ils passent par des edge functions Supabase **absentes du dépôt** (`supabase/functions` vide) : non vérifiable |
| Serveur MCP (11 outils : `list_meetings`, `get_meeting`, `get_transcript`, `list_tasks`, `update_task`, `create_report`, `transcribe_meeting`, `get_report`, `share_report`, `send_report_email`, `send_report_whatsapp`) | implémenté ; « boucle MCP jamais exécutée contre un vrai Supabase » |
| Tests | 85 tests contre un Supabase **simulé** |

## Sécurité (à traiter avant toute démonstration réelle)

- **Identifiants Twilio réels présents sur `main`** dans `services/Twilio-ingestor/.env.example` (signalé par la PR #3, toujours présent). → **À révoquer et faire tourner chez Twilio**, puis à retirer de l'historique. La valeur n'est reproduite nulle part dans ces livrables.
- `main` accepte encore un décodage de jeton non vérifié (mode dev) et `BYPASS_AUTH` : la PR #4 l'interdit en staging et en production. Elle n'est pas fusionnée.
- La PR #4 apporte aussi :
  - un serveur MCP par utilisateur et des contrôles de propriété ;
  - le retrait des faux outils d'envoi ;
  - un 404 sur les sondes entre tenants.

  Elle est en brouillon et en conflit avec `main` (`dirty`).
- Selon l'audit, la clé de chiffrement AES est dérivée d'une constante publique.

## Ce qui n'a pas pu être démontré

- Aucune réunion réelle n'a été traitée ; aucun appel aux API Groq ou Gemini n'a été fait.
- Aucune synchronisation RapidoCRM, RapidoCMS ou RapidoRH, aucun Telegram, aucun Google Calendar.
- Aucune PR fusionnée, rien de déployé.

## Assets

- Icône RapidoMeet : `public/pwa/icons/icon-512.png` du dépôt. **Elle est absente de la charte FoodEatUp Formation.**
- Logos RapidoCRM, RapidoCMS, RapidoRH, FoodEatUp et BraindCode : chartes Formation (`video-20/assets/logos`).
