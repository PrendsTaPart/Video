# Voix off ElevenLabs — scripts et paramètres

## Choix de la voix

Au premier lancement, Claude Code appelle `ElevenLabs:list_agents` / la liste des
voix du workspace et sélectionne une voix française masculine, ton direct et
chaleureux (registre « collègue restaurateur », pas « présentateur télé »).

Écris l'ID retenu dans `config/voices.json` une fois pour toutes :

```json
{
  "voice_id": "<ID récupéré via list_voices>",
  "model_id": "eleven_multilingual_v2",
  "language": "fr",
  "settings": {
    "stability": 0.45,
    "similarity_boost": 0.75,
    "style": 0.35,
    "use_speaker_boost": true
  },
  "speed": 1.05
}
```

`stability` bas (0.45) = plus d'énergie et de variation, ce qu'il faut pour du
short-form. Au-dessus de 0.6 la voix devient plate.

**Coût maîtrisé** : ~340 caractères par épisode (blocs C+D+E) + la punchline
propre à l'épisode. Les blocs C, D et E sont **identiques sur les 30 épisodes** —
ils sont générés **une seule fois** et réutilisés. Seule la punchline change.
Total réel : 3 fichiers communs + 30 punchlines courtes.

---

## Blocs communs — générés UNE fois

### `vo/common/B-sting.mp3` — 1,2 s

```
FoodEatUp.
```
Prononciation : « foud-ite-eup ». Si ElevenLabs le lit mal, écrire
`Foude Ate Up.` dans le texte source.

### `vo/common/C-probleme-30.mp3` — cible 7,0 s (master 30 s)

```
Aujourd'hui, tu gères ton restaurant avec dix logiciels. Mille euros par mois. Et aucun ne se parle.
```

### `vo/common/C-probleme-45.mp3` — cible 11,5 s (LinkedIn 45 s)

```
Aujourd'hui, tu gères ton restaurant avec dix logiciels différents. Mille euros par mois. Et aucun ne communique avec les autres. Ta caisse ignore ton stock. Ton site ignore ta cuisine. Oublie tout ça.
```

### `vo/common/D-demo-30.mp3` — cible 9,0 s

```
Regarde. En un clic, ton site est prêt à vendre. Et il parle à ta caisse, à ton KDS, et il fait entrer le client dans ta boucle marketing.
```

### `vo/common/D-demo-45.mp3` — cible 12,5 s

```
Regarde. En un clic, ton site est prêt à vendre tes produits. Et le petit plus : il communique avec ton logiciel de caisse et ton KDS. Chaque commande fait entrer le client dans ta boucle marketing, automatiquement.
```

### `vo/common/E-closing-30.mp3` — cible 3,8 s

```
Avant, pendant, après le service. Prêt à augmenter ton chiffre d'affaires ?
```

### `vo/common/E-closing-45.mp3` — cible 4,8 s

```
FoodEatUp pilote ton restaurant avant, pendant et après le service. Alors, prêt à augmenter ton chiffre d'affaires ?
```

---

## Punchlines par épisode — `vo/punch/EPxx.mp3`

Placées à **5,0 s** dans le master 30 s (sur le beat comique du clip Higgsfield),
mixées avec ducking −8 dB du son diégétique.

| Épisode | Texte |
|---|---|
| EP01 | Sauf que lui, il est patient. Tes clients, non. |
| EP02 | Ça finit toujours par terre. |
| EP03 | Elle coule. On va la repêcher. |
| EP04 | Il gère mieux que ton logiciel actuel. |
| EP05 | Un seul outil, ça change tout. |
| EP06 | Enfin… c'était avant. |
| EP07 | Les quatre cents autres, on s'en occupe. |
| EP08 | Et si la compta se faisait toute seule ? |
| EP09 | Ton abonnement logiciel, par exemple. |
| EP10 | Mille euros par mois. Pour dix outils qui ne se parlent pas. |
| EP11 | Avec, tout arrive à bon port. |
| EP12 | Avec un KDS, il regarde son plat arriver. |
| EP13 | Un seul, ça suffisait. |
| EP14 | Lui au moins, il sait ce qu'il y a en stock. |
| EP15 | Une pièce bouge, tout s'écroule. |
| EP16 | On va refermer le robinet. |
| EP17 | Ni à ta marge. |
| EP18 | Sauve ton service, pas ton dos. |
| EP19 | Ça rebondit rarement tout seul. |
| EP20 | Tes vrais clients aussi devraient pouvoir. |
| EP21 | Un KDS, et le combat s'arrête. |
| EP22 | Pour dix logiciels qui ne se parlent même pas. |
| EP23 | Automatiser, oui. Mais bien. |
| EP24 | Récupère tes commandes en direct. |
| EP25 | Ça éclabousse. Et rarement toi. |
| EP26 | Prévois, au lieu de subir. |
| EP27 | Il suffit d'un truc mal placé. |
| EP28 | Tout arrive. Nulle part. |
| EP29 | Personne ne devrait travailler comme ça. |
| EP30 | Forme-le en un clic avec l'Académy. |

---

## Règle de calage

ElevenLabs ne garantit pas la durée exacte. Après génération, Claude Code mesure
avec `ffprobe` :

- Si le fichier dépasse la cible de **plus de 8 %** → regénère avec `speed` +0.05
  (max 1.15).
- Si l'écart reste > 8 % après deux essais → **allonge le bloc vidéo**, pas la
  voix. Une VO accélérée s'entend ; un plan tenu 0,5 s de plus, non.
- Si le fichier est plus court que la cible → laisse le silence en fin de bloc,
  ça respire.

Ne jamais couper une VO en plein mot pour tenir la timeline.
