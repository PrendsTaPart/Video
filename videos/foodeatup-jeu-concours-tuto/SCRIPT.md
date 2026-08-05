# Tutoriel — Lancer un jeu concours fidélité FoodEatUp

Module `marketing-fidelite` (Marketing, Fidélité & Iris), catalogue 157 tutoriels, item 14
« Lancer un **Jeu concours** fidélité ». Premier tutoriel livré sur ce module (0/24 avant
celui-ci, voir `videos/PROGRESSION-157-TUTORIELS.md`).

Durée livrée : **47,84 s** — H.264/yuv420p, AAC 48 kHz stéréo, faststart.
Audio : true peak **-7,3 dBFS** (mesuré sur le MP4 final, `astats` sur le fichier encodé).

Script validé par Michael le 2026-08-05 avant génération de la VO (STOP obligatoire
respecté, voir `FOODEATUP-TUTORIELS-WORKFLOW.md`).

## Voix off (voix Adam FR, `TGAegA0zNRi8I6nUdq3i`, 8 lignes)

| # | Texte | Durée | Ancrage |
|---|---|---:|---|
| N0 | Lancer un jeu concours fidélité sur FoodEatUp ? C'est prêt en une minute. | 3,94 s | carte d'intro |
| N1 | Dans Fidélité et jeux, ouvrez l'onglet Roue cadeaux et cliquez sur Créer une roue cadeaux. | 5,04 s | clic onglet + **zoom-punch** Créer une roue cadeaux |
| N2 | Nommez votre roue et choisissez la fréquence de jeu, ici un lancer tous les quatorze jours. | 4,86 s | titre + fréquence |
| N3 | Ajoutez vos lots segment par segment : bons d'achat, points fidélité, ou tentatives à retenter. | 5,38 s | défilement des segments |
| N4 | Définissez l'action d'entrée, par exemple la capture d'email, pour transformer chaque joueur en client fidèle. | 6,03 s | Action d'entrée → Email |
| N5 | Cliquez sur Enregistrer la roue : votre jeu concours est en ligne en quelques secondes. | 4,36 s | **zoom-punch** Enregistrer la roue + toast |
| N6 | Partagez le lien ou le QR code en salle pour capter des leads et fidéliser vos clients. | 4,62 s | carte finale (Copier le lien / QR imprimable) |
| N7 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | 5,02 s | carte de fin (CTA) |

N7 réutilise tel quel `foodeatup-tva-tuto/vo/N8.mp3` (CTA générique de la série, texte
identique) — pas de nouvel appel ElevenLabs pour cette ligne.

## Découpage (build.py)

| Seg | Source | Sortie | Contenu |
|---|---|---:|---|
| intro | carte | 4,30 s | LANCER UN JEU CONCOURS |
| A | 0,30 → 3,55 | 3,00 s | Fidélité & jeux, onglet Programme |
| B | 3,55 → 3,85 | 1,30 s | **zoom-punch** onglet Roue cadeaux (696, 324) |
| C | 3,90 → 3,95 | 3,00 s | état vide « Aucune roue » |
| D | 3,95 → 4,15 | 1,80 s | **zoom-punch** Créer une roue cadeaux (949, 717) |
| E | 6,50 → 11,00 | 5,30 s | Nouvelle roue : titre + fréquence (14 jours) |
| F | 12,00 → 18,00 | 5,80 s | Segments : bon €, points, retentez |
| G | 36,00 → 41,60 | 6,40 s | Action d'entrée : Email (capture de lead) |
| H | 44,20 → 44,55 | 1,00 s | **zoom-punch** Enregistrer la roue (258, 672) |
| I | 46,00 → 49,50 | 5,20 s | Toast « Roue enregistrée » + retour liste |
| J | 50,00 → 52,50 | 5,20 s | Carte finale : Copier le lien / QR imprimable |
| outro | carte | 7,70 s | CTA |

Coordonnées des 3 boutons cliqués mesurées par colour-thresholding (scan PIL sur le bleu
FoodEatUp) sur les frames réelles extraites du rush, pas eyeballées.

Piège rencontré et corrigé pendant le montage : la première version du segment D utilisait
la fenêtre source `4.20 → 4.50`, mais le clic réel sur « Créer une roue cadeaux » a lieu
entre 4,15 s et 4,25 s (vérifié par scan de fraction de bleu sur la bbox du bouton) — cette
fenêtre montrait donc déjà la transition post-clic, pas le bouton. Le zoom-punch atterrissait
hors du bouton (boîte orange sous le texte, coupée en bas de cadre). Corrigé en reculant la
fenêtre à `3.95 → 4.15` (bouton encore visible et immobile). Toujours vérifier le zoom-punch
sur une frame extraite du rendu final, pas seulement sur les coordonnées calculées.

Segments B/C/D initialement trop courts (2,84 s cumulés) pour porter N1 (5,04 s) : dérive de
2,3 à 3,8 s accumulée sur les lignes suivantes (même bug que documenté sur `tva`/
`mouvement-stock`). Corrigé en élargissant B/C/D à 1,30/3,00/1,80 s puis en resserrant
E/F/G/I/J sur leurs lignes VO respectives — dérive résiduelle finale : 0,12 s (N4) et 0,40 s
(N5), négligeable.

## Séquence « Utilisez cette fonctionnalité avec Claude » — absente, volontairement

Le MCP FoodEatUp expose `list_wheel_games` et `get_wheel_stats` (lecture seule) mais **aucun
outil de création/mise à jour d'une roue cadeaux**. Conformément à la règle du workflow
(« si aucun outil MCP ne correspond, ne pas ajouter cette séquence — pas de prompt
inventé »), cette vidéo n'a pas de séquence chatbot Claude, et la fiche Lovable
correspondante n'aura pas de champ `claudePrompt`.

## Animations

Mêmes principes que le reste de la série : Ken Burns sur les cartes, xfade (0,28 s),
bandeaux d'étape rendus en deux `drawtext` avec `box=1` (pas de `drawbox` animé — ffmpeg
6.1.1 n'évalue pas `t` dans ses expressions x/y, voir `FOODEATUP-TUTORIELS-WORKFLOW.md`),
encadré orange statique sur les 3 clics zoomés (pas de pulsation animée, `sin(t)` gelé de
toute façon dans ce même ffmpeg). Pas de clip avatar dans ce dossier.

## Statut publication (2026-08-05)

**Montage terminé, en attente de validation Michael avant toute publication** (RapidoCMS,
LinkedIn, site Lovable) — règle du 2026-08-02 dans `FOODEATUP-TUTORIELS-WORKFLOW.md`.
Vignette YouTube générée depuis `assets/intro.jpg` (redimensionnage neutre 1280×720, pas de
recadrage créatif) : `out/thumbnail-youtube.jpg`.
