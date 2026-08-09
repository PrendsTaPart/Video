# Configurer ses horaires et réservations

**Fiche** `configurer-horaires-et-reservations-site` · module `site-web-vitrine` · identifiant de série `t13`

> Ouvrir la réservation en ligne sans se retrouver complet à tort.

⚠️ **Film sans rush.** Ce tutoriel n'a pas de capture d'écran : il est en motion
design assumé. Aucun plan ne prétend montrer le produit — une planche
schématique dit « voici l'étape et ce qui compte », là où une fausse interface
prétendrait « voici l'écran ». Le jour où le rush existe, le film est remplacé ;
ce script, lui, reste.

## À quoi ça sert (texte de la fiche)

Les horaires du site ne sont pas un affichage : ce sont eux qui ouvrent et ferment les créneaux de réservation. Une coupure oubliée l'après-midi, et le site accepte des tables à quinze heures.

## Marche à suivre (texte de la fiche)

1. Saisissez vos horaires jour par jour, coupures comprises.
2. Activez la page réservations, puis publiez-la : tant qu'elle est en brouillon, elle n'existe pas pour le client.
3. Réglez la durée d'un couvert et la capacité : c'est ce qui détermine combien de tables un créneau accepte.
4. Vérifiez les disponibilités réelles sur une date donnée avant d'annoncer l'ouverture.
5. Contrôlez enfin le domaine : une page publiée sur un domaine non validé reste invisible.

## Astuce du chef

Publiez la page réservations un jour de fermeture. Vous verrez les créneaux se fermer d'eux-mêmes — c'est la meilleure preuve que les horaires sont bien pris en compte.

## Voix off

Adam - Instructor (`TGAegA0zNRi8I6nUdq3i`), `eleven_multilingual_v2`, français.

| # | Texte |
|---|---|
| N0 | Les horaires du site ne sont pas un affichage : ce sont eux qui ouvrent et ferment les créneaux. |
| N1 | Saisissez-les jour par jour, coupures comprises. |
| N2 | Activez la page réservations, puis publiez-la. En brouillon, elle n'existe pas pour le client. |
| N3 | Réglez la durée d'un couvert et la capacité : c'est ce qui détermine combien de tables un créneau accepte. |
| N4 | Vérifiez les disponibilités réelles sur une date avant d'annoncer l'ouverture. |
| N5 | Et contrôlez le domaine : une page publiée sur un domaine non validé reste invisible. |
| CTA | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! |

## Frise des jalons

**horaires** → **publier** → **capacité** → **domaine**

## Outils MCP correspondants

- `get_site_status`
- `toggle_site_page`
- `reservation_availability`
- `get_domain_status`

## Prompt Claude

> Donne-moi l'état du site de l'établissement [ID] — pages publiées, URL, domaine — puis les disponibilités de réservation pour le [DATE].
