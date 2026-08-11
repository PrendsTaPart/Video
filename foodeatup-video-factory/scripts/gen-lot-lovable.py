#!/usr/bin/env python3
"""Assemble un prompt Lovable par lot de 10 épisodes montés.

Pourquoi des lots : un tour Lovable coûte des crédits, qu'il traite un épisode
ou dix. Envoyer les vignettes une par une, c'est payer 150 tours pour un travail
qui en demande 15.

Le lot se remplit avec les épisodes **montés**, dans l'ordre de production — pas
dans l'ordre des numéros. Un épisode bloqué ne bloque pas le lot : il y entrera
quand il sera monté, dans un lot ultérieur. Sinon un seul chapitre Drive manquant
gèlerait dix vignettes.

  ./gen-lot-lovable.py          # état des lots, et écrit ceux qui sont complets
  ./gen-lot-lovable.py --force  # écrit aussi le lot en cours, même incomplet
"""
import json, os, sys, math

R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SOCIAL = os.path.join(os.path.dirname(R), "foodeatup-social")
TAILLE = 10
PHOTO = ("https://raw.githubusercontent.com/PrendsTaPart/Video/"
         "claude/foodeatup-video-factory-wtb7gs/foodeatup-social/"
         "public/brand/chef-foodeatup.jpg")

ENTETE = """# Lot {n} — vignettes des épisodes {premier} à {dernier}

À coller dans Lovable **en un seul message**, avec la photo du chef en pièce
jointe. Un tour, dix vignettes.

---

L'image jointe est la photo officielle du chef FoodEatUp — la même que sur les
lots précédents. Elle est aussi ici : {photo}

Génère les {nb} vignettes ci-dessous, une par épisode, en utilisant cette photo
comme image de référence et le prompt de chaque épisode tel quel.

**Le chef ne se redessine pas.** Même visage, même barbe, même toque, même
tablier au logo FoodEatUp. C'est la même personne sur les 150 épisodes, c'est ce
qui fait la série. Si une image sort avec un autre visage, refais-la plutôt que
de l'accepter.

Enregistre chaque image dans `public/vignettes/EPxxx.jpg` au format 9:16, et fais
pointer le `posterUrl` de l'épisode correspondant dessus dans `src/data/series.ts`.

Mets aussi à jour, pour ces {nb} épisodes, les trois liens de la bibliothèque
RapidoCMS : `masterRapidoUrl` (la vidéo montée), `higgsfield.videoSourceUrl` (le
clip d'origine de dix secondes) et `posterUrl`. Ils sont dans le fichier de
données rechargé — ne les invente pas.

Ne touche à rien d'autre dans le projet : ce message ne concerne que ces {nb}
images et les champs de ces {nb} épisodes.

## Trois défauts du premier jet, à ne pas reproduire

Les 300 vignettes générées jusqu'ici ont trois problèmes. Ils viennent d'une
lecture rapide de la consigne, pas d'une limite de l'outil.

1. **Le grisé ne se cuit pas dans l'image.** Les épisodes non sortis étaient
   désaturés dans le fichier JPEG. Le jour où l'épisode sort, sa vignette reste
   grise. Le grisé est un état, il est déjà posé en CSS par le site. Génère
   TOUTES les images en couleur, sans exception.

2. **Un seul logo.** Le tablier du chef porte déjà le logo FoodEatUp. N'ajoute
   aucun second badge, en bas à droite ni ailleurs — et surtout pas un logo
   redessiné. Deux marques sur la même image, dont une fausse, c'est le défaut
   le plus visible du premier jet.

3. **Chaque épisode a sa scène.** Les 300 premières images réutilisaient le même
   décor et la même pose, seul le texte changeait. Le prompt de chaque épisode
   décrit un gag précis et un décor de saison : suis-le. Si deux épisodes de la
   même saison sortent identiques, l'image n'a pas été lue.

"""


def episodes_montes():
    d = json.load(open(os.path.join(SOCIAL, "data", "series.json")))
    eps = [e for s in d["series"] for sa in s["saisons"] for e in sa["episodes"]]
    return sorted([e for e in eps if e["statut"] in ("publie", "monte")],
                  key=lambda e: e["numero"])


def ecrire(lot, n):
    d = os.path.join(SOCIAL, "lots")
    os.makedirs(d, exist_ok=True)
    corps = [ENTETE.format(n=n, premier=lot[0]["id"], dernier=lot[-1]["id"],
                           photo=PHOTO, nb=len(lot))]
    for e in lot:
        corps += [f"## {e['id']} — {e['titre']} · « {e['troisMots']} »", "",
                  f"*Saison {e['saison']} · {e['module']} · {e['chapitre']}*", "",
                  "```", e["promptVignette"], "```", ""]
    p = os.path.join(d, f"lot-{n:02d}.md")
    open(p, "w").write("\n".join(corps))
    return p


def main():
    force = "--force" in sys.argv
    montes = episodes_montes()
    total_lots = math.ceil(150 / TAILLE)
    print(f"{len(montes)} épisodes montés · {total_lots} lots prévus pour les 150")
    ecrits = []
    for i in range(0, len(montes), TAILLE):
        lot = montes[i:i + TAILLE]
        n = i // TAILLE + 1
        if len(lot) == TAILLE:
            ecrits.append(ecrire(lot, n))
            print(f"  lot {n:02d} — complet, {lot[0]['id']} → {lot[-1]['id']}")
        elif force:
            ecrits.append(ecrire(lot, n))
            print(f"  lot {n:02d} — INCOMPLET ({len(lot)}/{TAILLE}), écrit sur --force")
        else:
            manque = TAILLE - len(lot)
            print(f"  lot {n:02d} — {len(lot)}/{TAILLE}, il manque {manque} épisode(s) "
                  f"monté(s) avant d'envoyer le prompt")
    for p in ecrits:
        print("  ->", os.path.relpath(p, os.path.dirname(R)))


if __name__ == "__main__":
    main()
