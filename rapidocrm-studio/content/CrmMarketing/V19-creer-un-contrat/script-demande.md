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

À quoi ça sert : Envoyer un contrat à un client en partant d'un modèle prêt à l'emploi : on choisit le modèle, on borne les dates, on prend un modèle d'e-mail, et le contrat part.
Pour qui : Gérant ou commercial qui contractualise avec un client existant
Prompt Claude : Liste-moi mes [nombre] contrats en attente avec leur destinataire et leurs dates.

Étapes observées :
- 1. Ouvrir « Créer un contrat » depuis la fiche — fenêtre 3.5s, soit ~8 mots
- 2. Choisir un modèle dans la bibliothèque — fenêtre 5.0s, soit ~12 mots
- 3. Vérifier le destinataire du contrat — fenêtre 5.5s, soit ~13 mots
- 4. Fixer les dates de début et de fin — fenêtre 11.0s, soit ~27 mots
- 5. Choisir le modèle d'e-mail et envoyer — fenêtre 5.0s, soit ~12 mots
- 6. Lire la confirmation — fenêtre 8.0s, soit ~20 mots

Astuces : La bibliothèque dit combien de modèles existent · Un formulaire court · Le destinataire vient de la fiche
Erreurs fréquentes : Modifier le destinataire alors qu'il vient de la fiche : le contrat part à cette adresse-là. · Cliquer sur Envoyer sans avoir choisi de modèle d'e-mail : le contrat a besoin d'un message pour partir.

## SEO

`seo.titre` ≤ 60 caractères · `seo.description` entre 120 et 155 caractères ·
`seo.youtube_titre` ≤ 70 caractères, au format « <Titre> — RapidoCRM ».

Schéma : `src/schema/index.ts` → `ScriptSchema`.
