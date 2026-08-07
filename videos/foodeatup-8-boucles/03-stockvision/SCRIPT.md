# Boucle 03 — StockVisionAI (la boucle mère)

Slug : `boucle-03-stockvision` · Durée cible 90 s · Agents : Jarvis puis PrédiBot.

## Voix off (verbatim — ne pas réécrire)

Vendredi, dix-huit heures. Le saumon est fini. Vous retirez de la carte le plat qui
rapporte le plus. Trente couverts qui prendront autre chose. Ou qui ne reviendront pas.

"Il me reste combien de saumon ?"

FoodEatUp ne compte pas un stock. Il le fait parler. La quantité réelle. La date limite.
Et les plats qui en consomment — parce que vos fiches techniques le savent déjà.

C'est la seule boucle qui contient une prévision : le modèle lit l'historique par jour
de semaine, écarte les valeurs aberrantes, et injecte les jours fériés français.

Alors il détecte ce qui va manquer ce week-end, et prépare la commande fournisseur,
ligne par ligne. Vous validez avant l'envoi. Toujours.

À la réception, le contrôle HACCP se déclenche, le stock entre, la production se cale
sur ce qui s'est vraiment vendu.

Résultat : plus de rupture le samedi, et quatre à dix pour cent d'achats qui ne
finissent plus à la poubelle le dimanche.

**Note** : contrairement à la Boucle 02, la VO ne contient pas de phrase « si cette
boucle est coupée ». Le plan 7 la porte en texte à l'écran uniquement (voir plus bas),
pas en voix off — ne pas l'ajouter à la VO.

## Squelette 7 plans (~90 s, calé sur la durée réelle de la VO)

| # | Rôle |
|---|------|
| 1 | Le problème : vendredi 18h, saumon fini, retrait du plat le plus rentable. 30 couverts qui prennent autre chose ou ne reviennent pas. |
| 2 | La question à l'agent, en gros : « Il me reste combien de saumon ? » |
| 3 | (le plus long) Cascade : Besoins des fiches → Commande fournisseur → Réception et contrôle → Entrée en stock → Consommation par la production → Inventaire → Écart → Nouveaux besoins. Encart « prévision » au milieu : histogramme des ventes par jour de semaine, une valeur aberrante barrée, un jour férié surligné. |
| 4 | Commande fournisseur ligne par ligne, bouton « Valider avant envoi ». |
| 5 | Boucles voisines qui s'allument dans le ∞ : HACCP, E-commerce, Communication, Comptabilité (4 boucles, pas une seule). |
| 6 | Chiffres : 0 rupture le samedi · 4 à 10 % de gaspillage évité. |
| 7 | Texte à l'écran (pas en VO) : « Une rupture un samedi soir, ou quatre à dix pour cent des achats à la poubelle le dimanche. » Preuve : 14 outils MCP. Puis CTA Academy. |

## Assets à réutiliser (studio-video/assets/brand/)

- `mascots/agent-stockvision.png` — agent StockVisionAI pour les plans 2, 4.
- `mascots/chef-haccp.png` — clin d'œil boucle HACCP au plan 5.
- `product-screenshots/stockvision-gestion-stocks.png` — plan 1 ou 3 (le stock qui parle).
- `product-screenshots/controle-reception-manuel.png`, `detail-reception-livree.png` — plan 3 (réception) / plan 4.
- `product-screenshots/liste-courses.png`, `gestion-livraisons.png` — plan 3/4 (commande fournisseur).
- `logo-v2/foodeatup-logo-horizontal-mascot.png` — CTA plan 7.

## Statut
`script` (VO figée, pas encore générée en audio — préflight coût en attente de
confirmation avant l'appel ElevenLabs).
