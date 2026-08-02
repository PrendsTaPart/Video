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

## Comment ajouter une vidéo (à chaque tutoriel produit)

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

## Avatar HeyGen — statut (2026-08-02)

Demandé : générer des vidéos d'avatar 3D HeyGen avec Michael en chef de cuisine. **Impossible
dans cet environnement pour l'instant** : `HEYGEN_API_KEY` n'est pas présente (pas de `.env` à
la racine du dépôt dans cette session — une clé y avait été branchée lors d'une session
précédente, mais elle ne survit pas au changement de conteneur, et `.env` n'est jamais commité,
à raison). Le connecteur MCP `HyperFrames_by_HeyGen` disponible dans cette session n'est PAS un
générateur d'avatar humain — c'est un moteur d'animation HTML/CSS, sans rapport. Pour débloquer :
Michael doit fournir une clé API HeyGen (`app.heygen.com/settings/api`) à déposer en variable
d'environnement. En attendant, la photo transformée en chef (ci-dessus) peut servir de base
visuelle si Michael crée lui-même un avatar photo sur HeyGen et partage l'`avatar_id`.

## Tutoriels publiés

| # | Module | Sous-catégorie | Slug | claudePrompt ? |
|---|---|---|---|---|
| 1 | Configuration | 1 - Inscription, e-mail de confirmation | `creer-son-compte` | non — pas d'outil MCP (signup) |
| 2 | Configuration | 2 - monte votre boutique | `monter-sa-boutique` | non — pas d'outil MCP (fiche boutique) |
| 3 | Configuration | 3 - choisit votre abonnement | `choisir-son-abonnement` | non — pas d'outil MCP (paiement Stripe) |
