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

À quoi ça sert : Cette page décide de ce que vos clients voient. Votre identité côté logiciel, et surtout la fiche de la société émettrice : c'est elle qui apparaîtra en tête de vos devis et de vos factures, avec son logo, son adresse et sa couleur.
Pour qui : Gérant, dirigeant, ou toute personne chargée de l'apparence des documents commerciaux
Prompt Claude : Montre-moi les informations de ma société émettrice : nom, SIRET, adresse et coordonnées.

Étapes observées :
- 1. Ouvrir sa fiche profil — fenêtre 10.0s, soit ~25 mots
- 2. Renseigner son identité — fenêtre 7.0s, soit ~17 mots
- 3. Ajouter numéro et adresse — fenêtre 7.0s, soit ~17 mots
- 4. Sauvegarder — fenêtre 4.0s, soit ~10 mots
- 5. Compléter la fiche entreprise — fenêtre 16.0s, soit ~40 mots
- 6. Adresse et couleur des factures — fenêtre 19.0s, soit ~47 mots

Astuces : Deux blocs, deux identités · La couleur suit vos factures
Erreurs fréquentes : Confondre ses coordonnées personnelles et celles de la société : ce sont deux blocs distincts sur la même page. · Quitter la page sans cliquer sur sauvegarder : le bouton est en bas de la première section.

## SEO

`seo.titre` ≤ 60 caractères · `seo.description` entre 120 et 155 caractères ·
`seo.youtube_titre` ≤ 70 caractères, au format « <Titre> — RapidoCRM ».

Schéma : `src/schema/index.ts` → `ScriptSchema`.
