# FoodEatUp Academy — site de documentation Lovable (mémoire du projet)

**À relire à chaque nouvelle vidéo produite.** Ce fichier est la source de vérité du site
Lovable qui documente les tutoriels FoodEatUp — cible **157 vidéos / 14 modules / 11
catégories**, voir `videos/CATALOGUE-157-TUTORIELS.md` pour le détail complet (mis à jour le
2026-08-03, remplace l'ancienne cible à 91-94 vidéos / 5 modules). Chaque vidéo livrée doit
se terminer par l'ajout de son entrée ici (tableau "Tutoriels publiés" en bas) et l'envoi du
prompt Lovable correspondant au projet. **Avant de choisir un sujet, vérifier `src/data/
tutorials.ts` en direct sur Lovable** (pas seulement ce tableau, souvent en retard) : plusieurs
branches produisent en parallèle sans se voir, voir la note de fragmentation dans le tableau
plus bas.

## Identifiants du projet

- **Workspace Lovable** : `Contact.prendstapart` (id `NetRd8k1jtiPYJO1Jlaz`) — c'est le
  workspace "PrendsTaPart" demandé par Michael (le nom exact affiché diffère légèrement de
  celui qu'il a donné à l'oral, mais c'est le seul workspace de ce compte qui correspond à
  la marque PrendsTaPart, rôle *owner*).
- **Project ID** : `55ff35b7-c442-42c4-950c-8c7fd420c645`
- **Nom du projet** (auto-généré par Lovable) : *FoodEatUp Academy*
- **Preview** : https://id-preview--55ff35b7-c442-42c4-950c-8c7fd420c645.lovable.app
- **Éditeur Lovable** : https://lovable.dev/projects/55ff35b7-c442-42c4-950c-8c7fd420c645
- Stack : React + Tailwind + shadcn/ui (TanStack Start), 100% front, pas de backend.

## Règle de validation (ajoutée le 2026-08-02)

**Ne plus publier aucune vidéo sur Lovable ni sur LinkedIn sans validation explicite de
Michael au préalable.** Étapes : monter la vidéo → vérifier la checklist de compatibilité
→ livrer le fichier (`SendUserFile`) → **attendre un retour** → seulement après OK, faire
les étapes 1-5 ci-dessous (upload RapidoCMS, `claudePrompt`, prompt Lovable, tableau de
suivi). Un retour de correction relance le cycle (corriger → relivrer → attendre).

## Comment ajouter une vidéo (à chaque tutoriel produit, une fois validée par Michael)

1. Uploader le MP4 + la vignette sur RapidoCMS (`upload_file_tool`), comme pour la
   publication LinkedIn — récupérer les deux URLs S3 stables.
2. Écrire les champs `howItWorks` (étapes concrètes, à l'impératif) et `whatItsFor`
   (bénéfice pour le restaurateur) à partir du `SCRIPT.md` de la vidéo.
3. **Analyser les outils MCP FoodEatUp** (`mcp__FoodEatUp__*`) pour voir si une action de
   la vidéo correspond à un outil exposé. Si oui : écrire un `claudePrompt` copier-coller
   avec des `[placeholders]` entre crochets pour les valeurs à remplir, qui pousse Claude à
   appeler cet outil. Si non (beaucoup d'actions d'onboarding/UI n'ont pas d'équivalent
   MCP) : ne pas fabriquer de prompt, laisser `claudePrompt` absent — la section correspondante
   reste masquée sur le site (comportement déjà géré par le template).
4. Envoyer un prompt Lovable de la forme "Ajoute un tutoriel dans `src/data/tutorials.ts`,
   module `<moduleSlug>` : ```ts { ... }```" via `mcp__Lovable__send_message` sur le
   `project_id` ci-dessus (**ne jamais recréer de projet** — toujours réutiliser celui-ci).
5. Noter l'entrée dans le tableau "Tutoriels publiés" plus bas.

⚠️ `send_message` et `create_project` mettent régulièrement plus de 60s à répondre côté outil
(timeout client), **mais le message est bien reçu et traité côté Lovable** — ne pas renvoyer
le même prompt en double sur un timeout. Vérifier avec `get_project` (le `latest_commit_sha`
avance) ou `read_file` sur `src/data/tutorials.ts` avant de renvoyer quoi que ce soit.

## Modèle de données (`src/data/tutorials.ts`)

```ts
type Tutorial = {
  slug: string;
  title: string;
  moduleSlug: string;        // voir liste des modules ci-dessous
  subcategory: string;       // nom exact du sous-dossier Drive
  videoUrl: string;          // URL S3 RapidoCMS
  thumbnailUrl: string;      // URL S3 RapidoCMS (= la carte d'intro de la vidéo)
  durationSeconds: number;
  howItWorks: string[];
  whatItsFor: string;
  claudePrompt?: string;     // optionnel — voir étape 3 ci-dessus
  claudePrompts?: { title: string; prompt: string }[]; // optionnel — plusieurs exemples
                              // (ex: création directe + depuis une facture/image).
                              // Si présent, remplace claudePrompt (un seul des deux
                              // s'affiche, voir tutoriel.$slug.tsx). Ajouté le 2026-08-02
                              // pour saisir-ses-ingredients (create_ingredient direct +
                              // prompt "facture fournisseur (image)").
  chefTip?: string;
  chefTipAvatar?: string;    // optionnel — URL image, remplace l'icône chef par défaut
                              // sur l'astuce du chef de CE tutoriel (ex: vraie photo de
                              // Michael en chef, michael-chef-mascot.jpg). Par défaut
                              // (absent) : icône générique chefIcon.
};
```

## Les 14 modules / 11 catégories (mis à jour 2026-08-03 — remplace l'ancienne liste à 5 modules)

Le site a été réorganisé (nouveaux types `Category` + `Module.categorySlug` dans
`tutorials.ts`) pour coller au catalogue cible de 157 vidéos. Détail complet, intitulés des
157 vignettes et code couleur : `videos/CATALOGUE-157-TUTORIELS.md`. Les 5 modules déjà
existants gardent leur `moduleSlug` d'origine pour ne pas casser les tutoriels publiés.

| moduleSlug | Nom | Catégorie | Vidéos attendues |
|---|---|---|---:|
| `configuration` | Configuration Boutique | Configuration Boutique | 14 |
| `equipe-planning` | Équipe, Planning & RH | Équipe, Planning & RH | 20 |
| `site-web-vitrine` | Site Web & Vitrine | Site Web & Vitrine | 8 |
| `caisse-pos` | Caisse POS & Matériel | Caisse POS & Matériel | 7 |
| `hubrise-livraisons` | HubRise & Livraisons | HubRise & Livraisons | 4 |
| `caroline-ia` | Agent IA Caroline | Agent IA Caroline & Salle | 6 |
| `reservation-salle` | Réservations & Plan de salle | Agent IA Caroline & Salle | 5 |
| `service-commande` | Service Multi-Canal | Flux de Service & KDS | 3 |
| `kds-cuisine` | Écran Cuisine (KDS) | Flux de Service & KDS | 3 |
| `marketing-fidelite` | Marketing, Fidélité & Iris | Marketing, Fidélité & Iris | 24 |
| `stockvision-ai` | StockVision AI | StockVision AI | 20 |
| `haccp` | Hygiène & HACCP | Hygiène & HACCP | 30 |
| `comptabilite` | Comptabilité & Achats | Comptabilité & PrediBot | 10 |
| `predibot` | PrediBot (Agent IA Directeur) | Comptabilité & PrediBot | 3 |
| | | **Total** | **157** |

## Charte graphique appliquée au site

- Couleurs : fond crème `#FCF9E6`, texte marine `#0F1A23`, bleu `#007BFF`, orange `#FFA500`.
- Règle de contraste : texte marine sur fond clair, texte blanc sur fond bleu/orange/marine —
  jamais de texte orange sur fond clair (contraste insuffisant).
- Police : Goodly (marque, fichier réel non fourni) → Poppins/Fredoka en substitut.
- Logos officiels (`studio-video/assets/brand/logo-v2/`, poussés sur la branche
  `claude/107-tutorial-videos-feasibility-p170aw`) :
  - `foodeatup-logo-horizontal-mascot.png` — header, usage principal.
  - `foodeatup-mark-8.png` — favicon / petits espaces.
  - `foodeatup-logo-on-blue-card.png` — hero/bannières sur fond bleu.
- Règles d'usage strictes : jamais de bordure/rotation/recoloration/déformation, taille mini
  70px, zone de protection = demi-hauteur du logo tout autour.
- Motif de marque : silhouette arrondie de la toque du chef, utilisée en décoration de fond
  (composant `src/components/chef-hat-pattern.tsx` sur le site).
- Charte complète : `studio-video/assets/brand/Charte_FoodEatUp-v2.pdf` (33 pages, fournie
  par Michael le 2026-08-02, fait foi sur toute charte antérieure).

## Assets de marque supplémentaires (ajoutés le 2026-08-02)

- **Logos IA** (`studio-video/assets/brand/third-party-logos/`) : Claude, Mistral, OpenAI,
  WhatsApp — pour les blocs "Utiliser avec Claude" (site) et la séquence de fin des vidéos
  (voir règle dans `FOODEATUP-TUTORIELS-WORKFLOW.md`).
- **Photo de Michael** (`studio-video/assets/brand/profile/michael-kebail.jpg`) et sa
  version transformée en chef FoodEatUp par IA
  (`studio-video/assets/brand/profile/michael-chef-mascot.jpg`, générée via
  `mcp__RapidoCMS__images_to_image`) — ressemblance bien conservée, tablier FoodEatUp intégré.
  Utilisable pour une page "à propos"/fondateur sur le site.
- **11 captures d'écran produit réelles** (`studio-video/assets/brand/product-screenshots/`) :
  pointage, demande d'absence, ajout d'équipement, checklist hygiène, création de rôle, ajout
  d'employé, ajout de fournisseur, créer un devis, ajouter un client, dashboard productions,
  accueil HACCP. Référence pour associer chaque futur tutoriel à son outil MCP FoodEatUp.

## Avatar HeyGen — statut (2026-08-02, mis à jour)

Demandé : générer des vidéos d'avatar 3D HeyGen avec Michael en chef de cuisine, en mini
séquences muettes en début de vidéo (voix ElevenLabs uniquement, pour garder une seule voix
cohérente sur toute la série).

Michael a fourni une clé API HeyGen. **Testée, mais inutilisable dans cet environnement** :
`api.heygen.com` (et tous ses sous-domaines : `app.`, `upload.`, `resource.`) sont bloqués par
la politique réseau — refus de politique explicite (403 au CONNECT), pas une panne passagère.
Contrairement à ElevenLabs, il n'existe **aucun MCP qui relaie les appels HeyGen côté serveur**
dans cette session — le connecteur `HyperFrames_by_HeyGen` disponible ici n'est pas un
générateur d'avatar humain (moteur d'animation HTML/CSS sans rapport, ses propres instructions
le précisent). Donc même avec la clé, aucun appel direct n'est possible depuis ce conteneur.

**Chemin qui fonctionne** : Michael génère lui-même le/les clip(s) avatar sur `app.heygen.com`
(comme il le fait déjà pour les clips "Script N ..._1080p.mp4" du Drive) et les dépose dans le
chat comme n'importe quel autre asset. Le pipeline sait déjà gérer ce cas : pour une séquence
muette, extraire/couper la piste audio du clip HeyGen (`ffmpeg -an`) et ne garder que
l'image — la voix ElevenLabs prend le relais sur toute la narration, sans conflit. C'est
l'inverse exact du traitement appliqué sur `foodeatup-boutique-tuto` (où la voix native de
l'avatar était conservée) : ici la voix native est explicitely coupée.

## Tutoriels publiés

| # | Module | Sous-catégorie | Slug | claudePrompt ? |
|---|---|---|---|---|
| 1 | Configuration | 1 - Inscription, e-mail de confirmation | `creer-son-compte` | non — pas d'outil MCP (signup) |
| 2 | Configuration | 2 - monte votre boutique | `monter-sa-boutique` | non — pas d'outil MCP (fiche boutique) |
| 3 | Configuration | 3 - choisit votre abonnement | `choisir-son-abonnement` | non — pas d'outil MCP (paiement Stripe) |
| 4 | Configuration | 4 - profil entreprise | `configurer-son-profil-entreprise` | non — pas d'outil MCP (fiche identité entreprise) |
| 5 | Configuration | 5 - vos taux de TVA | `parametrer-sa-tva` | **oui** — `create_tva`. v3 validée par Michael le 2026-08-02 (script VO + séquence Claude animée 3 temps, module partagé) — publiée : RapidoCMS mis à jour (même URL S3, `durationSeconds` 29→38 sur Lovable) |
| 6 | Configuration | 6 - créer ses catégories | `creer-ses-categories` | **oui** — `create_category`. Validée et publiée le 2026-08-02 (RapidoCMS + LinkedIn 2026-08-05 16h + Lovable) |
| 7 | Configuration | 7 - ajouter ses fournisseurs | `ajouter-ses-fournisseurs` | **oui** — `create_supplier`. Validée et publiée le 2026-08-02 (RapidoCMS + LinkedIn 2026-08-06 07h + Lovable). Astuce du chef documente aussi l'affiliation produits/factures et l'OCR (capacités non montrées dans le rush lui-même) |
| 8 | Configuration | 8 - saisir ses ingrédients | `saisir-ses-ingredients` | **oui, 2 prompts** — `create_ingredient` (direct) + prompt "facture fournisseur (image)". Première vidéo à utiliser `claudePrompts[]` (nouveau champ, plusieurs exemples) et `chefTipAvatar` (photo réelle de Michael). Publiée le 2026-08-02 (RapidoCMS + LinkedIn 2026-08-07 07h + Lovable) |
| 9 | Configuration | 9 - régler ses unités | `regler-ses-unites` | non — `list_units` seul existe (lecture seule), pas de `create_unit`. Publiée le 2026-08-02 (RapidoCMS + LinkedIn 2026-08-06 16h + Lovable) |
| 10 | Configuration | 9 - créer ses produits | `creer-ses-produits` | **oui, 2 prompts** — `create_product` (direct) + prompt "photo du code-barres". Rush sans UI d'affiliation recette/ingrédient (et `create_product` n'a pas ce champ non plus) : logique métier (produit avec/sans recette → ce que la liste de courses ajoute) documentée en `chefTip` sur explication de Michael, pas inventée à l'écran. Publiée le 2026-08-02 (RapidoCMS + LinkedIn 2026-08-07 16h + Lovable) |
| 11 | Configuration | 13 - votre vitrine en ligne | `ouvrir-sa-vitrine-en-ligne` | **oui** — pas d'outil MCP de configuration de vitrine à proprement parler ; le `claudePrompt` documente le geste équivalent (template + couleurs + publication). Hébergée en raw GitHub (`videos/foodeatup-vitrine-tuto/out/`, branche `claude/foodeatup-academy-tutorials-n04713`) plutôt que RapidoCMS. Ajoutée sur Lovable le 2026-08-03 |
| 12 | Équipe & Planning | 1 - ajouter ses employés | `ajouter-ses-employes` | **oui** — `create_employee`. Première vidéo du module Équipe & Planning. Hébergée en raw GitHub (`videos/foodeatup-employes-tuto/out/`, branche `claude/foodeatup-tutorial-video-difgjz`) — RapidoCMS non authentifié dans cette session. Validée par le demandeur et publiée le 2026-08-03 (Lovable uniquement ; pas de RapidoCMS/LinkedIn) |
| 13 | Équipe & Planning | 2 - établir un contrat et son salaire | `etablir-son-contrat-et-son-salaire` | **oui** — `create_employee_contract`. Deuxième vidéo produite du module Équipe & Planning (suite d'« ajouter ses employés »). Indemnité transport, détails salaire/avantages, durée/précisions et document contractuel visibles dans le rush mais sans champ MCP correspondant — non repris dans le `claudePrompt` (même logique que `creer-ses-produits`). `chefTip` enrichi le 2026-08-03 à la demande de Michael (3 conseils : solde de congés auto, toujours joindre le contrat signé, penser à la date de fin pour un CDD). Hébergée en raw GitHub (`videos/foodeatup-contrat-tuto/out/`, branche `claude/foodeatup-tutorial-video-vn7udf`) — RapidoCMS non authentifié dans cette session. Validée par Michael et publiée le 2026-08-03 (Lovable uniquement ; pas de RapidoCMS/LinkedIn) |
| 14 | Équipe & Planning | 2 - assigner les tâches | `assigner-les-taches` | **oui, 3 prompts** — `assign_task` (`category` en champ libre). Création d'une tâche, modification (changement de récurrence) et complétion. Montage resserré à 41,9s à la demande de Michael (v1 à 49,9s). Hébergée en raw GitHub (`videos/foodeatup-taches-tuto/out/`, branche `claude/foodeatup-tutorial-video-difgjz`). Validée et publiée le 2026-08-03 (Lovable uniquement ; pas de RapidoCMS/LinkedIn) |
| 15 | Équipe & Planning | 3 - brancher Jarvis et son jeton | `brancher-jarvis-et-son-jeton` | non — aucun outil MCP FoodEatUp ne couvre l'appairage téléphone/QR (action physique de l'employé, pas automatisable). Activer Jarvis sur une fiche employé (onglet Jarvis), jeton/QR généré, gestion des sièges par Module Service > Jarvis (stats, tags de permission par rôle, "Générer" pour un nouvel employé). Introduit un module partagé `videos/_shared/jarvis_voice_sequence.py` (mini-animation 2 étages : sièges par rôle/permissions + contrôle vocal) qui remplace la séquence "Utiliser avec Claude" quand aucun outil MCP ne correspond. Hébergée en raw GitHub (`videos/foodeatup-jarvis-tuto/out/`, branche `claude/foodeatup-tutorial-video-vn7udf`) — RapidoCMS non authentifié dans cette session. Demande explicite de Michael de produire et publier en une fois (2026-08-03) : publiée directement (Lovable uniquement ; pas de RapidoCMS/LinkedIn) |
| 16 | Équipe & Planning | 3 - créer son code PIN | `creer-son-code-pin` | non — aucun outil MCP FoodEatUp ne couvre la gestion des codes PIN employé. Définir un code PIN (pointage + accès logiciel scopé au rôle) ; le QR code de la même page sert à l'appairage Bluetooth Jarvis. `chefTip` à tonalité sécurité (confidentialité du code, redéfinition si compromis, principe de moindre privilège via le rôle). VO réécrite courte dès le premier montage (23,3s) suite au retour sur le rythme du tuto précédent. Hébergée en raw GitHub (`videos/foodeatup-pin-jarvis-tuto/out/`, branche `claude/foodeatup-tutorial-video-difgjz`). Validée et publiée le 2026-08-03 (Lovable uniquement ; pas de RapidoCMS/LinkedIn) |
| 17 | Équipe & Planning | 3 - installer la borne d'accueil | `installer-la-borne-daccueil` | non — même raisonnement que `brancher-jarvis-et-son-jeton`/`creer-son-code-pin` : l'appairage borne/PIN est une action libre-service de l'employé sur une tablette partagée (scan de QR public, saisie du PIN), sans équivalent MCP. Rush = capture Chrome réelle (1920x1020 @60fps, chrome navigateur rogné en `1920x822` dans `build.py`) de la page kiosk publique : "Qui êtes-vous ?" → sélection profil → PIN 4 chiffres → "Pointer" ou "Mon espace" → grille de modules limitée au rôle. Segments initialement bien trop courts pour les VO générées (jusqu'à 9,3s de dérive) — corrigé en élargissant intro/A/C/D/F/G avant de re-livrer. Hébergée en raw GitHub (`videos/foodeatup-borne-tuto/out/`, branche `claude/foodeatup-tutorial-video-vn7udf`) — RapidoCMS non authentifié dans cette session. Demande explicite de Michael de produire et publier avec astuces du chef (2026-08-03) : publiée directement (Lovable uniquement ; pas de RapidoCMS/LinkedIn) |
| 18 | Équipe & Planning | 6 - Affichages et impression du planning par employé ou par poste | `imprimer-son-planning-par-poste` | **oui, 3 prompts** — `create_shift` (direct) + 2 prompts sans équivalent visuel dans le rush : « ajuster selon l'affluence » (`get_daily_brief`) et « anticiper les commandes » (`list_top_productions`). Rush dense (83s) resserré sur le fil du titre. Hébergée en raw GitHub (`videos/foodeatup-planning-poste-tuto/out/`, branche `claude/foodeatup-academy-tutorials-n04713`). Validée et publiée sur Lovable le 2026-08-03 — RapidoCMS/LinkedIn en attente |
| 19 | Équipe & Planning | 8 - Configuration et génération du QR code de pointage | `generer-qr-code-pointage` | non — configuration de sécurité anti-fraude (niveau de sécurité, géolocalisation, PIN/badge), aucun outil MCP FoodEatUp ne la couvre (volontairement). `howItWorks` (8 étapes) et `chefTip` particulièrement détaillés à la demande explicite de Michael. Hébergée en raw GitHub (`videos/foodeatup-qrcode-pointage-tuto/out/`, branche `claude/foodeatup-academy-tutorials-n04713`). Validée et publiée sur Lovable le 2026-08-03 — RapidoCMS/LinkedIn en attente |
| 20 | Équipe & Planning | 12 - Historique des pointages | `retrouver-les-pointages-historique` | **oui, 3 prompts** — dashboard/anomalies/écarts planning vs réel sur les mêmes données que la page. Hébergée en raw GitHub (`videos/foodeatup-historique-pointage-tuto/out/`, branche `claude/foodeatup-academy-tutorials-n04713`). Validée et publiée sur Lovable le 2026-08-03 — RapidoCMS/LinkedIn en attente |
| 21 | *(transversal, hors module produit)* | Connecter son MCP à Claude, Mistral, ChatGPT | `brancher-son-mcp-sur-claude` | pas de `claudePrompt` — cette vidéo EST déjà le mode d'emploi "utiliser avec Claude". Nouveau composant homepage `McpHighlight` (`src/components/mcp-highlight.tsx`) ajouté par l'agent Lovable, rattaché au module `configuration`. Hébergée en raw GitHub (`videos/foodeatup-mcp-tuto/out/`, branche `claude/foodeatup-academy-tutorials-n04713`). Validée et publiée sur Lovable le 2026-08-03 — RapidoCMS/LinkedIn en attente |
| 22 | Équipe & Planning | 14 - découvrir son accueil selon son rôle | `decouvrir-son-accueil-selon-son-role` | **oui, 2 prompts** — `create_employee` (rôle existant) + `update_employee` (réaffectation de rôle). Aucun outil MCP pour la création d'un rôle personnalisé (action UI uniquement, Équipe > Rôles > Créer un rôle) : documentée en `chefTip`, non fabriquée en `claudePrompt`. Rush : espace personnel manager → Équipe > Rôles → liste des rôles → modale de permissions par module → HACCP (0/41) pour le rôle manager → retour accueil recalculé. `chefTip` enrichi à la demande explicite de Michael avec plusieurs cas d'usage par métier (chef de partie, second de cuisine, serveur, directeur) : stagiaire hérite d'un rôle existant, création du rôle "Second de cuisine" avec permissions dédiées, réaffectation de rôle lors d'un changement de poste. Segments initialement trop courts pour les VO générées (2 à 4,3s de dérive) — corrigé en élargissant intro/B/C/E/H/I ; dérive nulle après correction. Hébergée en raw GitHub (`videos/foodeatup-accueil-role-tuto/out/`, branche `claude/foodeatup-tutorial-video-vn7udf`) — RapidoCMS non authentifié dans cette session. Validée et publiée sur Lovable le 2026-08-03 (Lovable uniquement ; pas de RapidoCMS/LinkedIn) |
| 23 | Équipe & Planning | 17 - poser un congé côté employé | `poser-un-conge-cote-employe` | non — `approve_leave`/`reject_leave`/`list_leaves` sont tous des actions côté manager ; aucun outil MCP pour la création d'une demande de congé côté employé (self-service). Première vidéo de la série tournée côté espace employé plutôt que côté back-office manager, à la demande explicite de Michael (« maintenant tu te place comme un employé »). Rush : tableau de bord solde de congés (acquis/soldé/pris/en attente) → demande "Congés payés" déjà en attente → nouvelle demande "Congé personnel" (unité Jours, dates de début/fin, pièce jointe optionnelle) → envoi, badge "En attente" et solde mis à jour. Segments dimensionnés dès le premier montage à partir des VO mesurées (dérive initiale 0,3–0,9s, deux ajustements ciblés → dérive nulle). Hébergée en raw GitHub (`videos/foodeatup-conge-employe-tuto/out/`, branche `claude/foodeatup-tutorial-video-vn7udf`) — RapidoCMS non authentifié dans cette session. Validée et publiée sur Lovable le 2026-08-03 (Lovable uniquement ; pas de RapidoCMS/LinkedIn) |
| 24 | Équipe & Planning | 4 - régler ses horaires par employé | `regler-ses-horaires-par-employe` | **oui** — `update_employee_schedule` (remplace le planning hebdomadaire complet). Rush : fiche employé → horaires actuels (lundi 8h-17h, 1h de pause) → modale d'édition → ajout d'un créneau (mardi), heures ajustées pour rejoindre le lundi → sauvegarde. `claudePrompt` exploite la lecture d'image native de Claude pour configurer les horaires à partir d'une photo d'un planning papier, à la demande explicite de Michael (message du 2026-08-03, avec le cas d'usage "ajuster selon l'affluence" repris en `chefTip`). Dérive nulle dès le premier montage (segments dimensionnés directement à partir des VO mesurées). Hébergée en raw GitHub (`videos/foodeatup-horaires-tuto/out/`, branche `claude/foodeatup-tutorial-video-vn7udf`). Publiée sur Lovable le 2026-08-03 |
| 25 | Équipe & Planning | 10 - commander ses cartes NFC pour le badge | `commander-ses-cartes-nfc` | non — commande de matériel physique (cartes PVC + puce NFC, impression via un prestataire externe Printags), aucun outil MCP correspondant. Rush : page de pointage → section Badges NFC & cartes marketing (2,50€/carte) → génération d'un identifiant de badge pour un employé → commande groupée (sélection des employés, prix calculé) → confirmation. Dérive nulle après un seul ajustement (segments C/E/G/I élargis). Hébergée en raw GitHub (`videos/foodeatup-nfc-tuto/out/`, branche `claude/foodeatup-tutorial-video-vn7udf`). Publiée sur Lovable le 2026-08-03 |
| 26 | Équipe & Planning | 19 - retrouver ses documents, paie et contrat | `retrouver-ses-documents-paie-et-contrat` | non — `update_employee` ne couvre que prénom/nom/email/téléphone/rôle (pas l'état civil, la sécurité sociale, le RIB ou le contact d'urgence montrés dans le rush) et `list_employee_documents` est une lecture seule côté manager ; aucun outil pour l'édition détaillée du profil ni l'import de documents côté employé (self-service). Rush : espace "Mon coin RH" → menu avatar → Profil (aperçu contrat) → Informations personnelles (état civil/coordonnées/santé, modifiables) → onglet Contrat ("Voir plus" : temps de travail, rémunération, primes/indemnités) → onglet Documents (carte identité, contrat de travail, import PDF/JPG/PNG). Dérive nulle dès le premier montage. Hébergée en raw GitHub (`videos/foodeatup-documents-tuto/out/`, branche `claude/foodeatup-tutorial-video-vn7udf`). Publiée sur Lovable le 2026-08-03 |
| 27 | Équipe & Planning | 18 - suivre ses performances côté employé | `suivre-ses-performances-cote-employe` | non — aucun outil MCP ne calcule/n'expose ce score de performance employé (métrique interne au produit, pas un endpoint API). Rush court (18,4s) : menu avatar → Performances → score global en anneau (131, "À améliorer") avec légende → classement de l'équipe (score + présence par employé, rang) → historique semaine par semaine. Dérive nulle après un seul ajustement (segments A/C/D élargis). Hébergée en raw GitHub (`videos/foodeatup-performances-tuto/out/`, branche `claude/foodeatup-tutorial-video-vn7udf`). Publiée sur Lovable le 2026-08-03 |
| 28 | **Comptabilité & Achats** *(nouveau module, première vidéo)* | 6 - changer les statuts d'une facture | `changer-les-statuts-dune-facture` | **oui** — `update_invoice_status` (transitions légales DGFiP : brouillon/en_attente/envoyee/acceptee/refusee/litige/payee/annulee). Rush : liste des factures (statuts, stats) → détail d'une facture → menu "Téléchargements et options" → "Marquer comme payée" → confirmation → statut mis à jour, stats actualisées. `chefTip` détaille l'usage des 8 statuts (notamment `litige` et `annulee`, jamais supprimer une facture pour la conformité). Dérive nulle dès le premier montage. Hébergée en raw GitHub (`videos/foodeatup-facture-statuts-tuto/out/`, branche `claude/foodeatup-tutorial-video-vn7udf`). Publiée sur Lovable le 2026-08-03 |

**Bilan module Équipe, Planning & RH au 2026-08-03** : 19/20 vidéos du catalogue publiées. Il manque uniquement #15 Pointer son Service — pauses & photo : le fichier fourni pour cette vidéo (à deux reprises) s'est révélé être un doublon du rush #14 (même taille en octets, 31 001 599, contenu vérifié identique — grille de modules "Mon espace", pas de pauses/pointage). En attente du bon fichier avant de pouvoir monter cette dernière vidéo et clore le module à 20/20.

**Fragmentation multi-session repérée le 2026-08-03** : au moins 3 branches ont produit des
tutoriels équipe-planning/configuration en parallèle sans se voir (`claude/foodeatup-tutorial-video-vn7udf`
— cette branche —, `claude/foodeatup-tutorial-video-difgjz`, `claude/foodeatup-academy-tutorials-n04713`),
d'où les doublons de numérotation `subcategory` ci-dessus (cosmétique — texte libre, pas de clé unique
côté site) et le retard de ce tableau sur le contenu réellement publié sur Lovable. `difgjz` a aussi
livré `monter-ses-recettes` (module `configuration`, sous-catégorie « 11 Monter ses recettes/fiches
techniques » du catalogue 157) — pas encore vérifié si présent sur Lovable au moment d'écrire cette
ligne. Voir `videos/CATALOGUE-157-TUTORIELS.md` (récupéré depuis `foodeatup-academy-tutorials-n04713`)
pour la cible complète : **157 vidéos, 14 modules, 11 catégories**. Avant de démarrer un nouveau
tutoriel, toujours relire `src/data/tutorials.ts` en direct sur Lovable (pas seulement ce tableau) pour
éviter de reproduire un sujet déjà couvert par une autre branche.
