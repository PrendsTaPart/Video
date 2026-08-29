# « Il était une fois un restaurant » — chanson (Suno)

La chanson est la seule source sonore du clip : l'audio des rushes n'est jamais repris.
Une fois générée, déposer le fichier ici sous le nom **`chanson.mp4`** (ou `chanson.mp3`),
puis lancer `python3 scripts/run_all.py`.

## Style / Description

```
Cinematic French pop ballad turning anthemic. 92 BPM, key of A minor moving to C major
at the final chorus. Intro: solo felt piano, room noise, distant kitchen clatter.
Verses: close-miked male baritone, intimate, almost spoken, upright bass and brushed drums.
Pre-chorus: strings swell, subtle synth pad. Chorus: full organic drums, layered backing
vocals, warm analog bass, wide reverb. Bridge: everything drops to piano and one voice.
Final chorus: choir, handclaps, brass accents, euphoric but restrained. Outro: back to
solo piano and the same room noise as the intro. Clean modern production, no autotune,
emotional and cinematic, French lyrics, storytelling.
```

**Titre** : `Il était une fois un restaurant`

## Paroles

```
[Intro]
(piano seul, bruit de salle vide)
Sept heures du matin, et personne

[Couplet 1]
Le bac est vide un vendredi
La carte date d'avant-hier
J'ai le carnet, j'ai le tableau
Et tout le reste est dans ma tête
Six tables et une mémoire
Un téléphone qui sonne dans le vide
Une table de douze qui n'existait pas
Et minuit qui ne retient rien

[Pré-refrain]
La pile grandit toute seule
Le quinze du mois qui suit
J'éteins la lampe, je ferme la porte
Et je recommence demain

[Refrain]
Il était une fois un restaurant
Quatre hommes, un seul vendredi soir
Le chef, le serveur, le patron
Et celui qui cherchait où aller
Il était une fois un restaurant
Qui parlait tout seul dans le noir
Et puis quelqu'un a décroché
À la première sonnerie

[Couplet 2]
Il cherche où aller ce soir-là
La carte date de mardi
Personne ne décroche nulle part
Il marche encore sous la pluie
Puis une voix, dix-huit heures quarante
La salle le voit à quarante et une
La cuisine l'apprend, le bureau le compte
Et rien de tout ça ne fait de bruit

[Pré-refrain]
Le plan de salle se remplit tout seul
Le planning tient avant samedi
La table était prête à son nom
Et le prénom du fils aussi

[Refrain]
Il était une fois un restaurant
Quatre hommes, un seul vendredi soir
Le chef, le serveur, le patron
Et celui qui cherchait où aller
Il était une fois un restaurant
Qui parlait tout seul dans le noir
Et puis quelqu'un a décroché
À la première sonnerie

[Pont]
(piano seul, une voix)
Vingt heures quinze
Les quatre au même endroit
Vingt heures trente et une, le plat part
Vingt heures trente-deux
Il ne remarque rien
Et c'est exactement ça, le métier

[Refrain final]
Il était une fois un restaurant
Où plus personne ne criait
Le chef, le serveur, le patron
Et le client — c'était le même
Il était une fois un restaurant
Vingt-trois heures cinquante, le Z avant d'éteindre
Sept heures du matin, le lendemain
Et cette fois, il n'est pas seul

[Outro]
(piano seul, bruit de salle qui se remplit)
Il était une fois un restaurant
```

## Si Suno coupe le morceau en deux

Générer en deux passes (couplets 1 + refrain / pont + refrain final), recoller les deux
fichiers, puis déposer le résultat en `chanson.mp4`. Le montage se recale tout seul : les
sections de `song-structure.json` sont des **poids**, normalisés sur la durée réelle du
fichier livré, puis calés sur les temps forts détectés.

## Si le calage ne tombe pas juste

Les frontières de sections sont estimées (poids en mesures + calage sur les temps forts).
Pour un calage à la main, relever les timecodes réels à l'écoute et écrire
`work/sections.override.json` :

```json
{
  "sections": [
    { "id": "refrain1", "start_sec": 74.2, "end_sec": 118.9 },
    { "id": "pont",     "start_sec": 226.0, "end_sec": 236.4 }
  ]
}
```

puis rejouer `python3 scripts/run_all.py --from 03`.
