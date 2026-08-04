# Tutoriel — Établir un contrat et son salaire FoodEatUp (module Équipe & Planning)

Deuxième vidéo du module `equipe-planning` (suite de "Ajouter ses employés"). Durée
livrée : **53,2 s** — H.264 High/yuv420p, AAC 48 kHz stéréo, faststart. Audio : true
peak **-7,2 dBFS**. Decode 0 erreur, moov avant mdat (faststart confirmé).

## Ce que montre le rush

Le rush (66,28 s, 1920x828) montre : liste "Employées" (carte "Alice charbit / Chef")
→ clic "Voir" → fiche employé, onglet Personnel → clic onglet "Salaire" → section
"Contrat de travail" vide ("Aucun contrat") → clic "Créer maintenant" → modal "Créer
un contrat" rempli en direct (type CDI, intitulé du poste "Chef de rang", date de
début 23/07/2026, salaire mensuel brut 1800€, indemnité transport 50€/mois, 35h et
5 jours par semaine, nom du responsable "jean dupont", détails salaire/avantages
— primes, mutuelle 60%, tickets restaurant 8€, pourboires partagés —, durée/
précisions "CDI avec 2 mois d'essai", document `contrat.pdf` joint) → clic "Créer
le contrat" → la fiche Salaire affiche aussitôt le contrat créé et le solde de
congés (0/25 jours utilisés, 25 jours restants).

## Voix off (9 lignes, voix Adam FR `TGAegA0zNRi8I6nUdq3i`)

| # | Texte | Durée | Segment |
|---|---|---:|---|
| N0 | Établir un contrat et fixer un salaire dans FoodEatUp ? Voici comment faire. | 4,18 s | intro |
| N1 | Ouvrez la fiche d'un employé, puis direction l'onglet Salaire. | 3,11 s | clic "Voir" → onglet Salaire |
| N2 | Cliquez sur Créer maintenant, choisissez le type de contrat, le poste et la date de début. | 4,73 s | clic "Créer maintenant" → G — type/poste/dates |
| N3 | Renseignez le salaire, les horaires et le nom du responsable. | 3,24 s | H — salaire/horaires/responsable |
| N4 | Ajoutez les avantages, la durée d'essai, et joignez le contrat en pièce jointe. | 4,26 s | I — avantages/durée/document |
| N5 | Cliquez sur Créer le contrat : il apparaît aussitôt dans la fiche, avec le solde de congés de l'employé. | 5,28 s | clic "Créer le contrat" → K — résultat (bénéfice) |
| N6 | Vous pouvez aussi le faire depuis Claude : copiez ce prompt, remplacez les crochets. | 4,41 s | étages 1+2 (réutilisé tel quel depuis `foodeatup-produits-tuto`/`foodeatup-employes-tuto`) |
| N7 | Collez-le dans la conversation : le contrat est créé en quelques secondes. | 3,66 s | étage 3 |
| N8 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | 5,02 s | carte de fin (CTA, réutilisé tel quel) |

N6/N8 réutilisés tels quels (texte générique identique) — zéro crédit ElevenLabs
dépensé sur ces deux lignes.

## Découpage

| Seg | Source | Sortie | Contenu |
|---|---|---:|---|
| intro | carte | 3,00 s | ÉTABLIR UN CONTRAT ET SON SALAIRE |
| A | 0,20 → 2,20 | 2,30 s | liste "Employées", carte Alice charbit |
| B | 2,20 → 2,50 | 0,90 s | **zoom-punch** sur "Voir" (392, 682) |
| C | 3,00 → 5,10 | 2,00 s | fiche ouverte, onglet Personnel |
| D | 5,10 → 5,40 | 0,90 s | **zoom-punch** sur l'onglet "Salaire" (1358, 362) |
| E | 5,50 → 7,40 | 2,00 s | "Contrat de travail" — Aucun contrat |
| F | 7,40 → 7,70 | 0,90 s | **zoom-punch** sur "Créer maintenant" (1432, 505) |
| G | 9,00 → 24,00 | 6,00 s | type CDI, poste, date de début |
| H | 24,00 → 42,00 | 6,00 s | salaire, indemnité, heures/jours, responsable |
| I | 42,00 → 58,30 | 6,00 s | détails salaire/avantages, durée, document |
| J | 58,30 → 58,60 | 0,90 s | **zoom-punch** sur "Créer le contrat" (1037, 718) |
| K | 60,00 → 66,28 | 5,00 s | fiche Salaire mise à jour + solde de congés |
| claude1 | carte générée | 6,00 s | reveal — prompt en gros, fond crème |
| claude2 | carte générée | 3,00 s | confirmation "Copié dans le presse-papiers !" |
| claude3 | carte générée | 6,00 s | mockup chatbot Claude |
| outro | carte | 6,20 s | CTA |

Coordonnées de clic mesurées directement sur les frames extraites du rush
(`ffmpeg -ss t -frames:v 1`), résolution source native 1920x828 — boutons identifiés
visuellement à chaque clic (mêmes coordonnées de "Voir" que sur
`foodeatup-employes-tuto`, cohérent : même composant de carte employé).

## Séquence Claude — module partagé

`mcp__FoodEatUp__create_employee_contract(establishment_id, employee_id, type?,
job_title?, start_date?, end_date?, base_salary?, weekly_hours?, days_per_week?,
manager_name?)` existe — schéma vérifié. L'indemnité transport, les détails
salaire/avantages, la durée/précisions et le document contractuel sont visibles à
l'écran mais n'ont pas de champ correspondant dans le schéma MCP (même logique que
`create_product` qui n'expose pas l'affiliation recette) :

> Crée un contrat [type de contrat] pour l'employé [ID employé], poste [intitulé du
> poste], à partir du [date de début], salaire brut mensuel de [salaire]€, [heures]h
> et [jours] jours par semaine, responsable [nom du responsable], pour mon
> établissement FoodEatUp (ID [ID établissement]).

Même texte côté fiche Lovable (`claudePrompt`).

## Animations

Mêmes principes que toute la série : Ken Burns sur les cartes, xfade (0,28 s),
bandeaux d'étape (accents restaurés, pas d'apostrophe dans les bandeaux — piège
`drawtext` déjà rencontré sur `foodeatup-ingredients-tuto`), encadré orange pulsant
sur les 4 clics ("Voir", onglet "Salaire", "Créer maintenant", "Créer le contrat").
Pas de clip avatar dans ce dossier.

## Statut publication

Montage terminé et checklist de compatibilité passée (H.264 High/yuv420p, AAC 48 kHz
stéréo, faststart, peak -7,2 dBFS, 0 erreur de décodage). Demande explicite de
Michael de produire et publier cette vidéo en une fois (message du 2026-08-03) :
RapidoCMS non disponible dans cette session (pas de serveur MCP attaché) — vidéo et
vignette hébergées via URL GitHub raw sur la branche `claude/foodeatup-tutorial-video-vn7udf`
de ce dépôt, même pattern que `ouvrir-sa-vitrine-en-ligne`/`diffuser-son-qrcode`/
`ajouter-ses-employes`. Lovable : tutoriel `etablir-son-contrat-et-son-salaire`
ajouté dans `src/data/tutorials.ts` (module `equipe-planning`).
