# 🎬 Storyboard — V1 Lancement FoodEatUp

**Master** : 9:16, 1080×1920, **45 s** · **Déclinaison** : LinkedIn 16:9, 60 s (intro fondateur rallongée).
**Template** : T1 (Problème→Solution) + bloc Offre · Charte FoodEatUp (bleu #0B6EFD), Mika, safe zones (rien dans 250 px haut/bas).
**Rendu** : pipeline local ffmpeg (gratuit) — HyperFrames MCP indisponible ; scène « chat Claude » + médaillon Mika reproduits via templates T2/T1.

| # | TC | Visuel | Animation | Carton (≤6 mots) | VO |
|---|----|--------|-----------|------------------|-----|
| 1 | 0:00–0:04 | Image IA #1 (cuisine débordée) | Zoom avant lent + léger shake | *(rien)* | « Vous êtes chef. Pas comptable, pas RH, pas informaticien. » |
| 2 | 0:04–0:08 | Mika buste, fond cuisine flou | Cut franc | « Et pourtant… » | « Et pourtant, vous passez vos soirées sur des tableurs. » |
| 3 | 0:08–0:14 | Split-screen : classeur HACCP papier ↔ écran FoodEatUp | Wipe latéral G→D | « Ça, c'était avant. » | « FoodEatUp, c'est votre restaurant piloté en parlant à votre IA. » |
| 4 | 0:14–0:22 | Scène chat Claude (image #4, logo Claude) → cut sur `ajout-produit` | Machine à écrire 6 s → coche verte → cut | « ✓ Exécuté par votre IA » | « Vous parlez. Elle agit. Votre carte importée, vos stocks suivis, votre HACCP conforme — sans saisir une ligne. » |
| 5 | 0:22–0:27 | Carrousel 4 écrans (recettes/stocks/planning/facture) | Enchaînement 1,2 s + Ken Burns | *(lower-thirds modules)* | « Vous pilotez. L'IA exécute. » |
| 6 | 0:27–0:38 | BLOC OFFRE sur image #2 (fond bleu, badge BÊTA) | −50 % en pop + pulsation, compteur places | « −50 % » · « `{PLACES}` places bêta » · « Jusqu'au `{DEADLINE}` » | « On ouvre `{PLACES}` places de bêta-testeurs. Vous obtenez `{DUREE}` à moitié prix. En échange : `{CONTREPARTIE}`. On construit l'outil avec vous. » |
| 7 | 0:38–0:45 | Image IA #3 (chef serein) + Mika | Mika incrusté, CTA monte du bas | « Lien en bio » · « Réservez votre place » | « `{PLACES}` places. Pas une de plus. Le lien est en bio. » |

## Écrans utilisés (captures)
- Plan 3 : `checklist-hygiene` (⚠️ substitut de `haccp-temperatures`, manquant → à générer/capturer).
- Plan 4 : `ajout-produit`.
- Plan 5 : `configuration-recette` (recettes) · `mes-productions` (stocks) · `qr-code-pointage` (planning) · **facture** (⚠️ `creer-devis` manquant → substitut/à générer).

## Visuels IA générés (RapidoCMS, HD, sans texte incrusté)
- `assets-generes/img1-chaos.png` (plan 1) · `img2-offre.png` (plan 6) · `img3-serenite.png` (plan 7) · `img4-chat-bg.png` (plan 4).

## Sound design
0:00–0:08 cuisine saturée → **cut sonore net** + silence 0,3 s → nappe calme → 0:14 frappe clavier + ding → 0:27 montée musicale (offre) → 0:38 résolution apaisée.
