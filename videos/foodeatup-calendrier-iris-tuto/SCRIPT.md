# Tutoriel — Calendrier de communication avec l'agent Iris

Module `marketing-fidelite` (« Marketing, Fidélité & Iris »), catalogue #24 « Calendrier
de Com' (agent Iris) » — voir `videos/CATALOGUE-157-TUTORIELS.md` (module 8, ligne 106-119).
**Premier tutoriel publié pour ce module** (0/24 avant cette vidéo, voir
`videos/PROGRESSION-157-TUTORIELS.md`).

Durée livrée : **55,7 s** — H.264 High/yuv420p, AAC 48 kHz stéréo, faststart.
Audio : true peak **-7,22 dBFS** (mesuré sur le MP4 final, `astats`). Decode 0 erreur.

**Demande explicite du demandeur de produire et publier cette vidéo en une fois**
(mêmes conditions que `foodeatup-jarvis-tuto` : les deux STOP habituels — validation du
script, puis validation de la vidéo avant publication — sont sautés sur autorisation
explicite donnée en amont).

## Ce que montre le rush

Rush fourni : `Visualiser_le_Calendrier_de_communication_de_Iris.mp4` (95,13 s, 1920x828,
25 fps, H.264/AAC). Il montre la page **Iris**, l'agent marketing IA de FoodEatUp :

1. Onglet **Opportunités** : liste des « Surstock » détectés cette nuit, triés par score
   urgence × valeur commerciale × fraîcheur.
2. Clic sur l'onglet **Calendrier** (≈2,6 s) : la semaine déjà planifiée s'affiche (posts
   par jour, statuts Refusé/À valider, boutons réseaux Facebook/LinkedIn/Instagram/TikTok).
3. Clic sur **Générer les propositions de la semaine** (≈11,2 s) : le bouton passe en
   « Fabrication en cours... » pendant ~22 s (aucun changement visuel, juste le bouton
   désactivé) puis affiche le toast « Propositions de la semaine générées. ».
4. Nouvelle semaine de propositions visible avec statut « À valider », visuels d'abord en
   « Visuel en cours... » puis remplacés par de vraies photos générées automatiquement.
5. Clic sur le menu **⋯** d'une proposition (≈63,0 s) puis sur **Valider & planifier**
   (≈63,4 s) dans le menu déroulant : badge passe à « Validé », toast « Proposition
   validée. ».

Coordonnées mesurées sur les frames extraites du rush (`ffmpeg -i ... -vf fps=2`, méthode
frame-accurate — pas de seek rapide avant `-i`, qui peut sauter au keyframe précédent et
fausser la mesure de plusieurs secondes sur cette source). Page très mobile (défilement
automatique constant sur toute la vidéo) : chaque bouton a été mesuré sur sa propre frame de
clic, pas sur une frame voisine (piège documenté dans `FOODEATUP-TUTORIELS-WORKFLOW.md`).

| Bouton | Coordonnées (1920×828) | Taille |
|---|---:|---:|
| Onglet « Calendrier » | (198, 210) | 220×64 |
| « Générer les propositions de la semaine » | (1585, 283) | 560×68 |
| Menu « ⋯ » sur une proposition | (1745, 268) | 30×30 |
| « Valider & planifier » (option du menu) | (1575, 320) | 190×36 |

## Voix off (10 lignes, voix Adam FR `TGAegA0zNRi8I6nUdq3i`)

| # | Texte | Durée | Ancrage |
|---|---|---:|---|
| N0 | Le calendrier de communication avec Iris, votre agent marketing FoodEatUp ? Voici comment ça marche. | 5,51 s | carte d'intro |
| N1 | Chaque nuit, Iris détecte les meilleures opportunités de publication dans votre activité. | 4,55 s | segment A (Opportunités) |
| N2 | Ouvrez l'onglet Calendrier, puis cliquez sur Générer les propositions de la semaine. | 4,13 s | segment C (post-clic onglet) |
| N3 | Iris analyse vos ventes, vos stocks et les temps forts du moment pour composer chaque publication. | 5,33 s | segment E (fabrication en cours) |
| N4 | En quelques secondes, textes et visuels arrivent, générés automatiquement. | 4,55 s | segment F (résultat) |
| N5 | Chaque proposition affiche la raison détectée : à vous de valider ou de refuser. | 4,55 s | segment H (visuels générés) |
| N6 | Une fois validée, la publication est planifiée automatiquement sur vos réseaux. | 4,36 s | segment K (Validé) |
| N7 | Vous pouvez aussi demander des propositions de campagnes à Claude : copiez ce prompt, remplacez les crochets. | 5,56 s | **séquence Claude — étage 1+2** (reveal + copié) |
| N8 | Collez-le dans la conversation : Iris vous propose aussitôt des campagnes chiffrées, prêtes à lancer. | 5,67 s | **séquence Claude — étage 3** (mockup chatbot) |
| N9 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | 5,02 s | carte de fin (CTA) |

N9 est réutilisée telle quelle depuis `foodeatup-jarvis-tuto/vo/N8.mp3` : la carte de
sortie fournie (`assets/outro.jpg`) est **pixel-identique** (même hash MD5
`bd812eb81382fbbcb5303d06101e6538`) à celle déjà utilisée sur `foodeatup-jarvis-tuto` et
`foodeatup-tva-tuto`, donc son texte générique de CTA est identique — copier le fichier a
évité un appel ElevenLabs.

N2 a été réécrite une fois en cours de montage : la version initiale séparait « ouvrez
Calendrier » (N2) et « cliquez sur Générer » (N3) en deux lignes distinctes ancrées sur le
clic (segment B) puis sur le clic Générer (segment D), ce qui a produit une dérive massive
au premier passage (voir plus bas) — fusionnées en une seule ligne N2 ancrée sur le segment
de contenu C (juste après le premier clic), ce qui libère un ancrage et laisse aux segments
de contenu suivants (E notamment) assez de place pour héberger les lignes plus longues.

## Découpage

| Seg | Source | Sortie | Contenu |
|---|---|---:|---|
| intro | carte | 6,30 s | CALENDRIER IA AVEC IRIS |
| A | 0,30 → 3,00 | 4,60 s | Opportunités détectées par Iris (bandeau « 1 · Iris détecte des opportunités ») |
| B | 2,50 → 2,80 | 0,90 s | **zoom-punch** sur l'onglet « Calendrier » (198, 210) |
| C | 3,00 → 6,00 | 4,20 s | Semaine déjà planifiée (bandeau « 2 · Calendrier de la semaine ») |
| D | 11,00 → 11,30 | 0,90 s | **zoom-punch** sur « Générer les propositions de la semaine » (1585, 283) |
| E | 11,30 → 12,00 | 6,00 s | Fabrication en cours (bandeau « Iris analyse vos données ») — ralenti fort (×0,12) sur un état statique du rush (bouton désactivé, aucune animation visible pendant ~22 s réelles) |
| F | 33,30 → 35,50 | 2,30 s | Toast « Propositions de la semaine générées. » (bandeau « Propositions générées ») |
| G | 44,00 → 48,00 | 3,40 s | Nouvelle semaine, visuels en cours de génération (bandeau « 3 · Textes et visuels par IA ») |
| H | 56,00 → 60,00 | 4,00 s | Visuels générés, propositions prêtes à valider |
| I | 62,90 → 63,15 | 0,90 s | **zoom-punch** sur le menu « ⋯ » (1745, 268) |
| J | 63,30 → 63,55 | 0,90 s | **zoom-punch** sur « Valider & planifier » (1575, 320) (bandeau « 4 · Validez la proposition ») |
| K | 63,55 → 67,50 | 5,00 s | Badge « Validé » + toast « Proposition validée. » |
| claude1 | carte générée | 4,20 s | reveal — prompt en gros, fond crème |
| claude2 | carte générée | 3,10 s | confirmation « Copié dans le presse-papiers ! » |
| claude3 | carte générée | 6,30 s | mockup chatbot Claude (logo + bulles) |
| outro | carte | 6,30 s | CTA |

Le segment E (« Fabrication en cours ») correspond à ~22 s réelles de rush où rien ne bouge
à l'écran (bouton désactivé, pas d'animation de chargement) — conformément à la règle
« éviter les blancs » de `FOODEATUP-TUTORIELS-WORKFLOW.md`, ce temps mort n'est pas
reproduit à l'identique : le segment est simplement étiré (`setpts`) sur une fenêtre source
très courte (0,7 s, contenu strictement statique donc aucun artefact visuel) pour laisser le
temps à la ligne VO N3 de jouer entièrement, puis le montage saute directement au toast de
résultat (segment F, `slideleft`).

## Bug de dérive rencontré et corrigé (premier passage)

Le premier découpage utilisait des segments courts calqués sur `foodeatup-tva-tuto`
(A=3,00s, C=2,60s, E=2,20s, F=3,30s, etc.) avec 11 lignes VO au lieu de 10 (une ligne dédiée
au clic « Générer » en plus). Résultat : dérive cumulée jusqu'à **+11,9 s** sur les
dernières lignes (`drift vs anchors` imprimé par `build.py`), la carte de sortie ayant dû
s'auto-étendre de 6,20 s à 17,87 s pour absorber le débordement — exactement le bug
« narration qui déborde et gonfle artificiellement la carte de sortie » documenté dans
`FOODEATUP-TUTORIELS-WORKFLOW.md`. Cause : les segments de contenu (A, C, E, F...) étaient
dimensionnés sur la durée du rush réel plutôt que sur la durée mesurée de la ligne VO qui
les commente, et deux lignes VO consécutives (« cliquez Générer » ancrée sur un zoom-punch
de 0,90 s, « Iris analyse... » juste après) ne pouvaient physiquement pas tenir dans le
temps disponible avant l'ancrage suivant.

Corrigé en :
1. **Fusionnant** les deux lignes de clic (« ouvrez Calendrier » + « cliquez Générer ») en
   une seule ligne N2, libérant un ancrage.
2. **Recalculant à la main**, pour chaque paire de lignes consécutives, la contrainte
   `S[segment_suivant] - S[segment_courant] >= durée(ligne_courante) + GAP` (en tenant
   compte du recouvrement `xfade` : un segment ne contribue que `target - 0,28s` à la
   frise), puis en redimensionnant chaque segment de contenu en conséquence (ex. E passé de
   2,20 s à 6,00 s, F de 3,30 s à... — voir tableau « Découpage » ci-dessus pour les valeurs
   finales) et les 3 étages Claude (`CLAUDE_STAGE_D`) de `[3.50, 2.50, 6.20]` à
   `[4.20, 3.10, 6.30]`.

Résultat vérifié après correction : **`drift vs anchors: none -- all lines on their
anchors`** (sortie de `build.py`), zéro extension de l'outro nécessaire (`OUTRO_D=6.30`
suffisant tel quel), total 55,68 s. `build.py` calcule et affiche systématiquement ce drift
(`abs(off[k]-anchor[k]) > 0.05`) — le build n'a pas planté sur un drift non nul, mais
c'est ce diagnostic qui a permis de repérer et corriger le problème avant livraison.

## Séquence Claude — module partagé (`videos/_shared/claude_prompt_sequence.py`)

`mcp__Foodeatup__propose_campaigns(establishment_id)` — « Agent IA marketing : 2-4
propositions de campagnes chiffrées depuis les données réelles (RFM, jours creux, marges,
marronniers) ». C'est l'outil MCP qui correspond exactement à l'agent Iris montré dans le
rush (même logique : proposer des actions marketing chiffrées à partir des données réelles
de l'établissement, à valider avant diffusion).

Prompt (identique côté vidéo et côté fiche Lovable `claudePrompt`) :

> Utilise Iris pour me proposer 2 à 4 campagnes marketing chiffrées pour mon établissement
> FoodEatUp (ID [ID établissement]), basées sur mes segments clients, mes jours creux et mes
> marges.

Réplique assistant (étage 3) : « Bien sûr ! Je prépare ces propositions de campagnes pour
votre établissement… ». Durées des 3 étages : `CLAUDE_STAGE_D = [4.20, 3.10, 6.30]`
(override du défaut partagé `[2.20, 1.30, 2.50]`, nécessaire car N7 (5,56 s) doit tenir sur
l'étage 1+2 et N8 (5,67 s) doit tenir entièrement sur l'étage 3 seul — voir règle « mesurer
la VO avant de fixer les durées de segment/étage » dans `FOODEATUP-TUTORIELS-WORKFLOW.md`).

`propose_campaigns` ne prend en paramètre que `establishment_id` : pas de deuxième prompt
`claudePrompts[]` nécessaire ici (contrairement à `saisir-ses-ingredients` ou
`creer-sa-checklist-hygiene`, qui combinent deux outils MCP distincts). Le rush ne montre
pas non plus la création/lancement d'une campagne à partir des suggestions d'Iris (pas de
`create_campaign`/`launch_campaign` filmé) : un second prompt aurait été inventé, donc pas
ajouté (règle « pas de prompt inventé »).

## Animations

Mêmes principes que toute la série : Ken Burns sur les cartes, xfade (0,28 s), bandeaux
d'étape (`banner()`, implémentation **corrigée** — deux `drawtext` avec `box=1`, PAS
`drawbox` + `drawtext`, voir `videos/foodeatup-mouvement-stock-tuto/build.py` et la section
« Pièges déjà rencontrés » de `FOODEATUP-TUTORIELS-WORKFLOW.md`), encadré orange pulsant sur
les 4 clics (onglet Calendrier, bouton Générer, menu ⋯, Valider & planifier). Aucun
apostrophe dans les textes de bandeau. Pas de clip avatar dans ce dossier (voix ElevenLabs
uniquement, comme le reste de la série).

## Checklist de compatibilité (vérifiée sur le MP4 final)

- Vidéo : H.264, profil **High**, `yuv420p`, 1920×828, 25 fps.
- Audio : AAC LC, 48 kHz, stéréo.
- `faststart` : `moov` avant `mdat` (vérifié par lecture des 200 premiers Ko du fichier).
- `ffmpeg -v error -i out.mp4 -f null -` → **0 erreur** de décodage.
- `ffmpeg -i out.mp4 -af astats -f null /dev/null` → **Peak level -7,22 dBFS** (cible
  -4 à -8 dBFS, pas de clipping).
- Durée : 55,68 s.
- Vignette : `out/thumbnail-youtube.jpg`, 1280×720, JPEG, 98 Ko (< 2 Mo) — `assets/intro.jpg`
  (1281×721) simplement redimensionnée + recadrage neutre centré (ratio source déjà très
  proche de 16:9, pas de recadrage créatif).

## Statut publication

Demande explicite de produire et publier cette vidéo en une fois (mêmes conditions que
`foodeatup-jarvis-tuto`) : les deux STOP habituels (validation du script, validation de la
vidéo avant publication) sont sautés sur autorisation donnée en amont. Voir le rapport final
de session pour le détail de la publication GitHub + Lovable (URLs hébergement, statut
RapidoCMS, commit de la fiche `tutorials.ts`).
