# Boucle 08 — Comptabilité

Slug : `boucle-08-comptabilite` · Durée cible 80 s · Agent : PrédiBot.

## Voix off (verbatim — ne pas réécrire)

Votre comptable vous rend les chiffres du mois en cours. Le quinze du mois suivant.
À ce moment-là, vous ne pilotez plus : vous constatez.

"Où part mon argent ce mois-ci ?"

Le mois n'est pas fini, et la réponse est déjà là. Parce que chaque service, chaque
commande fournisseur, chaque heure pointée est déjà un chiffre.

Première chose que FoodEatUp vérifie : vos taux de TVA sont-ils tenus ? Un encaissement
rangé sous le mauvais taux, et toute la déclaration part de travers — mieux vaut le voir
maintenant qu'en avril.

Ensuite il regarde ce qui se joue vraiment : les factures fournisseurs impayées qui
courent, les devis acceptés qui n'ont jamais été facturés, la masse salariale rapportée
au chiffre d'affaires — la seule ligne qui décide de la fin du mois.

"Prépare l'export du mois pour mon comptable." Les écritures sont rassemblées, les
écarts de caisse signalés. Le dossier attend votre relecture.

Un chiffre en retard ne se corrige pas. Il se subit.

## Squelette 7 plans

| # | Rôle |
|---|------|
| 1 | Le problème : les chiffres du mois arrivent le 15 du mois suivant → on ne pilote plus, on constate. Calendrier avec le décalage matérialisé. |
| 2 | La phrase à l'agent : « Où part mon argent ce mois-ci ? » |
| 3 | (le plus long) Cascade : Service encaissé → Écriture TVA → Facture fournisseur → Heures pointées → Charge du mois → Marge réelle → Décision. Ouvre sur un contrôle TVA : un encaissement mal ventilé (5,5 % vs 20 %) fait dérailler toute la déclaration. |
| 4 | Factures fournisseurs impayées qui courent, devis acceptés jamais facturés (argent laissé sur la table), masse salariale / CA. |
| 5 | « Prépare l'export du mois pour mon comptable. » Écritures rassemblées, écarts de caisse signalés, dossier en attente de relecture. |
| 6 | Boucles voisines : la comptabilité est alimentée par les sept autres (toutes s'allument, seule Comptabilité reste allumée). |
| 7 | « Un chiffre en retard ne se corrige pas. Il se subit. » Preuve : 19 outils MCP. |

## Assets à réutiliser

- Pas de nouveau visuel RapidoCMS (aucun plat en scène — sujet purement chiffré).
- `mascots/agent-laptop-homme.png` pour PrédiBot (plans 2 et 5).

## Statut
`rendu` — VO ElevenLabs (56,03 s), vidéo 62,83 s.
`out/boucle-08-comptabilite.mp4`, composition `studio-video/compositions/boucle-08-comptabilite.html`.
