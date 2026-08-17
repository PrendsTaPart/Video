# Générique d'ouverture, 5 s — à générer à la main dans Higgsfield

**Ce fichier est un prompt, pas une commande.** La règle du dépôt interdit
d'appeler Higgsfield pour produire un nouveau plan : le texte ci-dessous est à
coller dans l'interface, et le rendu à déposer dans `assets/generique/upeatfood-5s.mp4`.

## Ce que ce plan remplace

Le film ouvre aujourd'hui sur `logo_anime()` — le logo de marque zoomé sur
3,333 s, fabriqué en ffmpeg par `build-film.py`. C'est propre et ça tient, mais
c'est une plaque fixe : rien n'y bouge que l'échelle. Le générique demandé le
remplace par un vrai plan d'ouverture.

Contraintes à respecter pour qu'il se substitue sans retoucher le montage :

| | |
|---|---|
| durée | **5,0 s** |
| cadre | 1920 × 1080, 30 im/s |
| fin | l'image doit se stabiliser avant la dernière demi-seconde — le carton de titre enchaîne juste après |
| son | **aucun** — la piste est posée au montage (`bgm.mp3` couvre déjà l'ouverture) |

Le logo qui apparaît est `templates/logo_foodeatup.png`, la typo de la charte
est Poppins 800 (`templates/Poppins-800.ttf`).

## La charte, en valeurs exactes

Ce sont celles de `build-film.py`, à ne pas approximer :

- fond sable `#FAF6E3`
- encre `#0F1A23`
- accent orange `#FFA500`

## Le prompt

```
PLAN D'OUVERTURE DE FILM, 5 secondes, 1920 × 1080, 30 images par seconde,
format cinéma. AUCUNE VOIX, AUCUN TEXTE INCRUSTÉ, aucun sous-titre.

L'IDÉE — une salle de restaurant qui s'allume pour le service, filmée comme le
générique d'un studio : lent, tenu, sans effet. On ne montre personne. Le
restaurant est le personnage.

LE MOUVEMENT — un seul travelling avant très lent, au ras des tables, depuis le
fond de la salle vers le pass de la cuisine. La caméra ne tourne pas, ne
tremble pas, ne s'arrête pas brusquement : elle décélère sur la dernière
seconde et s'immobilise complètement avant la fin du plan.

CE QU'ON TRAVERSE, dans cet ordre —
  0,0 → 1,5 s : le noir se lève sur une salle éteinte, chaises encore
                retournées sur les tables, lumière bleutée de fin de nuit.
  1,5 → 3,0 s : les suspensions s'allument une par une en cascade vers le
                fond, chaude, ambrée ; les chaises sont maintenant en place,
                les nappes claires, une carafe d'eau prend la lumière.
  3,0 → 4,3 s : on approche du pass de la cuisine, inox propre, une lampe
                chauffante s'allume en orange ; buée légère.
  4,3 → 5,0 s : l'image se stabilise sur le pass, cadre net et immobile.

LA LUMIÈRE — bascule du bleu froid vers l'ambre chaud, franche mais continue,
jamais clignotante. La dominante finale doit être chaude, proche de #FFA500 sur
les sources, avec des blancs crème #FAF6E3 sur les nappes et des noirs profonds
#0F1A23 dans les coins du cadre.

LA MATIÈRE — bois sombre, laiton, inox brossé, textile crème. Grain de pellicule
fin, très léger flou d'objectif sur les bords, profondeur de champ courte. On
veut une image de long métrage, pas de publicité : pas de saturation excessive,
pas de reflets lenticulaires, pas de particules qui volent.

INTERDITS — aucun visage, aucune main, aucune silhouette humaine. Aucun texte,
logo ou chiffre dans l'image. Pas de coupe : un seul plan continu. Pas de zoom
numérique, pas de rotation, pas de mouvement de grue.
```

## Après le rendu

Déposer le fichier dans `assets/generique/upeatfood-5s.mp4`, puis dans
`build-film.py` remplacer l'appel à `logo_anime(marque)` par ce plan et porter
`T_LOGO` de 4,0 à 5,0.

⚠️ **Les minutages de la narration se recalculent après ce changement.** Le
générique rallonge l'ouverture de 1,667 s (le logo actuel rend 3,333 s), donc
les 66 répliques se décalent d'autant. `build-film.py` d'abord, puis :

```bash
python3 scripts/build-narration-film.py --recalculer
python3 scripts/build-film.py --narration assets/voix/conteur-film.mp3
```

Le script refuse de monter tant que les minutages n'ont pas été remis d'équerre,
donc l'oubli se signale tout seul.
