# FoodEatUp Academy — site de documentation Lovable (mémoire du projet)

**À relire à chaque nouvelle vidéo produite.** Ce fichier est la source de vérité du site
Lovable qui documente les 91 tutoriels FoodEatUp. Chaque vidéo livrée doit se terminer par
l'ajout de son entrée ici (tableau "Tutoriels publiés" en bas) et l'envoi du prompt Lovable
correspondant au projet.

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

## Les 5 modules (catégories du site = catégories du Drive)

| moduleSlug | Nom | Vidéos attendues |
|---|---|---:|
| `configuration` | Configuration | 14 |
| `equipe-planning` | Équipe & Planning | 20 |
| `comptabilite` | Comptabilité | 10 |
| `haccp` | HACCP | 30 |
| `stockvision-ai` | StockVision AI | 20 |

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
| 11 | Configuration | 13 - votre vitrine en ligne | `ouvrir-sa-vitrine-en-ligne` | **oui** — combine `apply_site_template` + `set_site_theme` + `publish_site`. Première vidéo avec avatar HeyGen (voix native conservée sur l'accroche, `vo/N0.mp3`). Publiée sur Lovable le 2026-08-03 — **RapidoCMS/LinkedIn en attente** : le connecteur RapidoCMS n'est pas autorisé dans cette session, `videoUrl`/`thumbnailUrl` pointent temporairement sur le raw GitHub de la branche (`videos/foodeatup-vitrine-tuto/out/`) — à remplacer par les URLs S3 RapidoCMS dès que le connecteur est disponible, puis planifier LinkedIn. **⚠️ bandeaux d'étape invisibles** (bug `banner()` trouvé et corrigé sur le tuto suivant, voir #12) — vidéo à re-rendre si Michael valide |
| 12 | Configuration | 14 - votre QR code | `diffuser-son-qrcode` | **oui** — `update_section` (réseaux sociaux) ; QR/flyers/cartes sont des générations client-side sans outil MCP. Dernier tutoriel du module Configuration (12/12 dossiers Drive disponibles). Sans avatar HeyGen (retiré à la demande de Michael). Validée et publiée sur Lovable le 2026-08-03 — RapidoCMS/LinkedIn en attente (même raison que #11, URLs GitHub raw temporaires). **Bug `banner()` corrigé sur cette vidéo** : l'évaluateur d'expression `drawbox` de cet ffmpeg échoue silencieusement (bandeau invisible) en combinant un décalage constant avec deux clamps `min/max` soustraits — simplifié à un seul clamp (slide-in only), voir `SCRIPT.md` de ce tuto pour le détail |
| 13 | Équipe & Planning | 6 - Affichages et impression du planning par employé ou par poste | `imprimer-son-planning-par-poste` | **oui, 3 prompts** — `create_shift` (direct, l'action montrée à l'écran) + 2 prompts demandés par Michael sans équivalent visuel dans le rush : « ajuster selon l'affluence » (`get_daily_brief`) et « anticiper les commandes » (`list_top_productions`), documentés uniquement en `claudePrompts[]`/`chefTip` sur Lovable, pas dans le script vidéo. Rush dense (83 s) resserré sur le fil du titre — modif de shift et « Tâches de la semaine » laissés de côté. Sans avatar HeyGen. Validée et publiée sur Lovable le 2026-08-03 — RapidoCMS/LinkedIn en attente (URLs GitHub raw temporaires). Première vidéo du module Équipe & Planning produite dans cette session — **une autre session travaille en parallèle sur ce même module** (`ajouter-ses-employes`, `assigner-les-taches`, `etablir-son-contrat-et-son-salaire` déjà présents sur d'autres branches) : vérifier les doublons de sujet avant de choisir la prochaine sous-catégorie |
| 14 | *(transversal, hors module produit)* | Connecter son MCP à Claude, Mistral, ChatGPT | `brancher-son-mcp-sur-claude` | pas de `claudePrompt` — cette vidéo EST déjà le mode d'emploi "utiliser avec Claude", un exemple de prompt n'aurait pas de sens. Contenu demandé explicitement par Michael au-delà de la fiche standard : lien MCP (`https://foodeatup.com/api/mcp`, confirmé à l'écran), explication de ce à quoi sert le MCP, et redirections vers Claude/Mistral/ChatGPT (domaines racine `claude.ai`/`chat.mistral.ai`/`chatgpt.com` — pas de chemin de réglages profond deviné, seul Claude est montré dans le rush). **Nouveau composant homepage `McpHighlight`** (`src/components/mcp-highlight.tsx`) ajouté sur l'accueil juste après la section vidéo tutoriel, avec logos + liens vers les 3 assistants + CTA vers la fiche complète — implémenté par l'agent Lovable sur brief de contenu, rattaché au module `configuration`. Validée et publiée sur Lovable le 2026-08-03 — RapidoCMS/LinkedIn en attente |
| 15 | Équipe & Planning | 8 - Configuration et génération du QR code de pointage | `generer-qr-code-pointage` | non — configuration de sécurité anti-fraude (niveau de sécurité, géolocalisation, PIN/badge), aucun outil MCP FoodEatUp ne la couvre (volontairement : pas le genre d'action à déléguer à un agent). `howItWorks` (8 étapes) et `chefTip` particulièrement détaillés à la demande explicite de Michael, module jugé plus complexe que les autres (rayon de géoloc, tolérance hors-zone, différence QR/PIN/badge NFC, désactiver vs supprimer un QR). Sans avatar HeyGen, sans séquence Claude. Validée et publiée sur Lovable le 2026-08-03 — RapidoCMS/LinkedIn en attente (URLs GitHub raw temporaires) |
