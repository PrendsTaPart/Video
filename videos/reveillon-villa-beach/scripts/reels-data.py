#!/usr/bin/env python3
"""Génère data/reels/*.json : les 5 Reels/TikTok de l'onglet « TikTok Reels » du plan
de campagne Excel (Plan_Campagne_Reveillon_Villa_Beach_2026.xlsx), adaptés à l'édition
confirmée 31 décembre 2026 -> 2027. Modifier ce fichier puis relancer `npm run reels:data`."""
import json, os

P = "assets/photos/"
END = lambda a, b, title="Réservez votre réveillon": {
    "id": "fin", "start": a, "end": b, "type": "endcard", "date": "31 décembre 2026",
    "title": title, "sub": "Préventes conseillées • Accès prioritaire",
    "venue": "Domaine Villa Beach", "address": "23 rue des Pyrénées, 91090 Lisses",
    "phone": "01 84 60 20 46", "url": None, "qr": None}
FMT = lambda d: {"width": 1080, "height": 1920, "fps": 30, "duration": d}
COMMON = {"draftLabel": "VERSION DE TRAVAIL · voix off et musique à finaliser",
          "source": "Plan_Campagne_Reveillon_Villa_Beach_2026.xlsx — onglet TikTok Reels"}

reels = {}

# 1 — Grand lancement (20–25 s)
reels["reel-01-lancement"] = {**COMMON, "title": "Reel 1 — Grand lancement", "format": FMT(25.6),
 "scenes": [
  {"id": "a1", "start": 0, "end": 1.6, "media": P + "silhouette-lumieres-villabeach.jpg", "fx": "50% 50%", "grade": "night", "zoom": "in",
   "texts": [{"role": "big", "text": "2027", "at": 0.15}]},
  {"id": "a2", "start": 1.6, "end": 3.2, "media": P + "piste-mains-levees.jpg", "fx": "65% 40%", "grade": "club", "zoom": "in",
   "texts": [{"role": "mid", "text": "approche…", "at": 1.7}]},
  {"id": "b", "start": 3.2, "end": 6.2, "type": "video", "media": "assets/video/terrasse-9x16.mp4", "grade": "dusk",
   "texts": [{"role": "kicker", "text": "31 décembre 2026", "at": 3.3}, {"role": "brand", "text": "Domaine Villa Beach", "at": 3.5}]},
  {"id": "c1", "start": 6.2, "end": 7.2, "media": P + "dj-neon-villabeach.jpg", "fx": "30% 50%", "grade": "salle-gen", "zoom": "in",
   "texts": [{"role": "mid", "text": "4 salles", "at": 6.25, "end": 10.2}]},
  {"id": "c2", "start": 7.2, "end": 8.2, "media": P + "salle-latino-renverse.jpg", "fx": "45% 50%", "grade": "salle-latino", "zoom": "in"},
  {"id": "c3", "start": 8.2, "end": 9.2, "media": P + "fete-villa.jpg", "fx": "35% 45%", "grade": "salle-retro", "zoom": "in"},
  {"id": "c4", "start": 9.2, "end": 10.2, "media": P + "couple-danse.jpg", "fx": "55% 40%", "grade": "salle-carib", "zoom": "in",
   "texts": [{"role": "low", "text": "4 ambiances", "at": 8.2, "end": 10.2}]},
  {"id": "d1", "start": 10.2, "end": 12.6, "media": P + "dj-platines-nb.jpg", "fx": "40% 50%", "grade": "salle-gen", "zoom": "in",
   "texts": [{"role": "mid", "text": "Une nuit inoubliable", "at": 10.4}]},
  {"id": "d2", "start": 12.6, "end": 15.0, "media": P + "ambiance-villa-hd.jpg", "fx": "35% 40%", "grade": "club", "zoom": "in"},
  {"id": "e", "start": 15.0, "end": 17.4, "type": "countdown", "beats": [15.1, 15.85, 16.6], "labels": ["3", "2", "1"], "kicker": "Jusqu'à 05 h"},
  {"id": "f", "start": 17.4, "end": 19.6, "media": P + "fete-villa.jpg", "fx": "70% 40%", "grade": "midnight", "celebrate": True,
   "texts": [{"role": "headline", "text": "Jusqu'à 05 h", "at": 17.6}]},
  END(19.6, 25.6, "Réservez maintenant")],
 "subtitles": [
  {"start": 0.3, "end": 3.1, "text": "Le 31 décembre, préparez-vous"},
  {"start": 3.3, "end": 6.1, "text": "à vivre une nuit exceptionnelle"},
  {"start": 6.3, "end": 8.6, "text": "Le Domaine Villa Beach vous donne rendez-vous"},
  {"start": 8.6, "end": 10.1, "text": "pour célébrer 2027"},
  {"start": 10.4, "end": 12.4, "text": "quatre salles, DJs, animations"},
  {"start": 12.6, "end": 14.9, "text": "et fête jusqu'à cinq heures"},
  {"start": 19.8, "end": 22.0, "text": "Réservez dès maintenant"}],
 "voiceover": {"lines": [{"start": 0.3, "text": "Le 31 décembre, préparez-vous à vivre une nuit exceptionnelle. Le Domaine Villa Beach vous donne rendez-vous pour célébrer 2027 : quatre salles, DJs, animations et fête jusqu'à cinq heures."},
                         {"start": 19.8, "text": "Réservez dès maintenant."}]},
 "music": {"sections": [{"style": "intro", "start": 0, "end": 3.2}, {"style": "houselight", "start": 3.2, "end": 6.2},
   {"style": "house", "start": 6.2, "end": 15.0}, {"style": "countdown", "beats": [15.1, 15.85, 16.6]},
   {"style": "drop", "start": 17.4, "end": 19.6}, {"style": "outro", "start": 19.6, "end": 25.6}]}}

# 2 — 4 univers (15–20 s)
SAL = [("Salle 1", "Team Généraliste ?", "Hits · Pop · R&B · House", P + "dj-neon-villabeach.jpg", "30% 50%", "salle-gen", "house"),
       ("Salle 2", "Team Latino ?", "Salsa · Bachata · Kizomba", P + "salle-latino-couple-1.jpg", "45% 40%", "salle-latino", "latin"),
       ("Salle 3", "Team 80-90-2000 ?", "Disco · Funk · Classics", P + "fete-villa.jpg", "35% 45%", "salle-retro", "disco"),
       ("Salle 4", "Team Caraïbéenne ?", "Zouk · Dancehall · Shatta", P + "couple-danse.jpg", "55% 40%", "salle-carib", "carib")]
sc = []; mu = []
for i, (n, name, g, img, fx, gr, st) in enumerate(SAL):
    a = i * 3.0
    sc.append({"id": f"s{i+1}", "start": a, "end": a + 3.0, "media": img, "fx": fx, "grade": gr, "zoom": "in",
               "salle": {"num": n, "name": name, "genres": g}})
    mu.append({"style": st, "start": a, "end": a + 3.0})
sc.append({"id": "t", "start": 12.0, "end": 14.0, "media": P + "piste-mains-levees.jpg", "fx": "55% 50%", "grade": "club", "celebrate": True,
           "texts": [{"role": "mid", "text": "4 salles, 4 ambiances !", "at": 12.1}]})
sc.append(END(14.0, 20.0, "Quelle sera votre salle ?"))
mu += [{"style": "drop", "start": 12.0, "end": 14.0}, {"style": "outro", "start": 14.0, "end": 20.0}]
reels["reel-02-quatre-univers"] = {**COMMON, "title": "Reel 2 — 4 univers", "format": FMT(20), "scenes": sc, "subtitles": [],
  "voiceover": {"optional": True, "lines": [{"start": 12.1, "text": "Quelle salle sera votre QG ?"}]}, "music": {"sections": mu}}

# 3 — Dîner de fête (20 s + carton)
reels["reel-03-diner"] = {**COMMON, "title": "Reel 3 — Dîner de fête", "format": FMT(22), "scenes": [
  {"id": "a", "start": 0, "end": 3, "media": P + "table-dressee-rose-bougies.jpg", "fx": "50% 50%", "grade": "warm", "zoom": "in",
   "texts": [{"role": "kicker", "text": "Réveillon 31.12.2026", "at": 0.1}, {"role": "title", "text": "Un dîner d'exception", "at": 0.3}]},
  {"id": "b", "start": 3, "end": 6, "media": P + "tartare-crevettes-mangue.jpg", "fx": "50% 50%", "grade": "warm", "zoom": "in",
   "texts": [{"role": "chip", "text": "Foie gras ou tartare", "at": 3.1}]},
  {"id": "c", "start": 6, "end": 10, "media": P + "serveur-cocktails-plateau.jpg", "fx": "50% 50%", "grade": "softblur",
   "texts": [{"role": "mid", "text": "Veau ou Saint‑Jacques", "at": 6.1}, {"role": "low", "text": "plats au choix", "at": 6.4}]},
  {"id": "d", "start": 10, "end": 13, "media": P + "table-dressee-rose-bougies.jpg", "fx": "20% 50%", "grade": "softblur",
   "texts": [{"role": "mid", "text": "Bûches du Nouvel An", "at": 10.1}, {"role": "low", "text": "dessert", "at": 10.4}]},
  {"id": "e", "start": 13, "end": 16, "media": P + "tartare-crevettes-mangue.jpg", "fx": "80% 50%", "grade": "blur",
   "cards": [{"big": "120 € / pers.", "small": "Dîner de fête · vin inclus", "at": 13.1},
             {"big": "180 € / pers.", "small": "Dîner Champagne", "at": 13.8},
             {"big": "Dès 19 h", "small": "puis les 4 salles jusqu'à 05 h", "at": 14.5}]},
  END(16, 22, "Réservez votre dîner")],
 "subtitles": [
  {"start": 0.3, "end": 2.9, "text": "Pour commencer la nouvelle année avec élégance"},
  {"start": 3.1, "end": 5.4, "text": "découvrez notre dîner de fête"},
  {"start": 6.1, "end": 8.2, "text": "Un menu raffiné, deux formules"},
  {"start": 8.2, "end": 11.4, "text": "et l'accès aux quatre salles"},
  {"start": 11.4, "end": 12.9, "text": "pour poursuivre la soirée"}],
 "voiceover": {"lines": [{"start": 0.3, "text": "Pour commencer la nouvelle année avec élégance, découvrez notre dîner de fête. Un menu raffiné, deux formules et l'accès aux quatre salles pour poursuivre la soirée."}]},
 "music": {"sections": [{"style": "intro", "start": 0, "end": 3}, {"style": "lounge", "start": 3, "end": 16}, {"style": "outro", "start": 16, "end": 22}]}}

# 4 — Expérience VIP (15 s + carton)
PK = [("Pack Classique", "200 €", "4 entrées · table · 1 bouteille", P + "amies-tenues-chic-bouteille.jpg", "45% 60%"),
      ("Pack Premium", "280 €", "4 entrées · table · bouteille premium", P + "bar-flamme-cocktail.jpg", "50% 45%"),
      ("Pack Magnum", "500 €", "8 entrées · table · magnum premium", P + "serveur-cocktails-plateau.jpg", "55% 55%"),
      ("Pack Ultra VIP", "1 200 €", "16 entrées · place Ultra VIP · réhoboam 4,5 L", P + "groupe-neon-villabeach.jpg", "50% 45%")]
sc = [{"id": "a", "start": 0, "end": 3, "media": P + "amies-tenues-chic-bouteille.jpg", "fx": "50% 35%", "grade": "club", "zoom": "in",
       "texts": [{"role": "kicker", "text": "Réveillon 31.12.2026", "at": 0.1}, {"role": "brand", "text": "Votre réveillon", "at": 0.25},
                 {"role": "tagline", "text": "en mode VIP", "at": 0.5}]}]
for i, (n, pr, inc, img, fx) in enumerate(PK):
    a = 3 + i * 2.5
    sc.append({"id": f"p{i+1}", "start": a, "end": a + 2.5, "media": img, "fx": fx, "grade": "dark", "zoom": "in",
               "texts": [{"role": "price", "label": n, "text": pr, "at": a + 0.08}, {"role": "menu", "text": inc, "at": a + 0.35}]})
sc.append(END(13, 19, "Réservez votre table"))
reels["reel-04-vip"] = {**COMMON, "title": "Reel 4 — Expérience VIP", "format": FMT(19), "scenes": sc,
 "subtitles": [{"start": 0.3, "end": 2.9, "text": "Tables, bouteilles et espaces VIP"},
               {"start": 3.1, "end": 5.4, "text": "Choisissez votre pack"},
               {"start": 5.6, "end": 8.0, "text": "et vivez le réveillon en grand"}],
 "voiceover": {"lines": [{"start": 0.3, "text": "Tables, bouteilles et espaces VIP. Choisissez votre pack et vivez le réveillon en grand."}]},
 "music": {"sections": [{"style": "build", "start": 0, "end": 3}, {"style": "drop", "start": 3, "end": 13}, {"style": "outro", "start": 13, "end": 19}]}}

# 5 — Countdown minuit (15 s + carton)
cd_beats = [round(8.0 + i * 0.3, 2) for i in range(10)]
reels["reel-05-countdown"] = {**COMMON, "title": "Reel 5 — Countdown minuit", "format": FMT(21), "scenes": [
  {"id": "h", "start": 0, "end": 4, "media": P + "silhouette-lumieres-villabeach.jpg", "fx": "50% 50%", "grade": "night", "zoom": "in",
   "texts": [{"role": "kicker", "text": "31 décembre 2026", "at": 0.1}, {"role": "big", "text": "23:59", "at": 0.3}]},
  {"id": "dj", "start": 4, "end": 6, "media": P + "dj-neon-villabeach.jpg", "fx": "30% 50%", "grade": "club", "zoom": "in",
   "texts": [{"role": "big", "text": "Prêts ?", "at": 4.1}]},
  {"id": "dj2", "start": 6, "end": 8, "media": P + "piste-mains-levees.jpg", "fx": "60% 45%", "grade": "club", "zoom": "in"},
  {"id": "cd", "start": 8, "end": 11, "type": "countdown", "beats": cd_beats, "labels": [str(10 - i) for i in range(10)], "kicker": "Minuit"},
  {"id": "ny", "start": 11, "end": 15, "media": P + "fete-villa.jpg", "fx": "70% 40%", "grade": "midnight", "celebrate": True,
   "texts": [{"role": "burst", "text": "Happy New Year", "at": 11.1, "end": 15}, {"role": "big", "text": "2027 !", "at": 11.4}]},
  END(15, 21, "Fêtez 2027 avec nous")],
 "subtitles": [],
 "voiceover": {"lines": []},
 "music": {"sections": [{"style": "intro", "start": 0, "end": 4}, {"style": "build", "start": 4, "end": 8},
   {"style": "countdown", "beats": cd_beats}, {"style": "drop", "start": 11, "end": 15}, {"style": "outro", "start": 15, "end": 21}]}}

os.makedirs("data/reels", exist_ok=True)
for k, v in reels.items():
    json.dump(v, open(f"data/reels/{k}.json", "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print(k, v["format"]["duration"], "s")
