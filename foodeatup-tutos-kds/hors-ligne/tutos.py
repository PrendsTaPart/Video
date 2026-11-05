# Tutoriel KDS n°14 « Wi-Fi coupé : la cuisine continue ».
# Écrans : vraie application KDS (dépôt braindcode1/foodeatup-kitchen-screen), rendue par
# outils/hors_ligne_test.dart avec le client MCP simulé (server.offline = true puis false).
# Aucun nom de restaurant à l'écran ; les points touchés viennent de ../ecrans-hors-ligne/manifeste.json.
import json, os
_M = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "ecrans-hors-ligne", "manifeste.json")))
T = [
 {"cle": "app-kds-hors-ligne", "numero": 14, "titre": "Wi-Fi coupé : la cuisine continue", "chef": "pose-08.webp",
  "hook": "Le Wi-Fi tombe, pas la cuisine",
  "ecrans": [[f] if x is None else [f, x, y] for f, x, y in _M["app-kds-hors-ligne"]],
  "etapes": ["Le bandeau signale la coupure", "Les gestes s'appliquent tout de suite", "Ils sont gardés et rejoués au retour du réseau", "Rien n'est perdu ni compté deux fois"],
  "voix": "[excited] Le Wi-Fi tombe ? La cuisine continue ! Regarde : un bandeau rouge s'affiche, hors ligne. Je touche un plat, puis BUMP : l'écran réagit tout de suite. [amazed] Les gestes sont gardés dans la tablette. Dès que le réseau revient, ils partent dans l'ordre, une seule fois. [laughs] Rien n'est perdu, t'as vu ?"},
]
