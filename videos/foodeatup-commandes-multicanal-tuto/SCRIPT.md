# Tutoriel — Retrouver ses commandes multi-canal

Module Service Multi-Canal. Durée livrée : **61,80 s** — H.264 High/yuv420p, AAC 48 kHz
stéréo, faststart. Audio : true peak **-7,2 dBFS**.

Rush fourni par Michael : `assets/screen.mp4` (30,88 s,
1920x828 @25fps), cartes intro/outro fournies (`assets/intro.jpg` = COMMANDES_MULTICANAUX,
`assets/outro.jpg` = CTA "Passez à la restauration intelligente").

Le rush montre le widget "Commandes" du tableau de bord (recherche, filtres Aujourd'hui/
7 jours/Tout, pastilles de statut, pastille de canal "Web · 3") -> clic sur une commande
pour ouvrir sa fiche détaillée (canal, statut, paiement, mode de service, articles, totaux,
client, notes) -> fermeture -> bouton "Ouvrir la gestion complète" -> page "Mes commandes"
complète avec recherche + filtres Statut/Canal/Date et ses stats (total commandes, en
attente, aujourd'hui, chiffre d'affaires).

## Voix off (10 lignes)

| # | Texte | Ancrage |
|---|---|---|
| N0 | Retrouver une commande, peu importe son canal, ça prend deux secondes sur FoodEatUp. | carte d'intro |
| N1 | Le tableau Commandes affiche tout d'un coup d'œil : le statut, le canal — vitrine, agent vocal, sur place — et vos filtres Aujourd'hui, 7 jours ou Tout. | widget board |
| N2 | Cliquez sur une commande pour ouvrir sa fiche complète. | clic sur la carte |
| N3 | Canal, statut, paiement, mode de service, articles et totaux : tout est là, avec les coordonnées du client. | scroll fiche détail |
| N4 | Pour aller plus loin, ouvrez la gestion complète des commandes. | fermeture + reveal bouton |
| N5 | Là, recherchez par numéro, client ou téléphone, et filtrez par statut, par canal ou par date. | clic + filtres page complète |
| N6 | Vous avez une vue d'ensemble totale : total des commandes, celles en attente, et le chiffre d'affaires du jour, tous canaux confondus. | stats + tableau |
| N7 | Vous pouvez aussi les retrouver depuis Claude : copiez ce prompt, remplacez les crochets. | étage 1+2 Claude |
| N8 | Collez-le dans la conversation : vos commandes du canal choisi s'affichent en quelques secondes. | étage 3 Claude |
| N9 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | carte de fin (CTA) — réutilisée telle quelle depuis `foodeatup-mes-commandes-tuto/vo/N8.mp3` |

## Découpage (raw -> segments)

| Seg | Source (raw) | Contenu |
|---|---|---|
| intro | carte | COMMANDES MULTI-CANAUX |
| A | 0.00 → 9.00 | Widget "Commandes" : recherche, filtres période, pastilles statut, pastille canal Web·3, cartes commandes |
| C | 9.00 → 24.00 | Clic sur CMD-2026-00101 -> fiche détail (canal/statut/payée, mode/table/téléphone, articles, totaux, client, notes) |
| D | 24.00 → 26.60 | Fermeture de la fiche, scroll -> bouton "Ouvrir la gestion complète" révélé |
| E | 26.60 → 26.90 | **zoom-punch** sur "Ouvrir la gestion complète (création manuelle, export)" (948, 709), bbox mesurée par seuillage colorimétrique (636,680)-(1260,740) |
| F | 26.90 → 30.88 | Page "Mes commandes" complète : stats + recherche + filtres Statut/Canal/Date + tableau |
| claude1 | carte générée | reveal — prompt en gros, fond crème |
| claude2 | carte générée | confirmation « Copié dans le presse-papiers ! » |
| claude3 | carte générée | mockup chatbot Claude |
| outro | carte | CTA |

Pas de zoom-punch sur le clic d'ouverture de la fiche commande (t≈9 s) ni sur la fermeture
(icône "X", t≈24 s) : coordonnées non mesurables avec certitude par seuillage colorimétrique
sur ces deux clics précis (icône fine / zone de carte large) — conformément à la règle du
pipeline de ne jamais deviner une coordonnée à l'œil. Seul le bouton "Ouvrir la gestion
complète" a une bbox mesurée nette (couleur bleu marque uniforme).

## Séquence Claude — module partagé

`mcp__FoodEatUp__list_orders(establishment_id, channel, status, date, limit)` existe et
correspond exactement aux filtres Statut/Canal/Date affichés sur la page "Mes commandes"
(schéma vérifié avant rédaction du prompt). Pas de paramètre de recherche libre par
numéro/client/téléphone côté MCP -> non repris dans le `claudePrompt`.

> Montre-moi mes commandes [du jour / des 7 derniers jours], canal [manuel / telephone /
> vitrine / agent_vocal / sur_place / facture / devis], statut [en_attente / confirmee /
> en_preparation / prete / livree / annulee], pour mon établissement FoodEatUp (ID [ID
> établissement]).

Même texte côté fiche Lovable (`claudePrompt`).

## Animations

Mêmes principes que toute la série : Ken Burns sur les cartes, xfade (0,28 s), bandeaux
d'étape (rendus en PNG via PIL + `overlay`, jamais `drawbox` animé sur `t`), encadré orange
pulsant sur le seul clic mesuré (E). Pas de clip avatar dans ce dossier.

## Statut publication

Nouveau tutoriel du module `service-commande` (Service Multi-Canal), en complément de
`mes-commandes-tous-canaux` (déjà publié, axé création/modification/suppression) : celui-ci
couvre l'angle recherche/filtrage/consultation ("retrouver"), demandé explicitement par
Michael avec la carte intro/outro et le rush "Retrouver vos commandes multiCanal".
