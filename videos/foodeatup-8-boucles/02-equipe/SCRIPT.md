# Boucle 02 — Équipe

Slug : `boucle-02-equipe` · Durée cible 80 s · Agent : PrédiBot.

## Voix off (verbatim — ne pas réécrire)

Le mardi, vous êtes trois en salle pour douze couverts. Le samedi, vous êtes trois
aussi — pour soixante. Personne n'a jamais regardé l'historique. On fait comme
d'habitude.

Alors vous demandez : "Qui bosse samedi soir ?"

FoodEatUp ne lit pas un tableau blanc. Il croise. Le planning de la semaine. Les
contrats en cours. Les pointages réels, pas les horaires prévus. Et surtout, les
réservations déjà prises pour samedi.

Là, il voit le trou : soixante couverts attendus, deux personnes en cuisine. Il vous
propose un shift de plus, et il vous montre ce qu'il coûte. Vous validez, ou pas.

"Valide le congé de Sarah pour la semaine du douze." Le congé passe, le planning se met
à jour, l'équipe est prévenue.

Et le coût du travail — vingt-cinq à trente-cinq pour cent de votre chiffre d'affaires
— remonte tout seul dans votre comptabilité.

Résultat : un planning fait en dix minutes, sur l'activité réelle.

Si cette boucle est coupée : sur-effectif le mardi, sous-effectif le samedi.
Systématiquement.

## Squelette 7 plans (~80 s)

| # | s | Rôle |
|---|---|------|
| 1 | 0–10 | Le problème, tel quel, sans logo : mardi 3 en salle / 12 couverts, samedi 3 en salle / 60 couverts. |
| 2 | 10–22 | La phrase dite à l'agent, en gros : « Qui bosse samedi soir ? » |
| 3 | 22–42 (le plus long) | Cascade : Recrutement → Contrat → Planning → Pointage réel → Congés → Coût constaté → Écart prévu/réel → Planning suivant. Superposer la courbe des couverts par créneau : c'est elle qui déforme le planning sous les yeux du spectateur. |
| 4 | 42–56 | Alerte « Samedi 20h — 60 couverts attendus, 2 en cuisine ». Proposition de shift + coût affiché. Bouton Valider. Mention à l'écran : contrat, planning contractuel et suppression d'employé exigent une confirmation humaine. |
| 5 | 56–68 | Boucles voisines qui s'allument dans le ∞ : Comptabilité. |
| 6 | 68–80 | Chiffres : planning fait en 10 min · coût du travail par service vs CA. |
| 7 | 80–85 (buffer jusqu'à ~80s réel) | « Sur-effectif le mardi, sous-effectif le samedi. Systématiquement. » Preuve : 18 outils MCP. |

## Assets à réutiliser (studio-video/assets/brand/)

- `mascots/agent-rh.png` — agent PrédiBot / RH pour les plans 2, 4, 7.
- `product-screenshots/rh-dashboard-conges-pointage.png` — plan 1 (le problème)
  et/ou plan 3 (pointage réel).
- `logo-v2/foodeatup-mark-8.png` — vignette (logo, pas une frame extraite).
- `profile/michael-chef-mascot.jpg` — optionnel si un plan bénéficie d'une
  présence humaine de marque.

## Statut
`script` (VO figée, pas encore générée en audio — préflight coût en attente
de confirmation avant l'appel ElevenLabs).
