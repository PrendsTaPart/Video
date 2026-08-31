# Clip musical de la saison 2 — « LA MAISON »

Le prompt Suno de la chanson du clip musical. Les clips sortent le **samedi**,
les épisodes en semaine (règle du catalogue Social FoodEatUp).

**Ce n'est pas une chanson sur la série.** Aucun film, aucun genre de cinéma,
aucun clin d'œil au format : c'est une histoire racontée à la première
personne, du rap français narratif, une année de la vie d'un restaurateur.
Michael ouvre, se noie, craque un mardi de février, et repart autrement. Le
refrain revient trois fois avec les mêmes mots et ne veut pas dire la même
chose la troisième fois — c'est là-dessus que tient le morceau.

Deux clips existent déjà et fixent la méthode : `le-clash` (144 BPM mesurés
pour 142 demandés) et `il-etait-une-fois-un-restaurant` (90,7 mesurés pour 92
demandés). **Le BPM demandé n'est jamais le BPM obtenu** : la grille de montage
se construit sur le tempo *mesuré* après génération.

---

## Ce que la chanson doit permettre au montage

La matière du clip, ce sont les **60 plans de la saison** (30 épisodes ×
2 scènes). Le montage suit l'histoire, pas l'ordre des épisodes : les plans
sont redistribués selon ce que raconte la ligne.

| Partie | Ce que le montage y met | Durée visée |
|---|---|---|
| Intro | la salle vide avant l'ouverture, un seul plan qui respire | 14 s |
| Couplet 1 — l'ouverture | les plans calmes, les premiers services, les visages | 40 s |
| Refrain | la salle pleine, les plans larges, l'énergie | 26 s |
| Couplet 2 — la noyade | les plans de chaos : téléphones, palettes, papiers, files | 40 s |
| Refrain | mêmes plans larges, coupes plus dures | 26 s |
| Pont — il craque | **un seul plan, sans coupe**, la salle vide au ralenti | 26 s |
| Couplet 3 — il repart | les gestes qui se posent, les écrans, les statuts qui basculent | 40 s |
| Refrain final | les trente épisodes en accéléré, un plan par épisode | 30 s |
| Outro | le dernier plan, le noir | 14 s |

≈ **4 min 16**. Si la prise sort plus courte, les sections se resserrent
proportionnellement : ce sont des cibles d'écriture, la grille de montage se
cale sur le tempo réellement mesuré.

Le pont est le seul endroit du clip où un plan tient sans coupe : si la prise
générée ne fait pas retomber la batterie, le parti pris disparaît. C'est le
premier critère de choix entre deux prises.

La répartition exacte des soixante plans entre ces sections est écrite dans
`clip-musical/plan-des-plans.json` : chaque plan y est placé pour ce qu'il
montre à cet endroit du récit, jamais pour son numéro d'épisode. Les soixante
y sont, aucun n'est laissé de côté.

---

## 1. Champ « Style of Music »

```text
French storytelling rap, early-2000s Paris sound: boom-bap drums with a fat live snare, warm upright bass, a soulful minor piano loop, string section swelling on the chorus, faint vinyl crackle underneath. Male lead vocal in French, clear urgent diction, fast conversational flow on the verses, half-sung anthemic chorus doubled by a small crowd of voices. Sincere and narrative, never aggressive, never boastful. 92 BPM, D minor, straight 4/4. On the bridge the drums drop out completely: piano and voice alone, spoken. No autotune, no trap hi-hats, no EDM drop, no brass. Clean modern mastering, warm low end, vocals forward.
```

## 2. Champ « Title »

```text
LA MAISON
```

## 3. Champ « Lyrics »

```text
[Intro — piano alone, vinyl crackle, no drums]
Sept heures du matin.
La salle est vide.
Elle m'attend.

[Couplet 1 — flow posé, presque parlé]
J'avais vingt-six ans, un bail, et pas un rond,
le local sentait le vieux, mon père a dit « fonce ».
J'ai peint les murs moi-même un dimanche de novembre,
j'ai dormi sur la banquette du fond entre deux commandes.
Premier soir : six clients, et j'ai pleuré dans la réserve —
pas de la tristesse, du trac, de la fierté, de la fièvre.
J'ai cru que c'était fait, j'ai cru que j'avais gagné.
Un restaurant c'est pas un rêve. C'est un métier.

[Refrain — batterie pleine, chœurs]
C'est ma maison, c'est mes murs, c'est mes tables,
c'est mon nom sur la porte et mon père dans le cadre.
J'ai tout donné, j'ai tout repris dans la gueule,
j'ai failli tout lâcher, j'ai jamais été seul.
C'est ma maison, et ce soir elle est pleine.
J'ai les mains qui tremblent, mais j'ouvre quand même.
C'est ma maison. Vingt-huit couverts. Un service.
Et personne ici ne sait ce que ça coûte.

[Couplet 2 — le flow accélère]
Puis l'année m'est tombée dessus comme un service sans fin :
le téléphone qui sonne quand j'ai les deux mains pleines,
le livreur qui se perd, le fournisseur qui se trompe,
le contrôle qui débarque et me demande mes relevés.
J'ai des feuilles partout, j'ai des chiffres dans la tête,
trois congés le même samedi — et c'est moi qui les ai signés.
J'ai compté le stock trois fois : trois résultats différents.
J'ai fermé à minuit. J'ai recompté en pleurant.

[Refrain]
C'est ma maison, c'est mes murs, c'est mes tables,
c'est mon nom sur la porte et mon père dans le cadre.
J'ai tout donné, j'ai tout repris dans la gueule,
j'ai failli tout lâcher, j'ai jamais été seul.
C'est ma maison, et ce soir elle est pleine.
J'ai les mains qui tremblent, mais j'ouvre quand même.
C'est ma maison. Vingt-huit couverts. Un service.
Et personne ici ne sait ce que ça coûte.

[Pont — parlé, piano seul, batterie coupée]
Un mardi de février,
j'ai posé les clés sur le comptoir.
J'ai regardé la salle vide
et j'ai pensé : j'arrête.
Ma mère a appelé.
Elle a rien dit d'utile.
Elle a juste dit : « t'as mangé ? »
…
J'ai repris les clés.

[Couplet 3 — le flow se calme, la batterie revient doucement]
J'ai pas changé de métier, j'ai changé de méthode.
J'ai arrêté de tout garder dans ma tête, c'est tout.
Ce que je note, je le retrouve. Ce que je sais, je le passe.
Le planning est sur le mur, plus dans mon estomac.
Le stock se compte tout seul, l'ardoise se solde,
le samedi est couvert avant même que je demande.
J'ai pas gagné au loto, j'ai juste posé les choses.
Et le soir quand je ferme, il me reste de la voix.

[Refrain final — chœurs pleins, cordes]
C'est ma maison, c'est mes murs, c'est mes tables,
c'est mon nom sur la porte et mon père dans le cadre.
J'ai tout donné, j'ai rien repris dans la gueule,
j'ai failli tout lâcher — j'ai jamais été seul.
C'est ma maison, et ce soir elle est pleine.
J'ai plus les mains qui tremblent quand j'ouvre le matin.
C'est ma maison. Vingt-huit couverts. Un service.
Et ce soir, pour la première fois, je respire.

[Outro — piano seul, puis silence]
Et mon père, dans le cadre, il dit rien.
Mais je crois qu'il sourit.
```

---

## Le détail qui porte tout le morceau

Le refrain est identique trois fois **à deux mots près**, et ces deux mots
sont le sujet de la chanson :

| | Refrain 1 et 2 | Refrain final |
|---|---|---|
| ligne 3 | j'ai **tout** repris dans la gueule | j'ai **rien** repris dans la gueule |
| ligne 6 | j'ai les mains qui tremblent, **mais j'ouvre quand même** | j'ai **plus** les mains qui tremblent |
| ligne 8 | personne ici ne sait ce que ça coûte | ce soir, pour la première fois, **je respire** |

Si Suno lisse ces trois lignes en les alignant sur le premier refrain, la
prise est à jeter : c'est tout ce que le morceau raconte. **À vérifier à
l'écoute avant de monter quoi que ce soit.**

## Réglages Suno

| Champ | Valeur |
|---|---|
| Mode | **Custom** — l'auto-génération réécrit les paroles |
| Instrumental | non |
| Style | le bloc ci-dessus, tel quel |
| Exclude styles | `trap, autotune, drill, reggaeton, EDM, brass band, country, aggressive` |
| Weirdness / Style influence | faibles — on veut une histoire lisible |

Générer **deux prises**, et choisir sur deux critères, dans cet ordre :

1. le pont retombe vraiment (batterie absente, voix parlée) ;
2. les trois lignes du tableau ci-dessus sont chantées telles qu'écrites.

## Après génération, avant montage

1. Mesurer le tempo réel (`scripts/tempo.py` du clip `le-clash`) — le BPM
   demandé n'est jamais celui obtenu.
2. Transcrire et aligner les paroles sur l'audio, pour faire tomber une coupe
   sur un mot et pas à peu près.
3. Construire la timeline sur les 60 plans, **redistribués selon l'histoire et
   non selon l'ordre des épisodes** : les plans de chaos sur le couplet 2, les
   gestes posés sur le couplet 3. Une source différente à chaque coupe, aucune
   fenêtre consommée deux fois.
4. Déposer par `publier_clip_musical` (master, court, paysage, carré, teaser,
   proxy), puis `lien_public` une fois la page YouTube en ligne.
