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

À quoi ça sert : Adresser la même lettre d'information à toutes ses entreprises clientes, à la date choisie, sans repasser par un outil d'e-mailing. Le logiciel en fait une campagne et confirme qu'elle est enregistrée.
Pour qui : Gérant ou responsable marketing qui anime son fichier clients
Prompt Claude : Liste-moi mes [nombre] dernières newsletters avec leur statut.

Étapes observées :
- 1. Ouvrir « Envoyer une newsletter » — fenêtre 3.5s, soit ~8 mots
- 2. Dire à qui la newsletter part — fenêtre 4.5s, soit ~11 mots
- 3. Fixer la date et l'heure d'envoi — fenêtre 6.0s, soit ~15 mots
- 4. Choisir le modèle de newsletter — fenêtre 3.0s, soit ~7 mots
- 5. Lire la confirmation — fenêtre 2.5s, soit ~6 mots

Astuces : Trois champs, dans l'ordre · Un aperçu sous chaque modèle · Une newsletter devient une campagne
Erreurs fréquentes : Choisir le modèle sans avoir renseigné la cible : la fenêtre commence par « Envoyé à », pas par la galerie. · Croire que l'envoi est parti : le bandeau dit « Campagne ajoutée avec succès », c'est-à-dire programmée.

## SEO

`seo.titre` ≤ 60 caractères · `seo.description` entre 120 et 155 caractères ·
`seo.youtube_titre` ≤ 70 caractères, au format « <Titre> — RapidoCRM ».

Schéma : `src/schema/index.ts` → `ScriptSchema`.
