# Tutoriel — Commander : Site, Agent vocal & QR code à table

Module `site-web-vitrine` (Site Web & Vitrine), site Lovable FoodEatUp Academy.
Rush fourni : `Commander_sur_votre_votre_site_Agent_vocal_ou_qrcode_a_table.mp4`
(66,36 s, 1920x828, 25 fps) — démo GoSushi, parcours de commande sur le site
vitrine uniquement (le rush ne filme pas l'agent vocal ni le QR code, qui ne
sont pas des écrans capturables ; ils sont introduits en VO + carte dédiée,
réutilisant la carte d'intro fournie qui les montre déjà tous les trois).

**v1 — brouillon, en attente de validation avant génération audio (STOP
obligatoire, voir `FOODEATUP-TUTORIELS-WORKFLOW.md`).**

## Déroulé du rush (analyse frame par frame)

| t (rush) | Écran |
|---:|---|
| 0-5 s | Page d'accueil du site vitrine (« GoSushi Démo »), scroll vers le menu |
| 5 s | Clic **AJOUTER** sur « Pizza » (15,00 €) |
| 5-16 s | Ajout d'autres plats (Dragon Roll 6 pcs, California Roll 8 pcs), badge panier qui grimpe, panier latéral qui récapitule (2×Pizza, 1×Dragon Roll, 1×California Roll = 89,90 €) |
| 16,6 s | Clic **Commander** (bas du panier) → passage à « Finaliser ma commande » |
| 17-19 s | Étape 1 « Comment récupérez-vous votre commande ? » → À emporter ; Étape 2 « Quand passez-vous ? » → Au plus vite (~30 min) |
| 19-40 s | Étape 3 « Vos coordonnées » : nom, email, téléphone, note cuisine |
| ~41 s | Clic **Passer au paiement** → chargement Stripe |
| 42-66 s | Page de paiement Stripe (moyen enregistré Visa/Link, puis formulaire carte manuel) — s'arrête avant la confirmation (aucun paiement réel déclenché dans le rush) |

## Voix off (v1, 10 lignes — voix Adam FR `TGAegA0zNRi8I6nUdq3i`)

| # | Texte | Ancrage |
|---|---|---|
| N0 | Trois façons de commander chez vous avec FoodEatUp : le site, l'agent vocal, ou le QR code à table. | carte d'intro |
| N1 | Sur le site, le client choisit ses plats et les ajoute au panier en un clic. | seg A + clic AJOUTER |
| N2 | Il compose sa commande, elle apparaît aussitôt dans son panier. | ajout des autres plats + clic Commander |
| N3 | Il choisit comment récupérer sa commande, et à quelle heure. | étapes 1-2 (à emporter / au plus vite) |
| N4 | Renseigne ses coordonnées pour être tenu informé du suivi. | étape 3 (coordonnées) |
| N5 | Et paie en toute sécurité, par carte, Apple Pay ou Google Pay. | clic Passer au paiement + page Stripe |
| N6 | Le même parcours existe par téléphone avec l'agent vocal, ou à table en scannant simplement le QR code. | carte transition (réutilise l'intro) |
| N7 | Vous pouvez aussi le faire depuis Claude : copiez ce prompt, remplacez les crochets. | étage 1+2 (reveal + copié) — **réutilisée telle quelle depuis `foodeatup-tva-tuto/vo/N6.mp3`**, texte identique |
| N8 | Collez-le dans la conversation : vous suivez vos commandes en quelques secondes. | étage 3 (mockup chatbot) |
| N9 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | carte de fin (CTA) — **réutilisée telle quelle depuis `foodeatup-tva-tuto/vo/N8.mp3`** |

N7 et N9 sont copiées telles quelles (texte identique, règle du workflow) —
économise 2 allers-retours ElevenLabs. Les 8 autres lignes (N0-N6, N8) sont à
générer.

## Découpage prévu (targets à ajuster après mesure des VO)

| Seg | Source (rush) | Cible | Contenu |
|---|---|---:|---|
| intro | carte fournie | 4,40 s | SITE, VOCAL & QR CODE |
| A | 0,50 → 4,90 | 3,00 s | Accueil + scroll menu |
| B | 4,90 → 5,15 | 0,90 s | **zoom-punch** AJOUTER Pizza (740, 486) |
| C | 5,30 → 16,60 | 4,50 s | Ajout des autres plats, panier qui se remplit |
| D | 16,60 → 16,85 | 0,90 s | **zoom-punch** Commander (1567, 762) |
| E | 17,00 → 20,00 | 3,00 s | Étapes 1-2 (à emporter / au plus vite) |
| F | 20,00 → 24,50 | 3,00 s | Étape 3, coordonnées |
| G | 40,80 → 41,05 | 0,90 s | **zoom-punch** Passer au paiement (632, 724) |
| H | 41,30 → 50,00 | 4,00 s | Page de paiement Stripe |
| transition | carte (= intro.jpg réutilisée) | 4,00 s | Vocal + QR code |
| claude1 | carte générée | 3,00 s | reveal — prompt |
| claude2 | carte générée | 2,30 s | « Copié dans le presse-papiers ! » |
| claude3 | carte générée | 5,30 s | mockup chatbot Claude |
| outro | carte fournie | 6,20 s (extensible) | CTA |

Coordonnées mesurées par grille de pixels sur les frames du rush
(`work/grid/*.png`), pas à l'œil.

## Séquence Claude — `mcp__Foodeatup__list_orders`

`list_orders(establishment_id, channel)` accepte exactement
`manuel|telephone|vitrine|agent_vocal|sur_place|facture|devis` — un
correspondance directe avec les 3 canaux du tutoriel (`vitrine` = site,
`agent_vocal` = agent vocal, `sur_place` = QR code à table).

**Prompt affiché dans la vidéo** (un seul, avec le canal en placeholder) :

> Montre-moi les commandes reçues aujourd'hui par [canal : vitrine /
> agent_vocal / sur_place] pour mon établissement FoodEatUp (ID [ID
> établissement]).

**Sur la fiche Lovable (`claudePrompts[]`, 3 exemples concrets)** :

1. « Commandes reçues via le site » — canal `vitrine`
2. « Commandes reçues via l'agent vocal » — canal `agent_vocal`
3. « Commandes reçues via le QR code à table » — canal `sur_place`

## Contenu prévu pour la fiche Lovable

- **howItWorks** : parcourir le menu et ajouter au panier · ajuster les
  quantités · choisir la récupération (à emporter/livraison/sur place) et
  l'horaire · renseigner ses coordonnées · payer en ligne en sécurité · le
  même parcours existe par téléphone (agent vocal) et à table (QR code).
- **whatItsFor** : trois canaux de commande pour ne rater aucune vente, avec
  un seul flux centralisé côté cuisine.
- **chefTip** : conseil sur la complémentarité des 3 canaux (site = hors
  horaires d'appel, agent vocal = absorbe le rush téléphone sans mise en
  attente, QR code = fluidifie la salle sans mobiliser un serveur).

## Statut

**v1 livrée.** Script validé par Michael (2026-08-06, demande explicite de
réaliser le tutoriel complet et de le publier une fois terminé — le STOP de
livraison est donc levé pour cette vidéo, comme documenté pour plusieurs
tutoriels précédents publiés sur instruction explicite).

Durée livrée : **44,96 s** — H.264 High/yuv420p 1920x828 25fps, AAC 48 kHz
stéréo, faststart. Audio : true peak **-7,2 dBFS** (mesuré sur le MP4 final,
identique à `foodeatup-tva-tuto`).

Offsets VO mesurés (`offsets:` de `build.py`, zéro dérive — chaque ligne
tombe sur son ancrage) :

| # | Offset | Durée |
|---|---:|---:|
| N0 | 0,30 s | 5,80 s |
| N1 | 6,32 s | 4,31 s |
| N2 | 10,85 s | 3,06 s |
| N3 | 14,13 s | 2,93 s |
| N4 | 17,27 s | 3,11 s |
| N5 | 20,60 s | 3,29 s |
| N6 | 24,11 s | 5,88 s |
| N7 | 30,21 s | 4,41 s |
| N8 | 34,84 s | 4,08 s |
| N9 | 39,14 s | 5,02 s |

Outro auto-étendue de 6,20 s → 7,35 s pour absorber la fin de N9 (mécanisme
standard du pipeline, voir `FOODEATUP-TUTORIELS-WORKFLOW.md`).

Livrables : `out/foodeatup-commander-via-site-vocal-qrcode-tuto-v1.mp4` +
`out/thumbnail-youtube.jpg` (recadrage neutre de `assets/intro.jpg`, sans
redesign, conformément à la règle du workflow).
