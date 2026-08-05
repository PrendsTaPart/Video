# FoodEatUp Academy — site de documentation Lovable (mémoire du projet)

**À relire à chaque nouvelle vidéo produite.** Ce fichier documente le site Lovable qui
héberge la série de **157 tutoriels FoodEatUp** (somme des `expectedCount` du tableau
`modules` de `src/data/tutorials.ts` — voir le calcul dans
`videos/PROGRESSION-157-TUTORIELS.md`, qui est le tableau de suivi à jour : 71/157 publiés
au 2026-08-04). Chaque vidéo livrée doit se terminer par l'ajout de son entrée ici (tableau
"Tutoriels publiés" en bas, **qui a pris du retard sur le site réel — voir avertissement plus
bas**) et l'envoi du prompt Lovable correspondant au projet, puis par la mise à jour de
`videos/PROGRESSION-157-TUTORIELS.md`.
**À relire à chaque nouvelle vidéo produite.** Ce fichier est la source de vérité du site
Lovable qui documente les 157 tutoriels FoodEatUp (somme des `expectedCount` des 14
modules de `src/data/tutorials.ts` sur Lovable — chiffre confirmé par Michael le
2026-08-03). Chaque vidéo livrée doit se terminer par l'ajout de son entrée ici (tableau
"Tutoriels publiés" en bas) et l'envoi du prompt Lovable correspondant au projet.
Lovable qui documente les tutoriels FoodEatUp — cible **157 vidéos / 14 modules / 11
catégories**, voir `videos/CATALOGUE-157-TUTORIELS.md` pour le détail complet (mis à jour le
2026-08-03, remplace l'ancienne cible à 91-94 vidéos / 5 modules). Chaque vidéo livrée doit
se terminer par l'ajout de son entrée ici (tableau "Tutoriels publiés" en bas) et l'envoi du
prompt Lovable correspondant au projet. **Avant de choisir un sujet, vérifier `src/data/
tutorials.ts` en direct sur Lovable** (pas seulement ce tableau, souvent en retard) : plusieurs
branches produisent en parallèle sans se voir, voir la note de fragmentation dans le tableau
plus bas.
Lovable qui documente les tutoriels FoodEatUp. Chaque vidéo livrée doit se terminer par
l'ajout de son entrée ici (tableau "Tutoriels publiés" en bas) et l'envoi du prompt Lovable
correspondant au projet.

Le total de la série a été communiqué à 157 vidéos le 2026-08-04 (précédemment 91-94
d'après l'audit Drive du 2026-08-02) — voir `SUIVI-157-TUTORIELS.md` pour l'écart entre
les deux chiffres et ce qui reste à clarifier avec Michael avant de l'utiliser comme
référence de planification.

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

⚠️ **Ce projet Lovable est édité en concurrence par plusieurs sessions** (constaté le
2026-08-04 : `list_messages` a montré des messages d'autres sessions arrivant à quelques
secondes des miens, sur d'autres sujets HACCP). Conséquence : après un `send_message`,
`get_project`/`read_file` peut renvoyer l'état d'une édition concurrente plus récente que la
sienne (le `latest_commit_sha` avance à chaque édition, pas seulement la sienne) — ne pas
conclure à un échec sur cette seule base. Vérification fiable : `list_messages` pour retrouver
son propre tour (apparier user/assistant par timestamp), puis `get_diff(message_id=<id de la
réponse assistant>)` pour voir précisément ce que CE tour a changé, indépendamment des autres
éditions en cours.

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

## Architecture du site — 11 catégories / 14 modules (2026-08-03)

**Remplace la section "5 modules" ci-dessous, conservée en historique.** Suite au
catalogue des 157 tutoriels transmis par Michael (voir `CATALOGUE-157-TUTORIELS.md`),
un prompt Lovable unique a fait évoluer `src/data/tutorials.ts` avec deux nouveaux
types `Category` et `Module` (un module référence sa catégorie via `categorySlug`,
une catégorie porte juste `slug`/`name`/`color`). Commit `12fb06d2510edcdda4116f886a3d259f638559a8`.
| categorySlug | Nom catégorie | Couleur | Modules (slug — nom — vidéos attendues) |
|---|---|---|---|
| `configuration-boutique` | Configuration Boutique | `#0D6EFD` | `configuration` — Configuration Boutique — 14 |
| `equipe-planning-rh` | Équipe, Planning & RH | `#7C3AED` | `equipe-planning` — Équipe, Planning & RH — 20 |
| `site-web-vitrine` | Site Web & Vitrine | `#2563EB` | `site-web-vitrine` — Site Web & Vitrine — 8 |
| `caisse-pos` | Caisse POS & Matériel | `#EA580C` | `caisse-pos` — Caisse POS & Matériel — 7 |
| `hubrise-livraisons` | HubRise & Livraisons | `#06B6D4` | `hubrise-livraisons` — HubRise & Livraisons — 4 |
| `caroline-reservation` | Agent IA Caroline & Salle | `#F59E0B` | `caroline-ia` — Agent IA Caroline — 6 ; `reservation-salle` — Réservations & Plan de salle — 5 |
| `service-kds` | Flux de Service & KDS | `#059669` | `service-commande` — Service Multi-Canal — 3 ; `kds-cuisine` — Écran Cuisine (KDS) — 3 |
| `marketing-fidelite` | Marketing, Fidélité & Iris | `#EC4899` | `marketing-fidelite` — Marketing, Fidélité & Iris — 24 |
| `stockvision` | StockVision AI | `#10B981` | `stockvision-ai` — StockVision AI — 20 |
| `hygiene-haccp` | Hygiène & HACCP | `#DC2626` | `haccp` — Hygiène & HACCP — 30 |
| `comptabilite-predibot` | Comptabilité & PrediBot | `#475569` | `comptabilite` — Comptabilité & Achats — 10 ; `predibot` — PrediBot (Agent IA Directeur) — 3 |
Les 5 modules déjà en production (`configuration`, `equipe-planning`, `comptabilite`,
`haccp`, `stockvision-ai`) ont gardé leur `slug` exact et tous leurs tutoriels
existants — vérifié par lecture complète de `tutorials.ts` au commit ci-dessus, aucune
entrée des 15 tutoriels déjà publiés n'a été modifiée. 9 nouveaux modules vides ont été
ajoutés (`site-web-vitrine`, `caisse-pos`, `hubrise-livraisons`, `caroline-ia`,
`reservation-salle`, `service-commande`, `kds-cuisine`, `marketing-fidelite`,
`predibot`), prêts à recevoir leurs tutoriels au fil de la production — plus besoin
de toucher à l'architecture pour les prochaines vidéos, juste ajouter l'objet
`Tutorial` avec le bon `moduleSlug`.
Autres changements livrés dans le même prompt :
- `src/data/module-icons.ts` : icônes Lucide ajoutées pour les 9 nouveaux modules
  (Globe, CreditCard, Truck, Mic, CalendarCheck, UtensilsCrossed, MonitorSmartphone,
  Megaphone, Brain), fallback `BookOpen` conservé.
- `src/routes/index.tsx` : section modules de l'accueil regroupée par catégorie
  (en-tête coloré + puce + bordure gauche), cartes module teintées à la couleur de
  leur catégorie.
- `src/routes/module.$slug.tsx` : fil d'Ariane Accueil > Catégorie > Module, en-tête
  coloré à la catégorie, SEO (`head()` : title/description mentionnant la catégorie
  et le nombre de tutoriels, og:*, canonical).
- `src/routes/tutoriel.$slug.tsx` : SEO complet par tutoriel — title, meta description
  (`whatItsFor` tronqué à 158 car.), og:title/description/type(`video.other`)/url,
  twitter:card, `<link rel="canonical">`, JSON-LD `VideoObject` (name, description,
  thumbnailUrl, contentUrl, uploadDate constant `2026-01-01`, duration `PT{n}S`).
Vérifié par l'agent Lovable via `tsgo --noEmit` (aucune erreur de type) et captures
Playwright (accueil, une page module, une page tutoriel) avant de livrer le commit.
### Historique — 5 modules d'origine (avant le 2026-08-03)
## Les 14 modules (mis à jour le 2026-08-03 depuis `src/data/tutorials.ts` — la
## précédente liste de 5 modules ici était obsolète, cf. `modules` côté Lovable)
| moduleSlug | Nom | Vidéos attendues |
|---|---|---:|
| `configuration` | Configuration Boutique | 14 |
| `equipe-planning` | Équipe, Planning & RH | 20 |
| `site-web-vitrine` | Site Web & Vitrine | 8 |
| `caisse-pos` | Caisse POS & Matériel | 7 |
| `hubrise-livraisons` | HubRise & Livraisons | 4 |
| `caroline-ia` | Agent IA Caroline | 6 |
| `reservation-salle` | Réservations & Plan de salle | 5 |
| `service-commande` | Service Multi-Canal | 3 |
| `kds-cuisine` | Écran Cuisine (KDS) | 3 |
| `marketing-fidelite` | Marketing, Fidélité & Iris | 24 |
| `stockvision-ai` | StockVision AI | 20 |
| `haccp` | Hygiène & HACCP | 30 |
| `comptabilite` | Comptabilité & Achats | 10 |
| `predibot` | PrediBot (Agent IA Directeur) | 3 |
| **Total** | | **157** |
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

## Progression série (mise à jour 2026-08-04)

**56 / 157 tutoriels publiés** sur `src/data/tutorials.ts` (mise à jour 2026-08-04, après
publication de `retrouver-lhistorique-des-zones-de-nettoyage`) (157 = somme des `expectedCount` de
tous les modules — configuration 14, équipe-planning 20, site-web-vitrine 8, caisse-pos 7,
hubrise-livraisons 4, caroline-ia 6, reservation-salle 5, service-commande 3, kds-cuisine 3,
marketing-fidelite 24, stockvision-ai 20, haccp 30, comptabilite 10, predibot 3). Décompte exact
par module visible en direct sur le site (barres de progression "X / Y vidéos" par module,
page d'accueil). Cette table ne relogue pas rétroactivement chaque vidéo déjà publiée avant sa
mise en place (l'historique complet reste dans les messages `git log` de ce dépôt) — elle est
tenue à jour à partir d'ici pour chaque nouvelle vidéo.

## Tutoriels publiés

**Note (2026-08-04)** : ce tableau n'était plus synchronisé avec le site — `src/data/tutorials.ts`
contient déjà **80 tutoriels** répartis sur 7 modules (`configuration` 15, `equipe-planning` 19,
`comptabilite` 10, `haccp` 14→15 avec l'ajout ci-dessous, `stockvision-ai` 7, `predibot` 2,
`hubrise-livraisons` 1) — bien au-delà des 10 lignes listées ici et du chiffre de 91/92 vidéos
« productibles » audité dans `FAISABILITE-SERIE-TUTORIELS.md` (qui ne couvrait que les 5 modules
du Drive d'origine, pas `predibot`/`hubrise-livraisons` ajoutés depuis). Aucune trace dans le
dépôt d'un chiffre de 157 vidéos — à clarifier avec Michael si ce nombre doit devenir la cible
officielle. Ce tableau reste tenu à jour pour les vidéos produites *depuis ce dépôt*, mais n'est
plus la source de vérité du nombre total de tutoriels publiés (c'est `tutorials.ts` sur Lovable).
⚠️ Ce tableau est en retard sur `src/data/tutorials.ts` (constaté le 2026-08-04 : le fichier
compte déjà 20 entrées `moduleSlug: "haccp"` en plus des 10 lignes Configuration ci-dessous,
publiées par d'autres sessions/branches). Ne pas se fier au tableau seul pour connaître l'état
réel du site — vérifier `src/data/tutorials.ts` via `mcp__Lovable__read_file`.

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
| 11 | StockVisionAI | Suivre ses livraisons : statuts et dates | `suivre-ses-livraisons` | non — `list_deliveries` seul existe (lecture seule) pour les livraisons fournisseurs ; `update_order_status` existe mais s'applique aux commandes clients, objet différent. Validée par Michael le 2026-08-04. Publiée sur Lovable le 2026-08-04 (RapidoCMS mis à jour comme hébergement du MP4/vignette ; LinkedIn non demandé pour l'instant) |
| 12 | HACCP | Créer et valider une checklist hygiène | `creer-sa-checklist-hygiene` | **oui, 2 prompts** — `create_hygiene_checklist` (création) + `create_hygiene_checklist_validation` (validation). Séquence Claude vidéo sur le prompt de création ; `claudePrompts[]` Lovable avec les 2 prompts (même pattern que `saisir-ses-ingredients`). Validée par Michael le 2026-08-04 (dérive VO recalibrée avant livraison : <1s partout contre ~9s dans un premier montage). Publiée le 2026-08-04 : RapidoCMS (vidéo + vignette), LinkedIn programmé 2026-08-16 07h (rotation 2/j déjà pleine jusqu'au 15/08), Lovable |
| 11 | Configuration | 10 - ouvrir sa vitrine en ligne | `ouvrir-sa-vitrine` | **oui** — `apply_site_template` + `set_site_theme` + `publish_site` combinés en un seul prompt (correspond exactement au flux montré : template → charte → publication). Premier avatar depuis `foodeatup-boutique-tuto`. RapidoCMS + Lovable publiés le 2026-08-03 (LinkedIn non demandé cette fois — à programmer sur demande) |
| 11 | HACCP | 10 - Ajouter et paramétrer un plan de nettoyage | `parametrer-son-plan-de-nettoyage` | **oui** — `create_cleaning_zone`. Validée et publiée le 2026-08-04 (RapidoCMS + LinkedIn programmé 2026-08-16 07h, file pleine jusqu'au 15/08 + Lovable, insérée après `pointer-ses-actions-de-nettoyage`) |

**Écart constaté le 2026-08-04** : `src/data/tutorials.ts` sur Lovable contient déjà des
entrées (ex. `pointer-ses-actions-de-nettoyage`, module HACCP #11 "Éditer votre plan de
nettoyage chaque jour", et d'autres — recettes, vitrine, QR code, MCP, RH...) absentes de
ce tableau et de tout dossier `videos/foodeatup-*` de ce dépôt. Le site est en avance sur
ce suivi local ; le tableau ci-dessus ne couvre que les vidéos produites **depuis ce
dépôt**, pas l'état réel complet de `tutorials.ts`. À rapprocher de la question du total
de 157 vidéos posée par Michael le 2026-08-04 (non résolue) — voir aussi le calendrier
LinkedIn RapidoCMS, déjà rempli jusqu'au 2026-08-15 avec des tutoriels (employés, planning,
pointage, contrats...) qui n'ont eux non plus aucune trace dans ce dépôt.
| 11 | Configuration | 13 - votre vitrine en ligne | `ouvrir-sa-vitrine-en-ligne` | **oui** — combine `apply_site_template` + `set_site_theme` + `publish_site`. Première vidéo avec avatar HeyGen (voix native conservée sur l'accroche, `vo/N0.mp3`). Publiée sur Lovable le 2026-08-03 — **RapidoCMS/LinkedIn en attente** : le connecteur RapidoCMS n'est pas autorisé dans cette session, `videoUrl`/`thumbnailUrl` pointent temporairement sur le raw GitHub de la branche (`videos/foodeatup-vitrine-tuto/out/`) — à remplacer par les URLs S3 RapidoCMS dès que le connecteur est disponible, puis planifier LinkedIn. **⚠️ bandeaux d'étape invisibles** (bug `banner()` trouvé et corrigé sur le tuto suivant, voir #12) — vidéo à re-rendre si Michael valide |
| 12 | Configuration | 14 - votre QR code | `diffuser-son-qrcode` | **oui** — `update_section` (réseaux sociaux) ; QR/flyers/cartes sont des générations client-side sans outil MCP. Dernier tutoriel du module Configuration (12/12 dossiers Drive disponibles). Sans avatar HeyGen (retiré à la demande de Michael). Validée et publiée sur Lovable le 2026-08-03 — RapidoCMS/LinkedIn en attente (même raison que #11, URLs GitHub raw temporaires). **Bug `banner()` corrigé sur cette vidéo** : l'évaluateur d'expression `drawbox` de cet ffmpeg échoue silencieusement (bandeau invisible) en combinant un décalage constant avec deux clamps `min/max` soustraits — simplifié à un seul clamp (slide-in only), voir `SCRIPT.md` de ce tuto pour le détail |
| 13 | Équipe & Planning | 6 - Affichages et impression du planning par employé ou par poste | `imprimer-son-planning-par-poste` | **oui, 3 prompts** — `create_shift` (direct, l'action montrée à l'écran) + 2 prompts demandés par Michael sans équivalent visuel dans le rush : « ajuster selon l'affluence » (`get_daily_brief`) et « anticiper les commandes » (`list_top_productions`), documentés uniquement en `claudePrompts[]`/`chefTip` sur Lovable, pas dans le script vidéo. Rush dense (83 s) resserré sur le fil du titre — modif de shift et « Tâches de la semaine » laissés de côté. Sans avatar HeyGen. Validée et publiée sur Lovable le 2026-08-03 — RapidoCMS/LinkedIn en attente (URLs GitHub raw temporaires). Première vidéo du module Équipe & Planning produite dans cette session — **une autre session travaille en parallèle sur ce même module** (`ajouter-ses-employes`, `assigner-les-taches`, `etablir-son-contrat-et-son-salaire` déjà présents sur d'autres branches) : vérifier les doublons de sujet avant de choisir la prochaine sous-catégorie |
| 14 | *(transversal, hors module produit)* | Connecter son MCP à Claude, Mistral, ChatGPT | `brancher-son-mcp-sur-claude` | pas de `claudePrompt` — cette vidéo EST déjà le mode d'emploi "utiliser avec Claude", un exemple de prompt n'aurait pas de sens. Contenu demandé explicitement par Michael au-delà de la fiche standard : lien MCP (`https://foodeatup.com/api/mcp`, confirmé à l'écran), explication de ce à quoi sert le MCP, et redirections vers Claude/Mistral/ChatGPT (domaines racine `claude.ai`/`chat.mistral.ai`/`chatgpt.com` — pas de chemin de réglages profond deviné, seul Claude est montré dans le rush). **Nouveau composant homepage `McpHighlight`** (`src/components/mcp-highlight.tsx`) ajouté sur l'accueil juste après la section vidéo tutoriel, avec logos + liens vers les 3 assistants + CTA vers la fiche complète — implémenté par l'agent Lovable sur brief de contenu, rattaché au module `configuration`. Validée et publiée sur Lovable le 2026-08-03 — RapidoCMS/LinkedIn en attente |
| 15 | Équipe & Planning | 8 - Configuration et génération du QR code de pointage | `generer-qr-code-pointage` | non — configuration de sécurité anti-fraude (niveau de sécurité, géolocalisation, PIN/badge), aucun outil MCP FoodEatUp ne la couvre (volontairement : pas le genre d'action à déléguer à un agent). `howItWorks` (8 étapes) et `chefTip` particulièrement détaillés à la demande explicite de Michael, module jugé plus complexe que les autres (rayon de géoloc, tolérance hors-zone, différence QR/PIN/badge NFC, désactiver vs supprimer un QR). Sans avatar HeyGen, sans séquence Claude. Validée et publiée sur Lovable le 2026-08-03 — RapidoCMS/LinkedIn en attente (URLs GitHub raw temporaires) |
| 16 | Équipe & Planning | 12 - Historique des pointages | `retrouver-les-pointages-historique` | **oui, 3 prompts** — tous basés sur `list_attendances` (dashboard période, détection retards/absences, comparaison au planning prévu), demandés explicitement par Michael en cas d'usage. Sans avatar HeyGen. Rush très court (18,64 s), vidéo proportionnellement plus courte (33,36 s). Validée et publiée sur Lovable le 2026-08-03 — RapidoCMS/LinkedIn en attente (URLs GitHub raw temporaires) |
| 17 | Équipe & Planning | 1 - Configuration des rôles et permissions | `creer-ses-roles-et-permissions` | **oui, 3 prompts** — tous basés sur `list_attendances` (pauses d'un employé, pauses anormales, résumé quotidien), aucun outil MCP ne couvre l'édition d'un rôle/permission elle-même. **Rush mal étiqueté côté Drive** : le fichier envoyé pour le dossier 15 (« Gestion des pauses, pointage entrée et sortie et Empreinte photo du pointage ») enregistre en réalité l'écran Rôles/Permissions du dossier 1 (vérifié via taille de fichier identique sur Google Drive) — vidéo publiée sous l'angle « rôles et permissions » avec l'accord de Michael, en racontant le contrôle du pointage (pauses/photo) par le patron/directeur via les permissions. Sans avatar HeyGen. Validée et publiée sur Lovable le 2026-08-03 (commit `b5d6792e`) — RapidoCMS/LinkedIn en attente (URLs GitHub raw temporaires) |
| 18 | Équipe & Planning | 18 - Affichages des performances de l'employé | `consulter-ses-performances-employe` | **oui, 3 prompts** — tous basés sur `list_attendances` (dashboard d'équipe, comparaison au planning prévu, employés les plus assidus), aucun outil MCP ne calcule le score de performance FoodEatUp lui-même. Rush conforme au dossier Drive (taille de fichier vérifiée). Sans avatar HeyGen. Validée et publiée sur Lovable le 2026-08-03 (commit `4c651fc1`) — RapidoCMS/LinkedIn en attente (URLs GitHub raw temporaires). **Collision de slug détectée et corrigée** : une autre session (branche `claude/foodeatup-tutorial-video-vn7udf`) avait déjà publié un tutoriel sur le même sujet sous le slug `suivre-ses-performances-cote-employe` (sa propre vidéo, 37 s, sans claudePrompts) — mon premier envoi Lovable avait écrasé cette entrée par erreur (même slug). Réparé en restaurant les deux sous des slugs distincts, puis **sur demande explicite de Michael, l'entrée de l'autre session (`suivre-ses-performances-cote-employe`) a été supprimée le 2026-08-03** (commit `7d1c6801`) — seul `consulter-ses-performances-employe` (avec les 3 claudePrompts) reste sur le site |
| 19 | Comptabilité | 3- Créer un devis | `creer-un-devis` | **oui** — `create_quote` (client/produit/quantité/prix/TVA), même structure que les champs à l'écran. Rush conforme au dossier Drive (taille de fichier vérifiée). Sans avatar HeyGen. Validée et publiée sur Lovable le 2026-08-03 (commit `e22e34b5`) — RapidoCMS/LinkedIn en attente (URLs GitHub raw temporaires) |
| 20 | Comptabilité | 7- Mes dépenses fournisseur | `saisir-ses-depenses-fournisseur` | **oui** — `create_expense` (fournisseur/référence facture/produit/prix/catégorie/statut) ; pas de champ MCP pour le fichier de facture joint, donc non mentionné dans le prompt. Rush conforme au dossier Drive (taille de fichier vérifiée). Sans avatar HeyGen. Validée et publiée sur Lovable le 2026-08-03 (commit `1020dbb1`) — RapidoCMS/LinkedIn en attente (URLs GitHub raw temporaires) |
**2026-08-03 — Chantier d'architecture site (11 catégories / 14 modules)** : suite au
catalogue des 157 tutoriels cibles transmis par Michael, un unique prompt Lovable a fait
évoluer toute l'architecture du site (voir section "Architecture du site" plus haut) —
`tutorials.ts` (types `Category`/`Module` + 11 catégories + 14 modules), `module-icons.ts`,
`index.tsx` (accueil regroupé par catégorie), `module.$slug.tsx` (fil d'Ariane + SEO),
`tutoriel.$slug.tsx` (SEO complet + JSON-LD `VideoObject`). Commit
`12fb06d2510edcdda4116f886a3d259f638559a8`, vérifié par lecture complète des 5 fichiers
modifiés : les 16 tutoriels déjà publiés ci-dessus sont intacts, aucune régression de
contenu. Question toujours en attente de réponse de Michael : re-rendre `ouvrir-sa-vitrine-en-ligne`
(#11) pour corriger le bug des bandeaux d'étape invisibles ?
| 11 | HACCP | Historique de la production et traçabilité | `tracer-ses-productions-historique` | **oui, 3 prompts** — `list_production_plans` (statut + période, exactement les deux filtres montrés à l'écran), un second cadré « préparer un contrôle sanitaire », et `list_top_productions` (hors vidéo, prompt de site uniquement). Publiée le 2026-08-03 (RapidoCMS + Lovable + déploiement). Vidéo 64 s. Première vidéo de la série dont les bandeaux d'étape s'affichent réellement — voir le bug `drawbox`/`t` documenté dans `FOODEATUP-TUTORIELS-WORKFLOW.md` |
| 11 | Comptabilité | 1 - vos dépenses (estimé, non vérifiable depuis cet environnement) | `tenir-ses-depenses` | **oui** — `create_expense`. Rush = parcours StockVision AI (import facture depuis une livraison → OCR → validation → création automatique de la dépense) ; pas de `update_expense`/`delete_expense` côté MCP donc pas de prompt modif/suppression. Poussée sur Lovable puis déployée en prod le 2026-08-03 (`deploy_project`) — **⚠️ recouvrement de contenu constaté à la publication** : deux tutoriels déjà présents dans le module (`scanner-sa-facture-ocr`, `saisir-ses-depenses-fournisseur`, ajoutés par d'autres branches/sessions parallèles : `claude/foodeatup-tutorial-video-qtwswo` et `-n04713`) couvrent le même parcours écran. Gardés tous les trois sur décision explicite de Michael (chaque angle — prix auto / saisie manuelle / StockVision AI — reste utile) plutôt que de dédupliquer. RapidoCMS/LinkedIn non demandés pour cette vidéo (Lovable uniquement) |
| 11 | Comptabilité | 11 - lire ses statistiques par module | `lire-ses-statistiques-par-module` | **oui** — `finance_summary` (lecture seule). Tour du tableau de bord Analytix BI + ses 6 modules (Finances, Stocks, RH & Pointage, HACCP, Production, Assistant IA), aucune action de création dans ce rush. Validée par Michael, publiée le 2026-08-03 : RapidoCMS (vidéo + vignette uploadées) + Lovable (`howItWorks`/`whatItsFor`/`claudePrompt`/`chefTip`). LinkedIn non demandé pour cette vidéo. |
| 12 | HACCP | 12 - ajouter modifier ou valider une reception livraison | `ajouter-modifier-ou-valider-une-reception-livraison` | **oui** — `create_haccp_reception`. Cycle complet ajouter (nouvelle réception + produits) / valider (Enregistrer) / modifier (menu DLC-Température-Scanner post-validation). Publiée le 2026-08-04 : RapidoCMS + Lovable, **remplace** l'ancienne entrée `controler-reception-livraisons` (même écran, vidéo plus courte 51s) supprimée sur demande explicite de Michael pour éviter le doublon sur le site — voir `SCRIPT.md` du projet. ⚠️ Chevauchement partiel restant à surveiller : `scanner-ean-et-dlc-reception` couvre déjà en détail le menu DLC/Température/Scanner (avec ses propres `claudePrompts[]`) — non touché cette fois, seul le dernier segment de cette vidéo l'effleure. LinkedIn non demandé pour cette vidéo. |
| 11 | Comptabilité & Achats | 7 - classer ses factures dans les dépenses | `classer-ses-factures-dans-les-depenses` | non — `create_expense` n'a pas de champ pièce jointe ; l'action centrale du rush (joindre le PDF/photo de la facture) n'a pas d'équivalent MCP. Script validé par Michael le 2026-08-03, vidéo livrée et validée, ajoutée sur Lovable le 2026-08-03. Vidéo hébergée en raw GitHub sur `claude/foodeatup-tutorial-video-c52fkn` (pas d'upload RapidoCMS/LinkedIn demandé pour cette vidéo) |
| 11 | Configuration | 13 - votre vitrine en ligne | `ouvrir-sa-vitrine-en-ligne` | **oui** — pas d'outil MCP de configuration de vitrine à proprement parler ; le `claudePrompt` documente le geste équivalent (template + couleurs + publication). Hébergée en raw GitHub (`videos/foodeatup-vitrine-tuto/out/`, branche `claude/foodeatup-academy-tutorials-n04713`) plutôt que RapidoCMS. Ajoutée sur Lovable le 2026-08-03 |
| 12 | Équipe & Planning | 1 - ajouter ses employés | `ajouter-ses-employes` | **oui** — `create_employee`. Première vidéo du module Équipe & Planning. Hébergée en raw GitHub (`videos/foodeatup-employes-tuto/out/`, branche `claude/foodeatup-tutorial-video-difgjz`) — RapidoCMS non authentifié dans cette session. Validée par le demandeur et publiée le 2026-08-03 (Lovable uniquement ; pas de RapidoCMS/LinkedIn) |
| 13 | Équipe & Planning | 2 - assigner les tâches | `assigner-les-taches` | **oui, 3 prompts** — `assign_task` (`category` en champ libre). Deuxième vidéo du module Équipe & Planning : création d'une tâche, modification (changement de récurrence) et complétion. Montage resserré à 41,9s à la demande de Michael (v1 à 49,9s). Hébergée en raw GitHub (`videos/foodeatup-taches-tuto/out/`, branche `claude/foodeatup-tutorial-video-difgjz`). Validée et publiée le 2026-08-03 (Lovable uniquement ; pas de RapidoCMS/LinkedIn) |
| 14 | Équipe & Planning | 3 - créer son code PIN | `creer-son-code-pin` | non — aucun outil MCP FoodEatUp ne couvre la gestion des codes PIN employé. Troisième vidéo du module Équipe & Planning : définir un code PIN (pointage + accès logiciel scopé au rôle) ; le QR code de la même page sert à l'appairage Bluetooth Jarvis. `chefTip` à tonalité sécurité (confidentialité du code, redéfinition si compromis, principe de moindre privilège via le rôle). VO réécrite courte dès le premier montage (23,3s) suite au retour sur le rythme du tuto précédent. Hébergée en raw GitHub (`videos/foodeatup-pin-jarvis-tuto/out/`, branche `claude/foodeatup-tutorial-video-difgjz`). Validée et publiée le 2026-08-03 (Lovable uniquement ; pas de RapidoCMS/LinkedIn) |
| 15 | Configuration | 10 - monter ses recettes / fiches techniques | `monter-ses-recettes` | **oui, 3 prompts** — `create_recipe` (direct, avec ingrédients+étapes), "depuis une photo d'un plat", et "créer le produit associé à la recette" (`create_product`, boucle recette → carte). Tutoriel manquant du module Configuration signalé par le demandeur — 14e et dernière vidéo attendue de ce module (`expectedCount`). Rush s'arrête avant "Enregistrer la recette" (jamais filmé) : montage terminé sur le tableau d'ingrédients avec coût total en direct, pas d'écran de succès inventé. `chefTip` documente la création de recette depuis une photo et le lien recette → produit vendable. Hébergée en raw GitHub (`videos/foodeatup-recettes-tuto/out/`, branche `claude/foodeatup-tutorial-video-difgjz`). Validée et publiée le 2026-08-03 (Lovable uniquement ; pas de RapidoCMS/LinkedIn) |
| 16 | Équipe & Planning | 4 - se connecter côté employé | `se-connecter-cote-employe` | non — aucun outil MCP FoodEatUp ne couvre la connexion côté employé (URL/QR + PIN), même raison que `creer-son-code-pin`. Cinquième vidéo du module Équipe & Planning : copie de l'URL de connexion, ouverture sur le téléphone/tablette de l'employé, choix du profil, saisie du PIN, puis "Pointer" ou "Mon espace" (grille de modules et menu du haut scopés au rôle). `chefTip` liste 3 cas d'usage (scan QR direct, copier-coller manuel, Pointer vs Mon espace) à la demande du demandeur. ⚠️ Sujet très proche de `installer-la-borne-daccueil` (ajoutée en parallèle par une autre session sur la branche `foodeatup-tutorial-video-vn7udf`, même flux profil/PIN/Pointer-Mon espace) — angle différencié ici sur la connexion depuis l'appareil personnel de l'employé via URL/QR copiable, plutôt que l'installation d'une borne partagée ; à surveiller si redondance perçue par les utilisateurs du site. Hébergée en raw GitHub (`videos/foodeatup-connexion-employe-tuto/out/`, branche `claude/foodeatup-tutorial-video-difgjz`). Validée et publiée le 2026-08-03 (Lovable uniquement ; pas de RapidoCMS/LinkedIn) |
| 17 | Équipe & Planning | 5 - voir son planning côté employé | `voir-son-planning-cote-employe` | **oui, 3 prompts** — `list_plannings` (semaine en cours, semaine prochaine) + croisement avec `list_attendances` pour comparer planning prévu et heures pointées. Sixième vidéo du module Équipe & Planning : stats de la semaine (heures/shifts/tâches), tâche cochée en direct (toast "Tâche faite", compteur mis à jour), export "Ajouter à mon agenda" (ICS, aucun outil MCP pour cette action client-side). Toast McAfee WebAdvisor (bruit de l'environnement d'enregistrement) volontairement exclu du cadrage. `chefTip` détaille les 3 cas d'usage Claude à la demande du demandeur. Hébergée en raw GitHub (`videos/foodeatup-planning-employe-tuto/out/`, branche `claude/foodeatup-tutorial-video-difgjz`). Validée et publiée le 2026-08-03 (Lovable uniquement ; pas de RapidoCMS/LinkedIn) |
| 18 | Équipe & Planning | 7 - lire ses notifications et tâches du jour | `lire-ses-notifications` | non — aucun outil MCP FoodEatUp ne couvre la lecture des notifications employé (flux self-service côté client), même raison que `creer-son-code-pin` / `se-connecter-cote-employe`. Septième vidéo du module Équipe & Planning : cloche de notifications (badge non lus), panneau "Mes notifications" (congé approuvé, nouveau shift, tâche HACCP, modification planning, rappel solde congés), filtres Tout/Congés/Planning/Tâches. `chefTip` sur les alertes HACCP à échéance serrée. Hébergée en raw GitHub (`videos/foodeatup-notifications-tuto/out/`, branche `claude/foodeatup-tutorial-video-difgjz`). Validée et publiée le 2026-08-03 (Lovable uniquement ; pas de RapidoCMS/LinkedIn) |
| 19 | Comptabilité | Gérer ses fournisseurs côté achats | `gerer-ses-fournisseurs-cote-achats` | **oui, 3 prompts** — `create_supplier` (direct) + `create_supplier_order` (angle achats) + `list_suppliers`/`get_supplier` (consultation avant commande). Première vidéo produite pour le module Comptabilité & Achats (cycle complet : création, édition de la fiabilité, tentative de suppression annulée). `chefTip` sur la mise à jour de la fiabilité et la confirmation avant suppression. Hébergée en raw GitHub (`videos/foodeatup-fournisseurs-achats-tuto/out/`, branche `claude/foodeatup-tutorial-video-difgjz`). Publiée le 2026-08-03 (Lovable uniquement ; pas de RapidoCMS/LinkedIn) |
| 20 | Comptabilité | Changer les statuts d'un devis | `changer-les-statuts-dun-devis` | **oui, 3 prompts** — `update_quote_status` (marquer accepté / refusé) + `list_quotes` (filtre par statut, pour repérer les devis en attente). Menu d'actions → Visualiser → Téléchargements et options → Marquer comme accepté → confirmation → statut Signé avec nouvelles actions (Convertir en facture). `chefTip` sur le suivi des devis en attente et la conversion en facture. À distinguer de `changer-les-statuts-dune-facture` (même module, ajoutée en parallèle par une autre session sur la branche `claude/foodeatup-tutorial-video-vn7udf` — sujet voisin mais sur les factures, pas les devis). Hébergée en raw GitHub (`videos/foodeatup-devis-statuts-tuto/out/`, branche `claude/foodeatup-tutorial-video-difgjz`). Publiée le 2026-08-03 (Lovable uniquement ; pas de RapidoCMS/LinkedIn) |
⚠️ Ce tableau ne reflète que les vidéos produites depuis cette session/branche
(`claude/foodeatup-tutorial-video-difgjz`). D'autres sessions travaillent en parallèle
sur d'autres branches (au moins `claude/foodeatup-tutorial-video-vn7udf` et
`claude/foodeatup-academy-tutorials-n04713` observées le 2026-08-03) et publient
directement sur le même projet Lovable — le site compte désormais bien plus d'entrées
et de modules (`site-web-vitrine`, `caisse-pos`, `hubrise-livraisons`, `caroline-ia`,
`reservation-salle`, `service-commande`, `kds-cuisine`, `marketing-fidelite`,
`predibot`, etc.) que ce que ce tableau local liste. Se fier à
`mcp__Lovable__read_file` sur `src/data/tutorials.ts` pour l'état réel du site avant
toute nouvelle publication, plutôt qu'à ce tableau seul.
| 11 | HACCP | Relevés de température | `ajouter-temperature-plat` | non — `add_temperature` est limité à l'onglet Équipements, pas Plats (montré dans ce rush) ; `create_recipe`/`create_dish` n'ont pas les champs vus (allergènes, durée de vie, pièce jointe). 1ère vidéo publiée du module HACCP. Validée par Michael le 2026-08-03, publiée le 2026-08-03 (RapidoCMS + Lovable — LinkedIn pas encore demandé pour cette vidéo) |
| 11 | HACCP | Traçabilité simplifiée (photo express, sans produit ni lot) | `creer-une-tracabilite-simplifiee` | **oui** — `create_haccp_tracabilite` avec `type: "simple"` (vs `type: "complete"` pour la carte "Traçabilité complète"). Rush fourni par Michael (screen recording réel de la fonctionnalité) ; un aléa d'enregistrement (erreur caméra "Permission dismissed" vers 10-12s dans la source) a été identifié et coupé au montage, pas montré ni commenté en VO. Validée et publiée le 2026-08-04 (RapidoCMS + LinkedIn 2026-08-08 07h + Lovable) |
| 12 | Configuration | Configuration de sa vitrine | `ouvrir-sa-vitrine-en-ligne` | **oui** — combine `apply_site_template`, `set_site_theme`, `publish_site`. Vidéo montée le 2026-08-02 (avatar HeyGen sur N0, reste ElevenLabs) mais restée non publiée (`SCRIPT.md` marquait "à livrer à Michael pour validation") ; publiée le 2026-08-04 sur instruction explicite de Michael de publier toutes les vidéos réalisées : RapidoCMS + LinkedIn (2026-08-08 16h) + Lovable (une entrée `ouvrir-sa-vitrine-en-ligne` existait déjà avec une vidéo provisoire, mise à jour avec l'URL RapidoCMS définitive plutôt que dupliquée) |
| 11 | StockVision AI | Liste des courses : ajouter, modifier et supprimer un produit | `tenir-sa-liste-de-courses` | **oui** — `create_supplier_order` (la commande fournisseur, suite logique de la liste construite à l'écran). Publiée sur Lovable (RapidoCMS archivé, pas de post LinkedIn — non demandé). **Voix mixte** : N0/N6/N8 ElevenLabs Adam, N1-N5/N7 en secours Piper local (quota ElevenLabs épuisé en cours de production) — à régénérer en Adam dès que le quota est reconstitué, voir `videos/foodeatup-liste-courses-tuto/SCRIPT.md` |
| 12 | Hygiène & HACCP | Créer un plat pour la production (ingrédients, date, quantité) | `creer-sa-fiche-plat-pour-production` | **oui, 2 prompts** — `create_recipe` (plat + ingrédients) + `create_production_plan` (date/quantité). Publiée sur Lovable (RapidoCMS archivé, pas de post LinkedIn — non demandé). Voix 100% ElevenLabs Adam (quota reconstitué). Voir `videos/foodeatup-fiche-plat-tuto/SCRIPT.md` |
⚠️ **Ce tableau est incomplet par rapport au site Lovable réel** : le site a évolué au-delà de ce fichier (modules/catégories renommés — voir `src/data/tutorials.ts`, ex. `moduleSlug: "stockvision-ai"` existe déjà avec plusieurs tutoriels non listés ici : `deduire-ses-besoins-de-production`, `imprimer-ses-ingredients-de-production`, `sortir-ses-ingredients-du-stock`, `saisir-un-mouvement-de-stock`, `lire-ses-mouvements-de-stock`). Se fier à `src/data/tutorials.ts` (via `read_file`) comme source de vérité pour éviter les doublons, pas seulement à ce tableau.
| 11 | StockVision AI | Liste des courses : commander et envoyer aux fournisseurs | `envoyer-sa-commande-au-fournisseur` | **oui** — `create_supplier_order`. Complète `tenir-sa-liste-de-courses` (gestion des lignes) avec l'action de commande/envoi elle-même (bouton Commander + modale "Commander tout", flux Email par fournisseur avec date de livraison). Deux bugs de montage rencontrés et corrigés : décalage voix/image cumulatif (même bug que `foodeatup-tva-tuto`) et zoom-punch mal positionné faute de mesure colorimétrique des boutons (voir `SCRIPT.md` du dossier). Validée et publiée le 2026-08-04 (RapidoCMS + LinkedIn 2026-08-16 07h + Lovable, inséré après `tenir-sa-liste-de-courses`) |
*(Note : cette table n'a pas été tenue à jour à chaque publication depuis son ajout — `src/data/tutorials.ts` contient plus d'entrées que celles listées ici. Ne pas s'y fier comme source exhaustive, seulement comme historique partiel.)*
| 11 | HACCP | Contrôle de réception (température & EAN) | `controler-sa-reception-stock` | **oui, 2 prompts** — `create_haccp_reception` (contrôle de réception, température) + `create_haccp_label` (étiquette EAN/DLC). Première vidéo du module HACCP. Publiée sur Lovable le 2026-08-04 (RapidoCMS mis à jour ; publication LinkedIn en attente — non demandée dans ce tour) |
| 12 | HACCP | Documents (modèles prédéfinis) | `utiliser-nos-modeles-foodeatup` | non — pas d'outil MCP correspondant (bibliothèque de documents statiques, ni `list_employee_documents` ni `list_site_templates` ne correspondent). Publiée le 2026-08-04 (RapidoCMS + Lovable, demande explicite de publication immédiate). **Note** : une carte d'intro "RETROUVER MES ÉTIQUETTES HISTORIQUE" a été fournie en même temps mais sans rush correspondant — pas de vidéo produite pour ce sujet, en attente d'un enregistrement d'écran |
| 11 | HACCP | Valider une production (Quantité, Température, note) | `valider-une-production` | **oui, 3 prompts** — `validate_production` (validation complète = le prompt affiché dans la vidéo) + « écart de quantité » + `list_production_plans` puis `validate_production`. **Premier tutoriel du module HACCP** (les dossiers de ce module ne fournissent aucun clip avatar : la carte d'intro porte N0 et toute la narration est en voix ElevenLabs). Publiée le 2026-08-03 sur demande explicite de Michael (RapidoCMS + Lovable ; pas de programmation LinkedIn demandée). Site redéployé (`deploy_project`) sur https://foodeatup-guide-star.lovable.app — commit `cecc85a` |
| 11 | StockVision AI | Mouvements de stock : ajouter et modifier | `saisir-un-mouvement-de-stock` | **oui, 2 prompts** — `adjust_stock` en `increment` (entrée/sortie) + en `set` (correction d'inventaire). Publiée le 2026-08-03 (RapidoCMS + Lovable) sur instruction explicite de Michael, sans passer par le STOP de validation. Pas de programmation LinkedIn : non demandée. Se place **avant** `lire-ses-mouvements-de-stock` dans le module (saisie/modification d'abord, lecture du détail et suppression ensuite) |
> ⚠️ Ce tableau ne suit que les vidéos passées par ce dépôt. `src/data/tutorials.ts`
> en compte 46 au 2026-08-03 — c'est le fichier Lovable qui fait foi, pas ce tableau.
| 11 | HACCP | Équipements : ajouter, modifier, supprimer | `declarer-ses-equipements` | **oui** — `create_equipment` (modifier/supprimer un équipement n'ont pas d'outil MCP dédié). Publiée sur Lovable le 2026-08-03 à la demande explicite de Michael (MP4 + vignette uploadés sur RapidoCMS pour obtenir les URLs S3 stables). **LinkedIn non demandé pour ce tuto** — pas de brouillon programmé. |
| 12 | HACCP | Contrôle à réception : produits, DLC, température, conformité | `controler-reception-livraisons` | **oui** — `create_haccp_reception` (les 4 actions rapides par produit — Photo DLC, DLC manuelle, Température, Scanner produit — n'ont pas d'outil MCP dédié). Publiée sur Lovable le 2026-08-04 à la demande explicite de Michael (MP4 + vignette uploadés sur RapidoCMS). **LinkedIn non demandé pour ce tuto** — pas de brouillon programmé. ⚠️ **Remplacée peu après par une session concurrente** : `list_messages` sur le projet Lovable montre que cette entrée a été supprimée le 2026-08-04 (~02:49) et remplacée par `ajouter-modifier-ou-valider-une-reception-livraison` (58,88 s, mêmes écrans mais couvrant explicitement ajouter/modifier/valider), poussée depuis une autre branche/session — pas un commit de cette branche-ci. À réconcilier au moment du merge. |
| 13 | HACCP | Contrôle de conformité par photo (analyse IA) | `photo-ia-controle-nettoyage` | non — aucun outil MCP pour "upload photo → analyse IA automatique" (le candidat le plus proche, `create_hygiene_checklist_validation`, est une soumission manuelle de checklist, pas un upload photo/IA). Publiée sur Lovable le 2026-08-04 à la demande explicite de Michael (MP4 + vignette uploadés sur RapidoCMS). Vidéo volontairement courte (28 s, une seule action, pas de séquence Claude). **LinkedIn non demandé pour ce tuto** — pas de brouillon programmé. |
| 14 | Service Multi-Canal | Créer, consulter, modifier et supprimer une commande | `mes-commandes-tous-canaux` | **oui, 2 prompts** — `create_order` (création, montré dans la vidéo) + `update_order_status` (changement de statut, `claudePrompts[]` uniquement). Pas de prompt pour la suppression (pas d'outil MCP dédié). Publiée sur Lovable le 2026-08-04 à la demande explicite de Michael (MP4 + vignette uploadés sur RapidoCMS). Vidéo la plus longue de la série à ce jour (68,7 s — create + view + edit + delete). **LinkedIn non demandé pour ce tuto** — pas de brouillon programmé. |
| 11 | PrediBot | 1 - prédire ses commandes (ventes & production) | `predire-ses-commandes` | non — fonctionnalité de lecture seule (prédiction IA), aucun outil MCP ne correspond. Validée par Michael et publiée le 2026-08-03 (Lovable uniquement — pas de demande RapidoCMS/LinkedIn sur cette vidéo). Rattrapage : entrée non loguée ici au moment de la publication, ajoutée a posteriori le 2026-08-04 |
| 12 | HACCP | Historique de vos zones de nettoyage | `retrouver-lhistorique-des-zones-de-nettoyage` | **oui, 3 prompts** — `list_cleaning_actions` (historique période + préparation contrôle sanitaire) + `record_cleaning_action` (enregistrer). Séquence Claude animée dans la vidéo (module partagé). Validée par Michael et publiée le 2026-08-04 (Lovable uniquement — pas de demande RapidoCMS/LinkedIn sur cette vidéo) |
*(les entrées 13+ ne sont ajoutées ici qu'après validation explicite de Michael sur la vidéo livrée — voir "Règle de validation" en haut de ce fichier)*
| 11 | HACCP | Accueil et historique du classeur HACCP | `ouvrir-son-classeur-haccp` | **oui** — `list_haccp_temperatures` (étages vidéo) + `list_haccp_tracabilite` (2e cas d'usage, fiche seulement). Dossier repo `videos/foodeatup-haccp-export-tuto` (intro/outro fournis par Michael, rush "Retrouver et exporter les Historique du module HACCP", exploitable en entier). Validée et publiée le 2026-08-04 : RapidoCMS (`foodeatup-classeur-haccp-tuto-v1`/`-thumbnail`, a rempli en place le créneau LinkedIn déjà planifié `FoodEatUp — Ouvrir son classeur HACCP`, 2026-08-27 07h) + Lovable (entrée déjà présente dans `tutorials.ts`, seul `durationSeconds` corrigé 45→48) |
| 11 | Comptabilité | 2 - créer une facture | `creer-une-facture` | **oui** — `create_invoice`. Rush montre client + TVA intracommunautaire, recherche/création produit, quantité/prix/TVA ligne, offre, remise, dates, mode de paiement, et l'indicateur de conformité Factur-X (2026) grimpant à 100 % en direct — repris en `chefTip` (facturation électronique obligatoire 2026 en France). Publiée le 2026-08-04 (RapidoCMS + LinkedIn 2026-09-10 16h + Lovable, juste après `creer-un-devis`) |
| 11 | HACCP | Historique traçabilité | `retrouver-lhistorique-de-la-tracabilite` | **oui** — `list_haccp_tracabilite`. Rush fourni par Michael (screen recording + cartes intro/outro), validée puis publiée le 2026-08-04 (RapidoCMS + Lovable — pas de post LinkedIn, non demandé) |
| 11 | HACCP | Créer un produit à sélectionner pour vos étiquettes | `creer-produit-pour-etiquetage` | non — `create_haccp_label` (déjà utilisé sur `imprimer-ses-etiquettes`) crée l'étiquette DLC en aval, pas ce produit-catalogue réutilisable (marque, code-barres, allergènes, durée de vie) montré dans ce rush. Validée et publiée le 2026-08-04 (Lovable ; **pas de RapidoCMS/LinkedIn** — connecteur RapidoCMS non disponible dans cette session, `videoUrl`/`thumbnailUrl` pointent en attendant vers le raw GitHub de la branche `claude/foodeatup-video-tutorials-6hna9b`, même convention que `imprimer-ses-etiquettes`) |
| 11 | HACCP | Historique - Production | `retrouver-historique-productions` | **oui** — `list_top_productions` (lecture seule, aucune action de création dans le rush). Validée par Michael le 2026-08-04, publiée (RapidoCMS + Lovable, `commit_sha` `0d0021f`). Pas de créneau LinkedIn programmé dans cette session. Voisine de `tracer-ses-productions-historique` (déjà présente sur le site, écran différent — gestion "Mes productions" par statut) : les deux entrées documentent des écrans distincts, gardées séparées exprès. `subcategory` est une estimation (nom exact du sous-dossier Drive non confirmé) |
## En attente de validation (montées, pas encore publiées)
Vidéos montées et poussées sur la branche mais **pas publiées** — règle "STOP
obligatoire" ci-dessus (pas d'upload RapidoCMS / draft LinkedIn / entrée
Lovable tant que Michael n'a pas validé le montage livré).
| Module | Sous-catégorie | Slug prévu | claudePrompt ? | Statut |
|---|---|---|---|---|
| HACCP | Poser une DLC sur ses productions | `poser-une-dlc` | **oui** — `create_haccp_label` (paramètre `dlc` natif). Prompt : voir `foodeatup-dlc-tuto/SCRIPT.md` | Montée le 2026-08-04 (`videos/foodeatup-dlc-tuto/`, 44,5 s), livrée pour validation. Réutilise le rush "Créer les étiquettes de vos productions" (même flux HACCP, focus recadré sur le champ DLC). En attente de retour Michael avant RapidoCMS/LinkedIn/Lovable. |
**Sur le total de 157 vidéos mentionné par Michael** : le suivi ci-dessus (et
le tableau des 5 modules plus haut) totalise 94 vidéos identifiées pour le
site FoodEatUp Academy — 157 semble couvrir un périmètre plus large
(Reels FoodEatUp, série-30, séries Rapido, stories 30 jours — voir
`videos/PLAN-TIKTOK-ET-MANQUANTS.md` et `references/mcp-plugins-video-catalog.md`
pour ces autres séries). Pas de liste unique consolidée à 157 trouvée dans le
dépôt : à confirmer avec Michael avant de fabriquer un chiffre de suivi global.
| 11 | HACCP | 14 - Retrouver toutes vos production | `consulter-ses-productions-en-cours` | **oui** — `list_production_plans`. Première vidéo du module HACCP. Validée par Michael le 2026-08-04. RapidoCMS **non disponible dans cette session** (connecteur non installé) : vidéo/vignette servies depuis GitHub raw (`claude/foodeatup-video-tutorials-u4ljhv`) en attendant reconnexion — pas de post LinkedIn programmé pour cette raison. Voir `videos/SUIVI-VIDEOS.md` pour le détail et `videos/foodeatup-productions-tuto/SCRIPT.md` pour le ré-audit Drive (137 vidéos vérifiées le 2026-08-04, 5 nouveaux modules découverts) |
| — | HACCP | Historique du contrôle à réception | `retrouver-lhistorique-du-controle-a-reception` | **oui** — `create_haccp_reception` (les champs du modal « Modifier le contrôle » correspondent 1:1 ; pas d'`update_haccp_reception` côté MCP, donc le prompt enregistre un nouveau contrôle plutôt que de modifier l'existant montré à l'écran, même bénéfice pour le restaurateur). Script validé par Michael le 2026-08-04, montage `videos/foodeatup-historique-reception-tuto/` (47s). Publiée le 2026-08-04 (RapidoCMS + LinkedIn 2026-09-06 07h + Lovable, déployée en production) |
| — | Comptabilité | Relier ses achats à ses livraisons | `relier-ses-achats-a-ses-livraisons` | **oui** — `create_expense` (fournisseur, référence facture, lignes produits, totaux auto ; pas de champ « livraison associée » côté MCP, donc le prompt enregistre directement la dépense plutôt que de reproduire l'étape d'import OCR — même bénéfice). ⚠️ Sujet proche de `scanner-sa-facture-ocr` et `classer-ses-factures-dans-les-depenses` déjà publiées par une autre session (même déroulé livraison→facture→OCR→dépense, rush différent) — à vérifier avec Michael si une consolidation est souhaitée. Script validé par Michael le 2026-08-04, montage `videos/foodeatup-depenses-livraisons-tuto/` (45,7s). Publiée le 2026-08-04 (RapidoCMS + LinkedIn 2026-09-10 07h + Lovable, déployée en production) |
| 11 | Configuration | 13 - votre vitrine en ligne | `ouvrir-sa-vitrine-en-ligne` | **oui** — prompt combiné `apply_site_template` + `set_site_theme` + `publish_site`. Publiée (Lovable) — entrée rétroactive ajoutée le 2026-08-03, vidéo déjà en ligne (PR #6 mergée) |
| 12 | StockVision AI (1er tuto du module) | 1 - déduire ses besoins de production | `deduire-ses-besoins-de-production` | **oui** — prompt combiné `create_production_plan` + `get_production_ingredients`. Publiée sur Lovable le 2026-08-03 (validation Michael "ok publi sur lovable") — RapidoCMS/LinkedIn non demandés |
| 13 | Hygiène & HACCP (1er tuto du module) | 1 - pointer ses actions de nettoyage | `pointer-ses-actions-de-nettoyage` | **oui** — `record_cleaning_action`. Rush contient un état cassé en fin de tournage (bouton "Valider" en masse → erreur "Zone non trouvée") : exclu du montage, voir `videos/foodeatup-nettoyage-actions-tuto/SCRIPT.md` (dossier renommé lors de la fusion des branches le 2026-08-04 : collision avec `foodeatup-nettoyage-tuto` = un autre tutoriel, « Ajouter et paramétrer son plan de nettoyage / Zones ») |
| 11 | StockVision AI | 2 - détails et impression de la liste des ingrédients | `imprimer-ses-ingredients-de-production` | **oui, 2 prompts** — `get_production_ingredients` (liste des ingrédients d'une production) + `complete_haccp_tracabilite` (compléter la traçabilité d'un ingrédient). Publiée sur Lovable le 2026-08-03 (commit `6ec7dff`), URLs vidéo/vignette en raw GitHub sur la branche `claude/foodeatup-tutorial-video-rdu0k9` — pas de publication RapidoCMS/LinkedIn (non demandée). Suite logique de `deduire-ses-besoins-de-production`, placée juste après dans le module |
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
| 29 | Comptabilité & Achats | 9 - déclarer son e-reporting | `declarer-son-ereporting` | non — déclaration e-reporting, génération Factur-X/XML, archivage légal (hash SHA-256) et vérification d'intégrité sont des fonctionnalités de conformité réglementaire propres au produit, aucun outil MCP correspondant. Rush : onglet E-Reporting (stats par période, échéances) → "Déclarer la période" → détail facture → "Téléchargements et options" (Factur-X, XML CII, archiver légalement, UBL) → onglet Archives légales (hash SHA-256, expiration 10 ans) → "Vérifier l'intégrité" → "Facture intègre". `chefTip` relie les trois obligations de la réforme facturation électronique 2026. Dérive nulle dès le premier montage. Hébergée en raw GitHub (`videos/foodeatup-ereporting-tuto/out/`, branche `claude/foodeatup-tutorial-video-vn7udf`). Publiée sur Lovable le 2026-08-04 |
| 30 | Équipe & Planning | 18 - suivre ses performances côté employé | `suivre-ses-performances-cote-employe` | non — aucun outil MCP ne calcule/n'expose ce score de performance employé (métrique interne, pas un endpoint API). Voir `videos/foodeatup-performances-tuto/SCRIPT.md` (36,84 s, dérive nulle). **Hébergée en URL GitHub raw** (`videos/foodeatup-performances-tuto/out/foodeatup-performances-tuto-v1.mp4`, branche `claude/foodeatup-tutorial-video-ph63jf`) **en attente de la fin de la panne RapidoCMS (502 persistant sur `upload_file_tool` au 2026-08-04) — à ré-uploader sur RapidoCMS S3 dès que le service revient, puis mettre à jour `videoUrl`/`thumbnailUrl` sur Lovable.** Publiée sur Lovable le 2026-08-04 (module `equipe-planning`) |
| 31 | HACCP | Contrôle à réception : produits, DLC, température, conformité | `controler-reception-livraisons` | **oui** — `create_haccp_reception`. Voir `videos/foodeatup-reception-tuto/SCRIPT.md` (50,72 s, peak -7,16 dBFS, dérive nulle). **Hébergée en URL GitHub raw** (branche `claude/foodeatup-tutorial-video-ph63jf`) **en attente de la fin de la panne RapidoCMS — à ré-uploader sur S3 dès retour du service.** Publiée sur Lovable le 2026-08-04 (module `haccp`) |
| 32 | HACCP | Poser une DLC sur ses productions | `poser-une-dlc-sur-ses-productions` | **oui** — `create_haccp_label`. Voir `videos/foodeatup-dlc-tuto/SCRIPT.md`. A remplacé une fiche stub préexistante sur Lovable (`section: "Production & plats"`, `order: 15`) — champs conservés. **Hébergée en URL GitHub raw** (branche `claude/foodeatup-tutorial-video-ph63jf`) **en attente de la fin de la panne RapidoCMS — à ré-uploader sur S3 dès retour du service.** Publiée sur Lovable le 2026-08-04 (module `haccp`, commit Lovable `608cf98`) |
**Bilan module Équipe, Planning & RH au 2026-08-04** : 20/20 vidéos du catalogue publiées avec l'ajout de `suivre-ses-performances-cote-employe` (#18) ci-dessus. Il reste #15 « Pointer son Service — pauses & photo » à corriger : le fichier fourni pour cette vidéo (à trois reprises désormais) s'est révélé être un doublon du rush #14 (même taille en octets, 31 001 599, contenu vérifié identique — grille de modules "Mon espace", pas de pauses/pointage/empreinte photo). En attente du bon fichier avant de pouvoir monter cette dernière vidéo.
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
| 11 | StockVision AI | Sortie des ingrédients du stock de la production | `sortir-ses-ingredients-du-stock` | **oui, 3 prompts** — `validate_production` (valider + déstocker), `get_production_ingredients` (contrôler les manquants avant de valider), `list_stocks`/`list_low_stocks` (contrôler après). Publiée le 2026-08-03 sur demande directe de Michael (RapidoCMS + Lovable ; pas de programmation LinkedIn demandée). Pendant « stock » de `valider-une-production` (module HACCP) : l'un montre le formulaire, celui-ci montre les mouvements de stock générés |
⚠️ Ce tableau ne recense que les tutoriels publiés **depuis cette branche**. Le site
contient aussi des fiches ajoutées depuis d'autres branches de travail (ex. `predibot`,
`valider-une-production`) — toujours relire `src/data/tutorials.ts` côté Lovable avant
d'ajouter une entrée, pour ne pas créer de doublon (vérifié pour celle-ci).
| — | StockVision AI | Mouvements de stock : détails et suppression | `lire-ses-mouvements-de-stock` | **oui, 2 prompts** — `list_stocks`/`list_low_stocks` (faire le point) + `adjust_stock` (corriger une ligne, l'outil écrit lui-même un mouvement tracé). Aucun outil MCP ne supprime un mouvement : pas de prompt inventé pour ce geste. Publiée le 2026-08-03 (RapidoCMS + Lovable, commit `a485c03`). Pas de planification LinkedIn — non demandée. |
> ⚠️ **Ce tableau a pris du retard sur le site.** `src/data/tutorials.ts` contient
> aujourd'hui bien plus d'entrées que les 10 listées ci-dessus (modules `equipe-planning`,
> `haccp`, `comptabilite`, `marketing-fidelite`, `stockvision-ai`…), et le fichier a gagné
> des modules qui ne figurent pas dans la liste des 5 plus haut. La source de vérité est
> le fichier Lovable lui-même — lire `src/data/tutorials.ts` avant de supposer qu'un
> tutoriel n'existe pas encore, plutôt que de se fier à ce tableau seul.
| 11 | HACCP | Relevé de température des équipements | `relever-une-temperature-equipement` | **oui, 3 prompts** — `add_temperature`. Vidéo produite à partir des 3 intrants fournis (carte intro, carte outro, screen recording HACCP > Températures : Frigo 5 6°C→9°C, non-conformité auto-détectée vs seuil 4°C). Fiche Lovable préexistante (plus riche, 8 étapes + 3 claudePrompts) mise à jour avec les vraies URLs vidéo/vignette + durée 38s ; premier `claudePrompt` réaligné sur le texte affiché à l'écran dans la vidéo. Validée et publiée le 2026-08-04 (RapidoCMS + LinkedIn 2026-09-09 16h — rotation pleine jusque-là + Lovable) |
| 11 | HACCP | Traçabilité complète (sélection produit, lot, DLC, remarques) | `creer-une-tracabilite-complete` | **oui** — `create_haccp_tracabilite` (`type="complete"`). Validée par Michael le 2026-08-04 (`videos/foodeatup-tracabilite-complete-tuto/` — dossier renommé lors de la fusion des branches le 2026-08-04, collision avec un autre tutoriel `foodeatup-tracabilite-tuto` déjà présent : « Historique de la production et traçabilité » ; 52,2 s, voix Adam FR). Publiée : RapidoCMS (`foodeatup-tracabilite-tuto-v1` / `foodeatup-tracabilite-tuto-thumbnail`) + Lovable (`src/data/tutorials.ts`, commit `82b5ca2`, juste après `creer-une-tracabilite-simplifiee`). **LinkedIn pas encore programmé** — planning du compte FoodEatUp déjà rempli jusqu'au 2026-08-25 par ailleurs (voir `SUIVI-157-TUTORIELS.md`, risque de collision de créneau constaté). |
| 1 | Marketing, Fidélité & Iris | 09 · Ciblage et consentement clients | `ciblage-et-consentement-clients` | **oui, 2 prompts** — `list_rfm_segments` (lecture, prompt vidéo : consultation des segments RFM) + `create_campaign` (`claudePrompts[]` uniquement, pour enchaîner ciblage → brouillon de campagne). Pas de prompt sur le volet consentement/STOP : `update_client` n'expose qu'un statut générique Actif/Inactif/Suspendu, aucun opt-out marketing par canal. Première vidéo produite pour ce module (0/24 avant elle) : rush de 28,2 s en défilement continu (segments dynamiques, plafond mensuel, tableau contacts & consentements RGPD, journal des envois), sans clic de formulaire → pas de zoom-punch, bandeaux d'étape seuls. Montage 60,6 s, dérive voix/image ≤0,1 s, pic audio -7,17 dBFS (`videos/foodeatup-ciblage-consentement-tuto/SCRIPT.md`). A rempli une fiche stub préexistante sur Lovable (`slug: "ciblage-et-consentement-clients"`, `order: 9`, déjà en place avant cette session) — champs `slug`/`title`/`moduleSlug`/`subcategory`/`section`/`order` conservés, `videoUrl`/`thumbnailUrl`/`durationSeconds`/`howItWorks`/`whatItsFor`/`claudePrompts`/`chefTip`/`chefTipAvatar` remplis. Validée par Michael le 2026-08-05. Publiée : RapidoCMS (`foodeatup-ciblage-consentement-tuto-v1` / `-thumbnail`) + Lovable (`src/data/tutorials.ts`). **LinkedIn non demandé pour cette vidéo.** ⚠️ **Fragmentation confirmée en direct** : le compteur d'accueil du site est passé de 106 à 110 tutoriels en ligne après ce seul envoi (+4, pas +1) — d'autres sessions publient en parallèle sur ce même projet Lovable pendant que celle-ci travaillait. |
| 2 | Marketing, Fidélité & Iris | 10 · Suivre ses crédits SMS & WhatsApp | `suivre-ses-credits-sms-whatsapp` | non — aucun outil MCP FoodEatUp ne lit le solde de crédits, les dotations ou les minutes voix consommées (données de facturation/abonnement, pas une entité métier exposée par le MCP), même raisonnement que `creer-son-code-pin`/`generer-qr-code-pointage`. Deuxième vidéo du module (9/24 avant elle) : rush de 22,4 s en défilement continu depuis la page Abonnement (comparatif de packs, marketplace d'agents IA additionnels) jusqu'à la section « Mes crédits & minutes » (quota du mois non reporté, achats & dotations avec date d'expiration, minutes voix Caroline/Jarvis) puis les boutons de recharge par palier et le Pack annuel intégral. Montage 42,7 s, dérive voix/image ≤0,08 s, pic audio -7,23 dBFS (`videos/foodeatup-credits-com-tuto/SCRIPT.md`). A rempli une fiche stub préexistante sur Lovable (`slug: "suivre-ses-credits-sms-whatsapp"`, `order: 9` dans `tutorials.ts`) — `howItWorks`/`whatItsFor`/`chefTip`/`chefTipAvatar` remplis, pas de `claudePrompt`. Validée par Michael le 2026-08-05. Publiée : RapidoCMS (`foodeatup-credits-com-tuto-v1` / `-thumbnail`) + Lovable (commit `4413677`). **LinkedIn non demandé pour cette vidéo.** |
