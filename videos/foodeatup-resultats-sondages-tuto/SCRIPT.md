# Tutoriel — Résultats des sondages (module Marketing, Fidélité & Iris)

Catalogue #18 du module `marketing-fidelite` (24 vidéos attendues), sous-catégorie
« Jeux & sondages ». Intrants fournis : carte d'intro `R_SULTATS_SONDAGES.jpg`
(mascotte fondateur, 1281x721), carte de fin `page_fin_vid..jpg` (CTA générique,
même carte que le reste de la série) et rush `Retrouver_le_résultat_de_vos_sondages.mp4`
(1920x828, 25 fps, 30,8 s, H.264/AAC).

## Statut : produite sur autorisation directe (2026-08-05)

Même cas que `foodeatup-documents-nettoyage-tuto` et `foodeatup-classeur-haccp-tuto` :
structure, voix off, montage, vignette et publication (GitHub + RapidoCMS + Lovable)
explicitement redemandés en un seul message par l'utilisateur, consigne de publier
« une fois le montage terminé ». Le STOP de validation script/vidéo est levé pour
cette vidéo par cette autorisation explicite ; le fichier est quand même livré via
`SendUserFile` avant publication pour repérage immédiat si correction nécessaire.

## Ce que montre le rush

| t (s) | Écran |
|---:|---|
| 0,0–2,3 | Module "Fidélité & jeux" (tableau de bord : Membres fidélité 4, Points en circulation 15, Points distribués 25, Bons à valider 0), onglet **Sondages** déjà actif, carte "sondage express" (Actif, 3 questions, déclencheur lien/QR, récompense 15 pts) avec boutons Lien / **Résultats (0)** / Modifier / Archiver |
| ≈2,5 | **Clic sur "Lien"** (≈1348, 698) — ouvre le sondage public dans un nouvel onglet |
| 9,0–17,0 | Formulaire public "sondage express" (page cliente, fond crème) : étoiles "Notez votre expérience" (4/5 sélectionné), échelle NPS "Quelle est la probabilité que vous nous recommandiez" (0 à 10, "5" sélectionné), case "Qu'avez-vous le plus apprécié" (service coché), champ Email optionnel, bouton "Envoyer mes réponses" |
| ≈16,8 | **Clic sur "Envoyer mes réponses"** (≈696, 719, page cliente) |
| 18,0–19,5 | Confirmation "✅ Merci pour votre avis !" |
| 20,5–21,5 | Retour au module Fidélité & jeux, carte "sondage express" |
| ≈21,0 | **Clic sur "Résultats"** (≈1496, 698) |
| 22,0–29,0 | Panneau "Sondage express — 1 réponse(s)" : "Notez votre expérience (1 rép.) — Moyenne : 4/5", "Quelle est la probabilité... (1 rép.) — Score NPS : -100", "Qu'avez-vous le plus apprécié (1 rép.) — Service — 1" |

Coordonnées mesurées sur les frames extraites en pleine résolution (1920x828).

## Séquence Claude — outil MCP correspondant

`mcp__Foodeatup__get_survey_results(establishment_id, survey_id)` — « Résultats
agrégés d'un sondage (moyennes, NPS, répartitions) » — correspond exactement à
ce que montre le rush (moyenne étoiles, score NPS, répartition des réponses).
Séquence rendue par `videos/_shared/claude_prompt_sequence.py`, seuls changent
le texte du prompt et la réplique assistant :

> Montre-moi les résultats du sondage [nom du sondage] pour mon établissement
> FoodEatUp (ID [ID établissement]).

Réplique assistant : « Bien sûr ! Je récupère les résultats de ce sondage pour
votre établissement… ». Même texte de prompt côté fiche Lovable (`claudePrompt`).

## Voix off (9 lignes, voix Adam FR `TGAegA0zNRi8I6nUdq3i`)

| # | Texte | Ancrage |
|---|---|---|
| N0 | Retrouver le résultat de vos sondages sur FoodEatUp ? Notes, recommandations, tout est déjà calculé pour vous. | carte d'intro |
| N1 | Depuis Fidélité et jeux, ouvrez l'onglet Sondages et cliquez sur Lien pour partager votre sondage express. | segment B — clic Lien |
| N2 | Votre client note son expérience, répond aux questions, puis envoie ses réponses en un clic. | segment C — formulaire public |
| N3 | De retour sur FoodEatUp, cliquez sur Résultats pour consulter les réponses. | segment H — clic Résultats |
| N4 | Note moyenne, score de recommandation, réponses détaillées : tout est calculé automatiquement. | segment I — panneau résultats |
| N5 | Un aperçu clair de la satisfaction client, prêt à partager avec votre équipe. | segment I (suite) — bénéfice |
| N6 | Vous pouvez aussi le faire depuis Claude : copiez ce prompt, remplacez les crochets. | **étage 1+2** (reveal + copié) — réutilisé tel quel depuis `foodeatup-categories-tuto/vo/N6.mp3`, texte identique |
| N7 | Collez-le dans la conversation : les résultats de votre sondage s'affichent en quelques secondes. | **étage 3** (mockup chatbot) |
| N8 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | carte de fin (CTA) — réutilisé tel quel depuis `foodeatup-dlc-tuto/vo/N8.mp3` |

N6/N8 copiés depuis des tutoriels précédents (texte identique, même voix) —
zéro crédit ElevenLabs dépensé sur ces deux lignes.

## Découpage prévu (durées cibles ajustées après mesure des VO)

| Seg | Source (rush) | Cible | Contenu | Punch |
|---|---|---:|---|---|
| intro | carte | ~7,0 s | RÉSULTATS SONDAGES | — |
| A | 0,00–2,30 | 3,0 s | Module Fidélité & jeux, onglet Sondages, carte "sondage express" | — |
| B | 2,30–2,60 | 0,9 s | zoom-punch clic "Lien" | (1348,698) |
| C | 9,50–11,00 | 4,0 s | Formulaire public : étoiles + NPS + case service | — |
| D | 16,50–16,80 | 0,9 s | zoom-punch clic "Envoyer mes réponses" | (696,719) |
| E | 18,00–19,30 | 2,8 s | Confirmation "Merci pour votre avis" | — |
| F | 20,60–21,00 | 2,0 s | Retour module, carte "sondage express" | — |
| G | 21,00–21,30 | 0,9 s | zoom-punch clic "Résultats" | (1496,698) |
| H | 22,00–29,00 | 6,0 s | Panneau résultats (moyenne, NPS, répartition) | — |
| claude1 | carte générée | 2,20 s | reveal — prompt en gros, fond crème |
| claude2 | carte générée | 1,30 s | confirmation « Copié dans le presse-papiers ! » |
| claude3 | carte générée | 2,50 s | mockup chatbot Claude (logo + bulles) |
| outro | carte | ~6,0 s | CTA (auto-étendu si nécessaire) | — |

Transitions : `fade` sur les enchaînements continus (intro→A, F→G, la bascule
vers/entre les 3 étages Claude en `slideleft`), `slideleft` ailleurs (coupures
de contexte : A→B, B→C, C→D, D→E, E→F, G→H, H→claude1).

## Pas de crop nécessaire

Rush déjà en 1920x828 natif (pas de chrome navigateur à recadrer), comme
`foodeatup-dlc-tuto` — contrairement à `foodeatup-documents-tuto` (capture
Chrome 1920x1020 nécessitant un crop).

## Compatibilité cible (checklist avant livraison)

H.264 High/yuv420p 1920x828 25fps, AAC LC 48 kHz stéréo, faststart (moov avant
mdat), true peak visé ≈ -7 dBFS sur le MP4 final, 0 erreur de décodage.

## Statut publication

En cours — voir tâches de la session : montage → QA → vignette → push GitHub →
upload RapidoCMS → fiche Lovable (module `marketing-fidelite`, avec
`claudePrompt` et `chefTip`) → mise à jour de `LOVABLE-FOODEATUP-DOCS.md` /
`PROGRESSION-157-TUTORIELS.md`.
