# Bonus — Découpage en 7 shorts verticaux (1080×1920) · TikTok / Instagram

Plan **seulement** (pas de rendu). Chaque short = 1 phase, réutilise la VO, les captures
et les visuels RapidoCMS déjà produits, en format vertical (comme la version 9:16 déjà livrée
dans `videos/foodeatup-tuto-5min/`). Objectif : 20–35 s, hook + 1 bénéfice + CTA.

| # | Titre short | Phase | Durée~ | Hook (à l'écran) | Contenu | Assets | CTA |
|---|-------------|-------|--------|------------------|---------|--------|-----|
| 1 | « Ton resto en ligne en 5 min » | 1 | 25 s | « La seule étape 100 % web » | Compte + création boutique | modifier-profil, ajout-boutique, p1, Mika | foodeatup.com |
| 2 | « TVA + carte, les fondations » | 2 | 22 s | « 2 réglages avant l'IA » | TVA + catégories | ajouter-tva, ajouter-categorie, p2 | — |
| 3 | « Branche ton IA à ton resto » | 3 | 30 s | « Claude, Mistral ou OpenAI » | MCP StockVisionAI + prompt contexte | p3, logos, `https://foodeatup.com/api/mcp` | Guide MCP |
| 4 | « Ta carte créée par l'IA » | 4 | 35 s | « Fini la saisie plat par plat » | Import carte → produits, coût matière | ajout-produit, configuration-recette, p4 | — |
| 5 | « Gère ton équipe + QR pointage » | 5 | 28 s | « Un QR par employé » | Employés/rôles, plannings, congés | ajout-employe, qr-code-pointage, pointage, p5 | — |
| 6 | « HACCP sans stress » | 6 | 30 s | « Conformité exportable en PDF » | Températures, DLC, checklists | ajouter-equipement, checklist-hygiene, p6 | — |
| 7 | « PrediBot anticipe tes ventes » | 7 | 28 s | « Moins de gaspillage » | Stocks, factures, PrediBot | mes-productions, ajouter-client, p7 | Réserver une démo |

**Format** : reprendre le compositeur vertical `videos/foodeatup-tuto-5min/build_fe.py`
(carte + médaillon Mika + sous-titres, zones TikTok-safe) en filtrant sur la phase voulue.
Recos : hook burné 0–2 s, sous-titres karaoké, 1 seule idée par short, CTA final.
