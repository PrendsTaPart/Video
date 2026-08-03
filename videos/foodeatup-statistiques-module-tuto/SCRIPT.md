# Tutoriel — Lire ses statistiques par module (FoodEatUp)

Intrants fournis par Michael : `LIRE_SES_STATISTIQUES_PAR_MODULE.jpg` (carte intro),
`page_fin_vid..jpg` (carte outro CTA, générique — identique aux autres tutos),
`Statistique_et_performances_par_Module.mp4` (screen recording, **1920×828, 25 fps,
50,64 s**).

## Ce que montre le rush

Le rush parcourt le tableau de bord **« Analytix BI »** (« Statistiques & Business
Intelligence ») puis chacun de ses 6 modules :

1. **Tableau de bord** (0–9s) — 4 KPI globaux (Chiffre d'affaires, Commandes, Marge
   brute, Score HACCP), un graphique « Évolution du chiffre d'affaires » avec tooltip
   au survol, puis la grille des 6 modules.
2. **Finances** (~11–19s) — mêmes 4 KPI recalculés sur le module, + graphique « CA par
   catégorie » (donut) + « Top 5 produits ».
3. **Stocks** (~19–27s) — graphique « Mouvements de stock (entrées/sorties) » + liste
   « Produits sous seuil alerte » (ex. Poissonnerie 0/5, Mozarella 2/5…).
4. **RH & Pointage** (~27–32s) — Heures travaillées, Jours d'absence, Types de congés,
   « Congés par type » (vide sur ce compte de démo).
5. **HACCP** (~32–38s) — Taux de conformité HACCP, Anomalies températures (94,4 %),
   graphique « Anomalies par mois ».
6. **Production** (~38–43s) — graphique « Production prévue vs réalisée ».
7. **Assistant IA** (~43–50,6s) — champ « Posez une question sur vos données BI »
   (ex. « Pourquoi ma marge a-t-elle baissé ? »).

Chaque module a son propre sélecteur de dates (période commune : 30/06/2026 →
29/07/2026) et son propre bouton « Appliquer », visible en haut de chaque page. Aucune
action de création : c'est un tutoriel de **lecture** (navigation + interprétation des
chiffres), pas de saisie.

## ⚠️ Points à valider avant de générer quoi que ce soit (script pas encore audio)

Conformément à `videos/FOODEATUP-TUTORIELS-WORKFLOW.md` (étape 3, STOP obligatoire) et
`videos/LOVABLE-FOODEATUP-DOCS.md` (règle de validation du 2026-08-02) : **le script
ci-dessous n'est pas encore validé, aucune VO ni montage n'a été lancé.**

1. **Module Lovable** : les 5 catégories actuelles du site
   (`configuration` / `equipe-planning` / `comptabilite` / `haccp` / `stockvision-ai`)
   ne couvrent pas exactement une fonctionnalité transverse comme Analytix BI (elle
   touche Finances, Stocks, RH, HACCP et Production à la fois). Proposition : la ranger
   sous `comptabilite` (le tableau de bord s'ouvre sur les KPI financiers, et le prompt
   Claude proposé porte sur les finances) — **à confirmer, ou dites-moi si vous préférez
   un nouveau moduleSlug dédié (ex. `statistiques-bi`)**.
2. **Prompt Claude** : aucune action de création dans ce rush, donc je propose d'utiliser
   l'outil MCP en **lecture** `mcp__FoodEatUp__finance_summary` (CA facturé/encaissé,
   impayés, dépenses, marge sur une période) — c'est la donnée la plus proche de l'écran
   Finances montré à l'écran. Prompt proposé :
   > Donne-moi la synthèse financière de mon établissement FoodEatUp (ID
   > [ID établissement]) du [date début] au [date fin].
   **À confirmer** (ou remplacer par un autre outil `get_daily_brief` / `get_pos_report`
   si vous préférez un angle différent).
3. **Numéro de sous-catégorie** dans le Drive/tableau de suivi — je n'ai pas ce numéro,
   à me donner ou je le déduis de la suite logique (11).

## Voix off proposée (10 lignes, Adam FR `TGAegA0zNRi8I6nUdq3i`)

| # | Texte | Durée estimée | Segment |
|---|---|---:|---|
| N0 | Vos statistiques FoodEatUp, module par module, en un coup d'œil. | ~4,1 s | intro |
| N1 | Le tableau de bord Analytix BI réunit votre chiffre d'affaires, vos commandes et votre marge sur la période choisie. | ~7,2 s | A — Tableau de bord |
| N2 | Ouvrez le module Finances pour votre chiffre d'affaires par catégorie et votre top 5 produits. | ~5,5 s | B — Finances |
| N3 | Le module Stocks repère aussitôt les produits sous leur seuil d'alerte. | ~4,7 s | C — Stocks |
| N4 | RH et Pointage suivent les heures travaillées, les absences et les congés de votre équipe. | ~5,8 s | D — RH & Pointage |
| N5 | HACCP affiche vos anomalies de température, et Production compare le prévu au réalisé. | ~5,8 s | E+F — HACCP / Production |
| N6 | Et l'assistant IA répond en langage naturel à toutes vos questions sur ces données. | ~5,5 s | G — Assistant IA (bénéfice) |
| N7 | Vous pouvez aussi interroger vos statistiques depuis Claude : copiez ce prompt, remplacez les crochets. | ~6,1 s | étage 1 (reveal) |
| N8 | Collez-le dans la conversation : votre synthèse financière arrive en quelques secondes. | ~5,5 s | étage 3 (chatbot) |
| N9 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | 5,02 s | carte de fin (CTA, **réutilisé tel quel** depuis `foodeatup-produits-tuto/vo/N8.mp3` — zéro crédit ElevenLabs) |

Durées N0–N8 estimées au même rythme que les tutos précédents (~16 car/s) — seront
mesurées exactement après génération.

## Découpage proposé (source 1920×828, 25 fps)

| Seg | Source | Sortie visée | Contenu | Bannière (sans apostrophe) |
|---|---|---:|---|---|
| intro | carte | 3,00 s | LIRE SES STATISTIQUES PAR MODULE | — |
| A | 0,50 → 9,80 | 6,00 s | Tableau de bord Analytix BI, KPI + graphique + grille modules | 1 · Tableau de bord |
| B | 11,50 → 19,00 | 5,00 s | Finances : KPI, CA par catégorie, top 5 produits | 2 · Finances |
| C | 19,50 → 27,00 | 4,50 s | Stocks : mouvements + produits sous seuil | 3 · Stocks |
| D | 27,30 → 32,00 | 4,00 s | RH & Pointage : heures, absences, congés | 4 · RH et Pointage |
| E | 32,30 → 37,80 | 4,00 s | HACCP : conformité, anomalies températures | 5 · HACCP |
| F | 38,00 → 42,50 | 3,50 s | Production : prévu vs réalisé | 6 · Production |
| G | 43,00 → 50,60 | 5,00 s | Assistant IA : question en langage naturel | 7 · Assistant IA |
| claude1 | carte générée | 6,00 s | reveal — prompt en gros, fond crème | — |
| claude2 | carte générée | 3,00 s | confirmation « Copié dans le presse-papiers ! » | — |
| claude3 | carte générée | 6,00 s | mockup chatbot Claude | — |
| outro | carte | 6,20 s (extensible) | CTA | — |

Transitions : `fade` entre chaque page (navigation continue, même style que les clics
dans les tutos précédents), `slideleft` pour les 3 étages Claude (scènes distinctes),
`fade` claude3 → outro. Aucun zoom-punch : ce rush ne montre aucun clic sur un bouton
d'action primaire (Ajouter/Créer/Enregistrer), uniquement de la navigation entre pages
de lecture — cohérent avec la règle "pas de zoom-punch inventé".

## Séquence Claude — module partagé

`mcp__FoodEatUp__finance_summary(establishment_id, date_from?, date_to?)` — lecture
seule, correspond à l'écran Finances montré dans le rush (schéma vérifié : CA facturé,
encaissé, impayés, dépenses, marge sur une période).

> Donne-moi la synthèse financière de mon établissement FoodEatUp (ID
> [ID établissement]) du [date début] au [date fin].

Même texte prévu côté fiche Lovable (`claudePrompt`), une fois validé.

## Animations

Mêmes principes que toute la série : Ken Burns sur les cartes intro/outro, xfade
(0,28 s) entre tous les segments, `setpts` pour le retiming (jamais `zoompan` sur la
vidéo réelle). Pas de bandeau avec apostrophe (bug déjà rencontré sur
`foodeatup-ingredients-tuto`) — vérifié sur toutes les bannières ci-dessus.

## Statut

**Script en attente de validation (pas de VO générée, pas de montage lancé).** Une fois
le script + les 3 points ci-dessus confirmés (module Lovable, prompt Claude, numéro de
sous-catégorie), je génère la VO (Adam FR ElevenLabs, réutilisation du N9/outro), monte
la vidéo, puis la livre pour validation finale avant toute publication (RapidoCMS,
LinkedIn, Lovable) — comme pour tous les tutos précédents.
