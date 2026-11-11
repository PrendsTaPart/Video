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

À quoi ça sert : C'est le second écran de l'inscription : celui où votre société entre dans le logiciel. Tout ce que vous saisirez ensuite — clients, devis, factures — sera rattaché à cette entreprise. La renseigner correctement dès le départ vous évite de tout reprendre plus tard.
Pour qui : Gérant ou dirigeant qui vient de créer son accès personnel et ouvre l'espace de sa société
Prompt Claude : Liste-moi les [nombre] dernières entreprises enregistrées, avec leur SIRET et leur dirigeant.

Étapes observées :
- 1. Nommer l'entreprise — fenêtre 9.0s, soit ~22 mots
- 2. Renseigner l'e-mail de l'entreprise — fenêtre 9.0s, soit ~22 mots
- 3. Saisir le SIRET — fenêtre 8.0s, soit ~20 mots
- 4. Valider la création — fenêtre 2.5s, soit ~6 mots
- 5. Définir son mot de passe — fenêtre 6.5s, soit ~16 mots
- 6. Entrer dans son espace — fenêtre 16.1s, soit ~40 mots

Astuces : Le SIRET peut attendre · Deux adresses différentes
Erreurs fréquentes : Saisir son nom personnel dans le champ nom de l'entreprise : cet écran attend une société, pas une personne. · Un SIRET incomplet : le champ en attend quatorze, et le rappelle dans son libellé.

## SEO

`seo.titre` ≤ 60 caractères · `seo.description` entre 120 et 155 caractères ·
`seo.youtube_titre` ≤ 70 caractères, au format « <Titre> — RapidoCRM ».

Schéma : `src/schema/index.ts` → `ScriptSchema`.
