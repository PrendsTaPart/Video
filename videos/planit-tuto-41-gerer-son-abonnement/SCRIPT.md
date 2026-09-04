# Tutoriel 41 — Gérer son abonnement et ses factures

Fiche MCP `tutoriel_spec(numero: 41)`, slug `gerer-son-abonnement`.
Capture source : « Vidéo 41 — Factures et reçus de paiement » — 25,85 s, 392 × 852.

| Ligne | Rôle | Texte |
|---|---|---|
| N0 | présentation | Bienvenue dans l'Académie Plan'It. Aujourd'hui : votre abonnement et vos factures. Vous changez de formule et vous récupérez vos justificatifs sans écrire à personne. |
| N1 | écran de départ | Dans « Mes crédits IA », le solde s'affiche en haut : 342 crédits, plan Starter. |
| N2 | l'historique | En dessous, chaque crédit reçu est daté, avec son expiration. |
| N3 | l'accès | Plus bas, les formules — Starter, Pro — et « Voir mes factures ». |
| N4 | la liste | Chaque facture porte son numéro, son montant et la mention « Payée ». |
| N5 | retrouver | La recherche et les filtres — aujourd'hui, sept jours, trente jours — retrouvent une période. |
| N6 | télécharger | « Télécharger » passe par Stripe : vingt et un kilo-octets de PDF. |
| N7 | le résultat | Votre justificatif est prêt pour la comptabilité. |
| N8 | astuce (leo) | Regardez deux mois de consommation avant de changer de formule. |

Voix : ElevenLabs *Perle* `UaGvaD7NWzU5mJNoUqoY`, `eleven_multilingual_v2`.
Flux : `sKOYDZDaS0015NSEy5C1`.

## Données personnelles — ce qui a été masqué, et pourquoi

La capture montre la facture Stripe ouverte en PDF. Son en-tête porte des
données réelles : la raison sociale et son adresse postale, un numéro de
téléphone, le nom du client et son adresse e-mail. Rien de tout cela n'a sa
place dans un tutoriel public.

`assets/screencast.mp4` est donc une **version retravaillée** de la capture, pas
la capture brute. Un bloc de 292 × 66 pixels en (34, 248) est pixellisé à partir
de t = 23,5 s, au facteur 13 — assez pour que le texte soit irrécupérable. Ce qui
reste lisible : « Facture », le numéro `TZ8ZJOQI-0256`, les dates d'émission et
d'échéance, le montant « 9,99 € dus le 1 septembre 2026 », la ligne de
description et le total. C'est-à-dire tout ce que le tutoriel doit montrer.

La commande qui produit ce fichier :

```
ffmpeg -i <capture brute> -filter_complex \
  "[0:v]crop=292:66:34:248,scale=22:5:flags=neighbor,scale=292:66:flags=neighbor[px];\
   [0:v][px]overlay=34:248:enable='gte(t,23.5)'[v]" \
  -map "[v]" -map 0:a? -c:v libx264 -profile:v high -pix_fmt yuv420p -crf 18 \
  -c:a aac -b:a 128k assets/screencast.mp4
```

Deux passages sont **écartés du montage** plutôt que masqués :

- **11,7 → 14,3 s** — la page `pay.stripe.com` s'ouvre sur un écran noir sans
  contenu. Rien à montrer.
- **16,2 → 24,2 s** — retour sur un formulaire de connexion CRM, puis le panneau
  Téléchargements d'Android. Celui-ci liste des fichiers personnels sans rapport
  avec Plan'It (documents scolaires, domaines tiers). Aucun recadrage propre n'est
  possible : le passage est coupé.

## Écart entre la fiche et l'application

La fiche dit « Ouvrez Réglages puis "Facturation" ». L'application n'a pas
d'entrée « Facturation » : l'écran s'appelle **« Mes crédits IA »**, et les
factures s'atteignent par le lien **« Voir mes factures »**, à droite du titre
« Plans ». La voix off suit l'application.

## État

Le montage est prêt à être lancé, mais **les neuf lignes de voix n'ont pas pu
être générées** : l'API ElevenLabs répond « Your subscription has a failed or
incomplete payment. Complete the latest invoice to continue usage. » La lecture
du compte fonctionne toujours (les voix se listent) ; seule la génération est
bloquée. Une fois la facture ElevenLabs réglée, il suffit de générer les neuf
lignes ci-dessus dans `vo/` puis de lancer `python3 episode.py`.

## La capture 39 — ce qu'elle contient, et où elle pourrait aller

L'autre enregistrement livré, « Vidéo 39 — Solde et rechargement de crédits »
(1 min 53, 392 × 852), a été analysé image par image :

| Temps | Écran |
|---|---|
| 0 → 18 s | « Mes crédits IA » — plan **Free**, 42 crédits, historique, crédits reçus |
| 18 → 40 s | le web `plani-t.fr/billing?plan=starter` — « Vos crédits, réglés en ligne. », Mensuel / Annuel −20 %, Starter 9,99 €/mois ou 95,90 €/an, Pro 24,99 €, Business 69,99 €, recharges ponctuelles 500 crédits à 14,99 € et 2 000 à 49,99 € |
| 40 → 90 s | `checkout.stripe.com` — formulaire d'abonnement, 112,25 MAD par mois, bascule MAD / EUR |
| 90 → 96 s | « En cours de traitement », puis « Paiement confirmé » sur `plani-t.fr/billing/success` |
| 96 → 113 s | retour dans l'application : plan **Starter**, **342 crédits** |

**Bonne nouvelle sur la vie privée** : le paiement est fait dans
l'**environnement de test** de Stripe — le bandeau « Environnement de test » est
affiché en permanence, la carte est `4242 4242 4242 4242` (la carte de test
publique de Stripe), le titulaire est « Test demo ». Aucune donnée bancaire
réelle. La seule donnée personnelle est l'**adresse e-mail** du compte, visible
dans le champ « E-mail » du formulaire entre 53 et 90 s environ ; elle demande le
même traitement que les blocs de la facture.

**Où la placer.** Aucune fiche du catalogue ne porte « recharger ses crédits » ou
« s'abonner ». La fiche 40 « Comprendre ses crédits » est déjà en ligne depuis le
28/08 et son montage suit fidèlement son propre texte — la consommation, le coût
par action, l'historique — ce que cette capture ne montre pas. La remplacer la
rendrait moins juste, pas plus.

La fiche **41** est le seul foyer cohérent : sa promesse est « Vous changez de
formule et récupérez vos factures ». La capture 39 montre exactement le premier
membre de la phrase, la capture 41 le second. Proposition, à valider : monter la
41 sur les **deux captures concaténées** (39 puis 41), l'e-mail pixellisé sur la
première comme les blocs d'identité le sont sur la seconde.
