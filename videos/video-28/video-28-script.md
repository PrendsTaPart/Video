# Vidéo 28 — « J'ai créé mon département de prospection avec des agents IA »

Durée : 73 s · 1080×1920 · voix ElevenLabs Noé (eleven_v4) · sous-titres incrustés · musique + effets sonores de la série.

Ton script est repris avec un seul ajout, vérifié dans RapidoCRM le 27/10/2026 : « Aujourd'hui, mon pipeline compte soixante-dix prospects… et aucune vente signée par ce système. » Les workflows n8n ont été vérifiés le 27/10 : la mention à l'écran est « Vérifiés dans n8n : 5 workflows ProspectAI actifs ».

## Voix off

Avant, pour trouver des clients, il fallait prospecter, rechercher des entreprises, récupérer leurs informations, préparer les e-mails et gérer toutes les relances.
Alors j'ai commencé à créer mes propres scénarios avec n8n.
J'ai développé plusieurs workflows pour la recherche de prospects, l'enrichissement des données, les campagnes et le suivi commercial.
Puis je les ai connectés à mon écosystème RapidoCRM et Prospection.
Aujourd'hui, j'ai même des workflows spécialisés : un pour orchestrer les campagnes, un pour enrichir les prospects, un pour détecter les réponses, un pour les relances et un pour le reporting quotidien.
Et grâce aux MCP, mes agents IA peuvent accéder aux outils de prospection qui leur sont autorisés.
L'objectif, ce n'est plus de faire travailler une personne sur chaque étape.
C'est de construire un département commercial où les automatisations exécutent les processus, les agents IA prennent en charge les tâches adaptées, et RapidoCRM centralise le suivi.
Mais attention : trouver des prospects, ce n'est pas encore signer des clients.
Aujourd'hui, mon pipeline compte soixante-dix prospects… et aucune vente signée par ce système.
C'est exactement ce que je dois mesurer : les réponses, les rendez-vous et les ventes.
Dans la prochaine étape, je veux pouvoir donner un objectif commercial à mon équipe IA, suivre ses résultats et améliorer les scénarios, avec les bonnes validations.
Et toi, tu laisserais une équipe d'agents IA préparer ta prospection ?

## Vérifications

- Vérifié : RapidoCRM `get_stats_pipeline_global` donne 70 prospects (69 « Nouveau Prospect », 1 « Qualification »), 0 gagné, 0 perdu.
- Vérifié : les outils MCP montrés existent (`rechercher_prospects`, `prospecter_entreprise`, `ajouter_prospect_pipeline` dans RapidoCRM ; `prospection_history` dans Prospection).
- **Vérifié dans n8n (27/10)** : les cinq workflows spécialisés existent et sont **actifs** :
  - ProspectAI – Main Orchestrator (I8GtBKUrdnMhKAmp) : aucune exécution conservée ;
  - ProspectAI – Batch Enrichment (oYwHahchXkA9j9Pb) : aucune exécution conservée ;
  - ProspectAI – Reply Detector (XRgZp74UgyEzi2qs) : **42 exécutions, succès** (toutes les 2 h) ;
  - ProspectAI – Follow-up Sequencer (Cig6vkgyuUWtq5Ap) : **6 exécutions, succès** ;
  - ProspectAI – Daily Report (BHdwTEW1mDZkTkOp) : **6 exécutions, succès** (22 h UTC).
- **Également actifs** : « RapidoCRM — Prospection Leades / Envoi mail », « RapidoCRM prospecter prospect », « RapidoCRM prospecter entreprise », « MCP Prospection », « Prospection LinkedIn », « MCP Relais — Communication et CRM ».
- Le taux de réussite des workflows ne dit rien des réponses ni des ventes : le pipeline RapidoCRM compte 0 vente gagnée.
- Aucune prospection, aucun envoi, aucun appel n'a été lancé.
