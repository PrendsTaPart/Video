# Tutoriels & formations Rapido — plan de production

> Fichier de pilotage lu **à chaque exécution de la routine** (toutes les 5 h :
> 1 h 40, 6 h 40, 11 h 40, 16 h 40, 21 h 40, heure de Paris).
> Chaque exécution prend les **3 premiers éléments non cochés** (`- [ ]`), les produit,
> les coche (`- [x]`), complète le **journal** en bas, puis pousse sur la branche
> `tutoriels-rapido`.

## Règles impératives

1. **Ne jamais modifier le code** de `rapido-crm`, `rapido-cms`, `rapido-RH`.
   Ces dépôts servent **uniquement** à lancer les applications en local (données de
   démonstration fictives) pour filmer les écrans. Aucun commit, aucun push dessus.
2. **Higgsfield** : ne jamais générer de nouvelle vidéo (règle du `CLAUDE.md` du dépôt).
3. **Ne rien publier** sur des comptes réels (réseaux sociaux, RapidoCMS de production,
   YouTube…) sans l'accord explicite de Michael. Ne pas utiliser les MCP RapidoCRM /
   RapidoCMS / RapidoRH de production pour écrire des données.
4. **Données fictives uniquement** à l'écran (aucune donnée client réelle, aucun email réel).
5. **Disque limité** : cloner ce dépôt en mode partiel/sparse, sans `videos/` (voir
   « Mise en route »). Supprimer les rendus intermédiaires après commit.
6. Si un élément est bloqué (application qui ne démarre pas, crédit épuisé…), le marquer
   `- [!]` avec la raison dans le journal et passer au suivant.

## Mise en route d'une exécution

```bash
# Dépôt vidéo, sans les 6 Go de rendus historiques
git clone --depth 1 --filter=blob:none --no-checkout -b tutoriels-rapido https://github.com/PrendsTaPart/video /home/user/video
git -C /home/user/video sparse-checkout set --no-cone '/*' '!/videos/' '/videos/tutoriels-rapido/'
git -C /home/user/video checkout tutoriels-rapido
# Application à filmer (lecture seule)
git clone --depth 1 https://github.com/PrendsTaPart/rapido-crm /home/user/rapido-crm   # ou rapido-cms / rapido-RH
```

Lancement local d'une application Laravel 11 + Vue (pour filmer) :
`composer install`, `.env` en SQLite, `php artisan key:generate`, `php artisan migrate --seed`,
création d'un compte de démonstration + données fictives (via tinker/seeders locaux, **sans
modifier les fichiers suivis par git**), `npm ci && npm run build`, `php artisan serve`.

## Chaîne de production d'un tutoriel

1. **Repérage** : lire les vues/routes/contrôleurs de l'écran concerné ; lister chaque
   champ, bouton, onglet et action. Rédiger `tutoriels-rapido/<ID>/script.md`
   (accroche 5 s → objectif → étapes écran par écran → astuce → appel à l'action).
2. **Captures** : Playwright (Chromium préinstallé) filme chaque écran
   (`recordVideo`, 1920×1080) en suivant le script (clics, saisie, survols) + captures PNG.
3. **Voix** : ElevenLabs (connecteur) — voix française unique pour toute la série
   (noter son `voice_id` ci-dessous dès la 1re exécution). Fichier `voix.mp3`.
4. **Montage** : composition HyperFrames (HTML + GSAP) dans `tutoriels-rapido/<ID>/` :
   enregistrements d'écran + zooms, surlignages, curseur animé, encarts, sous-titres
   (règles de sous-titres du `studio-video/CLAUDE.md`), intro/outro aux couleurs du Rapido
   (CRM `#4CAF50`, CMS `#03A9F5`, RH `#7E57C2`). Rendu 16:9 1920×1080 ;
   version 9:16 pour les formations courtes si pertinent.
5. **Miniature** (sans Lovable ni service externe) : gabarit local
   `tutoriels-rapido/_gabarit/miniature.html` rendu en PNG 1280×720 par
   `node tutoriels-rapido/_gabarit/miniature.cjs --product crm --num CRM02 --title "…" --em "…" --tag "…" --shot capture.png --out tutoriels-rapido/<ID>/miniature.png`
   (`--shot` = une vraie capture de l'écran filmé).
6. **Dépôt** : `videos/tutoriels-rapido/<ID>.mp4`, `tutoriels-rapido/<ID>/miniature.png`,
   script, sous-titres `.srt`. Commit + push sur `tutoriels-rapido`.

## Références à remplir au fil des exécutions

- Voix ElevenLabs : `voice_id = TGAegA0zNRi8I6nUdq3i` (« Adam — Instructor », modèle `eleven_v4`) — en attente de validation par Michael sur la vidéo pilote CRM02
- Miniatures : gabarit local `tutoriels-rapido/_gabarit/` (Lovable retiré à la demande de Michael)
- Étude de la concurrence : `tutoriels-rapido/CONCURRENCE.md`

---

## 0. Préparation (à faire en premier)

- [x] P1 — Étude de la concurrence (HubSpot Academy, Pipedrive, Zoho, Salesforce Trailhead, Hootsuite, Buffer, Agorapulse, Lucca, PayFit, Monday, Asana, Notion) : formats, durées, structure, miniatures → `CONCURRENCE.md`
- [x] P2 — Charte des tutoriels (intro/outro, habillage, typographies, sous-titres) + gabarit HyperFrames réutilisable `tutoriels-rapido/_gabarit/`
- [x] P3 — Validation de la voix ElevenLabs et du gabarit de miniature sur la vidéo pilote CRM02
- [x] P4 — Recette de lancement local de chaque application (CRM, CMS, RH) avec données fictives, documentée dans `tutoriels-rapido/LANCEMENT.md`

## ⚠️ Blocage RapidoCRM (13/11/2026)

Le dépôt `rapido-crm` (branche par défaut, merge de la PR #97 du 07/09/2026) contient des **marqueurs de conflit git
non résolus** : 98 fichiers du build `public/build/assets` (dont le chunk partagé `vue-vendor-D2P1ka8e.js`) et
3 sources (`resources/views/admin/layouts/admin.blade.php`, `resources/views/admin/tutoriels/templates/editeur_pdf.blade.php`,
`resources/js/components/CalendarComponent.vue`). Conséquence : **aucun composant Vue de RapidoCRM ne se charge**
(Clients, prospection, pipeline, campagnes…). Les écrans en Blade pur (inscription, tableau de bord, profil) fonctionnent.
**Décision de Michael (13/11/2026) : recompiler en local pour filmer, sans toucher au dépôt.** Fait :
- copie de travail **hors dépôt** `/home/user/rapido-crm-film` (sans `.git`, aucun commit/push possible) ;
- dans cette copie seulement : marqueurs de conflit résolus en gardant la version la plus récente, et
  `EntrepriseProfil.vue` (tronqué : la section « Entreprise » de l'accordéon enchaîne sur la fin d'un formulaire de
  facture, déjà le cas avant la fusion) refermé pour compiler — cette section reste vide à l'écran ;
- `npm run build` dans la copie, servie sur le port 8124 (voir LANCEMENT.md). Le dépôt `rapido-crm` reste intact.
→ **CRM04 à CRM43 débloqués.** À signaler à l'équipe : le dépôt garde ses marqueurs et `EntrepriseProfil.vue` tronqué.

## A. RapidoCRM — un tutoriel par onglet / écran

- [x] CRM01 — Créer son compte et choisir son forfait
- [x] CRM02 — Visite guidée du tableau de bord
- [x] CRM03 — Compléter son profil et sa configuration
- [x] CRM04 — Prospecter sur Google Maps
- [x] CRM05 — Rechercher une entreprise par SIRET
- [x] CRM06 — La fiche entreprise et la fiche contact (pas d'écran « notes » dans l'interface : les notes passent par le MCP)
- [x] CRM07 — Le pipeline : étapes, déplacement, clôture
- [x] CRM08 — L'agent vocal IA : configuration, appels entrants, catalogue
- [x] CRM09 — Historique des appels
- [x] CRM10 — Contacts et entreprises
- [x] CRM11 — Catalogue produits et offres
- [x] CRM12 — Créer et envoyer un devis
- [x] CRM13 — Factures et suivi des paiements
- [x] CRM14 — Dépenses
- [x] CRM15 — Contrats et signature électronique
- [x] CRM16 — Modèles de contrats
- [x] CRM17 — Campagnes email
- [x] CRM18 — Campagnes SMS et aperçu
- [x] CRM19 — Newsletters
- [x] CRM20 — Campagnes automatiques
- [x] CRM21 — Segments
- [x] CRM22 — Modèles d'emails et de SMS (éditeur)
- [x] CRM23 — Workflows : créer, activer, suivre
- [x] CRM24 — Formulaires (refait le 15/11 : lien public)
- [x] CRM25 — CTA et pages
- [x] CRM26 — Programme de fidélité et cartes NFC
- [x] CRM27 — Jeux concours
- [x] CRM28 — Sondages
- [x] CRM29 — Avis clients
- [x] CRM30 — Cartes de visite digitales
- [!] CRM31 — Salons et leads de salon (16/11 : aucun écran « Salons » dans RapidoCRM, seulement les outils MCP create_salon, enregistrer_lead_salon, remercier_leads_salon, get_salon_stats → décision de Michael : formation motion design « salons avec Claude » ou abandon ; voir Ahmed.md)
- [x] CRM32 — Événements
- [x] CRM33 — Agenda et rendez-vous
- [x] CRM34 — Visioconférence et stratégie à l’écran (publié)
- [x] CRM35 — Tâches
- [x] CRM36 — Équipe commerciale et objectifs
- [x] CRM37 — Stratégies commerciales des produits (publié)
- [x] CRM38 — Historique de tous les échanges (publié)
- [x] CRM39 — Documents clients et bibliothèque (publié)
- [x] CRM40 — Bibliothèque de prompts (publié)
- [x] CRM41 — Notifications (publié)
- [x] CRM42 — Facturation de l'abonnement et packs (sélecteurs corrigés le 16/11, voix 830 cr. — en file)
- [x] CRM43 — Connecter RapidoCRM à Claude (MCP)
- [x] CRM44 — Les relances automatiques (devis et factures) + suivi d'ouverture des devis
- [x] CRM45 — Le prévisionnel pondéré et les affaires à relancer (pipeline)
- [x] CRM46 — Personnaliser le design d'un formulaire
- [x] CRM47 — Intégrer un formulaire à son site (iframe) et suivre les réponses
- [x] CRM48 — Les CTA : pop-up, bannière et encart sur votre site (publié)
- [x] CRM49 — Statistiques des CTA et test A/B (publié)

### Nouveaux modules (séance du 15/11, 16 h 50) — ordre de production
- [x] CRM50 — Sites et pages : publication, SEO, sitemap
- [x] CRM51 — Connecter son nom de domaine
- [x] CRM52 — Le sous-domaine d'envoi des e-mails (SPF, DKIM, DMARC)
- [ ] CRM53 — L'éditeur : sections et modèles gratuits
- [ ] CRM54 — L'éditeur sur téléphone
- [ ] CRM55 — Les ventes en ligne : bouton d'achat et paiement (Stripe en mode test, aucun paiement réel)
- [x] CRM56 — Les lead magnets (scénario, `leadmagnets-demo.php`, essai à blanc, voix 880 cr. — en file)
- [x] CRM57 — Le tunnel de vente créé par Claude (outil creer_tunnel_de_vente) (scénario, `tunnel-demo.php`, essai à blanc, voix 847 cr. — en file)
- [x] CRM58 — Bibliothèque : partage suivi et statistiques de téléchargement (scénario, `bibliotheque-demo.php`, essai à blanc, voix 995 cr. — en file)
- [x] CRM59 — Connecter son IA (Claude, ChatGPT, Le Chat, Grok) (voix 882 cr. — en file)
- [x] CRM60 — Les 100 agents IA (voix 720 cr. — en file)
- [x] CRM61 — Un prompt par outil MCP (voix 662 cr. — en file)
- [x] CRM62 — Fusionner les doublons (scénario, démo `doublons-demo.php`, essai à blanc, voix 905 cr. — en file de tournage)
- [x] CRM63 — Les séquences de prospection (scénario, démo `sequences-demo.php`, essai à blanc, voix 894 cr. — en file)
- [x] CRM64 — Le score des prospects (scénario, démo `score-demo.php`, essai à blanc, voix 738 cr. — en file)
- [x] CRM65 — La carte de visite digitale en 1 clic (boucle marketing)
- [x] CRM66 — Les puces NFC
- [x] CRM67 — Le programme de fidélité et la caisse
- [x] CRM68 — Le formulaire de devis en ligne
- [x] CRM69 — Connecter RapidoRH : l'équipe IA au travail
- [x] CRM70 — Appeler vos clients en un clic (téléphonie : clic pour appeler, journal, rappel, « Qui m'appelle ? »)
- [~] CRM71 — Appeler un client depuis sa fiche et le prompteur temps réel (17/11 : l'appel depuis la fiche est montré dans CRM70 ; le prompteur temps réel n'existe pas encore dans RapidoCRM)
- [x] CRM72 — (couvert par CRM86, publié le 17/11) Analyse des appels, enregistrement et tâches envoyées à l'équipe IA
- [x] CRM73 — L'agent IA sur votre site web (18/11 : voix 995 crédits, 2e prise, publié RapidoCMS + Académie ; réindexation horaire et source citée une fois ajoutées)
- [x] CRM74 — Boîte de réception et tickets (18/11 : voix 988 crédits, 2e prise, publié RapidoCMS + Académie ; retard des tickets visible sans attendre la commande planifiée)
- [x] CRM75 — Dessiner sa stratégie avec la Marketing Map
- [x] CRM76 — Suivre ses prospects en direct sur la carte
- [x] CRM77 — Écrire un article de blog optimisé SEO (18/11 : voix 1 105 crédits, 2e prise, publié RapidoCMS + Académie ; bouton « Enregistrer et publier » ajouté)
- [ ] CRM78 — Mots-clés, scores et tendances : le calendrier de publication
- [ ] CRM79 — Publicités Google Ads et Meta Ads pilotées par les agents IA
- [ ] CRM80 — La communication par entreprise et le tableau de bord KPI
- [x] CRM81 — Le portail client (lien magique : devis, factures, contrats, demandes, fidélité, rendez-vous) (17/11 : voix 938 crédits, 2e prise, publié RapidoCMS + Académie ; bugs corrigés : facture payée « À régler », aucune confirmation dans la boîte de réception)
- [x] CRM82 — Sécuriser son compte : la double authentification (17/11 : voix 1 090 crédits, 2e prise après répartition des actions, publié RapidoCMS + Académie)
- [x] CRM83 — La facture électronique Factur-X (17/11 : voix 978 crédits, publié RapidoCMS + Académie ; bouton « Compléter mon entreprise » ajouté au CRM)
- [x] CRM84 — Suivre les e-mails et SMS envoyés, gérer les désinscriptions (voix 1 158 crédits, publié le 17/11)
- [ ] CRM87 — Toute la communication d'un client (chronologie tous canaux, filtres, prochaines actions) — écran `/communication/client/{id}`
- [ ] CRM88 — Confier un événement à l'équipe RapidoRH (devis signé, ticket urgent, appel, bloc de Marketing Map → tâches des employés IA)
- [ ] CRM89 — Marketing Map : audience des pages et statistiques des posts RapidoCMS reliés aux blocs
- [x] CRM90 — Centre d'aide public et répartition des nouveaux prospects (18/11 : voix 982 crédits, publié RapidoCMS + Académie ; centre d'aide en 419 corrigé)
- [x] CRM86 — Transformer vos appels en actions (appels de l'agent vocal → analyse de réunion, réglages : analyse automatique, enregistrement des appels de l'équipe ; développé le 17/11, PR #115 commit 98b21f25) — publié le 17/11 (1 min 16, RapidoCMS + Académie)
- [x] CRM85 — Transformer une réunion en actions (analyse de réunion développée le 17/11, PR #115 ; tournage en cours)

### Inventaire du 17/11 (après-midi) — fonctionnalités de RapidoCRM sans tutoriel ou avec un tutoriel périmé
- **Développées, écran prêt, sans tutoriel** (écrans audités 1440 / 390 px : aucune erreur JS ni réseau, aucun débordement) :
  CRM73 agent IA des sites (⚠️ modèle de langage simulé), CRM74 boîte de réception et tickets, CRM77 blog, CRM53 / CRM54 éditeur (sections, 70 modèles,
  téléphone), CRM55 ventes en ligne (clé Stripe de test), CRM81 portail client, CRM82 double authentification, CRM83 Factur-X, CRM84 suivi des envois
  et désinscriptions.
- **Tutoriels périmés** (tournés le 13/11, avant la refonte du module les 15–17/11) → à retourner : CRM13 factures (+ Factur-X), CRM15 contrats v2
  (signature, relances, reconduction), CRM17 / CRM18 campagnes e-mail et SMS (audiences, compteur SMS, aperçu, test), CRM21 segments (constructeur
  ET / OU), CRM27 jeux concours v2 (4 mécaniques), CRM28 sondages v2 (logique conditionnelle).
- **Prévus au plan mais absents du code** (pas de tutoriel possible) : CRM71 prompteur temps réel, CRM72 enregistrement et analyse des appels,
  CRM78 mots-clés et calendrier de publication, CRM79 publicités Google / Meta, CRM80 communication par entreprise et KPI, CRM31 écran Salons.
- **RapidoMeet → RapidoCRM** (précision de Michael, 17/11 : le dépôt RapidoMeet n'est pas à utiliser ; ses fonctionnalités ont été reprises dans RapidoCRM).
  Vérification du code de RapidoCRM (branche `correctifs-tutoriels` et toutes les branches distantes, dont l'ancienne `master`) :
  | RapidoMeet | Dans RapidoCRM | État |
  |---|---|---|
  | Nouvelle réunion (envoi audio / vidéo), transcription, rapport, liste des réunions | « Analyse de réunion » `/analyse` (développé le 17/11 à la demande de Michael, remplace les maquettes « Analyse visio ») | ✅ import Teams / Zoom / Meet (.vtt, .srt, .txt) ou texte collé ; audio / vidéo via ElevenLabs Scribe sur activation (`REUNIONS_TRANSCRIPTION`) ; compte rendu, PDF, statistiques — tutoriel CRM85 |
  | Extraction des tâches, décisions, contacts ; actions envoyées au CRM / RH / CMS avec confirmation | idem | ✅ tâches (RapidoCRM ou liste RapidoRH), contacts, rendez-vous, décisions, questions, rubriques par type — toujours après confirmation humaine (RapidoCMS non relié) |
  | Transcription en direct | — | ⛔ absent |
  | Agenda, visio de rendez-vous | Agenda, visio Whereby + stratégies à l'écran | ✅ (tutoriels CRM33, CRM34) |
  | Scénarios | Workflows | ✅ (CRM23) |
  | Skills marketplace | 100 agents IA, un prompt par outil | ✅ (CRM60, CRM61) |
  | Éditeur d'e-mails, éditeur PDF, pages de destination | Modèles e-mail / SMS, éditeur (brochures A4), Sites v2 | ✅ (CRM22, CRM50) — éditeur à filmer (CRM53 / 54) |
  | Intégrations, clés d'API, abonnement, espace d'équipe, notifications | Connexions MCP, jetons d'API, abonnement et packs, utilisateurs, notifications | ✅ (CRM42, CRM59, CRM69, CRM41, CRM36) |
  | Statistiques | Tableau de bord, statistiques par module | ✅ (CRM02) |
  | Export comptable | — | ⛔ absent (seuls les exports CSV de formulaires, jeux, sondages) |
  | Affiliation | — | ⛔ absent (seulement le parrainage du programme de fidélité) |
  → Michael a choisi (17/11) de développer réellement l'analyse de réunion : livrée dans la PR brouillon #115 (commit 9d3f49d0, 16 tests, 488 tests verts
  SQLite + MySQL 8), tutoriel **CRM85**. Reste hors périmètre : transcription en direct, export comptable, affiliation.


## B. RapidoCMS — un tutoriel par onglet / écran

- [x] CMS01 — Créer son compte et choisir un pack
- [x] CMS02 — Visite guidée du tableau de bord
- [x] CMS03 — Connecter ses réseaux sociaux (Facebook, Instagram, LinkedIn, TikTok)
- [~] CMS04 — Connecter LinkedIn → fusionné dans CMS03 (un seul écran, quatre panneaux)
- [~] CMS05 — Connecter TikTok → fusionné dans CMS03
- [x] CMS06 — Créer son kit de marque
- [x] CMS07 — Les clés d'API et les intégrations (Zapier, Make, n8n)
- [x] CMS08 — Rédiger un post avec l'IA
- [x] CMS09 — Générer un visuel IA
- [~] CMS10 — Transformer une photo (image vers image) → fonction disponible uniquement via le connecteur MCP : traitée dans CMS24
- [ ] CMS11 — La bibliothèque de fichiers
- [ ] CMS12 — Mes templates
- [ ] CMS13 — Mes prompts
- [ ] CMS14 — Propositions de contenus
- [ ] CMS15 — Le calendrier éditorial
- [ ] CMS16 — Programmer, décaler, annuler une publication
- [ ] CMS17 — Les campagnes
- [ ] CMS18 — Statistiques des publications
- [ ] CMS19 — Historique
- [ ] CMS20 — Cartes de visite digitales et pages de liens
- [ ] CMS21 — Blog
- [ ] CMS22 — Notifications et email
- [ ] CMS23 — Abonnements, packs et paiement
- [x] CMS24 — Connecter RapidoCMS à Claude (MCP)

## C. RapidoRH — un tutoriel par onglet / écran

- [x] RH01 — Créer son espace et son compte administrateur
- [x] RH02 — Visite guidée du tableau de bord
- [x] RH03 — Inviter et gérer ses collaborateurs
- [x] RH04 — Départements
- [x] RH05 — Rôles et permissions
- [x] RH06 — Créer un projet
- [x] RH07 — Listes de tâches et Kanban
- [x] RH08 — Détail d'une tâche
- [x] RH09 — Documents et liens du projet
- [x] RH10 — Les dailies
- [x] RH11 — Agenda
- [x] RH12 — Rendez-vous
- [ ] RH13 — Pointage des horaires
- [x] RH14 — Congés
- [x] RH15 — Espace collaborateur (vue membre)
- [ ] RH16 — Modèles d'emails
- [x] RH17 — Notifications (email, WhatsApp)
- [x] RH18 — Abonnement et facturation
- [x] RH19 — Connecter RapidoRH à Claude (MCP)

### RapidoRH V2 — employés IA et collaboration (voix Adam, une prise)
- [x] RH20 — Transformer une idée en projet
- [x] RH21 — Valider le travail d'un employé IA
- [x] RH22 — Créer et activer une routine
- [x] RH23 — La messagerie d'équipe
- [x] RH24 — Demander une information et débloquer une tâche
- [x] RH25 — Le forum d'entraide et la connaissance validée
- [x] RH26 — Les paramètres IA de l'entreprise
- [ ] RH27 — Réunions Whereby (bloqué : aucune clé Whereby fournie)
- [x] RH28 — Découvrir vos employés IA
- [x] RH29 — Configurer et activer un employé IA
- [x] RH30 — Confier une tâche à un employé IA
- [x] RH31 — Suivre le travail de vos employés IA
- [x] RH32 — Demander un congé (collaborateur)
- [ ] RH33 — Répondre dans la messagerie (collaborateur ; voix non générée : crédits ElevenLabs épuisés)

## D. Formations métier (avec Rapido et l'IA)

### Marketing & communication
- [x] F01 — Construire sa ligne éditoriale en 1 heure avec l'IA
- [x] F02 — Un mois de contenus en une après-midi (RapidoCMS)
- [ ] F03 — Écrire un post qui engage : structure et accroches
- [ ] F04 — Visuels de marque cohérents avec un kit de marque
- [ ] F05 — Lire ses statistiques et décider quoi refaire
- [ ] F06 — Newsletter qui se lit : objet, contenu, fréquence
- [ ] F07 — Communication de crise et avis négatifs

### Commercial & prospection
- [ ] F08 — Définir sa cible et son fichier de prospects
- [ ] F09 — Prospection locale avec Google Maps et SIRET
- [ ] F10 — Le premier appel : script et qualification (agent vocal)
- [x] F11 — Le cold email qui obtient des réponses (16/11 : script vérifié dans le code de RapidoCRM, voix générée — en file de rendu)
- [x] F12 — Piloter son pipeline et ses prévisions (16/11 : script vérifié dans le code de RapidoCRM, voix générée — en file de rendu)
- [x] F13 — Le devis qui se signe : présentation et relances (16/11 : script vérifié dans le code de RapidoCRM, voix générée — en file de rendu)
- [x] F14 — Salons : avant, pendant, après (16/11 : script vérifié dans le code de RapidoCRM, voix générée — en file de rendu)
- [x] F15 — Fidéliser : programmes, jeux concours, avis (16/11 : script vérifié dans le code de RapidoCRM, voix générée — en file de rendu)
- [x] F40 — Transformer sa carte de visite en machine à prospects (carte digitale, NFC, devis en ligne) (script, voix générée — en file de rendu)
- [x] F41 — Du lead magnet à la vente : construire son tunnel avec Claude (script, voix générée — en file de rendu)
- [x] F42 — Fidélité digitale : tampons, parrainage et récompenses qui font revenir (script, voix générée — en file de rendu)
- [x] F43 — Faire travailler son équipe IA : CRM + RapidoRH connectés (script, voix générée — en file de rendu)

### Gestion de projet & équipe
- [ ] F16 — Lancer un projet : découpage, rôles, échéances
- [ ] F17 — Le Kanban au quotidien
- [ ] F18 — Le daily efficace en 5 minutes
- [ ] F19 — Intégrer un nouveau collaborateur
- [ ] F20 — Gérer congés et charge de travail

### Intelligence artificielle
- [x] F21 — Comprendre l'IA générative pour son entreprise (script, voix générée — en file de rendu)
- [x] F22 — Bien écrire un prompt (script, voix générée — en file de rendu)
- [x] F23 — Qu'est-ce qu'un connecteur MCP ? (script, voix générée — en file de rendu)
- [x] F24 — Brancher la suite Rapido à Claude (script, voix générée — en file de rendu)
- [x] F25 — Agents IA : déléguer sans perdre le contrôle (script, voix générée — en file de rendu)
- [x] F26 — Automatiser avec les workflows Rapido (script, voix générée — en file de rendu)

### Par secteur d'activité
- [ ] F27 — Restaurant & food : Rapido au quotidien
- [ ] F28 — Artisans & BTP
- [ ] F29 — Agences & freelances
- [ ] F30 — Commerce de proximité
- [ ] F31 — Immobilier
- [ ] F32 — Services aux entreprises (PME)
- [ ] F33 — Santé & bien-être
- [ ] F34 — Associations & événementiel

## E. Site web RapidoSoftware — vrais écrans

Dépôt `rapido-software`, branche `ccr-dbfe6358-2gefhr` (jamais `production` sans l'accord de Michael).
Hébergement des vidéos (décision de Michael, 13/11/2026) : 720p, dans la bibliothèque RapidoCMS du compte (S3).
Mise à jour du site : `python3 _gabarit/export-site.py /home/user/rapido-software/resources/data/academie.json`.
- [ ] W1 — Remplacer les captures et démos de la page RapidoCRM par les vrais écrans filmés (boucles vidéo courtes + animations HTML/CSS)
- [ ] W2 — Idem page RapidoCMS
- [ ] W3 — Idem page RapidoRH
- [x] W5 — Marketplace de prompts (/marketplace-prompts) : 46 prompts CRM/CMS/RH/suite, filtres logiciel · catégorie · fonctionnalité · outil MCP, champs [entre crochets] en formulaire, Claude / ChatGPT / Mistral, bouton Infos → tutoriel (commit b0aee81, branche ccr-dbfe6358-2gefhr)
- [x] W4 — Accueil : section « tutoriels » qui présente les vidéos réalisées → « Académie Rapido » (/academie, page vidéo, section accueil et pages produit), branche ccr-dbfe6358-2gefhr, commit 08cf25d

---

## Journal des exécutions

| Date (Paris) | Éléments traités | Résultat | Notes |
|---|---|---|---|
| 13/11 01 h 40 | P1, P2 | Perdu | La session de la routine n'avait pas le dépôt vidéo : push refusé (403), travail resté dans le conteneur. Routine mise en pause. |
| 13/11 02 h 50 | P1, P2, P3, P4, CRM01 | Fait | Voix et style validés par Michael ; chaîne générique `_gabarit/make.sh` (tournage, minutage, montage, rendu, miniature). |
| 13/11 02 h 30 | Pilote CRM02 (vidéo + miniature) | Fait, en attente de validation | `videos/tutoriels-rapido/CRM02.mp4` (1 min 07, −14 LUFS), `tutoriels-rapido/CRM02/miniature.png`. Gabarits : `_gabarit/build-tutoriel.py`, `_gabarit/miniature.cjs`, `_gabarit/demo-crm.php`. |


## Correctifs RapidoCRM (13/11/2026, demande de Michael : « résous les bugs en même temps »)

Branche `correctifs-tutoriels` du dépôt `rapido-crm` (poussée, **pas de PR** : toute PR vers `production`
est fusionnée et déployée automatiquement — à ouvrir avec l'accord de Michael) :
- marqueurs de conflit de la fusion #97 résolus (3 sources) et `public/build` recompilé → les écrans Vue chargent ;
- `EntrepriseProfil.vue` : bloc de 1 073 lignes perdu à la fusion a5cfe8b (21/08) restauré depuis e1a9304 ;
- `public/assets/js/toasts.js` : ne supprime plus les conteneurs `.alert` vides/masqués réservés aux erreurs
  → le bouton « Créer » d'un pipeline fonctionne de nouveau (il ne trouvait plus `#pipelineError`).
Les mêmes correctifs sont appliqués à la copie de tournage `/home/user/rapido-crm-film`.

Suite (même branche, 13/11 après-midi) :
- contrats : modèles par défaut proposés dans la fiche client ; page de signature et PDF ne plantent plus
  sur un modèle par défaut ; variables `{{client_nom}}`… remplies (`ContratVariablesService`) ;
- CKEditor : plugins `emoji`/`codesnippet` en 404 → plus aucun éditeur de texte riche ne s'ouvrait
  (campagnes e-mail, devis, factures, boîte mail) ; bandeau « version is not secure » supprimé ;
- campagne SMS : aperçu lisible (texte blanc, casse d'origine) et au nom de la société ;
- modèles e-mail/SMS : recherche et catégorie s'appliquent aussi aux modèles globaux ; texte « liste vide » SMS ;
- workflows : « créer depuis un modèle » ouvre l'éditeur (au lieu d'un JSON brut) ; menu Filtre branché
  (il contenait les textes d'exemple Bootstrap) ;
- **sécurité** : routes de back-office sans `auth` (workflows, segmentation, pipeline, contrats,
  historique général, analyse, /test, /test/email, /test-logo/{id}, upload-ckeditor…) passées sous `auth`.
- Reste à signaler (non corrigé, choix produit) : `POST devis/{id}/signer` est public et non signé
  (n'importe qui peut signer un devis par son numéro) ; critères de segment saisis en JSON brut.

## Blocage voix (13/11, 16 h) — crédits ElevenLabs épuisés
Quota du compte atteint (101 crédits restants, ~800–1 000 par épisode). CRM23 est scénarisé
(`CRM23/tuto.json`) mais sans voix. Reprise dès recharge des crédits : générer la voix avec le texte
des paragraphes (voix Adam - Instructor), puis `bash _gabarit/file.sh CRM23`.
CRM20 : recentré sur « campagnes automatiques » (bouton de la liste Clients + suivi des envois programmés).

## Formations agents IA (14/11/2026) — page /academie/agents-ia du site

Motion design (gabarit formation, voix Adam), une par étape du guide :
- [x] AG01 — Connecter un MCP à son assistant IA
- [x] AG02 — Créer un agent IA spécialisé
- [x] AG03 — Confier une routine à un agent
- [x] AG04 — Le loop-engineering : des routines qui s'améliorent
- [x] AG05 — Les KPI qui pilotent le loop-engineering

## Session programmée 1/6 (14/11/2026, 19 h 30)
- CRM35 « Les tâches de l'équipe » publié (refilmé une fois pour la synchronisation voix/image).
- CRM36 « L'équipe commerciale et ses objectifs » publié (refilmé : premier rendu désynchronisé car tourné pendant
  l'encodage 720p de CRM35 (machine saturée) → ne jamais tourner pendant un encodage ou un rendu.
- Correctifs RapidoCRM (commits LOCAUX sur correctifs-tutoriels, non poussés — aucune GitHub Action) :
  - Tâches : l'origine reste lisible si le workflow a été supprimé (withTrashed).
  - Commerciaux (sécurité) : profil, édition, objectifs, disponibilité et suppression limités à la société
    (avant : User::findOrFail / User::destroy sur n'importe quel identifiant) ; page objectifs qui plantait
    sans objectifs ; jauge « 100 % atteints » sans objectif → 0 % + lien ; objectifs mensuels comparés aux
    envois du mois ; ObjectifCommercialService partagé avec l'outil MCP update_commercial_objectifs.

### Session du 14/11 (soir) — suite des tutoriels CRM
- Publiés : CRM37 (stratégies, republié avec la stratégie visible en visio), CRM38 (historique), CRM39 (documents
  et bibliothèque), CRM40 (prompts, génération simulée faute de clé IA locale), CRM34 (visio + stratégie, salle
  de visio simulée faute de service de visio local). Académie : 57 épisodes.
- Correctifs rapido-crm (locaux, non poussés) : stratégies, historique (montants TTC faux, devis d'une autre
  société), API fiches clients (18 actions sans contrôle, dont la suppression), bibliothèque (tailles, images de
  l'éditeur), prompts privés, éditeur de prompts, notifications (tâche assignée, devis ouvert), visio
  (organisateur refusé, panneau stratégie), accents mal encodés, chemin des assets.
- Session programmée 2/6 (00:30) : ses tâches CRM37–CRM39 étaient déjà faites ; rattrapage CRM41 Notifications
  publié (notifications « tâche confiée » et « devis ouvert » ajoutées au CRM, textes d'exemple « Clover Bistro »
  en dur retirés). À signaler : fuseau de l'application codé en dur `Africa/Tunis` (config/app.php), APP_TIMEZONE ignoré.
- Reste : CRM31 Salons, CRM42 Abonnement et packs.

### Session du 15/11 (nuit) — formulaires et fuseau horaire (demande de Michael)
- RapidoCRM : refonte des formulaires (lien public /f/{slug}, iframe à hauteur automatique, design personnalisable
  avec aperçu, réponses + export CSV, notifications, sécurité), fuseau horaire dans le profil entreprise.
- Vidéos : CRM24 refait (lien public), CRM46 (design), CRM47 (intégration iframe sur un site fictif servi en local
  sur le port 8131 par _gabarit/site-demo, et suivi des réponses).

### Session du 15/11 (nuit, suite) — CTA et audit concurrentiel (demande de Michael)
- Recherche HubSpot (formats, ciblage, A/B, statistiques) et comparatifs CRM PME 2026 ; audit complet dans
  rapido-crm/docs/AUDIT_CONCURRENTS_2026-11-15.md.
- RapidoCRM : CTA refondus (4 formats, design, ciblage, période, A/B, widget, suivi, statistiques, 3 outils MCP),
  désinscription des envois marketing (RGPD).
- Vidéos : CRM48 (création d'un CTA pop-up et intégration sur le site fictif), CRM49 (statistiques et test A/B).

### Session programmée 3/6 (15/11, 04:30)
- CRM40, CRM41, CRM34 : déjà publiés lors des sessions précédentes.
- CRM42 Abonnement et packs : exploré, données fictives (`_gabarit/abonnement-demo.php`, `avant-CRM42.sh`),
  scénario `CRM42/tuto.json`, essai à blanc validé. **Voix impossible : quota ElevenLabs épuisé (326 crédits
  restants, 824 nécessaires)** — à reprendre dès que le quota est rechargé (puis file.sh, planche, publication).
- CRM31 Salons : non repris, même blocage (voix).
- Correctifs rapido-crm (commits locaux, non poussés) :
  - « Error initializing abonnement: Attempt to read property id on null » : venait du code (EmailService, utilisateur
    sans abonnement actif) → cas géré, plus d'erreur au journal ;
  - facture PDF d'abonnement entièrement en dur (1490 €, « Annuelle », dates de 2024) → vraies valeurs ;
  - historique : prix mensuel affiché pour un abonnement annuel → prix selon la périodicité ;
  - téléchargement de facture d'abonnement sans contrôle de propriété → limité au titulaire ;
  - historique des packs : « 30 agent_vocal » → « 30 min d'agent vocal », « Gb » → « Go ».
- Contrôle mobile 390 px : 29 écrans, aucun débordement (dont les nouveaux écrans Jeux et Sondages).
- Jeux concours v2 et sondages v2 livrés dans la même nuit (voir CLAUDE.md de rapido-crm).

### Séance du 15/11, 16 h 50 — nouveaux modules (interrompue : fin des crédits de la session)
- Épisodes CRM50–CRM69 et formations F40–F43 ajoutés au plan.
- Scénarios écrits : CRM65 (carte digitale en 1 clic), CRM66 (NFC), CRM67 (fidélité et caisse), CRM68 (devis en ligne), CRM69 (RapidoRH).
- CRM65 : voix générée (Adam, une prise, 68 s, `CRM65/audio/voix.mp3`) ; le tournage a échoué sur un `TimeoutError` Playwright
  (voir `/tmp/claude-0/CRM65.log` si encore présent) → relancer `bash _gabarit/file.sh CRM65` après `bash _gabarit/serveurs.sh`,
  corriger le sélecteur fautif dans `CRM65/tuto.json` si besoin (essai à blanc conseillé).
- Voix CRM66–CRM69 : NON générées (dépense refusée par Michael pendant la séance) — demander son accord avant de générer.
- Copie de tournage `rapido-crm-film` synchronisée (migrations 160000, 170000, 180000) et données fictives créées
  (`_gabarit` : `_gabarit/cartes-demo.php`, via `php artisan tinker` : carte « Léa Martin », programme « Carte café », formulaire « Demande de devis »).

### Séance du 15/11, 18 h 30 → 22 h (heure de Paris) — reprise programmée (accord de Michael : toutes les voix, une prise)
- Conteneur neuf : copie de tournage recréée (`/home/user/rapido-crm-film`, `vendor` partagé par lien avec rapido-crm, base SQLite
  « Studio Lumière » via `demo-crm.php` + `cartes-demo.php` + nouveau `sites-demo.php`). RapidoCMS (8125) et RapidoRH (8126) non installés ici.
- CRM65 : l'essai à blanc ne montre aucune cible manquante ; relancé tel quel → **rendu OK (76 s)**. Le `TimeoutError` venait du
  serveur à froid, pas d'un sélecteur.
- Nouvel outil `_gabarit/essai-blanc.cjs` (vérifie chaque cible d'un scénario, saisies comprises, sans voix ni vidéo) et
  `_gabarit/reperage.cjs` (titres, boutons, liens et champs d'un écran pour écrire un scénario).
- Voix générées (Adam, eleven_v4, une prise) : CRM66 (859 cr.), CRM67 (990), CRM68 (982), CRM69 (1 091), CRM50 (956), CRM51 (815), CRM52 (852), CRM62 (905), CRM63 (894), CRM64 (738), CRM59 (882), CRM60 (720), CRM61 (662), CRM56 (880), CRM58 (995), F40 (1 160), F41 (960), F42 (1 027), F43 (1 077), F21 (1 098), F22 (1 056), F23 (1 049), F24 (901), F25 (1 022), F26 (929)
  → 6 545 crédits.
- CRM66 : **rendu OK (56 s)** après une première tentative perdue (disque plein pendant le rendu). CRM69 : relancé après un plantage
  du navigateur (même cause).
- Scénarios écrits et validés à blanc : CRM50 (sites, SEO, audit, plan du site), CRM51 (nom de domaine, domaine fictif
  `studio-lumiere-demo.fr`), CRM52 (sous-domaine d'envoi SPF / DKIM / DMARC) ; `avant-`/`apres-CRM51.sh` et `CRM52.sh` remettent le site
  de démo à zéro. CRM68 : le formulaire de démo a 5 produits → clic sur le 4e « + » au lieu du 6e.
- ⚠️ Disque : le conteneur a saturé deux fois (ancien clone `/home/user/Video` de 17 Go impossible à supprimer par l'agent,
  dépendances Composer clonées avec leur historique git). Garder > 3 Go libres avant un rendu.

## Journal — 16/11, exécution de 7 h 10
- Redémarrage du conteneur vers 2 h : CRM56 coupé pendant son rendu → rendu seul ; file relancée (`/tmp/claude-0/file15.sh` → 18).
- Publiés (RapidoCMS + Académie) depuis 2 h : CRM50, 51, 62, 65, 66, 68, 69. Lot 2 (CRM52, 59, 60, 63, 64, 67) encodé en fin de file15.
- CRM56 vérifié (défauts mineurs : zone « Design » non surlignée, adresse locale dans le code d'intégration). CRM61 : écran blanc de 4 s en fin → corrigé, retournage.
- Nouveaux : CRM57 (tunnel créé par Claude, démo par TunnelVenteService), formations F21–F26 (IA, prompt, MCP, Claude, agents, workflows). Voix : CRM57 (847), F21 (1 098), F22 (1 056), F23 (1 049), F24 (901), F25 (1 022), F26 (929).
- Copie de tournage synchronisée avec rapido-crm (5 migrations de l'autre agent : agents IA, journal MCP, agent des sites, idempotence, tickets) : l'écran Connexions plantait (table webhooks absente).
- Disque : ~1 Go libre ; les fichiers déjà poussés de videos/ sont retirés de l'arbre (`git update-index --skip-worktree` puis suppression).

## Journal — 17/11, séance de l'après-midi (demande de Michael : nouveaux modules)
- Revue du travail de l'autre agent (Téléphonie, Marketing Map, constructeur de segments) : 470 tests verts SQLite + MySQL 8 ; parcours testés au navigateur
  (1440 / 390 px) sans erreur. Ergonomie corrigée dans rapido-crm (commits 5dec7885, 662a164b, PR brouillon #115) : conditions bloquantes de la
  téléphonie visibles avec action, numéros lisibles, rappel étiqueté ; modèles de carte en lignes de trois, état « Active », lien de partage visible
  avec copie, cadrage 2,5D / 3D.
- Publiés (RapidoCMS + publication.json + Académie : 102 épisodes) : CRM70 (67 s), CRM75 (78 s), CRM76 (72 s). Voix Adam, une prise : 1 034 + 1 236 + 1 135
  = 3 405 crédits. CRM70 et CRM75 retournés une fois (cadrage), sans nouvelle voix.
- Téléphonie filmée en mode simulé (`TWILIO_SIMULATE=true` dans la copie de tournage seulement) : message simulé remplacé à l'image par celui d'un vrai
  appel (`replace_text`), bandeau « Mode test » masqué (nouvelle option `css` de record.cjs). Démo : `telephonie-demo.php`, `marketing-map-demo.php`.
- Piège : le cadrage (`zone`) d'un paragraphe s'applique dès son début : ne pas cadrer une fenêtre qui s'ouvre au milieu du paragraphe.
- Piège : `fusion-academie.py` lit les épisodes dans le fichier exporté : enchaîner export (enregistrer-publication.py) puis fusion, sans revenir au fichier d'origine entre les deux.

### Journal 17/11 (après-midi) — analyse de réunion
- Michael : développer réellement l'analyse de réunion dans RapidoCRM (reprise de RapidoMeet). Livré dans la PR brouillon #115
  (commit 9d3f49d0 puis correctifs d'analyse : « aujourd'hui, on fait le point » n'est plus un rendez-vous, « est-ce que vous pouvez… ? »
  est une question et non une tâche ; trouvés pendant le repérage du tutoriel). 488 tests verts SQLite + MySQL 8.
- CRM85 tourné (2 prises : la 1re décalée de 7 s sur le dépôt, titre désormais rempli d'un coup), voix Adam une prise = 1 989 crédits,
  publié : RapidoCMS `tutoriel-rapido-CRM85.mp4/.png`, Académie 103 épisodes (rapido-software).
- essai-blanc.cjs gère désormais `upload` (dépôt de fichier) comme record.cjs.
- Appels → analyse de réunion (accord de Michael, y compris la dépense d'enregistrement) : livré PR #115 commit 98b21f25. Débogage pendant le repérage :
  webhook de fin d'appel de l'agent vocal en 500 à chaque appel (imports manquants, GREATEST() MySQL seulement) — corrigé ; analyse : « 8 000 €. »
  non relevé, « décaler notre rendez-vous » pris pour un nouveau rendez-vous, politesse prise pour une question, rappel attribué au client,
  appelant qui se présente affiché « Client » ; bouton « CopierLe compte rendu » ; statuts bruts « termine / non defini » et numéros coupés dans
  le journal de l'agent vocal — tous corrigés. CRM86 tourné et publié (voix 1 226 crédits), Académie 104 épisodes.

### Inventaire du 17/11 (soir) — travail des autres agents récupéré
- RapidoCRM (session 0191…) : blog (mesure de lecture, prospects par article, commentaires), Marketing Map (audience, posts RapidoCMS), agent IA
  du site (simulateur, sources, statut de commande), boîte de réception (réponse depuis la file), vue Communication, événements vers RapidoRH.
  Écrans vérifiés en 1440 / 390 px : conformes au design system (sites-ecran, encadrés, pastilles, états vides). Seule la Segmentation (ancien écran)
  n'était pas conforme → corrigée (commit 29396a58).
- RapidoRH (branche ccr-281b30bc-x0biva) : outil crm-event-tool (événements CRM → tâches des employés IA), F1 (identifiants limités à l'entreprise).
  Tutoriel RH correspondant à prévoir quand la branche sera fusionnée et déployée.
- Site : pages produits refondues avec fil conducteur, nouvelles fonctionnalités et vrais écrans, plus aucun « V2 » (PR brouillon #49).


## Journal — 18/11, nuit (demande de Michael : revue du travail de l'autre agent, bugs, tutoriels)

- Revue des écrans livrés par l'autre session (blog, agent du site, relation client, KPI RapidoRH), tests navigateur 1440 / 390 px.
- **Bugs corrigés dans rapido-crm** (PR #115) :
  - ⚠️ rappels externes en 419 en production : `routes/api.php` passe par le groupe `web` (CSRF) ; Twilio (téléphonie, SMS STOP), compte rendu
    RapidoRH, centre d'aide, commentaires et mesure du blog, API REST des outils ne pouvaient pas aboutir (tests sans CSRF) → exemptés, test qui rejoue
    le vrai CSRF (a2f77654) ;
  - base de connaissances des agents du site réindexée toutes les heures (daaaf29b) ; source citée une seule fois (bd1eb476) ;
  - tickets : retard visible dès l'échéance dépassée, sans attendre `tickets:sla` (baefe326, c34e8448) ;
  - blog : bouton « Enregistrer et publier » (06a10f23) ;
  - casse : première lettre forcée par le thème sur les écrans `sites-ecran` (adresses e-mail), Score des prospects.
- Tutoriels : CRM77 blog publié (2e prise : cadrage des commentaires) ; CRM73 (2e prise : questions saisies d'un coup), CRM74, CRM90 en cours.
- Copie de tournage : `APP_URL=http://127.0.0.1:8124` (liens des sources de l'agent), resynchronisée par `tar` (pas de rsync dans le conteneur).
