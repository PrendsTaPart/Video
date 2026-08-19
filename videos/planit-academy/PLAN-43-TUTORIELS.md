# Académie Plan'It — plan de production des 43 tutoriels

Plan de fabrication de la série complète, calé sur les fiches du **MCP Plan'It
Video** (`tutoriel_lister` → 43 fiches, toutes en statut `a_produire`) et sur les
fonctionnalités réellement présentes dans le dépôt `PrendsTaPart/planit-app`
(lecture seule).

**État au 19/08/2026** : 5 / 43 montés — tutoriels **00** « Créer son compte »,
**01** « Se connecter », **02** « Retrouver son mot de passe », **05** « Utiliser
une carte de prompt » et **06** « Chercher la bonne carte de prompt ». Les trois
premiers sont déposés et en ligne sur leur fiche MCP.

---

## 1. Le pipeline, validé sur le tutoriel 00

Cinq étapes, dont trois automatisées. C'est ce cycle qu'on répète 42 fois.

| # | Étape | Outil | Automatisé |
|---|---|---|---|
| 1 | **Capturer** l'écran du parcours dans l'app | Téléphone, capture d'écran | non |
| 2 | **Analyser** les écrans image par image et écrire le découpage | ffmpeg + lecture des frames | oui |
| 3 | **Écrire** la voix off, une ligne par plan (≤ 6 s) | fiche MCP → texte | oui |
| 4 | **Générer** la voix | ElevenLabs — voix *Perle* `UaGvaD7NWzU5mJNoUqoY` | oui |
| 5 | **Monter** : intro + avatar + démo + outro | `build_bumpers.py` / `build_video.py` | oui |
| 6 | **Déposer** la vidéo sur la fiche | `enregistrer_video` (MCP) | oui |

### Les trois règles issues du tutoriel 00

1. **Chaque plan dure exactement sa ligne de voix off.** Le montage lit la durée
   du MP3 et en déduit la vitesse du plan. Aucune durée n'est fixée au jugé —
   c'est ce qui a fait dériver les tutoriels FoodEatUp.
2. **Aucune ligne de voix off ne dépasse 6 secondes.** Au-delà, elle déborde de
   son plan et le décalage s'accumule.
3. **Zéro génération Higgsfield.** Les habillages sont dessinés (Pillow + ffmpeg)
   à partir des tokens réels de `app_colors.dart`. Règle du dépôt, respectée.

### Constantes de la série

| Élément | Valeur |
|---|---|
| Format | 1080 × 1920 (9:16) · 30 fps · H.264 High / AAC 48 kHz |
| Durée cible | 50 à 70 s (les fiches annoncent « 1 min ») |
| Voix off | ElevenLabs *Perle*, `eleven_multilingual_v2` |
| Avatar | HeyGen, avatar féminin, fond transparent, ≈ 11 s d'ouverture |
| Ouverture / fin | `build_bumpers.py`, titre et couleur pris sur la fiche |
| Punchline | « Vous planifiez une fois. Vos agents s'occupent du reste. » — **invariable** |
| Polices | Sora (titres) · Manrope (corps) — `videos/_shared/fonts/` |

---

## 2. Les 43 fiches, par étape du parcours

Le MCP range les tutoriels en **6 étapes de parcours** — c'est l'ordre dans
lequel un utilisateur découvre le produit, et donc l'ordre de production.

### Étape 1 — Ouvrir la porte (4)

| N° | Slug | Titre | Module |
|---:|---|---|---|
| **0** | `creer-son-compte` | Créer son compte Plan'It | configuration-onboarding |
| 1 | `se-connecter` | Se connecter à son espace | configuration-onboarding |
| 2 | `retrouver-son-mot-de-passe` | Retrouver son mot de passe | configuration-onboarding |
| 3 | `premiers-reglages` | Les premiers réglages de votre entreprise | configuration-onboarding |

### Étape 2 — Brancher ses logiciels (3)

| N° | Slug | Titre | Module |
|---:|---|---|---|
| 12 | `brancher-google` | Brancher Google Agenda et Gmail | connexions-api-mcp |
| 13 | `brancher-un-serveur-mcp` | Brancher un serveur MCP | connexions-api-mcp |
| 14 | `gerer-ses-connecteurs` | Gérer et débrancher ses connecteurs | connexions-api-mcp |

### Étape 3 — Faire connaissance (5)

| N° | Slug | Titre | Module |
|---:|---|---|---|
| 21 | `deposer-ses-documents` | Déposer ses documents dans la base de connaissance | base-de-connaissance |
| 22 | `organiser-sa-base-de-connaissance` | Organiser sa base de connaissance | base-de-connaissance |
| 23 | `mettre-a-jour-un-document` | Mettre à jour un document déjà déposé | base-de-connaissance |
| 24 | `verifier-une-source` | Vérifier d'où vient une réponse | base-de-connaissance |
| 25 | `retirer-un-document` | Retirer un document de la base | base-de-connaissance |

### Étape 4 — Parler à ses agents (15)

| N° | Slug | Titre | Module |
|---:|---|---|---|
| 15 | `premiere-conversation` | Sa première conversation avec un agent | chat-agentique |
| 16 | `donner-du-contexte-dans-le-chat` | Donner du contexte dans une conversation | chat-agentique |
| 17 | `reprendre-une-conversation` | Reprendre une conversation plus tard | chat-agentique |
| 18 | `corriger-une-reponse` | Corriger une réponse au lieu de tout refaire | chat-agentique |
| 19 | `changer-de-modele` | Changer de modèle dans une conversation | chat-agentique |
| 20 | `parler-a-plusieurs-agents` | Faire travailler plusieurs agents ensemble | chat-agentique |
| 30 | `confirmer-une-action-sensible` | Confirmer une action sensible | chat-agentique |
| 31 | `parler-a-son-agent-a-la-voix` | Parler à son agent à la voix | chat-agentique |
| 26 | `comprendre-les-skills` | Comprendre à quoi servent les skills | skills-plugins |
| 27 | `activer-un-skill` | Activer un skill sur un agent | skills-plugins |
| 28 | `installer-un-plugin` | Installer un plugin | skills-plugins |
| 29 | `desactiver-un-skill` | Désactiver un skill ou un plugin | skills-plugins |
| 32 | `ecouter-la-reponse` | Écouter la réponse de son agent | profil-avatar-3d |
| 33 | `choisir-son-avatar` | Choisir l'avatar 3D de son agent | profil-avatar-3d |
| 34 | `personnaliser-la-fiche-agent` | Personnaliser la fiche de son agent | profil-avatar-3d |

### Étape 5 — Faire travailler (8)

| N° | Slug | Titre | Module |
|---:|---|---|---|
| 5 | `utiliser-une-carte-de-prompt` | Utiliser une carte de prompt | bibliotheque-prompts |
| 6 | `chercher-une-carte-de-prompt` | Chercher la bonne carte de prompt | bibliotheque-prompts |
| 7 | `enregistrer-sa-propre-carte` | Enregistrer sa propre carte de prompt | bibliotheque-prompts |
| 9 | `partager-une-carte-a-son-equipe` | Partager une carte à son équipe | bibliotheque-prompts |
| 8 | `transformer-une-carte-en-routine` | Transformer une carte en routine | taches |
| 10 | `lancer-une-tache-longue` | Lancer une tâche qui prend du temps | taches |
| 11 | `suivre-ses-taches` | Suivre l'avancement de ses tâches | taches |
| 38 | `creer-une-automatisation` | Créer sa première automatisation | automatisations |

### Étape 6 — Piloter (8)

| N° | Slug | Titre | Module |
|---:|---|---|---|
| 4 | `lire-son-tableau-de-bord` | Lire son tableau de bord | accueil-statistiques |
| 35 | `lire-le-temps-gagne` | Lire le temps gagné par vos agents | accueil-statistiques |
| 36 | `suivre-ses-indicateurs` | Choisir les indicateurs de son accueil | accueil-statistiques |
| 37 | `recevoir-un-rapport-automatique` | Recevoir un rapport automatique | notifications |
| 39 | `regler-ses-notifications` | Régler ses notifications | notifications |
| 40 | `comprendre-ses-credits` | Comprendre ses crédits | credits-facturation |
| 41 | `gerer-son-abonnement` | Gérer son abonnement et ses factures | credits-facturation |
| 42 | `gerer-ses-appareils` | Gérer ses appareils connectés | appareils |

---

## 3. Les captures d'écran — le vrai goulot

> **Où sont les captures.** Elles arrivent dans le dossier Drive partagé
> **« enregistrements d'écran »** (`1HTE6WPmD52qBSV0t-uYKF1a-OGbmtBgD`). Chaque
> fichier y est numéroté selon la liste de la personne qui filme — cette
> numérotation **ne correspond pas** aux numéros de tutoriel : rattacher chaque
> capture à sa fiche **par son contenu**, pas par son titre. Relevé du
> 19/08/2026 : « Vidéo 2 » → tuto 01, « Vidéo 3 » → tuto 02, « Vidéo 6 »
> (création et modification d'une tâche) → tuto **05**, « Vidéo 9 » (liste des
> prompts et recherche) → tuto **06**.
>
> Les captures récentes sont en **392 × 852** et sonores, sans filigrane CapCut :
> le recadrage est `crop=392:824:0:28` (barre de statut Android), contre
> `crop=590:1180:0:80` pour les trois premières.

Tout le reste est automatisé. **Seule la capture d'écran demande un téléphone et
un compte dans le bon état.** Elle se fait donc en **lots**, une session de
capture couvrant plusieurs tutoriels d'un même écran.

> Ne pas capturer tutoriel par tutoriel. Une session de 20 minutes sur l'écran
> Chat fournit la matière de 8 vidéos ; découpée après coup, elle coûte huit fois
> moins cher que huit captures séparées.

| Lot | Écrans de l'app | Tutoriels | Prérequis de compte |
|---|---|---|---|
| **A** | Splash, onboarding, signin, signup, OTP, reset, réglages | 0 · 1 · 2 · 3 | **compte neuf, jamais connecté** |
| **B** | Connexions API — onglets *Services* et *MCP*, bottom sheet | 12 · 13 · 14 | compte vierge, aucun connecteur |
| **C** | Base de connaissance — accueil, entretien SSE, aperçu, édition | 21 · 22 · 23 · 24 · 25 | Google branché (lot B) |
| **D** | Chat MCP — accueil, tiroir, bulles, outils, confirmation, « + » | 15 · 16 · 17 · 18 · 19 · 20 · 30 · 31 | **≥ 1 serveur MCP connecté (lot B)** |
| **E** | Skills & Plugins — listes, recherche, interrupteurs, ZIP | 26 · 27 · 28 · 29 | connecteurs MCP requis présents, sinon 424 |
| **F** | Profil, avatar 3D — génération, personnalisation, chat parlant | 32 · 33 · 34 | profil complété |
| **G** | Bibliothèque de prompts — liste, recherche, création, publication | 5 · 6 · 7 · 9 | ≥ 3 prompts existants |
| **H** | Tâches — liste, formulaire, détail, historique | 8 · 10 · 11 | ≥ 1 prompt (lot G) |
| **I** | Automatisations N8N | 38 | workflow disponible |
| **J** | Tableau de bord peuplé, filtres, indicateurs | 4 · 35 · 36 | **historique d'exécutions (lots G/H)** |
| **K** | Centre de notifications, préférences, ouverture depuis push | 37 · 39 | notifications reçues |
| **L** | Crédits, historique de consommation, factures | 40 · 41 | consommation réelle |
| **M** | Paramètres des périphériques (Bluetooth…) | 42 | casque appairé |

### Trois dépendances à ne pas inverser

1. **D après B.** L'écran d'accueil du chat affiche les bulles des serveurs MCP
   *connectés*. Sans connecteur, il est vide et il n'y a rien à filmer.
2. **E après B.** L'activation d'un plugin est refusée en **424** si un
   connecteur MCP requis manque — et le tutoriel 28 doit montrer le cas nominal.
3. **J en dernier.** Le tutoriel 00 se termine sur « Taux de réussite 0 % » et
   « Aucune activité sur la période ». Un tutoriel *tableau de bord* sur un compte
   vide ne montre rien : il faut d'abord que les lots G et H aient généré des
   exécutions.

---

## 4. Vagues de production

Six vagues, dans l'ordre du parcours utilisateur — qui est aussi l'ordre qui
satisfait les dépendances.

| Vague | Lots | Tutoriels | Nb | Sortie |
|---|---|---|---:|---|
| 1 — Ouvrir la porte | A | 0 · 1 · 2 · 3 | 4 | **0 · 1 · 2 faits**, reste 3 |
| 2 — Brancher | B | 12 · 13 · 14 | 3 | |
| 3 — Faire connaissance | C | 21 → 25 | 5 | |
| 4 — Parler aux agents | D · E · F | 15-20 · 26-34 | 15 | vague la plus lourde |
| 5 — Faire travailler | G · H · I | 5-11 · 38 | 8 | **5 · 6 faits** (captures hors vague) |
| 6 — Piloter | J · K · L · M | 4 · 35-37 · 39-42 | 8 | dépend des vagues 4-5 |

**Charge par vidéo, une fois le pipeline en place** : ≈ 10 lignes de voix off
(≈ 100 crédits ElevenLabs / ≈ 0,02 $ la ligne), 1 plan avatar HeyGen, un rendu
de 2-3 minutes. **La capture reste le poste dominant.**

### Cadence proposée

Une vague par semaine, captures groupées en début de semaine, montage et dépôt
en fin de semaine. **6 semaines pour les 42 restants**, la vague 4 pouvant être
scindée en deux (D+E, puis F) si 15 vidéos en une semaine est trop dense.

---

## 5. Gabarit de voix off réutilisable

Les fiches MCP sont structurées à l'identique — la voix off se dérive
mécaniquement de `tutoriel_spec(numero: N)` :

| Ligne | Source dans la fiche | Rôle |
|---|---|---|
| N1 | `commentCaMarche[0]` | l'écran de départ |
| N2…Nk | `commentCaMarche[1..]` | une ligne par étape |
| avant-dernière | `astuce.texte` | le conseil qui évite l'erreur classique |
| dernière | `promesse` reformulée | ce qui est acquis |
| **N final** | punchline, invariable | signature |

Le tutoriel 00 suit exactement ce gabarit : N3 reprend mot pour mot l'astuce de
l'agent *nina* (« utilisez votre adresse professionnelle plutôt qu'une adresse
personnelle »), et N9 reformule la promesse.

**Les fiches portant des `cartes` de prompt** (13, 5, et d'autres) méritent un
plan supplémentaire montrant la carte à l'écran, avec son `coutEstime` et son
`connecteurRequis`. À traiter comme un plan de plus, pas comme une vidéo à part.

---

## 6. Vignettes

Chaque fiche a sa spécification de vignette (`vignette_spec`) : **1280 × 720,
exporté en 2560 × 1440**, avec une couleur de module, une pose d'avatar et une
règle de composition.

| Variante | Règle | Exemple |
|---|---|---|
| **A** | Concept ou découverte : l'avatar domine | 0 (`ecran-splash`), 15 (`ecran-chat-accueil`) |
| **B** | Manipulation à l'écran : l'écran domine | 13 (`ecran-mcp-liste`), 5 (`ecran-taches-liste`) |

Couleurs de module relevées : Authentification `#4F2DF9` · Tâches `#6A2EF5` ·
Connexions API & MCP `#8236F8` · Chat agentique `#9438F0`. Ce sont des dérivés
de `AppColors.primary` / `primaryButton` — la palette est cohérente avec l'app.

Les vignettes se rendent via la route `/rendu/vignette?numero=N` puis se déposent
avec `enregistrer_vignette`. **À industrialiser en une passe** une fois les 43
captures disponibles, plutôt qu'au fil de l'eau.

---

## 7. Points à trancher

1. **Fiche 5 — incohérence de vignette.** La fiche porte sur *Utiliser une carte
   de prompt* (module `bibliotheque-prompts`), mais sa `vignette_spec` annonce
   `titreCourt: "Retrouver ses tâches"`, module *Tâches*, écran
   `ecran-taches-liste`. L'un des deux est faux — à corriger côté MCP avant de
   produire la vignette.
2. **Email de vérification en anglais.** « Welcome to Plan'It! » dans une app
   entièrement française (Gmail propose de le traduire). Visible dans le tutoriel
   00. À remonter au backend.
3. **Retour au login après vérification OTP.** `verification_code.dart` renvoie
   sur `/signin`, obligeant à ressaisir des identifiants tout juste choisis. Le
   tutoriel 00 l'explique ; une connexion automatique le supprimerait.
4. **Tutoriel 3 « premiers réglages ».** Aucun écran de réglages d'entreprise
   identifié dans `planit-app` lors de la lecture. À confirmer : écran existant,
   à venir, ou fiche à re-cadrer ?
5. **Voix de l'avatar HeyGen.** Soit importer *Perle* dans HeyGen pour une voix
   unique sur toute la série, soit assumer deux voix distinctes (avatar / voix
   off). Recommandation : **une seule voix**, plus lisible à l'échelle de 43
   épisodes.
6. **Tutoriels 31 et 32 (voix).** Ils portent sur du son — commande vocale
   Bluetooth et écoute de la réponse. La capture d'écran seule ne suffira pas :
   prévoir la captation audio du téléphone.

---

## 8. Suivi

Le MCP est le tableau de bord de la série :

- `videos_manquantes` → ce qui reste à produire
- `enregistrer_video(numero, videoUrl, duree, chapitres)` → dépôt d'un montage
- `enregistrer_vignette` · `enregistrer_transcription` · `ajouter_carte_prompt`
- `definir_statut` → passage de `a_produire` à en ligne

Un tutoriel n'est **terminé** que lorsque la vidéo, la vignette et la
transcription sont déposées sur sa fiche.
