#!/usr/bin/env python3
"""Série 2 — « Une journée ». Dix métiers, un seul service, trois moments.

31 épisodes, en deux saisons :

    saison 1  En cuisine                   15 épisodes   EP301 → EP315
    saison 2  En salle, au bureau, ailleurs 16 épisodes  EP316 → EP331

Pourquoi ce format et pas un autre
----------------------------------
Les cinq premières séries montrent le logiciel. Celle-ci montre **le métier**,
et laisse le logiciel apparaître par contraste. Un chef de partie ne se
reconnaît pas dans une démonstration de fiche technique ; il se reconnaît dans
un vendredi 19 h 40 où il manque deux portions.

La structure avant / pendant / après n'est pas un habillage : c'est le
découpage du modèle. « Avant le service » recouvre la boucle gestion, « après »
recouvre la boucle vente, et « pendant » est le croisement lui-même — le seul
endroit où les deux boucles se touchent. Chaque épisode est donc rattaché à
une boucle sans qu'on ait à le décider au cas par cas.

La règle qui fait la série : les incidents se croisent
------------------------------------------------------
Sans ça, on obtient trente journées parallèles qui ne se touchent jamais —
c'est-à-dire trente vidéos, pas une série.

Quatre incidents traversent le service, chacun vu par trois à cinq métiers :

    LE PLAT QUI REVIENT    le chef le voit au pass, le chef de rang a pris la
                           réclamation, le plongeur le voit arriver plein, le
                           patron le retrouve en geste commercial sur le Z,
                           le client écrit l'avis le soir
    LA RUPTURE DE 19 H 40  le chef de partie tape le fond, le second cherche
                           un substitut, le serveur doit l'annoncer en salle
    LA TABLE DE DOUZE      le chef de rang encaisse le choc, la cuisine reçoit
                           douze couverts d'un coup, le patron a dit oui au
                           téléphone trois jours plus tôt
    LE CONTRÔLE SURPRISE   le plongeur est en première ligne, le chef sort les
                           relevés, le patron signe

`incident` porte le nom de l'incident vu dans l'épisode. Deux épisodes qui
partagent un incident se répondent — c'est ce que le site affichera.

Le plongeur n'a pas trois moments égaux
---------------------------------------
Cinq métiers fois trois moments font une grille propre, mais tous les métiers
n'ont pas trois moments à raconter. Le plongeur avant le service, il n'y a
presque rien. On garde les trois cases — la série a besoin de son rythme — mais
`densite` dit lesquelles sont courtes, et le montage les tient à 20 secondes
au lieu de 37,5. Une case tenue de force à trente-sept secondes se voit.
"""
import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from modele_boucles import BOUCLES, PAR_SLUG  # noqa: E402

PHASES = [
    ("avant", "Avant le service", "gestion"),
    ("pendant", "Pendant le service", "croisement"),
    ("apres", "Après le service", "vente"),
]

# ── Les dix métiers, dans l'ordre de la brigade ──────────────────────────────
# `boucles` : ce que le poste touche réellement. `amplitude` vient des journées
# du guide (`foodeatup-guide-star/src/data/metiers.ts`).

METIERS = [
    # saison 1 — en cuisine
    dict(slug="chef-de-cuisine", nom="Le chef de cuisine", saison=1,
         amplitude="07h00 → 23h00", socle="cuisine",
         boucles=["configuration", "stockvisionai", "haccp", "equipe"],
         accroche="Il ouvre, il produit, il ferme. Sa journée entière tient "
                  "dans une seule application.",
         tension="Il est le seul à voir la marge et le coup de feu en même "
                 "temps."),
    dict(slug="second", nom="Le second de cuisine", saison=1,
         amplitude="07h00 → 22h00", socle="cuisine",
         boucles=["stockvisionai", "haccp", "configuration"],
         accroche="Il tient la mise en place et le coup de feu. Son parcours "
                  "s'arrête là où commence la clôture du chef.",
         tension="Il répare ce que personne n'a vu venir, sans jamais "
                 "arrêter le service."),
    dict(slug="chef-de-partie", nom="Le chef de partie", saison=1,
         amplitude="09h00 → 22h30", socle="cuisine",
         boucles=["stockvisionai", "configuration"],
         accroche="Un poste, une carte, et la quantité juste. Trop, c'est "
                  "de la perte ; pas assez, c'est un plat retiré.",
         tension="Il est le premier à savoir qu'il va manquer quelque chose, "
                 "et le dernier qu'on écoute."),
    dict(slug="cuisinier", nom="Le cuisinier", saison=1,
         amplitude="09h30 → 22h30", socle="cuisine",
         boucles=["haccp", "stockvisionai"],
         accroche="Il exécute, il trace, il nettoie. Trois gestes, deux "
                  "cents fois.",
         tension="Ce qu'on lui demande de noter, personne ne le relit — "
                 "jusqu'au jour du contrôle."),
    dict(slug="plongeur", nom="Le plongeur", saison=1,
         amplitude="11h00 → 23h30", socle="cuisine",
         boucles=["haccp"],
         accroche="Il voit passer tout ce que la salle renvoie. C'est le "
                  "premier indicateur du restaurant, et personne ne le lit.",
         tension="Sa boucle est la seule dont l'échec ferme le restaurant."),

    # saison 2 — en salle, au bureau, ailleurs
    dict(slug="patron", nom="Le patron, directeur de salle", saison=2,
         amplitude="08h00 → minuit", socle="salle",
         boucles=["comptabilite", "equipe", "ecommerce", "fidelite"],
         accroche="Il tient la salle et les chiffres. Deux métiers, une "
                  "personne, la même journée.",
         tension="Il dit oui au téléphone trois jours avant, et il découvre "
                 "le vendredi ce que ça coûte."),
    dict(slug="chef-de-rang", nom="Le chef de rang", saison=2,
         amplitude="11h00 → 23h30", socle="salle",
         boucles=["ecommerce", "fidelite", "communication"],
         accroche="Six tables, quatre canaux, une seule mémoire. La sienne.",
         tension="Il encaisse la réclamation que la cuisine ne verra jamais."),
    dict(slug="serveur", nom="Le serveur", saison=2,
         amplitude="11h30 → 23h00", socle="salle",
         boucles=["ecommerce", "communication"],
         accroche="Il porte, il annonce, il rassure. Et il apprend les "
                  "ruptures en même temps que le client.",
         tension="Il est l'interface du restaurant, avec zéro information."),
    dict(slug="communication", nom="Le responsable de la communication",
         saison=2, amplitude="le poste n'existe pas", socle="bureau",
         boucles=["communication", "fidelite", "ecommerce"],
         accroche="Ce poste n'existe pas. C'est le patron qui poste à 23 h, "
                  "mal, quand il y pense.",
         tension="La seule boucle qui touche les sept autres est celle que "
                 "personne ne tient."),
    dict(slug="client", nom="Le client", saison=2,
         amplitude="19h30 → 22h30", socle="salle",
         boucles=["ecommerce", "fidelite"],
         accroche="Il ne verra jamais le logiciel. Il verra tout ce que le "
                  "logiciel a fait — ou pas fait.",
         tension="Son « avant le service » n'est pas la mise en place : "
                 "c'est la réservation, trois jours plus tôt."),
]

# ── Les quatre incidents qui traversent le service ───────────────────────────

INCIDENTS = {
    "plat-retour": dict(
        nom="Le plat qui revient", heure="20h15",
        quoi="Un pavé part, revient dix minutes plus tard. Trop cuit, dit la "
             "table.",
        vu_par=["chef-de-cuisine", "chef-de-rang", "plongeur", "patron",
                "client"]),
    "rupture": dict(
        nom="La rupture de 19 h 40", heure="19h40",
        quoi="Il reste deux portions de la pièce du jour, et huit tables "
             "n'ont pas commandé.",
        vu_par=["chef-de-partie", "second", "serveur", "chef-de-cuisine"]),
    "table-douze": dict(
        nom="La table de douze", heure="20h00",
        quoi="Douze couverts arrivent d'un coup. Le patron avait dit oui au "
             "téléphone, mardi.",
        vu_par=["patron", "chef-de-rang", "chef-de-cuisine", "second"]),
    "controle": dict(
        nom="Le contrôle surprise", heure="15h00",
        quoi="Un inspecteur pousse la porte entre les deux services.",
        vu_par=["plongeur", "cuisinier", "chef-de-cuisine", "patron"]),
}

# ── Ce que chaque métier vit, phase par phase ────────────────────────────────
# Trois entrées par métier : titre, ce qui se passe, l'incident traversé s'il y
# en a un, et la densité (« pleine » ou « courte »).

JOURNEES = {
    "chef-de-cuisine": [
        ("La cuisine est vide, et dans quatre heures tout doit être prêt",
         "Sept heures. Il ouvre seul, relève les températures, contrôle la "
         "livraison, et décide la carte du jour sur ce qui est arrivé.",
         None, "pleine"),
        ("Il voit la marge et le coup de feu en même temps",
         "Le pass, les quatre canaux, la table de douze qui tombe, et le pavé "
         "qui revient. Il tranche sans quitter son poste.",
         "plat-retour", "pleine"),
        ("Deux fermetures, et le chiffre avant d'éteindre",
         "Il ferme midi, il ferme le soir. Une photo pour le nettoyage, les "
         "pertes saisies, et la marge du jour qui s'affiche seule.",
         None, "pleine"),
    ],
    "second": [
        ("Il prépare ce que le chef décidera",
         "La mise en place pour deux services, sans savoir encore lesquels "
         "des plats vont partir. Il produit large, il étiquette tout.",
         None, "pleine"),
        ("Il répare sans arrêter le service",
         "Dix-neuf heures quarante : deux portions. Il trouve le substitut, "
         "prévient la salle, et rien ne s'arrête.",
         "rupture", "pleine"),
        ("Il rend une cuisine que le chef peut fermer",
         "Il range, il compte ce qui reste, il note ce qui a manqué. Sa "
         "journée s'arrête là où commence la clôture.",
         None, "courte"),
    ],
    "chef-de-partie": [
        ("La quantité juste, décidée à dix heures",
         "Son poste, sa carte, et une seule question : combien. Trop, c'est "
         "de la perte ; pas assez, c'est un plat retiré à vingt heures.",
         None, "pleine"),
        ("Il est le premier à savoir, le dernier qu'on écoute",
         "Il tape le fond du bac à 19 h 40. Il l'avait dit à dix heures.",
         "rupture", "pleine"),
        ("Ce qui reste dit ce qu'il fallait commander",
         "Il pèse ce qui n'est pas parti. C'est la seule mesure honnête de "
         "la journée, et elle arrive trop tard pour servir.",
         None, "courte"),
    ],
    "cuisinier": [
        ("Exécuter, tracer, recommencer",
         "Réception, températures, étiquettes. Trois gestes qu'on lui "
         "demande de noter et que personne ne relit.",
         None, "pleine"),
        ("Deux cents fois le même geste, sans une erreur",
         "Il envoie. Il n'a ni la vue d'ensemble ni le temps de la "
         "demander.",
         None, "pleine"),
        ("Le contrôle tombe entre les deux services",
         "Quinze heures. L'inspecteur demande les relevés du mois. Ils sont "
         "sur un cahier, ou ils sont à jour.",
         "controle", "pleine"),
    ],
    "plongeur": [
        ("Il arrive quand tout le monde est déjà là",
         "Onze heures. Rien à préparer, tout à recevoir. Sa journée commence "
         "au premier plat sale.",
         None, "courte"),
        ("Le premier indicateur du restaurant",
         "Il voit revenir les assiettes. Pleines ou vides, c'est le seul "
         "avis client qui ne ment pas — et personne ne le lui demande.",
         "plat-retour", "pleine"),
        ("Sa boucle est la seule qui ferme le restaurant",
         "Le plan de nettoyage, les relevés, la traçabilité. Les sept autres "
         "boucles coûtent de la marge. Celle-ci coûte la fermeture.",
         "controle", "pleine"),
    ],
    "patron": [
        ("Il ouvre les livres avant d'ouvrir la porte",
         "Huit heures. Le chiffre d'hier, les réservations du soir, le "
         "planning, et la table de douze qu'il a acceptée mardi.",
         "table-douze", "pleine"),
        ("Il tient la salle et les chiffres en même temps",
         "Il place, il rassure, il encaisse. Et il fait le geste commercial "
         "sur le pavé qui est revenu.",
         "plat-retour", "pleine"),
        ("Il sait avant d'éteindre s'il a gagné de l'argent",
         "Le Z, les pertes, le coût du travail du service. Trois chiffres "
         "qu'on découvre d'habitude à la fin du mois.",
         None, "pleine"),
    ],
    "chef-de-rang": [
        ("Six tables, quatre canaux, une seule mémoire",
         "Il prend son rang, relit les notes des réservations, et découvre "
         "qu'une table de douze arrive à vingt heures.",
         "table-douze", "pleine"),
        ("Il encaisse ce que la cuisine ne verra jamais",
         "La réclamation sur le pavé, c'est lui. La rupture à annoncer, "
         "c'est lui. Entre les deux, il porte.",
         "plat-retour", "pleine"),
        ("Ce qu'il sait de ses clients repart avec lui",
         "Les allergies, les habitudes, le prénom du fils. Tout est dans sa "
         "tête, et sa tête rentre chez elle à minuit.",
         None, "pleine"),
    ],
    "serveur": [
        ("Il dresse une salle dont il ne connaît pas encore la carte",
         "Onze heures trente. Il monte les tables. Le plat du jour, il "
         "l'apprendra en même temps que les clients.",
         None, "courte"),
        ("Il apprend les ruptures en même temps que le client",
         "« Je suis désolé, il n'y en a plus. » Il le découvre à la table, "
         "devant quelqu'un qui l'avait déjà choisi.",
         "rupture", "pleine"),
        ("Il range une salle et remonte la suivante",
         "Le service du soir se prépare pendant qu'on débarrasse celui du "
         "midi. Deux fois par jour, tous les jours.",
         None, "courte"),
    ],
    "communication": [
        ("Le poste que personne ne tient",
         "Il n'y a pas de responsable de la communication. Il y a un patron "
         "qui poste à vingt-trois heures, mal, quand il y pense.",
         None, "pleine"),
        ("Pendant le service, personne ne communique",
         "C'est justement l'heure où il y aurait quelque chose à montrer. "
         "Tout le monde est en salle.",
         None, "courte"),
        ("Ce qu'on aurait pu dire, et qu'on n'a pas dit",
         "Douze kilos de saumon à écouler avant vendredi. La boucle "
         "communication est la seule qui touche les sept autres — et c'est "
         "celle qui reste vide.",
         None, "pleine"),
    ],
    "client": [
        ("Son avant le service, c'est trois jours plus tôt",
         "Il cherche, il compare, il réserve. Sur le site du restaurant ou "
         "sur une plateforme qui prend sa commission — ça se joue là.",
         None, "pleine"),
        ("Il ne verra jamais le logiciel",
         "Il verra une table prête à son nom, une allergie déjà notée, un "
         "plat qui revient trop cuit. Tout ce que le logiciel a fait, ou "
         "n'a pas fait.",
         "plat-retour", "pleine"),
        ("Ce qu'il écrit le soir vaut le service entier",
         "Vingt-trois heures, dans le métro, trois étoiles. Personne au "
         "restaurant ne saura jamais que c'était le pavé.",
         "plat-retour", "pleine"),
    ],
}

# ── L'épisode supplémentaire ─────────────────────────────────────────────────
# Il ne montre pas la journée mais le mois. C'est la fermeture du huit : la
# trésorerie qui repart vers les achats.

EXTRA = dict(
    slug="expert-comptable", nom="L'expert-comptable et le patron",
    titre="Le mois, pas la journée",
    accroche="Trente journées ont fini ici.",
    quoi="Les trente services de la série arrivent sur un même tableau. Ce "
         "n'est plus un métier qu'on regarde, c'est ce que les dix métiers "
         "ont produit ensemble.",
    boucle="comptabilite", phase="apres",
)


# ── Ce que le métier dit à l'écran ───────────────────────────────────────────
# À la première personne, 25 à 30 mots. Le personnage parle de son poste, pas
# du logiciel : c'est la règle de la série. Le manque se dit, il ne se plaint
# pas — « personne ne me l'a demandé » et non « on ne m'écoute jamais ».

DITS = {
    "chef-de-cuisine/avant": "J'ouvre à sept heures. Températures, livraison, "
        "et je décide la carte du jour sur ce qui est arrivé. Personne ne "
        "verra cette heure-là.",
    "chef-de-cuisine/pendant": "Je suis le seul ici à voir la marge et le coup "
        "de feu en même temps. Alors je tranche vite, et je me trompe parfois.",
    "chef-de-cuisine/apres": "Je ferme deux fois par jour. Le soir, je veux "
        "savoir si on a gagné de l'argent avant d'éteindre — pas à la fin du "
        "mois.",
    "second/avant": "Je prépare pour deux services sans savoir encore lesquels "
        "des plats vont partir. Alors je produis large, et j'étiquette tout.",
    "second/pendant": "Vingt heures moins vingt, il reste deux portions. Je "
        "trouve autre chose, je préviens la salle, et rien ne s'arrête. "
        "C'est mon métier.",
    "second/apres": "Je rends une cuisine que le chef peut fermer. Ma journée "
        "s'arrête là où commence la sienne.",
    "chef-de-partie/avant": "Mon poste, ma carte, une seule question : "
        "combien. Trop, c'est de la perte. Pas assez, c'est un plat retiré à "
        "vingt heures.",
    "chef-de-partie/pendant": "Je tape le fond du bac à dix-neuf heures "
        "quarante. Je l'avais dit ce matin. Personne ne me l'a demandé deux "
        "fois.",
    "chef-de-partie/apres": "Je pèse ce qui n'est pas parti. C'est la seule "
        "mesure honnête de la journée, et elle arrive trop tard.",
    "cuisinier/avant": "Réception, températures, étiquettes. On me demande de "
        "tout noter. Je ne sais pas qui le relit.",
    "cuisinier/pendant": "J'envoie. Deux cents fois le même geste, sans une "
        "erreur. Je n'ai ni la vue d'ensemble ni le temps de la demander.",
    "cuisinier/apres": "Quinze heures, l'inspecteur veut les relevés du mois. "
        "Ils sont sur un cahier. On verra bien.",
    "plongeur/avant": "J'arrive quand tout le monde est déjà là. Rien à "
        "préparer : ma journée commence au premier plat sale.",
    "plongeur/pendant": "Je vois revenir les assiettes. Pleines ou vides, "
        "c'est le seul avis client qui ne ment pas. Personne ne me le demande.",
    "plongeur/apres": "Le nettoyage, la traçabilité, c'est moi. Les autres "
        "postes coûtent de la marge quand ils lâchent. Le mien coûte la "
        "fermeture.",
    "patron/avant": "J'ouvre les livres avant la porte. Le chiffre d'hier, les "
        "réservations, et la table de douze que j'ai acceptée mardi au "
        "téléphone.",
    "patron/pendant": "Je place, je rassure, j'encaisse. Et je fais le geste "
        "commercial sur le plat qui est revenu, sans savoir encore ce qu'il "
        "m'a coûté.",
    "patron/apres": "Le Z, les pertes, le coût du service. Trois chiffres "
        "qu'on découvre d'habitude à la fin du mois. Moi je les veux ce soir.",
    "chef-de-rang/avant": "Je prends mon rang, je relis les notes des "
        "réservations. Et je découvre qu'une table de douze arrive à vingt "
        "heures.",
    "chef-de-rang/pendant": "La réclamation, c'est moi. La rupture à "
        "annoncer, c'est moi. Entre les deux, je porte.",
    "chef-de-rang/apres": "Les allergies, les habitudes, le prénom du fils. "
        "Tout est dans ma tête, et ma tête rentre chez elle à minuit.",
    "serveur/avant": "Je monte les tables. Le plat du jour, je l'apprendrai en "
        "même temps que les clients.",
    "serveur/pendant": "« Je suis désolé, il n'y en a plus. » Je le découvre à "
        "la table, devant quelqu'un qui l'avait déjà choisi.",
    "serveur/apres": "Je range une salle et je remonte la suivante. Deux fois "
        "par jour, tous les jours.",
    "communication/avant": "Ce poste n'existe pas chez nous. C'est le patron "
        "qui poste à vingt-trois heures, mal, quand il y pense.",
    "communication/pendant": "Pendant le service, personne ne communique. "
        "C'est justement l'heure où il y aurait quelque chose à montrer.",
    "communication/apres": "Douze kilos de saumon à écouler avant vendredi. La "
        "seule boucle qui touche les sept autres est celle que personne ne "
        "tient.",
    "client/avant": "Je cherche, je compare, je réserve. Sur le site du "
        "restaurant ou sur une plateforme qui prend sa commission — ça se "
        "joue là.",
    "client/pendant": "Je ne verrai jamais leur logiciel. Je verrai une table "
        "à mon nom, une allergie déjà notée, ou un plat qui revient trop cuit.",
    "client/apres": "Vingt-trois heures, dans le métro, trois étoiles. "
        "Personne là-bas ne saura jamais que c'était le pavé.",
    "expert-comptable/apres": "Trente services arrivent sur le même tableau. "
        "Ce n'est plus un métier que je regarde : c'est ce que dix métiers ont "
        "produit ensemble.",
}


def episodes():
    """Les 31 épisodes, numérotés à partir de EP301."""
    out, n = [], 301
    for m in METIERS:
        for (ph, label, cote), (titre, quoi, inc, dens) in zip(
                PHASES, JOURNEES[m["slug"]]):
            # La boucle de l'épisode : celle du métier qui correspond au côté
            # de la phase. « Pendant » est le croisement — on prend alors la
            # première boucle du métier, celle qui le définit.
            candidates = [b for b in m["boucles"]
                          if cote == "croisement"
                          or PAR_SLUG[b]["grande"] == cote]
            boucle = candidates[0] if candidates else m["boucles"][0]
            out.append(dict(
                id=f"EP{n}", n=n, saison=m["saison"], metier=m["slug"],
                metierNom=m["nom"], phase=ph, phaseLabel=label,
                titre=titre, quoi=quoi, incident=inc, densite=dens,
                boucle=boucle, amplitude=m["amplitude"], socle=m["socle"],
                accrocheMetier=m["accroche"], tension=m["tension"],
                dit=DITS[f"{m['slug']}/{ph}"],
            ))
            n += 1
    out.append(dict(
        id=f"EP{n}", n=n, saison=2, metier=EXTRA["slug"],
        metierNom=EXTRA["nom"], phase=EXTRA["phase"],
        phaseLabel="Le mois entier", titre=EXTRA["titre"],
        quoi=EXTRA["quoi"], incident=None, densite="pleine",
        boucle=EXTRA["boucle"], amplitude="le mois", socle="bureau",
        accrocheMetier=EXTRA["accroche"],
        tension="Trente services deviennent un seul chiffre.",
        dit=DITS["expert-comptable/apres"],
    ))
    return out


if __name__ == "__main__":
    eps = episodes()
    print(f"{len(eps)} épisodes — "
          f"saison 1 : {sum(1 for e in eps if e['saison'] == 1)}, "
          f"saison 2 : {sum(1 for e in eps if e['saison'] == 2)}")
    croises = {}
    for e in eps:
        if e["incident"]:
            croises.setdefault(e["incident"], []).append(e["id"])
    print("\nincidents croisés :")
    for k, v in croises.items():
        print(f"  {INCIDENTS[k]['nom']:26} {len(v)} épisodes  {' '.join(v)}")
    print(f"\ncases courtes (20 s) : "
          f"{sum(1 for e in eps if e['densite'] == 'courte')}")
