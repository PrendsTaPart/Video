# foodeatup-chaines — vidéo commerciale « Chaînes »

Cible : dirigeants et directeurs financiers de chaînes de boulangerie et de restauration
(5 à 60 points de vente). Objectif : décrocher un rendez-vous.

**Angle unique : l'écart entre sites, pas la moyenne.**

## État au 2026-08-07

| Bloc | Périmètre | État |
|---|---|---|
| `boulangerie/` | séquences 1 à 4 (~55 s) | **composition muette rendue et vérifiée** — VO en attente |
| `restauration/` | séquences 1 à 4 | non produit (C3) |
| `commun/` | séquences 5 à 9 | **bloqué** — voir ci-dessous |

### Deux points bloquants, tous deux documentés dans `SOURCES.md`

1. **La vue consolidée multi-établissements n'existe pas dans le MCP FoodEatUp.**
   Les ~250 outils prennent tous un `establishment_id` singulier et obligatoire ; aucun
   n'accepte plusieurs sites, aucun ne liste les établissements, aucun rôle « siège ».
   Les séquences 5, 6 et 8 montreraient un écran non vérifié : **elles ne sont pas
   produites**. Les séquences 1 à 4, elles, ne contiennent aucun plan produit — c'est
   pourquoi elles ont pu être faites (et c'est l'ordre d'exécution prévu au brief :
   valider la séquence 2 avant tout le reste).
   *Réserve : ce constat porte sur la surface MCP, pas forcément sur l'application web.*

2. **Les quatre chiffres `[À CONFIRMER]` n'ont pas été fournis.** La vidéo est écrite en
   **version sans chiffres**, conformément à la clause C0 : formuler la question plutôt
   qu'affirmer la réponse. Aucun pourcentage, aucun montant à l'écran — l'écart est
   *montré*, jamais quantifié.

## Arborescence

```
foodeatup-chaines/
  chaines.json          état, durées, voix off
  SOURCES.md            tout chiffre affiché doit y figurer (aujourd'hui : aucun)
  _fonts/               Fredoka + Baloo 2 (woff2, inlinés en base64 au build)
  boulangerie/
    build.py            génère index.html
    check.py            40 critères d'acceptation (C0 + contrat HyperFrames)
    index.html          la composition — 530 Ko, auto-portée
    assets/img/         carnet.png, fournee.png, logo-horizontal.png, mark-eight.png
```

## Régénérer

```bash
cd boulangerie
python3 build.py     # réécrit index.html
python3 check.py     # 40/40 attendu
```

## Choix techniques à connaître

**Polices.** La charte C0 demande « corps Inter ou Nunito » — or le guide HyperFrames
**bannit explicitement** Inter et Nunito. Résolu à l'intérieur de la charte elle-même :
**Fredoka** pour les titres (déjà au dépôt), **Baloo 2** pour le corps. Les deux sont sur
la liste de la charte, aucune n'est bannie. Inlinées en `@font-face` base64 (un `<link>`
Google Fonts casse le déterminisme du rendu).

**Empilement des scènes.** Chaque scène porte un `z-index` explicite. Sans lui, la scène
sortante reste visible **sous** la suivante : GSAP promeut les éléments animés en calques
de composition, et un calque promu se rasterise au-dessus du fond d'une scène frère
postérieure — alors même que l'ordre DOM, les styles calculés et `elementFromPoint`
indiquent tous l'inverse. Constaté au contrôle visuel : « L'écart » (s3) transparaissait
sous les séquences 3 et 4. `check.py` vérifie ce point.

**Scènes longues assumées.** Le guide HyperFrames conseille ≤ 5 s par scène ; ici une
scène = une séquence du brief (10 à 15 s), parce que chaque séquence est **une animation
continue à révélation progressive** (le tableau se remplit, les barres se déforment).
La découper redémarrerait l'animation. Chaque scène a une activité permanente.

**Aucun plan produit.** Règle C0 : rien du logiciel avant la seconde 60. Ces séquences
s'arrêtent à 55 s — elles ne montrent donc aucune capture, par construction.

## Contrôle visuel

Le rendu a été vérifié sur 10 frames réelles (Chromium). Deux défauts trouvés et corrigés :
la scène « L'écart » qui transparaissait (z-index), et les 5 plateaux de la séquence 4
superposés au pixel près — l'empilement ne se voyait pas.

Pour re-vérifier, il faut une copie de test : le runtime HyperFrames et les shaders WebGL
plantent le renderer headless, et `python3 -m http.server` (mono-thread) bloque le
chargement. La copie de test inline GSAP, neutralise `HyperShader.init` et se charge en
`file://`. Elle n'est pas versionnée — `index.html` garde ses trois `<script src>` CDN,
comme l'exige le contrat d'import.

Piège rencontré : `page.evaluate("tl.pause(t)")` renvoie l'objet Timeline GSAP, que
Playwright tente de sérialiser — graphe circulaire, blocage complet. Écrire
`page.evaluate("(t)=>{tl.pause(t);}", t)`, qui ne renvoie rien.

## Prochaines étapes

1. Trancher sur la vue groupe (existe / roadmap / n'existe pas).
2. Fournir les quatre chiffres, ou confirmer la version sans chiffres.
3. Choisir la voix ElevenLabs et donner l'accord de coût → génération VO → **recalage des
   `data-duration` sur la durée réelle de la VO** (règle C0 : la VO fixe les durées).
4. Import HyperFrames (`import-claude-design-from-url`) puis rendu.

## Provenance des visuels

`carnet.png` et `fournee.png` ont été générés sur RapidoCMS (`generate_image`), puis
détourés (flood fill depuis les bords), recadrés et réduits. Aucune IP tierce, aucun
logo d'enseigne, aucun visage, aucun texte lisible dans les illustrations.
