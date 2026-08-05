# Tutoriel — Retrouver votre agenda marketing (module Campagnes & automatisations) FoodEatUp

Rush fourni par Michael : `Retrouver votre agenda marketing.mp4` (40,8 s, 1920×828,
25 fps, h264+aac, exploitable en entier). Intro `TON_AGENDA_MARKETING.jpg` (mascotte
chef, calendrier), outro `page_fin_vid..jpg` — carte CTA générique déjà utilisée sur
le reste de la série (identique octet pour octet à `foodeatup-haccp-export-tuto/assets/outro.jpg`).

**Statut : v1 montée, validée et publiée (2026-08-05).** VO générée (ElevenLabs,
voix Adam FR `TGAegA0zNRi8I6nUdq3i` ; N6 et N8 réutilisés tels quels depuis
`foodeatup-haccp-export-tuto/vo/` — texte générique identique, zéro crédit sur ces
deux lignes), montage `build.py` terminé.

Durée livrée : **54,72 s** — H.264 High/yuv420p 1920×828 25 fps, AAC 48 kHz stéréo,
faststart confirmé (moov avant mdat). Peak level mesuré sur le MP4 final : **-7,1 dBFS**
(cohérent avec le reste de la série).

## Déroulé observé dans le rush (extraction de frames toutes les 2 s + frames ciblées)

1. `t≈0-2,3s` — Onglet **Agent IA** (module Campagnes & automatisations) : KPIs
   (CA marketing 30 j 43,5 €, Messages 30 j, Contacts joignables 38, Automations
   actives 3/7), section « Votre directeur marketing ia » avec 2 propositions
   chiffrées (« Rentrée Spéciale Jeudi », « Reconquête À Risque Jeudi ») et leur
   justification réelle (marge négative, jeudi = jour le plus creux).
2. `t≈3-4,6s` — Clic sur l'onglet **Agenda** → « Agenda marketing » : calendrier
   août 2026, badges **« Jour creux — jeudi »** sur chaque jeudi détecté.
3. `t≈7,7-7,95s` — Survol du jeudi 6 → bouton **« Créer → »** apparaît, clic.
4. `t≈9,5-11,5s` — Modale « Nouvelle campagne », étape **1. Cible** : nom de
   campagne pré-rempli (« Booster le jour creux »), canal (Email/SMS/WhatsApp/Vocal),
   message.
5. `t≈12-19s` — Étape **2. Message** : variables (`{prenom} {plat_prefere} {code}
   {lien}`), champ Offre (« -5 »), Code promo (« code5 »), URL de destination,
   bloc « Envoi test ».
6. `t≈19,6-26,6s` — Étape **3. Planification** : choix Envoyer maintenant / **Planifier**
   (sélectionné), date et heure saisies (20/08/2026 15:17), marronniers à venir
   (Rentrée J-27, Halloween J-87).
7. `t≈26,8-28,1s` — Étape **4. Conformité** : Segment 39 clients, Contactables 38
   après conformité, Coût estimé 0,08 € (email), Exclus par les garde-fous (1 STOP).
8. `t≈28,15-28,4s` — Clic **« Confirmer la planification »**.
9. `t≈30,3-31s` — Retour calendrier, toast « Campagne planifiée — elle partira
   automatiquement dans la fenêtre légale. »
10. `t≈34,3-36s` — Onglet Campagnes : « Booster le jour creux » apparaît en liste,
    statut **Planifiée 20/08/2026 14:17:00**.

## Voix off (9 lignes)

| # | Texte | Durée | Segment |
|---|---|---:|---|
| N0 | Votre agenda marketing FoodEatUp repère vos jours creux avant vous. Suivez le guide. | 4,86 s | intro |
| N1 | Votre agent IA marketing propose des campagnes chiffrées sur vos vraies données : jour creux, marge, historique. | 6,69 s | A (Agent IA, propositions) |
| N2 | Ouvrez l'onglet Agenda : chaque jour creux détecté apparaît sur votre calendrier, prêt à agir. | 5,85 s | B + clic C (Créer) |
| N3 | Cliquez sur Créer, choisissez votre segment de clients : tous, champions, fidèles, à risque. | 5,69 s | D (étape 1 Cible) |
| N4 | Rédigez votre message avec l'offre et le code promo, puis planifiez l'envoi à la date de votre choix. | 5,33 s | E + F (étapes 2 Message + 3 Planification) |
| N5 | Un dernier écran vérifie la conformité : contacts joignables, coût estimé, exclusions STOP. Confirmez, c'est planifié. | 8,12 s | G + clic H (Confirmer) + I (toast) |
| N6 | Vous pouvez aussi le faire depuis Claude : copiez ce prompt, remplacez les crochets. | 4,41 s | **réutilisé tel quel** depuis `foodeatup-haccp-export-tuto/vo/N6.mp3` — étages 1+2 |
| N7 | Collez-le dans Claude : les propositions de campagnes de votre agenda marketing s'affichent aussitôt. | 5,28 s | étage 3 (mockup chatbot) |
| N8 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | 5,02 s | **réutilisé tel quel** depuis `foodeatup-haccp-export-tuto/vo/N8.mp3` — carte de fin |

## Découpage (segments, offsets réels imprimés par `build.py`)

| Seg | Source | Sortie | Contenu |
|---|---|---:|---|
| intro | carte | 4,40 s | TON AGENDA MARKETING |
| A | 0,20 → 2,30 | 6,80 s | Agent IA : propositions chiffrées |
| B | 4,80 → 7,30 | 5,50 s | Agenda : jours creux détectés |
| C | 7,70 → 7,95 | 0,90 s | **zoom-punch** clic « Créer → » (1046, 372) |
| D | 9,50 → 11,50 | 5,90 s | Étape 1 · Cible |
| E | 12,00 → 19,00 | 5,50 s | Étape 2 · Message |
| F | 19,60 → 26,60 | 3,00 s | Étape 3 · Planification |
| G | 26,80 → 28,10 | 4,50 s | Étape 4 · Conformité |
| H | 28,15 → 28,40 | 0,90 s | **zoom-punch** clic « Confirmer la planification » (1323, 654) |
| I | 30,30 → 31,00 | 2,70 s | Campagne planifiée (toast) |
| claude1/2/3 | cartes générées | 3,00 / 2,30 / 5,60 s | reveal / copié / mockup chatbot |
| outro | carte | 6,83 s (auto-étendue depuis 6,20 s) | CTA |

Coordonnées mesurées sur les frames réelles (`ffmpeg -ss t -frames:v 1`). Dérive
résiduelle (1,1-1,8 s sur N1-N4) absorbée sans cascade par l'auto-extension de la
carte de sortie — pattern déjà accepté sur `foodeatup-haccp-export-tuto`.

## Bug rencontré et corrigé sur ce montage

Le `banner()` copié tel quel depuis `foodeatup-haccp-export-tuto/build.py` utilise
deux `drawbox` avec un `x` animé en fonction de `t` pour le bandeau d'étape — or
`drawbox` (ffmpeg 6.1.1 de cet environnement) n'évalue son `x` qu'une seule fois à
l'initialisation : la plaque orange/bleue reste garée hors champ, seul le texte
blanc de `drawtext` s'affiche (illisible sur fond clair). Bug déjà documenté dans
`FOODEATUP-TUTORIELS-WORKFLOW.md` et déjà corrigé sur d'autres tutos de la série,
mais visiblement pas répercuté dans `foodeatup-haccp-export-tuto/build.py` lui-même.
Corrigé ici en reprenant le correctif de référence de
`foodeatup-mouvement-stock-tuto/build.py` : le bandeau est fait de deux `drawtext`
partageant la même expression de glissement (`box=1` de `drawtext`, qui lui
réévalue bien `x` à chaque frame) — plaque orange décalée de 10 px à gauche,
plaque bleue par-dessus. Vérifié visuellement sur une frame extraite avant/après
(bandeau « Agenda » illisible → lisible).

## Séquence Claude — module partagé

`mcp__FoodEatUp__propose_campaigns(establishment_id)` correspond exactement à
« l'Agent IA marketing » montré à l'écran (2-4 propositions de campagnes chiffrées
depuis les données réelles : RFM, jours creux, marges, marronniers) — vérifié par
un appel réel sur l'établissement 26 (GoSushi). Prompt (identique côté vidéo et
côté fiche Lovable `claudePrompt`) :

> Propose-moi des campagnes marketing pour mon établissement FoodEatUp (ID [ID
> établissement]), basées sur mes jours creux et mes segments de clients.

Réponse assistant (étage 3, mockup) : « Bien sûr ! Votre jour le plus creux est
mercredi. Je vous propose : « Mercredi Délicieux » pour vos clients prometteurs
(-10 %), et « Retour des Risqués » pour reconquérir vos 2 clients à risque. » —
reprend les vraies données retournées par l'appel MCP réel (`slowest_day: mercredi`,
segments `prometteurs`/`a_risque`, noms de campagnes proposés), pas des chiffres
inventés. Le jeudi montré dans le rush correspond à un instantané différent des
données réelles (établissement capturé à un autre moment) ; la réponse Claude
utilise les données actuelles de l'établissement de test, cohérence interne
maintenue en le précisant ici.

Second cas d'usage possible en `claudePrompts[]` (fiche Lovable uniquement, pas
d'étage vidéo dédié) : `mcp__FoodEatUp__create_campaign(...)` pour créer directement
le brouillon de campagne depuis Claude, une fois la cible choisie — pattern
`saisir-ses-ingredients`.

## Astuce du chef / conseil (Lovable, `chefTip`)

« Votre agenda marketing repère vos jours creux tout seul : pas besoin d'ouvrir un
tableur pour savoir quand relancer. Laissez l'Agent IA proposer la campagne
chiffrée, vous n'avez plus qu'à choisir votre segment et valider — le reste part
automatiquement dans la fenêtre légale. Conseil : envoyez votre offre 3 jours
avant un marronnier, pas le jour même — c'est le délai conseillé par FoodEatUp
pour laisser le temps à vos clients de réserver. »

## Cas d'usage (Lovable, `howItWorks` / `whatItsFor`)

- **Comment ça marche** : Ouvrez Campagnes & automatisations → onglet Agenda →
  repérez les jours creux détectés sur votre calendrier ainsi que les marronniers
  à venir → cliquez sur Créer → choisissez votre segment de clients (étape Cible)
  → rédigez votre message avec offre et code promo (étape Message) → planifiez la
  date d'envoi (étape Planification) → vérifiez la conformité (contacts
  joignables, coût, exclusions STOP) → confirmez : la campagne part
  automatiquement dans la fenêtre légale.
- **À quoi sert le marketing dans un restaurant** : remplir les tables aux
  moments qui en ont besoin — relancer un client qui ne revient plus, combler un
  jour creux, ou profiter d'un temps fort commercial. Un **marronnier**, c'est une
  date fixe et récurrente du calendrier (Rentrée, Halloween, Saint-Valentin...)
  sur laquelle les clients attendent une offre chaque année. L'agenda marketing
  centralise tout ça au même endroit : jours creux détectés automatiquement dans
  l'activité de l'établissement et marronniers à venir (alerte 3 jours avant
  chaque échéance), avec des campagnes déjà chiffrées proposées par l'Agent IA
  sur les vraies données (segments RFM, marge, historique).

## Statut publication

Vidéo montée, bug du bandeau corrigé, validée et **publiée le 2026-08-05** :
- **RapidoCMS** : `foodeatup-agenda-marketing-tuto-v1` / `-thumbnail`
- **LinkedIn** (compte FoodEatUp, id 68807312) : brouillon `id 631` planifié au
  prochain créneau libre de la rotation (2 vidéos/j, 7h/16h) — **2026-09-11 07:00**
- **Lovable** (FoodEatUp Academy) : remplit la fiche placeholder déjà présente
  dans `src/data/tutorials.ts` — slug `retrouver-son-agenda-marketing`, module
  `marketing-fidelite` (Marketing, Fidélité & Iris), sous-catégorie
  « 07 · Pack marketing & campagnes », `howItWorks`/`whatItsFor`/`chefTip`/
  `claudePrompt` renseignés (commit Lovable `89a1940`).
