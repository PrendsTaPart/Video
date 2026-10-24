"""
Les dix vidéos « pages de l'Académie » (octobre 2026).

Tout le contenu vient des fichiers de données du dépôt Académie
(foodeatup-guide-star) : connecteur-mcp.ts, formation-ia.ts, boucles-home.ts,
foodeatup-tarifs.ts, premiersPas.ts, client-restaurant.ts, predibot-guide.ts,
partenaires.ts. Aucun montant ni aucune promesse qui n'y figure pas.

Un « cue » est un mot (ou une suite de mots) de la voix off : la scène ou
l'élément démarre dessus. Les cues se lisent dans l'ordre de la voix.
"""

LOGO = "assets/brand/foodeatup-logo-horizontal-mascot.png"
CHEF = "assets/brand/chef-icon.svg"

# Affichage des sous-titres : ce qui est épelé à l'oral s'écrit normalement.
URL_REPL = [
    ("tutoriel point foodeatup point com, slash M C P", "tutoriel.foodeatup.com/mcp"),
    ("tutoriel point foodeatup point com, slash devenir formateur", "tutoriel.foodeatup.com/devenir-formateur"),
    ("tutoriel point foodeatup point com, slash devenir apporteur affaires", "tutoriel.foodeatup.com/devenir-apporteur-affaires"),
    ("site point foodeatup point com, slash tarifs", "site.foodeatup.com/tarifs"),
    ("slash M C P", "/mcp"),
    ("quatre cent six", "406"),
    ("cinquante pour cent", "50 %"),
    ("deux cent cinquante euros", "250 €"),
    ("cent soixante-dix", "170"),
    ("quarante-neuf euros", "49 €"),
    ("quatre-vingt-dix-neuf euros", "99 €"),
    ("cent dix-neuf euros", "119 €"),
    ("neuf août deux mille vingt-six", "9 août 2026"),
    ("Frigo deux à neuf degrés", "Frigo 2 à 9 °C"),
    ("en dix minutes", "en 10 minutes"),
]


def final(cue, url, tagline, note=None):
    items = [
        {"kind": "img", "src": LOGO, "cls": "logo-end", "cue": "+0.15"},
        {"kind": "url", "text": url, "icon": "link", "color": "#ffffff", "cue": "+0.6"},
    ]
    if note:
        items.append({"kind": "note", "text": note, "cue": "+0.9"})
    items += [
        {"kind": "pill", "text": tagline, "icon": "star", "color": "#c88100", "cue": "+1.2"},
        {"kind": "img", "src": CHEF, "cls": "chef-end", "cue": "+1.6"},
    ]
    return {"cue": cue, "final": True, "note": "Fin", "layout": "center", "items": items}


VIDEOS_SPEC = {
    # 1 ───────────────────────────────────────────────────────────────────
    "01": {
        "slug": "connecter-assistant-ia", "vo": "01", "music": "m-tech1",
        "title": "Connecter son assistant IA à l'Académie FoodEatUp",
        "comment": "Page /connecter-son-assistant-ia — source : src/data/connecteur-mcp.ts.",
        "about": "Brancher Claude, ChatGPT, Le Chat, Cursor ou VS Code sur le connecteur MCP public et gratuit de l'Académie.",
        "source": "`src/data/connecteur-mcp.ts` (RESUME_CONNECTEUR, CLIENTS_MCP, FAQ_CONNECTEUR).",
        "replace": URL_REPL,
        "vo_text": "Et si votre assistant IA devenait votre formateur FoodEatUp ? L'Académie a un connecteur MCP public et gratuit : sans compte, et sans clé d'API. Dans Claude, ouvrez Réglages, Connecteurs, puis Ajouter un connecteur personnalisé. Collez l'adresse : tutoriel.foodeatup.com/mcp. Laissez l'authentification sur aucune. Ça marche aussi avec ChatGPT, Le Chat de Mistral, Cursor et VS Code. Ensuite, demandez simplement : forme-moi à FoodEatUp. Parcours par métier, vidéos, quiz et exercices, en français. Et aucune donnée de votre restaurant n'est lue : seulement le catalogue de l'Académie.",
        "scenes": [
            {"cue": None, "note": "Accroche", "layout": "center", "items": [
                {"kind": "big", "icon": "robot", "text": "Votre IA", "sub": "formateur FoodEatUp", "cue": "+0"}]},
            {"cue": "L'Académie a", "kicker": "Le connecteur <b>MCP</b><br>de l'Académie", "layout": "wrap", "items": [
                {"kind": "pill", "icon": "check", "color": "#059669", "text": "Public", "cue": "public"},
                {"kind": "pill", "icon": "check", "color": "#059669", "text": "Gratuit", "cue": "gratuit"},
                {"kind": "pill", "icon": "check", "color": "#059669", "text": "Sans compte", "cue": "sans compte"},
                {"kind": "pill", "icon": "check", "color": "#059669", "text": "Sans clé d'API", "cue": "sans clé"}]},
            {"cue": "Dans Claude", "kicker": "Dans <b>Claude</b>", "items": [
                {"kind": "row", "num": 1, "text": "Réglages", "cue": "Réglages"},
                {"kind": "row", "num": 2, "text": "Connecteurs", "cue": "Connecteurs"},
                {"kind": "row", "num": 3, "color": "#c88100", "text": "Ajouter un connecteur personnalisé", "cue": "Ajouter"}]},
            {"cue": "Collez", "kicker": "L'adresse à coller", "layout": "center", "items": [
                {"kind": "url", "icon": "link", "color": "#ffffff", "text": "tutoriel.foodeatup.com/mcp", "cue": "tutoriel", "pulse": "+1.6"},
                {"kind": "badge", "icon": "lock", "text": "Authentification : aucune", "cue": "Laissez"}]},
            {"cue": "Ça marche", "kicker": "Aussi avec", "layout": "grid2", "items": [
                {"kind": "tile", "icon": "chat", "text": "ChatGPT", "cue": "ChatGPT"},
                {"kind": "tile", "icon": "chat", "color": "#c88100", "text": "Le Chat (Mistral)", "cue": "Le Chat"},
                {"kind": "tile", "icon": "code", "text": "Cursor", "cue": "Cursor"},
                {"kind": "tile", "icon": "code", "color": "#c88100", "text": "VS Code", "cue": "VS"}]},
            {"cue": "Ensuite", "kicker": "Il vous forme", "items": [
                {"kind": "bubble", "who": "me", "text": "Forme-moi à FoodEatUp", "cue": "forme-moi"},
                {"kind": "row", "icon": "map", "text": "Parcours par métier", "cue": "Parcours"},
                {"kind": "row", "icon": "play", "text": "Vidéos", "cue": "vidéos"},
                {"kind": "row", "icon": "check", "color": "#059669", "text": "Quiz et exercices", "cue": "quiz"}]},
            {"cue": "Et aucune", "layout": "center", "items": [
                {"kind": "big", "icon": "lock", "color": "#059669", "text": "0 donnée", "sub": "de votre restaurant", "cue": "aucune"},
                {"kind": "pill", "icon": "book", "text": "Seulement le catalogue", "cue": "seulement"}]},
            final("l'Académie", "tutoriel.foodeatup.com/mcp", "Gratuit, sans compte"),
        ],
    },
    # 2 ───────────────────────────────────────────────────────────────────
    "02": {
        "slug": "formation-ia", "vo": "02", "music": "m-tech2",
        "title": "Se former à FoodEatUp avec son assistant IA",
        "comment": "Page /formation-ia — source : src/data/formation-ia.ts.",
        "about": "Les deux connecteurs (Académie pour apprendre, FoodEatUp pour agir), un prompt prêt à l'emploi et la règle d'une leçon à la fois.",
        "source": "`src/data/formation-ia.ts` (CONNECTEURS, PROMPTS « Comprendre FoodEatUp en 10 minutes », CONSIGNE_RYTHME).",
        "replace": URL_REPL,
        "vo_text": "Se former à FoodEatUp avec son assistant IA, c'est deux connecteurs. Le premier, l'Académie, pour apprendre : les modules, les fiches, les vidéos et les parcours métier. Il est public, en lecture seule. Le second, FoodEatUp, pour agir : votre compte piloté en langage naturel. Shifts, ingrédients, HACCP, carte, factures. Lui demande un jeton personnel, généré depuis votre compte. Ensuite, choisissez un prompt prêt à l'emploi, par exemple : comprendre FoodEatUp en dix minutes. Une seule règle : une leçon à la fois. Une vidéo, une explication, et l'assistant attend votre feu vert. Tous les prompts sont sur la page Formation IA de l'Académie.",
        "scenes": [
            {"cue": None, "note": "Accroche", "layout": "center", "items": [
                {"kind": "stat", "text": "2", "sub": "connecteurs", "cue": "+0"},
                {"kind": "pill", "icon": "robot", "text": "Votre assistant IA", "cue": "assistant"}]},
            {"cue": "Le premier", "kicker": "<b>Apprendre</b>", "items": [
                {"kind": "row", "icon": "book", "text": "FoodEatUp Académie", "sub": "tutoriel.foodeatup.com/mcp", "cue": "l'Académie"},
                {"kind": "pill", "icon": "check", "color": "#059669", "text": "Modules", "cue": "modules"},
                {"kind": "pill", "icon": "check", "color": "#059669", "text": "Fiches", "cue": "fiches"},
                {"kind": "pill", "icon": "check", "color": "#059669", "text": "Vidéos et parcours métier", "cue": "vidéos"},
                {"kind": "badge", "icon": "lock", "bg": "#059669", "text": "Public · lecture seule", "cue": "public"}]},
            {"cue": "Le second", "kicker": "<em>Agir</em>", "items": [
                {"kind": "row", "icon": "bolt", "color": "#c88100", "text": "FoodEatUp", "sub": "foodeatup.com/api/mcp", "cue": "FoodEatUp"},
                {"kind": "pill", "icon": "team", "text": "Shifts", "cue": "Shifts"},
                {"kind": "pill", "icon": "box", "text": "Ingrédients", "cue": "ingrédients"},
                {"kind": "pill", "icon": "thermo", "text": "HACCP", "cue": "HACCP"},
                {"kind": "pill", "icon": "receipt", "text": "Carte et factures", "cue": "carte"},
                {"kind": "badge", "icon": "key", "text": "Jeton personnel", "cue": "jeton"}]},
            {"cue": "Ensuite", "kicker": "Un prompt prêt", "layout": "center", "items": [
                {"kind": "bubble", "who": "me", "text": "Comprendre FoodEatUp en 10 minutes", "cue": "comprendre"}]},
            {"cue": "Une seule règle", "kicker": "Une leçon <b>à la fois</b>", "items": [
                {"kind": "row", "num": 1, "text": "Une vidéo", "cue": "vidéo"},
                {"kind": "row", "num": 2, "text": "Une explication", "cue": "explication"},
                {"kind": "row", "num": 3, "color": "#059669", "text": "Votre feu vert", "cue": "feu"}]},
            final("Tous les prompts", "tutoriel.foodeatup.com/formation-ia", "Les prompts sont prêts"),
        ],
    },
    # 3 ───────────────────────────────────────────────────────────────────
    "03": {
        "slug": "huit-boucles", "vo": "03", "music": "m-resto1",
        "title": "FoodEatUp en huit boucles",
        "comment": "Page d'accueil de l'Académie — source : src/data/boucles-home.ts.",
        "about": "Les huit boucles du logiciel, dans l'ordre de la page d'accueil, avec leur nom technique.",
        "source": "`src/data/boucles-home.ts` (BOUCLES_HOME : titre, nom technique, résultat).",
        "replace": URL_REPL,
        "vo_text": "FoodEatUp, c'est huit boucles qui tournent ensemble. Un : la boutique et la carte. Un prix change, vos marges suivent. Deux : l'équipe et les plannings. Trois : le stock et les achats, avec StockVision AI. Quatre : l'HACCP, un dossier prêt chaque jour. Cinq : la vente en ligne, sans commission. Six : la communication, au bon moment. Sept : la fidélité, pour faire revenir les clients. Et huit : les chiffres et la comptabilité, avec PrediBot. Le chiffre du jour, avant d'éteindre la lumière. Chaque boucle a ses vidéos sur l'Académie FoodEatUp.",
        "scenes": [
            {"cue": None, "note": "Accroche", "layout": "center", "items": [
                {"kind": "big", "icon": "loop", "text": "8 boucles", "sub": "qui tournent ensemble", "cue": "+0"}]},
            {"cue": "Un", "layout": "grid2", "note": "Les huit boucles", "items": [
                {"kind": "tile", "num": "01", "text": "Boutique et carte", "sub": "Configuration", "cue": "Un"},
                {"kind": "tile", "num": "02", "text": "Équipe et plannings", "sub": "Équipe & planning", "cue": "Deux"},
                {"kind": "tile", "num": "03", "text": "Stock et achats", "sub": "StockVision AI", "cue": "Trois"},
                {"kind": "tile", "num": "04", "text": "HACCP", "sub": "Dossier prêt chaque jour", "cue": "Quatre"},
                {"kind": "tile", "num": "05", "color": "#c88100", "text": "Vente en ligne", "sub": "Sans commission", "cue": "Cinq"},
                {"kind": "tile", "num": "06", "color": "#c88100", "text": "Communication", "sub": "Iris", "cue": "Six"},
                {"kind": "tile", "num": "07", "color": "#c88100", "text": "Fidélité", "sub": "Faire revenir", "cue": "Sept"},
                {"kind": "tile", "num": "08", "color": "#c88100", "text": "Chiffres et compta", "sub": "PrediBot", "cue": "huit", "pulse": "+3.6"}]},
            final("Chaque boucle", "tutoriel.foodeatup.com", "Une boucle, ses vidéos"),
        ],
    },
    # 4 ───────────────────────────────────────────────────────────────────
    "04": {
        "slug": "tarifs-essai", "vo": "04", "music": "m-resto2",
        "title": "Combien coûte FoodEatUp",
        "comment": "Tarifs — source : src/data/foodeatup-tarifs.ts (TARIFS_VERIFIES_LE = 2026-08-09). Prix HT par établissement, TVA 20 % en sus.",
        "about": "Les trois packs, l'annuel, l'essai et l'offre Premiers Pas, avec la date de vérification.",
        "source": "`src/data/foodeatup-tarifs.ts` (PACKS, MOIS_PAYES_EN_ANNUEL, ESSAI_JOURS, OFFRE_PREMIERS_PAS, MENTION_TVA, TARIFS_VERIFIES_LE). Source de vérité : site.foodeatup.com/tarifs.",
        "replace": URL_REPL,
        "vo_text": "Combien coûte FoodEatUp ? Trois packs, par établissement, hors taxes. StockVision, à 49 € par mois : stocks, recettes, commandes fournisseurs, planning et facturation. Le pack avec OCR et HACCP, à 99 € : il remplace les classeurs et les tableurs. Et la version avec prédiction IA, à 119 €. En annuel, vous payez dix mois pour douze. Vous pouvez essayer sept jours, gratuitement, sans engagement. Et pour démarrer, l'offre Premiers Pas : votre carte et votre vitrine, gratuites la première année. Tarifs vérifiés le 9 août 2026. La grille complète est sur site.foodeatup.com/tarifs.",
        "scenes": [
            {"cue": None, "note": "Accroche", "layout": "center", "items": [
                {"kind": "big", "icon": "euro", "text": "3 packs", "sub": "par établissement · HT", "cue": "+0"}]},
            {"cue": "StockVision", "kicker": "Prix HT par mois", "items": [
                {"kind": "price", "text": "StockVision", "amount": "49 €", "sub": "Stocks, recettes, commandes, planning, facturation", "cue": "StockVision"},
                {"kind": "price", "text": "StockVision + OCR + HACCP", "amount": "99 €", "sub": "Remplace les classeurs et les tableurs", "highlight": True, "cue": "Le pack"},
                {"kind": "price", "text": "+ Prédiction IA", "amount": "119 €", "sub": "Prévisions de stock et de ventes", "cue": "Et la version"},
                {"kind": "note", "text": "TVA 20 % en sus", "cue": "+1"}]},
            {"cue": "En annuel", "layout": "center", "items": [
                {"kind": "stat", "text": "10 / 12", "sub": "en annuel : 10 mois payés", "cue": "En annuel"},
                {"kind": "badge", "icon": "check", "bg": "#059669", "text": "Essai 7 jours, sans engagement", "cue": "Vous pouvez"}]},
            {"cue": "Et pour démarrer", "kicker": "Pour démarrer", "items": [
                {"kind": "price", "text": "Premiers Pas", "amount": "0 € la 1re année", "sub": "Votre carte et votre vitrine en ligne", "highlight": True, "cue": "Premiers"}]},
            {"cue": "Tarifs vérifiés", "final": True, "note": "Fin", "layout": "center", "items": [
                {"kind": "img", "src": LOGO, "cls": "logo-end", "cue": "+0.1"},
                {"kind": "badge", "icon": "calendar", "text": "Vérifiés le 9 août 2026", "cue": "vérifiés"},
                {"kind": "url", "icon": "link", "color": "#ffffff", "text": "site.foodeatup.com/tarifs", "cue": "site"},
                {"kind": "img", "src": CHEF, "cls": "chef-end", "cue": "+2.6"}]},
        ],
    },
    # 5 ───────────────────────────────────────────────────────────────────
    "05": {
        "slug": "premiers-pas", "vo": "05", "music": "m-resto3",
        "title": "Les premiers pas sur FoodEatUp",
        "comment": "Page /premiers-pas — source : src/data/premiersPas.ts (8 jalons).",
        "about": "Les huit jalons de la configuration initiale, dans l'ordre.",
        "source": "`src/data/premiersPas.ts` (PREMIERS_PAS : titres des jalons 1 à 8).",
        "replace": URL_REPL,
        "vo_text": "Vous démarrez sur FoodEatUp ? Suivez les premiers pas, jalon par jalon. Un : ouvrir la porte. Votre compte et votre établissement. Deux : les réglages qui bloquent tout le reste. TVA, unités, catégories. Trois : brancher votre IA. À partir d'ici, vous pouvez arrêter de cliquer : votre assistant configure à votre place. Quatre : votre carte. Cinq : votre salle. Six : votre équipe. Sept : encaisser et envoyer en cuisine. Et huit : être en règle dès le premier jour, avec votre classeur HACCP. Huit jalons, et vous pouvez ouvrir.",
        "scenes": [
            {"cue": None, "note": "Accroche", "layout": "center", "items": [
                {"kind": "big", "icon": "rocket", "text": "Premiers pas", "sub": "jalon par jalon", "cue": "+0"}]},
            {"cue": "Un", "note": "Les huit jalons", "items": [
                {"kind": "row", "num": 1, "text": "Ouvrir la porte", "sub": "Compte et établissement", "cue": "Un"},
                {"kind": "row", "num": 2, "text": "Les réglages de base", "sub": "TVA, unités, catégories", "cue": "Deux"},
                {"kind": "row", "num": 3, "color": "#c88100", "text": "Brancher votre IA", "sub": "Elle configure à votre place", "cue": "Trois", "pulse": "arrêter de cliquer"},
                {"kind": "row", "num": 4, "text": "Votre carte", "cue": "Quatre"},
                {"kind": "row", "num": 5, "text": "Votre salle", "cue": "Cinq"},
                {"kind": "row", "num": 6, "text": "Votre équipe", "cue": "Six"},
                {"kind": "row", "num": 7, "text": "Encaisser et envoyer en cuisine", "cue": "Sept"},
                {"kind": "row", "num": 8, "color": "#059669", "text": "En règle dès le 1er jour", "sub": "Classeur HACCP", "cue": "huit"}]},
            final("Huit jalons", "tutoriel.foodeatup.com/premiers-pas", "Vous pouvez ouvrir"),
        ],
    },
    # 6 ───────────────────────────────────────────────────────────────────
    "06": {
        "slug": "parcours-client", "vo": "06", "music": "m-resto4",
        "title": "Le parcours du client au restaurant",
        "comment": "Parcours côté convive — source : src/data/client-restaurant.ts (10 fiches client).",
        "about": "Ce que vit le client, de la carte en ligne à l'avis, et le module pro derrière chaque geste.",
        "source": "`src/data/client-restaurant.ts` (fichesClient, cotePro.moduleSlug, astuce de la fiche 1).",
        "replace": URL_REPL,
        "vo_text": "Et côté client, comment ça se passe ? Il trouve le restaurant et lit la carte à jour sur son téléphone. Il commande sur le site du restaurant, ou à table, avec le QR code. Il paie, et reçoit son reçu. Il réserve une table. Il rejoint le programme de fidélité, cumule ses points à chaque passage, et utilise ses récompenses. Il reçoit les offres, sans être submergé. Et il laisse un avis après son passage. Chaque geste du client s'appuie sur un module que le restaurateur active dans FoodEatUp. Et la carte qu'il lit, c'est celle de la caisse : un plat épuisé disparaît de son écran.",
        "scenes": [
            {"cue": None, "note": "Accroche", "layout": "center", "items": [
                {"kind": "big", "icon": "phone", "text": "Côté client", "cue": "+0"}]},
            {"cue": "Il trouve", "layout": "grid2", "note": "Les gestes du client", "items": [
                {"kind": "tile", "icon": "search", "text": "Voir la carte", "cue": "trouve"},
                {"kind": "tile", "icon": "cart", "text": "Commander en ligne", "cue": "commande"},
                {"kind": "tile", "icon": "qr", "text": "QR code à table", "cue": "table"},
                {"kind": "tile", "icon": "card", "text": "Payer, reçu", "cue": "paie"},
                {"kind": "tile", "icon": "calendar", "text": "Réserver", "cue": "réserve"},
                {"kind": "tile", "icon": "heart", "color": "#c88100", "text": "Fidélité", "cue": "rejoint"},
                {"kind": "tile", "icon": "star", "color": "#c88100", "text": "Cumuler des points", "cue": "cumule"},
                {"kind": "tile", "icon": "gift", "color": "#c88100", "text": "Récompenses", "cue": "utilise"},
                {"kind": "tile", "icon": "megaphone", "color": "#c88100", "text": "Offres", "cue": "reçoit les offres"},
                {"kind": "tile", "icon": "chat", "color": "#c88100", "text": "Laisser un avis", "cue": "laisse"}]},
            {"cue": "Chaque geste", "kicker": "Un geste, <b>un module</b>", "layout": "wrap", "items": [
                {"kind": "pill", "icon": "shop", "text": "Site vitrine", "cue": "module"},
                {"kind": "pill", "icon": "qr", "text": "Service et commande", "cue": "+1.8"},
                {"kind": "pill", "icon": "receipt", "text": "Caisse", "cue": "+2.1"},
                {"kind": "pill", "icon": "calendar", "text": "Réservation", "cue": "+2.4"},
                {"kind": "pill", "icon": "heart", "text": "Marketing et fidélité", "cue": "+2.7"}]},
            {"cue": "Et la carte", "kicker": "La carte = <b>la caisse</b>", "layout": "center", "items": [
                {"kind": "bubble", "who": "bot", "text": "Plat épuisé : il disparaît de l'écran du client", "cue": "épuisé"}]},
            final("écran", "tutoriel.foodeatup.com", "Chaque geste, un module"),
        ],
    },
    # 7 ───────────────────────────────────────────────────────────────────
    "07": {
        "slug": "predibot", "vo": "07", "music": "m-tech3",
        "title": "PrediBot, votre restaurant sur WhatsApp",
        "comment": "Module PrediBot — source : src/data/predibot-guide.ts (intro, 6 agents, alertes, cas d'usage).",
        "about": "PrediBot pilote FoodEatUp depuis WhatsApp : six agents et des alertes avant que ça déraille.",
        "source": "`src/data/predibot-guide.ts` (predibotIntro, predibotAgents, predibotCases, predibotAlerts).",
        "replace": URL_REPL,
        "vo_text": "PrediBot, c'est votre restaurant dans votre poche. Stocks, congés, fournisseurs, HACCP, prévisions : tout se pilote depuis une conversation WhatsApp. Vous demandez en langage naturel, PrediBot exécute dans FoodEatUp. Derrière lui, six agents : stocks, HACCP, achats et fournisseurs, équipe, production, et configuration. Et surtout, il vous alerte avant que ça déraille. Frigo 2 à 9 °C : seuil dépassé. Une réception fournisseur pas encore contrôlée. Un stock critique avant le service de samedi. Découvrez PrediBot sur l'Académie FoodEatUp.",
        "scenes": [
            {"cue": None, "note": "Accroche", "layout": "center", "items": [
                {"kind": "big", "icon": "phone", "text": "PrediBot", "sub": "votre restaurant dans votre poche", "cue": "+0"}]},
            {"cue": "Stocks", "kicker": "Tout sur <b>WhatsApp</b>", "layout": "wrap", "items": [
                {"kind": "pill", "icon": "box", "text": "Stocks", "cue": "Stocks"},
                {"kind": "pill", "icon": "calendar", "text": "Congés", "cue": "congés"},
                {"kind": "pill", "icon": "truck", "text": "Fournisseurs", "cue": "fournisseurs"},
                {"kind": "pill", "icon": "thermo", "text": "HACCP", "cue": "HACCP"},
                {"kind": "pill", "icon": "chart", "text": "Prévisions", "cue": "prévisions"}]},
            {"cue": "Vous demandez", "kicker": "Vous écrivez, il exécute", "items": [
                {"kind": "bubble", "who": "me", "text": "Quels stocks sont bas ?", "cue": "demandez"},
                {"kind": "bubble", "who": "wa", "text": "3 produits sous le seuil. Je prépare la commande fournisseur ?", "cue": "exécute"}]},
            {"cue": "Derrière lui", "kicker": "<b>6 agents</b>", "layout": "grid2", "items": [
                {"kind": "tile", "icon": "box", "color": "#007BFF", "text": "Stocks", "cue": "stocks"},
                {"kind": "tile", "icon": "thermo", "color": "#16A34A", "text": "HACCP", "cue": "HACCP"},
                {"kind": "tile", "icon": "truck", "color": "#9333EA", "text": "Achats et fournisseurs", "cue": "achats"},
                {"kind": "tile", "icon": "team", "color": "#c88100", "text": "RH et équipe", "cue": "équipe"},
                {"kind": "tile", "icon": "chef", "color": "#DC2626", "text": "Production", "cue": "production"},
                {"kind": "tile", "icon": "settings", "color": "#0EA5E9", "text": "Configuration", "cue": "configuration"}]},
            {"cue": "Et surtout", "kicker": "Il vous <em>alerte</em>", "items": [
                {"kind": "bubble", "who": "wa", "text": "⚠️ Frigo 2 : 9 °C relevé à 14h32 — seuil dépassé", "cue": "Frigo"},
                {"kind": "bubble", "who": "wa", "text": "Réception Metro non contrôlée depuis 11h", "cue": "réception"},
                {"kind": "bubble", "who": "wa", "text": "Stock saumon critique avant le service de samedi", "cue": "critique"}]},
            final("Découvrez", "tutoriel.foodeatup.com/module/predibot", "Agent IA directeur"),
        ],
    },
    # 8 ───────────────────────────────────────────────────────────────────
    "08": {
        "slug": "devenir-formateur", "vo": "08", "music": "m-entre1",
        "title": "Devenir formateur FoodEatUp",
        "comment": "Page /devenir-formateur — source : src/data/partenaires.ts (profil formateur). Seul montant publié : 50 % par formation sur place, 250 € l'après-midi.",
        "about": "Le profil formateur : missions, rémunération publiée, contenus fournis, statut.",
        "source": "`src/data/partenaires.ts` (profilsPartenaires[formateur] : remuneration, remunerationDetail, avantages, FAQ).",
        "replace": URL_REPL,
        "vo_text": "Vous aimez transmettre ? Devenez formateur FoodEatUp. Vous formez les équipes des restaurants de votre région, sur place ou à distance. Vous touchez 50 % de chaque formation sur place : 250 € par après-midi. Pas de plafond, pas d'exclusivité. Pas besoin de connaître le logiciel : vous êtes formé à FoodEatUp et au protocole MCP, avec plus de 170 vidéos, des prompts prêts à l'emploi et un compte de démonstration. Il vous faut un statut d'indépendant, ou l'envie de le devenir. Candidatez sur tutoriel.foodeatup.com/devenir-formateur.",
        "scenes": [
            {"cue": None, "note": "Accroche", "layout": "center", "items": [
                {"kind": "big", "icon": "school", "color": "#7c3aed", "text": "Formateur", "sub": "FoodEatUp", "cue": "+0"}]},
            {"cue": "Vous formez", "kicker": "Vous formez les équipes", "layout": "wrap", "items": [
                {"kind": "pill", "icon": "map", "text": "Dans votre région", "cue": "région"},
                {"kind": "pill", "icon": "shop", "text": "Sur place", "cue": "sur place"},
                {"kind": "pill", "icon": "play", "text": "À distance", "cue": "distance"}]},
            {"cue": "Vous touchez", "layout": "center", "items": [
                {"kind": "stat", "text": "50 %", "sub": "de chaque formation sur place", "cue": "cinquante"},
                {"kind": "badge", "icon": "euro", "text": "250 € l'après-midi", "cue": "deux cent"},
                {"kind": "pill", "icon": "check", "color": "#059669", "text": "Pas de plafond", "cue": "plafond"},
                {"kind": "pill", "icon": "check", "color": "#059669", "text": "Pas d'exclusivité", "cue": "d'exclusivité"}]},
            {"cue": "Pas besoin", "kicker": "Formé avant <b>votre 1re mission</b>", "items": [
                {"kind": "row", "icon": "school", "text": "FoodEatUp et protocole MCP", "cue": "formé"},
                {"kind": "row", "icon": "play", "text": "Plus de 170 vidéos", "cue": "plus de"},
                {"kind": "row", "icon": "chat", "text": "Prompts prêts à l'emploi", "cue": "prompts"},
                {"kind": "row", "icon": "shop", "text": "Compte de démonstration", "cue": "compte"}]},
            {"cue": "Il vous faut", "layout": "center", "items": [
                {"kind": "big", "icon": "card", "text": "Indépendant", "sub": "ou prêt à le devenir", "cue": "statut"}]},
            final("Candidatez", "tutoriel.foodeatup.com/devenir-formateur", "Candidatez en 10 minutes"),
        ],
    },
    # 9 ───────────────────────────────────────────────────────────────────
    "09": {
        "slug": "devenir-apporteur-affaires", "vo": "09", "music": "m-entre2",
        "title": "Devenir apporteur d'affaires FoodEatUp",
        "comment": "Page /devenir-apporteur-affaires — source : src/data/partenaires.ts (profil apporteur). Rémunération : commission sur les ventes, barème présenté au rendez-vous (aucun montant).",
        "about": "Le profil apporteur d'affaires : présenter un restaurateur, FoodEatUp fait le reste.",
        "source": "`src/data/partenaires.ts` (profilsPartenaires[apporteur-affaires] : promesse, avantages, étapes, FAQ).",
        "replace": URL_REPL,
        "vo_text": "Vous connaissez des restaurateurs débordés par leurs stocks, leur HACCP ou leurs plannings ? Présentez-les à FoodEatUp. Vous ne vendez pas, vous ne négociez pas, vous n'installez pas : la mise en relation suffit. Nous faisons la démonstration, le devis, la signature et l'installation. Vous touchez une commission sur les ventes conclues grâce à vous. Le barème est présenté au rendez-vous. Aucune exclusivité, aucun quota : un contact par an, ou dix par mois. Et vous suivez l'avancement de chaque contact. Une prise en main d'une heure suffit. Rendez-vous sur tutoriel.foodeatup.com/devenir-apporteur-affaires.",
        "scenes": [
            {"cue": None, "note": "Accroche", "layout": "center", "items": [
                {"kind": "big", "icon": "handshake", "text": "Apporteur d'affaires", "cue": "+0"},
                {"kind": "pill", "icon": "box", "text": "Stocks", "cue": "stocks"},
                {"kind": "pill", "icon": "thermo", "text": "HACCP", "cue": "HACCP"},
                {"kind": "pill", "icon": "calendar", "text": "Plannings", "cue": "plannings"}]},
            {"cue": "Présentez-les", "kicker": "Vous <b>présentez</b>", "items": [
                {"kind": "row", "icon": "cross", "color": "#dc2626", "text": "Vous ne vendez pas", "cue": "vendez"},
                {"kind": "row", "icon": "cross", "color": "#dc2626", "text": "Vous ne négociez pas", "cue": "négociez"},
                {"kind": "row", "icon": "cross", "color": "#dc2626", "text": "Vous n'installez pas", "cue": "n'installez"},
                {"kind": "badge", "icon": "check", "bg": "#059669", "text": "La mise en relation suffit", "cue": "mise"}]},
            {"cue": "Nous faisons", "kicker": "<b>Nous</b> faisons le reste", "items": [
                {"kind": "row", "num": 1, "text": "Démonstration", "cue": "démonstration"},
                {"kind": "row", "num": 2, "text": "Devis", "cue": "devis"},
                {"kind": "row", "num": 3, "text": "Signature", "cue": "signature"},
                {"kind": "row", "num": 4, "text": "Installation", "cue": "l'installation"}]},
            {"cue": "Vous touchez", "layout": "center", "items": [
                {"kind": "big", "icon": "euro", "color": "#c88100", "text": "Commission", "sub": "sur les ventes conclues", "cue": "commission"},
                {"kind": "badge", "icon": "calendar", "text": "Barème présenté au rendez-vous", "cue": "barème"}]},
            {"cue": "Aucune", "kicker": "Sans contrainte", "items": [
                {"kind": "pill", "icon": "check", "color": "#059669", "text": "Aucune exclusivité, aucun quota", "cue": "Aucune"},
                {"kind": "pill", "icon": "team", "text": "1 contact par an ou 10 par mois", "cue": "un contact"},
                {"kind": "pill", "icon": "chart", "text": "Suivi de chaque contact", "cue": "suivez"},
                {"kind": "pill", "icon": "clock", "text": "Prise en main : 1 heure", "cue": "prise"}]},
            final("Rendez-vous sur", "tutoriel.foodeatup.com/devenir-apporteur-affaires", "Vous présentez, nous concluons"),
        ],
    },
    # 10 ──────────────────────────────────────────────────────────────────
    "10": {
        "slug": "pannes-connecteur", "vo": "10", "music": "m-tech4",
        "title": "Connecteur FoodEatUp : les 5 pannes fréquentes",
        "comment": "Page /connecter-son-assistant-ia (section pannes) — source : src/data/connecteur-mcp.ts (ERREURS_FREQUENTES).",
        "about": "Les cinq pannes réelles au branchement du connecteur et leur solution.",
        "source": "`src/data/connecteur-mcp.ts` (ERREURS_FREQUENTES : symptôme, cause, solution).",
        "replace": URL_REPL,
        "vo_text": "Votre connecteur FoodEatUp ne répond pas ? Voici les cinq pannes les plus fréquentes. Un : connecté, mais aucun outil. Vérifiez que l'adresse finit bien par /mcp, puis retirez et rajoutez le connecteur. Deux : le client réclame une clé. Choisissez aucune authentification : le connecteur de l'Académie est public. Trois : erreur 406. L'en-tête Accept doit annoncer JSON et event stream ; les clients officiels le font seuls. Quatre : l'assistant répond de mémoire. Nommez la source : avec le connecteur de l'Académie FoodEatUp. Cinq : les réponses arrivent en anglais. Écrivez votre question en français. Et la page santé du connecteur affiche le nombre d'outils réellement servis.",
        "scenes": [
            {"cue": None, "note": "Accroche", "layout": "center", "items": [
                {"kind": "big", "icon": "bug", "color": "#dc2626", "text": "5 pannes", "sub": "et leur solution", "cue": "+0"}]},
            {"cue": "Un", "kicker": "<b>1</b> · Aucun outil", "items": [
                {"kind": "row", "icon": "link", "text": "L'adresse finit par /mcp", "cue": "Vérifiez"},
                {"kind": "row", "icon": "loop", "text": "Retirer, puis rajouter", "cue": "retirez"}]},
            {"cue": "Deux", "kicker": "<b>2</b> · Il réclame une clé", "items": [
                {"kind": "badge", "icon": "lock", "bg": "#059669", "text": "Authentification : aucune", "cue": "Choisissez"},
                {"kind": "row", "icon": "book", "text": "Le connecteur de l'Académie est public", "cue": "public"}]},
            {"cue": "Trois", "kicker": "<b>3</b> · Erreur 406", "items": [
                {"kind": "bubble", "who": "bot", "text": "Accept: application/json, text/event-stream", "cue": "L'en-tête"},
                {"kind": "row", "icon": "check", "color": "#059669", "text": "Les clients officiels le font seuls", "cue": "les clients"}]},
            {"cue": "Quatre", "kicker": "<b>4</b> · Réponse de mémoire", "items": [
                {"kind": "bubble", "who": "me", "text": "Avec le connecteur de l'Académie FoodEatUp, donne-moi le parcours d'un chef de rang", "cue": "Nommez"}]},
            {"cue": "Cinq", "kicker": "<b>5</b> · Réponses en anglais", "layout": "center", "items": [
                {"kind": "big", "icon": "globe", "text": "En français", "sub": "écrivez votre question en français", "cue": "Écrivez"}]},
            final("Et la page", "tutoriel.foodeatup.com/mcp/sante", "Le nombre d'outils servis"),
        ],
    },
}
