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

À quoi ça sert : Vous ne vous souvenez plus de votre mot de passe et vous êtes bloqué devant la page de connexion. RapidoCRM vous envoie un lien par e-mail, vous en choisissez un nouveau, et vous retrouvez votre tableau de bord sans appeler personne.
Pour qui : Toute personne qui a déjà un compte RapidoCRM et n'arrive plus à se connecter
Prompt Claude : Liste-moi les [nombre] utilisateurs de mon CRM, avec leur nom et leur adresse e-mail.

Étapes observées :
- 1. Ouvrir « mot de passe oublié » — fenêtre 6.0s, soit ~15 mots
- 2. Saisir son adresse e-mail — fenêtre 7.5s, soit ~18 mots
- 3. Recevoir le lien de réinitialisation — fenêtre 8.0s, soit ~20 mots
- 4. Choisir un nouveau mot de passe — fenêtre 12.5s, soit ~31 mots
- 5. Se reconnecter — fenêtre 11.0s, soit ~27 mots
- 6. Retrouver son tableau de bord — fenêtre 6.1s, soit ~15 mots

Astuces : Le lien part tout de suite · Vous n'avez pas besoin de l'ancien mot de passe
Erreurs fréquentes : Saisir une autre adresse que celle du compte : aucun message n'arrivera, sans que rien ne le signale. · Deux mots de passe différents dans les deux champs : le nouveau mot de passe n'est pas enregistré.

## SEO

`seo.titre` ≤ 60 caractères · `seo.description` entre 120 et 155 caractères ·
`seo.youtube_titre` ≤ 70 caractères, au format « <Titre> — RapidoCRM ».

Schéma : `src/schema/index.ts` → `ScriptSchema`.
