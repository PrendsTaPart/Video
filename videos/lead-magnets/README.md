# 30 formations à débloquer (lead magnets)

Une formation par épisode (1 à 30) de « Mon quotidien d'entrepreneur avec l'IA » : promesse, public, outils (liens), étapes, prompts à copier, garde-fous et **ce qui est réellement en place** (repris des audits de chaque épisode, sans chiffre inventé).

| Élément | Où |
|---|---|
| Contenu source | `formations.json` (généré par `formations_part1-4.py`) |
| Couvertures 1600×900 | `couvertures/` : illustrations générées par Lovable (sans visage ni logo) + vrai portrait + titre |
| Illustrations brutes | `illustrations/` |
| PDF A4 (4-5 pages) | `pdf/formation-NN.pdf` |
| Gabarit PDF et couverture | `gabarit/` (HTML rendu par Playwright : `node render.js cover|pdf 1 2 …`) |
| Site | dépôt `PrendsTaPart/michael-au-quotidien` : `/formations`, `/formations/<slug>`, `/coaching` |

Chaque PDF se termine par l'offre « 1er mois offert » du logiciel lié (activation sur demande, conditions confirmées par écrit) et l'accompagnement one-to-one **sur devis** (configuration Claude / ChatGPT, MCP, orchestration agentique).

Note : le PDF est conçu en HTML/CSS (charte BraindCode / FoodEatUp) et rendu par Chromium ; il n'est pas exporté de Figma.
