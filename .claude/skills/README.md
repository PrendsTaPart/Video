# Les routines FoodEatUp — version d'essai

Ces routines tournent **ici, dans Claude Code**, et pas encore dans Plan'It.
C'est délibéré : la doctrine de la bible (LIVRE IV) veut qu'une routine fasse
ses preuves avant d'être promue.

## La règle de promotion

Une routine passe de l'essai à la version courante après **trois exécutions
réussies et quatorze jours d'observation**. Pas avant. Une routine qui a marché
une fois a eu de la chance ; une routine qui a marché trois fois sur deux
semaines a rencontré des cas différents.

**Trois routines nouvelles par semaine au maximum.** La limite n'est pas
arbitraire : au-delà, on n'observe plus rien, on empile.

## Ce qui est en essai

| Routine | Ce qu'elle fait | Cadence attendue |
|---|---|---|
| `publication-du-jour` | la sortie éditoriale du jour, articles, posts et vidéo | quotidienne |
| `trous-de-publication` | les écrans dont on n'a jamais parlé, et de quoi les combler | hebdomadaire |
| `episode-multicanal` | déposer un épisode monté et préparer ses six réseaux | à l'événement |

Chacune termine par `enregistrer_execution_routine` (MCP BraindCode). **Une
routine dont l'exécution n'est pas mesurée ne se pilote pas** : c'est ce qui
permettra plus tard de dire si elle mérite d'être promue, et ce qu'elle coûte.

## Les garde-fous

`.claude/hooks/garde-fous.sh`, branché en `PreToolUse`, refuse les trois gestes
qui ne se rattrapent pas — **envoyer, dépenser, détruire**. Le filtre de
`settings.json` présélectionne largement ; le script décide sur le nom exact,
pour qu'un motif trop large ne bloque jamais du travail légitime en silence.

Un quatrième verrou n'est pas dans les hooks parce qu'il est déjà dans les
données : **rien ne se planifie sur un réseau sans qu'un humain ait mis la
pièce en `valide`**, dans `/admin/production`. Aucun outil MCP n'expose ce
geste, et aucun n'existera. Le catalogue refuse lui-même une planification sur
une pièce non validée — un verrou tenu par la structure vaut mieux qu'un verrou
tenu par un filtre.

`.claude/journal-mcp.jsonl` consigne chaque appel MCP. Il n'est pas versionné :
c'est une trace d'exécution, pas du code.

## Écrire une routine de plus

Trois choses, sans lesquelles elle n'est pas installable :

1. **Un objectif chiffré.** « Faire mieux » n'est pas un objectif. « Zéro
   contenu daté d'aujourd'hui encore en brouillon à midi » en est un.
2. **Des garde-fous écrits en interdits explicites**, pas en recommandations.
3. **Ce qu'elle rend à la fin**, en cinq lignes au plus — et le droit de dire
   « rien à faire ». Un rapport qui donne l'illusion du travail est pire que
   pas de rapport.
