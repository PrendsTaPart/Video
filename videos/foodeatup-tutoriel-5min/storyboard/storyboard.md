# Storyboard — « FoodEatUp, le tutoriel complet en 5 min » (16:9, 1920×1080)

Charte FoodEatUp (bleu `#0B6EFD`, orange `#F7941E`, fond clair). Logo permanent.
- **Bumper avatar** (ouverture de chapitre) : Mika (buste, clip HeyGen) à gauche + illustration RapidoCMS + titre de phase à droite.
- **Cartes étapes** : capture d'écran plein cadre à droite dans un cadre navigateur, **zoom lent type Ken Burns**, panneau texte à gauche (n° d'étape, titre, sous-titre) + lower-third + VO.
- Sous-titres incrustés, musique de fond discrète, `loudnorm I=-14`.

| # | Timecode~ | Plan | Visuel (asset) | Caméra | Texte écran | VO |
|---|-----------|------|----------------|--------|-------------|----|
| 0 | 0:00 | Intro | `assets-generes/intro.jpg` + Mika | zoom avant lent | « FoodEatUp — le tutoriel en 5 min » | s00 |
| 1a | 0:16 | Bumper P1 | Mika + `p1.jpg` | — | Phase 1 · Compte & boutique | s10 |
| 1b | 0:22 | Étape 1 | `modifier-profil.png` (+`connexion.png`) | Ken Burns | Étape 1 · Créer votre compte | s11 |
| 1c | 0:35 | Étape 2 | `ajout-boutique.png` | Ken Burns | Étape 2 · Créer votre boutique | s12 |
| 2a | 0:51 | Bumper P2 | Mika + `p2.jpg` | — | Phase 2 · Fondations | s20 |
| 2b | 0:56 | Étape 3 | `ajouter-tva.png` | Ken Burns | Étape 3 · Configurer la TVA | s21 |
| 2c | 1:06 | Étape 4 | `ajouter-categorie.png` | Ken Burns | Étape 4 · Créer vos catégories | s22 |
| 3a | 1:17 | Bumper P3 | Mika + `p3.jpg` | — | Phase 3 · Connecter votre IA | s30 |
| 3b | 1:22 | Étape 5 | `qr-code-pointage.png` + **logos Claude/Mistral/ChatGPT/WhatsApp** + **`https://foodeatup.com/api/mcp`** | Ken Burns | Étape 5 · Connexion MCP StockVisionAI | s31 |
| 4a | 1:40 | Bumper P4 | Mika + `p4.jpg` | — | Phase 4 · Contenu par l'IA | s40 |
| 4b | 1:45 | Étape 6 | `ajout-produit.png` | Ken Burns | Étape 6 · Importer votre carte | s41 |
| 4c | 1:57 | Étape 7 | `ajouter-ingredient.png` | Ken Burns | Étape 7 · Créer vos ingrédients | s42 |
| 4d | 2:07 | Étape 8 | `configuration-recette.png` | Ken Burns | Étape 8 · Recettes & coût matière | s43 |
| 4e | 2:17 | Étape 9 | `ajouter-plat.png` | Ken Burns | Étape 9 · Composer « Ma carte » | s44 |
| 4f | 2:24 | Étape 10 | `ajout-fournisseur.png` | Ken Burns | Étape 10 · Fournisseurs | s45 |
| 5a | 2:32 | Bumper P5 | Mika + `p5.jpg` | — | Phase 5 · Équipe (RH) | s50 |
| 5b | 2:37 | Étape 11 | `ajout-employe.png` + `creation-role.png` | Ken Burns | Étape 11 · Employés, rôles & QR | s51 |
| 5c | 2:47 | Étape 12 | `pointage.png` + `demande-absence.png` | Ken Burns | Étape 12 · Plannings & congés | s52 |
| 6a | 2:57 | Bumper P6 | Mika + `p6.jpg` | — | Phase 6 · HACCP | s60 |
| 6b | 3:02 | Étape 13 | `ajouter-equipement.png` | Ken Burns | Étape 13 · Équipements & températures | s61 |
| 6c | 3:12 | Étape 14 | `assets-generes/p6.jpg` (card DLC) | zoom lent | Étape 14 · Étiquettes DLC & traçabilité | s62 |
| 6d | 3:20 | Étape 15 | `zone-nettoyage.png` + `checklist-hygiene.png` | Ken Burns | Étape 15 · Nettoyage & checklists | s63 |
| 7a | 3:29 | Bumper P7 | Mika + `p7.jpg` | — | Phase 7 · Exploitation | s70 |
| 7b | 3:34 | Étape 16 | `mes-productions.png` | Ken Burns | Étape 16 · Stocks & production | s71 |
| 7c | 3:44 | Étape 17 | `ajouter-client.png` | Ken Burns | Étape 17 · Clients, devis & factures | s72 |
| 7d | 3:53 | Étape 18 | `assets-generes/p7.jpg` (card PrediBot) | zoom lent | Étape 18 · PrediBot & bilan | s73 |
| 8 | 4:05 | Outro CTA | `assets-generes/cta.jpg` + Mika | zoom arrière lent | « Réservez une démo · BraindCode Academy » | s99 |

**Total ≈ 4:20–4:40** (≤ 5:00). Transitions : fondu court entre plans ; le bumper « pousse » vers la carte étape.

## Mapping des captures (imposé → fichier)
`assets/screens/foodeatup/` : ajout-boutique · modifier-profil · connexion · ajouter-tva · ajouter-categorie ·
ajout-produit · ajouter-plat · configuration-recette · ajouter-ingredient · ajout-fournisseur · ajout-employe ·
creation-role · qr-code-pointage · pointage · demande-absence · ajouter-equipement · zone-nettoyage ·
checklist-hygiene · mes-productions · ajouter-client.
- **Substitutions** (pas de capture fidèle fournie) : *étiqueteuse/DLC* → card RapidoCMS `p6.jpg` ; *créer-devis* → card `p7.jpg` / `ajouter-client`. Noté au manifest.
- **Chapitre 3 (MCP)** : logos `claude.png`, `mistral.jpg`, ChatGPT & WhatsApp (texte), `foodeatup-mark.png` + `https://foodeatup.com/api/mcp`.
