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

À quoi ça sert : Savoir où en sont vos contrats — combien sont partis, combien sont signés, combien attendent — et rouvrir n'importe lequel d'entre eux tel qu'il a été envoyé au client.
Pour qui : Gérant ou commercial qui suit ses contrats en cours
Prompt Claude : Liste-moi mes contrats au statut [statut] avec leur entreprise et leur date de création.

Étapes observées :
- 1. Lire les trois compteurs de contrats — fenêtre 3.5s, soit ~8 mots
- 2. Retrouver un contrat dans l'historique — fenêtre 2.5s, soit ~6 mots
- 3. Ouvrir le contrat généré — fenêtre 8.0s, soit ~20 mots
- 4. Revenir à la liste — fenêtre 2.2s, soit ~5 mots

Astuces : Trois compteurs, trois états · La recherche porte sur le fichier · Le contrat garde ses pages de signature
Erreurs fréquentes : Oublier de cliquer sur appliquer après avoir choisi un filtre : le tableau ne bouge pas tant que le filtre n'est pas appliqué. · Laisser un filtre posé et croire que l'historique est vide : le bouton annuler remet la liste complète.

## SEO

`seo.titre` ≤ 60 caractères · `seo.description` entre 120 et 155 caractères ·
`seo.youtube_titre` ≤ 70 caractères, au format « <Titre> — RapidoCRM ».

Schéma : `src/schema/index.ts` → `ScriptSchema`.
