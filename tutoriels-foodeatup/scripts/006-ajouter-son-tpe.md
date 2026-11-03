# 006 — Ton TPE relié à la caisse

- Fiche : `ajouter-son-tpe` — Ajouter son terminal de paiement (TPE) (https://tutoriel.foodeatup.com/tutoriel/ajouter-son-tpe)
- Module : caisse-pos · Où tourner : Service › Intégrations › Terminaux de paiement
- Durée visée : 45-75 s · Voix : Adam `TGAegA0zNRi8I6nUdq3i`, ElevenLabs `eleven_v4`, une prise

## Accroche (3 premières secondes)
« Retaper le montant sur le terminal, c'est l'erreur à chaque coup de feu. »

## Plan de tournage (pour Mouna)
1. Écran de départ : Service › Intégrations › Terminaux de paiement.
2. Geste : donner un libellé « Comptoir » au terminal, le rattacher au poste de caisse.
3. Geste : sur une note, Paiement (F10) › Carte (TPE) › Envoyer au TPE.
4. Résultat à montrer 2 s : « Présentez la carte au terminal », puis le paiement accepté.
5. Plan de coupe : un terminal Smile&Pay qui affiche le montant.

## Voix off (texte envoyé à ElevenLabs)
[excited] Retaper le montant sur le terminal en plein coup de feu ? C'est là que l'erreur arrive. On l'évite.
Tu ouvres Service, Intégrations, Terminaux de paiement. Ton terminal est là. Donne-lui un nom qui parle : « Comptoir », « Terrasse ». Jamais son numéro de série !
Tu le rattaches à ton poste de caisse comme terminal par défaut.
Maintenant, sur une note : Paiement. Tu choisis Carte TPE, puis Envoyer au TPE.
[amazed] Le montant part tout seul sur le terminal. Le client présente sa carte… et le résultat revient dans la caisse. Rien à retaper !
[whispers] Le bouton Carte tout court, lui, c'est pour un terminal externe, en saisie manuelle.
Et si le terminal ne répond pas, la caisse garde la main : elle ne relance jamais un second débit sans vérifier.
Essaie-le dans ton mode école.

## Sous-titre de fin / appel à l'action
« Essaie-le dans ton mode école. »

## À vérifier avant de tourner
- Le test d'envoi au TPE déclenche un vrai paiement : le filmer sur un terminal de démo, jamais en école (appels sortants coupés) ni sur le TPE réel du restaurant 26 (CLAUDE.md : TPE réel en base locale).
- Libellés exacts « Carte (TPE) » et « Envoyer au TPE » dans PosPaymentModal.
