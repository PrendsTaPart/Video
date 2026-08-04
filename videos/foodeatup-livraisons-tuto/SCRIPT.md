# Tutoriel — Suivre ses livraisons (statuts & dates)

Module StockVisionAI (menu « Gestion des livraisons »). Rush source : `assets/screen.mp4`,
1920x828, 25 fps, 44,46 s.

## Ce que montre le rush

1. `0-8s` — Page « Gestion des livraisons » : cartes livraison (Fournisseur, Prévu, Reçue/
   Mode de livraison, Prix, Statut).
2. `8-16s` — Filtre par statut via le menu déroulant « Toutes les livraisons » : En attente /
   Expédiée / Livrée.
3. `16-24s` — Clic sur le crayon à côté de « Prévu » → modale « Modifier la date de
   livraison » → nouvelle date → Enregistrer.
4. `24-32s` — Clic sur le crayon à côté de « Mode de livraison » → modale « Modifier le mode
   de livraison » (liste déroulante, ex. « Livraison standard ») → Enregistrer.
5. `32-44s` — Bouton « Marquer comme expédiée » → modale de confirmation « Confirmer le
   changement de statut ? » → Confirmer → statut mis à jour dans la carte.

## Pas de séquence Claude sur cette vidéo

Vérifié côté `mcp__Foodeatup__*` : `list_deliveries` est en lecture seule (aucun
`update_delivery_status`/`update_delivery_date`/`update_delivery_mode`). `update_order_status`
existe mais s'applique aux **commandes clients** (statuts `en_attente|confirmee|en_preparation|
prete|livree|annulee`) — objet différent des livraisons fournisseurs montrées ici (statuts
`en_attente|expediee|livree`, + édition date/mode). Aucun outil ne correspond 1:1 aux actions du
rush → pas de `claudePrompt` inventé, même règle que sur `foodeatup-unites-tuto`.

## Voix off proposée (7 lignes) — À VALIDER AVANT GÉNÉRATION AUDIO

| # | Texte | Ancrage |
|---|---|---|
| N0 | Suivre ses livraisons sur FoodEatUp, en toute simplicité. | carte d'intro |
| N1 | Filtrez-les par statut : en attente, expédiée, ou livrée. | filtre menu déroulant |
| N2 | Modifiez la date prévue en un clic sur le crayon. | modale date |
| N3 | Changez aussi le mode de livraison à tout moment. | modale mode de livraison |
| N4 | Marquez une livraison comme expédiée, puis confirmez : le statut se met à jour aussitôt. | bouton + confirmation |
| N5 | Vous gardez une vue claire sur chaque commande fournisseur, du départ à la réception. | bénéfice |
| N6 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | carte de fin (CTA, réutilisable) |

N6 réutilisable tel quel depuis un `vo/N*.mp3` existant de la série (texte CTA identique) —
zéro crédit ElevenLabs.
