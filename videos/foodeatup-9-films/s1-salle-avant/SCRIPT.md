# S1 · Salle — avant le service

Premier film du parcours salle. Même grammaire que les trois films cuisine —
fond crème de la charte, cadre écran 1560 px, coches orange sous l'écran —
avec le **liseré salle `#F59E0B`** à la place du vert cuisine.

Couvre les 13 étapes de la phase « avant » du parcours salle, 09h30 → 11h45
(`src/data/journees.ts`).

## Ce que ce film raconte, et que les films cuisine ne racontaient pas

En cuisine, la journée commence par des gestes de conformité : pointer,
relever, tracer. En salle, elle commence par **des gens qui ont déjà essayé de
vous joindre pendant la nuit**. Le film s'ouvre là-dessus : les réservations
tombées à minuit, les appels pris par Caroline pendant que la salle était
vide. C'est le seul film de la série dont la première scène montre du travail
déjà fait par quelqu'un d'autre.

## Voix off (verbatim)

Neuf heures trente. La salle est vide, les chaises encore sur les tables. Mais
la journée, elle, a déjà commencé sans moi.

Je pointe, je récupère mes tâches. Et je regarde ce que la nuit a laissé.

Mes réservations du jour, dans l'ordre. Le nom, l'heure, le nombre de
couverts, la table.

Cette nuit, pendant que personne n'était là, Caroline a décroché. Je réécoute
les appels, je vérifie ce qu'elle a noté. Rien ne s'est perdu à onze heures du
soir sur un répondeur.

Un appel ce matin, une réservation de plus. Je l'ajoute, elle prend sa place
dans le service.

Ce soir je suis complet à vingt heures : je ferme le créneau. Personne ne
réservera une table qui n'existe pas.

La six est bancale, je la bloque. Elle disparaît du plan, et du site.

Je prépare mon plan de salle. Qui va où, avec combien de couverts, et à quelle
heure la table se libère.

Je vérifie les QR codes de mes tables. C'est par là que mes clients
commanderont tout à l'heure.

Onze heures quinze. Les commandes web sont déjà tombées. Je les regarde avant
d'ouvrir, pas pendant le coup de feu.

Onze heures quarante-cinq. Ma salle est prête, et je n'ai encore vu personne.

## Étapes couvertes

| Heure | Étape | Écran |
|---|---|---|
| 09h30 | Je pointe mon entrée | POINTAGE |
| 09h35 | Je récupère mes tâches du jour | TACHES |
| 09h40 | Je consulte mes réservations du jour ★ | RESAS |
| 09h50 | Je réécoute les appels pris par Caroline ★ | APPELS |
| 10h00 | J'ajoute une réservation reçue par téléphone | AJOUT-RESA |
| 10h10 | J'ouvre ou je ferme des créneaux | CRENEAUX |
| 10h20 | Je bloque une table indisponible | TABLES |
| 10h30 | Je prépare mon plan de table ★ | PLACER |
| 10h40 | Je vérifie les QR codes de mes tables | QRCODE |
| 11h00 | Je retire de la carte ce qui manque | ⬜ aucune fiche — non montré |
| 11h15 | Je vérifie les commandes web déjà tombées | WEB |
| 11h30 | Je prends ma pause repas | (partage l'écran de pointage) |
| 11h45 | J'ouvre mon fond de caisse | ⬜ à tourner — non montré |

Onze étapes sur treize sont montrées. Les deux manquantes sont dites par la
voix ou tues : le retrait de carte n'a pas de fiche, et le fond de caisse
attend le tournage du module Caisse POS.

## Sources écran

| Réf | Tutoriel | Durée | Remarque |
|---|---|---|---|
| `POINTAGE` | `pointer-son-service-cote-employe-v2` | 43,96 s | déjà utilisé en cuisine |
| `TACHES` | `lire-ses-notifications-v1` | 29,24 s | **1920×1020** — recadrage différent |
| `RESAS` | `foodeatup-reservations-jour-tuto` | 24,68 s | fourni par Michael, S3 le refuse |
| `APPELS` | `foodeatup-appels-reservations-tuto` | 36,08 s | |
| `AJOUT-RESA` | `foodeatup-reservation-tuto-v1` | 47,92 s | |
| `CRENEAUX` | `foodeatup-creneaux-reservation-tuto-v1` | 52,08 s | |
| `TABLES` | `foodeatup-gerer-tables-tuto-v1` | 64,80 s | |
| `PLACER` | `foodeatup-placer-un-client-a-table-tuto-v1` | 38,44 s | |
| `QRCODE` | `diffuser-son-qrcode-v1` | 43,36 s | |
| `WEB` | `foodeatup-commandes-multicanal-tuto-v1` | 61,80 s | à ne pas confondre avec `mes-commandes-tous-canaux`, utilisé en C2 |
