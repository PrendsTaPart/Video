#!/usr/bin/env python3
"""Jeu de démonstration FICTIF pour l'application Recettes : « Bistrot de l'École » (n°900).
Remplace assets/demo/mena.json dans une COPIE jetable de l'application (jamais dans le dépôt).
Aucune donnée de client réel : recettes, prénoms, prix et coûts inventés.
python3 bistrot_demo.py <sortie.json>"""
import json, sys
ING = "asset:assets/demo/ingredients/"
def ing(i, nom, q, u, img=None, all=()):
    return {"ingredient_id": i, "name": nom, "quantity": float(q), "unit": u, "note": "", "image_url": (ING + img) if img else None, "allergens": list(all), "linked_recipe_id": None}
CATS = [(901, "Préparations", "#C9B79C"), (902, "Cafés", "#B07F5A"), (903, "Boissons fraîches", "#6FA8BD"), (904, "Plats du midi", "#D98C5F"), (905, "Desserts", "#C46A8B")]
# id, nom, cat, kind, temp, label temp, minutes, difficulté, rendement, libellé rendement, contenant, ingrédients, étapes(texte, durée s), astuce, conservation, DLC h, service, plat lié (nom, ttc)
R = [
 (9001, "Vinaigrette maison", 901, "preparation", "froid", "Froid", 5, 1, 10, "1 flacon de 500 ml · 10 salades", "Flacon verseur 500 ml",
  [ing(1, "Huile de colza", 300, "ml"), ing(2, "Vinaigre de vin", 100, "ml"), ing(3, "Moutarde", 40, "g", all=["Moutarde"]), ing(4, "Sel fin", 4, "g")],
  [("Mettre la moutarde et le sel dans le flacon.", None), ("Ajouter le vinaigre et fermer.", None), ("Secouer 20 secondes.", 20), ("Ajouter l'huile, refermer et secouer encore.", 20)],
  "Toujours secouer avant de servir.", "Flacon fermé au frais (0-4 °C)", 72, [], None),
 (9002, "Pâte à crêpes", 901, "preparation", "froid", "Froid", 10, 1, 20, "1 bac de 2 L · 20 crêpes", "Bac gradué 2 L",
  [ing(5, "Farine T45", 500, "g", all=["Gluten"]), ing(6, "Œufs", 6, "pièce", all=["Œufs"]), ing(7, "Lait entier", 1000, "ml", "lait-entier.webp", ["Lait"]), ing(8, "Beurre fondu", 50, "g", all=["Lait"]), ing(4, "Sel fin", 2, "g")],
  [("Mélanger la farine et le sel.", None), ("Ajouter les œufs et fouetter.", None), ("Verser le lait petit à petit en fouettant.", None), ("Ajouter le beurre fondu.", None), ("Laisser reposer au frais.", 1800)],
  "Le repos rend la pâte plus souple : ne le saute pas.", "Bac filmé au frais (0-4 °C)", 48, [], None),
 (9003, "Expresso", 902, "boisson", "chaud", "Chaud", 1, 1, 1, "1 tasse", "Tasse 7 cl",
  [ing(9, "Café en grains", 8, "g")],
  [("Moudre 8 g de café.", None), ("Tasser et extraire.", 25), ("Servir avec une bûchette de sucre.", None)],
  "Une extraction trop courte donne un café acide.", "", None, ["Tasse 7 cl", "Une bûchette de sucre"], ("Expresso", 2.0)),
 (9004, "Cappuccino", 902, "boisson", "chaud", "Chaud", 2, 2, 1, "1 tasse", "Tasse 18 cl",
  [ing(9, "Café en grains", 8, "g"), ing(7, "Lait entier", 120, "ml", "lait-entier.webp", ["Lait"])],
  [("Extraire un expresso.", 25), ("Faire mousser le lait.", 30), ("Verser la mousse sur le café.", None)],
  "Lait bien froid au départ : la mousse tient mieux.", "", None, ["Tasse 18 cl"], ("Cappuccino", 3.5)),
 (9005, "Chocolat chaud", 902, "boisson", "chaud", "Chaud", 3, 1, 1, "1 tasse", "Tasse 25 cl",
  [ing(10, "Chocolat en poudre", 25, "g"), ing(7, "Lait entier", 220, "ml", "lait-entier.webp", ["Lait"]), ing(11, "Crème fouettée", 20, "g", "creme-liquide-35.webp", ["Lait"])],
  [("Chauffer le lait.", 60), ("Ajouter le chocolat et fouetter.", None), ("Servir avec la crème fouettée.", None)],
  "Sans crème sur demande : retire la ligne avant de servir.", "", None, ["Tasse 25 cl"], ("Chocolat chaud", 3.8)),
 (9006, "Citronnade maison", 903, "boisson", "froid", "Froid", 3, 1, 1, "1 verre de 40 cl", "Verre 40 cl",
  [ing(12, "Jus de citron", 40, "ml", "jus-citron.webp"), ing(13, "Sirop de canne", 25, "ml", "sirop-canne.webp"), ing(14, "Eau plate", 250, "ml", "eau-plate.webp"), ing(15, "Feuilles de menthe", 4, "pièce", "feuilles-menthe-fraiche.webp"), ing(16, "Glaçons", 6, "pièce", "glacons.webp")],
  [("Mettre les glaçons dans le verre.", None), ("Verser le jus de citron et le sirop.", None), ("Compléter avec l'eau et mélanger.", None), ("Décorer avec la menthe.", None)],
  "Goûte une fois par service : les citrons changent d'acidité.", "", None, ["Verre 40 cl", "Une paille papier"], ("Citronnade maison", 3.9)),
 (9007, "Thé glacé pêche", 903, "boisson", "froid", "Froid", 2, 1, 1, "1 verre de 40 cl", "Verre 40 cl",
  [ing(17, "Thé noir infusé froid", 250, "ml"), ing(18, "Sirop de pêche", 25, "ml"), ing(16, "Glaçons", 6, "pièce", "glacons.webp")],
  [("Mettre les glaçons dans le verre.", None), ("Verser le sirop puis le thé.", None), ("Mélanger et servir.", None)],
  "Le thé s'infuse la veille au frais.", "", None, ["Verre 40 cl"], ("Thé glacé pêche", 3.9)),
 (9008, "Croque-monsieur", 904, "plat", "chaud", "Chaud", 8, 2, 1, "1 assiette", "Assiette plate",
  [ing(19, "Pain de mie", 2, "tranche", all=["Gluten"]), ing(20, "Jambon blanc", 1, "tranche"), ing(21, "Emmental râpé", 40, "g", all=["Lait"]), ing(22, "Béchamel", 30, "g", all=["Lait", "Gluten"])],
  [("Tartiner la béchamel sur une tranche.", None), ("Ajouter jambon et emmental, fermer.", None), ("Gratiner au four.", 360), ("Servir avec la salade.", None)],
  "Le fromage doit être doré, pas brûlé : surveille la dernière minute.", "", None, ["Assiette plate", "Salade verte"], ("Croque-monsieur", 9.5)),
 (9009, "Salade César", 904, "plat", "froid", "Froid", 10, 2, 1, "1 assiette", "Assiette creuse",
  [ing(23, "Salade romaine", 120, "g"), ing(24, "Poulet grillé", 100, "g"), ing(25, "Parmesan", 20, "g", all=["Lait"]), ing(26, "Croûtons", 20, "g", all=["Gluten"]), ing(27, "Sauce César", 30, "ml", all=["Œufs", "Poissons", "Lait"])],
  [("Laver et essorer la romaine.", None), ("Trancher le poulet.", None), ("Dresser salade, poulet, croûtons.", None), ("Ajouter parmesan et sauce au dernier moment.", None)],
  "La sauce au dernier moment : la salade reste croquante.", "", None, ["Assiette creuse"], ("Salade César", 12.0)),
 (9010, "Tarte au citron", 905, "dessert", "froid", "Froid", 40, 3, 8, "1 tarte · 8 parts", "Moule à tarte 24 cm",
  [ing(28, "Pâte sablée", 300, "g", all=["Gluten", "Œufs", "Lait"]), ing(12, "Jus de citron", 150, "ml", "jus-citron.webp"), ing(6, "Œufs", 4, "pièce", all=["Œufs"]), ing(29, "Sucre", 150, "g"), ing(8, "Beurre", 100, "g", all=["Lait"])],
  [("Cuire la pâte à blanc.", 900), ("Chauffer citron, sucre et œufs en fouettant.", 300), ("Ajouter le beurre hors du feu.", None), ("Garnir et laisser prendre au frais.", None)],
  "Une crème qui nappe la cuillère est prête.", "Au frais (0-4 °C) · DLC sur l'étiquette", 48, ["Part sur assiette dessert"], ("Tarte au citron", 5.5)),
 (9011, "Mousse au chocolat", 905, "dessert", "froid", "Froid", 20, 2, 6, "6 verrines", "Verrine 15 cl",
  [ing(30, "Chocolat noir", 200, "g", all=["Lait"]), ing(6, "Œufs", 6, "pièce", all=["Œufs"]), ing(29, "Sucre", 40, "g")],
  [("Faire fondre le chocolat.", 120), ("Monter les blancs avec le sucre.", None), ("Mélanger les jaunes au chocolat.", None), ("Incorporer les blancs délicatement et répartir.", None)],
  "Incorpore les blancs en soulevant : la mousse reste légère.", "Au frais (0-4 °C) · DLC sur l'étiquette", 48, ["Verrine 15 cl"], ("Mousse au chocolat", 5.0)),
 (9012, "Crêpe sucre", 905, "dessert", "chaud", "Chaud", 3, 1, 1, "1 crêpe", "Assiette dessert",
  [ing(31, "Pâte à crêpes", 100, "ml"), ing(29, "Sucre", 10, "g"), ing(8, "Beurre", 5, "g", all=["Lait"])],
  [("Graisser la crêpière.", None), ("Verser une louche de pâte.", None), ("Cuire chaque face.", 60), ("Sucrer et plier en quatre.", None)],
  "Une louche rase par crêpe : elles ont toutes la même taille.", "", None, ["Assiette dessert"], ("Crêpe sucre", 3.5)),
]
PRIX = {"Huile de colza": (3.2, "L"), "Vinaigre de vin": (2.1, "L"), "Moutarde": (6.0, "kg"), "Sel fin": (0.8, "kg"), "Farine T45": (1.1, "kg"), "Œufs": (0.25, "pièce"),
        "Lait entier": (1.05, "L"), "Beurre fondu": (9.5, "kg"), "Beurre": (9.5, "kg"), "Café en grains": (18.0, "kg"), "Chocolat en poudre": (7.5, "kg"), "Crème fouettée": (6.0, "kg"),
        "Jus de citron": (4.5, "L"), "Sirop de canne": (5.0, "L"), "Eau plate": (0, "L"), "Feuilles de menthe": (0.05, "pièce"), "Glaçons": (0.01, "pièce"), "Thé noir infusé froid": (1.2, "L"),
        "Sirop de pêche": (5.0, "L"), "Pain de mie": (0.12, "tranche"), "Jambon blanc": (0.6, "tranche"), "Emmental râpé": (11.0, "kg"), "Béchamel": (4.0, "kg"), "Salade romaine": (4.0, "kg"),
        "Poulet grillé": (14.0, "kg"), "Parmesan": (22.0, "kg"), "Croûtons": (8.0, "kg"), "Sauce César": (9.0, "L"), "Pâte sablée": (5.0, "kg"), "Sucre": (1.2, "kg"), "Chocolat noir": (13.0, "kg"), "Pâte à crêpes": (1.5, "L")}
def base(u): return {"g": ("kg", 1000), "ml": ("L", 1000)}.get(u, (u, 1))
def cout(lignes):
    out = []
    for l in lignes:
        p, pu = PRIX[l["name"]]; _, div = base(l["unit"])
        out.append({"name": l["name"], "quantity": l["quantity"], "unit": l["unit"], "supplier": None, "packaging": None, "price_ht": p, "price_unit": pu, "line_cost": round(l["quantity"] / div * p, 2)})
    return {"material": round(sum(x["line_cost"] for x in out), 2), "lines": out}
recipes, catalogue, couts = {}, [], {}
for (i, nom, cat, kind, temp, tl, mn, dif, ren, rl, cont, ings, steps, tip, stock, dlc, serv, plat) in R:
    alls = sorted({a for x in ings for a in x["allergens"]})
    manques = [] if any(d for _, d in steps) else ["durees_etapes"]
    resume = {"id": i, "name": nom, "category_id": cat, "kind": kind, "kind_source": "fiche", "temperature": temp, "temperature_source": "fiche", "temperature_label": tl,
              "preparation_minutes": mn, "difficulty": dif, "yield": float(ren), "yield_label": rl, "container": cont, "image_url": None, "allergens": alls,
              "allergens_label": ", ".join(alls) if alls else "Aucun allergène majeur", "steps_count": len(steps), "active": True, "version": 1, "manques": manques}
    catalogue.append(resume)
    recipes[str(i)] = {**resume, "description": f"{nom} – {tl.lower()}. {cont}.", "tip": tip, "service_notes": serv, "storage_notes": stock, "shelf_life_hours": dlc,
        "ingredients": ings, "steps": [{"id": i * 10 + n, "number": n + 1, "text": t, "duration_seconds": d, "image_url": None, "video": None, "video_url": None, "tips": []} for n, (t, d) in enumerate(steps)],
        "video": None, "linked_dishes": [{"id": i + 7000, "name": plat[0], "active": True, "price_ttc": plat[1], "price_ht": round(plat[1] / 1.1, 2)}] if plat else [],
        "version_info": {"number": 1, "date": "2026-10-20T10:00:00+02:00", "author": "Camille"}}
    couts[str(i)] = cout(ings)
cats = [{"id": c, "name": n, "color": col, "fallback_color": col, "icon": None, "count": sum(1 for r in R if r[2] == c), "unclassified": False} for c, n, col in CATS]
ids = lambda *c: [r[0] for r in R if r[2] in c]
path = [
 {"day": 1, "title": "Cafés et service", "intro": "Bienvenue au Bistrot de l'École ! Aujourd'hui, on découvre l'application et les cafés de la carte.",
  "essentials": ["Mains lavées à chaque prise de poste", "Le lait est un allergène : vérifie la fiche avant de répondre", "Quantités et gestes viennent de la fiche, jamais de mémoire"],
  "goals": ["Suivre une fiche pas à pas", "Trouver une recette en trois touches", "Répondre à « il y a du lait ? » avec la fiche"], "kind": "application", "recipe_ids": ids(902), "missions": ["visite_accueil", "visite_etape", "premiere_recette", "allergenes"]},
 {"day": 2, "title": "Préparations du matin", "intro": "Les préparations de base, faites le matin pour toute la journée.", "essentials": ["Étiquette chaque préparation avec sa DLC"], "goals": ["Réaliser les préparations de la fiche"], "kind": "recettes", "recipe_ids": ids(901), "missions": []},
 {"day": 3, "title": "Boissons fraîches", "intro": "Citronnade et thé glacé, au verre.", "essentials": ["Glaçons toujours à la pince"], "goals": ["Servir chaque boisson fraîche de la carte"], "kind": "recettes", "recipe_ids": ids(903), "missions": []},
 {"day": 4, "title": "Plats du midi", "intro": "Les plats servis au déjeuner.", "essentials": ["Allergènes vérifiés avant chaque envoi"], "goals": ["Dresser les plats du midi"], "kind": "recettes", "recipe_ids": ids(904), "missions": []},
 {"day": 5, "title": "Desserts et révision", "intro": "Les desserts maison et une révision de la semaine.", "essentials": ["Les desserts se servent froids sauf la crêpe"], "goals": ["Réaliser les desserts de la carte"], "kind": "recettes", "recipe_ids": ids(905), "missions": []},
]
d = {"bootstrap": {"venue": {"id": 900, "name": "Bistrot de l'École", "city": "Ville fictive", "logo_url": None},
     "subscription": {"active": True, "plan": {"slug": "premiers-pas", "name": "Premiers Pas"}, "status": "active", "free_period_ends_on": "2026-12-31", "renewal_price_yearly": None,
                      "url": "https://foodeatup.com/establishment/900/subscription", "modules": {"recettes": True, "equipe": True, "production": False, "etiquettes": False}},
     "theme": {"mode": "foodeatup", "colors": {}, "radii": {"card": 16, "button": 16}}, "trainer": {"name": "Le chef", "portrait_url": None}, "languages": ["fr", "en", "vi"],
     "settings": {"idle_seconds": 180, "rush": True, "auto_voice": True, "school_mode_first_launch": True}, "data_version": "demo-bistrot-1", "device": {"id": 1, "name": "Tablette cuisine"}},
     "catalog": {"version": "demo-bistrot-1", "categories": cats, "recipes": catalogue}, "recipes": recipes,
     "employees": [{"id": 101, "name": "Camille", "photo_url": None, "has_pin": True}, {"id": 102, "name": "Sami", "photo_url": None, "has_pin": True}, {"id": 103, "name": "Léa", "photo_url": None, "has_pin": False}],
     "path": path, "full_costs": couts}
json.dump(d, open(sys.argv[1], "w"), ensure_ascii=False)
print(len(recipes), "recettes")
