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

À quoi ça sert : Écrire le message aujourd'hui et laisser le logiciel l'envoyer au jour et à l'heure choisis. Le message part tout seul, même si vous n'êtes pas devant l'écran ce matin-là.
Pour qui : Gérant ou commercial qui prépare ses relances à l'avance
Prompt Claude : Liste-moi mes [nombre] modèles de SMS.

Étapes observées :
- 1. Ouvrir le panneau Communication de la fiche — fenêtre 3.5s, soit ~8 mots
- 2. Choisir « Planifier un SMS » — fenêtre 2.5s, soit ~6 mots
- 3. Dire à qui le SMS part — fenêtre 4.0s, soit ~10 mots
- 4. Choisir le modèle de SMS — fenêtre 3.5s, soit ~8 mots
- 5. Fixer la date et l'heure d'envoi — fenêtre 6.5s, soit ~16 mots
- 6. Valider la planification — fenêtre 4.8s, soit ~12 mots

Astuces : Sept actions dans le même panneau · Un aperçu avant de choisir · La même fenêtre pour l'e-mail
Erreurs fréquentes : Chercher la planification dans la page Campagnes : elle est dans le panneau Communication de la fiche entreprise. · Laisser la date vide et cliquer sur Envoyer : sans date et heure d'envoi, il n'y a rien à planifier.

## SEO

`seo.titre` ≤ 60 caractères · `seo.description` entre 120 et 155 caractères ·
`seo.youtube_titre` ≤ 70 caractères, au format « <Titre> — RapidoCRM ».

Schéma : `src/schema/index.ts` → `ScriptSchema`.
