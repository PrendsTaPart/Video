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

À quoi ça sert : Ouvrir l'historique des devis, filtrer par statut ou par entreprise, et repartir de la ligne trouvée : la consulter dans un nouvel onglet, la modifier, ou en télécharger le fichier.
Pour qui : Gérant ou commercial qui cherche un devis passé
Prompt Claude : Liste-moi mes [nombre] derniers devis avec leur destinataire, leur statut et leur montant.

Étapes observées :
- 1. Ouvrir l'historique des devis — fenêtre 6.0s, soit ~15 mots
- 2. Ouvrir le menu d'une ligne — fenêtre 6.0s, soit ~15 mots
- 3. Visualiser le devis — fenêtre 6.0s, soit ~15 mots
- 4. Télécharger le devis — fenêtre 6.0s, soit ~15 mots
- 5. Les autres actions de la ligne — fenêtre 4.1s, soit ~10 mots

Astuces : Visualiser ouvre un onglet · Quatre gestes par ligne · Les filtres se cumulent
Erreurs fréquentes : Croire que le devis a disparu alors qu'un filtre est encore actif. · Confondre Visualiser et Modifier : le premier ouvre le devis en lecture dans un nouvel onglet, le second rouvre le formulaire.

## SEO

`seo.titre` ≤ 60 caractères · `seo.description` entre 120 et 155 caractères ·
`seo.youtube_titre` ≤ 70 caractères, au format « <Titre> — RapidoCRM ».

Schéma : `src/schema/index.ts` → `ScriptSchema`.
