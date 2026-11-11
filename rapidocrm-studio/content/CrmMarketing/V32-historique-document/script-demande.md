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

À quoi ça sert : Retrouver les fichiers attachés à un client — leur nom, leur type, leur poids, leur date d'ajout — et les télécharger ou les supprimer depuis la même ligne.
Pour qui : Gérant ou commercial qui gère les pièces jointes d'un client
Prompt Claude : Donne-moi la fiche complète de l'entreprise numéro [identifiant].

Étapes observées :
- 1. Ouvrir l'historique des documents — fenêtre 7.5s, soit ~18 mots
- 2. Lire le tableau des documents — fenêtre 5.5s, soit ~13 mots
- 3. Télécharger ou supprimer un document — fenêtre 3.5s, soit ~8 mots
- 4. Annuler et revenir à la liste — fenêtre 1.7s, soit ~4 mots

Astuces : Le poids est affiché · Deux actions, un seul menu · La confirmation vient du navigateur
Erreurs fréquentes : Prendre le message de liste vide pour une absence de documents : il s'affiche aussi le temps du chargement. · Valider la confirmation de suppression trop vite : c'est le navigateur qui la pose, et elle est en anglais.

## SEO

`seo.titre` ≤ 60 caractères · `seo.description` entre 120 et 155 caractères ·
`seo.youtube_titre` ≤ 70 caractères, au format « <Titre> — RapidoCRM ».

Schéma : `src/schema/index.ts` → `ScriptSchema`.
