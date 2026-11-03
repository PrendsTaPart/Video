# Tutoriel — Brancher Jarvis et son jeton FoodEatUp (module Équipe & Planning)

Troisième vidéo du module `equipe-planning` (suite d'« établir un contrat et son
salaire »). Durée livrée : **58,1 s** — H.264 High/yuv420p, AAC 48 kHz stéréo,
faststart. Audio : true peak **-7,3 dBFS**. Decode 0 erreur, moov avant mdat
(faststart confirmé).

## Ce que montre le rush

Le rush (45,68 s, 1920x828) montre : liste "Employées" (Alice Charbit / Jean Dupont /
Soulayma abdenbi) → clic "Voir" sur Alice → fiche employé, onglet Personnel → clic
onglet "Jarvis" → section "Assistant vocal Jarvis" (Désactivé) avec son explication
("Jarvis donne à cet employé un accès vocal aux outils qu'il a le droit d'utiliser —
mêmes permissions que son rôle — révocable à tout moment") → clic "Activer Jarvis" →
badge "Activé" + boutons "Régénérer le jeton"/"Désactiver" + jeton et QR code révélés
("Copiez le jeton ou scannez le QR maintenant — il ne sera plus jamais affiché") →
menu hamburger → "Module Service" (déplié) → "Jarvis" → page module Jarvis (mockup
téléphone) : "Première utilisation" (mic violet) → "Bonjour alice / Siège appairé"
(mic vert) → onglet "Sièges" du mockup : "2/3 appairé(s)", stats Total/Appairés/Libres,
Alice Charbit (MANAGER, tags Stock/Courses/Finances, "Appairé") → Jean Dupont
(Appairé) → Soulayma abdenbi (MANAGER, mêmes tags, "Libre") → clic "Générer" → retour
à l'onglet Jarvis : "Bonjour soulayma / Siège appairé" + QR + toast "QR généré — à
scanner maintenant." Le détour "Régénérer le jeton" (confirmation "L'ancien sera
immédiatement révoqué") n'est pas repris dans le montage : hors sujet pour ce
tutoriel (affectation d'un jeton, pas régénération).

## Voix off (9 lignes, voix Adam FR `TGAegA0zNRi8I6nUdq3i`)

| # | Texte | Durée | Segment |
|---|---|---:|---|
| N0 | Brancher Jarvis, l'assistant vocal, et générer son jeton dans FoodEatUp ? Voici comment faire. | 5,46 s | intro |
| N1 | Ouvrez la fiche d'un employé, puis direction l'onglet Jarvis. | 3,11 s | clic "Voir" → onglet Jarvis |
| N2 | Cliquez sur Activer Jarvis : un jeton et un QR code sont générés, à copier ou scanner tout de suite. | 5,98 s | clic "Activer Jarvis" → G — jeton/QR |
| N3 | Retrouvez Jarvis dans Module Service, pour gérer tous les sièges vocaux de votre équipe. | 4,60 s | H — menu > Module Service |
| N4 | Une fois le QR scanné, l'employé est reconnu par la voix et peut piloter FoodEatUp à l'oral. | 4,96 s | J — côté employé (mockup téléphone) |
| N5 | Jarvis s'adapte au rôle de chacun : chaque employé n'accède qu'aux outils que ses permissions autorisent. | 5,88 s | K — onglet Sièges (tags de permission) |
| N6 | Pour un nouvel employé, cliquez sur Générer, faites-lui scanner le QR : son siège est aussitôt appairé. | 6,11 s | clic "Générer" → N — résultat |
| N7 | Chaque siège est unique à un employé, avec ses propres droits d'accès — et vous, vous gérez tout FoodEatUp à la voix, simplement en parlant à Jarvis. | 8,80 s | mini-animation Jarvis (2 étages) |
| N8 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | 5,02 s | carte de fin (CTA, réutilisé tel quel) |

N8 réutilisé tel quel depuis `foodeatup-contrat-tuto/vo/` (texte générique — zéro
crédit ElevenLabs dépensé). Les 8 autres lignes sont spécifiques à ce tutoriel (aucune
autre réutilisable telle quelle : contenu Jarvis inédit dans la série).

## Découpage

| Seg | Source | Sortie | Contenu |
|---|---|---:|---|
| intro | carte | 3,60 s | BRANCHER JARVIS ET SON JETON |
| A | 0,20 → 2,20 | 2,60 s | liste "Employées", carte Alice Charbit |
| B | 2,20 → 2,50 | 0,90 s | **zoom-punch** sur "Voir" (392, 682) |
| C | 3,00 → 5,90 | 2,60 s | fiche ouverte, onglet Personnel |
| D | 5,90 → 6,20 | 0,90 s | **zoom-punch** sur l'onglet "Jarvis" (1618, 493) |
| E | 6,30 → 7,45 | 2,30 s | "Assistant vocal Jarvis" — Désactivé |
| F | 7,45 → 7,75 | 0,90 s | **zoom-punch** sur "Activer Jarvis" (1086, 763) |
| G | 9,00 → 13,00 | 6,20 s | Activé + jeton/QR révélés |
| H | 21,50 → 26,30 | 4,20 s | menu hamburger → Module Service déplié |
| I | 26,30 → 26,65 | 0,90 s | **zoom-punch** sur "Jarvis" (nav, 140, 611) |
| J | 29,00 → 33,50 | 5,60 s | page module Jarvis, mockup téléphone (première utilisation → Bonjour alice) |
| K | 34,00 → 37,00 | 4,20 s | onglet "Sièges" — stats + Alice (rôle/permissions) |
| L | 37,50 → 39,40 | 2,30 s | Soulayma — Libre |
| M | 39,40 → 39,70 | 0,90 s | **zoom-punch** sur "Générer" (1110, 459) |
| N | 41,00 → 45,68 | 5,20 s | "Bonjour soulayma / Siège appairé" + QR généré |
| jarvis1 | carte générée | 6,50 s | un siège par employé (rôle + permissions) |
| jarvis2 | carte générée | 6,50 s | contrôlez FoodEatUp à la voix |
| outro | carte | 6,20 s | CTA |

Coordonnées de clic mesurées directement sur les frames extraites du rush
(`ffmpeg -ss t -frames:v 1`), résolution source native 1920x828. Les segments G à N
sont volontairement généreux (5,6-6,2 s) pour absorber la dérive : les lignes VO de ce
tutoriel sont plus longues (jusqu'à 8,8 s pour N7) que sur les tutos précédents — un
premier passage avec des segments calqués sur `foodeatup-contrat-tuto` (2,0-5,0 s)
avait produit jusqu'à 5,5 s de dérive cumulée en fin de vidéo, au point que N7 aurait
démarré après la fin du premier étage de la mini-animation Jarvis. Corrigé en
élargissant les segments concernés — dérive résiduelle maximale 0,95 s (N7), aucun
étage sans narration.

## Mini-animation Jarvis — module partagé (nouveau, pas de séquence Claude)

Aucun outil `mcp__FoodEatUp__*` ne couvre l'appairage téléphone/QR (action physique,
non automatisable) : pas de `claudePrompt` pour ce tutoriel, et la séquence "Utilisez
cette fonctionnalité avec Claude" est remplacée par une mini-animation générique
expliquant le principe de Jarvis, dans `videos/_shared/jarvis_voice_sequence.py`
(nouveau module, même esprit que `claude_prompt_sequence.py` : rendu PNG via PIL,
`card(..., fade=False)`, transitions `slideleft`) :

1. **`render_jarvis_stage1_png`** — un siège Jarvis par employé : 3 avatars (Alice/
   Jean/Soulayma) reliés à un hub "JARVIS" central, chacun avec ses tags de
   permission selon son rôle (Manager → Stock/Courses/Finances, Admin → Équipe/
   Comptabilité/Config) — illustre "Jarvis s'adapte au rôle et aux permissions de
   chacun", cohérent avec l'onglet "Sièges" du rush.
2. **`render_jarvis_stage2_png`** — mic pulsant sur fond crème Claude
   (`#F0EEE6`), dégradé bleu→violet (couleurs réelles du bouton micro Jarvis dans
   l'app), anneaux de "ondes sonores" concentriques — illustre "Contrôlez FoodEatUp à
   la voix".

**Piège rencontré et corrigé pendant la construction du module** : un remplissage
`fill=(r,g,b,alpha)` dessiné directement sur l'image de base (pas de calque séparé +
`Image.alpha_composite`) ne fait *pas* de fondu réel — PIL écrit le tuple RGBA tel
quel et `convert("RGB")` jette juste le canal alpha, donnant un aplat opaque plutôt
qu'une teinte claire. Résultat observé : cercles d'avatar et pastilles de tag rendus
en couleur pleine, texte de même teinte dessiné par-dessus devenu invisible. Corrigé
avec un helper `_tint(color, bg, frac)` qui pré-mélange la couleur avec le fond et
peint un RGB opaque — voir le commentaire dans `jarvis_voice_sequence.py`.

## Animations

Mêmes principes que toute la série : Ken Burns sur les cartes, xfade (0,28 s),
bandeaux d'étape, encadré orange pulsant sur les 5 clics ("Voir", onglet "Jarvis",
"Activer Jarvis", "Jarvis" en navigation, "Générer"). Pas de clip avatar dans ce
dossier.

## Statut publication

Montage terminé et checklist de compatibilité passée (H.264 High/yuv420p, AAC 48 kHz
stéréo, faststart, peak -7,3 dBFS, 0 erreur de décodage). Demande explicite de
Michael de produire et publier cette vidéo en une fois. RapidoCMS non disponible dans
cette session (pas de serveur MCP attaché) : vidéo et vignette hébergées via URL
GitHub raw sur la branche `claude/foodeatup-tutorial-video-vn7udf` de ce dépôt, même
pattern que les tutoriels précédents. Lovable : tutoriel
`brancher-jarvis-et-son-jeton` ajouté dans `src/data/tutorials.ts` (module
`equipe-planning`), sans `claudePrompt` (pas d'outil MCP équivalent), avec un
`chefTip` détaillé sur le principe rôle/permissions et la révocation automatique au
départ d'un employé.
