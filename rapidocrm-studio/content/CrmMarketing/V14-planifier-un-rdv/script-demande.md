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

À quoi ça sert : Poser un créneau avec un client et prévenir tout le monde d'un coup : les invités reçoivent l'invitation, les organisateurs sont nommés, et le rappel part tout seul avant l'heure.
Pour qui : Gérant ou commercial qui cale un point avec un client
Prompt Claude : Liste-moi mes [nombre] rendez-vous de la semaine avec leur date et leur statut.

Étapes observées :
- 1. Ouvrir « Prendre un rendez-vous » — fenêtre 5.0s, soit ~12 mots
- 2. Donner un titre au rendez-vous — fenêtre 10.0s, soit ~25 mots
- 3. Fixer le créneau, début et fin — fenêtre 28.0s, soit ~70 mots
- 4. Choisir les invités et les organisateurs — fenêtre 12.0s, soit ~30 mots
- 5. Type de rendez-vous, rappel et mode d'envoi — fenêtre 10.0s, soit ~25 mots
- 6. Ajouter une note et enregistrer — fenêtre 7.0s, soit ~17 mots

Astuces : Le champ propose, vous choisissez · Trois types, trois usages · La note voyage avec le rendez-vous
Erreurs fréquentes : Confondre invités et organisateurs : les invités reçoivent l'invitation, les organisateurs tiennent le rendez-vous. · Régler le rappel sans choisir de mode d'envoi : le délai est fixé, mais rien ne dit par quel canal il part.

## SEO

`seo.titre` ≤ 60 caractères · `seo.description` entre 120 et 155 caractères ·
`seo.youtube_titre` ≤ 70 caractères, au format « <Titre> — RapidoCRM ».

Schéma : `src/schema/index.ts` → `ScriptSchema`.
