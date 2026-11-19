# Prompt Lovable · Vidéothèque FoodEatUp & Villa Beach (avec serveur MCP de publication)

À coller tel quel dans un nouveau projet Lovable.

---

Crée une application « Vidéothèque FoodEatUp » : un site qui présente toutes nos vidéos verticales (séries FoodEatUp et Villa Beach) et un serveur MCP qui permet à Claude d'y publier de nouvelles vidéos.

## 1. Données (Lovable Cloud / Supabase)

Table `videos` :
- `id` uuid, `slug` texte unique, `titre` texte, `collection` texte, `episode` entier (facultatif), `application` texte (facultatif), `etape` texte (TOFU / MOFU / BOFU, facultatif)
- `video_url` texte (MP4 HTTPS), `miniature_url` texte (facultatif), `format` texte (défaut `9:16`)
- `legende` texte (texte du post), `foodeatup_asset_id` entier (facultatif)
- `publie` booléen (défaut false), `publie_le` timestamptz, `cree_le` timestamptz défaut now(), `source` texte (`import` ou `mcp`)

RLS : lecture publique des lignes `publie = true` uniquement ; aucune écriture depuis le navigateur. Les écritures passent par le serveur MCP (clé de service côté serveur).

Remplis la table au premier déploiement avec les 42 vidéos du fichier JSON suivant (un tableau d'objets aux mêmes noms de champs ; garde `publie` tel quel, `source = 'import'`) :
https://raw.githubusercontent.com/PrendsTaPart/Video/059d2742a022487638a8881df5ec9e6b06e96c41/videos/lovable-videotheque/videos.json

Ne télécharge pas les vidéos : `video_url` et `miniature_url` sont des adresses publiques à lire directement dans la balise `<video>`.

## 2. Site

Style : fond nuit `#0F1A23`, cartes `#16242F`, accent bleu `#007BFF`, une seule action orange `#FFA500` par écran, police Manrope, textes en français.

- **Accueil** : titre « Nos vidéos », compteur, filtres par collection (Série · Les 10 applications FoodEatUp, Villa Beach, Villa Beach · plats…), recherche par titre, grille de cartes verticales 9:16 (miniature, titre, collection, badge épisode / étape si présents). Au survol, la vidéo se lance sans le son.
- **Page vidéo** `/v/:slug` : lecteur vertical avec son, titre, collection, légende avec bouton « Copier la légende », bouton « Télécharger le MP4 », vidéos de la même collection en dessous. Balises Open Graph (titre, miniature, vidéo).
- **Page `/mcp`** : explique comment connecter Claude (adresse du serveur, en-tête d'authentification, liste des outils avec leurs paramètres, exemple de requête JSON-RPC).
- Responsive : 2 colonnes sur téléphone, 4 à 5 sur ordinateur.

## 3. Serveur MCP (fonction serveur `mcp`)

Crée une fonction serveur (edge function) exposée à `/functions/v1/mcp` qui implémente le protocole MCP en **Streamable HTTP** (JSON-RPC 2.0, version de protocole `2025-06-18`) :
- `POST` avec `initialize` → renvoie `protocolVersion`, `capabilities: { tools: {} }`, `serverInfo: { name: "videotheque-foodeatup", version: "1.0.0" }` et un `Mcp-Session-Id` ;
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
`claude mcp add --transport http videotheque <adresse>/functions/v1/mcp --header "Authorization: Bearer <clé>"`
