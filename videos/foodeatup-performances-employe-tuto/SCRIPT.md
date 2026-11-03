# Tutoriel — Suivre ses performances (côté employé) FoodEatUp

Module Équipe & Planning, dossier Drive « 18-Affichages des performances de
l'employé » — fichier vérifié via `mcp__Google_Drive__search_files` (taille
identique, 8 619 599 octets) : pas de mélange de dossier cette fois. Durée
livrée : **46,40 s** — H.264 High/yuv420p, AAC 48 kHz stéréo, faststart.
Audio : max -6,5 dBFS. Sans avatar HeyGen.

Rush très court (18,42 s), capturé avec le chrome du navigateur visible
(onglets/barre d'adresse) — recadré en amont (`crop=1920:828:0:191`) pour
retrouver le cadrage 1920×828 standard de la série, sans bordure navigateur.

## Voix off (7 lignes)

| # | Texte | Durée | Segment |
|---|---|---:|---|
| N1 | Chaque employé retrouve son planning personnel dès sa connexion à FoodEatUp. | 4,41 s | A |
| N2 | Depuis le menu de son profil, il ouvre l'onglet Performances. | 3,11 s | A2 (zoom-punch) |
| N3 | Il y retrouve son score global, son statut — Excellent, Moyen ou À améliorer — et le détail de ses horaires jour par jour. | 7,78 s | B |
| N4 | Le classement de l'équipe et l'historique des performances semaine par semaine donnent une vision claire de sa progression. | 5,93 s | C |
| N5 | En tant que directeur, demandez directement à Claude un dashboard de performance de toute votre équipe : copiez ce prompt, remplacez les crochets. | 7,60 s | étages 1+2 |
| N6 | Collez-le dans la conversation : assiduité, heures travaillées et classement de l'équipe s'affichent en quelques secondes. | 6,45 s | étage 3 |
| N7 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | 5,02 s | carte de fin (réutilisée) |

## Découpage

| Seg | Source | Sortie | Contenu |
|---|---|---:|---|
| intro | carte | 2,50 s | SUIVRE SES PERFORMANCES CÔTÉ EMPLOYÉ |
| A | 0,00 → 3,00 | 5,00 s | « Mon planning » — vue employé (Soulayma Abdenbi) |
| A2 | 3,40 → 4,30 | 4,00 s | **zoom-punch** sur « Performances » dans le menu profil |
| B | 7,00 → 8,30 | 8,50 s | Score circulaire (131, « À améliorer »), légende Excellent/Moyen/À améliorer, 4 cartes date/heures |
| C | 9,00 → 13,00 | 7,00 s | Classement de l'équipe (SA/AN/PB, scores) + badge Rang 1/15 + historique hebdomadaire (graphique) |
| claude1 | carte générée | 4,00 s | reveal — prompt en gros, fond crème |
| claude2 | carte générée | 4,20 s | confirmation « Copié dans le presse-papiers ! » |
| claude3 | carte générée | 7,20 s | mockup chatbot Claude |
| outro | carte | 6,20 s | CTA |

## Séquence Claude — module partagé

Aucun outil MCP ne calcule le score de performance FoodEatUp lui-même
(algorithme interne : heures, ponctualité, tâches). En revanche, un
directeur peut demander à Claude un vrai dashboard d'équipe à partir des
données de pointage réelles via
`list_attendances(establishment_id, date_from, date_to)` — même outil que
`retrouver-les-pointages-historique` et `creer-ses-roles-et-permissions`,
demandé explicitement par Michael pour cette vidéo.

> Fais-moi un dashboard de performance de mon équipe (heures travaillées,
> ponctualité) pour la semaine du [date début] au [date fin], pour mon
> établissement FoodEatUp (ID [ID établissement]).

Prompts de cas d'usage supplémentaires prévus pour la fiche Lovable
(`claudePrompts[]`), tous basés sur le même outil :
- Comparer les heures travaillées d'un employé à son planning prévu sur
  plusieurs semaines.
- Identifier les employés les plus assidus (moins de retards) sur une
  période donnée.

## Animations

Mêmes principes que toute la série : Ken Burns sur les cartes, xfade
(0,28 s), bandeaux d'étape (module `banner()` corrigé — slide-in seul),
encadré orange pulsant en zoom-punch sur l'item de menu « Performances ».

## Statut publication

Vidéo à livrer à Michael pour validation avant publication RapidoCMS/
LinkedIn/Lovable. RapidoCMS non autorisé dans cette session — publication
CMS/LinkedIn en attente dans tous les cas.
