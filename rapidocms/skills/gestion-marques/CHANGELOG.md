# CHANGELOG — gestion-marques

## 1.0.0 — 2026-07-10
### Ajouté
- Skill `gestion-marques` (cluster `rapidocms`) : création/édition/suppression de marque et
  gestion de la bibliothèque d'assets officiels par marque.
- Agent `gestionnaire-marques` : gardien de la cohérence multi-enseignes.
- Contrat live câblé sur les tools `create_brand` / `edit_brand` / `delete_brand` /
  `add_asset` / `remove_asset` (introspection du schéma) :
  - `create_brand` requis : `nom`, `langue`, `slogan` ; optionnels `couleurs` (hex CSV),
    `font_family` (ENUM web-safe), `logo` (URL publique), `site_web`.
  - `add_asset(asset_id, brand_id)` / `remove_asset(asset_id)`.
- Garde-fous : multi-marques sans défaut silencieux, écriture marque = confirmation niveau 2,
  `delete_brand` = nom exact retapé, couleurs depuis `./rapido-kb/charte-graphique.md`
  (jamais inventées), `font_family` mappée depuis l'ENUM introspecté (choix expliqué),
  logo/asset via `upload_file_tool` → URL publique.
- Convention de nommage d'asset : `"<Marque> — <type> — <variante>"`.
- Intégrations documentées (INTEGRATIONS.md) : `contenu-conforme-marque` (étape 0 lit
  `get_brand` + assets, KB = source de vérité), `video-marketing` + `prompts-visuels-pro`
  (logos = assets de marque, fin des « logos GitHub »).
- Tests : création, ambiguïté multi-marques, suppression destructive (tests.md).

### À faire (hors périmètre de ce dépôt)
- Appliquer les patchs d'intégration dans le dépôt plugin (skills concernés).
- Vérifier l'ENUM `font_family` par introspection au premier run (le serveur fait foi).
