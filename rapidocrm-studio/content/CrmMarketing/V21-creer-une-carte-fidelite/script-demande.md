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

À quoi ça sert : Doter son enseigne d'une carte de fidélité en trois écrans : une taille, un modèle, une relecture. La carte rejoint ensuite les programmes de fidélité, avec ses clients et ses points.
Pour qui : Gérant qui lance un programme de fidélité
Prompt Claude : Liste-moi mes programmes de fidélité avec leur nombre de clients et de points offerts.

Étapes observées :
- 1. Ouvrir l'assistant de carte de fidélité — fenêtre 6.0s, soit ~15 mots
- 2. Choisir la taille de la carte — fenêtre 5.0s, soit ~12 mots
- 3. Choisir le modèle de carte — fenêtre 4.0s, soit ~10 mots
- 4. Relire le récapitulatif et enregistrer — fenêtre 4.7s, soit ~11 mots
- 5. Retrouver la carte dans les programmes de fidélité — fenêtre 5.1s, soit ~12 mots

Astuces : Trois étapes, affichées en haut · Les dimensions sont écrites sur chaque carte · La page d'arrivée chiffre le programme
Erreurs fréquentes : Chercher un bouton Terminer : c'est Enregistrer, en bas à droite du récapitulatif, qui crée la carte. · Croire qu'un choix est définitif : chaque ligne du récapitulatif porte un bouton Modifier.

## SEO

`seo.titre` ≤ 60 caractères · `seo.description` entre 120 et 155 caractères ·
`seo.youtube_titre` ≤ 70 caractères, au format « <Titre> — RapidoCRM ».

Schéma : `src/schema/index.ts` → `ScriptSchema`.
