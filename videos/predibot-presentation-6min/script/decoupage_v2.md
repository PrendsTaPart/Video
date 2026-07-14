# PrediBot — Catalogue COMPLET des commandes (re-analyse image-par-image des 6 clips)
> Objectif : montrer CHAQUE commande avec SON résultat. Ordre naturel commande → résultat préservé.
> Logo WhatsApp gardé en haut des segments WhatsApp.

## Crops RGPD
- WA : `crop=1514:984:392:44,delogo=x=1058:y=890:w=430:h=70` + bandeau WhatsApp vert (logo) ajouté en haut.
- BR : `crop=1904:930:8:100,delogo=x=1440:y=830:w=440:h=70`.
- Flouter : emails/téléphones employés (RH, Employées), bloc Laiterie du Cap Bon.

## GEN_MCP — Configuration (config.mp4, 80s) — 5 commandes
| # | Commande | WA (cmd) | Résultat |
|---|----------|----------|----------|
| 1 | « je veux ajouter un employé » | 9–15 | BR *Employées* 15–20 |
| 2 | « ajouter un fournisseur » | 21–30 | BR *Liste des Fournisseurs* 30–32 |
| 3 | « ajouter un ingrédient » | 33–45 | BR *Liste des Ingrédients* 45–47 |
| 4 | « ajouter un produit menu » | 48–57 | WA *Produit ajouté ✓* 57 |
| 5 | « ajouter une recette » | 63–77 | BR *Mes recettes (52)* 77.3–80 |

## MCP_HACCP — Conformité (haccp.mp4, 15s) — 1 commande
| 6 | « je veux modifier une température » (ID 158, 20°C) | 3.5–9 | BR *Températures* (Frigo 5 @ 20°C non conforme) 10.5–15 |

## MCP_GF — Fournisseurs (fournisseur.mp4, 26s) — 2 commandes
| 7 | « liste mes commandes » | 8–12 | WA *8 dernières commandes* 12–18 |
| 8 | « valide la commande 2986, conforme, RAS » | 16–20 | BR *Réception / Livrée* 22–26 |

## MCP_RH — Ressources humaines (rh.mp4, 54s) — 5 commandes
| 9 | « liste mes employés » | 3–6 | WA *liste équipe* 6–12 |
| 10 | « liste mes congés » | 21–24 | WA *congés en attente* 24–30 |
| 11 | « approuve le congé N45 » | 33–36 | WA *Congé #045 approuvé ✓* 39 |
| 12 | « rejette le congé 1023 en raison de test » | 36–39 | WA *Congé #1023 rejeté ✓* 42 |
| 13 | « classement / pointages employés » | 42–45 | WA *CLASSEMENT DES EMPLOYÉS* 48–54 |

## MCP_stock — Stocks (stock.mp4, 63s) — 6 commandes
| 14 | « liste mes stocks » | 3–6 | WA *12 derniers stocks* 6–12 |
| 15 | « liste mes recettes » | 15–18 | WA *7 dernières recettes* 15–21 |
| 16 | « vérifie le fournisseur louay » | 21–24 | WA *Fournisseur trouvé (ID 108)* 24–27 |
| 17 | « crée une commande fournisseur » | 27–42 | BR *Liste Courses / Livraisons* 30–36 + WA *CMD créée* 45–48 |
| 18 | « génère le dashboard stock » | 48–51 | BR *Dashboard Stock* (182/39/193835€/26) 54–62 |

## MCP_production — Production (production.mp4, 113s) — 8 commandes
| 19 | « liste mes productions » | 4–8 | WA *8 dernières productions* 8–12 |
| 20 | « vérifie les ingrédients de la production 1594 » | 12–16 | WA *ingrédients manquants* 16–20 |
| 21 | « je veux valider une production » | 20–36 | BR *Mes productions* 24–32 |
| 22 | « je veux ajouter une production » (recette 195) | 48–60 | BR *Mes productions* 52 |
| 23 | « prédit mes productions des prochains jours » | 60–64 | WA *PRÉDICTION 4 prochains jours* 64–72 |
| 24 | « analyse la rentabilité des plats » | 72–76 | WA *ANALYSE DE RENTABILITÉ* 76–84 |
| 25 | « top plats / meilleurs plats » | 84–88 | WA *TOP PLATS 30 jours* 84–88 |
| 26 | « génère le dashboard production » | 88–96 | BR *Dashboard Production* (528/121 + donuts) 104–112.5 |

## Total : 26 paires commande → résultat (27 commandes en comptant la CMD créée)
Structure vidéo : Hook → sting → Mika intro → orchestrateur → socle → [Mika annonce agent → toutes ses commandes+résultats] ×6 → alertes → 2 canaux → retour hook → hook de fin.
