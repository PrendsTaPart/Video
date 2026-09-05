# S01E03 — « Le visage qu'elle a choisi »

Série **Michael remonte le temps**. Une minute, 1080×1920, 30 ips.
Trente secondes de film — le graveur d'Alexandrie, la frappe, le pot scellé — puis la queue
animée de la série : trois secondes de transition, vingt de méthode, sept de hook.

**Aucune vidéo n'a été générée.** Les trois plans existaient déjà dans la bibliothèque
Higgsfield et ont été récupérés par MCP.

> **Le brief était écrit en 45 s ; l'épisode sort en 60 s.** C'est la règle de série fixée
> après l'épisode 2 — 30 s de film, 3 s de transition « COUPEZ », 20 s de méthode, 7 s de
> hook de fin. Le bloc film et tous ses réglages sont ceux du brief ; seule la queue suit
> le nouveau format, comme pour les épisodes 1 et 2.

## Les livrables

| Fichier | Durée | Pour quoi |
|---|---|---|
| `deliverable/S01E03-cleopatre-60s.mp4` | 60 s | le film complet |
| `deliverable/S01E03-cleopatre-30s.mp4` | 30 s | le bloc film seul — TikTok et Reels |
| `deliverable/S01E03-cleopatre-30s-queue.mp4` | 30 s | transition + méthode + hook |
| `deliverable/S01E03-cleopatre-vignette.jpg` | — | image à 00:25,0 |

Tous autour de −14,9 LUFS, fondu de 0,5 s en sortie.

## Le bloc film — 00:00 → 00:30

| Plan | Higgsfield | Scène | Réplique |
|---|---|---|---|
| P1 | `088e5eca` | Atelier monétaire du palais, le burin dans la matrice | « Il était une fois une reine qui voulait choisir son visage… » |
| P2 | `0684bfeb` | La frappe, puis la matrice pressée dans la cire | « Une seule matrice. Mille pièces. Et le même sceau sur chaque pot. » |
| P3 | `8ad6d27b` | La nuit tombée : la matrice, les trois pièces, le pot | « Deux mille ans plus tard, il ne reste rien d'elle… » |

Raccords francs à 10,0 et 20,0 s. Accroche « Elle n'a jamais posté. On connaît son visage. »
de 00:00,3 à 00:03,0. Sous-titres brûlés, deux lignes et sept mots par ligne au plus.

**L'accent du marteau est à 11,9 s, pas à 12,6.** Le brief demande trois images de noir
« sur le second coup de marteau » et annonce 12,6 s. La mesure dit autre chose : entre 1 et
5 s du plan 2, les deux coups sortent à 1,5 s (−8,3 dB) et 1,9 s (−5,5 dB), soit 11,5 et
11,9 s de film ; à 12,6 s il ne reste que −14 dB. L'accent est donc calé sur le second coup
réel, à 11,9 s — ce que le plan demande en toutes lettres. Le son n'est pas touché : l'image
saute, le son continue.

**Les sous-titres sont montés à y = 1110.** À 1250, la hauteur héritée de l'épisode 2, ils
tombaient sur le sceau de cire — donc sur l'emblème de l'annonceur. Le défaut s'est vu en
montant un emblème d'essai ; il est corrigé.

### L'emblème dans le sceau

Aucune marque fournie : **le sceau reste lisse et rien n'est incrusté.** Déposer une PNG à
fond transparent dans `assets/annonceur/embleme.png` l'active. Elle est alors posée avec un
relief — une copie sombre et floue décalée de cinq pixels fait le creux, et l'emblème passe
à 82 % d'opacité pour que la matière de la cire se lise à travers. Le mécanisme a été
éprouvé avec un emblème d'essai avant d'être livré, pas seulement écrit.

Deux écarts au brief, tous deux mesurés :

**La fenêtre commence à 27 s, pas à 24.** Avant 27 s la perche finit sa montée et le pot
n'est pas encore posé : à 24,5 s on ne voit que son col, le sceau est hors champ. Y poser un
emblème l'aurait fait flotter dans le vide.

**Le suivi est relevé à l'œil.** Le suivi colorimétrique du module a été essayé et ne tient
pas sur ce plan : le brasero est la source principale et inonde tout l'établi de la même
teinte que la cire, si bien que la boîte détectée fait mille pixels de large là où le sceau
en fait deux cent soixante. Sur 27 → 30 s le plan est verrouillé et le sceau ne bouge pas :
deux points suffisent. `npm run suivre` redessine la boîte sur trois images pour vérifier.

## La queue animée — 00:30 → 01:00

Elle vient de `../module-methode-rapidocms`. Cet épisode n'y apporte que deux lignes de
voix off, toutes deux lues au débit naturel :

| Rôle | Créneau | Texte |
|---|---|---|
| Ouverture | 00:33 → 00:35 | « Votre image, partout la même. » |
| Punchline | 00:53,8 → 00:58,8 | « Elle, elle a choisi son visage. Vous, vous avez RapidoCMS. » |

L'ardoise de la transition porte **SCÈNE 3**.

## Les faits

`episode.json` porte sous `faits` les six points que l'épisode avance : l'innovation de
Cléopâtre VII qui met son image là où ses prédécesseurs mettaient des divinités, le portrait
volontairement non idéalisé, les tétradrachmes d'Antioche sans face principale, la double
fonction propagande et solde, la circulation jusqu'à Patras, et le fait qui porte la chute —
les monnaies sont la seule image réaliste de la reine qui nous reste.

## Ce qui n'a pas été fait

**L'épisode n'est pas déclaré au catalogue**, comme pour les épisodes 1 et 2 : le vocabulaire
demandé est celui du catalogue Social, pas celui de RapidoCMS, et la série n'existe dans
aucun des deux. La réponse à la question était « on verra plus tard ».
