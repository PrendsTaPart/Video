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

À quoi ça sert : Écrire une fois un message qu'on envoie souvent — la facture est partie, le devis est prêt — et le rappeler d'un clic au lieu de le retaper. Le template porte son texte, son bouton d'action et sa catégorie.
Pour qui : Gérant ou commercial qui envoie les mêmes messages toute la semaine
Prompt Claude : Liste-moi mes [nombre] templates SMS.

Étapes observées :
- 1. Ouvrir la page des templates SMS — fenêtre 5.8s, soit ~14 mots
- 2. Nommer le template — fenêtre 5.7s, soit ~14 mots
- 3. Écrire le message — fenêtre 6.5s, soit ~16 mots
- 4. Ajouter le bouton et valider — fenêtre 6.0s, soit ~15 mots
- 5. Retrouver le template dans la liste — fenêtre 6.0s, soit ~15 mots

Astuces : Le bot peut écrire le message · Le CTA se choisit dans une liste · La liste se filtre par catégorie
Erreurs fréquentes : Laisser la catégorie vide et ne plus retrouver le template derrière le filtre en haut de page. · Fermer la modale sans le bouton ajouter, tout en bas : rien n'est enregistré.

## SEO

`seo.titre` ≤ 60 caractères · `seo.description` entre 120 et 155 caractères ·
`seo.youtube_titre` ≤ 70 caractères, au format « <Titre> — RapidoCRM ».

Schéma : `src/schema/index.ts` → `ScriptSchema`.
