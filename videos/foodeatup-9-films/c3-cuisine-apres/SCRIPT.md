# C3 · Cuisine — après le service

Troisième film de la série, et dernier du parcours cuisine. Même grammaire
que C1 et C2 : fond crème de la charte du site, cadre écran 1560 px, coches
orange en rangée sous l'écran, liseré cuisine `#059669`.

Couvre les 11 étapes de la phase « après » du parcours cuisine, 14h30 →
23h00 (`src/data/journees.ts`). Le film a deux mouvements — la fermeture du
midi, puis celle du soir — et la voix off marque la coupure.

## Voix off (verbatim)

Quatorze heures trente. Le service est fini. Ce qu'il reste sur les plans de
travail, personne ne s'en souviendra demain. Sauf si je l'écris maintenant.

Chaque reste reçoit sa date limite. Le plat, la quantité, l'équipement de
stockage. J'imprime mes étiquettes, je les colle, et le frigo redevient
lisible pour tout le monde.

Ce qui est parti en pertes, je le saisis. Ce qui a été transformé aussi. Mon
stock du soir n'est pas une estimation, c'est un relevé.

Ma traçabilité du midi se referme en trois gestes. Je pointe ma coupure.

Vingt-deux heures quinze. Le vrai travail de fermeture commence.

Mêmes étiquettes, mêmes DLC, mêmes pertes. Puis je pointe mes zones de
nettoyage, une par une, au fur et à mesure.

Une photo. L'intelligence artificielle regarde à ma place et me dit ce qui
n'est pas propre. Pas le lendemain matin : maintenant, quand je peux encore
y retourner.

Ma check-list de conformité, mon dernier relevé de températures.

Vingt-trois heures. Je pointe ma sortie. Ma journée entière est écrite, et je
n'ai rien recopié.

## Étapes couvertes

| Heure | Étape | Écran |
|---|---|---|
| 14h30 | Je pose les DLC sur mes restes | DLC |
| 14h35 | J'imprime mes étiquettes de stockage | ETIQUETTES |
| 14h45 | Je saisis mes pertes et mouvements de stock | STOCK |
| 14h55 | Je trace mon service | TRACA |
| 15h00 | Je pointe ma coupure | POINTAGE |
| 22h15 | DLC, étiquettes et pertes de fin de service | (repris — la voix le dit, le carton de nuit tient l'image) |
| 22h30 | Je pointe mes zones de nettoyage | NETTOYAGE |
| 22h40 | Une photo, l'IA contrôle mon nettoyage ★ | PHOTO-IA |
| 22h45 | Ma check-list hygiène de fermeture | CONFORMITE |
| 22h50 | Dernier relevé de température | TEMPERATURE |
| 23h00 | Je pointe ma sortie | POINTAGE |

Les onze étapes ont toutes une source disponible, ce qui n'était le cas ni
pour C1 ni pour C2. Deux nuances tout de même : les gestes de 22h15 répètent
littéralement ceux de 14h30, donc le film les dit sans les remontrer — c'est
le propos, pas une économie ; et le pointage de la coupure (15h00) partage
l'écran de pointage montré à 23h00, faute de place dans une scène de 4,57 s
qui porte déjà la traçabilité.

## Sources écran

| Réf | Tutoriel | Durée |
|---|---|---|
| `DLC` | `foodeatup-dlc-tuto-v1` | 44,48 s |
| `ETIQUETTES` | `imprimer-ses-etiquettes-v1` | 61,68 s |
| `STOCK` | `foodeatup-mouvement-stock-tuto-v1` | 52,20 s |
| `TRACA` | `foodeatup-tracabilite-simplifiee-tuto-v1` | 47,96 s |
| `NETTOYAGE` | `pointer-ses-actions-de-nettoyage-v1` | 46,52 s |
| `PHOTO-IA` | `foodeatup-nettoyage-ia-tuto-v1` | 28,00 s |
| `CONFORMITE` | `foodeatup-conformite-tuto-v1` | 52,48 s |
| `POINTAGE` | `pointer-son-service-cote-employe-v2` | 43,96 s |
| `TEMPERATURE` | `foodeatup-temperature-tuto-v1` | 37,68 s |

`PHOTO-IA` ne dure que 28 s : la fenêtre utile y est plus étroite qu'ailleurs
(10 % → 65 % = 2,8 → 18,2 s). C'est le plan clé du film, à découper avec soin.
