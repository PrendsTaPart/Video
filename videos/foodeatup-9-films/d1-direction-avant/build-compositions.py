#!/usr/bin/env python3
"""Génère les 9 scènes de D1 · Direction avant le service.

Premier film du parcours direction : liseré `#475569`, le gris ardoise.

Le film le plus dense de la série — 14 étapes en 72 secondes. Il tient parce
que les étapes s'enchaînent par blocs : achats, réception, comptabilité,
équipe. Chaque scène enchaîne deux ou trois écrans du même bloc plutôt que
d'en isoler un, ce qui donne au montage le rythme d'un tour de table plutôt
que celui d'une démonstration.

Une seule étape n'a aucune fiche — le traitement des congés (10h50). Elle
passe en schéma animé. Le schéma est écrit ici plutôt que dans la grammaire
commune : il ne sert qu'à ce film.

Bornes issues des timings réels de la voix (`assets/transcript.json`) :

   0,00  Huit heures. Le restaurant est vide…
   7,67  PrediBot me dit ce qui va sortir…
  19,51  De ces deux-là, je déduis mes besoins…
  27,41  J'envoie mes commandes aux fournisseurs…
  35,27  Mes factures partent dans les dépenses…
  42,75  Dix heures. Mon équipe…
  50,95  Une demande de congé arrive…                 (schéma animé)
  55,71  Je vérifie les pointages de la semaine…
  63,27  Onze heures. Je n'ai encore parlé à personne…
  67,68  (fin de la voix, le film court jusqu'à 72,60)
"""

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "_serie"))
from serie import Serie  # noqa: E402

s = Serie(metier=Serie.DIRECTION, sous="d1")

# Schéma du traitement d'un congé : une demande, une réponse, et le planning
# qui se met à jour de lui-même. Le sujet est la propagation, pas le
# formulaire — c'est pour ça qu'aucune capture ne conviendrait ici.
CONGE_HTML = """          <div class="md-card" id="mdDemande" style="top:60px;">
            <div class="nom">Congé — 14 au 18 avril</div>
            <div class="prix">Nadia · service du soir</div>
          </div>
          <div class="md-canal" id="mdRep" style="left:210px; top:360px;">Accepté<span class="etat">en un clic</span></div>
          <div class="md-canal" id="mdPlan" style="left:950px; top:360px;">Planning<span class="etat" id="mdPlanEtat">à replanifier</span></div>
          <div class="md-lien" id="mdFleche" style="left:610px; width:340px; top:412px;"></div>
"""
CONGE_JS = (
    '        tl.fromTo("#mdDemande", { opacity:0, y:-16 }, { opacity:1, y:0, duration:.35, ease:"back.out(1.5)" }, .45);\n'
    '        tl.fromTo("#mdRep", { opacity:0, scale:.85 }, { opacity:1, scale:1, duration:.3, ease:"back.out(1.8)" }, 1.2);\n'
    '        tl.fromTo("#mdPlan", { opacity:0, scale:.85 }, { opacity:1, scale:1, duration:.3, ease:"back.out(1.8)" }, 1.45);\n'
    '        tl.to("#mdFleche", { scaleX:1, duration:.35, ease:"power2.out" }, 2.0);\n'
    # La bascule : c'est le planning qui se met à jour, pas le manager.
    '        tl.to("#mdPlanEtat", { opacity:0, duration:.15 }, 2.4);\n'
    '        tl.set("#mdPlanEtat", { innerText:"à jour", color:"#059669" }, 2.55);\n'
    '        tl.to("#mdPlanEtat", { opacity:1, duration:.2 }, 2.55);\n'
    '        tl.to("#mdPlan", { borderColor:"#059669", duration:.3 }, 2.55);\n'
)

SCENES = {
    "d1-s1-huit-heures.html": s.carton(
        "d1-s1-huit-heures", "0.00", "7.67", "directeur-bureau", "vid-plate-bureau",
        "Huit heures", "La journée est déjà écrite quelque part",
        title_at=".8", sub_at="1.6",
    ),
    "d1-s2-previsions.html": s.ecran(
        "d1-s2-previsions", "7.67", "11.84", "08:00", "CE QUI VA SORTIR AUJOURD'HUI",
        "SCENE-2", "vid-scene-2",
        ["PrediBot", "StockVision", "Plus au feeling"],
    ),
    "d1-s3-courses.html": s.ecran(
        "d1-s3-courses", "19.51", "7.90", "08:30", "MA LISTE SE REMPLIT SEULE",
        "SCENE-3", "vid-scene-3",
        ["Besoins déduits", "Produit par produit", "Avec les quantités"],
    ),
    "d1-s4-fournisseurs.html": s.ecran(
        "d1-s4-fournisseurs", "27.41", "7.86", "08:50", "COMMANDES, LIVRAISONS, BONS",
        "SCENE-4", "vid-scene-4",
        ["Commandes envoyées", "Livraisons suivies", "BL validé"],
    ),
    "d1-s5-factures.html": s.ecran(
        "d1-s5-factures", "35.27", "7.48", "09:30", "CHAQUE FACTURE, SA LIVRAISON",
        "SCENE-5", "vid-scene-5",
        ["Classées", "Reliées", "Rien à reconstituer"],
    ),
    "d1-s6-equipe.html": s.ecran(
        "d1-s6-equipe", "42.75", "8.20", "10:30", "MON ÉQUIPE, MA SEMAINE",
        "SCENE-6", "vid-scene-6",
        ["Tâches assignées", "Planning publié", "Et imprimé"],
    ),
    # Schéma animé : le traitement des congés n'a aucune fiche.
    "d1-s7-conge.html": s.motion(
        "d1-s7-conge", "50.95", "4.76", "10:50", "UNE DEMANDE DE CONGÉ",
        CONGE_HTML, CONGE_JS, ["Une seule réponse", "Le planning suit"],
    ),
    "d1-s8-pointages.html": s.ecran(
        "d1-s8-pointages", "55.71", "7.56", "11:00", "LES POINTAGES DE LA SEMAINE",
        "SCENE-8", "vid-scene-8",
        ["Ce qui a été travaillé", "Un relevé, pas une estimation"],
    ),
    "d1-s9-onze-heures.html": s.carton(
        "d1-s9-onze-heures", "63.27", "9.33", "directeur-portrait", "vid-plate-portrait",
        "Je n'ai encore parlé à personne", "Et tout est déjà en route",
        amb_opacity=".85", title_at=".6", sub_at="1.5",
    ),
}

if __name__ == "__main__":
    s.ecrire(SCENES)
