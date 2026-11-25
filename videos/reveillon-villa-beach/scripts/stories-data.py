#!/usr/bin/env python3
"""Génère data/stories/*.json : les 10 stories Instagram (onglet « Stories Instagram » du plan
de campagne Excel), édition 31 décembre 2026 -> 2027. Version finale : pied de page avec la date
en grand, menu présenté comme exclusif au 31 décembre, vraies vidéos du domaine, formats
originaux. Zones Instagram : 0-250 px (profil) et 1580-1920 px (réponse) laissées libres ;
la zone ≈1080-1400 px reste libre quand un sticker est prévu (clé "sticker")."""
import json, os

P = "assets/photos/"
V = "assets/video/"
FMT = lambda d: {"width": 1080, "height": 1920, "fps": 30, "duration": d}
BASE = {"footer": "Jeudi 31 décembre 2026|Réservations 01 84 60 20 46",
        "source": "Plan_Campagne_Reveillon_Villa_Beach_2026.xlsx — onglet Stories Instagram"}
S = {}

def story(key, title, dur, scenes, music, sticker=None):
    S[key] = {**BASE, "title": title, "format": FMT(dur), "scenes": scenes, "music": {"sections": music},
              **({"sticker": sticker} if sticker else {})}

story("story-01-teaser", "Story 1 — Teaser", 7, [
  {"id": "a", "start": 0, "end": 7, "type": "video", "media": V + "terrasse-approche.mp4", "grade": "night-video",
   "texts": [{"role": "mid", "text": "Une nuit exceptionnelle", "at": 0.5, "top": 420}, {"role": "low", "text": "se prépare…", "at": 2.4, "top": 760}]}],
  [{"style": "intro", "start": 0, "end": 7}], "Compte à rebours (fin : 31/12/2026 19:00)")

story("story-02-annonce", "Story 2 — Annonce (invitation)", 7, [
  {"id": "inv", "start": 0, "end": 7, "type": "invite", "bg": {"type": "video", "media": V + "jardin-pergola-9x16.mp4", "grade": "endvideo"},
   "invite": {"kicker": "Le plus grand réveillon", "title": "du Nouvel An", "date": "31 · 12 · 2026", "venue": "Domaine Villa Beach · Lisses", "at": 0.3}}],
  [{"style": "intro", "start": 0, "end": 2}, {"style": "house", "start": 2, "end": 7}], "Appel (puis lien dès publication du site)")

story("story-03-quatre-salles", "Story 3 — 4 salles (sondage)", 8, [
  {"id": "g", "start": 0, "end": 8, "type": "grid4", "gridStyle": "top:400px;height:660px;", "grid": [
     {"media": P + "dj-neon-villabeach.jpg", "fx": "30% 50%", "grade": "salle-gen", "label": "Généraliste", "at": 0.2},
     {"media": P + "salle-latino-couple-1.jpg", "fx": "45% 40%", "grade": "salle-latino", "label": "Latino / SBK", "at": 0.6},
     {"media": P + "fete-villa.jpg", "fx": "35% 45%", "grade": "salle-retro", "label": "80/90/2000", "at": 1.0},
     {"media": P + "couple-danse.jpg", "fx": "55% 40%", "grade": "salle-carib", "label": "Caraïbéenne", "at": 1.4}],
   "texts": [{"role": "brand", "text": "Quelle sera la vôtre ?", "at": 1.9, "top": 280}]}],
  [{"style": "house", "start": 0, "end": 2}, {"style": "latin", "start": 2, "end": 4}, {"style": "disco", "start": 4, "end": 6}, {"style": "carib", "start": 6, "end": 8}],
  "Sondage : Généraliste / Latino / 80-2000 / Caraïbes")

story("story-04-diner", "Story 4 — Dîner (menu exclusif)", 9, [
  {"id": "a", "start": 0, "end": 2.4, "media": P + "tartare-crevettes-mangue.jpg", "fx": "50% 50%", "grade": "warm",
   "texts": [{"role": "title", "text": "Le menu du 31 décembre", "at": 0.15}, {"role": "stamp", "text": "Exclusif · un seul soir", "at": 1.1, "top": 1000}]},
  {"id": "m", "start": 2.4, "end": 9, "type": "menucard", "trans": "rise",
   "bg": {"media": P + "table-dressee-rose-bougies.jpg", "fx": "40% 50%", "grade": "softblur"},
   "menu": {"kicker": "Menu exclusif · 31.12.2026", "title": "120 € · 180 € Champagne", "stamp": "Uniquement\nle 31.12", "stampAt": 2.6, "courses": [
     {"k": "Entrée", "v": "Foie gras maison · ou tartare exotique"},
     {"k": "Plat", "v": "Pavé de veau · ou Saint-Jacques, risotto aux cèpes"},
     {"k": "Dessert", "v": "Bûches du Nouvel An"},
     {"k": "Dès 19 h", "v": "puis les 4 salles jusqu'à 05 h"}]}}],
  [{"style": "intro", "start": 0, "end": 2.4}, {"style": "lounge", "start": 2.4, "end": 9}], "Réserver le dîner (appel / lien)")

story("story-05-vip", "Story 5 — VIP", 7, [
  {"id": "a", "start": 0, "end": 2.2, "type": "video", "media": V + "jardin-pergola-9x16.mp4", "grade": "dusk",
   "texts": [{"role": "title", "text": "Votre table vous attend", "at": 0.15}]},
  {"id": "b", "start": 2.2, "end": 7, "media": P + "amies-tenues-chic-bouteille.jpg", "fx": "45% 45%", "grade": "club", "trans": "flash",
   "texts": [{"role": "price", "label": "Packs VIP à partir de", "text": "200 €", "at": 2.3}, {"role": "menu", "text": "Table · bouteille · entrées incluses", "at": 2.7}]}],
  [{"style": "build", "start": 0, "end": 2.2}, {"style": "drop", "start": 2.2, "end": 7}], "Appel / réservation")

beats = [round(2.6 + i * 0.32, 2) for i in range(10)]
story("story-06-compte-a-rebours", "Story 6 — Compte à rebours", 9, [
  {"id": "ck", "start": 0, "end": 2.6, "type": "clock", "digital": "23:59"},
  {"id": "cd", "start": 2.6, "end": 5.8, "type": "countdown", "beats": beats, "labels": [str(10 - i) for i in range(10)], "kicker": "Minuit", "trans": "flash"},
  {"id": "ny", "start": 5.8, "end": 9, "media": P + "fete-villa.jpg", "fx": "70% 40%", "grade": "midnight", "celebrate": True, "trans": "flash",
   "texts": [{"role": "burst", "text": "Happy New Year", "at": 5.9}, {"role": "big", "text": "2027 !", "at": 6.2, "top": 700}]}],
  [{"style": "intro", "start": 0, "end": 2.6}, {"style": "countdown", "beats": beats}, {"style": "drop", "start": 5.8, "end": 9}],
  "Partager / taguer ses amis")

story("story-07-clubbing", "Story 7 — Clubbing tarifs", 7, [
  {"id": "a", "start": 0, "end": 7, "media": P + "piste-mains-levees.jpg", "fx": "55% 50%", "grade": "blur",
   "texts": [{"role": "kicker", "text": "Clubbing · par personne", "at": 0.1, "top": 290}],
   "rows": [{"label": "Entrée simple", "price": "20 €", "at": 0.4}, {"label": "Entrée + 1 conso", "price": "30 €", "at": 0.8},
            {"label": "Entrée + 3 consos", "price": "40 €", "at": 1.2}, {"label": "Entrée + 10 consos", "price": "100 €", "at": 1.6}]}],
  [{"style": "house", "start": 0, "end": 7}], "Réserver")

story("story-08-anniversaire", "Story 8 — Anniversaire", 7, [
  {"id": "a", "start": 0, "end": 7, "media": P + "groupe-neon-villabeach.jpg", "fx": "50% 45%", "grade": "dark", "celebrate": True,
   "texts": [{"role": "title", "text": "Né en décembre ?", "at": 0.3, "end": 1.8, "out": True},
             {"role": "price", "label": "Offre anniversaire", "text": "1 bouteille offerte", "at": 1.9},
             {"role": "menu", "text": "pour 5 entrées · pièce d'identité requise", "at": 2.3}]}],
  [{"style": "drop", "start": 0, "end": 7}], "Partager à un ami né en décembre")

story("story-09-dress-code", "Story 9 — Dress code", 7, [
  {"id": "a", "start": 0, "end": 3.5, "media": P + "couple-danse-bleu.jpg", "fx": "50% 45%", "grade": "dark",
   "texts": [{"role": "kicker", "text": "Dress code", "at": 0.2}, {"role": "title", "text": "Chic & élégant", "at": 0.4}]},
  {"id": "b", "start": 3.5, "end": 7, "media": P + "amies-tenues-chic-bouteille.jpg", "fx": "40% 40%", "grade": "dark", "trans": "whip",
   "texts": [{"role": "kicker", "text": "Pour le 31 décembre", "at": 3.55}, {"role": "title", "text": "Sortez vos plus belles tenues", "at": 3.65}]}],
  [{"style": "lounge", "start": 0, "end": 7}], "Question : « Ta tenue du 31 ? »")

story("story-10-dernier-cta", "Story 10 — Dernier CTA", 7, [
  {"id": "fin", "start": 0, "end": 7, "type": "endcard", "date": "Jeudi 31 décembre 2026", "title": "Réservez votre soirée",
   "note": "Dernières places · préventes conseillées", "sub": "Accès prioritaire", "venue": "Domaine Villa Beach",
   "address": "23 rue des Pyrénées, 91090 Lisses", "phone": "01 84 60 20 46", "url": None, "qr": None,
   "bgVideo": V + "terrasse-pergola.mp4", "trans": "none"}],
  [{"style": "outro", "start": 0, "end": 7}], "Appel / lien de prévente")

os.makedirs("data/stories", exist_ok=True)
for k, v in S.items():
    json.dump(v, open(f"data/stories/{k}.json", "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print(k, v["format"]["duration"], "s")
