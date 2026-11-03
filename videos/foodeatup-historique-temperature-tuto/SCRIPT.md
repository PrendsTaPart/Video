# Tutoriel — Retrouver l'historique de mes relevés de température

Module **Stocks & HACCP**. Durée livrée : **32,68 s** — H.264/yuv420p, AAC 48 kHz
stéréo, faststart. Pas d'avatar : voix off ElevenLabs de bout en bout (Adam -
Instructor, `TGAegA0zNRi8I6nUdq3i`, même voix que le reste de la série
FoodEatUp).

Rush fourni par Michael (`assets/screen.mp4`, 1920x828, 24,44 s) : Production
> Températures (relevés du jour) -> Historique (4 modules HACCP) ->
Historique > Températures (dashboard, filtres, Équipements/Plats, export
CSV). Le rush se termine par une notification d'extension navigateur (McAfee
WebAdvisor) déclenchée par le téléchargement du CSV — hors-sujet produit,
coupée : le montage s'arrête à 19,8 s de rush (sur 24,44 s disponibles).

## Voix off (9 lignes)

| # | Texte | Durée | Segment |
|---|---|---:|---|
| N1 | Retrouvez vos relevés du jour, équipement par équipement. | 3,06 s | A |
| N2 | Ouvrez Historique HACCP. | 1,99 s | B |
| N3 | Conformes et alertes, pour vos équipements et vos plats. | 3,16 s | C |
| N4 | Basculez entre Équipements et Plats. | 1,93 s | D |
| N5 | Filtrez par statut, équipement ou période. | 2,40 s | E |
| N6 | Exportez en CSV. | 1,44 s | F |
| claude_reveal | Vous pouvez aussi le faire depuis Claude : copiez ce prompt, remplacez les crochets. | 4,41 s | claude1 (réutilisée depuis `foodeatup-vitrine-tuto/vo/N6.mp3`) |
| claude_result | Collez-le dans la conversation : votre historique de températures arrive aussitôt. | 4,21 s | claude3 |
| outro_cta | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | 5,02 s | carte de fin (réutilisée depuis `foodeatup-vitrine-tuto/vo/N8.mp3`) |

Première passe de VO trop longue pour des segments d'écran aussi courts
(dérive jusqu'à 25 s, vidéo finale à 52 s) — réécrite en lignes courtes
(2-3 s) alignées sur le temps d'écran réellement disponible par état, comme
le reste de la série.

## Découpage

| Seg | Source | Sortie | Contenu |
|---|---|---:|---|
| intro | carte (fournie par Michael) | 2,60 s | RETROUVER MES RELEVÉS HISTORIQUE |
| A | 0,00 → 4,00 | 3,00 s | Production > Températures, relevés du jour |
| B | 6,50 → 8,50 | 2,30 s | Historique HACCP : 4 modules (Températures, Traçabilité, Nettoyage, Production) |
| C | 10,50 → 13,00 | 3,00 s | Historique > Températures : dashboard (total, conformes, alertes, non conformes) |
| D | 14,00 → 16,00 | 2,00 s | Bascule Équipements / Plats |
| E | 16,00 → 19,30 | 3,00 s | Filtres statut + date |
| F | 19,30 → 19,80 | 1,00 s (ralenti) | Clic Exporter CSV |
| claude1 | carte générée | 4,60 s | reveal — prompt en gros, fond crème |
| claude2 | carte générée | 1,40 s | confirmation « Copié dans le presse-papiers ! » |
| claude3 | carte générée | 4,40 s | mockup chatbot Claude |
| outro | carte (fournie par Michael) | 8,09 s (auto-étendue) | CTA |

## Séquence Claude — module HACCP

Outil correspondant exactement à ce que montre le rush :
`list_haccp_temperatures(establishment_id, equipment_id?, type?, start_date?,
end_date?)` — filtre l'historique par équipement et par période, comme les
filtres visibles à l'écran (segment E).

> Liste mes relevés de température HACCP pour l'équipement [nom de
> l'équipement] entre le [date de début] et le [date de fin], pour mon
> établissement FoodEatUp (ID [ID établissement]).

Même texte côté fiche Lovable (`claudePrompts`).

## Animations

Mêmes principes que toute la série : setpts pour la vitesse (jamais zoompan
sur du rush réel), xfade (0,28 s) sur chaque coupe, bandeaux d'étape sans
apostrophe (bug connu sur `foodeatup-ingredients-tuto`). Pas de punch-zoom
sur cette vidéo (rush trop court par état pour l'accueillir proprement).

## Statut publication

Assets intro/outro et rush fournis par Michael, déjà dans la charte
FoodEatUp standard. Vidéo livrée pour validation avant publication
RapidoCMS/LinkedIn (Lovable mis à jour directement, cf. demande explicite).
