# Série « 10 applications FoodEatUp » : 30 épisodes (TOFU, MOFU, BOFU par application).
# Chaque épisode = une liste de phrases ; chaque phrase = une scène.
# Visuels : "B:texte" mots qui claquent ; "P:ecran|mot" un écran réel ; "D:ecran1,ecran2|mot" deux écrans ;
#           "C:MOT" fin avec mot-clé à commenter.  <br> = retour à la ligne, *mot* = mot surligné.

APPS = {
 "haccp":      dict(nom="FoodEatUp HACCP", site="haccp.foodeatup.fr", note="", cle="HACCP", cible="restaurateurs"),
 "caisse":     dict(nom="FoodEatUp Caisse Mobile", site="caisse.foodeatup.fr", note="", cle="CAISSE", cible="restaurateurs"),
 "kds":        dict(nom="FoodEatUp KDS", site="kds.foodeatup.fr", note="", cle="CUISINE", cible="restaurateurs"),
 "menu":       dict(nom="FoodEatUp Menu digital", site="tablette.foodeatup.fr", note="", cle="MENU", cible="restaurateurs"),
 "fidelite":   dict(nom="FoodEatUp Fidélité", site="fidelite.foodeatup.fr", note="", cle="FIDÈLE", cible="restaurateurs"),
 "recettes":   dict(nom="FoodEatUp Recettes", site="recette.foodeatup.fr", note="", cle="RECETTE", cible="restaurateurs"),
 "production": dict(nom="FoodEatUp Production", site="prep-pilot-kitchen-flow.lovable.app", note="Aperçu · application en préparation", cle="PROD", cible="restaurateurs"),
 "labo":       dict(nom="FoodEatUp Laboratoire", site="lab.foodeatup.fr", note="", cle="LABO", cible="restaurateurs"),
 "game":       dict(nom="FoodEatUp Game", site="foodeatup.com/foodeatup-game", note="", cle="JOUER", cible="particuliers"),
 "cocuisinage":dict(nom="Cocuisinage by FoodEatUp", site="foodeatup.com/cocuisinage", note="", cle="COCUISINE", cible="particuliers"),
}
ORDRE = ["haccp", "caisse", "kds", "menu", "fidelite", "recettes", "production", "labo", "game", "cocuisinage"]
FUNNEL = ["tofu", "mofu", "bofu"]
ETIQ = {"tofu": "1/3 · Le problème", "mofu": "2/3 · Comment ça marche", "bofu": "3/3 · Passe à l'action"}

E = {}
E["haccp", "tofu"] = ("Ton classeur HACCP, rempli à 23 heures", [
 ("Vingt-trois heures. Le service est fini.", "B:23 h"),
 ("Et toi, tu remplis le classeur HACCP de toute la journée.", "B:Le *classeur*<br>de la journée"),
 ("Les températures du matin, tu les inventes un peu.", "B:Un peu *inventées*"),
 ("Le jour du contrôle, c'est la panique.", "B:Contrôle =<br>*panique*"),
 ("Et si chaque relevé se faisait en un geste, au moment où tu ouvres le frigo ?", "P:haccp/telephone-nuit-temperature.webp|Un geste"),
 ("Ou même à la voix, sans lâcher ta poêle ?", "P:haccp/telephone-nuit-jarvis.webp|À la voix"),
 ("Demain, je te montre comment.", "B:Demain,<br>*je te montre*"),
 ("Commente HACCP, je t'envoie le lien.", "C:HACCP"),
])
E["haccp", "mofu"] = ("FoodEatUp HACCP : comment ça marche", [
 ("Hier, je te parlais du classeur HACCP rempli à vingt-trois heures.", "B:Hier :<br>le *classeur*"),
 ("Voici l'application qui le remplace.", "P:haccp/telephone-nuit-accueil.webp|FoodEatUp HACCP"),
 ("Tu ouvres le frigo, tu touches l'équipement, tu notes la température.", "P:haccp/telephone-nuit-temperature.webp|Températures"),
 ("Si c'est trop chaud, elle te dit quoi faire, tout de suite.", "B:Trop chaud ?<br>*Elle te guide*"),
 ("Tu as les mains prises ? Tu lui parles.", "P:haccp/telephone-nuit-jarvis.webp|À la voix"),
 ("Elle imprime aussi tes étiquettes de date limite.", "P:haccp/telephone-nuit-etiquette.webp|Étiquettes"),
 ("Et le jour du contrôle, tout l'historique est là.", "D:haccp/telephone-contraste-historique.webp,haccp/tablette-nuit-historique.webp|Historique"),
 ("Commente HACCP, je t'envoie le lien.", "C:HACCP"),
])
E["haccp", "bofu"] = ("Passe ton HACCP sur téléphone dès cette semaine", [
 ("Ton HACCP sur ton téléphone, c'est possible dès cette semaine.", "B:Dès *cette semaine*"),
 ("Tu installes l'application sur Android.", "P:haccp/telephone-clair-accueil.webp|Android"),
 ("Tu la relies à ton compte FoodEatUp avec un simple code.", "B:Un simple<br>*code*"),
 ("Ton équipe s'entraîne d'abord en mode école, sans rien casser.", "B:Mode *école*"),
 ("Nettoyage, hygiène, traçabilité : tout est au même endroit.", "D:haccp/telephone-blanc-hygiene.webp,haccp/telephone-nuit-tracabilite.webp|Tout au même endroit"),
 ("Plus de classeur à vingt-trois heures.", "B:Fini<br>le *classeur*"),
 ("Commente HACCP, je t'envoie le lien pour l'essayer.", "C:HACCP"),
])

E["caisse", "tofu"] = ("Ton serveur fait combien d'allers-retours à la caisse ?", [
 ("Ton serveur prend la commande à table.", "B:Commande<br>*à table*"),
 ("Puis il traverse la salle pour la taper à la caisse.", "B:Aller…"),
 ("Puis il revient avec le terminal pour encaisser.", "B:…et *retour*"),
 ("Le samedi soir, ce sont des kilomètres.", "B:Des *kilomètres*"),
 ("Et si le téléphone de ton serveur devenait ta caisse ?", "P:caisse/telephone-01-accueil.webp|Ta caisse"),
 ("Demain, je te montre comment.", "B:Demain,<br>*je te montre*"),
 ("Commente CAISSE, je t'envoie le lien.", "C:CAISSE"),
])
E["caisse", "mofu"] = ("FoodEatUp Caisse Mobile : comment ça marche", [
 ("Hier, je te parlais des allers-retours à la caisse.", "B:Hier :<br>les *allers-retours*"),
 ("Avec FoodEatUp Caisse Mobile, ton serveur voit tout le plan de salle sur son téléphone.", "P:caisse/telephone-02-plan-de-salle.webp|Plan de salle"),
 ("Il prend la commande à table, plat par plat.", "P:caisse/telephone-03-commande.webp|Commande"),
 ("Elle part directement en cuisine.", "P:caisse/telephone-07-kds.webp|En cuisine"),
 ("Le client paie avec sa carte, sur le téléphone.", "P:caisse/telephone-05-paiement.webp|Sans contact"),
 ("Et le ticket est prêt.", "P:caisse/telephone-06-ticket.webp|Le ticket"),
 ("Commente CAISSE, je t'envoie le lien.", "C:CAISSE"),
])
E["caisse", "bofu"] = ("Ta caisse dans la poche de ton équipe", [
 ("Ta caisse dans la poche de ton équipe, ça se met en place vite.", "B:Dans *la poche*"),
 ("L'application s'installe sur un téléphone Android.", "P:caisse/telephone-01-accueil.webp|Android"),
 ("Tu la relies à ton compte FoodEatUp, et ta carte est déjà là.", "B:Ta carte est<br>*déjà là*"),
 ("Tes serveurs voient les commandes qui arrivent et les notifications.", "D:caisse/telephone-08-commande-entrante.webp,caisse/telephone-09-notifications.webp|En direct"),
 ("Et toi, tu suis tes chiffres de la journée.", "P:caisse/telephone-10-statistiques.webp|Tes chiffres"),
 ("Elle prend même les couleurs de ton restaurant.", "D:caisse/telephone-11-style-braise.webp,caisse/telephone-12-style-brasserie.webp|Ton style"),
 ("Commente CAISSE, je t'envoie le lien.", "C:CAISSE"),
])

E["kds", "tofu"] = ("Le coup de feu : qui sait quoi en cuisine ?", [
 ("Coup de feu. Les tickets s'empilent.", "B:Coup *de feu*"),
 ("Le chaud crie, le froid n'a rien entendu.", "B:Personne<br>*n'entend*"),
 ("La table 7 attend depuis vingt minutes.", "B:Table 7<br>*attend*"),
 ("Et le dessert part avant le plat.", "B:Le dessert<br>*avant le plat*"),
 ("Et si chaque poste voyait ses plats, et ceux des autres, en même temps ?", "P:kds/10-cuisine-grand-ecran.webp|En même temps"),
 ("Demain, je te montre comment.", "B:Demain,<br>*je te montre*"),
 ("Commente CUISINE, je t'envoie le lien.", "C:CUISINE"),
])
E["kds", "mofu"] = ("FoodEatUp KDS : l'écran de cuisine qui envoie la table en même temps", [
 ("Hier, je te parlais du coup de feu.", "B:Hier :<br>le *coup de feu*"),
 ("Avec FoodEatUp KDS, chaque poste a son écran avec ses plats à préparer.", "P:kds/01-poste-sombre.webp|Chaque poste"),
 ("Chaque ticket a son minuteur : vert, orange, puis rouge.", "P:kds/12-cuisine-tablette.webp|Minuteur"),
 ("Le cuisinier touche le ticket quand c'est prêt.", "B:Un geste :<br>*prêt*"),
 ("Au passe, on voit quand toute la table est prête.", "P:kds/03-pass.webp|Le passe"),
 ("Et la salle sait quand appeler le client.", "P:kds/17-ecran-appel.webp|Écran d'appel"),
 ("Commente CUISINE, je t'envoie le lien.", "C:CUISINE"),
])
E["kds", "bofu"] = ("Ta cuisine équipée en cinq minutes", [
 ("Ton écran de cuisine peut être prêt en quelques minutes.", "B:Prêt en<br>*quelques minutes*"),
 ("Grand écran, tablette ou téléphone : tu choisis.", "D:kds/12-cuisine-tablette.webp,kds/19-cuisine-telephone.webp|Tu choisis"),
 ("Tu le relies à FoodEatUp avec un code, sans mot de passe.", "B:Un *code*"),
 ("Toutes les commandes arrivent : salle, borne, emporter.", "P:kds/10-cuisine-grand-ecran.webp|Tout arrive"),
 ("Un guide et un mode école forment ta brigade.", "P:kds/05-guide.webp|Le guide"),
 ("Commente CUISINE, je t'envoie le lien.", "C:CUISINE"),
])

E["menu", "tofu"] = ("Ton client attend qu'on lui apporte la carte", [
 ("Ton client s'assoit. Il attend la carte.", "B:Il attend<br>*la carte*"),
 ("Puis il attend qu'on prenne sa commande.", "B:Il *attend*"),
 ("Puis il attend l'addition.", "B:Il attend<br>*encore*"),
 ("Pendant ce temps, ton équipe court partout.", "B:Ton équipe<br>*court*"),
 ("Et si ta carte vendait à ta place, directement sur la table ?", "P:menu/tablette-02-carte.webp|Sur la table"),
 ("Demain, je te montre comment.", "B:Demain,<br>*je te montre*"),
 ("Commente MENU, je t'envoie le lien.", "C:MENU"),
])
E["menu", "mofu"] = ("FoodEatUp Menu digital : la carte vivante sur chaque table", [
 ("Hier, ton client attendait la carte.", "B:Hier :<br>il *attendait*"),
 ("Avec FoodEatUp Menu digital, une tablette l'accueille sur la table.", "P:menu/tablette-01-accueil.webp|Bienvenue"),
 ("Il parcourt la carte en photos.", "P:menu/tablette-02-carte.webp|En photos"),
 ("Il choisit ses options et voit les allergènes.", "P:menu/tablette-04-fiche.webp|Options"),
 ("Il commande, et suit sa commande en direct.", "D:menu/tablette-05-panier.webp,menu/tablette-06-cuisine-en-direct.webp|En direct"),
 ("Il peut même jouer en attendant.", "P:menu/tablette-07-jeux.webp|Il joue"),
 ("Commente MENU, je t'envoie le lien.", "C:MENU"),
])
E["menu", "bofu"] = ("Mets ta carte sur tes tables", [
 ("Ta carte sur tes tables, sans rien ressaisir.", "B:Rien à<br>*ressaisir*"),
 ("Tu relies la tablette à FoodEatUp avec un code.", "B:Un *code*"),
 ("Ta carte, tes prix et tes ruptures arrivent tout seuls.", "P:menu/tablette-03-smoothies.webp|Tout seul"),
 ("Tu mets tes couleurs et ton logo.", "P:menu/c01-200-fr.webp|Tes couleurs"),
 ("Et le client rejoint ta fidélité à la fin du repas.", "P:menu/tablette-08-fidelite.webp|Fidélité"),
 ("Commente MENU, je t'envoie le lien.", "C:MENU"),
])

E["fidelite", "tofu"] = ("Ta carte de fidélité en carton est au fond d'un sac", [
 ("Ta carte de fidélité en carton ?", "B:La carte<br>en *carton*"),
 ("Elle est au fond d'un sac, ou à la poubelle.", "B:Au fond<br>*d'un sac*"),
 ("Et toi, tu ne sais même pas qui sont tes clients fidèles.", "B:Qui revient ?<br>*Mystère*"),
 ("Et si ton client rejoignait ta fidélité en dix secondes, au comptoir ?", "P:fidelite/foodeatup-01-attract.webp|10 secondes"),
 ("Demain, je te montre comment.", "B:Demain,<br>*je te montre*"),
 ("Commente FIDÈLE, je t'envoie le lien.", "C:FIDÈLE"),
])
E["fidelite", "mofu"] = ("FoodEatUp Fidélité : la fidélité en dix secondes", [
 ("Hier, je te parlais de la carte en carton.", "B:Hier :<br>le *carton*"),
 ("Avec FoodEatUp Fidélité, une tablette est posée sur ton comptoir.", "P:fidelite/bubble-coffee-01-attract.webp|Au comptoir"),
 ("Ton client tape son numéro de téléphone. C'est tout.", "P:fidelite/02-phone.webp|Son numéro"),
 ("Il voit ses points et ses récompenses.", "D:fidelite/04-home.webp,fidelite/05-rewards.webp|Ses points"),
 ("Il fait tourner la roue cadeaux.", "P:fidelite/07-wheel.webp|La roue"),
 ("Et tout remonte dans ton FoodEatUp.", "B:Tout remonte<br>*chez toi*"),
 ("Commente FIDÈLE, je t'envoie le lien.", "C:FIDÈLE"),
])
E["fidelite", "bofu"] = ("Pose ta borne de fidélité cette semaine", [
 ("Ta borne de fidélité peut être sur ton comptoir cette semaine.", "B:Cette *semaine*"),
 ("Elle prend les couleurs de ton restaurant.", "D:fidelite/boulangerie-01-attract.webp,fidelite/sushi-01-attract.webp|Tes couleurs"),
 ("Boulangerie, burger, sushi ou trattoria.", "D:fidelite/street-burger-01-attract.webp,fidelite/trattoria-01-attract.webp|Ton style"),
 ("Tu la relies à FoodEatUp avec un code.", "B:Un *code*"),
 ("Et tes clients reviennent.", "B:Ils *reviennent*"),
 ("Commente FIDÈLE, je t'envoie le lien.", "C:FIDÈLE"),
])

E["recettes", "tofu"] = ("La recette existe. Elle n'est juste jamais suivie.", [
 ("La recette existe.", "B:La recette<br>*existe*"),
 ("Elle est dans un classeur que personne n'ouvre.", "B:Un classeur<br>*fermé*"),
 ("Le nouveau te demande toutes les cinq minutes.", "B:« Chef ?<br>*Chef ?* »"),
 ("Et le même plat change selon qui le prépare.", "B:Jamais<br>*le même*"),
 ("Et si chaque recette se suivait une étape à la fois, en photo et à voix haute ?", "P:recettes/tablette-01-etape.webp|Une étape"),
 ("Demain, je te montre comment.", "B:Demain,<br>*je te montre*"),
 ("Commente RECETTE, je t'envoie le lien.", "C:RECETTE"),
])
E["recettes", "mofu"] = ("FoodEatUp Recettes : une étape à la fois", [
 ("Hier, je te parlais du classeur que personne n'ouvre.", "B:Hier :<br>le *classeur*"),
 ("Avec FoodEatUp Recettes, ton équipe choisit la recette.", "P:recettes/telephone-01-accueil.webp|Choisir"),
 ("Une étape par écran, avec la photo du geste.", "P:recettes/telephone-02-etape.webp|Une étape"),
 ("La voix lit l'étape, et le minuteur tourne.", "P:recettes/tablette-01-etape.webp|Minuteur"),
 ("Les allergènes sont en un coup d'œil.", "P:recettes/telephone-04-allergenes.webp|Allergènes"),
 ("Et toi, tu vois ce que coûte chaque recette.", "P:recettes/tablette-03-cout-complet.webp|Le coût"),
 ("Commente RECETTE, je t'envoie le lien.", "C:RECETTE"),
])
E["recettes", "bofu"] = ("Forme ton équipe dès le premier jour", [
 ("Chaque recette réussie, dès le premier jour.", "B:Dès le<br>*premier jour*"),
 ("Tu relies la tablette à FoodEatUp : tes recettes arrivent toutes seules.", "B:Rien à<br>*ressaisir*"),
 ("Tu publies des missions de formation.", "P:recettes/tablette-05-missions.webp|Missions"),
 ("Chaque employé s'entraîne sur son téléphone.", "P:recettes/telephone-05-mission.webp|S'entraîner"),
 ("Et la recette est finie, sans se tromper.", "P:recettes/telephone-03-termine.webp|Réussie"),
 ("Commente RECETTE, je t'envoie le lien.", "C:RECETTE"),
])

E["production", "tofu"] = ("La rupture découverte à neuf heures", [
 ("Neuf heures. Tu lances ta sauce tomate.", "B:9 h"),
 ("Et là, plus d'ail.", "B:Plus *d'ail*"),
 ("Ta feuille de production était sur un papier taché.", "B:Un papier<br>*taché*"),
 ("Et la traçabilité, tu la feras plus tard.", "B:Plus *tard…*"),
 ("Et si ton téléphone te disait, avant de commencer, ce qui manque ?", "P:production/01.png|Ce qui manque"),
 ("Demain, je te montre ce qu'on prépare.", "B:Demain,<br>*je te montre*"),
 ("Commente PROD, je t'envoie le lien.", "C:PROD"),
])
E["production", "mofu"] = ("FoodEatUp Production : ce qu'on prépare", [
 ("Hier, je te parlais de la rupture découverte à neuf heures.", "B:Hier :<br>la *rupture*"),
 ("On prépare FoodEatUp Production. Voici un aperçu.", "B:Un *aperçu*"),
 ("Le matin, tu vois tes productions du jour et ce qui est prêt.", "P:production/01.png|Aujourd'hui"),
 ("Il manque un ingrédient ? Tu le vois avant de commencer.", "P:production/03.png|Il manque"),
 ("La recette se met à la bonne quantité, étape par étape.", "P:production/05.png|Pas à pas"),
 ("Tu valides, et l'étiquette sort.", "P:production/06.png|Valider"),
 ("Commente PROD, je te préviens à la sortie.", "C:PROD"),
])
E["production", "bofu"] = ("Sois prévenu à la sortie de FoodEatUp Production", [
 ("FoodEatUp Production arrive bientôt.", "B:Bientôt"),
 ("Ton plan de la semaine, d'après ton stock.", "P:production/02.png|Ta semaine"),
 ("Des prévisions pour savoir combien produire.", "P:production/07.png|Prévisions"),
 ("Les courses qui manquent, prêtes pour ton fournisseur.", "P:production/08.png|Les courses"),
 ("Et ton registre de production, toujours à jour.", "P:production/09.png|Registre"),
 ("Commente PROD, je te préviens à la sortie.", "C:PROD"),
])

E["labo", "tofu"] = ("Ton labo au petit matin, avec cinq boutiques à livrer", [
 ("Quatre heures du matin. Ton labo démarre.", "B:4 h *du matin*"),
 ("Les commandes des boutiques sont arrivées par message.", "B:Des *messages*<br>partout"),
 ("Il faut produire, étiqueter, charger le camion.", "B:Produire.<br>Étiqueter.<br>*Livrer.*"),
 ("Et le siège veut ses chiffres.", "B:Le siège<br>*attend*"),
 ("Et si tout ton labo tenait sur un seul écran ?", "P:labo/hub-labo.webp|Un seul écran"),
 ("Demain, je te montre comment.", "B:Demain,<br>*je te montre*"),
 ("Commente LABO, je t'envoie le lien.", "C:LABO"),
])
E["labo", "mofu"] = ("FoodEatUp Laboratoire : ton labo sur un seul écran", [
 ("Hier, je te parlais de ton labo à quatre heures du matin.", "B:Hier :<br>*4 h du matin*"),
 ("Avec FoodEatUp Laboratoire, les commandes des boutiques arrivent au même endroit.", "P:labo/hub-labo.webp|Les commandes"),
 ("Tu vois ce qu'il faut produire aujourd'hui.", "P:labo/production.webp|Production"),
 ("Tu prépares chaque boutique, carton par carton.", "P:labo/picking.webp|Préparation"),
 ("Et les tournées de livraison sont prêtes.", "P:labo/tournees.webp|Tournées"),
 ("Commente LABO, je t'envoie le lien.", "C:LABO"),
])
E["labo", "bofu"] = ("Essaie FoodEatUp Laboratoire gratuitement", [
 ("Ton labo sur un seul écran, tu peux l'essayer.", "B:Essaie-le"),
 ("Sur ordinateur dans le labo.", "P:labo/fabrication.webp|Au labo"),
 ("Et sur téléphone, au poste.", "D:labo/m-production.webp,labo/m-fabrication.webp|Sur téléphone"),
 ("L'essai est gratuit pendant sept jours.", "B:Essai gratuit<br>*7 jours*"),
 ("Commente LABO, je t'envoie le lien.", "C:LABO"),
])

E["game", "tofu"] = ("Ton client attend son plat en fixant son téléphone", [
 ("Ton client attend son plat.", "B:Il *attend*"),
 ("Il fait défiler son téléphone, et il oublie où il est.", "B:Il *oublie*<br>où il est"),
 ("Et si, pendant ce temps, il jouait à un jeu de ton restaurant ?", "P:game/coup-de-feu.webp|Il joue"),
 ("Et qu'il gagnait un dessert ?", "B:Un dessert<br>*à gagner*"),
 ("Demain, je te montre comment.", "B:Demain,<br>*je te montre*"),
 ("Commente JOUER, je t'envoie le lien.", "C:JOUER"),
])
E["game", "mofu"] = ("FoodEatUp Game : des mini-jeux faits pour les restaurants", [
 ("Hier, ton client attendait son plat.", "B:Hier :<br>il *attendait*"),
 ("FoodEatUp Game, c'est un magasin de mini-jeux sur le thème du restaurant.", "D:game/coup-de-feu.webp,game/burger-architect.webp|Mini-jeux"),
 ("Course, cuisine, réflexion, adresse.", "D:game/sushi-tempo.webp,game/barista-minute.webp|Pour tous"),
 ("Pas de compte, pas de publicité, et ça marche même sans connexion.", "B:Pas de compte.<br>*Pas de pub.*"),
 ("Et avec l'adresse de ton restaurant, il joue à tes jeux, avec ton lot à gagner.", "P:game/pizza-creator.webp|Ton lot"),
 ("Commente JOUER, je t'envoie le lien.", "C:JOUER"),
])
E["game", "bofu"] = ("Télécharge FoodEatUp Game", [
 ("FoodEatUp Game, c'est gratuit.", "B:*Gratuit*"),
 ("Sur téléphone et sur tablette Android.", "P:game/bubble-tea-lab.webp|Android"),
 ("Pour patienter, pour s'amuser en famille, ou pour gagner un lot dans ton restaurant préféré.", "D:game/chef-mystere.webp,game/burger-architect.webp|En famille"),
 ("Restaurateur ? Tes clients jouent, et ils reviennent.", "B:Ils *reviennent*"),
 ("Commente JOUER, je t'envoie le lien.", "C:JOUER"),
])

E["cocuisinage", "tofu"] = ("Ce soir, on mange quoi ?", [
 ("Ce soir, on mange quoi ?", "B:On mange<br>*quoi ?*"),
 ("Tu ouvres le frigo, et tu n'as aucune idée.", "B:Aucune<br>*idée*"),
 ("Et si les restaurants que tu aimes te donnaient leurs recettes ?", "P:cocuisinage/05-recette-nutrition.png|Leurs recettes"),
 ("Et te disaient quoi cuisiner avec ce que tu as chez toi ?", "P:cocuisinage/08-frigo.png|Ton frigo"),
 ("Demain, je te montre comment.", "B:Demain,<br>*je te montre*"),
 ("Commente COCUISINE, je t'envoie le lien.", "C:COCUISINE"),
])
E["cocuisinage", "mofu"] = ("Cocuisinage : tes restaurants dans ta poche", [
 ("Hier, je te demandais : ce soir, on mange quoi ?", "B:Hier :<br>*on mange quoi ?*"),
 ("Cocuisinage, c'est l'application de tes restaurants préférés.", "P:cocuisinage/01-pour-toi.png|Tes restaurants"),
 ("Tu découvres les lieux près de chez toi.", "P:cocuisinage/02-explorer.png|Explorer"),
 ("Tu cuisines leurs recettes, étape par étape.", "P:cocuisinage/60-pas-a-pas.png|Pas à pas"),
 ("Tu planifies tes repas, et ta liste de courses se fait toute seule.", "D:cocuisinage/06-mon-assiette.png,cocuisinage/07-courses.png|Tes repas"),
 ("Tu scannes un produit pour savoir s'il est bon.", "P:cocuisinage/09-scanner.png|Scanner"),
 ("Commente COCUISINE, je t'envoie le lien.", "C:COCUISINE"),
])
E["cocuisinage", "bofu"] = ("Rejoins Cocuisinage", [
 ("Cocuisinage, c'est pour toi, à la maison.", "B:Pour *toi*"),
 ("Tu réserves une table ou tu commandes chez tes restaurants.", "D:cocuisinage/15-reserver.png,cocuisinage/16-commander.png|Réserver"),
 ("Tu gardes toutes tes cartes de fidélité au même endroit.", "P:cocuisinage/45-portefeuille-cartes.png|Tes cartes"),
 ("Et tu poses tes questions de cuisine au chef.", "P:cocuisinage/64-parler-au-chef.png|Le chef"),
 ("Commente COCUISINE, je t'envoie le lien.", "C:COCUISINE"),
])

def episodes():
    out = []
    n = 0
    for a in ORDRE:
        for f in FUNNEL:
            n += 1
            titre, phrases = E[a, f]
            out.append(dict(n=n, app=a, funnel=f, titre=titre, phrases=phrases,
                            slug=f"ep{n:02d}-{a}-{f}", **{k: v for k, v in APPS[a].items()}))
    return out

if __name__ == "__main__":
    import json
    eps = episodes()
    for e in eps:
        txt = " ".join(p[0] for p in e["phrases"])
        print(e["n"], e["slug"], len(txt.split()), "mots")
    json.dump(eps, open(__file__.replace("episodes.py", "episodes.json"), "w"), ensure_ascii=False, indent=1)
