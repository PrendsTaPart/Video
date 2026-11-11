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

À quoi ça sert : Voir les devis établis pour un client, leur période de validité, leur statut et leur prix, puis ouvrir celui qu'on cherche. Le logiciel prévient quand la période de signature est passée.
Pour qui : Gérant ou commercial qui suit ses propositions commerciales
Prompt Claude : Liste-moi mes [nombre] devis en attente avec leur destinataire et leur montant.

Étapes observées :
- 1. Ouvrir l'historique des devis — fenêtre 11.5s, soit ~28 mots
- 2. Lire le tableau des devis — fenêtre 5.5s, soit ~13 mots
- 3. Ouvrir un devis — fenêtre 3.5s, soit ~8 mots
- 4. Lire l'alerte de période de signature — fenêtre 3.2s, soit ~7 mots

Astuces : Deux couleurs de statut · Le devis dit lui-même qu'il est périmé · Le chargement peut prendre quelques secondes
Erreurs fréquentes : Relancer un devis dont la période de signature est passée : le bandeau rouge le dit dès l'ouverture. · Confondre le prix affiché au tableau et le total après remise, qui figure dans le devis.

## SEO

`seo.titre` ≤ 60 caractères · `seo.description` entre 120 et 155 caractères ·
`seo.youtube_titre` ≤ 70 caractères, au format « <Titre> — RapidoCRM ».

Schéma : `src/schema/index.ts` → `ScriptSchema`.
