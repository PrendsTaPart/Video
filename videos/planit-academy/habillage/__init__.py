"""Gabarits d'habillage des vidéos Plan'It — ouverture, présentatrice, fin.

Trois gabarits réutilisables, tous en 1080 × 1920 / 30 fps / H.264 High. Ils ne
dépendent d'aucun épisode : on leur passe un texte, un numéro, une voix, et ils
rendent un MP4 prêt à monter.

    from pathlib import Path
    from habillage import (Ouverture, rendre_ouverture,
                           Presentatrice, rendre_presentatrice,
                           Fin, rendre_fin)

    rendre_ouverture(Ouverture(titre="Brancher un MCP", numero=13),
                     Path("out/intro.mp4"))
    rendre_presentatrice(Presentatrice(titre="Brancher un MCP",
                                       promesse="Vos logiciels métier deviennent utilisables.",
                                       numero=13, voix=Path("vo/N0.mp3")),
                         Path("out/presenter.mp4"))
    rendre_fin(Fin(suivant="Gérer ses connecteurs", couleur="#8236F8"),
               Path("out/outro.mp4"))

En ligne de commande :

    python3 -m habillage ouverture --titre "Brancher un MCP" --numero 13
    python3 -m habillage presentatrice --titre "…" --promesse "…" --voix vo/N0.mp3
    python3 -m habillage fin --suivant "Gérer ses connecteurs" --couleur "#8236F8"
"""

from .fin import Fin, rendre_fin
from .ouverture import Ouverture, rendre_ouverture
from .presentatrice import Presentatrice, rendre_presentatrice

__all__ = [
    "Ouverture", "rendre_ouverture",
    "Presentatrice", "rendre_presentatrice",
    "Fin", "rendre_fin",
]
