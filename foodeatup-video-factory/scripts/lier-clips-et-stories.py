#!/usr/bin/env python3
"""Relie à l'inventaire les clips et les stories présents sur le disque.

    python3 scripts/lier-clips-et-stories.py

Un fichier dans `dist/hooks/` ou `dist/stories/` ne sert à rien tant que
l'inventaire ne porte pas son adresse : le site lit l'inventaire, pas le disque.
Vingt-quatre clips récupérés sur Higgsfield ont vécu plusieurs semaines dans ce
trou — écrits directement sur le site, jamais rapatriés ici, puis effacés à la
première régénération. Ce script ferme le trou dans les deux sens : ce qui est
sur le disque obtient une adresse, et ce qui avait déjà une adresse sur le site
la retrouve.

Deux hébergements, et ce n'est pas un hasard :

  `clips-du-site.json` porte les adresses S3 de RapidoCMS, pour les clips qui y
  ont été téléversés. Elles priment : c'est l'hébergement de production.

  Tout le reste est servi depuis ce dépôt, par `raw.githubusercontent.com` —
  c'est déjà le cas des cent quarante-six stories. Un fichier commité ne
  disparaît pas ; une URL de CDN de générateur, si.

Le script ne remplace jamais une adresse déjà posée.
"""
import json
import os
import pathlib
import subprocess

R = pathlib.Path(__file__).resolve().parent.parent
SOCIAL = R.parent / "foodeatup-social"
INVENTAIRE = SOCIAL / "data" / "series.json"
REPRISES = SOCIAL / "data" / "clips-du-site.json"

# Le nom de la branche est inscrit dans chaque adresse publiée. Ce n'est pas
# un détail de configuration : mille six cents URL en dépendent, et retirer la
# branche qu'elles nomment les casse toutes d'un coup. Elle change ici, et
# partout dans l'inventaire en même temps — jamais l'un sans l'autre.
BRANCHE = "claude/foodeatup-video-production-8slc4o"
BRUT = f"https://raw.githubusercontent.com/PrendsTaPart/Video/{BRANCHE}/foodeatup-video-factory/dist"


def duree_lisible(f):
    """« 5 min 55 » — la durée telle qu'on l'affiche à côté du lecteur."""
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "csv=p=0", str(f)], capture_output=True, text=True).stdout.strip()
    if not out:
        return None
    s = int(float(out))
    return f"{s // 60} min {s % 60:02d}"


def main():
    d = json.load(open(INVENTAIRE, encoding="utf-8"))
    reprises = json.load(open(REPRISES, encoding="utf-8")) if REPRISES.exists() else {}

    hooks = {p.stem for p in (R / "dist" / "hooks").glob("*.mp4")}
    stories = {p.stem for p in (R / "dist" / "stories").glob("*.mp4")}
    shorts = {p.stem for p in (R / "dist" / "youtube").glob("*.mp4")}
    paysages = {p.stem for p in (R / "dist" / "youtube-paysage").glob("*.mp4")}
    facebooks = {p.stem for p in (R / "dist" / "facebook").glob("*.mp4")}
    # `dist/tiktok/` porte les masters de 37,5 s, pas cette famille-là.
    tiktoks = {p.stem for p in (R / "dist" / "tiktok-story").glob("*.mp4")}
    masters = {p.stem for p in (R / "dist" / "tiktok").glob("*.mp4")}

    clips, sts, yts, pys, fbs, tks, bas, deja = 0, 0, 0, 0, 0, 0, 0, 0
    mst = 0
    films = 0
    for s in d["series"]:
        # Le film assemblé, au niveau de la série. `GeneriqueFilm` ne portait
        # que les mentions de l'affiche : de quoi annoncer un film, pas de quoi
        # le montrer. C'est ce fichier que l'accueil prend en hero.
        f = s.get("film")
        if f:
            film = R / "dist" / "film" / f"{s['slug']}.mp4"
            if not film.exists():
                film = R / "dist" / "film" / "upeatfood.mp4"
            pose = f.get("url")
            url = reprises.get(f"film-{s['slug']}", {}).get("url") or pose or (
                f"{BRUT}/film/{film.name}" if film.exists() else None
            )
            if url and url != pose:
                f["url"] = url
                f["duree"] = duree_lisible(film) if film.exists() else None
                films += 1

        for sa in s["saisons"]:
            # La bande-annonce a elle aussi sa version YouTube : même montage,
            # plus le carton de fin. Elle est rangée sous la clé de fichier
            # `<serie>-S<n>`, qui sert aussi de clé de reprise — les reprises
            # sont indexées par nom de fichier, pas par identifiant d'épisode.
            ba = sa.get("bandeAnnonce")
            if ba:
                cle = f"{s['slug']}-S{sa['numero']}"
                for champ, dossier, presents in (
                    ("shortUrl", "youtube", shorts),
                    ("videoYoutubeUrl", "youtube-paysage", paysages),
                    ("storyFacebookUrl", "facebook", facebooks),
                    ("videoTiktokUrl", "tiktok-story", tiktoks),
                ):
                    pose = ba.get(champ)
                    url = reprises.get(cle, {}).get(champ) or pose or (
                        f"{BRUT}/{dossier}/{cle}.mp4" if cle in presents else None
                    )
                    if url and url != pose:
                        ba[champ] = url
                        bas += 1

            for e in sa["episodes"]:
                i = e["id"]
                repris = reprises.get(i, {})

                # Une reprise l'emporte sur ce qui est déjà posé : c'est tout
                # son objet. Elle sert à basculer un épisode du dépôt vers
                # RapidoCMS, or l'adresse du dépôt est justement là avant elle.
                # Ne remplir que les cases vides revenait à ne jamais basculer.
                actuel = e["higgsfield"].get("videoSourceUrl")
                if not actuel or repris.get("videoSourceUrl"):
                    url = repris.get("videoSourceUrl") or actuel or (
                        f"{BRUT}/hooks/{i}.mp4" if i in hooks else None
                    )
                    if url and url != actuel:
                        e["higgsfield"]["videoSourceUrl"] = url
                        clips += 1
                    elif url:
                        deja += 1
                else:
                    deja += 1

                # Le master de 37,5 s. Il manquait à ce script, et le trou
                # s'est vu quand une autre session a monté trente-neuf masters
                # d'un coup : les fichiers étaient là, le site n'en servait
                # aucun. Un montage sans adresse n'existe pour personne.
                pose = e.get("videoUrl")
                url = repris.get("videoUrl") or pose or (
                    f"{BRUT}/tiktok/{i}.mp4" if i in masters else None
                )
                if url and url != pose:
                    e["videoUrl"] = url
                    if not e.get("dureeSecondes"):
                        e["dureeSecondes"] = 37.5
                    mst += 1
                # L'adresse et le statut vont ensemble, dans les deux sens : le
                # site refuse un épisode sorti sans vidéo autant qu'une vidéo
                # sur un épisode pas sorti. C'est un test qui l'a appris, pas
                # une relecture.
                #
                # Le rattrapage est hors du « si l'adresse est neuve » : une
                # première passe avait posé trente-neuf adresses sans toucher
                # aux statuts, et la seconde ne les voyait plus puisque leur
                # adresse n'était plus neuve. Un appariement qui ne se répare
                # qu'au moment de la pose ne répare jamais le passé.
                if e.get("videoUrl") and e.get("statut") in ("a_produire", "bloque"):
                    e["statut"] = "monte"

                st = e.get("story")
                pose = (st or {}).get("url")
                # Même règle côté story : la reprise écrase, le dépôt ne sert
                # que de valeur par défaut quand rien n'est encore posé.
                url = repris.get("storyUrl") or pose or (
                    f"{BRUT}/stories/{i}.mp4" if i in stories else None
                )
                if url and url != pose:
                    # Neuf saisons 6 n'avaient pas de fiche story du tout : leur
                    # montage existait sur le disque et restait invisible faute
                    # d'un objet où poser l'adresse. Le hook et la punchline
                    # d'une story sont, par construction, ceux de l'épisode.
                    if st is None:
                        st = e["story"] = {
                            "format": "9:16 · 1080 × 1920 · 10 s",
                            "hook": e["accroche"].rstrip("."),
                            "punchline": e["punchline"].rstrip("."),
                            "url": None,
                        }
                    st["url"] = url
                    sts += 1

                # Le Short YouTube, même règle encore. Il n'existe que pour un
                # épisode qui a déjà une story, puisqu'il en est la suite.
                sh = e.get("shortYoutube")
                pose = (sh or {}).get("url")
                url = repris.get("shortUrl") or pose or (
                    f"{BRUT}/youtube/{i}.mp4" if i in shorts else None
                )
                if url and url != pose:
                    if sh is None:
                        sh = e["shortYoutube"] = {
                            "format": "9:16 · 1080 × 1920 · 12,5 s",
                            "url": None,
                        }
                    sh["url"] = url
                    yts += 1

                # La version paysage, pour la page de chaîne et la lecture sur
                # téléviseur — là où un Short vertical arrive entre deux bandes
                # noires. Elle n'a pas de vignette à elle : le site sert celle
                # de `vignetteEpisode(id, "youtube")`, qui est déjà le 16:9 de
                # l'épisode. Une adresse de plus dans la donnée serait une
                # deuxième vérité sur la même image.
                py = e.get("videoYoutube")
                pose = (py or {}).get("url")
                url = repris.get("videoYoutubeUrl") or pose or (
                    f"{BRUT}/youtube-paysage/{i}.mp4" if i in paysages else None
                )
                if url and url != pose:
                    if py is None:
                        py = e["videoYoutube"] = {
                            "format": "16:9 · 1920 × 1080 · 12,5 s",
                            "url": None,
                        }
                    py["url"] = url
                    pys += 1

                # La story Facebook : même image, même format que le Short,
                # mais un carton qui porte l'appel à l'action et l'adresse du
                # site plutôt que le nom d'une chaîne. Une vidéo native
                # Facebook est repartagée sans sa légende ; si l'adresse n'est
                # pas dans l'image, elle n'est nulle part.
                fb = e.get("storyFacebook")
                pose = (fb or {}).get("url")
                url = repris.get("storyFacebookUrl") or pose or (
                    f"{BRUT}/facebook/{i}.mp4" if i in facebooks else None
                )
                if url and url != pose:
                    if fb is None:
                        fb = e["storyFacebook"] = {
                            "format": "9:16 · 1080 × 1920 · 12,5 s",
                            "url": None,
                        }
                    fb["url"] = url
                    fbs += 1

                # La vidéo TikTok : même moule, carton au nom du compte.
                # Sur TikTok le nom d'utilisateur est cliquable depuis le
                # lecteur, comme la chaîne sur YouTube — inutile d'y écrire
                # l'adresse du site, qui n'est nécessaire que sur Facebook.
                tk = e.get("videoTiktok")
                pose = (tk or {}).get("url")
                url = repris.get("videoTiktokUrl") or pose or (
                    f"{BRUT}/tiktok-story/{i}.mp4" if i in tiktoks else None
                )
                if url and url != pose:
                    if tk is None:
                        tk = e["videoTiktok"] = {
                            "format": "9:16 · 1080 × 1920 · 12,5 s",
                            "url": None,
                        }
                    tk["url"] = url
                    tks += 1

    open(INVENTAIRE, "w", encoding="utf-8").write(json.dumps(d, ensure_ascii=False, indent=2))

    eps = [e for s in d["series"] for sa in s["saisons"] for e in sa["episodes"]]
    total_clips = sum(1 for e in eps if e["higgsfield"].get("videoSourceUrl"))
    total_st = sum(1 for e in eps if (e.get("story") or {}).get("url"))
    total_yt = sum(1 for e in eps if (e.get("shortYoutube") or {}).get("url"))
    total_py = sum(1 for e in eps if (e.get("videoYoutube") or {}).get("url"))
    total_fb = sum(1 for e in eps if (e.get("storyFacebook") or {}).get("url"))
    total_tk = sum(1 for e in eps if (e.get("videoTiktok") or {}).get("url"))
    print(f"{clips} clip(s), {mst} master(s), {sts} story(ies), {yts} Short(s), "
          f"{pys} paysage(s), {fbs} Facebook, {tks} TikTok et "
          f"{bas} bande(s)-annonce(s) reliés — {deja} clips l'étaient déjà")
    print(f"inventaire : {total_clips} clips, {total_st} stories, {total_yt} Shorts, "
          f"{total_py} paysages, {total_fb} Facebook, {total_tk} TikTok "
          f"sur {len(eps)} épisodes")

    orphelins = sorted(hooks - {e["id"] for e in eps})
    if orphelins:
        print(f"⚠️ fichiers sans épisode : {', '.join(orphelins)}")


if __name__ == "__main__":
    main()
