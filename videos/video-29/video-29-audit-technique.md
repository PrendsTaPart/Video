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

## Non vérifié

- **Workflows n8n** WF08_Veille_Trends_V1, WF01_Analyse_MotsCles_V1, WF05_Blog_Content_V1, WF02_SEO_OnPage_V1 : le connecteur n8n n'est pas activé dans cette conversation. Les noms et les nœuds viennent du brief et sont signalés à l'écran. Aucun résultat d'exécution n'est montré.
- **Connexion n8n → site** (stockage des résultats SEO, envoi d'articles) : non prouvée.
- **Glossaire** : présenté comme prochaine étape, pas comme fonctionnalité automatisée.
- **Trafic Google, positions, prospects générés** : aucun chiffre affiché.

## Captures et visuels

- Aucune capture n8n réelle (connecteur inactif). Les cartes des workflows sont des reconstitutions signalées.
- Le site public n'a pas pu être capturé : les URL testées `site.foodeatup.com/blog/…` répondent 404. Les articles sont donc montrés sous forme de cartes construites à partir des données réelles du MCP (titre, date, pilier, mots-clés).
- Logos FoodEatUp et BraindCode : fichiers officiels (`video-20/assets/logos/chartes`).

## À corriger

- Le schéma de sortie de `get_inbound_stats` (champ `periode`).
