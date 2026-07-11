# Analyse du MCP RapidoCMS — outils réels par famille

**Serveur** : `https://cms.rapidosoftware.com/mcp` · **company_id 321** (KEBAIL-ALI, admin).
**Compatible IA** : Claude · Mistral · OpenAI (connecteur MCP neutre).
Liste vérifiée en session (outils réellement exposés et testés). Regroupée pour le script.

## 1) Comptes & profil
- `list_connected_accounts` — pages/ comptes connectés par réseau (facebook, instagram, linkedin, linkedin_profile, tiktok)
- `get_profile` · `get_company` · `get_brand`
> **Règle clé (chap. 2)** : Instagram se connecte **à travers Facebook** (compte pro relié à la Page côté Meta Business) — visible dans `config-facebook` / `config-linkedin` / `config-tiktok`.

## 2) Génération IA (visuels)
- `generate_image` (prompt + taille `hd`/`standard`) → image hébergée en bibliothèque S3.

## 3) Bibliothèque de médias
- `upload_file_tool` (URL publique → S3, type image/video/doc) · `list_all_files`
- `add_asset` · `remove_asset`

## 4) Publication — brouillons & planification
- `create_draft_tool` · `edit_draft_tool` · `delete_draft_tool` · `list_drafts_tool`
- `schedule_draft_tool` (post_date **Y-m-d**, post_heure **H:i:s**) · `cancel_schedules_post` · `list_scheduled_posts`
> Formats à citer à l'écran (chap. 5) : **date = année-mois-jour**, **heure = heure-minute-seconde**.

## 5) Campagnes & analyse
- `create_campagne` · `edit_campagne` · `delete_campagne`
- `add_post_campagne` (exige un **post planifié**, pas un brouillon) · `remove_post_campagne` · `list_posts_campagne` · `list_campagnes`
- `ingishts_campagne` · `post_insights` — statistiques (j'aime, engagement, portée)

## 6) Éditeur, templates & marque
- `create_post_template` · `list_card_templates` · `assign_card_template`
- `create_brand` · `edit_brand` · `delete_brand` (chartes/marques)
- `add_prompt` · `edit_prompt` · `delete_prompt` · `list_prompts` (bibliothèque de prompts)

## 7) Cartes digitales (NFC / QR)
- `add_digital_card` · `edit_digital_card` · `delete_digital_card` · `list_digital_card`
- `add_card_page_link` · `edit_card_page` · `delete_card_page_link` · `list_card_page`

---
**Familles pour les lower-thirds (crédibilité technique)** :
Comptes → `list_connected_accounts` · IA → `generate_image` · Bibliothèque → `upload_file_tool` ·
Publication → `create_draft_tool · schedule_draft_tool` · Campagnes → `create_campagne · add_post_campagne · ingishts_campagne` ·
Éditeur/Marque → `create_post_template · create_brand · list_prompts` · Cartes → `add_digital_card`.
