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

À quoi ça sert : Mettre une vraie première page devant un contrat, choisie dans une galerie, sans ouvrir d'éditeur. Le contrat s'ouvre ensuite sur cette page au lieu de commencer sec sur l'article 1.
Pour qui : Gérant ou commercial qui envoie ses contrats lui-même
Prompt Claude : Liste-moi mes [nombre] templates de contrat avec leur titre.

Étapes observées :
- 1. Ouvrir la liste des templates de contrat — fenêtre 4.3s, soit ~10 mots
- 2. Ouvrir le choix de la couverture — fenêtre 4.7s, soit ~11 mots
- 3. Choisir la couverture et confirmer — fenêtre 6.0s, soit ~15 mots
- 4. Voir la couverture en tête du contrat — fenêtre 6.5s, soit ~16 mots

Astuces : La galerie tient sur deux pages · « Aucun » est un choix, pas un vide · Le marketplace prolonge la galerie
Erreurs fréquentes : Fermer la fenêtre par la croix sans cliquer sur confirmer : la couverture n'est pas enregistrée. · Chercher la couverture dans l'éditeur de contrat : elle se choisit depuis la liste des templates, par le bouton plus de la ligne.

## SEO

`seo.titre` ≤ 60 caractères · `seo.description` entre 120 et 155 caractères ·
`seo.youtube_titre` ≤ 70 caractères, au format « <Titre> — RapidoCRM ».

Schéma : `src/schema/index.ts` → `ScriptSchema`.
