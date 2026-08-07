# Les 8 boucles FoodEatUp — série Academy

Série de 9 vidéos (1 "principe" + 8 boucles) pour l'Academy FoodEatUp
(`foodeatup-guide-star`, module transversal `les-8-boucles`).

## Décisions actées avec Michael (2026-08-07)

- **Pipeline** : MCP `HyperFrames_by_HeyGen` (`compose` + `render_video`, paiant) +
  MCP `ElevenLabs` (`text_to_speech`, payant) — PAS le pipeline local
  ffmpeg/PIL de `videos/FOODEATUP-TUTORIELS-WORKFLOW.md` (qui régit une série
  différente : tutoriels screen-recording produit). Pas non plus le pipeline
  local `npx hyperframes` de `studio-video/` (Reels verticaux) : décision
  explicite de Michael de suivre P0 tel quel malgré l'auto-désactivation
  documentée du MCP pour les clients CLI — à vérifier au premier appel.
- **Palette** : crème `#FCF9E6` / marine `#0F1A23` / bleu `#007BFF`
  (+ bleu marketing `#147AFF` pour le schéma des boucles) / orange CTA
  `#FFA500` — voir `boucles.json`.
- **Ordre de production** : Boucle 02 (Équipe) en premier (pilote), avant
  la vidéo 0 et la Boucle 01.
- **Vignettes** : logo FoodEatUp (pas une frame extraite), voir
  `studio-video/assets/brand/logo-v2/`.
- **Intégration Academy** : édition directe de `src/data/tutorials.ts` dans
  `foodeatup-guide-star` (accès dépôt direct) — pas de prompts à coller
  dans Lovable (L1-L4 de la doc d'origine remplacés par des commits directs).

## Assets de marque réutilisables

Tout dans `studio-video/assets/brand/` (dépôt Video) :
- `logo-v2/` — logo horizontal, logo sur carte bleue, mark "8"/infini.
- `mascots/` — agents 3D : `agent-rh.png` (Boucle 02), `agent-stockvision.png`
  (Boucle 03), `chef-haccp.png` (Boucle 04), `agent-laptop-femme.png`
  (achats), `agent-laptop-homme.png` (copilote), `chef-recette.png`
  (production).
- `product-screenshots/` — captures produit réelles fournies par Michael,
  dont `rh-dashboard-conges-pointage.png` et `stockvision-gestion-stocks.png`
  (ajoutées le 2026-08-07).
- `third-party-logos/` — logos IA tiers (Claude, OpenAI, Mistral) pour les
  mentions factuelles des modèles utilisés.
- `profile/michael-chef-mascot.jpg` — photo réelle de Michael en mascotte
  chef FoodEatUp.

## Statut

Voir `boucles.json` (`videos[].status` : `a_produire` → `script` → `vo` →
`compo` → `rendu` → `publie`).
