# Tutoriel — Retrouver les pointages (historique) FoodEatUp

Module Équipe & Planning, dossier Drive « 12-Historique des pointage des
employés ». Durée livrée : **33,36 s** — H.264 High/yuv420p, AAC 48 kHz
stéréo, faststart. Audio : true peak **-7,26 dBFS**. Sans avatar HeyGen.
Rush très court (18,64 s) — vidéo proportionnellement plus courte que le
reste de la série.

## Voix off (6 lignes)

| # | Texte | Durée | Segment |
|---|---|---:|---|
| N1 | Consultez l'historique de pointage de votre équipe sur la période de votre choix. | 4,21 s | A |
| N2 | Cliquez sur Exporter PDF pour obtenir un rapport imprimable de tous les pointages. | 4,62 s | A2 (zoom-punch) |
| N3 | Un suivi complet des heures d'arrivée, pauses et heures de sortie, prêt pour votre comptabilité. | 5,69 s | B |
| N4 | Vous pouvez aussi demander ça à Claude : copiez ce prompt, remplacez les crochets. | 4,36 s | étages 1+2 |
| N5 | Collez-le dans la conversation : votre dashboard de pointages est prêt en quelques secondes. | 4,68 s | étage 3 |
| N6 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | 5,02 s | carte de fin (réutilisée) |

## Découpage

| Seg | Source | Sortie | Contenu |
|---|---|---:|---|
| intro | carte | 2,50 s | RETROUVER LES POINTAGES HISTORIQUE |
| A | 0,00 → 8,00 | 4,70 s | Table Pointage (employé/date/heures/pauses/temps total/statut), sélecteur de période |
| A2 | 8,00 → 10,00 | 5,10 s | **zoom-punch** sur « Exporter PDF » (1262, 284) |
| B | 11,00 → 18,64 | 6,20 s | Visionneuse PDF : rapport « Historique des Pointages » exporté |
| claude1 | carte générée | 3,00 s | reveal — prompt en gros, fond crème |
| claude2 | carte générée | 2,30 s | confirmation « Copié dans le presse-papiers ! » |
| claude3 | carte générée | 5,30 s | mockup chatbot Claude |
| outro | carte | 6,20 s | CTA |

## Séquence Claude — module partagé

Correspond exactement à `list_attendances(establishment_id, date_from,
date_to)` — la table filtrée par période affichée à l'écran.

> Fais-moi un dashboard des pointages de mon équipe du [date début] au
> [date fin] pour mon établissement FoodEatUp (ID [ID établissement]).

Même texte côté fiche Lovable (`claudePrompt`), + prompts de cas d'usage
supplémentaires demandés par Michael (détection d'anomalies, comparaison aux
horaires prévus) en `claudePrompts[]` — tous basés sur le même outil
`list_attendances`, avec des questions d'analyse différentes.

## Animations

Mêmes principes que toute la série : Ken Burns sur les cartes, xfade
(0,28 s), bandeaux d'étape (slide-in seul), encadré orange pulsant sur le
clic Exporter PDF.

## Statut publication

Vidéo à livrer à Michael pour validation avant publication RapidoCMS/
LinkedIn/Lovable. RapidoCMS non autorisé dans cette session — publication
CMS/LinkedIn en attente dans tous les cas.
