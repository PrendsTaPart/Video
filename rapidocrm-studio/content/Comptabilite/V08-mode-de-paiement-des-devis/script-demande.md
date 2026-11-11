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

À quoi ça sert : Dire, sur le devis lui-même, par quel moyen le client réglera — espèce, carte bleue, virement ou chèque. Le devis part avec l'information, et quand il devient une facture, personne n'a à la redemander.
Pour qui : Gérant ou commercial qui prépare un devis avant de l'envoyer
Prompt Claude : Liste-moi mes [nombre] devis en attente avec leur destinataire et leur montant.

Étapes observées :
- 1. Ouvrir la liste des devis — fenêtre 4.5s, soit ~11 mots
- 2. Ouvrir le devis en modification — fenêtre 4.0s, soit ~10 mots
- 3. Descendre au mode de paiement — fenêtre 4.0s, soit ~10 mots
- 4. Choisir le mode et enregistrer — fenêtre 2.5s, soit ~6 mots
- 5. Lire la confirmation — fenêtre 2.1s, soit ~5 mots

Astuces : Un seul moyen à la fois · Le récapitulatif est juste en dessous · L'envoi se décide dans la même modale
Erreurs fréquentes : Chercher le mode de paiement dans le tableau des devis : il est dans le formulaire du devis, sous le statut. · Cocher un mode et quitter sans enregistrer : c'est le bouton modifier, en bas de la modale, qui valide.

## SEO

`seo.titre` ≤ 60 caractères · `seo.description` entre 120 et 155 caractères ·
`seo.youtube_titre` ≤ 70 caractères, au format « <Titre> — RapidoCRM ».

Schéma : `src/schema/index.ts` → `ScriptSchema`.
