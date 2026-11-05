# Application de caisse mobile — rapport (05/11/2026)

## Audit des 6 vidéos existantes
L'application est toujours en version 0.21.0, celle du tournage. Ses écrans n'ont pas changé, donc aucune version `-v2` n'a été faite et les fiches existantes n'ont pas été touchées.

## Trois gestes ajoutés
Il s'agit des gestes que la série ne couvrait pas encore :
- réservations et liste d'attente ;
- tickets du jour ;
- rapport X et clôture.

Fabrication :
- **Écrans** : ceux de l'application, au format téléphone, tirés de son test de captures (restaurant fictif « Le Bistrot du Marché ») ;
- **Voix** : Adam (`eleven_v4`), une seule prise ;
- **Durée** : de 17 à 19 secondes par vidéo.

Publication :
- **RapidoCMS** : les 6 fichiers sont déposés et leurs adresses répondent 206 ;
- **Académie** : PR #12, fusionnée.

## À signaler
Le ticket de démonstration imprime le SIRET et le numéro de TVA de FoodEatUp SASU, l'éditeur du logiciel. Ce ne sont pas les données d'un client, et ils sont peu lisibles à l'échelle de la vidéo. Il serait toutefois plus propre que la démonstration de l'application utilise des mentions fictives.
