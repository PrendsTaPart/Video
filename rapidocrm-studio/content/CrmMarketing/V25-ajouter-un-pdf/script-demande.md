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

À quoi ça sert : Attacher un document au client — une carte, un tarif, une fiche technique — pour le retrouver dans sa fiche plutôt que dans une boîte mail.
Pour qui : Gérant ou commercial qui range les documents d'un client
Prompt Claude : Donne-moi la fiche complète de l'entreprise numéro [identifiant].

Étapes observées :
- 1. Ouvrir « Ajouter un PDF » depuis la fiche — fenêtre 4.0s, soit ~10 mots
- 2. Nommer le document — fenêtre 6.5s, soit ~16 mots
- 3. Choisir le fichier et l'ajouter — fenêtre 5.5s, soit ~13 mots
- 4. Retrouver la fiche et ses documents — fenêtre 7.3s, soit ~18 mots

Astuces : Deux champs, pas plus · Le nom prime sur le fichier · Annuler reste possible
Erreurs fréquentes : Fermer la fenêtre après avoir choisi le fichier : c'est le bouton Ajouter qui l'attache à la fiche. · Chercher l'import dans le bloc Documentation de la page : le bouton s'appelle « Ajouter un PDF » dans le panneau de droite.

## SEO

`seo.titre` ≤ 60 caractères · `seo.description` entre 120 et 155 caractères ·
`seo.youtube_titre` ≤ 70 caractères, au format « <Titre> — RapidoCRM ».

Schéma : `src/schema/index.ts` → `ScriptSchema`.
