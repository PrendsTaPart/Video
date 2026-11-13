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
Règle : on ne modifie pas `rapido-crm` → **CRM04 à CRM43 en attente de la décision de Michael** ; la production
continue avec les sections B (RapidoCMS) puis C (RapidoRH), puis D. Reprendre la section A dès que le dépôt est corrigé.

## A. RapidoCRM — un tutoriel par onglet / écran

- [x] CRM01 — Créer son compte et choisir son forfait
- [x] CRM02 — Visite guidée du tableau de bord
- [x] CRM03 — Compléter son profil et sa configuration
- [ ] CRM04 — Prospecter sur Google Maps
- [ ] CRM05 — Rechercher une entreprise par SIRET
- [ ] CRM06 — Gérer ses prospects et leurs notes
- [ ] CRM07 — Le pipeline : étapes, déplacement, clôture
- [ ] CRM08 — L'agent vocal IA : configuration et premiers appels
- [ ] CRM09 — Historique des appels
- [ ] CRM10 — Contacts et entreprises
- [ ] CRM11 — Catalogue produits et offres
- [ ] CRM12 — Créer et envoyer un devis
- [ ] CRM13 — Factures et suivi des paiements
- [ ] CRM14 — Dépenses
- [ ] CRM15 — Contrats et signature électronique
- [ ] CRM16 — Modèles de contrats
- [ ] CRM17 — Campagnes email
- [ ] CRM18 — Campagnes SMS et aperçu
- [ ] CRM19 — Newsletters
- [ ] CRM20 — Campagnes automatiques
- [ ] CRM21 — Segments
- [ ] CRM22 — Modèles d'emails et de SMS (éditeur)
- [ ] CRM23 — Workflows : créer, activer, suivre
- [ ] CRM24 — Formulaires
- [ ] CRM25 — CTA et pages
- [ ] CRM26 — Programme de fidélité et cartes NFC
- [ ] CRM27 — Jeux concours
- [ ] CRM28 — Sondages
- [ ] CRM29 — Avis clients
- [ ] CRM30 — Cartes de visite digitales
- [ ] CRM31 — Salons et leads de salon
- [ ] CRM32 — Événements
- [ ] CRM33 — Agenda et rendez-vous
- [ ] CRM34 — Visioconférence
- [ ] CRM35 — Tâches
- [ ] CRM36 — Équipe commerciale et objectifs
- [ ] CRM37 — Stratégie commerciale assistée par IA
- [ ] CRM38 — Statistiques et engagement
- [ ] CRM39 — Documents et stockage
- [ ] CRM40 — Bibliothèque de prompts et assistant
- [ ] CRM41 — Notifications
- [ ] CRM42 — Facturation de l'abonnement et packs
- [ ] CRM43 — Connecter RapidoCRM à Claude (MCP)

## B. RapidoCMS — un tutoriel par onglet / écran

- [x] CMS01 — Créer son compte et choisir un pack
- [x] CMS02 — Visite guidée du tableau de bord
- [x] CMS03 — Connecter ses réseaux sociaux (Facebook, Instagram, LinkedIn, TikTok)
- [~] CMS04 — Connecter LinkedIn → fusionné dans CMS03 (un seul écran, quatre panneaux)
- [~] CMS05 — Connecter TikTok → fusionné dans CMS03
- [ ] CMS06 — Créer son kit de marque
- [x] CMS07 — Les clés d'API et les intégrations (Zapier, Make, n8n)
- [ ] CMS08 — Rédiger un post avec l'IA
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
- [ ] CMS24 — Connecter RapidoCMS à Claude (MCP)

## C. RapidoRH — un tutoriel par onglet / écran

- [ ] RH01 — Créer son espace et son compte administrateur
- [ ] RH02 — Visite guidée du tableau de bord
- [ ] RH03 — Inviter et gérer ses collaborateurs
- [ ] RH04 — Départements
- [ ] RH05 — Rôles et permissions
- [ ] RH06 — Créer un projet
- [ ] RH07 — Listes de tâches et Kanban
- [ ] RH08 — Détail d'une tâche
- [ ] RH09 — Documents et liens du projet
- [ ] RH10 — Les dailies
- [ ] RH11 — Agenda
- [ ] RH12 — Rendez-vous
- [ ] RH13 — Pointage des horaires
- [ ] RH14 — Congés
- [ ] RH15 — Espace collaborateur (vue membre)
- [ ] RH16 — Modèles d'emails
- [ ] RH17 — Notifications (email, WhatsApp)
- [ ] RH18 — Abonnement et facturation
- [ ] RH19 — Connecter RapidoRH à Claude (MCP)

## D. Formations métier (avec Rapido et l'IA)

### Marketing & communication
- [x] F01 — Construire sa ligne éditoriale en 1 heure avec l'IA
- [ ] F02 — Un mois de contenus en une après-midi (RapidoCMS)
- [ ] F03 — Écrire un post qui engage : structure et accroches
- [ ] F04 — Visuels de marque cohérents avec un kit de marque
- [ ] F05 — Lire ses statistiques et décider quoi refaire
- [ ] F06 — Newsletter qui se lit : objet, contenu, fréquence
- [ ] F07 — Communication de crise et avis négatifs

### Commercial & prospection
- [ ] F08 — Définir sa cible et son fichier de prospects
- [ ] F09 — Prospection locale avec Google Maps et SIRET
- [ ] F10 — Le premier appel : script et qualification (agent vocal)
- [ ] F11 — Le cold email qui obtient des réponses
- [ ] F12 — Piloter son pipeline et ses prévisions
- [ ] F13 — Le devis qui se signe : présentation et relances
- [ ] F14 — Salons : avant, pendant, après
- [ ] F15 — Fidéliser : programmes, jeux concours, avis

### Gestion de projet & équipe
- [ ] F16 — Lancer un projet : découpage, rôles, échéances
- [ ] F17 — Le Kanban au quotidien
- [ ] F18 — Le daily efficace en 5 minutes
- [ ] F19 — Intégrer un nouveau collaborateur
- [ ] F20 — Gérer congés et charge de travail

### Intelligence artificielle
- [ ] F21 — Comprendre l'IA générative pour son entreprise
- [ ] F22 — Bien écrire un prompt
- [ ] F23 — Qu'est-ce qu'un connecteur MCP ?
- [ ] F24 — Brancher la suite Rapido à Claude
- [ ] F25 — Agents IA : déléguer sans perdre le contrôle
- [ ] F26 — Automatiser avec les workflows Rapido

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

Dépôt `rapido-software`, branche `site-vrais-ecrans` (jamais `production`).
- [ ] W1 — Remplacer les captures et démos de la page RapidoCRM par les vrais écrans filmés (boucles vidéo courtes + animations HTML/CSS)
- [ ] W2 — Idem page RapidoCMS
- [ ] W3 — Idem page RapidoRH
- [ ] W4 — Accueil : section « tutoriels » qui présente les vidéos réalisées

---

## Journal des exécutions

| Date (Paris) | Éléments traités | Résultat | Notes |
|---|---|---|---|
| 13/11 01 h 40 | P1, P2 | Perdu | La session de la routine n'avait pas le dépôt vidéo : push refusé (403), travail resté dans le conteneur. Routine mise en pause. |
| 13/11 02 h 50 | P1, P2, P3, P4, CRM01 | Fait | Voix et style validés par Michael ; chaîne générique `_gabarit/make.sh` (tournage, minutage, montage, rendu, miniature). |
| 13/11 02 h 30 | Pilote CRM02 (vidéo + miniature) | Fait, en attente de validation | `videos/tutoriels-rapido/CRM02.mp4` (1 min 07, −14 LUFS), `tutoriels-rapido/CRM02/miniature.png`. Gabarits : `_gabarit/build-tutoriel.py`, `_gabarit/miniature.cjs`, `_gabarit/demo-crm.php`. |
