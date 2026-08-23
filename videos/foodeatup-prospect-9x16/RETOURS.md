# Retours et suites données

## Moody — 23/08, 16 h 27

| Retour | Suite donnée | État |
|---|---|---|
| « Tu peux même changer à la main chaque séquence » | Chaque scène est paramétrique : durée dans `build_mockups.py` (`SCENES`), contenu dans sa fonction `sN_frame`, b-roll dans `build_broll.py` (`S1_IMAGES` / `S7_IMAGES`). On modifie une scène et on rejoue une seule commande. | ✅ déjà le cas |
| « J'aurais ajouté le logo FoodEatUp au début et à la fin » | Sting d'ouverture **S0** ajouté (2,6 s) : le logo se pose, souligné d'un trait orange, avec la signature « la restauration, pilotée par l'IA ». La fin portait déjà le logo sur la carte CTA. | ✅ fait |
| « Comme on vise les franchises, j'aurais mis des images de snack / boulangerie type CHB, Tasty Crousty, Kyser » | Le b-roll bistro est remplacé par **4 photos verticales snack / boulangerie / borne** générées via RapidoCMS (`assets/rapidocms/`), animées en Ken Burns : comptoir de snack en rush, tacos/kebab au coup de feu, vitrine de boulangerie le matin, borne de commande tactile. La scène de clôture passe sur une équipe de snack en fin de service. | ✅ fait |

### Une réserve sur le point « franchises »

Les images reprennent **le format** de ces enseignes (comptoir de vente à emporter,
vitrine chauffante, tenue noire et casquette, borne tactile), mais **aucune marque
n'est identifiable** : ni logo, ni enseigne, ni signalétique lisible. Mettre en scène
CHB, Tasty Crousty ou Kyser dans une vidéo commerciale FoodEatUp les ferait apparaître
comme clients ou partenaires — ça demande leur autorisation écrite, et sans elle c'est
un usage de marque contestable. Si un accord existe avec l'une de ces enseignes, dis-le
moi : on refait les plans avec leur identité, et c'est même un argument bien plus fort.

## Voix off

Cinq voix françaises comparées sur la même ligne (`vo/essais/`) : Lucas (actuelle),
Adrien Clairon, Kael, Rémy, Yann. En attente du choix de Michael pour regénérer les
16 lignes — une variable dans `script/script.json`, puis `build_vo.py`.
