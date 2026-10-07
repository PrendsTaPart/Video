#!/usr/bin/env python3
"""Étape 6 — proposition de calendrier sur 4 semaines (bd-video/calendrier.csv), sans rien programmer.

Un épisode tous les 2 ou 3 jours, stories entre les épisodes, LinkedIn le mardi et le jeudi matin.
Les légendes reprennent les phrases de la BD (aucun chiffre ni promesse ajoutés).
"""
import csv
import datetime as dt
import os
import subprocess

ROOT = os.path.join(subprocess.check_output(["git", "rev-parse", "--show-toplevel"], text=True).strip(), "bd-video")
START = dt.date(2026, 10, 12)  # lundi
MENTION = "Inspiré de l'histoire de Mickael, chef et fondateur."
TAGS = "#restauration #restaurant #chef #FoodEatUp"
TAGS_LI = "#restauration #franchise #IA #FoodEatUp"

EP = {  # numéro → (titre court, accroche tirée de la BD)
    1: ("Une journée sans FoodEatUp", "Pourquoi tenir un restaurant est-il si épuisant ?"),
    2: ("La même journée, avec FoodEatUp", "Ce soir, je dîne avec ma famille."),
    3: ("La brigade passe à l'écran", "Une seule saisie, et tout le restaurant communique."),
    4: ("Expansion & franchise", "Ce soir-là, la brigade augmentée est devenue une famille."),
    5: ("Le laboratoire et les agents", "L'IA propose, l'humain décide."),
    6: ("Une infinité de solutions", "Les solutions sont infinies."),
}
LI_ANGLE = {1: "Le vrai coût d'une journée sans outil.", 2: "Une seule saisie, pas dix.",
            3: "La vitrine du restaurant, pilotée depuis la carte.", 4: "Grandir sans perdre son goût.",
            5: "Prévoir au lieu de subir.", 6: "Votre restaurant est unique. Votre FoodEatUp aussi."}


def cap_episode(n):
    t, h = EP[n]
    return (f"« {h} » La Brigade augmentée, épisode {n}/6 : {t}. Une BD FoodEatUp devenue série. "
            f"Testez FoodEatUp, lien en bio. {MENTION} {TAGS} #BD")


def cap_story(n, kind):
    t, h = EP[n]
    lead = {"teaser": f"Ce soir : épisode {n}, {t}.", "personnage": "Le personnage du jour de la Brigade augmentée.",
            "citation": "La citation du jour, par Mickael."}[kind]
    return f"{lead} Voir l'épisode : lien en bio. {MENTION} #FoodEatUp #restauration #BD"


def cap_linkedin(n):
    t, h = EP[n]
    return (f"{LI_ANGLE[n]} « {h} » Épisode {n} de La Brigade augmentée, la BD FoodEatUp sur le quotidien d'un "
            f"restaurateur, adaptée en vidéo (sous-titrée, lisible sans le son). Pour tester FoodEatUp : lien en commentaire. "
            f"{MENTION} {TAGS_LI}")


def cap_film():
    return ("Le film complet : « D'une cuisine épuisée à une famille de restaurants. » Les 88 pages de La Brigade "
            f"augmentée en une seule vidéo. Testez FoodEatUp, lien en bio. {MENTION} {TAGS} #BD")


def main():
    rows = []
    add = lambda day, hour, net, fmt, f, cap: rows.append(
        [(START + dt.timedelta(days=day)).isoformat(), hour, net, fmt, f, cap, "brouillon — à valider"])
    ep_days = {1: 0, 2: 3, 3: 6, 4: 9, 5: 12, 6: 15}  # lun, jeu, dim, mer, sam, mar
    for n, d in ep_days.items():
        # Teaser la veille (story), épisode le jour J, deux stories le lendemain.
        if d:
            add(d - 1, "12:00", "TikTok", "Story 15 s", f"renders/tiktok/story-ep{n:02d}.mp4", cap_story(n, "teaser"))
            for net in ("Instagram", "Facebook"):
                add(d - 1, "12:00", net, "Story 15 s", f"renders/{net.lower()}/story-ep{n:02d}-1-teaser.mp4", cap_story(n, "teaser"))
        add(d, "18:30", "TikTok", "Épisode 9:16", f"renders/episodes/ep{n:02d}.mp4", cap_episode(n))
        for net in ("Instagram", "Facebook"):
            add(d, "18:30", net, "Reel 60–90 s", f"renders/{net.lower()}/reel-ep{n:02d}.mp4", cap_episode(n))
        for net in ("Instagram", "Facebook"):
            add(d + 1, "12:00", net, "Story 15 s", f"renders/{net.lower()}/story-ep{n:02d}-2-personnage.mp4", cap_story(n, "personnage"))
            add(d + 2 if n < 6 else d + 1, "19:00" if n < 6 else "19:30", net, "Story 15 s",
                f"renders/{net.lower()}/story-ep{n:02d}-3-citation.mp4", cap_story(n, "citation"))
    # LinkedIn : mardi et jeudi 8 h 30, un épisode à chaque fois (4:5 dans le fil).
    li_days = [1, 3, 8, 10, 15, 17]
    for n, d in zip(range(1, 7), li_days):
        add(d, "08:30", "LinkedIn", "4:5 · 60–120 s", f"renders/linkedin/linkedin-ep{n:02d}-4x5.mp4", cap_linkedin(n))
    # Semaine 4 : le film complet, puis deux rappels LinkedIn.
    add(17, "12:00", "TikTok", "Story 15 s", "renders/tiktok/story-ep01.mp4",
        f"Demain : les 88 pages de La Brigade augmentée en un seul film. {MENTION} #FoodEatUp #restauration #BD")
    for day, n in ((20, 2), (23, 4), (26, 5)):  # rappels en stories, semaine 4
        for net in ("Instagram", "Facebook"):
            add(day, "12:00", net, "Story 15 s", f"renders/{net.lower()}/story-ep{n:02d}-2-personnage.mp4", cap_story(n, "personnage"))
    add(18, "18:30", "TikTok", "Film complet 9:16", "renders/film/film.mp4", cap_film())
    add(22, "08:30", "LinkedIn", "9:16 · 60–120 s", "renders/linkedin/linkedin-ep02-9x16.mp4", cap_linkedin(2))
    add(24, "08:30", "LinkedIn", "9:16 · 60–120 s", "renders/linkedin/linkedin-ep04-9x16.mp4", cap_linkedin(4))
    rows.sort(key=lambda r: (r[0], r[1], r[2]))
    with open(os.path.join(ROOT, "calendrier.csv"), "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["date", "heure", "reseau", "format", "fichier", "legende", "statut"])
        w.writerows(rows)
    print(f"{len(rows)} publications du {rows[0][0]} au {rows[-1][0]}")


if __name__ == "__main__":
    main()
