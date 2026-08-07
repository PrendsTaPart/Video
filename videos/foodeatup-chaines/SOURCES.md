# SOURCES.md — vidéo « Chaînes »

Règle C0 : tout chiffre affiché à l'écran ou prononcé en voix off doit figurer ici.
Trois catégories : `[SOURCÉ]`, `[EXEMPLE]`, `[À CONFIRMER]`.

**État au 2026-08-07 : aucun chiffre `[SOURCÉ]`. La vidéo est écrite en VERSION SANS
CHIFFRES**, conformément à la clause C0 : « Si je ne te les donne pas, écris la vidéo
SANS eux, en formulant la question au lieu d'affirmer la réponse. »

---

## [À CONFIRMER] — les quatre chiffres bloquants

Aucun n'a été fourni. Aucun n'est utilisé dans la production actuelle.

| # | Chiffre attendu | Où il servirait | Statut |
|---|---|---|---|
| 1 | Taux d'invendus moyen d'une chaîne de boulangerie | Boulangerie, séq. 2 et 4 | **non fourni** |
| 2 | Écart de food cost constaté entre sites d'une même enseigne | Restauration, séq. 2 | **non fourni** |
| 3 | Délai moyen de remontée d'un consolidé en restauration multi-sites | Séq. 4 (les « 45 jours ») | **non fourni** |
| 4 | Toute économie chiffrée attribuée à FoodEatUp | Nulle part — écarté | **non fourni** |

### Conséquence rédactionnelle appliquée

- Le `[CHIFFRE]` de la VO boulangerie est remplacé par la formulation interrogative
  prévue en C2 : « personne dans l'entreprise ne saurait le donner ».
- « Six semaines » devient « plusieurs semaines » (variante C2 explicite).
- **Aucun axe chiffré sur les barres de la séquence 2.** Les barres sont
  différenciées par leur longueur relative seule, sans pourcentage affiché — l'écart
  est montré, jamais quantifié.
- La frise de la séquence 4 est graduée « Jour 1 → Jour 45 » **en tant que repère de
  délai générique**, non comme mesure de la chaîne du prospect. C'est un ordre de
  grandeur de cycle comptable, pas une donnée mesurée. Si vous jugez ce repère lui-même
  trop affirmatif, il se retire en un mot (`FRISE_LABELS` dans `build.py`).

---

## [EXEMPLE] — chiffres d'illustration, étiquetés à l'écran

| Élément | Valeur | Traitement à l'écran |
|---|---|---|
| Nombre de magasins | 12 | Cardinal narratif, pas une mesure. Nommés « Magasin 01 » à « Magasin 12 ». |
| Longueurs relatives des 12 barres (séq. 2) | générées, non chiffrées | Aucun nombre affiché. Suite déterministe figée en dur dans le HTML (pas de `Math.random()` — contrainte de déterminisme HyperFrames). |
| Quantités manuscrites des carnets (séq. 3) | illisibles par construction | Rendues comme des gribouillis, jamais comme des nombres lisibles. Aucune valeur à sourcer. |

Aucun de ces éléments n'est présenté comme une donnée de marché ni comme un résultat
FoodEatUp.

---

## [SOURCÉ]

*(vide)*

---

## Vérification produit — bloquante, non levée

C0 étape 3 impose de vérifier l'existence d'une vue consolidée multi-établissements
avant d'écrire la séquence 6.

**Résultat de l'interrogation du MCP FoodEatUp (2026-08-07) : cette vue n'existe pas.**

- Les ~250 outils exposés prennent tous `establishment_id` — `integer`, **singulier**,
  **`required`**. Vérifié notamment sur `finance_summary`, `get_daily_brief`,
  `get_site_stats`, `get_pos_report`, `get_subscription_overview`,
  `list_top_productions`, `list_attendances`, `search_entities`.
- Aucun outil n'accepte un tableau d'IDs, ni un `company_id` / `group_id`.
- Aucun outil ne **liste** les établissements : le MCP ne permet même pas de constater
  qu'un groupe possède plusieurs sites.
- Aucun comparatif inter-sites, aucun rôle « siège ».
- Zéro occurrence de `multi-établissement`, `vue groupe`, `rôle siège` ou `inter-sites`
  dans la documentation produit du dépôt (`LOVABLE-FOODEATUP-DOCS.md` + ~94 fiches
  tutoriels).

**Portée de cette conclusion :** elle vaut pour la surface MCP, pas nécessairement pour
l'application web. Une vue siège peut exister sans être exposée en MCP — à confirmer
par Michael.

**Conséquence sur le périmètre produit :** les séquences 5 à 9 (tronc commun C1) et la
séquence 6 en particulier montrent un écran consolidé qui n'a pas été vérifié.
**Elles ne sont pas produites.** Seules les séquences 1 à 4 le sont : elles ne
contiennent aucun plan produit (règle C0 : aucun plan produit avant la seconde 60).

---

## Interdits C0 — contrôle

- [x] Aucun témoignage, logo client ou nom d'enseigne réelle
- [x] Aucune comparaison nommée à un concurrent
- [x] Aucune promesse de résultat financier
- [x] Aucune capture produit (ces séquences n'en contiennent aucune par construction)
- [x] Sites nommés « Magasin 01 » … « Magasin 12 » — aucun nom d'entreprise existante
- [x] Aucun visage reconnaissable
