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

À quoi ça sert : Rassembler en une page tout ce qui s'est passé avec un client : e-mails, SMS, rendez-vous, contrats, documents, factures, devis, dépenses et notes. Chaque journal s'ouvre d'un clic.
Pour qui : Gérant ou commercial qui reprend un dossier client
Prompt Claude : Donne-moi les statistiques d'interactions du mois pour l'entreprise numéro [identifiant].

Étapes observées :
- 1. Ouvrir le panneau Entreprise de la fiche — fenêtre 5.5s, soit ~13 mots
- 2. Ouvrir l'historique de l'entreprise — fenêtre 4.0s, soit ~10 mots
- 3. Parcourir les neuf journaux — fenêtre 4.0s, soit ~10 mots
- 4. Choisir le journal à consulter — fenêtre 3.3s, soit ~8 mots

Astuces : Neuf journaux, un seul écran · Le même bouton partout · Quatre entrées dans l'accordéon
Erreurs fréquentes : Chercher l'historique dans le bloc Communication : il est dans l'accordéon Entreprise. · S'arrêter à la première rangée de cartes : six autres journaux attendent plus bas.

## SEO

`seo.titre` ≤ 60 caractères · `seo.description` entre 120 et 155 caractères ·
`seo.youtube_titre` ≤ 70 caractères, au format « <Titre> — RapidoCRM ».

Schéma : `src/schema/index.ts` → `ScriptSchema`.
