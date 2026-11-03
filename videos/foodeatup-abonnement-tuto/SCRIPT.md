# Tutoriel — Choisir son abonnement FoodEatUp

Module 1 « CONFIGURATION », dossier Drive `3 - choisit votre abonnement`.
**Rebuild** : ce dossier contenait déjà une v1 (30s) d'une session précédente, qui avait
le même bug de lecture que la v1 de `foodeatup-inscription-tuto` (AAC 96kHz mono, pas de
faststart) et aucune animation. Michael a redéposé les mêmes assets sources ; refait
intégralement avec le pipeline actuel.

Durée livrée : **37,2 s** — H.264 High/yuv420p, AAC 48 kHz stéréo, faststart.
Audio : true peak **-7,3 dBFS** (mesuré sur le MP4 final).

## Voix off

| # | Texte | Durée | Placement |
|---|---|---:|---|
| N0 | Passer à un abonnement StockVision, c'est activer tout de suite HACCP, OCR et bien plus. | 5,75 s | carte d'intro |
| N1 | Choisissez le pack StockVision, OCR et HACCP. | 3,53 s | liste des packs |
| N2 | Le récapitulatif s'affiche : prix, facturation mensuelle, et sept jours d'essai gratuit. | 5,02 s | modal « Finaliser votre commande » |
| N3 | Cliquez sur Continuer vers le paiement, puis renseignez votre email. | 3,60 s | clic Continuer + page paiement |
| N4 | Entrez les informations de votre carte bancaire : numéro, date d'expiration, et le nom du titulaire. | 5,98 s | saisie carte |
| N5 | Un clic sur Démarrer la période d'essai, et c'est parti. | 3,06 s | clic Démarrer |
| N6 | Votre abonnement est activé, profitez-en dès maintenant ! | 2,64 s | confirmation |
| N7 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | 4,96 s | carte de fin (CTA) |

## Découpage

| Seg | Source | Sortie | Contenu |
|---|---|---:|---|
| intro | carte | 4,0 s | CHOISIR SON ABONNEMENT |
| A | 0,30 → 2,30 | 3,20 s | liste des 3 packs |
| B | 2,30 → 2,80 | 0,90 s | **zoom-punch** sur « Choisir ce pack » (1522, 693) |
| C | 3,00 → 7,40 | 4,30 s | récapitulatif de commande |
| D | 7,40 → 7,90 | 0,90 s | **zoom-punch** sur « Continuer vers le paiement » (1037, 707) |
| E | 10,20 → 14,00 | 2,80 s | page de paiement, email |
| F | 14,00 → 44,00 | 6,80 s | saisie carte bancaire |
| G | 44,00 → 44,50 | 0,90 s | **zoom-punch** sur « Démarrer la période d'essai » (1373, 641) |
| H | 54,00 → 56,80 | 3,60 s | « Abonnement activé ! » |
| outro | carte | 12,25 s (auto-étendue) | CTA |

Coupes volontaires : **8,0 → 10,2 s** (transition/chargement vide) et **44,5 → 54,0 s**
(spinner de traitement puis coche de validation intermédiaire — 9,5 s de temps mort avant
la vraie page de confirmation).

## Point de vigilance rencontré — script vocal trop long pour le déroulé

Première passe : les durées de segments ont été fixées "au jugé" avant de vérifier contre
la durée réelle des lignes VO. Résultat : chaque ligne dépassait légèrement son créneau,
et comme le placement des VO est **poussé séquentiellement** (jamais de chevauchement),
ce dépassement s'accumule ligne après ligne — tout l'excédent (~16 s) atterrit sur la
carte de fin, qui s'étirait à **22,46 s** de silence quasi total avant la ligne CTA.
Correctif en deux temps : raccourcir les 3 lignes les plus longues (N1, N2, N6) et
redonner de l'air aux segments correspondants. Résultat : extension ramenée à 12,25 s.
**Leçon pour la suite** : caler les durées de segment sur la longueur réelle des lignes
VO *avant* de lancer le montage, pas après.

## Animations

Mêmes principes que les deux premiers tutoriels : Ken Burns sur les cartes fixes, xfade
(0,28 s) à chaque raccord, bandeaux d'étape glissants, encadré orange pulsant sur chaque
clic. Aucun clip avatar dans ce dossier (voix ElevenLabs de bout en bout).
