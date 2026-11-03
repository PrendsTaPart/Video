# Ajustements Prompts Claude Code — v2 (revue senior, 2026-07-06)

Revue critique du document `Prompts_Claude_Code_Soulayma` contre le cahier des
charges v1.0 (04/07/2026). **Ne remplace pas le document d'origine : c'est un
patch à appliquer dessus.** Chaque correction est numérotée C1…C15 avec le lot
concerné, le problème, et le texte corrigé à substituer.

---

## C1 — CRITIQUE · Numérotation des lots incohérente entre l'addendum et les prompts

**Problème.** Les deltas D1–D12 référencent une numérotation qui ne correspond
ni aux prompts ni au diagramme 3.4 du CdC :

| Delta | Lot indiqué | Lot RÉEL (doc prompts) |
|---|---|---|
| D1 (galerie templates) | « Lot 2 — Éditeur » | **Lot 1** (moteur de site) — le Lot 2 des prompts est le tunnel |
| D3 (éditeur CMS visuel) | « Lot 2/3 » | **Lot 1 + Lot 3** |
| D4 (espace client) | « Lot 4 — Tunnel » | **Lot 2** (tunnel) + Lot 4 (fidélité/OTP déjà là) |
| D6 (réservation publique) | « Lot 6 — Réservation » | **nouveau périmètre du Lot 1/2** — le Lot 6 des prompts est le KDS |
| D7 (design KDS) | « Lot 5 — KDS » | **Lot 6** — le Lot 5 des prompts est Cloudflare |
| D11 (dashboard hub) | Lot 12 | OK mais c'est un vrai lot d'un jour, pas une ligne de recette |
| Lot 9 texte | « kitchen_stations du lot 5 » | **du lot 6** |

Le diagramme 3.4 du CdC utilise ENCORE une autre numérotation (Lot 4 = Tunnel,
Lot 5 = KDS…). Trois numérotations pour les mêmes lots = collisions de branches
et de PR garanties.

**Correction.** Ajouter en tête du document ce tableau de correspondance
UNIQUE, et renuméroter les deltas :

```
Numérotation CANONIQUE (celle des prompts, qui fait foi pour les branches) :
Lot 0 Fondations · Lot 1 Site multi-pages (+D1 templates, +D3 éditeur visuel,
+D6 résa publique) · Lot 2 Tunnel (+D4 espace client) · Lot 3 Agent Configurateur
(+D2) · Lot 4 Fidélité/jeux/leads/blog (+D5 Caroline) · Lot 5 Domaines Cloudflare
· Lot 6 KDS (+D7 design) · Lot 7 QR table v2 · Lot 8 Connecteur Rapido ·
Lot 9 MCP scoping (+D9, D12) · Lot 10 Jarvis gateway (+D8) · Lot 11 Monétisation
(+D10, MAJ v5) · Lot 12 Durcissement/démo (+D11 dashboard) ·
Lots 13-15 Sprint 2 · B/F/D-lots NF525.
Le diagramme 3.4 du CdC se lit à travers ce tableau.
```

## C2 — CRITIQUE · Les prompts référencent des sections du CdC que la session ne verra jamais

**Problème.** « Schémas détaillés : voir sections 4.3, 6.2 et 7 du cahier des
charges (je te les colle si besoin) », « voir section 7.3 », « CDC 10.7 »…
Une session Claude Code fraîche n'a PAS le CdC : chaque référence est un trou
que l'agent comblera en inventant, ou une interruption pour demander.

**Correction.** Nouveau **Lot -1 (30 min, à faire AVANT le Lot 0)** :

```
Lot -1 — Specs dans le repo
Commit dans /docs/specs/ : cahier-des-charges-v6.md (export complet),
prompts-lots-v2.md (ce document), schemas/ (les sections 4.3, 6.2, 7.4, 10.7,
11.8 extraites en fichiers séparés). Chaque prompt de lot remplace « voir
section X du CdC » par « lis /docs/specs/schemas/<fichier>.md ». Aucun lot ne
démarre tant que ce commit n'est pas mergé.
```

## C3 — CRITIQUE · Modèle IA hardcodé et obsolète

**Problème.** Lot 3 : « API Anthropic, modèle claude-sonnet-4-6 ». Ce nom de
modèle n'existe pas (la famille actuelle est Claude 5 / Opus 4.8 / Haiku 4.5) ;
et hardcoder un ID de modèle dans un prompt le fige dans le code.

**Correction (Lot 3, tâche 1).** « …API Anthropic, **modèle lu depuis
`config('services.anthropic.model')` (défaut : `claude-sonnet-5`), jamais
hardcodé dans les services** ; prévoir un fallback configuré (dégradation vers
un modèle plus petit si erreur 529/overloaded) … ». Même règle pour le
MarketingAgentService (Lot 15).

## C4 — MAJEUR · Préambule commun : ajouts non négociables

Ajouter au préambule (après « Commits atomiques ») :

```
- Secrets : JAMAIS de clé/token/credential dans le code, les prompts, les
  fixtures, les tests ou les commits — uniquement .env + config(). Avant chaque
  PR : grep du diff pour sk_, api_key, token, password en dur.
- Aucun nouveau package Composer/NPM sans justification une ligne dans
  CLAUDE.md (nom, rôle, alternative écartée).
- Toute nouvelle surface publique (route, webhook, page) est derrière un
  feature flag par établissement (réutiliser le pivot features des plans) :
  un module qui déraille en prod se coupe par tenant sans déploiement.
- Toute date/heure métier (créneaux, fenêtres légales, planifications) est
  manipulée en Europe/Paris explicitement, jamais via le fuseau serveur.
- Migrations : toujours réversibles (down() réel) tant que le lot n'est pas
  mergé ; migrate:fresh interdit sur toute base partagée.
- Definition of done d'un lot : critères d'acceptation verts + suite de tests
  complète verte + revue de PR humaine (Soulayma) + CLAUDE.md à jour. Pas de
  merge sans les quatre.
```

## C5 — MAJEUR · Lot 2 (tunnel) : trous de robustesse paiement

Ajouter aux tâches du Lot 2 :

```
7. Robustesse paiement : vérification de signature sur TOUS les webhooks Stripe
   (constructEvent, secret dédié par endpoint) ; clé d'idempotence Stripe sur la
   création du PaymentIntent (uuid de commande) ; gestion des événements
   payment_intent.payment_failed et .canceled (commande → statut échouée,
   créneau libéré ATOMIQUEMENT) ; job de réconciliation horaire qui requête les
   PaymentIntents « succeeded » sans commande confirmée (webhook perdu) et
   répare ; devise unique EUR assertée côté serveur.
8. Décrément de stock : à la confirmation, décrémenter les ingrédients via les
   fiches techniques recettes (même mécanique que validate_production). Si la
   fiche n'existe pas : ne rien décrémenter et logguer (pas d'invention de
   coûts). C'est le flux « une commande met à jour les stocks » promis par le
   CdC — il n'était dans AUCUN lot.
```

## C6 — MAJEUR · Lot 10 (Jarvis) : quota vérifié seulement à l'ouverture

**Problème.** « Laravel refuse l'ouverture de session si quota épuisé » + usage
posté à la fermeture : une session ouverte à 59 min de quota peut durer 3 h
gratuites ; un crash du gateway avant le POST de fermeture = usage perdu.

**Correction (Lot 10, tâche 4).** « Comptage : le gateway POSTe l'usage par
**battements de 60 s** (upsert incrémental sur jarvis_usage, clé de session),
pas seulement à la fermeture ; Laravel renvoie `quota_remaining` à chaque
battement et le gateway **termine la session proprement** (message vocal
« quota épuisé ») quand il tombe à 0. Un battement manquant > 3 min = session
considérée morte, usage arrêté au dernier battement. »

Ajouter à la tâche 2 : « Dégradation : si Deepgram ou ElevenLabs sont
indisponibles, réponse vocale d'erreur pré-enregistrée (asset local) puis
fermeture propre — jamais de silence. »

## C7 — MAJEUR · Lot 13 (campagnes) : fuseau horaire des fenêtres légales

Ajouter à la tâche 3 : « Les fenêtres légales (20h–8h, dimanche, fériés)
s'évaluent **en Europe/Paris** quel que soit le TZ du serveur ou du client —
tests Feature avec Carbon::setTestNow sur les DEUX bords de chaque fenêtre
(19h59/20h00, 7h59/8h00, samedi 23h59/dimanche 0h00) et sur un changement
d'heure été/hiver. » (Un serveur en UTC enverrait légalement à 20h30 Paris.)

## C8 — MAJEUR · Lot 3 (agent) : allowlist de contexte (RGPD)

Ajouter aux garde-fous : « Le contexte envoyé à l'API Anthropic est construit
par **allowlist explicite** (établissement, menu, horaires, photos, charte) —
JAMAIS de données clients (noms, emails, téléphones, historique d'achat
individuel). Pour le MarketingAgentService (Lot 15) : segments et agrégats
uniquement, jamais de lignes clients nominatives. Test : le payload construit
pour un établissement de seed ne contient aucun email/téléphone. »

## C9 — Lot 5 (Cloudflare) : cas d'erreur manquants

Ajouter : « Gestion d'erreurs CF : 429 (backoff + retry job), token
absent/invalide en env (l'écran Domaine affiche "indisponible", le reste du
module ne casse pas), quota custom hostnames atteint (message explicite),
changement de domaine (delete ancien AVANT create nouveau, jamais deux actifs),
et un domaine déjà pris par un autre tenant → refus (contrainte unique globale
sur hostname). »

## C10 — Lot 6 (KDS) : jeton d'affichage = surface d'attaque

Ajouter : « Le display_token donne un accès sans login : le rendre long
(random 40+), le scoper en LECTURE + bump uniquement (aucune donnée client
au-delà du prénom + notes de commande), throttle par token, et journaliser la
régénération. La page /kds/{token} envoie X-Robots-Tag: noindex. »

## C11 — Lot 8 (Rapido) : formats vérifiés en pratique

Confirmé en production réelle (tests du 2026-07-02 sur RapidoCMS) :
`schedule_draft_tool` attend `post_heure` au format **`H:i:s` avec des
deux-points** (ex. `23:35:00`) — la description de l'outil qui dit `H-i-s` est
FAUSSE ; et le serveur compare l'heure programmée à l'horloge **Europe/Paris**.
Corriger la ligne du Lot 8 (« schedule_draft_tool (post_date 'Y-m-d',
post_heure 'H:i:s' — attention la doc de l'outil ment) ») et coder le client
en conséquence + test d'intégration sandbox.

## C12 — Lot 1 (SSR) : cache et pages non publiées

Ajouter : « Cache de réponse par page publiée (Cache::tags par storefront,
purge à la publication et à l'édition) — le SSR Inertia par requête ne tiendra
pas la charge d'un site indexé sinon. Pages non publiées : 404 + noindex, y
compris via le domaine custom. »

## C13 — Stratégie de branches quand les lots se chevauchent

Le Gantt fait tourner jusqu'à 4 lots en parallèle sur une seule dev. Ajouter au
préambule :

```
- Ordre de merge = ordre de dépendance du tableau C1, pas ordre de fin.
- Rebase quotidien de chaque branche de lot sur main ; conflit > 30 min =
  signal que deux lots touchent le même fichier → extraire la partie commune
  dans un mini-lot mergé d'abord.
- Les migrations d'un lot non mergé ne sont JAMAIS référencées par un autre lot
  (le Lot 9 attend le merge du Lot 6 pour update_kds_item_status, il ne pointe
  pas sa branche).
```

## C14 — Lot 12 : la démo a besoin d'un tenant de démo reproductible

Ajouter tâche 0 : « Seeder DemoEstablishmentSeeder : un établissement complet
(menu 25 plats avec photos, fiches techniques, 3 employés avec rôles distincts,
2 postes KDS + pass, programme fidélité, 50 clients, 200 commandes historisées
pour les segments RFM) — idempotent, rejouable, utilisé par TOUTES les recettes
de lot et la démo S4/S7. Sans lui, chaque critère d'acceptation se teste sur
des données différentes. »

## C15 — Dépendances externes : à déclencher AVANT le code

Checklist fondateurs à lancer J1 (chaque item a des semaines de délai) :
- [ ] Approbation API Google Business Profile (Lot 4/GBP — délai en semaines)
- [ ] Compte Google Wallet Issuer
- [ ] Profil WhatsApp Business + premiers templates soumis à Meta (bloque Lot 14)
- [ ] Sender ID SMS déclaré + numéro vocal sortant (bloque Lot 13/14)
- [ ] Token Cloudflare + zone sites.foodeatup.com (bloque Lot 5)
- [ ] Ticket infra Reverb/WSS (reverse proxy AWS) — semaine 1, pas semaine 3
- [ ] AWS KMS provisionné (bloque B1/NF525 — les choix crypto de P0 en dépendent)
- [ ] Clés API : Anthropic, Deepgram, ElevenLabs (quota vérifié), Stripe metered prices
