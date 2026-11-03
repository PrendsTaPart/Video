# Tutoriel — Faire son contrôle de conformité FoodEatUp

Module Lovable `haccp` (Hygiène & HACCP). Durée livrée : **52,5 s** — H.264
High/yuv420p, AAC 48 kHz stéréo, faststart. Audio : true peak **-7,2 dBFS**.
Decode 0 erreur, moov avant mdat (faststart confirmé).

## Ce que montre le rush

Rush (24,88 s, fourni par Michael, piste audio quasi silencieuse -91dB — pas de
narration native) : liste « Checklist hygiène » (onglets Hygiène du personnel /
État des locaux) → clic sur un point de contrôle → modal de validation
(date « Relevé le », zone « Fait à », réponse Oui/Non/Non Évalué) → commentaire
+ photo jointe → clic Valider → toast « Checklist validée avec succès ! » et
item mis à jour (date + statut Conforme).

## Voix off (9 lignes)

| # | Texte | Durée | Segment |
|---|---|---:|---|
| N0 | Envie de suivre votre checklist hygiène sans reprendre un carnet papier ? Voici comment faire un contrôle de conformité sur FoodEatUp. | 7,11 s | intro |
| N1 | Dans Hygiène, ouvrez la checklist et cliquez sur le point à contrôler. | 3,60 s | A + clic B |
| N2 | Choisissez la zone concernée, puis indiquez si le point est conforme, non conforme ou non évalué. | 5,93 s | C (zone + résultat) |
| N3 | Ajoutez un commentaire et une photo à l'appui pour garder une preuve horodatée. | 4,31 s | D (commentaire + photo) |
| N4 | Cliquez sur Valider : le contrôle est enregistré aussitôt, avec la date et l'heure exactes. | 5,33 s | clic E + F (succès) |
| N5 | Toute votre traçabilité hygiène reste centralisée, prête à présenter lors d'un contrôle sanitaire. | 5,69 s | F (bénéfice, même écran) |
| N6 | Vous pouvez aussi enregistrer ce contrôle depuis Claude : copiez ce prompt, remplacez les crochets. | 5,43 s | étages 1+2 |
| N7 | Collez-le dans la conversation : votre checklist est validée en quelques secondes. | 4,31 s | étage 3 |
| N8 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | 5,02 s | carte de fin (CTA, réutilisée) |

N8 réutilisé tel quel depuis `foodeatup-bl-tuto/vo/` (texte générique — zéro
crédit ElevenLabs dépensé). N0-N7 générés via ElevenLabs, voix Adam FR
(`TGAegA0zNRi8I6nUdq3i`), `eleven_multilingual_v2`.

## Découpage

| Seg | Source | Sortie | Contenu |
|---|---|---:|---|
| intro | carte | 2,80 s | FAIRE SON CONTRÔLE DE CONFORMITÉ |
| A | 0,30 → 2,70 | 5,50 s | liste Checklist hygiène |
| B | 2,70 → 3,10 | 0,90 s | **zoom-punch** sur le point de contrôle (1717, 501) |
| C | 3,10 → 10,50 | 6,50 s | modal : zone « A - Cuisine Quotidien » + réponse Oui |
| D | 10,50 → 19,00 | 5,00 s | commentaire + photo jointe |
| E | 19,00 → 19,50 | 0,90 s | **zoom-punch** sur Valider (1024, 759) |
| F | 20,50 → 24,88 | 11,50 s | toast succès + item mis à jour (Conforme) |
| claude1 | carte générée | 6,50 s | reveal — prompt en gros, fond crème |
| claude2 | carte générée | 3,00 s | confirmation « Copié dans le presse-papiers ! » |
| claude3 | carte générée | 6,50 s | mockup chatbot Claude |
| outro | carte | 6,20 s | CTA |

Coordonnées des boutons eyeballées sur frames extraites (marge large gardée
avec le zoom 1.20x). F est volontairement long (setpts ralenti ~2.6x sur un
raw de 4,38s) pour porter à la fois N4 (validation) et N5 (bénéfice
traçabilité) sur le même écran de succès — même principe que G1/G2 sur
`foodeatup-bl-tuto`.

## Séquence Claude — module partagé

`mcp__FoodEatUp__create_hygiene_checklist_validation(establishment_id,
template_id, reponses, zone_controle?, commentaires?, statut?)` — schéma
vérifié, correspond exactement à ce que montre le rush (zone + réponse
oui/non/non évalué + commentaire) :

> Valide le point de contrôle [nom du point de contrôle] (modèle ID [ID du
> modèle]) pour la zone [zone contrôlée], réponse [oui/non/non évalué],
> commentaire [commentaire], pour mon établissement FoodEatUp (ID [ID
> établissement]).

Même texte côté fiche Lovable (`claudePrompt`). Pas de champ photo exposé par
l'outil MCP — non mentionné dans le prompt (règle : pas de prompt inventé).

## Animations

Mêmes principes que toute la série : Ken Burns sur les cartes, xfade (0,28 s),
bandeaux d'étape, encadré orange pulsant sur les 2 clics. Pas de clip avatar
dans ce dossier (VO ElevenLabs uniquement).

## Statut publication

Pipeline exécuté de bout en bout sur demande explicite de Michael (script,
voix, montage, QA, puis publication Lovable) — étapes de validation
intermédiaires proposées lors du tutoriel précédent (`foodeatup-bl-tuto`) et
déjà couvertes par cette demande groupée.
