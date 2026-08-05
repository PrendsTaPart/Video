# Tutoriel — Créer une campagne avec l'agent IA FoodEatUp (module Marketing, Fidélité & Iris)

Première vidéo du module `marketing-fidelite` (24 vidéos attendues, 0 publiée jusqu'ici —
voir `PROGRESSION-157-TUTORIELS.md`). Intrants fournis par Michael :
`CAMPAGNE_100_IA.jpg` (intro), `Créer une campagne avec l'agent IA FoodEatUp.mp4` (rush,
1920x828, 25fps, 31,24 s, piste audio native silencieuse à -91 dB — VO entièrement
ElevenLabs), `page_fin_vid..jpg` (outro CTA générique, réutilisée telle quelle).

## Déroulé observé dans le rush

| t≈ | Écran |
|---|---|
| 0-2,2s | Page **Campagnes & automatisations**, onglet "Campagnes" : KPI (CA marketing 30j 43,5€, Messages 30j 3, Contacts joignables 38, Automations actives 3/7) |
| 2,2-4,35s | Clic sur l'onglet **Agent IA** : "Votre directeur marketing ia" — *"Propositions construites sur vos données réelles : chaque idée est justifiée par vos chiffres, la remise est plafonnée à votre marge."* — état **"Aucune proposition"** |
| 4,35s | Clic sur **"Proposer des campagnes"** |
| 4,35-9,3s | "Analyse en cours..." |
| 9,3-13s | **3 propositions chiffrées** apparaissent : *Rentrée Spéciale Jeudi* (Tous, email, "Rentrée 0% réductions"), *Reconquête À Risque Jeudi* (À risque, email, "Retour exclusif 0%"), *Réactivation Perdus Rentrée* — chacune avec le raisonnement chiffré ("La marge moyenne négative empêche les réductions, et jeudi est le jour le plus creux avec seulement 1 commande et 30€ de revenus...") et un bouton **"Utiliser"** |
| 13-19s | Clic **"Utiliser"** → modal **"Nouvelle campagne"** (4 étapes : Cible / Message / Planification / Conformité) : étape 1, segments RFM calculés chaque nuit (Tous les clients 39, Champions 2, Fidèles 5, Prometteurs 7, À risque...), puis Nom de la campagne + Canal (Email/SMS/WhatsApp/Vocal, Email sélectionné) + Message pré-rempli |
| 19-23s | Étape 2 **Message** : variables `{prenom} {plat_prefere} {code} {lien}`, Offre "Rentrée 0% réductions", Code promo, URL de destination du lien tracké |
| 23-25s | Étape 3 **Planification** : "Envoyer maintenant" (si fenêtre légale 8h-20h) ou "Planifier" ; marronniers à venir (Rentrée J-27, Halloween J-87, envoi conseillé 3 jours avant) |
| 25-26,85s | Étape 4 **Conformité** : Segment 39 clients, Contactables 38 après conformité, Coût estimé 0,08€ email, Exclus par les garde-fous (1 — STOP désinscrits), *"Chaque message contient la procédure STOP. Dédup automatique : relancer n'enverra jamais deux fois au même client."* |
| 26,85s | Clic **"Lancer vers 38 client(s)"** |
| 26,85-31,24s | Toast : *"Campagne lancée : l'envoi part en file, conformité vérifiée client par client."* — la liste des campagnes affiche le nouveau statut **"Envoi..."** |

Coordonnées mesurées sur les frames réelles (`ffmpeg -ss t -frames:v 1`, puis fenêtres
5 fps autour de chaque clic pour pointer le timestamp exact), natif 1920x828 :
`BTN_PROPOSE = (1633, 360)` (« Proposer des campagnes »), `BTN_LANCER = (1330, 654)`
(« Lancer vers 38 client(s) »).

## Voix off (11 lignes, voix Adam FR `TGAegA0zNRi8I6nUdq3i`)

| # | Texte | Segment |
|---|---|---|
| N0 | Créer une campagne marketing FoodEatUp ? Laissez votre agent IA s'en occuper. | intro + A |
| N1 | Direction l'onglet Agent IA, votre directeur marketing intelligent. | B |
| N2 | Un clic sur Proposer des campagnes, et l'IA analyse vos segments, vos jours creux et vos marges. | clic C + D + E |
| N3 | Chaque idée est chiffrée : cliquez sur Utiliser pour la transformer en campagne prête à l'envoi. | F |
| N4 | Le message, l'offre et le code promo sont déjà pré-remplis, à vous de les ajuster. | G |
| N5 | Envoyez maintenant ou planifiez, en pensant aux marronniers à venir. | H |
| N6 | La conformité est vérifiée automatiquement : contacts joignables, coût estimé, exclusions STOP. | I |
| N7 | Cliquez sur Lancer : la campagne part en file, conformité vérifiée client par client. | clic J + K |
| N8 | Vous pouvez aussi demander à l'agent IA de proposer vos campagnes depuis Claude : copiez ce prompt, remplacez les crochets. | claude1+2 |
| N9 | Collez-le dans la conversation : des idées de campagnes chiffrées arrivent aussitôt, prêtes à lancer. | claude3 |
| N10 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | carte de fin (CTA) — réutilisée depuis `foodeatup-nettoyage-ia-tuto/vo/N5.mp3` |

## Séquence Claude — module partagé

Outil correspondant à l'action montrée à l'écran (clic « Proposer des campagnes ») :
`mcp__Foodeatup__propose_campaigns(establishment_id)` — *« Agent IA marketing : 2-4
propositions de campagnes chiffrées depuis les données réelles (RFM, jours creux, marges,
marronniers) »* — correspondance exacte avec les 3 propositions vues à l'écran.

> Propose-moi des campagnes marketing pour mon établissement FoodEatUp (ID [ID
> établissement]) : des idées chiffrées à partir de mes segments clients, mes jours creux
> et mes marges.

Le reste du flux (création du brouillon + lancement réel) est couvert par
`mcp__Foodeatup__create_campaign` et `mcp__Foodeatup__launch_campaign` (confirm:true) —
proposé en second exemple dans `claudePrompts[]` côté fiche Lovable (voir
`LOVABLE-FOODEATUP-DOCS.md`), pas dans la vidéo elle-même (un seul prompt à l'écran,
conformément à la règle de la série).

## Animations

Mêmes principes que toute la série : `setpts` pour la vitesse (jamais `zoompan` sur la
vidéo réelle), zoom-punch en crop fixe sur les 2 clics (Proposer des campagnes, Lancer),
bandeaux d'étape en deux `drawtext` (plate = `box=1`, pas de `drawbox` animé — voir le
piège documenté dans `FOODEATUP-TUTORIELS-WORKFLOW.md`), xfade 0,28s partout, cartes
intro/outro en fond flou + overlay net. Pas de clip avatar. Séquence "Utilisez cette
fonctionnalité avec Claude" en 3 temps, module partagé
`videos/_shared/claude_prompt_sequence.py`, étages allongés (4,60 / 2,40 / 5,90 s au lieu
du défaut 2,20/1,30/2,50) car N8 et N9 sont plus longues que la moyenne de la série.

## Fiche Lovable

- **slug** : `creer-une-campagne-par-ia` — fiche placeholder déjà existante dans le scaffold
  du module (order 6, section "Pack marketing & campagnes", titre imposé par
  `CATALOGUE-157-TUTORIELS.md`), remplie avec le contenu complet plutôt que dupliquée.
  Premier envoi Lovable créé par erreur un doublon sous le slug `creer-campagne-agent-ia`
  (sans repérer le placeholder existant) — supprimé dans un second envoi correctif.
- **title** : Créer une campagne par IA — agent FoodEatUp
- **moduleSlug** : `marketing-fidelite` (première vidéo publiée dans ce module — catégorie
  *Marketing, Fidélité & Iris*, 23 fiches placeholder restantes)
- **subcategory** : 06 · Pack marketing & campagnes
- **whatItsFor** : Laisser l'agent IA de FoodEatUp analyser vos segments clients, vos jours
  creux et vos marges pour proposer des campagnes marketing chiffrées, prêtes à l'envoi en
  quelques clics — email, SMS, WhatsApp ou vocal, conformité (STOP, dédoublonnage) vérifiée
  automatiquement avant le lancement.
- **howItWorks** :
  1. Ouvrez Campagnes & automatisations puis l'onglet Agent IA.
  2. Cliquez sur « Proposer des campagnes » : l'IA analyse vos segments RFM, vos jours creux
     et vos marges.
  3. Choisissez une proposition chiffrée et cliquez sur « Utiliser ».
  4. Ajustez la cible, le message, l'offre et le code promo si besoin.
  5. Envoyez maintenant ou planifiez en fonction des marronniers à venir.
  6. Vérifiez le récap de conformité (contactables, coût estimé, exclusions STOP) puis
     cliquez sur « Lancer ».
- **chefTip** : Les segments RFM (Champions, Fidèles, Prometteurs, À risque, Perdus) sont
  recalculés chaque nuit depuis vos commandes réelles — relancez « Proposer des campagnes »
  régulièrement plutôt qu'une seule fois : les idées évoluent avec votre activité, pas
  seulement au moment des marronniers.
- **chefTipAvatar** : `michael-chef-mascot.jpg`
- **claudePrompts** :
  1. *Demander des propositions à l'agent IA* — `propose_campaigns` (prompt ci-dessus).
  2. *Créer une campagne directement* — `create_campaign` :
     > Crée une campagne [canal email|sms|whatsapp|vocal] pour le segment [segment] de mon
     > établissement FoodEatUp (ID [ID établissement]), nommée « [nom] », avec le message
     > « [message] ».

## Statut

Vidéo montée, VO générée et publiée à la demande de Michael (workflow complet demandé dans
le même message : montage, VO ElevenLabs, publication Lovable FoodEatUp Academy, mise à
jour du dépôt, ajout du thumbnail). Publication limitée à Lovable + dépôt GitHub, comme
demandé — pas d'upload RapidoCMS ni de programmation LinkedIn dans cette tâche.
