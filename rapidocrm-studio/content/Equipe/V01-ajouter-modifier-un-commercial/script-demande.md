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
- **Durée cible 90 à 150 s.** Si ça dépasse, on coupe dans la démo — jamais dans
  le hook ni dans la punchline.

## Matière disponible

À quoi ça sert : Créer la fiche d'un membre de l'équipe commerciale : son identité, ses coordonnées, sa photo, et les objectifs mensuels sur lesquels il sera suivi. C'est cette fiche qui lui ouvre un accès au logiciel et qui alimente ensuite son suivi de performance.
Pour qui : Gérant ou administrateur qui constitue son équipe commerciale
Prompt Claude : Liste-moi mes commerciaux avec leur statut et leurs objectifs, les [nombre] premiers.

Étapes observées :
- 1. Ouvrir la page Commerciaux — fenêtre 5.0s, soit ~12 mots
- 2. Ouvrir le formulaire — fenêtre 7.0s, soit ~17 mots
- 3. Nommer le commercial et sa fonction — fenêtre 12.0s, soit ~30 mots
- 4. Renseigner ses coordonnées — fenêtre 14.0s, soit ~35 mots
- 5. Ajouter sa photo — fenêtre 9.0s, soit ~22 mots
- 6. Fixer ses objectifs mensuels — fenêtre 7.8s, soit ~19 mots
- 7. Lire l'avertissement d'activation — fenêtre 10.6s, soit ~26 mots

Astuces : Le mail d'activation dépend de votre boîte mail · Quatre compteurs, pas un de plus · La photo n'est pas décorative
Erreurs fréquentes : Créer le commercial sans avoir branché la boîte mail de la société : le compte est bien créé, mais le mail d'activation ne part pas. · Laisser les objectifs mensuels vides, et se retrouver avec une fiche de suivi qui n'affiche rien à mesurer.

## SEO

`seo.titre` ≤ 60 caractères · `seo.description` entre 120 et 155 caractères ·
`seo.youtube_titre` ≤ 70 caractères, au format « <Titre> — RapidoCRM ».

Schéma : `src/schema/index.ts` → `ScriptSchema`.
