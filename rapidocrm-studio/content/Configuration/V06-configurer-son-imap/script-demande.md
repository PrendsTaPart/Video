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

À quoi ça sert : C'est ce réglage qui ouvre la page Boîte mail du CRM. Une fois la messagerie de la société branchée, vous écrivez à vos clients et vous leur envoyez devis et factures depuis RapidoCRM, sans repasser par votre webmail.
Pour qui : L'administrateur de la société — seul un utilisateur ayant ce rôle peut configurer le profil de la compagnie
Prompt Claude : Liste-moi mes [nombre] derniers contacts avec leur adresse e-mail.

Étapes observées :
- 1. Ouvrir la section Boîte mail — fenêtre 5.0s, soit ~12 mots
- 2. Coller le mot de passe d'application — fenêtre 5.0s, soit ~12 mots
- 3. Renseigner les quatre paramètres — fenêtre 2.0s, soit ~5 mots
- 4. Enregistrer — fenêtre 4.0s, soit ~10 mots
- 5. Vérifier la fiche complétée — fenêtre 4.4s, soit ~10 mots

Astuces : Un mot de passe d'application, pas le vôtre · Les quatre autres champs ne changent pas · Révoquer sans changer de mot de passe
Erreurs fréquentes : Coller le mot de passe habituel du compte Google au lieu du mot de passe d'application : la connexion est refusée. · Chercher les mots de passe d'application sans avoir activé la validation en deux étapes — la page n'existe pas tant que celle-ci n'est pas active.

## SEO

`seo.titre` ≤ 60 caractères · `seo.description` entre 120 et 155 caractères ·
`seo.youtube_titre` ≤ 70 caractères, au format « <Titre> — RapidoCRM ».

Schéma : `src/schema/index.ts` → `ScriptSchema`.
