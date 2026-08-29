# Voix off — Saison 2 (30 phrases, une passe ElevenLabs)

**Voix de la saison** : `Adam - Instructor` — `TGAegA0zNRi8I6nUdq3i`, modèle `eleven_multilingual_v2`.
Validée sur l'épisode 01 : « FoodEatUp » est prononcé correctement (vérifié par retranscription ElevenLabs Scribe). Les prises sortent très bas (moyenne ≈ -36 dB) : normaliser chaque ligne avant montage.
Normalisation avant montage : **-16 LUFS / -1,5 dBTP**.

Même voix et mêmes réglages de stabilité / rythme sur les 30 épisodes. La voix off démarre à
2,0 s de l'outro et se termine avant 9,0 s : la fenêtre utile est de **7 s**
(≈ 105 caractères à un débit posé de 15 caractères/seconde).

C'est la voix off — et elle seule — qui prononce « FoodEatUp ». L'avatar Seedance ne le dit jamais.

## La ligne de transition (une seule prise pour les 30 épisodes)

> « Cette scène aurait pu être évitée ? »

Le pont entre le film et l'animation, identique sur les 30 épisodes : c'est la punchline qui transforme le gag en question. Elle est dite à 2,1 s de l'outro, sur le plan figé,
entre le clap « COUPEZ ! » et « Dans la vraie vie… ». Une seule prise ElevenLabs sert les 30 épisodes : la ligne ne change pas d'un épisode à l'autre. Changer `texte` et `voix_off` ici suffit à changer la signature de toute la saison.

Variantes validées, interchangeables sans retoucher le montage :

- « Cette scène aurait pu être évitée. »
- « Tout ça pour ça. »
- « On refait la scène ? »
- « Dommage. Il y avait plus simple. »
- « Cette scène n'existe pas chez eux. »
- « Scène coupée au montage. »
- « Vous auriez fait mieux ? »
- « Personne n'était obligé de vivre ça. »

## Les 30 lignes d'épisode

| # | Épisode | Phrase | Car. | ≈ durée |
|---|---|---|---|---|
| 01 | Le duel | Deux clients, une table ? Avec FoodEatUp, la réservation vérifie la place avant vous. | 85 | 5.7 s |
| 02 | Le contrôle | Le contrôle d'hygiène ? Avec FoodEatUp, chaque relevé est daté, rangé, prêt à montrer. | 86 | 5.7 s |
| 03 | Le critique | Le vrai critique, c'est chaque client. FoodEatUp réunit tous vos avis et vous aide à répondre. | 94 | 6.3 s |
| 04 | Le brunch des zombies | Le rush du dimanche n'est pas une invasion. FoodEatUp met tout le monde en file et remplit la salle table par table. | 116 | 7.7 s ⚠️ |
| 05 | Le casse | La clôture de caisse, c'est deux minutes, pas deux heures. FoodEatUp calcule l'écart pour vous. | 95 | 6.3 s |
| 06 | Le monstre | Dix, c'est dix. FoodEatUp fixe l'unité, la quantité et la date avant que le camion recule. | 90 | 6 s |
| 07 | La bombe | Un allergène, ça se sait avant de servir. FoodEatUp l'affiche sur chaque recette et sur votre site. | 99 | 6.6 s |
| 08 | Le documentaire | Vos clients font votre pub. FoodEatUp la récupère : la photo, l'avis, les points de fidélité. | 93 | 6.2 s |
| 09 | Le sous-marin | Chaque plat, chaque poste, chaque minute : l'écran cuisine FoodEatUp remplace les tickets et le ping. | 101 | 6.7 s |
| 10 | La boucle | Comptez une fois. FoodEatUp compte le reste, à chaque vente, à chaque livraison. | 80 | 5.3 s |
| 11 | La VAR | Les heures, on ne les discute plus, on les voit. Pointage, planning et contrat au même endroit. | 95 | 6.3 s |
| 12 | Le casting | Une offre, des candidatures classées, un statut par personne. Recruter sans courir après les CV. | 96 | 6.4 s |
| 13 | Le bouton rouge | Envoyez à la bonne personne, pas à toute la ville. FoodEatUp segmente vos clients et vous montre le retour de chaque campagne. | 126 | 8.4 s ⚠️ |
| 14 | Le naufrage | La terrasse ferme, la salle s'organise. Avec le plan de salle FoodEatUp, vous replacez tout le monde en trente secondes. | 120 | 8 s ⚠️ |
| 15 | Le procès | Chaque plat est noté sur la bonne table, à la bonne heure. Avec FoodEatUp, la note parle d'elle-même. | 101 | 6.7 s |
| 16 | La cave | Vos factures ne dorment plus à la cave. FoodEatUp affiche ce qui est payé, ce qui attend, et ce que ça vous coûte. | 114 | 7.6 s ⚠️ |
| 17 | Le round | Trois cents crêpes, c'est un plan de production. FoodEatUp calcule les ingrédients, prévient ce qui manque et met le stock à jour. | 130 | 8.7 s ⚠️ |
| 18 | Les douze | Douze ou cinquante, tout est écrit : la demande, le devis, la salle, la facture. FoodEatUp gère vos privatisations de bout en bout. | 131 | 8.7 s ⚠️ |
| 19 | La course-poursuite | Livrez là où vous livrez, pas plus loin. FoodEatUp définit vos zones, vos frais, et suit chaque commande. | 105 | 7 s |
| 20 | Les vampires | Le jour, l'heure, la remise, les boissons : tout est réglé d'avance. Quand ils sortent, FoodEatUp est déjà prêt. | 112 | 7.5 s ⚠️ |
| 21 | Le génie | Douze personnes, une note, zéro migraine. FoodEatUp divise la note par article, par personne ou en parts égales. | 112 | 7.5 s ⚠️ |
| 22 | Le poker | Chaque plat a un coût, une marge, un prix juste. FoodEatUp les calcule avant que vous misiez. | 93 | 6.2 s |
| 23 | La mémoire | Ses habitudes, vous les connaissez, même sans mémoire. FoodEatUp garde l'historique, les préférences et la fidélité de chaque client. | 133 | 8.9 s ⚠️ |
| 24 | La carte au trésor | Une commande, ça ne s'envole pas. Avec FoodEatUp, elle part de la table à la cuisine en une seconde. | 100 | 6.7 s |
| 25 | Les traders | Le téléphone répond tout seul. L'agent vocal FoodEatUp prend la réservation ou la commande pendant que vous servez. | 115 | 7.7 s ⚠️ |
| 26 | Le détective | Qui, quoi, quand : c'est écrit. Le plan de nettoyage FoodEatUp enregistre chaque action, pas besoin de détective. | 113 | 7.5 s ⚠️ |
| 27 | Le super-vilain | Un congé validé, un planning à jour, un samedi couvert. FoodEatUp vous prévient avant que vous signiez. | 103 | 6.9 s |
| 28 | Le jeu télé | La roue tourne, les lots sont limités, le stock suit. La fidélité FoodEatUp, c'est du jeu avec des règles. | 106 | 7.1 s ⚠️ |
| 29 | Les gangsters | L'ardoise est numérique : elle ne s'oublie pas, elle ne s'envole pas. Solde, historique, règlement, dans FoodEatUp. | 115 | 7.7 s ⚠️ |
| 30 | La cérémonie | Trente films. Un restaurant. Un seul système. FoodEatUp. | 56 | 3.7 s |

⚠️ = dépasse la fenêtre. Le texte du brief est conservé tel quel ; une variante courte est
proposée ci-dessous pour ces épisodes — à valider avant d'enregistrer la voix.

| # | Épisode | Variante courte proposée | Car. | ≈ durée |
|---|---|---|---|---|
| 04 | Le brunch des zombies | Le rush du dimanche n'est pas une invasion. FoodEatUp met tout le monde en file et remplit la salle. | 100 | 6.7 s |
| 13 | Le bouton rouge | Envoyez à la bonne personne, pas à toute la ville. FoodEatUp segmente et mesure vos campagnes. | 94 | 6.3 s |
| 14 | Le naufrage | La terrasse ferme, la salle s'organise. Avec FoodEatUp, vous replacez tout le monde en trente secondes. | 103 | 6.9 s |
| 16 | La cave | Vos factures ne dorment plus à la cave. FoodEatUp affiche ce qui est payé et ce qui attend. | 91 | 6.1 s |
| 17 | Le round | Trois cents crêpes, c'est un plan de production. FoodEatUp calcule les ingrédients et suit le stock. | 100 | 6.7 s |
| 18 | Les douze | Douze ou cinquante : la demande, le devis, la salle, la facture. FoodEatUp gère vos privatisations. | 99 | 6.6 s |
| 20 | Les vampires | Le jour, l'heure, la remise : tout est réglé d'avance. Quand ils sortent, FoodEatUp est prêt. | 93 | 6.2 s |
| 21 | Le génie | Douze personnes, une note, zéro migraine. FoodEatUp divise par article, par personne ou en parts égales. | 104 | 6.9 s |
| 23 | La mémoire | Même sans mémoire, vous connaissez ses habitudes. FoodEatUp garde l'historique et la fidélité. | 94 | 6.3 s |
| 25 | Les traders | Le téléphone répond tout seul. L'agent vocal FoodEatUp prend la réservation pendant que vous servez. | 100 | 6.7 s |
| 26 | Le détective | Qui, quoi, quand : c'est écrit. Le plan de nettoyage FoodEatUp enregistre chaque action. | 88 | 5.9 s |
| 28 | Le jeu télé | La roue tourne, les lots sont limités, le stock suit. La fidélité FoodEatUp, c'est réglé. | 89 | 5.9 s |
| 29 | Les gangsters | L'ardoise est numérique : elle ne s'oublie pas. Solde, historique, règlement, dans FoodEatUp. | 93 | 6.2 s |

---
Fichier généré par `scripts/build.mjs`, ne pas éditer à la main.
