# Plan'It — base de connaissance produit

**Tout ce qu'il faut pour écrire les 43 tutoriels sans rouvrir le dépôt
`PrendsTaPart/planit-app`.** Relevé par audit du code source (lecture seule),
commit `be5895d`.

Chaque libellé cité ici est **le texte exact affiché à l'écran** — c'est ce qui
permet à la voix off de nommer les boutons au mot près.

---

## 1. Ce qu'est Plan'It

Application mobile **Flutter 3** (Dart ^3.8) qui permet à un professionnel de
faire exécuter son travail par des agents IA :

1. Des **tâches planifiées** liées à des prompts, avec fréquence et statuts en temps réel.
2. Une **bibliothèque de prompts** personnels et publics, à variables.
3. Des **connexions** aux services Google et aux **serveurs MCP** (OAuth 2.0 + PKCE).
4. Un **chat agentique** où l'IA appelle réellement les outils des serveurs connectés.
5. Une **base de connaissance métier** (« Faire connaissance ») injectée dans chaque réponse.
6. Un **avatar 3D** personnalisable, qui parle.
7. Un **tableau de bord configurable** par widgets.
8. Des **crédits** consommés à l'action.

### Pile technique

| Couche | Technologie |
|---|---|
| Architecture | Clean Architecture par feature — `business` / `data` / `presentation` |
| État | `flutter_bloc` (Cubit) · injection `get_it` |
| Réseau | Dio 5 · **Laravel Sanctum** (token Bearer) |
| Stockage | `shared_preferences` · `flutter_secure_storage` (le token) |
| Temps réel | SSE (`core/services/sse_client.dart`, socle `core/chat_stream/`) |
| Push | `firebase_messaging` + `flutter_local_notifications` |
| Graphiques | `fl_chart` · **Polices** Sora (titres) + Manrope (corps) |
| 3D | modèles `.glb` rendus dans une iframe `three.js` · génération **Meshy AI** |

---

## 2. Design system — valeurs exactes

`lib/core/theme/app_colors.dart` · `app_text_styles.dart`

| Token | Valeur | Usage |
|---|---|---|
| `primary` | **`#4F2DF9`** | violet de marque, tableau de bord, chips |
| `primaryButton` | `#8236F8` | boutons secondaires |
| `accent` | **`#FE64D5`** | rose de marque |
| `success` | `#75AB00` | validations |
| `backgroundPage` | **`#EDEAFE`** | lavande, fond de toutes les pages claires |
| `textDark` | `#0B0516` | textes |
| `brandGradient` | `#FE64D5` → `#4F2DF9` (9 arrêts) | splash, boutons d'authentification |
| Chat MCP | `#241470` → `#4526D6` | fond dégradé sombre du chat |

**Règle du dépôt** : aucune couleur littérale dans les widgets, tout passe par
`AppColors`. Les tutoriels reprennent ces valeurs pour l'habillage.

---

## 3. Les 28 routes de l'application

`lib/core/config/app_routes.dart`

```
/splash  /onboarding  /signin  /signup  /verification
/forgot-password  /password-code-verification  /reset-password
/home  /dashboard  /tasks  /prompts  /chat
/api-connection  /kb  /kb-interview  /kb-preview  /kb-section-edit
/catalog-skills  /catalog-plugins  /profile
/notifications  /notification-settings
/credits  /credits-history  /invoices
/automation  /device-settings
```

Deep link MCP : **`planit://mcp/connected?mcp={key}`** (Android `AndroidManifest.xml`,
iOS `CFBundleURLSchemes: planit`).

---

## 4. Écran par écran — libellés exacts

### 4.1 Splash & onboarding

**Splash** (`/splash`) — fond `brandGradient`, logo blanc qui monte de −200 px en
`Curves.easeOut` sur 3 s, bouton **« Commencer »**.

**Onboarding** (`/onboarding`) — 3 pages, indicateur à points (`accent` pour la page active) :

| # | Titre | Description |
|---|---|---|
| 1 | **Planifie en un clic** | Organise tes tâches avec l'aide de l'IA. Garde une vision claire de tes priorités. |
| 2 | **Automatise tout** | Tes actions s'exécutent toutes seules selon ton planning. Moins d'effort, plus de résultats. |
| 3 | **Sois plus productif** | Analyse tes performances et découvre tes moments les plus efficaces. Gagne du temps chaque jour. |

### 4.2 Authentification

**Se connecter** (`/signin`) — « Connectez-vous à votre compte » · champs *Email*,
*Mot de passe* (œil barré) · lien **« Mot de passe oublié ? »** · bouton
**« Se connecter »** · pied « Vous n'avez pas de compte ? **Inscrivez-vous** ».

**Créer un compte** (`/signup`) — « Commencez à planifier intelligemment » ·
*Nom complet*, *Email*, *Mot de passe*, *Confirmer le mot de passe* · bouton
**« S'inscrire »** · « Vous avez déjà un compte ? **Connectez-vous** ».
Validation : **mot de passe d'au moins 6 caractères**, « Les mots de passe ne correspondent pas ».

**Vérifier le code** (`/verification`) — 6 cases · « Vous n'avez pas reçu de code? **Renvoyer** » ·
bouton **« Vérifier »**. Sur succès → `pushReplacementNamed('/signin')`.

**Mot de passe oublié ?** (`/forgot-password`) — « Entrez l'adresse e-mail associée
à votre compte. Nous enverrons votre code de confirmation. » · bouton **« Envoyer le code »**.

**Vérifiez votre code** (`/password-code-verification`) — « Entrez le code envoyé à
{email}. Veuillez le saisir ci-dessous. » · libellé *Code de vérification* ·
**« Renvoyer »** · **« Vérifier »** → `/reset-password`.

**Réinitialiser le mot de passe** (`/reset-password`) — « Entrez votre nouveau mot
de passe pour vous connecter » · *Nouveau mot de passe*, *Confirmer le mot de passe* ·
bouton **« Réinitialiser »** → `/signin`.

> ⚠️ **Pas d'authentification biométrique** dans l'application : aucune dépendance
> `local_auth`, aucun écran. Ne jamais l'annoncer dans un tutoriel.

### 4.3 Tableau de bord (`/dashboard`)

En-tête « **Bonjour {nom}** — Bienvenue dans votre espace Plan'it », bouton
**« Démarrer une conversation »**, icônes filtres et cloche.
Carte **« Aujourd'hui »**, KPI **« Taux de réussite »** et **« En attente »**,
bloc **« Activité — Touchez un jour pour le détail »**.

**Configurable** : « Vos indicateurs » → **« Configurer l'accueil »** (`home_config_screen`) :
onglets *Mes widgets* / *Ajouter*, réglages **Taille** (Petite · Moyenne · Grande),
**Type de graphique** (Tendance · Barres · Liste · Chiffre), **Période**, et un
**« Coût quotidien estimé de cette configuration »**. Actions : *Masquer*, *Afficher*,
*Supprimer* (« Vous pourrez le remettre à tout moment depuis le catalogue. »).

### 4.4 Tâches et routines (`/tasks`)

Fréquences réelles : **`once` · `daily` · `weekly` · `monthly`**.
Statuts : `pending` → `processing` → `completed` / `failed`.

**Guide de création** (`task_creation_guide`) — « Choisis comment tu veux créer ta tâche » :

| Option | Sous-titre |
|---|---|
| **Écrire librement une tâche** | Décris ta tâche en texte, l'IA fera le reste. |
| **Créer un nouveau prompt** | Construis ton propre modèle avec variables et format de sortie. |
| **Partir d'un prompt existant** | Sélectionne un modèle déjà prêt et remplis ses variables. |

**Routines** — écran distinct (`routine_form_screen`) : « Nouvelle routine »,
« Modifier la routine ». État vide : « Aucune routine pour l'instant — Ajoutez votre
première routine pour automatiser vos tâches récurrentes ».

**Historique** (`task_history`) — résultats copiables (« Texte copié dans le presse-papiers »).

### 4.5 Prompts (`/prompts`)

Onglets *Tous* / **« Mes prompts privés »** · « Recherche... » ·
« Aucun prompt ne correspond à ce filtre ».
Formulaire : *Nom du prompt*, *Description du prompt*, variables typées
(**Chaîne de caractères · Date · Email · Nombre**), **« Demander la publication »**,
**« Créer le prompt »** / **« Enregistrer »**. Retour : « Demande de publication envoyée ».

### 4.6 Connexion API (`/api-connection`)

Deux onglets : **Services** et **MCP**.

**Services Google et sociaux** — libellés exacts :

| Service | Description affichée |
|---|---|
| Gmail | Envoyez vos emails via vos automatisations |
| Google Calendar | Synchronisez vos tâches avec votre agenda |
| Google Drive | Stockez et partagez vos fichiers en toute sécurité |
| Google Slides | Créez et présentez vos diaporamas collaboratifs |
| Google Sheets | Gérez vos données avec des feuilles de calcul |
| LinkedIn | Publiez automatiquement vos contenus professionnels |
| Facebook | Planifiez vos publications sur votre page Facebook |
| Instagram | Automatisez vos posts et stories Instagram |
| Trello | Créez et suivez vos cartes directement depuis Plani't |
| Notion | Centralisez vos notes et tâches dans vos espaces Notion |

Rafraîchissement du token Google toutes les 3 minutes, ré-authentification transparente.

**MCP** — **« Ajouter un connecteur MCP »**, champ **« URL du serveur »** (« URL requise »),
boutons *Annuler* / *Ajouter*. Erreurs : « Le serveur MCP ne répond pas à cette adresse.
Vérifiez l'URL ou réessayez plus tard. », « Impossible d'ouvrir le navigateur ».
Vides : « Aucun service trouvé », « Aucun serveur MCP trouvé ».

**Flux de connexion** : tap *Connecter* → `POST /api/mcp/servers/{key}/connect` →
le backend renvoie `{auth_type:"oauth", url}` → navigateur externe → callback Laravel →
redirection `planit://mcp/connected?mcp={key}` → `McpDeepLinkService` rafraîchit la liste.

Carte connectée → bottom sheet : outils disponibles, test de connexion, déconnexion.

### 4.7 Chat agentique (`/chat`)

Accueil avec bulles d'agents MCP connectés · tiroir latéral d'historique par serveur ·
messages Markdown en streaming SSE · **tuile d'outils appelés** (nom, durée, statut) ·
**carte de confirmation obligatoire** avant toute action destructrice.

Bouton **« + »** de la barre de saisie : sélecteur de skills/plugins, **jauge de budget
du prompt fournie par le serveur**, éléments grisés avec la raison. Refus **409** si le
prompt système est plein.

Bandeau **« Faire connaissance »** tant que la base de connaissance n'est pas utilisable —
visibilité **pilotée par le backend**, jamais par un booléen local.

Vocal : « Parler à l'avatar », « 🎙 Écoute en cours… », « Écrivez ou maintenez le micro… ».
Assistant vocal mains libres nommé **Jarvis** ; nécessite l'autorisation
« Superposition aux autres applis » pour s'ouvrir depuis l'arrière-plan.

### 4.8 Base de connaissance (`/kb`)

**« Faire connaissance »** · compteur « {n} sections remplies » · badge **« Utilisable »**
(« L'assistant utilise déjà ces informations dans le chat. ») · astérisque sur les
**sections essentielles** (« elles suffisent pour que l'assistant vous connaisse »).

Boutons **« Commencer l'entretien »** / **« Continuer l'entretien »** et
**« Voir ce que l'assistant sait »**.

*Entretien* (`/kb-interview`) — streaming SSE, « Répondez à l'assistant… ».
*Aperçu* (`/kb-preview`) — « Ce que l'assistant sait », **lecture seule** « tel que
transmis à l'assistant à chaque message », lien « Modifier via les sections ».
*Édition* (`/kb-section-edit`) — « Décrivez cette partie de votre activité avec vos mots… ».

### 4.9 Skills & Plugins (`/catalog-skills`, `/catalog-plugins`)

Écran unique paramétré. « Rechercher un skill… » / « Rechercher un plugin… » ·
**« Actualiser »** (re-pull du dépôt GitHub du catalogue) · **« Importer un ZIP »**.
État vide : « Appuyez sur « Actualiser » pour récupérer le catalogue, ou importez votre
propre archive ZIP. » Liste fusionnée public + privé, badge « Perso », le privé masque
le public à slug égal.

**Activation refusée en 424** si des connecteurs MCP requis manquent → dialogue nommant
les connecteurs, bouton vers « Connexion API ».

### 4.10 Profil (`/profile`)

| Section | Entrées |
|---|---|
| **Profil** | Informations personnelles · Connexion API |
| **Assistant** | Choisir un avatar · **Faire connaissance** (« Présentez votre activité à l'assistant ») · **Skills** (« Compétences utilisables dans le chat ») · **Plugins** (« Ensembles de skills et de connecteurs ») |
| **Paramètres** | Notifications · **Voix & périphériques** · **Déconnexion** |

Édition (`profile_edit_screen`) : *Email*, *Nom d'utilisateur* → « Profil mis à jour avec succès ».

**Déconnexion** — dialogue **« Se déconnecter ? »** / « Cette action vous déconnectera de
votre compte. Voulez-vous continuer ? » / boutons **Non** et **Oui**. Révoque le token
Sanctum et supprime le token FCM.

### 4.11 Avatar 3D

**Bibliothèque** (`avatar_library_screen`) — onglets **« Mes avatars »** / **« Avatars par défaut »**.
Avatars fournis : **Brunette · Vroid · Brunette T · Chef Cuisinier · Commercial · Manager**.
Actions : *Renommer l'avatar*, dupliquer (« Avatar dupliqué ✓ »), supprimer
(« Cet avatar est fourni avec l'application : il sera masqué de votre bibliothèque et vous
pourrez le restaurer à tout moment. »). Activation → « Avatar activé ».

**Création** (`avatar_creation_screen`) — deux voies :
* **« Générer depuis ma photo »** — JPG · PNG · WEBP — max 10 Mo, « Pré-rempli par IA ».
* **« ou créer manuellement »** — *Identité* (Genre, Âge, Corpulence), *Apparence*
  (Peau, Yeux, Visage, Cheveux, Style, Couleur, Barbe), *Tenue* (Haut, Bas, Chaussures),
  *Accessoires* (Lunettes, Chapeau, Sac), *Style & Pose* (Style 3D, Pose, Expression).

Génération **~1-2 minutes via Meshy AI**.
> ⚠️ « **La synchronisation labiale n'est pas disponible sur les avatars générés par IA.** »

**Couleurs** (`avatar_color_screen`) — « Touchez une couleur pour l'appliquer en direct
sur l'avatar » : 🎨 Teinte de peau · 💇 Couleur des cheveux · 👕 Couleur de tenue ·
👁️ Couleur des yeux. « Les changements s'appliquent en temps réel dans le chat.
Appuyez sur Sauvegarder pour les conserver. » — **GRATUIT**.

**Voix de l'assistant** (`avatar_settings_screen`) — voix ElevenLabs proposées :

| Voix | `voice_id` | Caractère |
|---|---|---|
| Rachel | `21m00Tcm4TlvDq8ikWAM` | Douce et chaleureuse |
| Bella | `EXAVITQu4vr4xnSDxMaL` | Jeune et dynamique |
| Antoni | `ErXwobaYiN019PkySvjV` | Grave et naturelle |
| Josh | `TxGEqnHWrfWFTfGW9XjX` | Professionnel |

Phrase de test : « Bonjour, je suis votre assistant Planit. »

### 4.12 Notifications

**Centre** (`/notifications`) · **Préférences** (`/notification-settings`) avec « Tout désactiver » :

| Groupe | Réglages |
|---|---|
| **Tâches** | Rappels de tâches · Échéances dépassées · Confirmation de tâche terminée |
| **Prompts** | Validation d'un prompt public · Rejet d'un prompt public · Nouveau prompt disponible |

### 4.13 Crédits et factures

**Mes crédits IA** (`/credits`) — « Historique d'utilisation », « Acheter plus de crédits »,
« Voir mes factures », « Aucune action IA sur cette période ».

Packs : **Starter 100 crédits** · **PRO 500 crédits** · **Business 2000 crédits**.
Option **« Activer renouvellement automatique »**.
> « **Les crédits expirent à la fin du mois non utilisé.** »

**Mes factures** (`/invoices`) — « Aucune facture disponible pour le moment. Vos achats
apparaîtront ici. »

### 4.14 Voix & périphériques (`/device-settings`)

**« Voix & périphériques »** · **« Langue de Jarvis »** · **« Périphériques audio Bluetooth »**.
Vide : « Aucun périphérique audio appairé. Associez une oreillette ou un haut-parleur pour
utiliser Jarvis en mains libres. » · « Associer un périphérique » · états *Connecté* / *Appairé* ·
« Oublier ce périphérique ».

Vérifié à la capture du tutoriel 42 :

- **« Langue de Jarvis »** est un menu déroulant à quatre entrées — *Détection automatique*,
  *Français*, *العربية / Darija*, *English*. Français est la valeur par défaut.
- **« Associer un périphérique »** ne pose aucune feuille interne : le bouton **bascule vers
  les réglages Bluetooth du téléphone** (écran système, hors application). L'utilisateur
  y active le Bluetooth, choisit son oreillette, puis revient dans Plan'It.
- De retour, chaque ligne de la liste porte le nom du périphérique, l'état **« Appairé »**
  ou **« Connecté »** (un seul actif à la fois) et une **icône corbeille** à droite pour
  l'oublier. Aucune boîte de confirmation observée sur la capture.
- L'écran se rejoint depuis **Paramètres → « Voix & périphériques »**, juste au-dessus de
  « Déconnexion ».

---

## 5. Écarts relevés entre le produit et les fiches du MCP

À arbitrer avec l'équipe produit — **ne pas les narrer comme si de rien n'était**.

| # | Écart | Impact |
|---|---|---|
| 1 | **Fiche 1** promet « Activez la reconnaissance du visage ou de l'empreinte » et l'astuce « Activez la connexion biométrique ». **Aucune biométrie dans l'app.** | La voix off du tutoriel 01 ne le mentionne pas |
| 2 | L'email de vérification est **en anglais** (« Welcome to Plan'It! ») dans une app entièrement française — Gmail propose de le traduire | Contourné : la voix ne cite que le titre |
| 3 | Après vérification OTP, retour sur `/signin` : il faut ressaisir des identifiants tout juste choisis | Expliqué dans le tutoriel 00 |
| 4 | `vignette_spec` a des `titreCourt` **décalés d'un cran** : fiche 1 annonce « Créer son compte », fiche 2 « Se connecter », fiche 5 « Retrouver ses tâches » (module Tâches alors que la fiche traite des cartes de prompt) | On utilise `fiche.titreVignette`, qui est juste |
| 5 | Le gabarit de vignette du MCP est passé de 1280 × 720 à **1080 × 1920 (export 2160 × 3840)** en cours de production | Les vignettes ont été refaites au nouveau format |
| 6 | **Fiche 42 « Gérer ses appareils connectés »** promet « chaque appareil connecté à votre compte » et une coupure à distance (« Ouvrez Réglages puis "Appareils" », « Repérez les appareils inconnus », « Touchez "Déconnecter" »). **Cet écran n'existe pas.** L'écran réel est « Voix & périphériques » : langue de Jarvis et appairage Bluetooth des oreillettes | Le tutoriel 42 est monté sur l'application réelle. À corriger côté produit : `promesse`, `commentCaMarche`, `aQuoiCaSert` et l'écran de vignette `ecran-appareils` |

---

## 6. Ce qui reste à vérifier dans l'app pour certains tutoriels

Points non tranchés par le code lu, à confirmer par une capture d'écran :

- **Fiche 3 « Les premiers réglages de votre entreprise »** — aucun écran de réglages
  d'entreprise identifié. À recadrer, ou écran à venir.
- **Fiche 19 « Changer de modèle dans une conversation »** — pas de sélecteur de modèle
  repéré dans `mcp_chat_screen`.
- **Fiche 20 « Faire travailler plusieurs agents ensemble »** — à confirmer : le chat
  sélectionne un serveur MCP à la fois.
- **Fiches 31 / 32 (voix)** — commande vocale Bluetooth et écoute de la réponse : la
  capture d'écran seule ne suffira pas, prévoir la captation audio du téléphone.

---

## 7. Comment écrire une voix off à partir d'une fiche MCP

1. `tutoriel_spec(numero: N)` donne `titre`, `promesse`, `commentCaMarche[]`,
   `astuce.texte`, `cartes[]`.
2. **N0** (avatar) = « Bienvenue dans l'Académie Plan'It. Aujourd'hui : {titre}. {promesse} ».
3. **N1…Nk** = une ligne par étape de `commentCaMarche`, en **citant les libellés exacts
   de ce document** — c'est ce qui fait que le spectateur retrouve ce qu'il voit.
4. L'avant-dernière ligne reprend `astuce.texte`, **sauf si elle décrit une fonction
   absente du produit** (cf. §5).
5. **N10** = punchline invariable : « Vous planifiez une fois. Vos agents s'occupent du reste. Plan'It. »
6. Aucune ligne ne dépasse **6 secondes**.
