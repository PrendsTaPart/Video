# Plans tournés disponibles (bibliothèque Higgsfield)

Inventaire relevé le 2026-08-08. Ces plans sont **déjà générés et payés** : les
consulter avant toute nouvelle génération. Modèle `seedance_2_0`, 1280×720,
sans audio. Ils partagent trois personnages de référence — `<<<chef-hero>>>`,
`<<<serveur-hero>>>`, `<<<directeur-hero>>>` — donc la même personne traverse
toute la série, ce qui est exactement la promesse du film héros.

Récupération : `curl -sSL -o <fichier> "<url>"`. Puis **toujours** ré-encoder
au standard de la série avant de les incruster :

```bash
ffmpeg -i src.mp4 -vf "scale=1920:1080:flags=lanczos,fps=30,setsar=1" -an \
  -c:v libx264 -preset medium -crf 20 -pix_fmt yuv420p \
  -r 30 -g 30 -keyint_min 30 -sc_threshold 0 -movflags +faststart out.mp4
```

Le GOP court n'est pas cosmétique : voir NOTES §5 bis.4.

## Registre chaud / froid

La bibliothèque est déjà tournée dans les deux registres du volet « Avec /
Sans ». C'est la moitié du travail image du film héros qui est faite.

| Registre | Signature visuelle | Usage |
|---|---|---|
| **Avec** | lumière naturelle chaude, accent bleu, geste posé, profondeur de champ courte | les 9 films « avec », faces B du héros |
| **Sans** | gris plat, désaturé, couvert, expression résignée | les 9 miroirs « sans », faces A du héros |

Aucun plan « sans » ne montre d'interface tierce identifiable — conforme à la
contrainte juridique du §6.1 des NOTES.

## Inventaire

| Durée | Registre | Sujet | Sert à |
|---|---|---|---|
| 8 s | neutre | cuisine professionnelle déserte au petit matin, plan fixe | **C1 s1 (utilisé)**, ouverture héros |
| 6 s | neutre | salle de restaurant déserte, chaises sur les tables | S1 ouverture |
| 6 s | neutre | devanture du restaurant, lumières qui s'éteignent une à une | clôture héros |
| 4 s | neutre | macro cloche du passe qui vibre encore | **cloche du passe du film héros** |
| 8 s | avec | imprimante thermique déroulant un ticket Z | D3, S3 clôture de caisse |
| 6 s | avec | `chef-hero` scanne un code-barres au téléphone, faisceau bleu | C1 réception, C2 |
| 6 s | avec | `chef-hero` valide un ticket sur l'écran de cuisine | C2 service |
| 12 s | avec | `chef-hero` et un second cuisinier échangent, cadrage à égalité | C2, C3 |
| 6 s | avec | `serveur-hero` consulte un plan de salle sur tablette | S1 |
| 6 s | avec | `serveur-hero` accueille et installe un client | S2 |
| 8 s | avec | `directeur-hero` ouvre son portable, bureau rangé, matin | D1 |
| 6 s | avec | portrait `chef-hero`, lumière chaude de fin de journée | **C1 s8 (utilisé)** |
| 6 s | avec | portrait `serveur-hero`, même dispositif | S3 clôture |
| 6 s | avec | portrait `directeur-hero`, même dispositif | D3 clôture |
| 6 s | sans | `chef-hero` recopie des DLC à la main dans un cahier | **miroir C1** |
| 10 s | sans | `directeur-hero` recopie un chiffre entre sept onglets, le soir | **miroir D3**, face A du héros |
| 6 s | sans | trois tablettes dépareillées, câbles emmêlés, comptoir encombré | **miroir S2** |

Les trois portraits sont tournés au même dispositif (50 mm, hauteur d'œil,
lumière de fin de journée) : ils forment une série et doivent être montés
comme telle, jamais isolément.

## Ce qui manque encore

Aucun plan « sans » pour la salle en service ni pour la réception de
livraison, et aucun plan de transition jour/nuit pour le héros. À générer
quand ces films arriveront — pas avant, pour ne pas payer des plans qu'un
changement de scénario rendrait inutiles.
