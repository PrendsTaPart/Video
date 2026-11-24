#!/usr/bin/env python3
"""Génère data/stories/*.json : les 10 stories Instagram de l'onglet « Stories Instagram »
du plan de campagne Excel, édition confirmée 31 décembre 2026 -> 2027.
Stories : sans voix off ni sous-titres (souvent vues sans le son), musique de fond seule.
Les stickers (compte à rebours, sondage, lien, partage) se posent dans l'app Instagram :
la zone 1080-1400 px est laissée libre quand un sticker est prévu (clé "sticker")."""
import json, os

P = "assets/photos/"
FMT = lambda d: {"width": 1080, "height": 1920, "fps": 30, "duration": d}
BASE = {"draftLabel": "VERSION DE TRAVAIL · musique à finaliser",
        "footer": "31.12.2026 · Réservations 01 84 60 20 46",
        "source": "Plan_Campagne_Reveillon_Villa_Beach_2026.xlsx — onglet Stories Instagram"}
S = {}

def story(key, title, dur, scenes, music, sticker=None):
    S[key] = {**BASE, "title": title, "format": FMT(dur), "scenes": scenes, "subtitles": [], "music": {"sections": music},
              **({"sticker": sticker} if sticker else {})}

story("story-01-teaser", "Story 1 — Teaser", 7, [
  {"id": "a", "start": 0, "end": 7, "media": P + "silhouette-lumieres-villabeach.jpg", "fx": "50% 50%", "grade": "night", "zoom": "in",
   "texts": [{"role": "mid", "text": "Une nuit exceptionnelle", "at": 0.6},
             {"role": "low", "text": "se prépare…", "at": 3.0}]}],
  [{"style": "intro", "start": 0, "end": 7}], "Compte à rebours (fin : 31/12/2026 19:00)")

story("story-02-annonce", "Story 2 — Annonce", 7, [
  {"id": "a", "start": 0, "end": 7, "media": P + "fete-villa.jpg", "fx": "40% 45%", "grade": "midnight", "zoom": "in",
   "texts": [{"role": "kicker", "text": "31.12.2026", "at": 0.2}, {"role": "title", "text": "Le plus grand réveillon du Nouvel An", "at": 0.4},
             {"role": "low", "text": "Domaine Villa Beach • Lisses", "at": 1.4}]}],
  [{"style": "intro", "start": 0, "end": 2}, {"style": "house", "start": 2, "end": 7}], "Lien de réservation (dès publication du site) ou appel")

sal = [("Généraliste", P + "dj-neon-villabeach.jpg", "30% 50%", "salle-gen", "house"),
       ("Latino / SBK", P + "salle-latino-couple-1.jpg", "45% 40%", "salle-latino", "latin"),
       ("80 / 90 / 2000", P + "fete-villa.jpg", "35% 45%", "salle-retro", "disco"),
       ("Caraïbéenne", P + "couple-danse.jpg", "55% 40%", "salle-carib", "carib")]
sc, mu = [], []
for i, (n, img, fx, gr, st) in enumerate(sal):
    a = round(i * 1.25, 2)
    sc.append({"id": f"s{i}", "start": a, "end": round(a + 1.25, 2), "media": img, "fx": fx, "grade": gr, "zoom": "in",
               "salle": {"num": f"Salle {i+1}", "name": n, "genres": ""}})
    mu.append({"style": st, "start": a, "end": round(a + 1.25, 2)})
sc.append({"id": "q", "start": 5, "end": 8, "media": P + "piste-mains-levees.jpg", "fx": "55% 50%", "grade": "club",
           "texts": [{"role": "brand", "text": "4 salles • 4 ambiances", "at": 5.1}, {"role": "tagline", "text": "Quelle sera la vôtre ?", "at": 5.4}]})
mu.append({"style": "house", "start": 5, "end": 8})
story("story-03-quatre-salles", "Story 3 — 4 salles", 8, sc, mu, "Sondage : Généraliste / Latino / 80-2000 / Caraïbes")

story("story-04-diner", "Story 4 — Dîner", 8, [
  {"id": "a", "start": 0, "end": 2.5, "media": P + "table-dressee-rose-bougies.jpg", "fx": "50% 50%", "grade": "warm", "zoom": "in",
   "texts": [{"role": "title", "text": "Un dîner d'exception", "at": 0.2}]},
  {"id": "b", "start": 2.5, "end": 8, "media": P + "tartare-crevettes-mangue.jpg", "fx": "50% 50%", "grade": "dark", "zoom": "in",
   "cards": [{"big": "120 € / pers.", "small": "Dîner de fête", "at": 2.7},
             {"big": "180 € / pers.", "small": "Dîner Champagne", "at": 3.7},
             {"big": "Dès 19 h", "small": "Ouverture du restaurant", "at": 4.7}]}],
  [{"style": "intro", "start": 0, "end": 2.5}, {"style": "lounge", "start": 2.5, "end": 8}], "Réserver le dîner (lien ou appel)")

story("story-05-vip", "Story 5 — VIP", 7, [
  {"id": "a", "start": 0, "end": 7, "media": P + "amies-tenues-chic-bouteille.jpg", "fx": "45% 45%", "grade": "club", "zoom": "in",
   "texts": [{"role": "title", "text": "Votre table vous attend", "at": 0.2, "end": 1.6},
             {"role": "price", "label": "Packs VIP à partir de", "text": "200 €", "at": 1.7},
             {"role": "menu", "text": "Table · bouteille · entrées incluses", "at": 2.2}]}],
  [{"style": "build", "start": 0, "end": 2}, {"style": "drop", "start": 2, "end": 7}], "Appel / réservation")

beats = [round(0.6 + i * 0.45, 2) for i in range(10)]
story("story-06-compte-a-rebours", "Story 6 — Compte à rebours", 8, [
  {"id": "cd", "start": 0, "end": 5.1, "type": "countdown", "beats": beats, "labels": [str(10 - i) for i in range(10)], "kicker": "31.12.2026"},
  {"id": "ny", "start": 5.1, "end": 8, "media": P + "fete-villa.jpg", "fx": "70% 40%", "grade": "midnight", "celebrate": True,
   "texts": [{"role": "big", "text": "2027 !", "at": 5.2}]}],
  [{"style": "build", "start": 0, "end": 0.6}, {"style": "countdown", "beats": beats}, {"style": "drop", "start": 5.1, "end": 8}],
  "Partager / taguer ses amis")

story("story-07-clubbing", "Story 7 — Clubbing tarifs", 7, [
  {"id": "a", "start": 0, "end": 7, "media": P + "piste-mains-levees.jpg", "fx": "55% 50%", "grade": "blur",
   "texts": [{"role": "kicker", "text": "Clubbing · par personne", "at": 0.1}],
   "rows": [{"label": "Entrée simple", "price": "20 €", "at": 0.4}, {"label": "Entrée + 1 conso", "price": "30 €", "at": 0.9},
            {"label": "Entrée + 3 consos", "price": "40 €", "at": 1.4}, {"label": "Entrée + 10 consos", "price": "100 €", "at": 1.9}]}],
  [{"style": "house", "start": 0, "end": 7}], "Réserver")

story("story-08-anniversaire", "Story 8 — Anniversaire", 7, [
  {"id": "a", "start": 0, "end": 7, "media": P + "groupe-neon-villabeach.jpg", "fx": "50% 45%", "grade": "dark", "zoom": "in", "celebrate": True,
   "texts": [{"role": "title", "text": "Né en décembre ?", "at": 0.3, "end": 1.8},
             {"role": "price", "label": "Offre anniversaire", "text": "1 bouteille offerte", "at": 1.9},
             {"role": "menu", "text": "pour 5 entrées · pièce d'identité requise", "at": 2.3}]}],
  [{"style": "drop", "start": 0, "end": 7}], "Partager à un ami né en décembre")

story("story-09-dress-code", "Story 9 — Dress code", 7, [
  {"id": "a", "start": 0, "end": 3.5, "media": P + "couple-danse-bleu.jpg", "fx": "50% 45%", "grade": "dark", "zoom": "in",
   "texts": [{"role": "kicker", "text": "Dress code", "at": 0.2}, {"role": "title", "text": "Chic & élégant", "at": 0.4}]},
  {"id": "b", "start": 3.5, "end": 7, "media": P + "amies-tenues-chic-bouteille.jpg", "fx": "40% 40%", "grade": "dark", "zoom": "in",
   "texts": [{"role": "kicker", "text": "Dress code", "at": 3.5}, {"role": "title", "text": "Sortez vos plus belles tenues", "at": 3.6}]}],
  [{"style": "lounge", "start": 0, "end": 7}], "Question : « Ta tenue du 31 ? »")

story("story-10-dernier-cta", "Story 10 — Dernier CTA", 7, [
  {"id": "fin", "start": 0, "end": 7, "type": "endcard", "date": "31 décembre 2026", "title": "Réservez votre soirée",
   "sub": "Préventes conseillées • Accès prioritaire", "venue": "Domaine Villa Beach", "address": "23 rue des Pyrénées, 91090 Lisses",
   "phone": "01 84 60 20 46", "url": None, "qr": None}],
  [{"style": "outro", "start": 0, "end": 7}], "Téléphone / lien de prévente")

os.makedirs("data/stories", exist_ok=True)
for k, v in S.items():
    json.dump(v, open(f"data/stories/{k}.json", "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print(k, v["format"]["duration"], "s")
