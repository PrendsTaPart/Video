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

À quoi ça sert : Voir les factures émises pour un client, avec leur statut et leur total, puis ouvrir la facture elle-même pour la relire ou la télécharger.
Pour qui : Gérant ou commercial qui suit ce qui a été facturé à un client
Prompt Claude : Liste-moi mes [nombre] factures en attente avec leur montant.

Étapes observées :
- 1. Ouvrir l'historique des factures — fenêtre 7.0s, soit ~17 mots
- 2. Lire les colonnes du tableau — fenêtre 3.8s, soit ~9 mots
- 3. Ouvrir une facture — fenêtre 3.7s, soit ~9 mots
- 4. Lire la facture et la télécharger — fenêtre 2.7s, soit ~6 mots

Astuces : La facture s'ouvre dans un onglet · Le détail est en bas · Un champ de recherche au-dessus du tableau
Erreurs fréquentes : Chercher le détail des lignes dans le tableau : il est dans la facture, en bas. · Fermer l'onglet de la facture en croyant revenir en arrière : le journal est resté sur l'onglet précédent.

## SEO

`seo.titre` ≤ 60 caractères · `seo.description` entre 120 et 155 caractères ·
`seo.youtube_titre` ≤ 70 caractères, au format « <Titre> — RapidoCRM ».

Schéma : `src/schema/index.ts` → `ScriptSchema`.
