# Ahmed.md — Tâches manuelles pour terminer le projet Rapido (mis à jour le 15/11/2026)

Tâches qu'un humain doit faire (accès, comptes, argent, serveurs, validation). Les tâches des agents IA sont dans
`AGENT.md` de chaque dépôt (rapido-crm, rapido-software, video/tutoriels-rapido).

## 1. Mise en production RapidoCRM (crm.rapidosoftware.com)
- [ ] Sauvegarde complète de la base MySQL avant déploiement.
- [ ] Déployer la branche `production` (deploy.yml est désactivé : déploiement manuel), puis `php artisan migrate --force`
      (migrations 2026_11_16_* : sites, bibliothèque, lead magnets, commandes, cartes digitales, fidélité v2, modèles de l'éditeur,
      connexions MCP, formulaires de devis), `php artisan optimize:clear`.
- [ ] Crontab : `* * * * * php artisan schedule:run` (relances 9 h 15, contrats 9 h 05, fidélité 8 h 20, séquences et e-mails reçus
      toutes les 15 min, score le lundi 6 h 40…).
- [ ] Un worker de file d'attente permanent : `php artisan queue:work --tries=3` (supervisor) — nécessaire pour les tâches envoyées à RapidoRH.
- [ ] Variables d'environnement : `SITES_CIBLE_CNAME`, `SITES_IP`, `SITES_HOTES_APPLICATION`, `SITES_EMAIL_SPF_INCLUDE`, `MCP_HUB_URL` ;
      optionnel : `DOMAIN_CONNECT_PROVIDER_ID`, `ENTRI_APPLICATION_ID`, `ENTRI_SECRET`. Serveur web Caddy avec `on_demand_tls`
      (voir `config/sites.php`) pour les domaines personnels des clients.
- [ ] Twilio : déclarer l'URL `POST /api/sms/entrant/{company}` pour les STOP/START. Stripe : chaque société saisit sa clé.
- [ ] Renvoyer les devis envoyés avant le déploiement des liens signés (les anciens liens répondent 403).
- [ ] Réactiver la CI (`deploy.yml`) et conditionner `automerge.yml` aux tests verts (aujourd'hui : fusion sans tests).

## 2. RapidoRH et RapidoCMS reliés à RapidoCRM
- [ ] Dans RapidoRH : autoriser le domaine de retour de RapidoCRM dans `config/mcp.php` → `redirect_domains`
      (adresse affichée en bas de l'écran RapidoCRM › Connexions), puis déployer RapidoRH.
- [ ] Dans RapidoCRM › Connexions : connecter RapidoRH (`https://rh.rapidosoftware.com/mcp/rapidorh`) et RapidoCMS, créer les règles
      (projet, liste de tâches, agents IA / employés assignés), cliquer « test ».

## 3. Site RapidoSoftware
- [ ] Corriger le secret GitHub `EC2_HOST` (déploiement EC2 bloqué), puis déployer `production`.
- [ ] Relire et valider les pages Agents IA, Académie et les nouvelles pages solutions.

## 4. Vidéos tutoriels et formations
- [ ] Reconnecter le connecteur ElevenLabs (il demande de nouvelles autorisations) et valider le budget de crédits
      (~900 à 1 300 crédits par épisode ; 20 épisodes CRM50–CRM69 + 4 formations F40–F43 restent à produire).
- [ ] Valider la voix « Adam — Instructor » sur un épisode pilote.
- [ ] Publier sur les vrais réseaux sociaux / YouTube (les agents n'ont pas le droit de publier sur des comptes réels).

## 5. Téléphonie VoIP (plan : rapido-crm/docs/PLAN_VOIP_2026-11-15.md)
- [ ] Compte Twilio principal (sous-comptes par client), et compte Telnyx pour les appels vers mobiles (phase 2) ; moyens de paiement et plafonds de dépense.
- [ ] Dossier réglementaire des numéros français (pièce d'identité, justificatif d'adresse, Kbis) ; demandes de portage des numéros existants des clients.
- [ ] Clé de transcription (Deepgram ou Amazon Transcribe) et budget LLM ; instance AWS pour le service média temps réel, bucket S3 chiffré pour les enregistrements.
- [ ] Valider les tarifs des packs Téléphonie Essentiel / IA et la mention d'information sur l'enregistrement (relecture juridique RGPD / CNIL).

## 6. Matériel et options
- [ ] Commander des puces NFC NTAG213/215 (cartes, autocollants, présentoir) et imprimer les designs (RapidoCRM › Puces NFC › imprimante).
- [ ] Apple Wallet / Google Wallet (option) : créer les certificats émetteur (Apple Developer, Google Pay & Wallet Console).
- [ ] Relecture juridique : mentions RGPD des formulaires publics (cartes, fidélité, devis), règlement du programme de fidélité, CGV.
