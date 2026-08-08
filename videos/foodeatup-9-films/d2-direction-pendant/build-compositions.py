#!/usr/bin/env python3
"""Génère les 8 scènes de D2 · Direction pendant le service.

Six étapes, une par scène : le film le moins dense de la série, et c'est
cohérent avec son sujet. Le directeur ne fait pas de gestes pendant le
service — il lit ce que la machine a préparé pendant qu'il faisait autre
chose. Le montage suit ce rythme : des plans plus longs, moins de coupes.

Bornes issues des timings réels de la voix (`assets/transcript.json`) :

   0,00  Onze heures quinze. Le service a commencé sans moi…
  11,63  Iris m'a construit mon calendrier de communication…
  19,98  Mes stocks dormants…
  28,58  Justement, une campagne. L'IA l'écrit…
  35,91  Mes crédits SMS et WhatsApp…
  41,28  Treize heures trente. Je synchronise mes avis Google…
  50,23  Quatorze heures. Je regarde mon service en direct…
  57,89  Je n'ai pas quitté mon bureau…
  62,16  (fin de la voix, le film court jusqu'à 66,92)

⚠️ Les deux plans d'ambiance sont des reprises, faute de plan de direction
inutilisé dans la bibliothèque au registre « avec » — le seul disponible
(`7e963f00`, sept onglets et mine résignée) appartient au registre « sans »
et n'a rien à faire ici. L'ouverture prend le plan du tableau de bord généré
par Michael ; la clôture reprend le plan de bureau de D1, ce que la phrase
« je n'ai pas quitté mon bureau » rend acceptable.
"""

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "_serie"))
from serie import Serie  # noqa: E402

s = Serie(metier=Serie.DIRECTION, sous="d2")

SCENES = {
    "d2-s1-onze-heures.html": s.carton(
        "d2-s1-onze-heures", "0.00", "11.63", "tableau-de-bord", "vid-plate-tdb",
        "Onze heures quinze", "Le service a commencé sans moi",
        title_at="1.0", sub_at="1.9",
    ),
    "d2-s2-iris.html": s.ecran(
        "d2-s2-iris", "11.63", "8.35", "11:15", "IRIS A PRÉPARÉ MON CALENDRIER",
        "SCENE-2", "vid-scene-2",
        ["Je garde", "J'écarte", "Rien ne part sans moi"],
    ),
    "d2-s3-dormants.html": s.ecran(
        "d2-s3-dormants", "19.98", "8.60", "11:30", "MES STOCKS DORMANTS",
        "SCENE-3", "vid-scene-3",
        ["Ce qui ne bouge plus", "Ce qui va périmer", "Ce qu'il faut vendre"],
    ),
    "d2-s4-campagne.html": s.ecran(
        "d2-s4-campagne", "28.58", "7.33", "11:45", "UNE CAMPAGNE, TROIS CLICS",
        "SCENE-4", "vid-scene-4",
        ["L'IA écrit", "Je relis", "Je lance"],
    ),
    "d2-s5-credits.html": s.ecran(
        "d2-s5-credits", "35.91", "5.37", "11:50", "MES CRÉDITS SMS ET WHATSAPP",
        "SCENE-5", "vid-scene-5",
        ["Pas de surprise le vendredi soir"],
    ),
    "d2-s6-avis.html": s.ecran(
        "d2-s6-avis", "41.28", "8.95", "13:30", "MES AVIS GOOGLE, SYNCHRONISÉS",
        "SCENE-6", "vid-scene-6",
        ["Au même endroit", "Pas un onglet de plus"],
    ),
    "d2-s7-stats.html": s.ecran(
        "d2-s7-stats", "50.23", "7.66", "14:00", "MON SERVICE, MODULE PAR MODULE",
        "SCENE-7", "vid-scene-7",
        ["Ce qui tourne", "Ce qui coince", "Et où"],
    ),
    "d2-s8-bureau.html": s.carton(
        "d2-s8-bureau", "57.89", "9.03", "bureau", "vid-plate-bureau",
        "Je n'ai pas quitté mon bureau", "Et je sais ce qui s'est passé en salle",
        amb_opacity=".85", title_at=".6", sub_at="1.5",
    ),
}

if __name__ == "__main__":
    s.ecrire(SCENES)
