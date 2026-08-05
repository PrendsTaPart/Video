# Tutoriel — Débloquer les Avis clients (activer l'option Avis & réputation Google)

Catalogue 157 tutoriels : module `marketing-fidelite` (Marketing, Fidélité & Iris,
`#EC4899`), tutoriel **01 Débloquer les Avis clients** — voir
`CATALOGUE-157-TUTORIELS.md` ligne "8. Marketing, Fidélité & Iris". Module
actuellement à **0/24 publié** (`PROGRESSION-157-TUTORIELS.md`) : ce serait le tout
premier tutoriel du plus gros module du catalogue.

Rush fourni par Michael : `assets/screen.mp4` (19,72 s, 1920x828, 25 fps, piste
audio silencieuse -91 dB), `assets/intro.jpg` (`D_BLOQUER_LES_AVIS.jpg`, titre
"DÉBLOQUER LES AVIS" — cohérent cette fois avec le sujet, pas de carte mal
nommée), `assets/outro.jpg` (`page_fin_vid.jpg`, carte CTA générique déjà
réutilisée sur d'autres tutos).

## Analyse du rush

| t | Contenu |
|---:|---|
| 0,0-3,5 s | Page abonnement StockVision (plan actuel), scroll vers "Options & modules" |
| 3,5-9,5 s | Scroll jusqu'à la carte "Avis & réputation Google" (29€/mois) |
| ~9,6 s | **clic zoom-punch** sur "Ajouter cette option" (coord. source ≈ 367, 671) |
| 9,6-11,7 s | Modal "Changer de plan" : récapitulatif StockVision+OCR+Prediction+HACCP → Avis & réputation Google, total 29,00€ |
| ~11,8 s | **clic zoom-punch** sur "Continuer vers le paiement" (coord. source ≈ 1025, 689) → spinner "Redirection..." |
| 11,8-17,5 s | Redirection (chargement) |
| 17,5-19,72 s | Page de paiement Stripe (environnement de test) : "S'abonner à Avis & réputation Google — 29,00€ par mois", écran de vérification d'identité Stripe Link |

Rush court, coupe avant la confirmation de paiement (normal : un paiement Stripe
ne peut pas être finalisé dans un enregistrement de démo).

## Voix off (proposition, 7 lignes)

| # | Texte | Ancrage |
|---|---|---|
| N0 | Envie de débloquer les avis clients sur FoodEatUp ? Voici comment activer l'option en quelques clics. | carte d'intro |
| N1 | Dans Options et modules, repérez la carte Avis et réputation Google, à 29€ par mois. | scroll jusqu'à la carte |
| N2 | Cliquez sur Ajouter cette option pour l'ajouter à votre abonnement StockVision. | **zoom-punch** clic "Ajouter cette option" |
| N3 | Le récapitulatif s'affiche : votre offre passe à Avis et réputation Google, pour 29€ par mois. | modal "Changer de plan" |
| N4 | Cliquez sur Continuer vers le paiement pour finaliser votre commande. | **zoom-punch** clic "Continuer vers le paiement" |
| N5 | Vous êtes redirigé vers un paiement sécurisé par Stripe : une fois validé, votre plan est mis à jour immédiatement. | page de paiement Stripe |
| N6 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | carte de fin (CTA) — **réutilisable tel quel** |

## Séquence Claude — pas de prompt cette fois

Aucun outil `mcp__Foodeatup__*` ne correspond à l'action montrée (achat/activation
d'une option d'abonnement = paiement Stripe, comme sur `foodeatup-abonnement-tuto`
qui n'a pas non plus de `claudePrompt`). Les outils avis existants
(`list_reviews`, `moderate_review`, `reply_review`) concernent la *gestion* des
avis une fois l'option active, pas son *achat* — ce n'est pas ce que montre ce
rush. Pas de séquence "Utilisez cette fonctionnalité avec Claude" sur cette
vidéo, ni de `claudePrompt` sur la fiche Lovable (règle du workflow : ne pas
fabriquer de prompt sans action MCP correspondante à l'écran).

## Statut

**Brouillon — en attente de validation du script avant génération ElevenLabs**
(règle `FOODEATUP-TUTORIELS-WORKFLOW.md` §3, STOP obligatoire).
