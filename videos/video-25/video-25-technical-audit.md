# Vidéo 25 · Audit technique RapidoTuto (27/10/2026)

## Sources

- Dépôt `PrendsTaPart/rapidotuto-base`, branche principale, commit `6c869f7` (25/10, fusion de la PR #6).
- PR #1 à #6 : **toutes fusionnées** (24 et 25/10). #1 assistant IA, centre d'aide, statistiques, sécurité, MCP · #2 site vitrine, tunnel de vente, vidéo de présentation, fonds d'avatar, présentations commentées · #3 présentation en direct, forfaits, emails, exports CSV · #4 emails · #5 correction du crash serveur (500) · #6 correction des liens partagés `/watch`, `/live`, `/centre`, `/embed`.
- Projet Lovable `ba54c9e6-…` · application publique https://rapidotuto-base.lovable.app.
- Base de données Lovable, **lecture seule** (comptages et un projet de démonstration ; aucune donnée personnelle lue).

## Fonctionnalités : code / application / données

| Fonctionnalité | Code | Vérifié en ligne | Données réelles |
|---|---|---|---|
| Projets, storyboard en scènes | oui (`generate-storyboard`) | site vitrine + captures | 9 projets, 13 scènes |
| Enregistrement découpé par scène | oui | capture officielle | — |
| Import PDF / PPTX / images, scripts IA des diapositives | oui (`generate-slide-scripts`) | non testé | — |
| Voix | oui (`/api/elevenlabs-tts`) | non testé | 6 scènes avec voix |
| Avatar 3D | oui | rendu officiel `video/assets/avatar.png` | — |
| Export vidéo, forfaits (gratuit : 3 vidéos/mois, 5 min) | oui (`user_plans`) | grille tarifaire du site | — |
| `/watch/:token`, `/live/:token`, `/centre/:token`, `/embed/:token` | oui | pages d'erreur propres avec un jeton invalide (« lien invalide ou partage désactivé ») | **0** projet partagé, **0** centre d'aide |
| Assistant `/api/public/ask` | oui : Lovable AI Gateway, modèle `google/gemini-3-flash-preview`, réponse à partir des scripts ; refus si aucun script exploitable | non testé (pas de lien partagé) | **0** question |
| Questions sans réponse | oui (`assistant_questions`) | capture officielle | 0 |
| Demandes de support, « parler à un humain » | oui (`support_requests`) | non testé | 0 |
| Statistiques de visionnage | oui (`video_views`) | capture officielle | 0 vue |
| Tunnel commercial, demandes de démo | oui (`marketing_leads`, `funnel_events`) | formulaire « Demander une démo » sur le site | 0 lead, 16 événements de tunnel |
| Transfert vers RapidoCRM | **non** : aucune intégration RapidoCRM dans le code (le nom n'apparaît que dans des modèles de prompts) | — | — |
| Emails | oui (catalogue à la charte) | non envoyé | la roadmap indique que la réception en boîte n'est pas encore vérifiée |

## MCP RapidoTuto (`/mcp`, `rapidotuto-mcp` 0.1.0)

Authentification OAuth (Supabase) : chaque appel passe par le jeton de l'utilisateur, la sécurité au niveau des lignes s'applique, et chacun ne voit que ses données.

| Outil | Nature |
|---|---|
| `list_projects`, `get_project`, `list_brand_kits` | lecture |
| `create_project` | écriture (crée un brouillon) |
| `list_support_requests` | lecture |
| `update_support_request` | écriture (statut done / open) |
| `list_unanswered_questions` | lecture (30 derniers jours, regroupées par fréquence) |
| `get_tutorial_stats` | lecture |

Le MCP n'est pas branché à cette session de Claude Code : aucun outil n'a été appelé. L'analyse vient du code.

## Ce qui n'a pas pu être démontré

- Le mode `/live`, la réponse de l'assistant, la pause et la reprise : il n'y a aucun lien de partage, et en créer un serait une écriture en production.
- La génération de voix et de script dans l'app : elle demande une connexion et la création d'un projet.

## Assets

- Logos (`assets/logos/`) : l'icône RapidoTuto (`public/icon-512.png` du dépôt) et les chartes FoodEatUp, RapidoSoftware et BraindCode (MCP FoodEatUp Formation, `get_brand_guidelines`). **RapidoTuto n'a pas de logo dans la charte Formation** : seule l'icône du dépôt est utilisée, et le mot-symbole est composé en texte selon le README (« Rapido » gris, « Tuto » bleu).
- Captures et film : `public/media/screens/*.webp` et `public/media/rapidotuto-presentation.mp4` du dépôt, plus les captures du site public dans `assets/captures/`.
