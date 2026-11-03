# Vidéo 30 — Vérification des capacités réelles

Lecture seule le 27/10/2026, par le MCP RapidoCRM connecté à cette session. Aucun prospect créé, aucun appel, aucun e-mail ni SMS, aucune campagne, aucun workflow lancé. Le prompt de démonstration est affiché, mais pas exécuté.

## Observé en fonctionnement réel

| Étape | Source | Résultat |
|---|---|---|
| Segments | `list_segments` | 8 segments : Restauration rapide, Bar / brasserie, Traiteur, Chaînes et franchises, Restauration traditionnelle, Boulangerie-pâtisserie, Clients FoodEatUp, « 67uu » (vraisemblablement un test, non montré) |
| Pipeline | `get_stats_pipeline_global` | 70 prospects : 69 « Nouveau Prospect », 1 « Qualification », 0 gagné, 0 perdu, montant 0 € |
| Interactions (année) | `get_interaction_stats` | 8 : 3 RDV, 2 SMS, 1 e-mail, 1 newsletter, 1 appel |
| Agent vocal | `get_agent_vocal_config` | Actif, objectif « demo », ton « chaleureux », pitch FoodEatUp et catalogue configurés. **`twilio_connecte: false`, `pret_a_appeler: false`** (« Aucun numéro Twilio connecté »). Compteurs : 32 appels, 30,91 min consommées, 89,09 min restantes. |
| Workflows RapidoCRM | `list_workflows` | 17 (dont 1 [TEST-QA] exclu) : 3 actifs (Onboarding J0/J7/J14, Relance facture J+7, Relance devis J+3), les autres en brouillon, dont « Prospection complète avec agent IA » et « Prospection restaurants + agent vocal ». **0 exécution enregistrée.** |
| Outils MCP | catalogue du serveur | Présents : prospecter_prospect, prospecter_entreprise, prospecter_maps, rechercher_prospects, enregistrer_prospect, list_entreprises, list_contacts, list_segments, get_contacts_segment, ajouter_prospect_pipeline, deplacer_prospect_etape, get_historique_prospect, create_rdv, list_rdvs, create_devis, list_devis, send_email, send_sms, create_task, create_campagne, get_stats_pipeline, appeler_entreprise_vocal, prospecter_et_appeler_vocal |

## Pas observé : intégrations à finaliser

- **Appel téléphonique de bout en bout** : impossible aujourd'hui, Twilio n'est pas connecté. Les 32 appels du compteur n'ont pas été tracés dans cet audit (ni transcription, ni résultat, ni date). Ils ne sont donc ni montrés ni décrits comme des appels réels. La vidéo garde la formulation de projet.
- **« Caroline — Simulateur vocal »** : c'est un simulateur, pas un appel. Il n'est pas montré comme un appel.
- **Workflows n8n** (« RapidoCRM — Prospection Leades / Envoi mail », « MCP Prospection », « MCP Relais », « Prospection LinkedIn »…) : **non vérifiés**. Le connecteur n8n existe sur le compte, mais il n'est pas activé dans cette conversation. Il faut l'activer dans les réglages des connecteurs claude.ai pour l'audit.
- **Création de RDV / devis par l'agent** : outils présents, non exécutés (écritures en production). Captures réelles des écrans Agenda et Créer un devis issues du dépôt `rapidocrm-presentation-4min`.
- **Qualification automatique** : 1 seul prospect en « Qualification » sur 70, sans trace de l'auteur (humain ou agent).

## Conformité

- Prospect affiché fictif (« Le Comptoir »), coordonnées masquées ; aucun contact réel affiché.
- Avant tout appel réel : annonce de l'IA en début d'appel, opposition (Bloctel pour les particuliers), information RGPD et consentement à l'enregistrement.
- Envois, RDV, devis et campagnes : validation humaine avant exécution.
