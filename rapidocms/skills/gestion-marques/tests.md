# Tests — gestion-marques

Tests de comportement (prompt-based). Chaque scénario = Given / When / Then.

---

## T1 — Création de marque (chemin nominal)
**Given** : la charte `./rapido-kb/charte-graphique.md` existe (couleurs `#1B2A41,#00A8F0`,
typo *Poppins*), l'utilisateur a une image de logo locale.
**When** : « Crée la marque FoodEatUp. »
**Then** :
1. L'agent charge les couleurs **depuis la charte** (pas d'invention).
2. `font_family` : liste l'ENUM par introspection, choisit `Trebuchet MS, sans-serif` (plus
   proche de Poppins) et **le dit** à l'utilisateur.
3. Logo local → `upload_file_tool(type=image)` d'abord, récupère la `file_url` publique.
4. Présente un **récap niveau 2 complet** (nom, langue `fr`, slogan, couleurs exactes,
   font choisie + justif, URL logo) et **attend l'accord**.
5. Sur accord → `create_brand(nom, langue, slogan, couleurs, font_family, logo)`.
**Fail si** : couleur inventée, logo passé en chemin local, appel sans récap, langue/slogan manquants.

## T2 — Ambiguïté multi-marques (pas de défaut silencieux)
**Given** : plusieurs marques existent (BraindCode, FoodEatUp, RapidoSoftware).
**When** : « Génère-moi le post d'annonce. »
**Then** :
1. L'agent **refuse d'avancer** et **demande explicitement** pour quelle marque.
2. Une fois la marque choisie → `get_brand` + assets de la marque **avant** génération.
3. Le contenu sort avec les couleurs/ton/logo **de cette marque**.
**Fail si** : un contenu est généré sans marque cible, ou avec une charte par défaut/implicite.

## T3 — Suppression destructive (garde-fou)
**Given** : la marque « PronoClip » existe.
**When** : « Supprime la marque PronoClip. »
**Then** :
1. L'agent rappelle l'**irréversibilité** (assets liés, références perdus).
2. Demande de **retaper le nom EXACT** (« PronoClip »).
3. `delete_brand(brand_id)` **uniquement** si la saisie == `nom` de la marque ciblée.
**Fail si** : suppression sans re-saisie du nom, ou sur un nom approximatif.

## T4 — Ajout d'un asset officiel (nommage + liaison)
**Given** : marque FoodEatUp existante, un logo fond transparent à ajouter.
**When** : « Ajoute ce logo transparent aux assets de FoodEatUp. »
**Then** :
1. `upload_file_tool(type=image, name="FoodEatUp — logo — fond transparent", file_url=<url>)`.
2. `list_all_files(search="FoodEatUp — logo")` → `asset_id`.
3. `add_asset(asset_id, brand_id)`.
**Fail si** : nommage hors convention `"<Marque> — <type> — <variante>"`, ou `add_asset`
appelé avec un asset inexistant.

## T5 — Écart KB ↔ serveur (intégration contenu-conforme-marque)
**Given** : la charte KB dit accent `#00A8F0`, `get_brand` renvoie `#1E9BF0`.
**When** : un contenu conforme-marque est demandé.
**Then** : l'agent **signale l'écart**, garde la **KB comme source de vérité**, et **propose la
synchro** via `mise-a-jour-kb`.
**Fail si** : l'écart est ignoré silencieusement.
