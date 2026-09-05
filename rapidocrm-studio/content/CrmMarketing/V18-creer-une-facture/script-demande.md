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

À quoi ça sert : Facturer un client sans ressaisir ses coordonnées : on choisit un produit du catalogue, le logiciel calcule les montants, et la facture rejoint l'activité de la fiche.
Pour qui : Gérant ou commercial qui facture une prestation à un client existant
Prompt Claude : Liste-moi mes [nombre] factures en attente avec leur montant.

Étapes observées :
- 1. Ouvrir « Créer une facture » depuis la fiche — fenêtre 2.7s, soit ~6 mots
- 2. Logo et charte graphique de la facture — fenêtre 4.5s, soit ~11 mots
- 3. Choisir le produit à facturer — fenêtre 7.0s, soit ~17 mots
- 4. Laisser les montants se calculer — fenêtre 7.0s, soit ~17 mots
- 5. Délai, mentions légales et statut — fenêtre 5.5s, soit ~13 mots
- 6. Mode de paiement, totaux et enregistrement — fenêtre 3.5s, soit ~8 mots
- 7. Retrouver la facture dans l'activité de la fiche — fenêtre 3.0s, soit ~7 mots

Astuces : Trois documents, un seul panneau · Le carrousel cache le reste du catalogue · Le total se lit deux fois
Erreurs fréquentes : Saisir les montants à la main : ils viennent du produit et se recalculent tout seuls. · Oublier la date de fin : les deux dates bornent la période facturée.

## SEO

`seo.titre` ≤ 60 caractères · `seo.description` entre 120 et 155 caractères ·
`seo.youtube_titre` ≤ 70 caractères, au format « <Titre> — RapidoCRM ».

Schéma : `src/schema/index.ts` → `ScriptSchema`.
