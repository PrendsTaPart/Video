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

À quoi ça sert : Retrouver les messages courts envoyés à un client, avec leur date et leur contenu exact. Ce qui a été dit par SMS reste écrit quelque part.
Pour qui : Gérant ou commercial qui vérifie une relance
Prompt Claude : Donne-moi les statistiques d'interactions du mois pour l'entreprise numéro [identifiant].

Étapes observées :
- 1. Ouvrir l'historique des SMS — fenêtre 6.0s, soit ~15 mots
- 2. Lire le tableau des envois — fenêtre 3.5s, soit ~8 mots
- 3. Rouvrir un SMS envoyé — fenêtre 3.0s, soit ~7 mots
- 4. Revenir à la liste — fenêtre 1.2s, soit ~2 mots

Astuces : Le numéro est une colonne · Fermer, pas supprimer · Un champ de recherche au-dessus
Erreurs fréquentes : Chercher le contenu dans le tableau : il n'apparaît qu'en ouvrant la ligne. · Confondre le journal des SMS et celui des e-mails : ce sont deux cartes distinctes de l'historique.

## SEO

`seo.titre` ≤ 60 caractères · `seo.description` entre 120 et 155 caractères ·
`seo.youtube_titre` ≤ 70 caractères, au format « <Titre> — RapidoCRM ».

Schéma : `src/schema/index.ts` → `ScriptSchema`.
