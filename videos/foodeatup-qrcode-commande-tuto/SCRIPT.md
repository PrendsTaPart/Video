# Tutoriel — Commander par QR code (sur site)

Module Service Multi-Canal, slot Lovable déjà existant `commander-sur-site-qr-ou-vocal`
("Canaux de commande"), aujourd'hui en placeholder "en cours de tournage" — cette vidéo le
remplit (angle QR code ; l'agent vocal n'est pas montré dans ce rush).

Rush fourni par Michael : `assets/screen.mp4` (75,96 s, 1920x828 @25fps), cartes intro/outro
fournies (`assets/intro.jpg` = COMMANDER_PAR_QR_CODE, `assets/outro.jpg` = CTA identique aux
autres tutos, réutilisée telle quelle).

## Déroulé du rush (analyse frame par frame)

0–13 s : liste des réservations, modification d'une réservation (assignation de table) — hors
sujet pour ce tutoriel QR, **non repris au montage** (montage resserré sur le fil du sujet,
comme pratiqué sur le reste de la série).

13–25 s : menu de navigation → Configuration boutique → Plan de salle → sélection de la table
QA3 → panneau latéral (statut, "Changer le statut", bouton **"QR code de la table"**).

25–29 s : clic sur "QR code de la table" → modale avec le QR, le lien
(`http://127.0.0.1:8000/t/taufqa1e5zo5`), "Le client scanne pour voir sa commande et la
carte.", boutons Télécharger / Copier le lien.

29–37 s : bascule d'onglet navigateur (bruit d'enregistrement), **non repris**.

37–52 s : page client "Gosushi démo — Table QA3" (boutons "Appeler un serveur" / "Demander
l'addition"), carte par catégories (Entrée, Autres), ajout au panier au clic sur "+" : Pizza →
+California Roll 8 pcs → +Gyoza x6, récapitulatif panier + "Nombre de couverts" + bouton
"Commander · 40,80 €" qui se met à jour en direct.

52–55 s : clic sur "Commander" → toast "Commande transmise en cuisine !".

55–61 s : écran de suivi de commande `cmd-2026-00109` "Confirmée", "ENVOI N°1" avec chaque
plat "En attente", bouton "Payer l'addition · seul ou à plusieurs", section "Ajouter — envoi
n°2".

61–67 s : clic sur "Payer l'addition" → modale de partage (Tout payer 40,80 € / ÷2 / ÷3 / ÷4 /
montant libre) → sélection ÷4 → "Votre part : 10,20 €".

67–75,96 s : écran de paiement Stripe (Link, carte Visa enregistrée, "Payer 10,20 €",
"Paiement sécurisé Stripe — CB, Apple Pay, Google Pay"). Le rush s'arrête avant la confirmation
du paiement — le montage aussi (pas d'écran de succès inventé).

## Voix off (12 lignes)

| # | Texte | Ancrage |
|---|---|---|
| N0 | Commander sans appeler personne, juste avec un QR code sur la table ? C'est déjà prêt sur FoodEatUp. | carte d'intro |
| N1 | Depuis le plan de salle, sélectionnez une table et cliquez sur QR code de la table. | navigation + sélection table |
| N2 | Le lien s'affiche, prêt à télécharger ou à copier. Le client scanne pour voir sa commande et la carte. | modale QR |
| N3 | Sur son téléphone, le client retrouve la carte complète du restaurant, par catégories. | page client, carte |
| N4 | Il ajoute ses plats d'un simple clic : le récapitulatif se met à jour en direct. | ajout au panier |
| N5 | Un clic sur Commander, et la commande part directement en cuisine. | clic Commander + toast |
| N6 | Il suit le statut de chaque plat en temps réel, et peut ajouter un nouvel envoi à tout moment. | écran de suivi cmd-2026-00109 |
| N7 | Pour payer, un seul geste : tout régler, ou partager l'addition en deux, trois ou quatre. | modale de partage |
| N8 | Zéro attente, zéro erreur de commande : le client commande et paie à son rythme, sans mobiliser un serveur. | écran de paiement (bénéfice) |
| N9 | Vous pouvez aussi enregistrer une commande à table depuis Claude : copiez ce prompt, remplacez les crochets. | étage 1+2 Claude |
| N10 | Collez-le dans la conversation : la commande est créée en quelques secondes. | étage 3 Claude |
| N11 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | carte de fin (CTA) — **réutilisée telle quelle** depuis `foodeatup-commandes-multicanal-tuto/vo/N9.mp3` |

## Séquence Claude — module partagé

`mcp__FoodEatUp__create_order(establishment_id, items, customer_name, channel, service_mode,
table_id, notes)` correspond à la commande passée par le client via le QR code (canal
`vitrine`, mode `sur_place`, table renseignée) — c'est exactement ce que montre l'écran de
suivi (`cmd-2026-00109`, "Confirmée", facture/devis générés).

> Crée une commande pour la table [numéro de table], canal vitrine, mode sur_place, avec
> [plat] x[quantité] à [prix]€, pour mon établissement FoodEatUp (ID [ID établissement]).

Même texte côté fiche Lovable (`claudePrompt`). Pas d'outil MCP pour le paiement Stripe côté
client (fractionné ou non) ni pour la génération du lien QR lui-même (action client-side) : non
repris en prompt.

## Coordonnées mesurées (seuillage colorimétrique)

- "QR code de la table" (bouton bleu marque) : bbox (1398,470)-(1738,522), centre (1569, 495),
  taille ≈ (340, 52).
- "Commander · X €" (barre de panier bas d'écran) : bbox quasi pleine largeur
  (26,756)-(1872,808) — trop large pour un zoom-punch pertinent (le crop ~1600 px ne "punch"
  rien sur un bouton déjà pleine largeur), traité comme un cut simple, sans encadré.

## Statut publication

Remplit le slot Lovable préexistant `commander-sur-site-qr-ou-vocal` (module `service-commande`,
section "Canaux de commande", déjà présent en placeholder "en cours de tournage" avant cette
vidéo) — pas de nouvelle entrée à créer, mise à jour de l'entrée existante uniquement.
