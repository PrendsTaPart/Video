# Tutoriel — Créer un site par IA FoodEatUp

Module 3 « Site Web & Vitrine » (`site-web-vitrine`), tuto **05/8** du catalogue
(voir `videos/CATALOGUE-157-TUTORIELS.md`). Rush fourni : `Créer_son_site_avec_l'IA.mp4`
(41,68 s, 1920x828, 25 fps) — début de l'interview IA (agent FoodEatUp qui pose
12 questions pour générer le site), 3 des 12 questions visibles à l'écran.

Durée livrée : **40,28 s** — H.264 High/yuv420p, AAC 48 kHz stéréo, faststart.
Audio : true peak **-7,3 dBFS** (mesuré sur le MP4 final avec `astats`, dans la
marge cible du pipeline).

Pas d'avatar HeyGen dans ce dossier. Pas de clic à l'écran (interface de chat,
pas de bouton à zoomer) : segments en simple accélération (`setpts`) + bandeau
d'étape, sans zoom-punch.

## Voix off (8 lignes, voix Adam FR `TGAegA0zNRi8I6nUdq3i`)

| # | Texte | Durée | Ancrage |
|---|---|---:|---|
| N0 | Créer le site de votre restaurant avec l'IA ? Il suffit de répondre à quelques questions. | 4,96 s | carte d'intro |
| N1 | L'agent FoodEatUp vous pose une première question sur l'ambiance de votre établissement. | 4,26 s | segment A (interview démarrée) |
| N2 | Répondez simplement, en langage naturel : jeune, chaleureuse, vos plats signatures... | 5,04 s | segment B (réponses en langage naturel) |
| N3 | Douze questions suffisent pour cerner votre identité et vos plats. | 3,66 s | segment C, début (le site prend forme) |
| N4 | L'IA génère alors tout : pages, textes et mise en page, prêts à publier. | 5,02 s | segment C, suite (bénéfice, tenue sur le même plan) |
| N5 | Vous pouvez aussi le déclencher depuis Claude : copiez ce prompt, remplacez les crochets. | 4,49 s | étages 1+2 (reveal + copié) |
| N6 | Collez-le dans la conversation : votre site est généré en quelques secondes. | 4,02 s | étage 3 (mockup chatbot) |
| N7 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | 5,02 s | carte de fin (CTA) |

N7 réutilisée telle quelle depuis `foodeatup-tva-tuto/vo/N8.mp3` (texte CTA
identique).

**Bug de mapping rencontré et corrigé avant livraison** : au premier montage,
N4 (bénéfice) avait été branché sur l'étage Claude "reveal" et N5 (reveal) sur
l'étage "chatbot", tandis que N6 (chatbot, "Collez-le dans la conversation…")
n'était tout simplement jamais inclus dans le mix audio — laissé de côté par
erreur lors du passage de la numérotation à 9 lignes (gabarit série) à cette
vidéo qui n'en utilise que 8. Repéré en revérifiant le texte de chaque `.mp3`
contre son ancrage (règle déjà posée dans `FOODEATUP-TUTORIELS-WORKFLOW.md` à
propos de `foodeatup-fournisseurs-tuto`) avant tout envoi à validation — corrigé
en réalignant `anchor`/`keys` sur les 8 fichiers réels et en allongeant le
segment C pour absorber N3+N4 sans bavure sur l'étage Claude suivant.

## Découpage

| Seg | Source | Sortie | Contenu |
|---|---|---:|---|
| intro | carte | 5,30 s | CRÉER UN SITE PAR IA |
| A | 0,20 → 9,50 | 4,80 s | navigation + question 1 (ambiance) affichée |
| B | 9,50 → 24,00 | 5,20 s | réponse "Douce", question 2 (clientèle), réponse "Jeunes" |
| C | 24,00 → 41,60 | 10,10 s | question 3 (plats signatures), réponse "Sushi", question 4 (ton) — tenu plus long pour porter N3+N4 |
| claude1 | carte générée | 3,00 s | reveal — prompt en gros, fond crème |
| claude2 | carte générée | 2,30 s | confirmation « Copié dans le presse-papiers ! » |
| claude3 | carte générée | 5,30 s | mockup chatbot Claude |
| outro | carte | 6,17 s (auto-étendue) | CTA |

Rush très condensé (41,68 s couvrant seulement le tout début des 12 questions,
pas de récapitulatif du site généré) — accélération modérée sur A/B, et C tenu
volontairement long (facteur ×1,74 seulement) pour porter à la fois la fin de
l'interview et la ligne bénéfice sans nouvelle image disponible.

Offsets réels vérifiés après ce correctif (`offsets:` imprimé par `build.py`) :
N5 se termine à 29,01 s, l'étage `claude3` démarre à 29,02 s — raccord à moins
de 10 ms, aucune bavure d'une ligne sur le mauvais étage.

## Piège rencontré (bandeaux invisibles — `drawbox`/`t`)

Premier build : bandeaux d'étape invisibles (texte fantôme blanc sur le panneau
« ÉDITEUR IA » en bas à gauche, aucune plaque orange/bleue visible). Cause
identique au bug déjà documenté dans `FOODEATUP-TUTORIELS-WORKFLOW.md` :
`drawbox` (ffmpeg 6.1.1) n'évalue `x`/`y` qu'une fois à l'init, pas par frame —
un `x` glissant en fonction de `t` reste figé à sa valeur `t=0` (hors champ).
Corrigé en reprenant le `banner()` de référence de
`videos/foodeatup-mouvement-stock-tuto/build.py` : la plaque est la `box=1` de
`drawtext` (deux passes, orange puis bleue), qui elle réévalue bien son `x` à
chaque frame. Vérifié visuellement par extraction de frame après correctif
(bandeaux lisibles aux 3 étapes A/B/C).

## Séquence Claude — module partagé

Aucun outil MCP FoodEatUp ne couvre littéralement une interview conversationnelle
générative. L'équivalent exposé le plus proche est
`mcp__FoodEatUp__apply_site_template(establishment_id, slug, confirm)` (le site
est régénéré en un appel à partir d'un template), combiné à
`mcp__FoodEatUp__publish_site(establishment_id, confirm)` puisque le rush montre
justement un site prêt à publier en sortie d'interview. Séquence en 3 temps
(reveal → copié → mockup chatbot) via `videos/_shared/claude_prompt_sequence.py`,
mêmes durées d'étage que `foodeatup-tva-tuto` ([3.00, 2.30, 5.30]).

Prompt (identique côté vidéo et côté fiche Lovable `claudePrompt`) :

> Génère mon site avec l'IA : applique le template [nom du template] adapté à
> l'ambiance [ambiance] pour mon établissement FoodEatUp (ID [ID établissement]),
> puis publie-le.

## Astuce du chef

Soyez précis dans vos réponses (plats signatures, ambiance, clientèle) : plus
l'interview est détaillée, plus le site généré vous ressemble dès le premier
essai.

## Livrables

- `out/foodeatup-site-ia-tuto-v1.mp4` (34,88 s)
- `out/thumbnail-youtube.jpg` (1280x720, image d'ouverture fournie, resize neutre
  sans recadrage créatif)

## Statut

**Script validé par Michael le 2026-08-04** (avant génération voix/montage).
Montage terminé, en attente de validation du rendu final avant publication
(RapidoCMS + LinkedIn + site Lovable + mise à jour du catalogue) — voir règle
« STOP obligatoire » de `FOODEATUP-TUTORIELS-WORKFLOW.md`.
