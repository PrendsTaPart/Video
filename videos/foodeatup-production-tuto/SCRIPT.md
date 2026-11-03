# Tutoriel — Valider une production (Quantité, Température, note)

Module **HACCP**. Durée livrée : **47,0 s** — H.264 High/yuv420p 1920×828 @25 fps,
AAC-LC 48 kHz stéréo 192 kb/s, faststart (moov avant mdat). Audio : true peak
**-7,1 dBFS** (dans la marge cible du pipeline). Decode 0 erreur.

Pas de clip avatar dans ce dossier — conforme au module 4, qui n'en fournit aucun
(voir `FAISABILITE-SERIE-TUTORIELS.md` §3.1) : la carte d'intro porte N0 et toute
la narration est en voix ElevenLabs (Adam FR `TGAegA0zNRi8I6nUdq3i`).

## Voix off (9 lignes)

| # | Texte | Durée | Segment |
|---|---|---:|---|
| N0 | Valider une production dans FoodEatUp ? C'est en trois étapes. | 3,16 s | carte intro |
| N1 | Dans Mes productions, repérez la production prête et cliquez sur Valider la production. | 4,86 s | A + clic B |
| N2 | Première étape : saisissez la quantité réellement produite. L'efficacité se calcule toute seule. | 5,93 s | C |
| N3 | Deuxième étape : le contrôle HACCP. Température, qualité, hygiène, et vos notes de production. | 6,95 s | D |
| N4 | Vérifiez le récapitulatif, puis confirmez et validez. | 3,11 s | E + clic F |
| N5 | Le stock se met à jour tout seul, et la production part en historique HACCP. | 4,91 s | G (bénéfice) |
| N6 | Vous pouvez aussi le faire depuis Claude : copiez ce prompt, remplacez les crochets. | 4,41 s | étages 1+2 (réutilisé) |
| N7 | Collez-le dans la conversation : votre production est validée en quelques secondes. | 4,21 s | étage 3 |
| N8 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | 5,02 s | carte de fin (CTA, réutilisé) |

N6/N8 réutilisés depuis `foodeatup-tva-tuto/vo/` (lignes génériques). N7 régénéré —
il nomme l'objet validé, il n'est jamais réutilisable tel quel.

N0, N4 et N5 ont été régénérés en version courte après mesure : les premières prises
(5,09 / 6,95 / 6,40 s) faisaient déborder la narration d'environ 6 s sur le budget
visuel du rush (32 s seulement), ce qui aurait décalé chaque ligne d'un segment.

## Découpage

| Seg | Source | Sortie | Contenu |
|---|---|---:|---|
| intro | carte | 3,00 s | VALIDER SA PRODUCTION QUANTITÉ & TEMP |
| A | 0,00 → 5,50 | 5,00 s | page Mes productions : KPI (529 / 81 / 117 / 200), cartes de production |
| B | 5,55 → 5,95 | 0,90 s | **zoom-punch** sur Valider la production (1592, 504) |
| C | 5,95 → 11,95 | 6,60 s | étape 1 Quantités : 19 planifiées → 30 produites, efficacité 157,9 % |
| D | 12,15 → 19,95 | 7,60 s | étape 2 Contrôle HACCP : température, qualité OK, hygiène Conforme, note « fragile » |
| E | 20,05 → 23,40 | 3,60 s | étape 3 Confirmation : récapitulatif + encart stock/historique HACCP |
| F | 23,10 → 23,50 | 0,90 s | **zoom-punch** sur Confirmer et valider (1216, 646) |
| G | 26,40 → 32,15 | 5,60 s | liste rafraîchie : Prêts à produire 117→116, Réalisés 200→201, carte PD en Réalisé |
| claude1 | carte générée | 3,00 s | reveal — prompt en gros, fond crème |
| claude2 | carte générée | 2,30 s | confirmation « Copié dans le presse-papiers ! » |
| claude3 | carte générée | 5,30 s | mockup chatbot Claude |
| outro | carte | 6,20 s | CTA |

Les 2,6 s de spinner « Validation… » (23,8 → 26,4) sont coupées : rien à montrer.
Facteurs de vitesse tous proches de 1 (0,91 → 1,10) hors zoom-punch — le rush est
court et dense, il n'a pas besoin d'accélération.

Offsets VO réels : N0 0,35 · N1 3,73 · N2 8,81 · N3 14,96 · N4 22,13 · N5 25,93 ·
N6 31,20 · N7 36,01 · N8 41,15 — chaque ligne tient dans le segment qu'elle commente
(dérive max 0,76 s sur N1, qui se termine juste après le zoom-punch qu'elle annonce).

## Séquence Claude — module partagé

Un seul outil couvre tout l'assistant en 3 étapes montré à l'écran :
`validate_production(establishment_id, production_id, produced_quantity,
temperature_log, notes)`. Prompt :

> Valide la production [nom de la production] pour mon établissement FoodEatUp
> (ID [ID établissement]) : quantité réellement produite [nombre] portions,
> température de contrôle [température] degrés, note [votre remarque].

« degrés » plutôt que le symbole °C dans le prompt vidéo pour rester lisible en
gros corps ; même texte côté fiche Lovable (`claudePrompt`).

## Animations

Mêmes principes que toute la série : Ken Burns sur les cartes, xfade 0,28 s
(`slideleft` entre les étapes du wizard et entre les 3 étages Claude, `fade`
partout ailleurs), bandeaux d'étape numérotés, encadré orange pulsant sur les
2 clics. Aucun texte de bandeau ne contient d'apostrophe (piège `drawtext`).

## Statut publication

Publiée sur le site Lovable *FoodEatUp Academy* (module `haccp`,
slug `valider-une-production`) à la demande de Michael. Pas de programmation
LinkedIn sur cette vidéo (non demandée).
