# Épisode 9 · Une application client à 2 000 €, connectée à FoodEatUp et Figma

Projet client réalisé par BraindCode. **Le client n'est pas nommé** (pas d'accord de sa part) : la vidéo l'appelle « PEMA Coffee Shop », un nom de démonstration. Son nom, son logo, ses photos et sa marque sont retirés ou floutés partout (captures, fiche PDF, Academy, voix off). Vertical 1080 × 1920, 120 s (+ version de 44,3 s). **Rien n'a été publié.**

Le prix de 2 000 € est présenté comme le prix annoncé de ce projet. Aucune marge, aucun bénéfice, aucun encaissement n'est cité.

## Livrables

| Livrable | Fichier |
|---|---|
| Vidéo principale (120 s) | `renders/episode9-pema-coffee-shop_1080x1920.mp4` |
| Version courte (44,3 s) | `renders/episode9-pema-coffee-shop_45s_1080x1920.mp4` |
| Miniature « Une application client à 2 000 € » | `renders/miniature-episode9-1080x1920.jpg` |
| Voix off (Noé, ElevenLabs `eleven_v4`), mixage | `audio/` |
| Sous-titres SRT et ASS (120 s et 45 s) | `sous-titres/` |
| Captures réelles utilisées (extraits) | `captures/` |
| Script, storyboard, publications, rapports | ci-dessous |

## Sources étudiées

- **Dépôt privé du client** : 409 commits du 03/10 au 12/10/2026 (284 par Lovable, 89 par Claude, 34 par BraindCode), 36 pull requests. Lu en entier côté documentation : `README.md`, `AGENTS.md`, `roadmap.md`, `docs/RAPPORT_FINAL.md`, `docs/AUDIT.md`, `scripts/figma/README.md`, plus le code de la synchronisation, des tâches planifiées et des PDF.
- **Projet Lovable du client** : 181 messages, dont 87 prompts du 03/10 au 26/10/2026, lus via le MCP Lovable. Le dernier prompt date d'aujourd'hui : « Ajoute les intégrations d'agents (MCP) ». Ce changement n'est pas encore poussé sur GitHub.
- **Application.** Le site public du client n'est pas montré (il porte sa marque).
  - L'intérieur de l'app demande un compte de l'établissement. **Aucun identifiant client n'a été utilisé.** L'historique Lovable contient des identifiants : ils ne sont ni montrés ni repris ici.
  - La démo vient donc de l'**application réelle lancée en local**, avec le banc de test du dépôt (`e2e/fixtures.ts`) : Supabase simulé, jeu initial de 74 fiches, **aucun coût**. Aucun appel à la base de production, aucune recette modifiée.
- **MCP FoodEatUp** (connecté, lecture seule) : `list_recipes` sur l'établissement du client → 101 recettes, 15 catégories, sans aucun champ de prix ni de coût.
- **Figma** : non consulté pour ce montage (le connecteur vient d'être autorisé). Le modèle Figma (`NHugytw5z60UV5cKH4s0qK`) est décrit d'après `scripts/figma/README.md`.

## Rapport : fonctionnalités vérifiées

Légende : ✅ vérifié dans l'app ou le code · 🟡 partiel ou en cours · ⏳ prévu · ❌ non vérifiable ici

| Fonction | État | Preuve |
|---|---|---|
| Accueil à 9 catégories, cartes tactiles | ✅ | Capture 01 (jeu initial : 74 fiches, 9 catégories) |
| Recherche instantanée tolérante (« cold foam ») | ✅ | Capture 02 : 3 résultats |
| Filtres Chaud / Glacé / Frozen | ✅ | Démo, catégorie Ube |
| Fiche recette (contenant, température, temps, rendement, allergènes, ingrédients et quantités, service) | ✅ | Captures 05 et 06 |
| Mode pas à pas avec la formatrice virtuelle, barre de progression, ingrédients concernés | ✅ | Étapes 1/3 à 3/3 de l'Iced Ube latte vanille |
| Filtre des 14 allergènes réglementaires | ✅ | « Sans lait » → 32 recettes compatibles |
| Mode rush (une carte lisible à 1 m) | ✅ | Capture de la démo |
| Choix de la langue (13 langues rapides + recherche) | ✅ | Capture. Traductions préparées une fois et gardées en cache, pas d'IA en direct |
| Voix de la formatrice | 🟡 | Voix françaises enregistrées (ElevenLabs). Les langues à figer restent à choisir (roadmap) |
| Academy : 2 parcours, 18 étapes, certification | ✅ écran / 🟡 contenu | Écran capturé, flouté dans la vidéo (marque du client). Les incohérences du livret sont « à trancher » (roadmap) |
| Hors connexion (copie locale, service worker) | ✅ code | `AGENTS.md`, tests E2E du dépôt. Non filmé |
| Espace Responsable (PIN, hub, food cost, achats, versions) | ✅ code | Non filmé : coûts confidentiels, PIN serveur |
| Fiche PDF équipe générée dans le navigateur, « au design de la maquette Figma », sans prix | ✅ | PDF réel téléchargé (Iced Ube latte vanille) |
| Classeur PDF Figma (recto équipe, recto-verso Responsable avec achats et food cost) | 🟡 | Fiches remplies à l'état du 06/10. Mise à jour du 11/10, export et dépôt automatique des PDF : « reste à faire » |
| Serveur MCP de l'app pour les agents (Claude, ChatGPT) | 🟡 | Ajouté dans Lovable le 26/10 : 3 outils en lecture, sans coûts. Pas publié, pas testé avec un vrai assistant |
| Carte client publique `/carte/:slug` (sans coûts, sans quantités) | ✅ code | Non filmée : la fonction serveur demande la base de production |

## Rapport : intégration FoodEatUp

| Opération | Réalité | Dit dans la vidéo |
|---|---|---|
| **Lire** les recettes FoodEatUp | `appelerFoodEatUp` (MCP, OAuth PKCE ou jeton par établissement, chaque appel journalisé) : `list_recipes`, `list_dishes`, `list_ingredients`, `list_products`, `list_suppliers`, `get_cadencier` | « lues dans mon logiciel central » |
| **Synchroniser** la copie locale | Tâche planifiée chaque nuit à **4 h (Paris)**, si FoodEatUp est connecté, plus le bouton « Mettre à jour depuis FoodEatUp » (Responsable). Les quantités viennent de FoodEatUp ; rien n'est supprimé, seulement désactivé et signalé. Dernière synchro documentée : 04/10 (74 recettes, 86 fiches ingrédients) | « synchronisation programmée chaque nuit » |
| **Modifier** une recette dans FoodEatUp | `update_recipe` et `update_ingredient` depuis l'espace Responsable : aperçu, phrase de confirmation exacte, version précédente gardée, journal d'audit. Jamais automatique | « rien ne part vers FoodEatUp sans sa confirmation » |
| **Actualiser** la tablette | Le catalogue est relu depuis la copie Cloud (cache de 5 min), puis gardé hors ligne | « continuer à fonctionner même sans connexion » |

Rien n'est présenté comme instantané ou bidirectionnel automatique. Aucune écriture n'a été faite pour la vidéo.

## Rapport : Figma et food cost

- **Fiche équipe.** Le PDF réel est généré par l'app « au design de la maquette Figma », sans prix ni coût. Il est montré dans la vidéo.
- **Fiche Responsable « achats & food cost ».**
  - Elle existe dans le classeur Figma (versos, calcul dans `scripts/recettes/versos_figma_calcul.js`) et dans l'écran Food cost de l'app.
  - Elle est montrée en **schéma aux montants masqués** : les prix d'achat et coûts réels ne sont pas affichés.
- **À connecter.** Mettre à jour le classeur Figma à l'état du 11/10, exporter les PDF fiche par fiche, puis les déposer automatiquement (`/api/public/cron/fiches-pdf`).
- **Pour filmer le vrai modèle Figma.** Autorise le connecteur Figma (Paramètres de claude.ai → Connecteurs), ou envoie-moi un export PNG du cadre.

## Synthèse du développement (historique Lovable + GitHub)

1. **03/10, la base, en une journée (171 commits).**
   - Premier prompt : app tablette « façon écran de caisse », données du jeu de 74 fiches en 9 catégories, règles de charte et d'UX tablette.
   - Puis : Lovable Cloud et copie hors ligne, connexion au MCP FoodEatUp (synchro de nuit, PIN Responsable, food cost), PDF.
   - Puis : pack Figma (35 photos, 74 fiches PDF recto/verso), langues, mode formation, PWA, page d'accueil, BD « Une saisie, pas dix » et la formatrice virtuelle.
2. **04/10, le terrain (144 commits).**
   - Corrections de connexion et filtre allergènes sur une page à part.
   - Hub Responsable, traductions (dont le cinghalais).
   - Décision clé de Michael : « Je ne veux pas d'IA : tout doit être pré-enregistré ». Les textes et les voix de la formatrice sont donc figés.
3. **05/10, la finition (67 commits).** Mode rush, visuels de substitution, import des photos et vidéos d'étapes, vitrine publique, séparation des deux parcours.
4. **06/10 → 12/10, les consignes du client.** Fiches à jour au 06/10 puis au 11/10 (73 fiches actives), photos officielles, thèmes d'application, dossier de reprise Figma.
5. **26/10.** Serveur MCP de l'app pour les agents (Lovable), pas encore publié.

**Répartition.**
- Lovable construit l'interface au fil des prompts.
- Claude (Claude Code, 36 PR) fait l'audit, les tests (68 fichiers unitaires et 14 de bout en bout), les imports de données, les PDF et les scripts Figma.
- Michael décide : périmètre, charte, refus de l'IA en direct, validation des fiches avec le client.

## Voix off

> Aujourd'hui, je vous présente une application que j'ai développée pour un client, pour 2 000 euros. Et ce n'est pas simplement un catalogue de recettes : elle est connectée à mon écosystème FoodEatUp.
>
> Les recettes et la formation tenaient dans un classeur papier de 161 pages. L'objectif était simple : rendre toutes ces informations accessibles directement sur tablette, au comptoir.
>
> J'ai donc créé une application tactile : les catégories, la recherche instantanée, les ingrédients, les quantités, les allergènes, et un mode pas à pas qui guide chaque préparation. Il y a même une Academy pour former les nouveaux équipiers.
>
> Mais le plus intéressant, c'est la connexion à FoodEatUp. Les recettes et leurs compositions sont lues dans mon logiciel central, puis recopiées dans l'application par une synchronisation programmée chaque nuit, pour continuer à fonctionner même sans connexion. Et quand un responsable corrige une recette, rien ne part vers FoodEatUp sans sa confirmation.
>
> Pour les fiches techniques, j'utilise Figma. Une fiche équipe, avec la photo, les ingrédients et les étapes. Et une fiche responsable, avec les prix d'achat et le coût de revient, réservée à l'espace Responsable. Les fiches existent déjà ; la mise à jour automatique des PDF reste à terminer.
>
> Pour réaliser ce projet, j'ai utilisé Lovable, Claude, FoodEatUp et Figma. Mon travail, c'est de comprendre le besoin métier, construire les bons outils, connecter les données, et vérifier que tout fonctionne vraiment sur le terrain. L'IA accélère le développement ; les décisions et la validation restent humaines.
>
> Au final, on passe d'un classeur papier de 161 pages à une application de recettes, de formation et de fiches techniques, reliée à FoodEatUp. C'est exactement le type de solution métier que je veux rendre accessible avec BraindCode. Et demain, je vous présenterai un nouveau projet, et mon travail du jour.

**Anonymisation.** Les mots qui nommaient le client ont été coupés de la voix off d'origine ; aucune nouvelle voix n'a été générée.

**Écarts avec le brief.**
- La section Figma dit « les fiches existent déjà ; la mise à jour automatique des PDF reste à terminer », pour coller à l'état réel.
- La synchronisation est décrite comme « programmée chaque nuit », et non comme instantanée.

## Storyboard

| Temps | Scène | Images |
|---|---|---|
| 0–10,6 | Le projet client | Accueil réel de l'app sur tablette (nom remplacé par « PEMA Coffee Shop »), badge « PROJET CLIENT — 2 000 € », Michael (pose officielle), logos BraindCode et FoodEatUp |
| 10,6–21,6 | Le problème | Carte « PEMA Coffee Shop · nom de démonstration » (aucune photo du lieu), pile de feuilles (illustration), compteur « 161 pages », « UN BESOIN MÉTIER CONCRET », arrivée de la tablette |
| 21,6–32,8 | L'application | Captures réelles synchronisées sur la voix : catégories, recherche, ingrédients, allergènes, pas à pas, Academy |
| 32,8–46,3 | Démo réelle, sans voix | Iced Ube latte vanille : accueil → catégorie Ube → filtre Glacé → fiche → ingrédients → étapes 1/3, 2/3, 3/3 → mode rush |
| 46,3–63,6 | FoodEatUp | Réponse réelle du MCP (101 recettes). Les 4 opérations (lire, synchroniser, corriger, tablette à jour) et leur statut. Serveur MCP de l'app « pas encore publié » |
| 63,6–78,5 | Figma | Fiche équipe PDF réelle. Fiche Responsable en schéma, montants masqués. Statut du classeur Figma |
| 78,5–95,1 | La méthode | 3 prompts Lovable réels. 87 prompts · 409 commits · 82 fichiers de tests. Logos Lovable, Claude, FoodEatUp, Figma. « L'IA accélère / l'humain décide » |
| 95,1–110,2 | Avant / après | Carte PEMA + 161 pages → étape du pas à pas. Pastilles recettes, formation, fiches techniques, reliée à FoodEatUp. Michael, deux pouces levés |
| 110,2–120 | Carton | PEMA COFFEE SHOP × FOODEATUP × FIGMA × BRAINDCODE · PROJET CLIENT — 2 000 € · « Un problème métier. Une solution sur mesure. » |

**Version 45 s** : accroche → application → FoodEatUp → carton.

## Publications

**LinkedIn**
> J'ai développé une application métier pour un client, à 2 000 €.
>
> Chez un coffee shop client, les recettes et la formation tenaient dans un classeur papier de 161 pages. Aujourd'hui, l'équipe a une application tablette pensée pour le comptoir :
>
> ☕ catégories, recherche instantanée, ingrédients et quantités, 14 allergènes
> 👣 un mode pas à pas avec une formatrice virtuelle, et un mode rush lisible à un mètre
> 🎓 une Academy pour les nouveaux équipiers
> 🔗 les recettes lues dans FoodEatUp et recopiées chaque nuit, pour fonctionner même hors connexion
> 📄 des fiches techniques au design Figma : une version équipe sans prix, une version responsable avec le food cost
>
> Construit avec Lovable et Claude : 87 prompts, 409 commits, des tests automatisés. Mais ce sont la compréhension du métier, les décisions et la validation avec le client qui font l'application.
>
> C'est le type de solution sur mesure que je veux rendre accessible avec BraindCode.
>
> #IA #Lovable #ClaudeCode #FoodEatUp #Restauration #BuildInPublic

**Instagram**
> Un classeur de 161 pages → une appli tablette ☕📱
> Recettes, pas à pas, allergènes, formation, fiches techniques
> Reliée à FoodEatUp 🔗
> Projet client : 2 000 €
> #applicationmetier #ia #lovable #foodeatup #coffeeshop #entrepreneur
