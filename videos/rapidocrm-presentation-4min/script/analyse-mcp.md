# 🔌 Analyse du MCP RapidoCRM — outils réels (pour cadrer le script)

Source : catalogue d'outils réellement exposés par le serveur MCP RapidoCRM (`crm.rapidosoftware.com/mcp`).
La vidéo doit refléter ces familles réelles, pas une liste inventée. Lower-thirds techniques = noms d'outils ci-dessous.

## 1. Entreprises & contacts
`create_entreprise` · `update_entreprise` · `delete_entreprise` · `get_entreprise` · `list_entreprises` · `search_entreprises` · `rechercher_entreprise_siret` · `create_contact` · `update_contact` · `delete_contact` · `get_contact` · `list_contacts`

## 2. Pipeline & prospection
`ajouter_prospect_pipeline` · `deplacer_prospect_etape` · `enregistrer_prospect` · `enregistrer_tous_prospects` · `get_pipeline` · `get_stats_pipeline` · `get_stats_pipeline_global` · `get_historique_prospect` · `rechercher_prospects` · `prospecter_entreprise` · `prospecter_maps` · `prospecter_prospect` · `close_opportunity`

## 3. Commerciaux & objectifs
`create_commercial` · `delete_commercial` · `get_commercial` · `list_commerciaux` · `set_commercial_status` · `update_commercial_objectifs` · `update_commercial_profil` · `get_user_performance` · `create_user` · `get_user` · `list_users`

## 4. Campagnes (SMS / email / newsletter / sondage / jeu)
`create_campagne` · `lancer_campagne` · `list_campagnes` · `get_stats_campagne` · `send_sms` · `schedule_sms` · `send_email` · `schedule_email` · `send_newsletter` · `list_newsletters` · `lancer_sondage_entreprise` · `lancer_jeu_concours_entreprise`

## 5. Templates, CTA & segments
`create_template_email` · `create_template_sms` · `list_templates_email` · `list_templates_sms` · `delete_template_email` · `delete_template_sms` · `get_template` · `create_editor_template` · `list_editor_templates` · `delete_editor_template` · `list_cta` · `create_segment` · `recalculer_segment` · `get_contacts_segment` · `list_segments`

## 6. Devis, factures & contrats
`create_devis` · `list_devis` · `create_facture` · `get_facture` · `list_factures` · `create_contrat` · `get_contrat` · `list_contrats` · `update_contrat_status` · `delete_contrat` · `create_contrat_template` · `list_contrat_templates` · `update_contrat_template` · `delete_contrat_template`

## 7. Catalogue produits
`create_product` · `update_product` · `delete_product` · `get_product` · `list_products`

## 8. Agenda, RDV & tâches
`create_rdv` · `list_rdvs` · `create_evenement` · `list_evenements` · `get_today_schedule` · `create_task` · `log_activity` · `get_interaction_stats`

## 9. Finance & pilotage
`create_depense` · `list_depenses` · `get_revenue_summary` · `get_dashboard_kpis` · `get_dashboard_general_stats` · `get_top_clients` · `get_conversion_par_canal` · `get_loyalty_points`

## 10. Formulaires, sondages & jeux
`list_formulaires` · `get_formulaire_soumissions` · `list_sondages` · `get_sondage_resultats` · `list_jeux_concours`

---

## Correspondance script ↔ outils (crédibilité technique des lower-thirds)
| Plan | Écran | Outils MCP réels (lower-third) |
|------|-------|--------------------------------|
| Connexions | IMAP / Stripe / SMS | *(config compte)* |
| MCP + astuce 1 | chat Claude | `list_commerciaux` · `list_entreprises` · `list_templates_email` |
| Équipe + astuce 2 | commerciaux/objectifs | `create_commercial` · `update_commercial_objectifs` |
| Campagne SMS | tunnel 3 étapes | `create_campagne` · `lancer_campagne` · `schedule_sms` |
| Devis/factures/contrats + astuce 3 | documents | `create_facture` · `create_contrat` · `create_devis` |
| Quotidien | agenda/RDV/mail | `create_rdv` · `get_today_schedule` |
| Hook de fin | écosystème | *(RapidoCMS + RapidoRH — les 2 autres oiseaux)* |

## Mapping des 19 écrans fournis (sur 39 attendus)
| Fichier | Écran |
|---------|-------|
| crm-01 | Créer un compte — gérant |
| crm-02 | Créer un compte — entreprise (SIRET) |
| crm-03 | Profil |
| crm-04 | Connexion boîte mail (IMAP) |
| crm-05 | Connexion Stripe |
| crm-06 | Connexion SMS (Twilio) |
| crm-07 | Logo Claude (chapitre MCP) |
| crm-08 | Liste commerciaux (cards statut) |
| crm-09 | Ajouter un commercial |
| crm-10 | Objectifs commerciaux |
| crm-11 / 12 / 13 | CTA (liste / modal / créer) |
| crm-14 / 15 / 16 | Formulaires (liste / créer / source) |
| crm-17 | Catalogue produits |
| crm-18 | Ajouter un produit (prix HT, TVA) |
| crm-19 | **Campagne SMS — étape 1 ciblage** |

### Complément (2e lot — set désormais quasi complet, 36 écrans)
| Fichier | Écran |
|---------|-------|
| crm-20 | Boîte mail (25 mails · Non attribués · Spam · Corbeille) |
| crm-21 / 22 | Agenda mois (RDV colorés) / + programme |
| crm-23 | Prise de RDV (Visio/Physique/Tél + rappel SMS-Email + dispo commerciaux) |
| crm-24 / 25 / 26 / 27 | Contrat (ajouter titre / éditeur articles / ajouter sous-titre ×2) |
| crm-28 | **Créer un devis — Design (choix de charte graphique, sélecteur couleurs)** |
| crm-29 | Ajouter un contrat (dates + template mail + envoi) |
| crm-30 | **Campagne SMS — étape 2 (texte du SMS)** |
| crm-31 | **Campagne SMS — étape 3 (validation + aperçu téléphone)** |
| crm-32 | Campagne SMS — étape 1 ciblage (variante) |
| crm-33 | **Campagne SMS — choisir un modèle** (Fête des mères, Nouveau produit…) |
| crm-34 | Logo RapidoSoftware (3 oiseaux) |
| crm-35 | Key visual RapidoCRM (BraindCode, mockup) |
| crm-36 | **Logo RapidoCRM (3 oiseaux + wordmark vert)** |

→ Le **tunnel campagne SMS complet** est couvert en statique (crm-19/32 → 33 → 30 → 31). Le **logo 3 oiseaux** est disponible (PNG raster).

### État des gates ÉTAPE 0
- ✅ Écrans : 36/39 (il manque surtout : liste factures dédiée, profil admin détaillé, un 2e écran objectifs). Suffisant pour le storyboard.
- ✅ Logo 3 oiseaux : **PNG raster** (crm-36). ⚠️ Pas de vectoriel `.ai/.svg` → sting animable en approximation (3 formes colorées + logo), pas en motion vectoriel pur.
- ❌ **Screen recordings vidéo (SR-CRM-01..04) : ABSENTS.** Le tunnel SMS (SR-CRM-02) est couvrable par une **séquence animée des 4 écrans réels** (équivalent « Option B »).
- ✅ Typo : Liberation Sans = substitut métrique-compatible d'Arial.
- ⚠️ Avatar HeyGen (Mika parlant) : indisponible en CLI → boucle Mika en médaillon.
- ⚠️ FLOW-01 (hook) / FLOW-04 (outro) : Google Flow/Veo indisponible → substitut `generate_image` (photo statique + Ken Burns).
