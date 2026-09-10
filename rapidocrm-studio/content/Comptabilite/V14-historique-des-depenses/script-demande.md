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

À quoi ça sert : Voir en un écran ce que l'entreprise a dépensé, ce qui reste à payer et ce qui est réglé, puis descendre au détail ligne par ligne, filtrer, et repartir vers le fournisseur concerné.
Pour qui : Gérant qui surveille ses sorties d'argent
Prompt Claude : Liste-moi mes [nombre] dépenses en attente avec leur montant.

Étapes observées :
- 1. Ouvrir l'onglet dépenses — fenêtre 6.5s, soit ~16 mots
- 2. Lire le tableau des dépenses — fenêtre 7.0s, soit ~17 mots
- 3. Filtrer et trier la liste — fenêtre 8.0s, soit ~20 mots
- 4. Ouvrir le menu d'une dépense — fenêtre 6.0s, soit ~15 mots
- 5. Remonter à la fiche de l'entreprise — fenêtre 4.0s, soit ~10 mots

Astuces : Les dépenses sont le troisième onglet · Trois actions seulement · La carte bénéfices tient compte des dépenses
Erreurs fréquentes : Chercher les dépenses ailleurs que dans le troisième onglet de la page Facturation. · Chercher une entrée Visualiser dans le menu d'une dépense : il n'y en a pas, seulement Modifier, Télécharger et Voir l'entreprise.

## SEO

`seo.titre` ≤ 60 caractères · `seo.description` entre 120 et 155 caractères ·
`seo.youtube_titre` ≤ 70 caractères, au format « <Titre> — RapidoCRM ».

Schéma : `src/schema/index.ts` → `ScriptSchema`.
