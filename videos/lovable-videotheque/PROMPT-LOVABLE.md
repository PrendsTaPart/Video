# Prompt Lovable · Vidéos de la Villa Beach (avec serveur MCP de publication)

À coller tel quel dans un nouveau projet Lovable.

---

Crée une application « Villa Beach · Nos vidéos » : un site qui présente les vidéos verticales du restaurant Villa Beach (la carte et les plats) et un serveur MCP qui permet à Claude d'y publier de nouvelles vidéos de la Villa Beach.

## 1. Données (Lovable Cloud / Supabase)

Table `videos` :
- `id` uuid, `slug` texte unique, `titre` texte, `collection` texte, `episode` entier (facultatif), `application` texte (facultatif), `etape` texte (TOFU / MOFU / BOFU, facultatif)
- `video_url` texte (MP4 HTTPS), `miniature_url` texte (facultatif), `format` texte (défaut `9:16`)
- `legende` texte (texte du post), `foodeatup_asset_id` entier (facultatif, numéro de l'asset dans la bibliothèque FoodEatUp)
- `publie` booléen (défaut false), `publie_le` timestamptz, `cree_le` timestamptz défaut now(), `source` texte (`import` ou `mcp`)

RLS : lecture publique des lignes `publie = true` uniquement ; aucune écriture depuis le navigateur. Les écritures passent par le serveur MCP (clé de service côté serveur).

Remplis la table au premier déploiement avec les 11 vidéos du fichier JSON suivant (un tableau d'objets aux mêmes noms de champs ; garde `publie` tel quel, `source = 'import'`) :
https://raw.githubusercontent.com/PrendsTaPart/Video/100c23c65a6f9a6d70bd0547b8f37ab706bc99c2/videos/lovable-videotheque/videos.json

Ne télécharge pas les vidéos : `video_url` et `miniature_url` sont des adresses publiques à lire directement dans la balise `<video>`.

## 2. Site

Style Villa Beach, élégant et chaleureux : fond très sombre `#0D0A07`, cartes `#1A140E`, doré `#D9B46A` pour les accents et les boutons, crème `#F6EFE2` pour les textes, titres en Cormorant Garamond (italique pour les accroches), textes courants en Inter, en français. Logo officiel (à utiliser tel quel, jamais redessiné) : https://raw.githubusercontent.com/PrendsTaPart/Video/100c23c65a6f9a6d70bd0547b8f37ab706bc99c2/videos/plats-instagram/logo-villa-beach.png — en haut de page et en pied de page.

- **Accueil** : logo, titre « Nos vidéos », sous-titre « La carte et les plats de la Villa Beach », filtres par collection (« La carte », « Nos plats »), recherche par titre, grille de cartes verticales 9:16 (miniature, titre). Au survol, la vidéo se lance sans le son. Bouton doré « Réserver une table » vers https://villabeach.foodeatup.fr.
- **Page vidéo** `/v/:slug` : lecteur vertical avec son, titre, collection, légende avec bouton « Copier la légende », bouton « Télécharger le MP4 », bouton « Réserver une table » (https://villabeach.foodeatup.fr), vidéos de la même collection en dessous. Balises Open Graph (titre, miniature, vidéo).
- **Page `/mcp`** : explique comment connecter Claude (adresse du serveur, en-tête d'authentification, liste des outils avec leurs paramètres, exemple de requête JSON-RPC).
- Responsive : 2 colonnes sur téléphone, 4 à 5 sur ordinateur.

## 3. Serveur MCP (fonction serveur `mcp`)

Crée une fonction serveur (edge function) exposée à `/functions/v1/mcp` qui implémente le protocole MCP en **Streamable HTTP** (JSON-RPC 2.0, version de protocole `2025-06-18`) :
- `POST` avec `initialize` → renvoie `protocolVersion`, `capabilities: { tools: {} }`, `serverInfo: { name: "videos-villa-beach", version: "1.0.0" }` et un `Mcp-Session-Id` ;
- `notifications/initialized` → réponse 202 sans corps ;
- `tools/list` et `tools/call` ; réponses `{"jsonrpc":"2.0","id":…,"result":…}`, résultats d'outils sous la forme `{ content: [{ type: "text", text: JSON }], structuredContent: … }`, erreurs métier avec `isError: true` ;
- `GET` → 405 ; CORS ouvert ; `OPTIONS` géré.

Authentification : en-tête `Authorization: Bearer <clé>`, comparée au secret `MCP_API_KEY` (à créer dans les secrets du projet, jamais écrit dans le code). Sans clé valide : erreur 401. Les outils de lecture et d'écriture exigent tous la clé.

Outils (descriptions en français, schémas JSON stricts) :
1. `list_videos` — filtres `collection`, `publie` (booléen), `q` (texte), `limit` (≤ 100), `offset`. Renvoie id, slug, titre, collection, publie, video_url, miniature_url, page_url.
2. `get_video` — par `slug` ou `id`.
3. `list_collections` — collections et nombre de vidéos.
4. `publish_video` — paramètres : `titre` (obligatoire), `video_url` (obligatoire, HTTPS, MP4), `collection` (obligatoire), `miniature_url`, `legende`, `slug` (sinon généré depuis le titre, unique), `format` (défaut 9:16), `episode`, `foodeatup_asset_id`. Avant d'écrire : requête HEAD sur `video_url` (et `miniature_url`) qui doit répondre 200 ; refuse sinon. Crée la ligne avec `publie = true`, `publie_le = now()`, `source = 'mcp'`. Si le slug existe déjà avec la même `video_url`, renvoie la vidéo existante sans doublon. Renvoie la ligne et `page_url` (adresse publique `/v/:slug`).
5. `update_video` — par `slug` : modifie titre, legende, collection, miniature_url, video_url (avec la même vérification HEAD).
6. `unpublish_video` — par `slug` : `publie = false` (la vidéo disparaît du site, rien n'est supprimé).
7. `republish_video` — par `slug` : `publie = true`.

Pas d'outil de suppression définitive.

Journalise chaque appel d'écriture dans une table `mcp_journal` (outil, slug, date, résumé) visible sur la page `/mcp` (10 derniers).

## 4. À me renvoyer quand c'est prêt

L'adresse publique du site, l'adresse exacte du serveur MCP et le nom du secret à remplir (`MCP_API_KEY`), pour que je connecte Claude avec :
`claude mcp add --transport http videos-villa-beach <adresse>/functions/v1/mcp --header "Authorization: Bearer <clé>"`
