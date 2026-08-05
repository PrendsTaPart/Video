# Tutoriel — Lancer une campagne marketing FoodEatUp

**Livrable monté** : `out/foodeatup-campagne-marketing-tuto-v1.mp4` — 50,32 s, H.264/yuv420p
1920x828, AAC 48 kHz stéréo, faststart, peak audio mesuré **-7,3 dBFS**. Vignette YouTube :
`out/thumbnail-youtube.jpg` (recadrage neutre 1280x720 depuis `assets/intro.jpg`, 92 Ko).
Trois zoom-punch (clic "Nouvelle campagne", sélection segment "Tous les clients", clic
"Lancer vers 38 client(s)") — coordonnées mesurées par seuillage couleur (PIL/numpy) sur
les frames réelles, vérifiées visuellement après montage. Pas de `banner()` : la modale
affiche déjà ses 4 étapes en toutes lettres. **En attente de validation Michael avant
publication (STOP obligatoire, voir `FOODEATUP-TUTORIELS-WORKFLOW.md` §6).**

Module 8 « MARKETING, FIDÉLITÉ & IRIS » (`marketing-fidelite`), catalogue 157 tutoriels,
item **05 « Lancer une Campagne marketing »** (`videos/CATALOGUE-157-TUTORIELS.md`).
Premier tutoriel du module (0/24 publiés à ce jour, voir `videos/PROGRESSION-157-TUTORIELS.md`).

Intrants fournis par Michael : `assets/intro.jpg` (carte « LANCER UNE CAMPAGNE »),
`assets/outro.jpg` (carte CTA générique, réutilisée telle quelle), `assets/screen.mp4`
(screen recording 1920x828, 25 fps, 51,16 s, avec audio système — non utilisé, muet au montage).

**Statut : script validé par Michael (2026-08-05) — nom de campagne gardé tel quel
(« Reconquête clients à risque »), `establishment_id` en placeholder générique dans le
`claudePrompt`. Passage en génération VO + montage.**

## Déroulé observé dans le screen recording (frames extraites à 1 fps + zooms ciblés)

| t | Écran | Détail |
|---:|---|---|
| 0-4s | Page « Campagnes & automatisations » | Stats (CA marketing 30j 43,5€ · Messages 30j 3 · Contacts joignables 38 · Automations actives 3/7), onglets (Automations/Campagnes/Agent IA/Agenda/Templates WhatsApp/Segments), section « Campagnes one-shot » (liste existante : Test, Reconnaitre client à risque, 1er commande...) |
| 4s | Clic **Nouvelle campagne** (bouton bleu haut-droit) | Ouvre la modale « Nouvelle campagne » (wizard 4 étapes : 1. Cible · 2. Message · 3. Planification · 4. Conformité) |
| 5-7s | Étape **1. Cible** | Liste de segments RFM calculés chaque nuit : Tous les clients (39), Champions (2), Fidèles (5), Prometteurs (7), À risque... — sélection de **« Tous les clients »** (surbrillance bleue) |
| 8-19s | Étape **2. Message** (nom + canal) | Champ « Nom de la campagne » → texte tapé **« Reconquête clients à risque »** ; « Canal » : Email / SMS / WhatsApp / Vocal → **Email** sélectionné (carte verte) ; « Message » → texte tapé **« Bonjour {prenom}, on vous a manqué ! Profitez de -15 % sur votre prochaine commande avec le code RETOUR15. »** |
| 20-31s | Suite étape 2 (scroll) | Ligne `Variables : {prenom} {plat_prefere} {code} {lien}` ; champ **Offre** → `-15` ; champ **Code promo** → `retour15` ; champ URL de destination laissé vide (défaut : site) ; bloc « Envoi test » (non utilisé) → clic **Continuer** |
| 32-37s | Étape **3. Planification** | Choix **« Envoyer maintenant »** (vs « Planifier ») ; rappel des marronniers à venir (Rentrée J-27, Halloween J-87) → clic **Vérifier la conformité** (bouton passe en « Vérification... ») |
| 38-39s | Étape **4. Conformité** | Récap : Segment **39 clients** · Contactables **38** après conformité · Coût estimé **0,08 €** (email) · Exclus par les garde-fous (1) : STOP (désinscrits) 1 · note RGPD/STOP → clic **Lancer vers 38 client(s)** (icône fusée, passe en chargement) |
| 40-45s | Retour à la liste + toast | Notification bas-droite : **« Campagne lancée : l'envoi part en file, conformité vérifiée client par client. »** — la campagne apparaît dans la liste avec statut « Envoi... » |
| 46-51s | Page « Campagnes & automatisations » | Liste mise à jour, nouvelle entrée **« Reconquête clients à risque »** (Tous les clients · email) en tête |

Outils MCP FoodEatUp correspondants : `create_campaign` (crée le brouillon : name, channel,
segment, message_template, offer_label, promo_code, link_url) puis `launch_campaign`
(envoi réel, `confirm:true` — exactement le déroulé « Continuer » → « Lancer vers N client(s) »
observé dans la vidéo).

## Voix off (proposition, 11 lignes) — voix Adam FR (`TGAegA0zNRi8I6nUdq3i`)

| # | Texte | Ancrage |
|---|---|---|
| N0 | Lancer une campagne marketing sur FoodEatUp ? Suivez le guide. | carte d'intro |
| N1 | Depuis Campagnes, cliquez sur Nouvelle campagne. | clic Nouvelle campagne |
| N2 | Choisissez votre cible parmi les segments calculés chaque nuit. | étape Cible (segment "Tous les clients") |
| N3 | Nommez votre campagne et choisissez son canal, ici Email. | étape Message — nom + canal |
| N4 | Rédigez votre message, votre offre et votre code promo. | étape Message — texte + offre/code |
| N5 | Envoyez maintenant ou planifiez, dans le respect de la fenêtre légale. | étape Planification |
| N6 | Le coût et la conformité sont vérifiés avant chaque envoi. | étape Conformité (39→38, 0,08€) |
| N7 | Un clic sur Lancer, et votre campagne part en file, client par client. | clic Lancer + toast confirmation |
| N8 | Vous pouvez aussi la créer depuis Claude : copiez ce prompt, remplacez les crochets. | séquence Claude — étage 1+2 (reveal + copié) |
| N9 | Collez-le dans la conversation : votre campagne est prête en quelques secondes. | séquence Claude — étage 3 (mockup chatbot) |
| N10 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | carte de fin (CTA — réutilisable telle quelle) |

Durée cible : ~50-55 s (raw 51 s, resserré sur les temps morts de saisie).

## Séquence de fin « cas d'usage + prompt Claude » (module partagé)

`mcp__FoodEatUp__create_campaign` + `mcp__FoodEatUp__launch_campaign` existent tous les deux et
correspondent exactement au flux filmé (créer le brouillon puis lancer). Séquence en 3 temps
(reveal → copié → mockup chatbot Claude) via `videos/_shared/claude_prompt_sequence.py`, comme
sur le reste de la série.

Prompt (identique côté vidéo et côté fiche Lovable `claudePrompt`) :

> Crée une campagne email nommée [nom de la campagne] pour le segment [tous/champions/fideles/prometteurs/a_risque/perdus/nouveaux], avec le message « [votre message, avec {prenom}] », l'offre [-15%] et le code promo [CODE], puis lance-la pour mon établissement FoodEatUp (ID [ID établissement]).

## Fiche Lovable (`src/data/tutorials.ts`, à ajouter après validation)

```
slug: "lancer-une-campagne-marketing"
title: "Lancer une campagne marketing"
moduleSlug: "marketing-fidelite"
subcategory: "Campagnes"
durationSeconds: ~52 (à ajuster après montage final)
howItWorks: [
  "Depuis l'onglet Campagnes, cliquez sur Nouvelle campagne.",
  "Choisissez votre cible parmi les segments RFM calculés chaque nuit (Tous les clients, Champions, Fidèles...).",
  "Nommez la campagne, choisissez le canal (Email, SMS, WhatsApp, Vocal) et rédigez le message.",
  "Ajoutez votre offre et votre code promo — le lien tracké est généré automatiquement.",
  "Envoyez maintenant ou planifiez, en respectant la fenêtre légale d'envoi.",
  "Vérifiez la conformité (contactables après exclusions STOP, coût estimé), puis lancez.",
]
whatItsFor: "Toucher le bon segment de clients avec le bon message, sans risquer un envoi non conforme (STOP, fenêtre légale) — coût et portée connus avant de lancer."
claudePrompt: "<voir ci-dessus>"
```

## À valider avec Michael avant de continuer

1. **Script voix off ci-dessus** (STOP obligatoire avant génération ElevenLabs).
2. `establishment_id` exact à utiliser dans le `claudePrompt` (placeholder générique
   `[ID établissement]` en attendant).
3. Le nom de campagne utilisé dans le screen recording, **« Reconquête clients à risque »**,
   existe déjà en double dans la liste (Test/Reconnaitre client à risque/1er commande visibles
   dès l'écran d'accueil) — confirmer qu'on garde ce nom pour le tuto ou qu'on en choisit un
   plus neutre pour éviter la confusion avec les campagnes de démo déjà présentes sur le compte.
