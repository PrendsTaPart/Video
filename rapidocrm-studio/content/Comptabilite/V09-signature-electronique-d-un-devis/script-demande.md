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

À quoi ça sert : Faire signer un devis sans l'imprimer ni le scanner : on l'ouvre en pleine page, on trace la signature à la souris dans le cadre prévu, et on enregistre. Le devis signé reste attaché au dossier.
Pour qui : Gérant ou commercial qui fait valider un devis devant le client
Prompt Claude : Liste-moi mes [nombre] devis en attente avec leur destinataire et leur montant.

Étapes observées :
- 1. Ouvrir le menu du devis — fenêtre 5.5s, soit ~13 mots
- 2. Ouvrir le devis à signer — fenêtre 2.5s, soit ~6 mots
- 3. Signer dans le cadre — fenêtre 4.0s, soit ~10 mots
- 4. Remonter et enregistrer — fenêtre 4.2s, soit ~10 mots

Astuces : Le cadre est en bas à droite · Deux boutons en haut · Signer n'apparaît que sur un devis
Erreurs fréquentes : Tracer la signature et fermer la page : sans le bouton enregistrer, rien n'est gardé. · Chercher « Signer » sur une facture : l'entrée n'existe que dans le menu d'un devis.

## SEO

`seo.titre` ≤ 60 caractères · `seo.description` entre 120 et 155 caractères ·
`seo.youtube_titre` ≤ 70 caractères, au format « <Titre> — RapidoCRM ».

Schéma : `src/schema/index.ts` → `ScriptSchema`.
