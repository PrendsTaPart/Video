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

À quoi ça sert : Ne pas ressaisir une facture quand le devis est signé. Signer le devis crée la facture : mêmes lignes, même montant, même client, et elle apparaît dans l'onglet facture avec son propre numéro.
Pour qui : Gérant ou commercial qui facture ce qu'il vient de faire accepter
Prompt Claude : Liste-moi mes [nombre] dernières factures avec leur statut et leur montant.

Étapes observées :
- 1. Ouvrir le devis à convertir — fenêtre 6.0s, soit ~15 mots
- 2. Signer le devis et enregistrer — fenêtre 23.0s, soit ~57 mots
- 3. Lire ce que le logiciel annonce — fenêtre 5.0s, soit ~12 mots
- 4. Passer à l'onglet facture — fenêtre 12.0s, soit ~30 mots
- 5. Retrouver la facture créée — fenêtre 9.5s, soit ~23 mots

Astuces : La signature fait la facture · Le bandeau dit tout · Les compteurs suivent
Erreurs fréquentes : Chercher un bouton « convertir en facture » : il n'y en a pas. C'est la signature du devis qui crée la facture. · Croire que le client a reçu la facture : si la boîte mail n'est pas branchée, le bandeau le dit — « l'envoi de l'e-mail a échoué » — et la facture existe quand même.

## SEO

`seo.titre` ≤ 60 caractères · `seo.description` entre 120 et 155 caractères ·
`seo.youtube_titre` ≤ 70 caractères, au format « <Titre> — RapidoCRM ».

Schéma : `src/schema/index.ts` → `ScriptSchema`.
