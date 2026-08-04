# Tutoriel — Mes commandes : QR code, site web, agent vocal (toutes vos commandes)

Module « Service ». Rush fourni : `Mes_commandes_Qrcode_Site_web_Agent_vocal.mp4`
(1920x828, 25fps, 56,52 s). Intro fournie : `RETROUVER TOUTES MES COMMANDES QR / WEB / VOCAL.jpg`.
Outro CTA générique (réutilisée telle quelle).

Pas d'avatar sur ce rush — VO ElevenLabs (Adam FR, `TGAegA0zNRi8I6nUdq3i`) sur toute la vidéo.

## Déroulé observé dans le rush

| t≈ | Écran |
|---|---|
| 0-2,5s | Page **« Mes commandes »** : stats (Total commandes, En attente, Aujourd'hui, Chiffre d'affaires), filtres (statut/canal/date), table N° commande / Client / **Canal** (Manuel, Vitrine, Sur place…) / Statut / Total / Date / Actions |
| 2,5s | Clic **« + Nouvelle commande »** |
| 2,85-17s | Modale : Client enregistré/Canal, Nom du client/Téléphone, Mode de service/Statut |
| 17-21,5s | Ajout d'un article (« Kefta d'agneau grillée », qté 1, 18,50€), Notes |
| 21,5-21,85s | Clic **« Créer la commande »** — bandeau *« Une facture et un devis liés seront générés automatiquement »* |
| 21,85-27s | Toast succès *« Commande créée (facture et devis générés automatiquement) »*, retour à la liste (32→33 commandes) |
| 27-33s | Clic sur une commande → popup détail (CMD-2026-00040, statut, client, articles, total, liens facture/devis) |
| 33-44s | Clic **« Modifier »** → modale : Client/Canal/Mode de service/Statut, Articles (quantité ajustée), Notes |
| 44-44,35s | Clic **« Mettre à jour »** |
| 44,35-48,5s | Toast succès *« Commande mise à jour »*, liste rafraîchie |
| 48,5-52,85s | Clic sur le menu **« ⋮ »** de la ligne → Détails / Modifier / **Supprimer** |
| 52,85-56,52s | Confirmation *« Supprimer cette commande ? CMD-2026-00040 »* — boutons Supprimer/Annuler |

## Voix off (11 lignes)

| # | Texte | Segment |
|---|---|---|
| N0 | Peu importe le canal — QR code, site web ou agent vocal — toutes vos commandes arrivent au même endroit. | intro + A |
| N1 | Ouvrez « Mes commandes » : la liste complète, avec le canal, le statut et le total de chaque commande. | A |
| N2 | Cliquez sur « Nouvelle commande » pour en créer une manuellement. | B(clic) |
| N3 | Renseignez le client, le canal, le mode de service, puis ajoutez vos plats. | C+D |
| N4 | Cliquez sur « Créer la commande » : la facture et le devis sont générés automatiquement. | E(clic)+F |
| N5 | Cliquez sur une commande pour voir son détail, ou sur « Modifier » pour ajuster les articles et le statut. | G+H |
| N6 | Cliquez sur « Mettre à jour » pour enregistrer les changements. | I(clic)+J |
| N7 | Besoin de la retirer ? Cliquez sur « Supprimer » et confirmez. | K+L |
| N8 | Vous pouvez aussi le faire depuis Claude : copiez ce prompt, remplacez les crochets. | séquence Claude étages 1+2 — **réutilisée telle quelle** |
| N9 | Collez-le dans la conversation : votre commande est créée en quelques secondes. | séquence Claude étage 3 |
| N10 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | carte de fin (CTA) — **réutilisée telle quelle** |

## Séquence Claude — outils MCP correspondants

`create_order(establishment_id, items, customer_name, channel, service_mode, table_id, notes)`
correspond exactement à « Nouvelle commande » (génère facture + devis automatiquement, comme
montré dans le rush). `update_order_status(establishment_id, order_id, status)` correspond à
la modification du statut dans « Modifier la commande ». Aucun outil MCP pour la suppression
d'une commande — pas de prompt pour cette action.

> Crée une commande pour [nom du client], canal [manuel / vitrine / agent_vocal / sur_place],
> mode [sur_place / emporter / livraison], avec [plat] x[quantité] à [prix]€, pour mon
> établissement FoodEatUp (ID [ID établissement]).

Deuxième prompt (fiche Lovable uniquement, `claudePrompts[]`) :

> Change le statut de la commande [numéro de commande] en [en_attente / confirmee /
> en_preparation / prete / livree / annulee] pour mon établissement FoodEatUp
> (ID [ID établissement]).

## Statut build (2026-08-04)

Durée livrée : **68,72 s** (la plus longue de la série à ce jour — rush dense : create + view
+ edit + delete, 4 actions). Checklist de compatibilité passée : H.264 High/yuv420p, AAC LC
48 kHz stéréo, faststart, 0 erreur de décodage, true peak **-7,22 dBFS**. Quelques lignes VO
(N1, N3) débordent légèrement de leur ancrage nominal mais restent dans leur segment
thématique (pas de chevauchement avec le clic suivant) — vérifié par simulation avant rendu
final.

## Fiche Lovable

- **slug** : `mes-commandes-tous-canaux`
- **title** : Mes commandes : QR code, site web, agent vocal (toutes vos commandes)
- **moduleSlug** : `service-commande` si disponible, sinon `configuration` (à vérifier côté
  Lovable — voir liste des modules du site)
- **subcategory** : Créer, consulter, modifier et supprimer une commande
- **whatItsFor** : Centraliser toutes vos commandes — QR code table, site vitrine, agent vocal
  ou saisie manuelle — dans une seule liste, avec canal, statut et total visibles d'un coup
  d'œil. Créez, modifiez ou supprimez une commande sans changer d'écran.
- **chefTip** : Le canal affiché sur chaque ligne (Manuel, Vitrine, Sur place…) vous dit
  immédiatement d'où vient la commande sans avoir à l'ouvrir — utile en coup de feu pour
  prioriser. Et avant de supprimer une commande, vérifiez sa facture/devis liés (visibles dans
  le détail) : une commande facturée qui disparaît laisse la facture orpheline, mieux vaut
  parfois la passer en « Annulée » plutôt que la supprimer.
- **chefTipAvatar** : `michael-chef-mascot.jpg`

## Statut

Vidéo montée et publiée à la demande de Michael (workflow complet demandé dans le même
message : montage, VO, séquence Claude, publication Lovable, mise à jour du dépôt).
