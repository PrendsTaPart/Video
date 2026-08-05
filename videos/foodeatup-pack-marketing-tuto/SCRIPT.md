# Tutoriel — Activer le Pack Marketing FoodEatUp (module Marketing, Fidélité & Iris)

Troisième vidéo publiée du module `marketing-fidelite`, section "Pack marketing &
campagnes" (placeholder existant `activer-le-pack-marketing`, order 4). Intrants fournis
par Michael : `ACTIVER_LE_PACK_MARKETING.jpg` (intro), `Acheter l'abonnement marketing.mp4`
(rush, 1920x828, 25fps, 15,88 s — le plus court de la série, piste audio native silencieuse
à -91 dB, VO entièrement ElevenLabs), `page_fin_vid..jpg` (outro CTA générique, réutilisée
telle quelle).

## Déroulé observé dans le rush

| t≈ | Écran |
|---|---|
| 0-4,6s | Page abonnement **« Boostez votre gestion avec stockvision »** : plan actuel StockVision (Actif), toggle Mensuel/Annuel, 3 cartes de packs (Plan actuel / Passer à ce pack / Passer à ce pack — badge « Plus populaire ») |
| 4,6-5,2s | Scroll rapide + clic sur **« Ajouter cette option »** de la carte **Marketing & Commercial** (section « Options & modules ») — action trop rapide dans le rush pour l'isoler proprement en vidéo (moins de 0,6 s), pas de zoom-punch dessus |
| 5,2-15,88s | Carte **Marketing & Commercial** (99€/mois) affichée **« Activé ✓ »**, avec le détail des fonctionnalités incluses : Campagnes marketing, Agent IA marketing, Campagnes vocales, Minutes vocales marketing, Jeux concours & sondages — module unifié campagnes email/SMS/WhatsApp/vocal ciblées RFM, agent IA, 1 500 crédits et 30 min audio/mois inclus (mise en service 199€, offerte en annuel) |

## Voix off (6 lignes, voix Adam FR `TGAegA0zNRi8I6nUdq3i`)

| # | Texte | Segment |
|---|---|---|
| N0 | Envie de lancer des campagnes marketing avec FoodEatUp ? Activez le Pack Marketing en un clic. | intro + A |
| N1 | Depuis votre abonnement, retrouvez votre plan actuel et les packs disponibles. | A |
| N2 | Dans Options et modules, le pack Marketing et Commercial réunit campagnes email, SMS, WhatsApp et vocal, agent IA, jeux concours et sondages. | B |
| N3 | Cliquez sur Ajouter cette option : le pack est activé instantanément. | B |
| N4 | Mille cinq cents crédits et trente minutes audio par mois sont inclus dès l'activation. | B |
| N5 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | carte de fin (CTA) — réutilisée depuis `foodeatup-nettoyage-ia-tuto/vo/N5.mp3` |

**Aucune séquence Claude sur ce tuto.** L'action montrée (acheter/activer un pack ou module
d'abonnement) passe par Stripe et n'a pas d'outil `mcp__Foodeatup__*` équivalent (recherché
explicitement — aucun outil d'abonnement/pack/module trouvé dans le catalogue MCP FoodEatUp).
Conformément à la règle du pipeline, ni la vidéo ni la fiche Lovable n'ont de `claudePrompt`
— même traitement que la fiche placeholder `choisir-son-abonnement` (paiement Stripe).

## Montage

Rush le plus court de la série (15,88 s) : segment A (page abonnement, 0-4,6s) et segment B
(carte Marketing & Commercial activée, 5,2-15,88s), tous deux fortement ralentis via `setpts`
pour porter la voix off (contenu source statique, aucun mouvement de curseur pendant les
segments tenus — le ralenti est invisible). Le scroll + clic réel (4,6-5,2s dans le rush,
moins de 0,6s) n'est pas montré comme segment séparé : trop rapide pour l'isoler proprement,
une coupure franche (transition `slideleft`) entre la page d'abonnement et la vue confirmée
« Activé » se lit mieux qu'une frame floue de mi-scroll. Bandeaux d'étape en deux `drawtext`
(plate = `box=1`), xfade 0,28s, cartes intro/outro en fond flou + overlay net. Pas de clip
avatar, pas de zoom-punch (pas de clic isolable proprement dans le rush).

## Fiche Lovable

- **slug** : `activer-le-pack-marketing` — placeholder déjà existant dans le scaffold du
  module (order 4, section "Pack marketing & campagnes"), rempli avec le contenu complet.
- **title** : Activer le Pack Marketing FoodEatUp
- **moduleSlug** : `marketing-fidelite`
- **subcategory** : 04 · Pack marketing & campagnes
- **whatItsFor** : Activer le Pack Marketing & Commercial FoodEatUp pour débloquer les
  campagnes email/SMS/WhatsApp/vocal ciblées, l'agent IA marketing, les jeux concours et
  sondages — 1 500 crédits et 30 minutes audio par mois inclus, activation immédiate depuis
  votre abonnement.
- **howItWorks** :
  1. Ouvrez votre abonnement FoodEatUp.
  2. Faites défiler jusqu'à Options & modules.
  3. Repérez la carte Marketing & Commercial (99€/mois).
  4. Cliquez sur Ajouter cette option : le pack est activé instantanément.
- **chefTip** : Le Pack Marketing s'empile sur votre abonnement actuel — il ne le remplace
  pas. Vous gardez votre pack principal (StockVision, etc.) et ajoutez simplement les
  fonctionnalités marketing par-dessus, sans changer de formule.
- **chefTipAvatar** : `michael-chef-mascot.jpg`
- **claudePrompt** : absent (pas d'outil MCP équivalent — paiement Stripe, voir plus haut)

## Statut

Vidéo montée, VO générée et publiée à la demande de Michael (workflow complet demandé dans
le même message : montage, VO ElevenLabs, publication Lovable FoodEatUp Academy, mise à
jour du dépôt, ajout du thumbnail). Publication limitée à Lovable + dépôt GitHub, comme
demandé — pas d'upload RapidoCMS ni de programmation LinkedIn dans cette tâche. Placeholder
existant rempli directement, pas de doublon créé.
