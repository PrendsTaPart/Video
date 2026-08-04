# PrediBot — Découpage des rushes + carte des transitions WhatsApp↔Navigateur
> 6 clips reçus, 1920×1080 60fps. Chaque agent = commande WhatsApp → résultat réel dans l'app FoodEatUp (navigateur).

## Crops RGPD validés (image-par-image OK)
- **WA** (zone conversation) : `crop=1514:984:392:44` + `delogo=x=1058:y=890:w=430:h=70`
  → retire colonne contacts (numéros/noms réels), barre de titre, barre des tâches ; delogo « Activer Windows ». Garde header PrediBot + barre de saisie.
- **BR** (contenu app FoodEatUp) : `crop=1904:930:8:100` + `delogo=x=1440:y=830:w=440:h=70`
  → retire onglets navigateur, barre d'URL, barre des tâches ; delogo « Activer Windows ». Garde la nav FoodEatUp + le contenu.
- Extraits **muets** (`-an`) : évite toute fuite audio.
- À flouter en compo : bloc « Laiterie du Cap Bon » (email/tél réels) quand visible.

## Carte des segments (temps source)
| Clip | Durée | WhatsApp | Navigateur (résultat FoodEatUp) |
|------|-------|----------|----------------------------------|
| config | 80s | 0–18 (ajout employé) · 23–77 (ajout recette) | ~18.5–22.5 « Employées » · ~77.3–80 « Mes recettes (52) » |
| haccp | 15s | 0–9.5 (modifier température) | ~10.3–15 « Températures » (KPI 0 conformes / 4 non conformes, Frigo 5 @ 20°C) |
| fournisseur | 26s | 0–21 (commande + « valide la commande ») | ~22–26 « Réception »/« Livrée » (Commande KH-louay, Tomato 12kg) |
| rh | 54s | 0–54 (congés en attente → approuve) | — (reste WhatsApp) |
| stock | 63s | 0–29 (stocks critiques + lien) | 30–36 Livraisons (inutile) · **44–52 « Dashboard Stock »** (182/39/193835€/26 + graphe) · 54–63 tables |
| production | 113s | 8–100 (production, ingrédients manquants, prévision) | 104–113 « Dashboard Production » (528/121 + donuts + détail) |

## Extraits pour la composition (fenêtres retenues, à affiner)
| ID | Séq | Source | Fenêtre | Crop |
|----|-----|--------|---------|------|
| e08a | 8 | config | 3–14 | WA |
| e08b | 8 | config | 18.5–22.5 | BR |
| e08c | 8 | config | 60–74 | WA |
| e08d | 8 | config | 77.3–79.8 | BR |
| e09  | 9 | haccp | 2–9 | WA |
| e10  | 9-10 | haccp | 10.3–15 | BR |
| e11a | 11 | fournisseur | 6–20 | WA |
| e11b | 11 | fournisseur | 22–26 | BR |
| e12  | 12 | rh | 8–34 | WA |
| e13  | 13 | stock | 0–12 | WA |
| e14  | 14 | stock | 44–52 | BR (climax) |
| e15a | 15 | production | 64–96 | WA |
| e15b | 15 | production | 104–112.5 | BR |

## Flags (à valider au STOP)
1. **Séq 10 (journal HACCP PDF)** : aucune séquence PDF dans les rushes → carton graphique illustratif FoodEatUp (la fonction existe, cf. mémoire). Pas de fausse capture.
2. **Séq 14 (Dashboard Stock, le « waouh »)** : réel mais capture brute (bandeau « 32 lignes exclues — données à vérifier », graphe clairsemé, tables encombrées). À utiliser tel quel (honnête) ou refilmer une passe propre ? → Dashboard **Production** (donuts) est plus net et peut servir de climax alternatif.
3. **Avatar Mika** : rendu HeyGen désactivé pour ce client CLI → substitut local (image Mika + animation subtile + VO). À confirmer, ou fournir des clips HeyGen.
