# Tutoriel — Répondre aux avis

Module `marketing-fidelite` (Marketing, Fidélité & Iris), catalogue 157 tutoriels,
entrée "03 Répondre aux Avis clients" (voir `videos/CATALOGUE-157-TUTORIELS.md`), à la
suite du tutoriel `foodeatup-avis-google-tuto` (02 Synchro Google Avis).

Intrants fournis par Michael : carte d'ouverture `RÉPONDRE_AUX_AVIS.jpg`, carte de fin
`page_fin_vid..jpg` (générique, même asset que les tutoriels précédents), écran
`Répondre_à_un_avis_client.mp4` (1920x828, 30.92s, propre — aucune coupe nécessaire
cette fois, contrairement au tutoriel Synchro Google Avis).

Séquence "Utilisez cette fonctionnalité avec Claude" ajoutée : `mcp__FoodEatUp__
reply_review(establishment_id, review_id, body)` correspond exactement au flux montré
(rédiger puis publier une réponse). Le rush montre aussi une première action — publier
un avis en attente de modération (`mcp__FoodEatUp__moderate_review`, action `publish`)
— avec son propre zoom-punch, mais sans séquence Claude dédiée pour ne pas alourdir la
vidéo (une seule séquence Claude par vidéo dans la série jusqu'ici) ; documentée comme
second exemple dans `claudePrompts[]` côté Lovable.

Durée livrée : **43,12 s** — H.264 High/yuv420p, AAC 48 kHz stéréo, faststart.
Audio : true peak **-7,1 dBFS** (mesuré sur le MP4 final).

## Voix off (Adam FR, `TGAegA0zNRi8I6nUdq3i`)

| # | Texte | Durée | Placement |
|---|---|---:|---|
| N0 | Répondre aux avis clients, directement depuis FoodEatUp. | 3,19 s | carte d'intro |
| N1 | Un nouvel avis arrive : publiez-le en un clic pour qu'il apparaisse sur votre site. | 4,60 s | avis en attente + clic Publier (modération) |
| N2 | Une fois publié, cliquez sur Répondre pour donner suite à votre client. | 3,79 s | avis publié + clic Répondre |
| N3 | Rédigez votre réponse, ou laissez l'agent vous préparer un brouillon. | 3,71 s | modal, rédaction |
| N4 | Cliquez sur Publier : votre réponse apparaît aussitôt sous l'avis, signée par votre établissement. | 5,62 s | clic Publier (réponse) + toast |
| N5 | Résultat : un dialogue public qui rassure vos futurs clients et fait grimper votre taux de réponse. | 5,09 s | plan final, réponse visible |
| N6 | Vous pouvez aussi le faire avec Claude : copiez-collez ce prompt, avec l'identifiant de l'avis et votre réponse. | 5,93 s | séquence Claude, étapes 1-2 |
| N7 | Collez-le dans Claude, et votre réponse est publiée instantanément. | 3,37 s | séquence Claude, étape 3 |
| N8 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | 4,96 s | carte de fin (CTA) |

## Découpage

| Seg | Source | Sortie | Contenu |
|---|---|---:|---|
| intro | carte | 3,60 s | RÉPONDRE AUX AVIS |
| A | 2,00 → 3,20 | 3,30 s | avis "En attente de modération", bandeau "1 - Un nouvel avis" |
| B | 3,20 → 3,60 | 1,00 s | **zoom-punch** sur « Publier » modération (1570, 695) |
| C | 3,60 → 7,30 | 2,70 s | avis publié, bandeau "Avis publié" |
| D | 7,30 → 7,60 | 1,00 s | **zoom-punch** sur « Répondre » (1690, 696) |
| E | 7,60 → 16,80 | 3,70 s | modal "Répondre à Lina", rédaction, bandeau "2 - Rédigez votre réponse" |
| F | 16,80 → 17,10 | 1,00 s | **zoom-punch** sur « Publier » réponse (1176, 644) |
| G | 17,10 → 22,50 | 4,40 s | toast "Réponse publiée sur votre site" |
| H | 22,50 → 30,90 | 5,00 s | plan final, réponse du propriétaire visible sous l'avis |
| claude1-3 | cartes générées | 3,60 + 2,30 + 4,20 s | séquence "Utilisez avec Claude" (reveal, copié, chatbot mockup) |
| outro | carte | 10,43 s (auto-étendue) | CTA |

Pas de coupe volontaire cette fois — le rush est propre de bout en bout (contrairement à
`foodeatup-avis-google-tuto`, sans détour de menu ni erreur de démo à masquer).

## Coordonnées de boutons — page non scrollée

Contrairement au tutoriel Synchro Google Avis (page scrollée différemment selon le
moment du clic, piège documenté dans son propre SCRIPT.md), ce rush garde la page en
haut tout du long : une seule mesure par bouton a suffi, pas de piège de scroll cette
fois.

## Dérive VO vs segments — attendue et absorbée par la carte de fin

Neuf lignes de VO (~40 s de parole cumulée) pour 30,92 s de rush : la dérive
s'accumule progressivement d'une ligne à l'autre (jusqu'à ~4,8 s sur N7) plutôt que de
dépasser sur un seul segment trop court — leçon retenue du premier montage de
`foodeatup-avis-google-tuto` (où un seul segment sous-dimensionné avait fait dériver
toute la fin de 8 à 11 s). Ici, la dérive reste répartie et absorbée par l'extension
automatique de la carte de fin (6,50 s → 10,43 s), sans decalage audio/visuel choquant
sur aucun segment pris isolément (vérifié par relecture de la vidéo rendue).

## Animations

Mêmes principes que le reste de la série : Ken Burns sur les cartes fixes, xfade
(0,28 s) à chaque raccord, bandeaux d'étape en 2 `drawtext` (`box=1`), encadré orange
pulsant sur chaque clic. Séquence Claude partagée (`videos/_shared/claude_prompt_
sequence.py`), `CLAUDE_STAGE_D` personnalisé `[3.60, 2.30, 4.20]` pour laisser respirer
N6 (spanning reveal+copié) et N7 (chatbot mockup). Aucun clip avatar, voix ElevenLabs
de bout en bout.
