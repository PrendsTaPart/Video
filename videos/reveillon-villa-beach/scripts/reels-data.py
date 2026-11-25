#!/usr/bin/env python3
"""Génère data/reels/*.json : les 5 Reels/TikTok de l'onglet « TikTok Reels » du plan de
campagne Excel, édition 31 décembre 2026 -> 2027. Version finale : date toujours visible,
menu présenté comme exclusif au 31 décembre, vraies vidéos du domaine (terrasse, jardin),
formats originaux (invitation, grille 4 salles, horloge, carte menu tamponnée).
Modifier ce fichier puis relancer `npm run reels:data`."""
import json, os

P = "assets/photos/"
V = "assets/video/"
DATE = "Jeudi 31 décembre 2026"
FMT = lambda d: {"width": 1080, "height": 1920, "fps": 30, "duration": d}
COMMON = {"dateBadge": DATE, "source": "Plan_Campagne_Reveillon_Villa_Beach_2026.xlsx — onglet TikTok Reels"}

def END(a, b, title="Réservez votre réveillon", note=None, bg=V + "terrasse-pergola.mp4"):
    return {"id": "fin", "start": a, "end": b, "type": "endcard", "date": DATE, "title": title, "note": note,
            "sub": "Préventes conseillées • Accès prioritaire", "venue": "Domaine Villa Beach",
            "address": "23 rue des Pyrénées, 91090 Lisses", "phone": "01 84 60 20 46", "url": None, "qr": None,
            "bgVideo": bg}

SALLES = {
    "gen": ("Généraliste", "salle-gen", "Hits · Pop · R&B · House"),
    "lat": ("Latino / SBK", "salle-latino", "Salsa · Bachata · Kizomba"),
    "ret": ("80 / 90 / 2000", "salle-retro", "Disco · Funk · Classics"),
    "car": ("Caraïbéenne", "salle-carib", "Zouk · Dancehall · Shatta"),
}
INVITE = lambda: {"kicker": "Vous êtes invité·e", "title": "Le Réveillon", "date": "31 · 12 · 2026", "venue": "Domaine Villa Beach · Lisses"}
R = {}

# 1 — Grand lancement
R["reel-01-lancement"] = {**COMMON, "title": "Reel 1 — Grand lancement", "format": FMT(25.6), "scenes": [
  {"id": "inv", "start": 0, "end": 3.2, "type": "invite", "bg": {"type": "video", "media": V + "terrasse-approche.mp4", "grade": "endvideo"}, "invite": INVITE()},
  {"id": "v", "start": 3.2, "end": 5.6, "type": "video", "media": V + "jardin-fleurs-9x16.mp4", "grade": "dusk", "trans": "whip",
   "texts": [{"role": "big", "text": "2027 approche…", "at": 3.35, "top": 760}]},
  {"id": "g", "start": 5.6, "end": 9.6, "type": "grid4", "trans": "zoom", "grid": [
     {"media": P + "dj-neon-villabeach.jpg", "fx": "30% 50%", "grade": "salle-gen", "label": "Généraliste"},
     {"media": P + "salle-latino-renverse.jpg", "fx": "45% 50%", "grade": "salle-latino", "label": "Latino / SBK"},
     {"media": P + "fete-villa.jpg", "fx": "35% 45%", "grade": "salle-retro", "label": "80 / 90 / 2000"},
     {"media": P + "couple-danse.jpg", "fx": "55% 40%", "grade": "salle-carib", "label": "Caraïbéenne"}],
   "texts": [{"role": "stamp", "text": "4 salles · 4 ambiances", "at": 7.4, "top": 860}]},
  {"id": "dj", "start": 9.6, "end": 11.4, "media": P + "dj-platines-nb.jpg", "fx": "40% 50%", "grade": "salle-gen", "trans": "whip",
   "texts": [{"role": "mid", "text": "DJs invités", "at": 9.7, "top": 820}]},
  {"id": "bt", "start": 11.4, "end": 13.2, "media": P + "piste-mains-levees.jpg", "fx": "60% 45%", "grade": "club", "trans": "flash",
   "texts": [{"role": "mid", "text": "Blind test géant", "at": 11.5, "top": 820}]},
  {"id": "ld", "start": 13.2, "end": 15.0, "media": P + "salle-latino-renverse.jpg", "fx": "45% 50%", "grade": "salle-latino", "trans": "rise",
   "texts": [{"role": "big", "text": "Jusqu'à 05 h", "at": 13.3, "top": 760}]},
  {"id": "ck", "start": 15.0, "end": 17.4, "type": "clock", "digital": "23:59", "trans": "zoom"},
  {"id": "ny", "start": 17.4, "end": 19.6, "media": P + "fete-villa.jpg", "fx": "70% 40%", "grade": "midnight", "celebrate": True, "trans": "flash",
   "texts": [{"role": "burst", "text": "Bonne année", "at": 17.5}, {"role": "big", "text": "2027 !", "at": 17.8, "top": 700}]},
  END(19.6, 25.6, "Réservez maintenant")],
 "voiceover": {"lines": [{"start": 0.3, "text": "Le 31 décembre, préparez-vous à vivre une nuit exceptionnelle. Le Domaine Villa Beach vous donne rendez-vous pour célébrer 2027 : quatre salles, DJs, animations et fête jusqu'à cinq heures. Réservez dès maintenant."}]},
 "music": {"sections": [{"style": "intro", "start": 0, "end": 3.2}, {"style": "houselight", "start": 3.2, "end": 5.6},
   {"style": "house", "start": 5.6, "end": 15.0}, {"style": "build", "start": 15.0, "end": 17.4},
   {"style": "drop", "start": 17.4, "end": 19.6}, {"style": "outro", "start": 19.6, "end": 25.6}]}}

# 2 — 4 univers (quiz « Team ? »)
pics = {"gen": (P + "dj-neon-villabeach.jpg", "30% 50%"), "lat": (P + "salle-latino-couple-1.jpg", "45% 40%"),
        "ret": (P + "fete-villa.jpg", "35% 45%"), "car": (P + "couple-danse.jpg", "55% 40%")}
music = {"gen": "house", "lat": "latin", "ret": "disco", "car": "carib"}
sc, mu = [], []
for i, k in enumerate(["gen", "lat", "ret", "car"]):
    n, gr, ge = SALLES[k]; a = i * 3.0
    sc.append({"id": k, "start": a, "end": a + 3.0, "media": pics[k][0], "fx": pics[k][1], "grade": gr, "trans": ["none", "whip", "zoom", "rise"][i],
               "salle": {"num": f"Salle {i+1} / 4", "name": f"Team {n} ?", "genres": ge}})
    mu.append({"style": music[k], "start": a, "end": a + 3.0})
sc.append({"id": "g", "start": 12.0, "end": 14.6, "type": "grid4", "trans": "flash", "grid": [
   {"media": P + "dj-platines-nb.jpg", "fx": "40% 50%", "grade": "salle-gen", "label": "Généraliste", "at": 0},
   {"media": P + "couple-danse-salsa.jpg", "fx": "50% 40%", "grade": "salle-latino", "label": "Latino", "at": 0.15},
   {"media": P + "piste-mains-levees.jpg", "fx": "55% 50%", "grade": "salle-retro", "label": "80-90-2000", "at": 0.3},
   {"media": P + "couple-danse-sombre.jpg", "fx": "50% 40%", "grade": "salle-carib", "label": "Caraïbes", "at": 0.45}],
   "texts": [{"role": "stamp", "text": "Et vous, team quoi ?", "at": 13.0, "top": 860}]})
mu.append({"style": "drop", "start": 12.0, "end": 14.6})
sc.append(END(14.6, 20.6, "4 salles, une seule nuit", bg=V + "jardin-pergola-9x16.mp4"))
mu.append({"style": "outro", "start": 14.6, "end": 20.6})
R["reel-02-quatre-univers"] = {**COMMON, "title": "Reel 2 — 4 univers", "format": FMT(20.6), "scenes": sc,
  "voiceover": {"optional": True, "lines": [{"start": 12.1, "text": "Quelle salle sera votre QG ?"}]}, "music": {"sections": mu}}

# 3 — Dîner de fête : menu EXCLUSIF au 31 décembre
R["reel-03-diner"] = {**COMMON, "title": "Reel 3 — Dîner du réveillon (menu exclusif)", "format": FMT(24), "scenes": [
  {"id": "v", "start": 0, "end": 3.0, "type": "video", "media": V + "terrasse-approche.mp4", "grade": "dusk",
   "texts": [{"role": "kicker", "text": "Un soir. Un seul menu.", "at": 0.15}, {"role": "title", "text": "Le dîner du réveillon", "at": 0.4}]},
  {"id": "t", "start": 3.0, "end": 5.6, "media": P + "table-dressee-rose-bougies.jpg", "fx": "50% 50%", "grade": "warm", "trans": "whip",
   "texts": [{"role": "mid", "text": "Servi uniquement le 31 décembre", "top": 620, "at": 3.1},
             {"role": "stamp", "text": "Menu exclusif", "at": 4.0, "top": 1040}]},
  {"id": "e", "start": 5.6, "end": 7.8, "media": P + "tartare-crevettes-mangue.jpg", "fx": "50% 50%", "grade": "warm", "trans": "zoom",
   "texts": [{"role": "chip", "text": "Tartare exotique", "at": 5.7}, {"role": "low", "text": "avocat · crevettes · saumon · mangue", "at": 6.0, "top": 1060}]},
  {"id": "m", "start": 7.8, "end": 14.4, "type": "menucard", "trans": "rise",
   "bg": {"media": P + "table-dressee-rose-bougies.jpg", "fx": "30% 50%", "grade": "softblur"},
   "menu": {"kicker": "Menu du Nouvel An", "title": "31 décembre 2026", "stamp": "Exclusif\n31.12 uniquement", "stampAt": 4.4, "courses": [
     {"k": "Apéritif", "v": "2 amuse-bouches & coupe de bulles"},
     {"k": "Entrée au choix", "v": "Foie gras maison, chutney de figues · ou tartare exotique"},
     {"k": "Plat au choix", "v": "Pavé de veau, gratin dauphinois · ou noix de Saint-Jacques, risotto aux cèpes"},
     {"k": "Dessert", "v": "Assortiment de bûches du Nouvel An"},
     {"k": "Boissons", "v": "1 bouteille de vin pour 2"}]}},
  {"id": "p", "start": 14.4, "end": 18.0, "media": P + "tartare-crevettes-mangue.jpg", "fx": "80% 50%", "grade": "blur", "trans": "flash",
   "cards": [{"big": "120 € / pers.", "small": "Dîner de fête", "at": 14.5},
             {"big": "180 € / pers.", "small": "Dîner Champagne", "at": 15.1},
             {"big": "Dès 19 h", "small": "puis les 4 salles jusqu'à 05 h", "at": 15.7}]},
  END(18.0, 24.0, "Réservez votre dîner", note="Menu exclusif · uniquement le 31.12")],
 "voiceover": {"lines": [{"start": 0.3, "text": "Pour commencer la nouvelle année avec élégance, découvrez notre dîner de fête. Un menu raffiné, servi uniquement le soir du réveillon, deux formules et l'accès aux quatre salles pour poursuivre la soirée."}]},
 "music": {"sections": [{"style": "intro", "start": 0, "end": 3}, {"style": "lounge", "start": 3, "end": 18}, {"style": "outro", "start": 18, "end": 24}]}}

# 4 — Expérience VIP
PK = [("Pack Classique", "200 €", "4 entrées · table · 1 bouteille", P + "amies-tenues-chic-bouteille.jpg", "45% 60%"),
      ("Pack Premium", "280 €", "4 entrées · table · bouteille premium", P + "bar-flamme-cocktail.jpg", "50% 45%"),
      ("Pack Magnum", "500 €", "8 entrées · table · magnum premium", P + "serveur-cocktails-plateau.jpg", "55% 55%"),
      ("Pack Ultra VIP", "1 200 €", "16 entrées · place Ultra VIP · réhoboam 4,5 L", P + "groupe-neon-villabeach.jpg", "50% 45%")]
sc = [{"id": "a", "start": 0, "end": 3, "type": "video", "media": V + "jardin-pergola-9x16.mp4", "grade": "dusk",
       "texts": [{"role": "brand", "text": "Votre réveillon", "at": 0.15}, {"role": "tagline", "text": "en mode VIP", "at": 0.45}]}]
for i, (n, pr, inc, img, fx) in enumerate(PK):
    a = 3 + i * 2.5
    sc.append({"id": f"p{i+1}", "start": a, "end": a + 2.5, "media": img, "fx": fx, "grade": "dark", "trans": ["zoom", "whip", "rise", "flash"][i],
               "texts": [{"role": "price", "label": n, "text": pr, "at": a + 0.08}, {"role": "menu", "text": inc, "at": a + 0.35}]})
sc.append(END(13, 19, "Réservez votre table"))
R["reel-04-vip"] = {**COMMON, "title": "Reel 4 — Expérience VIP", "format": FMT(19), "scenes": sc,
 "voiceover": {"lines": [{"start": 0.3, "text": "Tables, bouteilles et espaces VIP. Choisissez votre pack et vivez le réveillon en grand."}]},
 "music": {"sections": [{"style": "build", "start": 0, "end": 3}, {"style": "drop", "start": 3, "end": 13}, {"style": "outro", "start": 13, "end": 19}]}}

# 5 — Countdown minuit
cd_beats = [round(8.0 + i * 0.3, 2) for i in range(10)]
R["reel-05-countdown"] = {**COMMON, "title": "Reel 5 — Countdown minuit", "format": FMT(21), "scenes": [
  {"id": "h", "start": 0, "end": 4, "type": "clock", "digital": "23:59"},
  {"id": "dj", "start": 4, "end": 6, "media": P + "dj-neon-villabeach.jpg", "fx": "30% 50%", "grade": "club", "trans": "flash",
   "texts": [{"role": "big", "text": "Prêts ?", "at": 4.1, "top": 760}]},
  {"id": "dj2", "start": 6, "end": 8, "media": P + "piste-mains-levees.jpg", "fx": "60% 45%", "grade": "club", "trans": "whip",
   "texts": [{"role": "mid", "text": "Tous ensemble…", "at": 6.1, "top": 820}]},
  {"id": "cd", "start": 8, "end": 11, "type": "countdown", "beats": cd_beats, "labels": [str(10 - i) for i in range(10)], "kicker": "Minuit"},
  {"id": "ny", "start": 11, "end": 15, "media": P + "fete-villa.jpg", "fx": "70% 40%", "grade": "midnight", "celebrate": True, "trans": "flash",
   "texts": [{"role": "burst", "text": "Happy New Year", "at": 11.1}, {"role": "big", "text": "2027 !", "at": 11.4, "top": 700}]},
  END(15, 21, "Fêtez 2027 avec nous")],
 "voiceover": {"lines": []},
 "music": {"sections": [{"style": "intro", "start": 0, "end": 4}, {"style": "build", "start": 4, "end": 8},
   {"style": "countdown", "beats": cd_beats}, {"style": "drop", "start": 11, "end": 15}, {"style": "outro", "start": 15, "end": 21}]}}

os.makedirs("data/reels", exist_ok=True)
for k, v in R.items():
    json.dump(v, open(f"data/reels/{k}.json", "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print(k, v["format"]["duration"], "s")
