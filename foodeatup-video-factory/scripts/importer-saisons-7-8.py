#!/usr/bin/env python3
"""Fait entrer les saisons 7 et 8 dans l'inventaire de l'usine.

    python3 scripts/importer-saisons-7-8.py [chemin/vers/le/site]

Pourquoi ce script existe.

`gen-site-data.py` réécrit `src/data/series.ts` et `src/data/contenu.ts` du site
à partir de `data/series.json`. Les saisons 7 et 8 ont été écrites directement
dans le site, sans passer par ici : à la première régénération, elles
disparaissaient — soixante épisodes, leurs cinq textes de post, leurs quatre
prompts. Ce script les rapatrie une bonne fois, dans le format de l'inventaire.

Il ne tourne qu'une fois. Ensuite, la vérité est ici, et le site en découle.

Il remplit aussi `story.url` sur tous les épisodes dont la story est montée :
le champ existait, il n'avait jamais été renseigné.

Et il rapatrie le calendrier. Trois décisions avaient été prises côté site sans
remonter ici : les dates de la saison 6, celles des saisons 7 et 8, et le
recalage d'EP010 dont la publication Facebook tombait un jour avant l'épisode
lui-même, sur un jour déjà pris. Sans ce rapatriement, la première
régénération les effaçait toutes les trois.
"""
import json, os, re, sys

R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INVENTAIRE = os.path.join(os.path.dirname(R), "foodeatup-social", "data", "series.json")
DIST = os.path.join(R, "dist")
BRANCHE = ("https://raw.githubusercontent.com/PrendsTaPart/Video/"
           "claude/foodeatup-video-production-8slc4o/foodeatup-video-factory/dist")

# Ce que `gen-site-data.py` sort de l'épisode pour le ranger dans contenu.ts.
# Le chemin inverse : on remet ces champs dans l'épisode de l'inventaire.
DEPUIS_CONTENU = ("scriptHeygen", "kit", "heygenPrompt", "montage",
                  "carrousel", "imageFacebook", "metier", "phase")


def bloc_json(src, marque, fin):
    i = src.index(marque) + len(marque)
    j = src.index(fin, i) + len(fin)
    return json.loads(src[i:j - 1])


def lire_site(site):
    s = open(os.path.join(site, "src/data/series.ts"), encoding="utf-8").read()
    series = bloc_json(s, "export const series: Serie[] = ", "\n];")
    c = open(os.path.join(site, "src/data/contenu.ts"), encoding="utf-8").read()
    m = "export const contenuParEpisode: Record<string, ContenuEpisode> = "
    contenu = bloc_json(c, m, "\n};")
    return series, contenu


def episode_inventaire(e, contenu):
    """L'épisode du site, remis dans la forme de l'inventaire."""
    ep = dict(e)
    c = contenu.get(e["id"], {})

    # Les textes de post redescendent dans chaque réseau.
    for reseau, pub in ep["reseaux"].items():
        pub.update(c.get("publications", {}).get(reseau, {}))

    ep["promptVignette"] = c.get("promptVignette", "")
    ep["higgsfield"] = dict(ep["higgsfield"])
    ep["higgsfield"]["prompt"] = c.get("higgsfieldPrompt")
    for k in DEPUIS_CONTENU:
        if c.get(k) is not None:
            ep[k] = c[k]

    # La story : l'objet descriptif de l'inventaire, pas l'URL toute seule.
    url = ep.pop("storyUrl", None)
    ep["story"] = {
        "format": "9:16 · 1080 × 1920 · 10 s",
        "hook": e["accroche"].rstrip(" .").strip(),
        "punchline": e["punchline"].rstrip(" .").strip(),
        "url": url,
    }
    ep["tutoriel"] = e.get("tutoriel")
    return ep


def main():
    site = sys.argv[1] if len(sys.argv) > 1 else "/workspace/food-series-hub-9214dbe2"
    series_site, contenu = lire_site(site)
    inv = json.load(open(INVENTAIRE, encoding="utf-8"))

    saisons_site = {sa["numero"]: sa for sa in series_site[0]["saisons"]}
    cible = inv["series"][0]
    presentes = {sa["numero"] for sa in cible["saisons"]}

    ajoutees = 0
    for numero in (7, 8):
        if numero in presentes:
            cible["saisons"] = [sa for sa in cible["saisons"] if sa["numero"] != numero]
        sa = saisons_site[numero]
        cible["saisons"].append({
            "numero": sa["numero"],
            "titre": sa["titre"],
            "pitch": sa["pitch"],
            "episodes": [episode_inventaire(e, contenu) for e in sa["episodes"]],
        })
        ajoutees += len(sa["episodes"])
    cible["saisons"].sort(key=lambda s: s["numero"])

    # `story.url` sur tout épisode dont la story est montée — le champ existait
    # depuis le début, il n'avait jamais été renseigné.
    montees = {f[:-4] for f in os.listdir(os.path.join(DIST, "stories")) if f.endswith(".mp4")}
    remplies = 0
    for s in inv["series"]:
        for sa in s["saisons"]:
            for e in sa["episodes"]:
                st = e.get("story")
                if isinstance(st, dict) and not st.get("url") and e["id"] in montees:
                    st["url"] = f"{BRANCHE}/stories/{e['id']}.mp4"
                    remplies += 1

    # Le calendrier vient du site : c'est là qu'il a été décidé, épisode par
    # épisode, et l'inventaire ne l'a jamais su.
    dates = {
        e["id"]: (e["datePrevue"], {r: p["date"] for r, p in e["reseaux"].items()})
        for sa in series_site[0]["saisons"] for e in sa["episodes"]
    }
    recales = 0
    for sa in cible["saisons"]:
        for e in sa["episodes"]:
            d = dates.get(e["id"])
            if not d:
                continue
            prevue, par_reseau = d
            avant = (e.get("datePrevue"), {r: p.get("date") for r, p in e["reseaux"].items()})
            e["datePrevue"] = prevue
            for r, p in e["reseaux"].items():
                if r in par_reseau:
                    p["date"] = par_reseau[r]
            if avant != (prevue, par_reseau):
                recales += 1

    json.dump(inv, open(INVENTAIRE, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print(f"calendrier rapatrié : {recales} épisodes recalés")
    total = sum(len(sa["episodes"]) for sa in cible["saisons"])
    print(f"saisons 7 et 8 importées : {ajoutees} épisodes — la série en compte {total}")
    print(f"story.url renseignée sur {remplies} épisodes")


if __name__ == "__main__":
    main()
