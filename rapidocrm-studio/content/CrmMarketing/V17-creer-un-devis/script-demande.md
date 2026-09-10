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

À quoi ça sert : Établir un devis sans quitter la fiche du client : on choisit un produit du catalogue et le logiciel remplit les montants. Le devis rejoint ensuite l'activité de l'entreprise, daté et horodaté.
Pour qui : Gérant ou commercial qui chiffre une prestation pour un client existant
Prompt Claude : Liste-moi mes [nombre] devis en attente avec leur destinataire et leur montant.

Étapes observées :
- 1. Ouvrir « Créer un devis » depuis la fiche — fenêtre 3.5s, soit ~8 mots
- 2. Logo et charte graphique du devis — fenêtre 4.0s, soit ~10 mots
- 3. Choisir le produit, les montants suivent — fenêtre 5.5s, soit ~13 mots
- 4. Fixer les dates du devis — fenêtre 5.0s, soit ~12 mots
- 5. Délai de paiement, mentions légales, statut — fenêtre 9.0s, soit ~22 mots
- 6. Mode de paiement, totaux et enregistrement — fenêtre 4.8s, soit ~12 mots
- 7. Retrouver le devis dans l'activité de la fiche — fenêtre 5.2s, soit ~12 mots

Astuces : Le devis part de la fiche client · Le logo se reprend du client · L'envoi se décide dans la même fenêtre
Erreurs fréquentes : Taper le prix à la main : les montants viennent du produit du catalogue et se recalculent tout seuls. · Cocher un statut et fermer la fenêtre : c'est le bouton Enregistrer, tout en bas, qui crée le devis.

## SEO

`seo.titre` ≤ 60 caractères · `seo.description` entre 120 et 155 caractères ·
`seo.youtube_titre` ≤ 70 caractères, au format « <Titre> — RapidoCRM ».

Schéma : `src/schema/index.ts` → `ScriptSchema`.
