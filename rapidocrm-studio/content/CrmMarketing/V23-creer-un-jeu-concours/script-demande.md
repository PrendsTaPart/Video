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

À quoi ça sert : Animer son fichier client avec une roue, une carte à gratter ou un quiz, sans rien coder : on part d'un modèle, on change l'image et le texte, on décrit les lots.
Pour qui : Gérant ou responsable marketing qui anime ses clients
Prompt Claude : Liste-moi mes [nombre] jeux concours du mois avec leur statut.

Étapes observées :
- 1. Ouvrir les jeux depuis la fiche entreprise — fenêtre 4.0s, soit ~10 mots
- 2. Choisir un modèle de jeu — fenêtre 5.0s, soit ~12 mots
- 3. Les trois étapes de personnalisation — fenêtre 5.0s, soit ~12 mots
- 4. Régler l'apparence et voir l'aperçu — fenêtre 9.0s, soit ~22 mots
- 5. Décrire les lots à gagner — fenêtre 6.5s, soit ~16 mots
- 6. Revenir à la fiche — fenêtre 3.7s, soit ~9 mots

Astuces : Trois types de jeux · Configuration à gauche, aperçu à droite · Le bouton « Mes jeux »
Erreurs fréquentes : Chercher à créer un jeu de zéro : on part toujours d'un modèle de la bibliothèque. · Décrire les lots sans leur donner de chance de gagner : un lot sans probabilité ne sort jamais.

## SEO

`seo.titre` ≤ 60 caractères · `seo.description` entre 120 et 155 caractères ·
`seo.youtube_titre` ≤ 70 caractères, au format « <Titre> — RapidoCRM ».

Schéma : `src/schema/index.ts` → `ScriptSchema`.
