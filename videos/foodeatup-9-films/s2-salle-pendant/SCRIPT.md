# S2 · Salle — pendant le service

Deuxième film du parcours salle. Liseré salle `#F59E0B`, reste de la
grammaire commun.

Couvre les 12 étapes de la phase « pendant » du parcours salle, 12h00 →
19h00 (`src/data/journees.ts`).

## Le parti pris : trois étapes de caisse, un seul schéma

Trois des douze étapes appartiennent au module Caisse POS, qui n'est pas
encore tourné : l'encaissement au comptoir (12h10), la séparation d'addition
(13h30) et la remise (13h40). Plutôt que trois scènes maigres de deux
secondes, elles sont réunies en **un seul schéma animé** — une addition qui se
sépare, puis une remise qui s'applique — parce que la voix off les nomme dans
la même respiration et que c'est le même objet à l'écran : une note.

C'est aussi ce qui évite le piège inverse : trois schémas d'affilée feraient
basculer le film du documentaire vers l'infographie.

## Voix off (verbatim — à générer)

Midi. Premier client. Je le place, la table passe en occupée, et la commande
qui suivra sera déjà rattachée à cette table.

Le client scanne le QR de sa table et commande lui-même. Ça tombe en cuisine
sans passer par moi.

Toutes mes commandes, dans une seule file. La salle, le comptoir, le site, la
livraison. Je vois d'où ça vient et où ça en est.

Une commande de livraison tombe. Elle entre dans la même file que les autres,
avec la même horloge.

Treize heures. Deux couverts qui ne viendront pas. Je passe la table en
no-show, elle se libère pour le service.

Au comptoir j'encaisse. À cette table, je sépare l'addition en trois. Sur
celle-là, j'applique la remise du midi. Trois gestes, une seule note.

J'inscris un client à la fidélité. Il repart avec des points, pas avec une
carte en carton.

Et je valide une récompense sur une autre table.

Dix-huit heures trente. Je reprends mes réservations du soir. Dix-neuf heures,
je replace mes clients. Le deuxième service commence, et la salle sait déjà
où elle va.

## Étapes couvertes

| Heure | Étape | Écran |
|---|---|---|
| 12h00 | J'accueille et je place mon premier client | PLACER |
| 12h05 | Le client commande en scannant le QR ★ | QRTABLE |
| 12h10 | Je prends une commande au comptoir | 🎬 schéma animé (Caisse POS) |
| 12h15 | Je suis mes commandes, tous canaux ★ | MULTI |
| 12h30 | Une commande de livraison tombe | MULTI (autre fenêtre) — voir ci-dessous |
| 13h00 | Je gère un no-show | NOSHOW |
| 13h30 | Je sépare une addition | 🎬 même schéma animé |
| 13h40 | J'applique une remise ou un avoir | 🎬 même schéma animé |
| 13h50 | J'inscris un client à la fidélité | FIDELITE |
| 14h00 | Je valide une récompense fidélité | RECOMPENSE |
| 18h30 | Je reprends mes réservations du soir | RESAS |
| 19h00 | Je place mes clients du soir | PLACER (autre fenêtre) |

Les douze étapes sont montrées. Aucune n'est passée sous silence.

## ⚠️ Deux entrées fausses dans le catalogue, trouvées sur ce film

| Slug | URL cataloguée | Contenu réel |
|---|---|---|
| `centraliser-les-commandes-livraison` | `foodeatup-caroline-voix-tuto-v1` | **configuration de l'agent vocal Caroline** — prompt système, simulateur, téléphonie. Rien sur la livraison. |
| `retrouver-toutes-mes-commandes` | `foodeatup-predibot-previsions-tuto-v1` | pointe sur PrediBot. Non vérifié image par image, mais le nom ne correspond pas — à contrôler avant tout usage. |

Vérifié image par image pour le premier. Consigné dans `sources-video.json`,
section `mauvaisMapping`, avec celui déjà trouvé sur C2
(`gerer-une-commande-en-direct-kds`). **Trois mappings fautifs sur une
soixantaine vérifiés jusqu'ici** : il faut contrôler chaque source avant de
la monter, jamais se fier au slug.

## ⚠️ Une plage à éviter dans une source

`booster-la-fidelite-programme-v1` : entre 55 % et 65 % de la source,
l'enregistrement laisse apparaître **la fenêtre de l'application Claude** sur
le bureau. Une application tierce n'a rien à faire dans un film FoodEatUp —
prélever avant.

## Sources écran

| Réf | Tutoriel | Durée |
|---|---|---|
| `PLACER` | `foodeatup-placer-un-client-a-table-tuto-v1` | 38,44 s |
| `QRTABLE` | `foodeatup-qrcode-table-tuto` | 45,40 s |
| `MULTI` | `foodeatup-commandes-multicanal-tuto-v1` | 61,80 s |
| `NOSHOW` | `foodeatup-noshow-tuto-v1` | 44,12 s |
| `FIDELITE` | `booster-la-fidelite-programme-v1` | 53,36 s |
| `RECOMPENSE` | `foodeatup-gerer-recompenses-tuto-v1` | 70,64 s |
| `RESAS` | `foodeatup-reservations-jour-tuto` | 24,68 s |
