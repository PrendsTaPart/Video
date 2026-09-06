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

À quoi ça sert : Savoir ce qui a été écrit à un client, et quand. Le journal liste les envois, et chaque ligne se rouvre pour relire l'e-mail tel qu'il est parti.
Pour qui : Gérant ou commercial qui vérifie un échange passé
Prompt Claude : Donne-moi les statistiques d'interactions du mois pour l'entreprise numéro [identifiant].

Étapes observées :
- 1. Ouvrir l'historique des e-mails — fenêtre 6.5s, soit ~16 mots
- 2. Lire le tableau des envois — fenêtre 3.0s, soit ~7 mots
- 3. Rouvrir un e-mail envoyé — fenêtre 5.0s, soit ~12 mots
- 4. Revenir à la liste — fenêtre 0.8s, soit ~2 mots

Astuces : Une ligne par envoi · L'objet en premier · Le journal sert aussi de point de départ
Erreurs fréquentes : Confondre l'œil et la suppression : l'œil ouvre, le bouton Supprimer se trouve à l'intérieur de la fenêtre. · Chercher le journal dans la boîte mail : il vit dans l'historique de l'entreprise.

## SEO

`seo.titre` ≤ 60 caractères · `seo.description` entre 120 et 155 caractères ·
`seo.youtube_titre` ≤ 70 caractères, au format « <Titre> — RapidoCRM ».

Schéma : `src/schema/index.ts` → `ScriptSchema`.
