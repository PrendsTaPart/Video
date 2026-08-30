# Saison 1 du « Coup de Feu » — ce que les masters montraient, ce qui a changé

Audit des trente épisodes de la saison 1, puis remontage complet. Rien n'a été
regénéré : mêmes clips Higgsfield, mêmes avatars HeyGen, mêmes voix ElevenLabs,
mêmes screencasts. Tout ce qui suit se joue au montage.

## Ce qu'il y avait à regarder

Vingt-quatre masters sur trente. Les six autres — EP004, EP009, EP011, EP012,
EP027, EP028 — n'ont jamais été montés faute de screencast (et d'avatar pour
EP012 et EP028). Ils restent hors saison tant que le Drive n'a pas leur
chapitre.

Le son n'était pas le problème : les vingt-quatre sortaient entre −14,2 et
−14,6 LUFS pour une cible à −14, crête vraie entre −1,5 et −2,3 dBTP. La chaîne
de normalisation fait son travail. Ce qui suit est ailleurs.

## Les six défauts mesurés

### 1. Vingt-deux épisodes sur vingt-quatre annonçaient « DIX LOGICIELS »

Le carton du milieu — le seul endroit de la série qui chiffre la promesse —
disait dix. Le chiffre du produit est huit. Seuls EP001 et EP002 portaient déjà
le carton refait ; les vingt-deux autres portaient l'ancien, avec dix pastilles
au lieu de huit et sans la ligne « et aucun ne se parle ».

Le carton « huit » existait dans `templates/` depuis des semaines, mais il
n'était pas le défaut du script de montage : chaque nouvel épisode repartait
donc sur le mauvais chiffre.

### 2. La chute n'était jamais écrite

La punchline — la phrase qui retourne le gag, à 5,0 s — n'existait que dans la
bande son. L'accroche, elle, était incrustée. Sur un fil social regardé sans le
son, on lisait donc la mise en place et on n'avait jamais le retournement : la
moitié de l'épisode qui fait rire ne franchissait pas l'écran muet.

### 3. Une accroche coupée aux deux bouts

`drawtext` ne replie pas et ne rétrécit pas : il dessine à la taille demandée et
ce qui dépasse du cadre est perdu, sans le moindre avertissement. Sur EP017 —
« Personne ne touche à ta dernière frite. » — le master affichait
« ersonne ne touche à ta dernière frit », premier et dernier mot rabotés, sur la
seule phrase que le spectateur lit pendant les trois premières secondes.

### 4. Une porte qui claque à 9,5 s

Mesuré sur les vingt-quatre : à 9,45 s l'ambiance du clip tapait encore entre
−7 et −20 dBFS, et à 9,52 s — première frame du carton — elle tombait à −28 à
−41 dBFS. Coupe franche, sans fondu, à l'endroit exact où le spectateur décide
s'il reste.

### 5. Un trou de son avant la signature

La respiration qui précède la voix de fin est voulue : sans elle, la dernière
syllabe de l'avatar tombe sur le premier mot de la signature. Mais sur
vingt-deux masters sur vingt-quatre, cette fenêtre était à **−120 dBFS** : le
silence numérique exact, pas un silence de studio. À l'oreille ce n'est pas une
respiration, c'est une coupure de son — on croit que le fichier a lâché.

### 6. Un quart de la vidéo est une image fixe

Détection de gel image par image, moyenne sur les vingt-quatre :

| Segment | Durée | Dont image figée |
|---|---:|---:|
| A — le gag | 9,5 s | 0,0 s |
| B/C — le carton | 9,0 s | **6,2 s** |
| D — avatar + logiciel | 10,0 s | 0 à 8,0 s selon le screencast |
| E + sting de marque | 9,0 s | **2,9 s** |

Le carton du milieu construit son propos en trois apparitions — le titre, les
pastilles, le prix — toutes posées à 16,2 s, puis ne bouge plus pendant les
2,3 dernières secondes. Et la fin enchaîne **deux** cartons de marque plein
écran, l'un derrière l'autre : la signature (28,5 → 32,5) puis le sting
(32,5 → 37,5). Neuf secondes sur trente-sept et demie — 24 % de l'épisode — à
regarder deux fois le même logo au-dessus de la même adresse.

## Deux défauts trouvés en cours de route

**Cinq clips changent de plan avant la fin.** EP002, EP003, EP013, EP014 et
EP022 : entre 7,2 et 8,5 s, le rendu Higgsfield enchaîne sur un tout autre cadre
— en général un chef qui parle face caméra, sans rapport avec le gag, et dont la
bouche bouge sans qu'aucun son n'en sorte. Personne ne l'avait vu parce que ça
n'existait pas : le segment A faisait 7 s quand ces clips ont été validés.
L'allonger à 9,5 s pour ne plus couper la chute a fait entrer dans le cadre ce
que la fenêtre courte laissait dehors.

**L'avatar entrait en parlant.** De 18,5 à 28,0 s, la parole était continue,
premier mot sur la première frame du segment. Le montage courant fait entrer
l'avatar en retard, sur une frame d'attente — on voit d'abord le logiciel, puis
quelqu'un vient l'expliquer — mais les masters de la saison 1 sont antérieurs à
cette correction.

## Ce qui a été corrigé, et comment

| Défaut | Correction | Où |
|---|---|---|
| Carton « dix » | `COMMUN_sting_BC_huit.mp4` devient le défaut | `build-episode.sh` |
| Chute muette à l'écran | La punchline est incrustée de 5,0 s à sa fin | `build-segment-a.sh` |
| Texte coupé | Mesure réelle de l'encre, puis rétrécissement ou repli | `ajuster-texte.py` |
| Coupe brutale à 9,5 s | Fondu de 0,40 s sur l'ambiance du clip | `build-segment-a.sh` |
| Trou avant la signature | Le lit musical se pose à −20 dB au lieu de s'éteindre | `build-episode.sh` |
| Plan parasite en fin de clip | Détection du changement de plan, arrêt et étirement | `build-segment-a.sh` |
| Avatar qui entre en parlant | Récupéré en remontant : le retard d'entrée existait déjà | `build-episode.sh` |

### Ce que ça donne, mesuré sur les vingt-quatre

| | Avant | Après |
|---|---|---|
| Carton « huit logiciels » | 2 épisodes sur 24 | **24 sur 24** |
| Punchline lisible sans le son | 0 sur 24 | **24 sur 24** |
| Niveau à 9,45 s, juste avant la coupe | −13 à −31 dBFS | **−23 à −30 dBFS** |
| Respiration avant la signature | −120 dBFS sur 22 épisodes | **−31 à −45 dBFS** |
| Loudness / crête vraie | −14,2 à −14,6 LUFS · −1,5 à −2,3 dBTP | −14,2 à −14,5 · −1,5 à −2,2 |
| Contrôle qualité | — | **24 conformes, 0 échec** |

Les deux lignes du milieu disent la même chose autrement : avant, le raccord
dépendait du clip — sur un épisode l'ambiance était encore à −13 dBFS quand le
carton arrivait, sur un autre elle était déjà à −31. Dix-huit décibels d'écart
d'un épisode à l'autre, au même endroit du montage. Après, l'écart est de sept.
C'est ça, la reconnaissance de série : le même geste au même moment.

Un script de remontage a été ajouté pour que l'opération soit refaisable :

```bash
./scripts/remonter-saison.sh 1          # toute la saison
./scripts/remonter-saison.sh 1 EP013    # ou quelques épisodes
```

Il repart des assets d'origine et ne génère rien. C'est l'outil qui manquait :
le montage évolue, les masters déjà sortis ne bougent pas, et au bout de
quelques semaines une saison n'est plus homogène — ce qui se voit bien plus
qu'un défaut isolé.

## Ce qui reste à décider

Trois choses n'ont pas été faites parce qu'elles dépassent la correction de
montage et changent le contrat de la série.

**La fin à neuf secondes.** C'est le plus gros gisement. Fondre la signature et
le sting en une seule sortie de 4 à 5 s rendrait quatre secondes au contenu et
ferait passer le master de 37,5 s à 33 s. Mais 37,5 s est écrit dans le contrôle
qualité, dans les données du site (`dureeSecondes`) et dans les deux cent seize
masters déjà sortis des autres saisons. À arbitrer pour la série entière, pas
pour une saison.

**Le carton du milieu.** Neuf secondes dont 6,2 figées. Il peut tenir en sept, ou
garder ses neuf secondes en animant le prix et les pastilles au lieu de les
poser d'un coup. Les deux demandent de refaire `COMMUN_sting_BC_huit.mp4`, donc
de retoucher les cent cinquante épisodes d'un coup — PR dédiée, comme le veut la
règle des gabarits.

**Le screencast illisible.** Le logiciel est incrusté à 960 × 414 dans un cadre
de 1080 de large : sur un téléphone, l'interface est là mais son texte ne se lit
pas. Sur EP013, à 24 s, l'écran est même vide — un menu latéral et une zone de
contenu blanche — pendant que l'avatar explique que PrediBot lit les vraies
données. Un zoom lent sur la zone active vaudrait mieux qu'une capture entière,
mais ça se décide chapitre par chapitre.

## Ce qui bloque encore, côté assets

| Épisode | Ce qui manque | Conséquence |
|---|---|---|
| EP013 | l'avatar dit « Une seule interface, pas dix » | rendu HeyGen à refaire sur « pas huit » |
| EP022 | la voix dit « Pour dix logiciels qui ne se parlent même pas » | voix ElevenLabs à refaire sur « huit » |
| EP010 | la voix dit « Pour dix outils qui ne se parlent pas » | voix ElevenLabs à refaire sur « huit » |

Ces trois épisodes sont montés dans leur **état cible** — texte incrusté et
carton à « huit » — et marqués `a_refaire` dans `state/`. Ils ne doivent pas
être publiés tant que la voix n'a pas rattrapé le texte. Le serveur ElevenLabs
n'a pas répondu pendant cette session (404), la génération n'a donc pas pu être
faite ici.

EP120, en saison 4, porte la même formule (« La réunion des dix logiciels »).
Son texte est corrigé dans les données ; son master sera à remonter avec sa
saison.
