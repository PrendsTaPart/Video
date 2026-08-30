# Prompt Claude — la recherche préalable aux agents de commercialisation FoodEatUp

> À coller dans une **conversation Claude** (claude.ai), pas dans Claude Code.
> Il ne produit pas de code : il produit la recherche et les prompts d'un
> nouveau projet — les agents IA qui commercialisent FoodEatUp.
>
> Prévoir deux ou trois échanges. Le prompt demande explicitement de poser ses
> questions avant de rédiger : une réponse d'un seul bloc serait moins bonne.

---

## Le prompt à coller

---

Tu vas m'aider à concevoir un système d'agents IA qui **commercialisent** un
logiciel SaaS. Avant d'écrire quoi que ce soit, lis tout et pose-moi les
questions qui te manquent — je préfère trois allers-retours à un livrable
qui suppose.

### Le produit

**FoodEatUp** est un logiciel de gestion pour la restauration, vendu en
abonnement. Il couvre dix modules : HACCP et hygiène, réservations et plan de
salle, caisse et encaissement, écran cuisine, stock et fournisseurs, recettes et
allergènes, ressources humaines (planning, pointages, recrutement), marketing
(campagnes, segments RFM, fidélité, avis), site vitrine et commande en ligne,
facturation et dépenses. Environ 85 écrans, pilotables par un serveur MCP de
187 outils.

Autour du produit gravitent quatre autres logiciels de la maison, tous dotés
d'un serveur MCP : un **hub** qui détient la carte des modules et des écrans,
une **académie** de tutoriels vidéo, un **site inbound** (articles, posts
sociaux, aimants à prospects, séquences e-mail), et un **catalogue social** qui
produit et publie des séries vidéo courtes. Ils partagent une clé commune, le
couple `module` + `ecran` : un article, un tutoriel et un épisode vidéo se
rattachent au même écran du logiciel.

### La cible

Restaurateurs indépendants et petites chaînes, en France. Le secteur compte
plus que le métier : un boulanger, un chef de cuisine, un franchisé et un
gérant indépendant n'ont ni les mêmes journées ni les mêmes douleurs.

### Ce que je te demande

**1 · Une recherche, pas une opinion.** Cherche et cite tes sources sur :

- comment les logiciels de gestion pour la restauration se vendent réellement en
  France aujourd'hui — canaux, cycle, prescripteurs, rôle des revendeurs et des
  éditeurs de caisse ;
- ce qui déclenche l'achat, et ce qui le bloque. Je veux les **objections
  réelles** — le coût, la peur de la migration, le personnel qui ne suivra pas,
  l'engagement, le matériel — pas des objections théoriques ;
- les repères chiffrés qu'on peut trouver : coût d'acquisition, durée du cycle,
  taux de transformation d'un essai, attrition. Quand un chiffre n'existe pas
  publiquement, **dis-le** plutôt que de l'estimer ;
- ce que font les concurrents en matière de contenu et de prospection, et ce
  qu'ils ne font pas.

**2 · La cartographie des agents.** Propose entre cinq et huit agents de
commercialisation. Pour chacun :

- sa raison d'être en une phrase — s'il en faut deux, c'est deux agents ;
- ce qu'il fait, ce qu'il ne fait **jamais**, et où passe la frontière avec
  l'humain ;
- **les gestes irréversibles qui lui sont interdits** : envoyer un message à un
  prospect réel, engager une dépense publicitaire, modifier un prix, signer.
  Ces trois-là sont non négociables — dis-moi s'il y en a d'autres ;
- son objectif chiffré, mesurable **sans lui demander son avis** ;
- ses KPI : un principal, deux secondaires, et **le contre-indicateur** qui dit
  qu'il travaille mal en ayant l'air de bien travailler (volume qui monte pendant
  que la qualité baisse) ;
- sa cadence — quotidienne, hebdomadaire, déclenchée par un événement.

**3 · Les prompts.** Pour chaque agent, le prompt système complet, prêt à
coller : rôle, contexte produit, méthode pas à pas, format de sortie exact,
garde-fous rédigés en interdits explicites, et **ce qu'il doit faire quand il
manque une information** — la réponse attendue est « demander ou écrire "à
vérifier" », jamais inventer.

**4 · Mon tableau de bord à moi.** Séparément des agents : qu'est-ce que je dois
regarder, à quelle fréquence, et quel geste chaque ligne appelle. Je veux une
liste d'actions et de décisions, pas un mur de compteurs. Distingue nettement
ce qui demande une décision humaine de ce qui s'observe.

**5 · L'ordre de mise en route.** Par quel agent commencer, et pourquoi.
Quel signal dit qu'il fonctionne avant d'en lancer un deuxième. Je m'impose
**trois agents nouveaux par mois au maximum** : dis-moi si c'est trop lent, trop
rapide, et sur quel critère.

### Contraintes que je ne discuterai pas

- **Aucun agent n'envoie rien à un prospect réel sans validation humaine.**
  Ils préparent des brouillons ; un humain envoie. Conçois le système avec cette
  contrainte comme une donnée, pas comme une limite provisoire à lever plus tard.
- **Aucune donnée personnelle de prospect inventée.** RGPD, et bon sens.
- Un agent sans objectif chiffré et sans garde-fou n'existe pas. S'il t'en vient
  un que tu ne sais pas doter des deux, dis-le et écarte-le.
- Le français, y compris dans les prompts.

### Deux choses à garder en tête

**Ce système sera dupliqué.** Il est conçu pour FoodEatUp, mais il doit se
reconfigurer pour une autre entreprise en changeant le produit, la cible et les
objectifs — sans réécrire les agents. Marque clairement, dans chaque prompt, ce
qui est **propre à FoodEatUp** et ce qui est **la structure réutilisable**.

**Je veux du désaccord.** Si un agent que je semble vouloir est une mauvaise
idée, dis-le et propose autre chose. Si la recherche contredit une hypothèse de
ce brief, la recherche gagne — signale-le explicitement plutôt que d'arranger
ta réponse.

### Comment procéder

Commence par tes questions. Puis livre dans cet ordre : la recherche sourcée,
la cartographie des agents, mon tableau de bord, l'ordre de mise en route, et
les prompts en dernier — ils découlent du reste et n'ont pas de sens avant.

---

## Après cette conversation

Ce que la conversation produit revient ici sous trois formes :

| Livrable | Destination |
|---|---|
| Les prompts système des agents | `.claude/skills/` du dépôt qui les fait tourner, une routine par agent |
| Les KPI et objectifs chiffrés | `definir_kpi` puis `rattacher_kpi_routine` sur le MCP BraindCode |
| Le tableau de bord personnel | l'onglet « Moi » de `/pilotage` — voir `PROMPT-LOVABLE-KPI-AGENTS.md` |

Et la même discipline que pour les routines de production : **trois exécutions
et quatorze jours d'observation** avant qu'un agent passe de l'essai à la
version courante.
