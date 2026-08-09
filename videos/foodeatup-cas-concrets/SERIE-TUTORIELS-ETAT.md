# Série tutoriels — état de production

Suivi des 30 vidéos décrites dans `SCRIPTS-HEYGEN-30.md`. Chaque vidéo suit la structure
validée sur `v01-fidelite/` : hook → problème → démo (logiciel + avatar par-dessus) →
punchline.

## Montées (4 / 30)

| # | Projet | Durée | Avatar HeyGen | Vidéo logiciel (fenêtre) |
|---|---|---|---|---|
| 01 | `t01-ingredients/` | 30,2 s | `gen-1` (10,22 s) | `foodeatup-ingredients-tuto` · 85→99 s |
| 02 | `t02-recettes/` | 28,2 s | `gen-2` (12,14 s) | `foodeatup-recettes-tuto` · 74→88 s |
| 03 | `t03-fournisseurs/` | 30,2 s | `gen-3` (9,24 s) | `foodeatup-fournisseurs-tuto` · 44→58 s |
| 04 | `t04-mes-commandes/` | 28,2 s | `gen-4` (9,24 s) | `foodeatup-mes-commandes-tuto` · 20→34 s |

Les fenêtres de 14 s ont été choisies en échantillonnant chaque rush : elles couvrent le
geste utile **et** sa confirmation à l'écran (« Succès ! Ingrédient ajouté », tableau des
ingrédients avec coût total, fiche fournisseur créée, commande créée + liste multicanal).

Les durées diffèrent (28,2 s / 30,2 s) parce que deux plans problème ne durent que 6 s au
lieu de 8. Sans importance pour TikTok, mais c'est voulu, pas un oubli.

## Réserves sur ces 4 montages

Trois écarts par rapport à la vidéo 1 validée, tous dus aux plans problème :

1. **Format** — les plans `hero-video/` sont en 1280 × 720 paysage. Ils sont montés en
   pillarbox (plan centré sur un fond flouté tiré de lui-même) : regardable, mais en
   dessous d'un plan nativement vertical.
2. **Silence** — ces plans n'ont pas de piste audio. Le bloc problème est donc muet
   pendant 6 à 8 s, là où celui de la vidéo 1 avait son ambiance.
3. **Visage** — c'est le personnage IA « Karim » du film héros, pas la photo de Michael
   utilisée dans la vidéo 1.

Le correctif est le même pour les trois : générer les plans problème en **9:16 natif, 8 s,
référence = photo de Michael**, avec les prompts du plan principal. Ces montages sont alors
mis à jour par simple remplacement de `assets/higgsfield/probleme.mp4` et re-rendu.

## Rendre à nouveau une vidéo

```bash
cd videos/foodeatup-cas-concrets/t01-ingredients
npx hyperframes check .
npx hyperframes render . -q high -o renders/video-t01-ingredients.mp4
```

## Produire les suivantes

Le carton hook est paramétrable — plus besoin d'une composition par vidéo :

```bash
cd videos/foodeatup-cas-concrets/motion
npx hyperframes render . -c compositions/hook-card.html -q high \
  -o renders/hook-t05.mp4 \
  --variables '{"num1":"…","rest1":"…","num2":"…","rest2":"…"}'
```

Puis le générateur d'assemblage :
`scratchpad/build_videos.py` (une entrée par vidéo dans la liste `VIDEOS`, puis
`npx hyperframes render`). Il calcule seul la hauteur d'affichage du logiciel à partir des
dimensions réelles du rush, et cale l'avatar sur sa durée réelle.

## Clips HeyGen restants

26 sur 30. Ils arrivent par lots dans `_heygen-inbox/` — voir son README pour la convention
de nommage et le contrôle qualité appliqué à chaque clip.
