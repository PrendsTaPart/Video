# Vidéo 29 — Audit technique

Lecture seule le 27/10/2026. Rien n'a été publié, modifié ni planifié.

## Vérifié (MCP Site FoodEatUp, `Foodeatup_Site_Admin`)

| Élément | Résultat |
|---|---|
| Piliers (`list_piliers`) | 7 : Food cost & marge, HACCP & traçabilité, Salle & réservations, Équipe & RH, Clients & fidélité, IA & technologie, Comparatifs & alternatives |
| Articles publiés | 3 : « Comment calculer son food cost réel… » (08/09/2026), « Quels plats garder, lesquels retirer : la méthode des quatre familles » (06/10/2026), « Michael fait son cinéma, saison 2… » (30/08/2026) |
| En relecture | 80 (food cost 13, comparatifs 12, HACCP 12, clients 12, salle 11, équipe 10, IA & techno 10) |
| Idées | une centaine (comptage manuel : 100) |
| Brief / rédaction / planifié | 0 / 0 / 0 |
| Outils éditoriaux présents | create_article_idea, update_article_status, check_article_ready, schedule_article, publish_article, get_editorial_calendar, get_publishing_gaps, create_social_derivatives |
| Indicateurs inbound | `get_inbound_stats` renvoie une erreur de validation de schéma (`periode` reçu en objet) : **non lisible**, aucun chiffre de trafic n'est montré |

## Vérifié dans n8n (27/10/2026, lecture seule)

| Workflow | ID | Statut | Nœuds réels |
|---|---|---|---|
| WF08_Veille_Trends_V1 | Y1gbQyDvbFaZER83 | actif · 16 nœuds | webhook → SerpAPI Google Trends + SerpAPI Google News + Reddit (API publique) + contexte RAG Supabase → score → **Gemini 2.5 Flash** → sauvegarde Supabase → callback |
| WF01_Analyse_MotsCles_V1 | 8dYc5TqBZpIM5ybV | actif | description : RAG + Search Console + SerpAPI + Claude + DataForSEO + gaps concurrents |
| WF05_Blog_Content_V1 | r9gPetr11HjtPvYT | actif | callbacks vers Supabase `wf-callback` |
| WF02_SEO_OnPage_V1 | 5KcrOpmWJIVmrUgT | actif | callbacks vers Supabase `wf-callback` |

Autres workflows de la même famille, actifs : WF00 Ingestion RAG, WF03 SEA Ads, WF04 LLM AI Overviews, WF06 Prompts LLM, WF07 Calendar Stats. **Webhooks sans authentification** (ex. `wf08-veille-trends`) : à protéger.

## Non vérifié

- **Exécutions** : aucune exécution conservée pour WF01, WF02, WF05 et WF08. Rien ne prouve qu'ils aient tourné récemment, et aucun résultat n'est montré.
- **Connexion n8n → site FoodEatUp** : **inexistante**. Les résultats vont dans un Supabase séparé (tables `veille_trends`…, callback `wf-callback`), pas dans le pipeline éditorial du site (MCP Site Admin).
- **Glossaire** : présenté comme prochaine étape, pas comme fonctionnalité automatisée.
- **Trafic Google, positions, prospects générés** : aucun chiffre affiché.

## Captures et visuels

- Pas de capture d'écran n8n. Les cartes des workflows reprennent les noms et les nœuds lus dans n8n, avec la mention « Vérifiés dans n8n · actifs · aucune exécution enregistrée ».
- Le site public n'a pas pu être capturé : les URL testées `site.foodeatup.com/blog/…` répondent 404. Les articles sont donc montrés sous forme de cartes construites à partir des données réelles du MCP (titre, date, pilier, mots-clés).
- Logos FoodEatUp et BraindCode : fichiers officiels (`video-20/assets/logos/chartes`).

## À corriger

- Le schéma de sortie de `get_inbound_stats` (champ `periode`).
