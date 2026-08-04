# Tutoriel — Assigner les tâches sur le planning FoodEatUp

Deuxième vidéo du module `equipe-planning` (Drive : dossier "ASSIGNER LES TÂCHES SUR
LE PLANNING"). Durée livrée : **41,9 s** (rythme resserré à la demande de Michael,
segments raccourcis vs. un premier montage à 49,9 s) — H.264 High/yuv420p, AAC 48 kHz
stéréo, faststart. Audio : true peak **-7,3 dBFS**. Decode 0 erreur, moov avant mdat.

## Ce que montre le rush (et ce qui n'est pas repris)

Le rush (85,1 s, 1920x828) montre : le planning équipe → clic "Nouvelle tâche" →
formulaire (intitulé "rangement de magasin", employé "alice charbit", date, heure,
priorité "Haute", catégorie "Ouverture", récurrence "Hebdomadaire") → clic "Assigner"
→ la tâche apparaît dans "Tâches de la semaine" → clic sur le crayon "Modifier" →
changement de la récurrence en "Quotidienne" → clic "Enregistrer" → clic sur la case
pour cocher la tâche terminée. La fin du rush (clic "Publier" sur le planning des
**shifts**, pas des tâches) n'est pas reprise : hors sujet pour cette vidéo centrée
sur les tâches (le titre du rush est "Ajout et modifications des tâches", pas
"publication du planning") — garde le montage concentré et sous 60s.

## Voix off (10 lignes, voix Adam FR `TGAegA0zNRi8I6nUdq3i`)

| # | Texte | Durée | Segment |
|---|---|---:|---|
| N0 | Assigner une tâche à votre équipe FoodEatUp, en quelques clics. | 3,47 s | intro |
| N1 | Cliquez sur Nouvelle tâche pour commencer. | 1,99 s | clic "Nouvelle tâche" |
| N2 | Donnez un nom à la tâche, choisissez l'employé et la date. | 3,24 s | C — intitulé/employé/date |
| N3 | Définissez l'heure, la priorité, la catégorie et la récurrence. | 3,58 s | D — heure/priorité/catégorie/récurrence |
| N4 | Cliquez sur Assigner : la tâche apparaît aussitôt dans le planning. | 3,34 s | clic Assigner → succès |
| N5 | Vous pouvez la modifier à tout moment, ici en changeant sa récurrence. | 3,66 s | clic crayon "Modifier" |
| N6 | Cliquez sur Enregistrer, puis cochez la tâche une fois terminée. | 3,34 s | Enregistrer + case à cocher |
| N7 | Vous pouvez aussi le faire depuis Claude : copiez ce prompt, remplacez les crochets. | 4,41 s | étages 1+2 (réutilisé tel quel depuis `foodeatup-produits-tuto`) |
| N8 | Collez-le dans la conversation : votre tâche est assignée en quelques secondes. | 4,02 s | étage 3 |
| N9 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | 5,02 s | carte de fin (CTA, réutilisé tel quel depuis `foodeatup-produits-tuto`) |

N7/N9 réutilisés tels quels — zéro crédit ElevenLabs dépensé sur ces deux lignes.

## Découpage

| Seg | Source | Sortie | Contenu |
|---|---|---:|---|
| intro | carte | 3,00 s | ASSIGNER LES TÂCHES SUR LE PLANNING |
| A | 0,20 → 5,60 | 2,60 s | planning équipe, semaine du 20 au 26 juillet |
| B | 5,60 → 5,90 | 0,90 s | **zoom-punch** sur "Nouvelle tâche" (1644, 540) |
| C | 6,30 → 24,00 | 6,00 s | intitulé "rangement de magasin", employé "alice charbit", date 24/07 |
| D | 33,00 → 55,00 | 6,00 s | heure 09:00, priorité "Haute", catégorie "Ouverture", récurrence "Hebdomadaire" |
| E | 55,00 → 55,30 | 0,90 s | **zoom-punch** sur "Assigner" (1039, 715) |
| F | 55,30 → 57,50 | 2,50 s | tâche listée, toast "Enregistré." |
| G | 59,30 → 59,60 | 0,90 s | **zoom-punch** sur le crayon "Modifier" (1664, 697) |
| H | 60,00 → 65,00 | 5,00 s | modale d'édition, récurrence Hebdomadaire → Quotidienne |
| I | 65,00 → 65,30 | 0,90 s | **zoom-punch** sur "Enregistrer" (1118, 715) |
| J | 69,50 → 69,80 | 0,90 s | **zoom-punch** sur la case à cocher (142, 693) |
| K | 69,80 → 74,00 | 3,00 s | tâche barrée, "1/1 · terminées cette semaine" |
| claude1 | carte générée | 6,00 s | reveal — prompt en gros, fond crème |
| claude2 | carte générée | 3,00 s | confirmation "Copié dans le presse-papiers !" |
| claude3 | carte générée | 6,00 s | mockup chatbot Claude |
| outro | carte | 6,20 s | CTA |

Coordonnées de clic mesurées directement sur les frames extraites du rush,
résolution source native 1920x828.

## Séquence Claude — module partagé

`mcp__FoodEatUp__assign_task(establishment_id, professional_id, name, category?,
date?, time?, priority?)` existe — schéma vérifié, `category` est un champ texte
libre (pas d'enum) :

> Assigne la tâche de nettoyage [nom de la tâche] à [prénom] [nom] (ID employé [ID
> employé]), le [date] à [heure], priorité [priorité], pour mon établissement
> FoodEatUp (ID [ID établissement]).

Même texte (variante "nettoyage") côté vidéo. Fiche Lovable : **3 exemples**
(`claudePrompts[]`) demandés explicitement — nettoyage, mise en place en salle,
préparation d'une recette — le champ `category` étant libre, les trois s'assignent
de la même façon derrière `assign_task`.

## Animations

Mêmes principes que toute la série : Ken Burns sur les cartes, xfade (0,28 s),
bandeaux d'étape, encadré orange pulsant sur les 5 clics (nouveau record de la
série : "Nouvelle tâche" → "Assigner" → crayon "Modifier" → "Enregistrer" → case à
cocher). Pas de clip avatar dans ce dossier.

## Statut publication

Montage terminé et checklist de compatibilité passée (H.264 High/yuv420p, AAC 48 kHz
stéréo, faststart, peak -7,3 dBFS, 0 erreur de décodage). **En attente de validation
avant publication** (règle du 2026-08-02, `videos/LOVABLE-FOODEATUP-DOCS.md`) : pas
d'upload RapidoCMS/LinkedIn (RapidoCMS non authentifié dans cette session de toute
façon), pas d'envoi du prompt Lovable tant que la vidéo n'a pas été revue.
