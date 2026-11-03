# Livraison — « RapidoRH & son MCP » (TikTok vertical)

## Fichier final
- `deliverable/rapidorh-mcp-tiktok.mp4` — **1080×1920**, **1:56**, H.264 + AAC, ~8 Mo. Rendu local (gratuit).

## Contenu
Ouverture **logo RapidoRH** + VO : « Bienvenue sur RapidoSoftware, sur l'application RapidoRH… ».
Mika en médaillon vidéo aux chapitres. Charte RapidoRH violet #7B61C4.
Chapitres : Intro → Compte → Organisation (rôles/permissions) → ⭐ MCP (`rh.rapidosoftware.com/mcp/rapidorh` + Claude/Mistral/OpenAI + **avertissement : l'IA agit avec vos droits admin**) → Équipe → Projets/Kanban → Quotidien (admin vs collaborateur) → Outro.
**4 Astuces du Chef** en scènes chat Claude (prompt + « ✓ Exécuté par votre IA » + résultat RapidoRH).

## Fichiers
- `script/analyse-mcp.md` (5 familles d'outils MCP réels) · `build_rrh.py` · `assemble_rrh.py`
- `assets/rapidorh/` (32 assets) · `audio/` (12 VO Adam FR + bgm)

## Reproduire
```bash
python3 build_rrh.py && python3 assemble_rrh.py
```

## Bonus — 4 shorts (plan) : MCP+sécurité · équipe en 1 prompt · projet+Kanban auto · état des lieux quotidien.
