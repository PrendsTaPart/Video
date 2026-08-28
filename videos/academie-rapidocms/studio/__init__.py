"""Studio de production des tutoriels vidéo RapidoCMS Académie.

    from studio import Episode, Plan, monter

Trois couches : `charte` (tokens et primitives), `habillage` (les gabarits
animés), `montage` (l'assemblage). `voix` fait la synthèse Kokoro locale et
`short` remonte l'épisode au format vertical.
"""

from .habillage import Ouverture, rendre_vignette
from .montage import Episode, Plan, dire_les_plans, monter, nettoyer
from .voix import Voix

__all__ = ["Episode", "Plan", "Ouverture", "Voix",
           "dire_les_plans", "monter", "nettoyer", "rendre_vignette"]
