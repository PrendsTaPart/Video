# 📖 BIBLE créative — Studio Vidéos de Vente (FoodEatUp · Écosystème Rapido)

Version 1 · Directeur créatif social media. **Studio réutilisable**, pas des one-shots.

## 1. Promesse centrale
> **« Vous pilotez, l'IA exécute. »** — jamais « l'IA gère seule ».
L'honnêteté = conversion. On montre un humain qui **commande**, et une IA qui **agit dans le back-office**.

## 2. Différenciateur (vs Komia, Zenchef, AirAgent, Repply…)
- **Agentique** : l'IA **AGIT** dans le logiciel (crée, planifie, facture), pas seulement répond.
- **De bout en bout** : **4 MCP** (FoodEatUp/StockVisionAI · RapidoCMS · RapidoRH · RapidoCRM) = un seul écosystème.
- **Piloté en parlant** : langage naturel via Claude / Mistral / OpenAI (connecteur MCP neutre).
- **Prix PME** : pensé pour les indépendants et TPE/PME, pas l'entreprise.

## 3. Les 6 piliers de contenu
| # | Pilier | Intention | Canal fort |
|---|--------|-----------|-----------|
| P1 | **Problème → Solution** | douleur concrète → l'outil résout | TikTok/Reels/FB |
| P2 | **Démo 1 phrase** | un prompt → un résultat à l'écran | TikTok/Reels |
| P3 | **Fondateur** | Mo parle caméra, vision & preuve | **LinkedIn** |
| P4 | **Preuve** | chiffre, cas client, avant/après | LinkedIn/FB |
| P5 | **Pédagogie / Mythe** | « non, l'IA ne remplace pas… » | LinkedIn/Reels |
| P6 | **Coulisses** | making-of, roadmap, équipe | TikTok/LinkedIn |

## 4. Signature visuelle
- **Mika** en hook (médaillon vidéo, présentateur).
- **Écrans produit zoomés** (Ken Burns lent) dans une carte navigateur.
- **Scène « chat Claude »** pour les démos de prompt : fond sombre, logo Claude, prompt en **machine à écrire**, coche **« ✓ Exécuté par votre IA »**, puis cut sur le résultat produit.
- **Lower-third produit** (nom fonctionnalité + outil MCP réel).
- **CTA final** : « **Réservez votre démo · lien en bio** ».

## 5. Formats
- **9:16 vertical** — TikTok / Reels / Facebook : 1080×1920, **15-30 s**. Zones safe : rien dans les 250 px haut/bas.
- **16:9 ou 1:1** — LinkedIn : **30-45 s**, caption **founder-led** (Mo à la 1re personne).

## 6. Règle du hook (0-3 s)
Toujours **une douleur concrète du restaurateur/dirigeant** — **jamais le nom du produit d'abord**.
Ex : « Vous saisissez encore vos plats un par un ? » · « L'HACCP vous vole 1h par jour ? » · « Vos posts, personne pour les faire ? »

## 7. Chartes couleur (par produit)
| Produit | Accent | Hex |
|---------|--------|-----|
| FoodEatUp | bleu + orange | `#0B6EFD` / `#F7941E` |
| RapidoCMS | bleu ciel | `#29ABE2` |
| RapidoRH | violet | `#7B61C4` |
| RapidoCRM | vert | `#48A850` |
| Écosystème Rapido | tri-color | vert+bleu+violet |

## 8. Chef de marque
**Mo** — 20 ans de cuisine, lauréat FrenchTech. Le **founder-led** est prioritaire sur LinkedIn (P3/P4).

## 9. Voix & rendu (technique)
- VO : ElevenLabs **Adam** `TGAegA0zNRi8I6nUdq3i`, `eleven_multilingual_v2`, FR oral.
- Rendu **local (gratuit)** via ffmpeg (HeyGen HyperFrames `render_video` désactivé en CLI). BGM −18 dB, `loudnorm I=-14`.
- Pipeline : `videos/vente-social/templates/studio.py` (3 templates paramétrables) + assembleur type `assemble_story.py`.

## 10. CTA & tracking
CTA unique : « **Réservez votre démo** ». Lien en bio (Instagram/TikTok), lien direct (LinkedIn/FB).
Toutes les vidéos rattachées à la campagne RapidoCMS **« Vente Social 2026 »** (post planifié, pas brouillon).
