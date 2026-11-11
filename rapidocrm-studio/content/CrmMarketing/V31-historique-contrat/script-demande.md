# Rédaction du script

## Ton — à respecter strictement

Français, vouvoiement, phrases courtes, rythme vif. Ludique sans être puéril.
Compréhensible d'un débutant total **et** utile à un expert : le débutant suit
les étapes, l'expert apprend les astuces et le prompt Claude.
Zéro jargon non expliqué — un mot technique (segment, workflow, webhook) est
défini en cinq mots à sa première occurrence.
Jamais « il suffit de », jamais « c'est très simple » : ça culpabilise celui qui
bloque. On dit **ce que ça change** pour l'utilisateur avant de dire où cliquer.

## Fabrication

- **Hook** : une question ou un constat qui pointe la douleur — jamais une
  description de fonctionnalité. Propose **3 alternatives** dans `hook.alternatives`.
- **Punchline** : courte, imagée, tournée vers le bénéfice — jamais un slogan
  générique. Propose **3 alternatives** dans `punchline.alternatives`.
- **Débit 150 mots/minute** : la voix de chaque étape doit tenir dans sa fenêtre
  vidéo (`fin_source − debut_source`). Si la voix déborde, on **ralentit la vidéo
  source** au rendu, on n'accélère jamais la voix.
- **Durée cible 55 à 150 s.** Si ça dépasse, on coupe dans la démo — jamais dans
  le hook ni dans la punchline.

## Matière disponible

À quoi ça sert : Voir d'un coup d'œil les contrats envoyés à un client, leurs dates de validité et leur statut, puis ouvrir le document lui-même pour le relire.
Pour qui : Gérant ou commercial qui vérifie l'état d'un engagement
Prompt Claude : Liste-moi mes [nombre] contrats en attente avec leur destinataire et leurs dates.

Étapes observées :
- 1. Ouvrir l'historique des contrats — fenêtre 6.0s, soit ~15 mots
- 2. Lire le tableau des contrats — fenêtre 3.3s, soit ~8 mots
- 3. Ouvrir le contrat — fenêtre 2.4s, soit ~6 mots
- 4. Parcourir le contrat, page par page — fenêtre 5.7s, soit ~14 mots

Astuces : Le contrat s'ouvre dans un onglet · Les vignettes servent de sommaire · Un champ de recherche au-dessus du tableau
Erreurs fréquentes : Chercher un bouton « Voir » : c'est le menu à trois points de la ligne qui ouvre le contrat. · Confondre la date de début du contrat et la date de son envoi : le tableau affiche la validité.

## SEO

`seo.titre` ≤ 60 caractères · `seo.description` entre 120 et 155 caractères ·
`seo.youtube_titre` ≤ 70 caractères, au format « <Titre> — RapidoCRM ».

Schéma : `src/schema/index.ts` → `ScriptSchema`.
