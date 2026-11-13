#!/usr/bin/env python3
"""Tutoriels vidéo de l'application Cocuisinage — un projet HyperFrames par sujet.

Entrées :
  - les images filmées dans la vraie application par `app/tool/tutoriels_test.dart`
    (dépôt App-Demo-FoodEatUp-, dossier captures/tutoriels/<sujet>/ : 0001.png… + plan.json) ;
  - la voix ElevenLabs de chaque sujet (assets/voix/<sujet>.mp3, voix « Adam », eleven_v4) ;
  - la musique des stories FoodEatUp (assets/audio/musique.mp3) ;
  - les images officielles (logo, mascotte, Végé-fruités) embarquées dans l'application, non retouchées.

Sortie : <sujet>/index.html (+ ses médias), à rendre avec `npx hyperframes render`.
Usage : python3 build.py --captures ../../../app-demo-foodeatup-/captures/tutoriels [sujet…]
"""
import argparse
import json
import re
import shutil
import subprocess
from pathlib import Path

ICI = Path(__file__).resolve().parent
APP_ASSETS_DEFAUT = Path('/home/user/app-demo-foodeatup-/app/assets')
GSAP = ICI.parents[1] / 'studio-video' / 'assets' / 'vendor' / 'gsap.min.js'

W, H = 1080, 1920
INTRO = 2.0  # le générique avant le téléphone
OUTRO = 2.6
ECRAN_L, ECRAN_H = 412, 915  # dp, comme le tournage
TEL_L = 600  # largeur de l'écran du téléphone dans la vidéo, en px
ECHELLE = TEL_L / ECRAN_L
TEL_H = round(ECRAN_H * ECHELLE)
TEL_X = (W - TEL_L) // 2
TEL_Y = 300

# sujet → (titre, Végé-fruité ou image de la mascotte, texte exact de la voix)
SUJETS = {
    'premier-lancement': ('Le premier lancement', 'cocuisinage/chef.webp',
        "Bienvenue dans Cocuisinage ! Au premier lancement, votre chef se présente : recettes, frigo, batch cooking, plan de repas, accords, scanner… Touchez « Suivant » : vos commerces de bouche, leurs recettes à cuisiner chez vous, et le chef qui répond à vos questions. Pour finir, cochez ce qui vous intéresse, puis touchez « Découvrir le réseau »."),
    'quartier': ('Mon Quartier Gourmand', 'vegefruits/capitaine-carotte.webp',
        "Mon Quartier Gourmand. La première fois, cinq Végé-fruités vous expliquent le jeu : touchez « Suivant », puis « Compris ». Juste en dessous, les commerces de votre quartier, et les propositions de la communauté, en vérification. Votre niveau et vos points sont comptés par FoodEatUp. Touchez « Mes missions » : chaque mission faite vous rapporte des points."),
    'autour-de-moi': ('Autour de moi', 'vegefruits/mango-queen.webp',
        "Autour de moi. La carte place les lieux du réseau ; activez la localisation pour voir les plus proches. Sous la carte, la liste des lieux : touchez-en un pour ouvrir sa fiche, puis suivez-le, réservez, ou commandez."),
    'recette': ('La fiche recette', 'vegefruits/don-tomate.webp',
        "La fiche recette. Touchez « Écouter la recette » pour tout entendre, ou le haut-parleur d'une étape pour l'écouter seule. L'appareil photo, lui, photographie l'étape : ouvrez-le, prenez la photo, puis touchez « Utiliser pour l'étape ». Elle reste sur votre téléphone, et vous pouvez la proposer à FoodEatUp."),
    'scanner': ('Le scanner', 'vegefruits/kevin-kiwi.webp',
        "Le scanner. Placez le code-barres dans le cadre, ou tapez-le, puis touchez « Analyser ». Vous voyez le Nutri-Score, le groupe NOVA, et les valeurs pour cent grammes, avant de mettre le produit dans le panier."),
    'moi': ('La page Moi', 'vegefruits/le-sage-brocoli.webp',
        "La page Moi. En haut, votre profil, et l'accès à Mon Quartier Gourmand. Puis vos raccourcis, rangés selon vos centres d'intérêt. Plus bas : vos points, votre portefeuille de cartes, vos restaurants suivis, et vos recettes favorites."),
}


def duree(f: Path) -> float:
    out = subprocess.check_output(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', str(f)])
    return float(out.strip())


def morceaux(texte: str) -> list[str]:
    """Des sous-titres courts : on coupe aux fins de phrase, puis aux deux-points et points-virgules."""
    parts = re.split(r'(?<=[.!?…;:])\s+', texte)
    res = []
    for p in parts:
        while len(p) > 70 and ', ' in p[30:]:
            i = p.index(', ', 30) + 1
            res.append(p[:i].strip())
            p = p[i:].strip()
        res.append(p.strip())
    return [r for r in res if r]


def sous_titres(texte: str, debut: float, total: float) -> list[tuple[float, float, str]]:
    """Temps de chaque morceau, proportionnel à sa longueur (la voix lit d'un débit régulier)."""
    ms = morceaux(texte)
    poids = [len(m) + 8 for m in ms]
    t, res = debut, []
    for m, p in zip(ms, poids):
        d = total * p / sum(poids)
        res.append((t, d, m))
        t += d
    return res


def html_esc(s: str) -> str:
    return s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')


def construire(sujet: str, captures: Path, app_assets: Path) -> Path:
    titre, perso, texte = SUJETS[sujet]
    dossier = ICI / sujet
    (dossier / 'media').mkdir(parents=True, exist_ok=True)
    src = captures / sujet
    plan = json.loads((src / 'plan.json').read_text())
    voix = ICI / 'assets' / 'voix' / f'{sujet}.mp3'
    d_voix = duree(voix)

    # L'écran filmé, ralenti juste ce qu'il faut pour suivre la voix.
    natif = plan['images'] / plan['fps']
    t_ecran = d_voix + 0.6
    lent = t_ecran / natif
    ecran = dossier / 'media' / 'ecran.mp4'
    subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-framerate', f"{plan['fps'] / lent:.5f}", '-i', str(src / '%04d.png'),
                    '-vf', 'fps=30,format=yuv420p', '-c:v', 'libx264', '-crf', '18', '-preset', 'slow', '-movflags', '+faststart', str(ecran)], check=True)
    t_ecran = duree(ecran)

    # Voix à -16 LUFS avant le mélange (FOODEATUP-TUTORIELS-WORKFLOW.md : loudnorm par ligne, pas sur le mix).
    subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-i', str(voix), '-af', 'loudnorm=I=-16:TP=-1.5:LRA=11', '-ar', '44100',
                    '-c:a', 'libmp3lame', '-b:a', '192k', str(dossier / 'media' / 'voix.mp3')], check=True)
    for f, dest in [(ICI / 'assets' / 'audio' / 'musique.mp3', 'musique.mp3'), (app_assets / perso, 'perso.webp'),
                    (app_assets / 'brand' / 'logo-foodeatup.png', 'logo.png'), (app_assets / 'fonts' / 'Fraunces-SemiBold.ttf', 'Fraunces.ttf'),
                    (app_assets / 'fonts' / 'Manrope-ExtraBold.ttf', 'Manrope.ttf'), (GSAP, 'gsap.min.js')]:
        shutil.copyfile(f, dossier / 'media' / dest)

    total = round(INTRO + t_ecran + OUTRO, 3)
    debut_voix = INTRO + 0.2
    subs = sous_titres(texte, debut_voix, d_voix)
    touchers = [(INTRO + (t['image'] - 1) / plan['fps'] * lent, t['x'], t['y']) for t in plan['touchers']]

    subs_html = '\n'.join(
        f'      <div id="st-{i}" class="clip st" data-start="{a:.3f}" data-duration="{d:.3f}" data-track-index="6"><span>{html_esc(m)}</span></div>'
        for i, (a, d, m) in enumerate(subs))
    doigts_html = '\n'.join(
        f'      <div id="doigt-{i}" class="clip doigt" data-start="{max(0, t - 0.35):.3f}" data-duration="1.1" data-track-index="{7 + i % 2}" '
        f'style="left:{TEL_X + x * ECHELLE - 60:.0f}px; top:{TEL_Y + y * ECHELLE - 60:.0f}px"><i class="onde"></i><i class="point"></i></div>'
        for i, (t, x, y) in enumerate(touchers))
    doigts_js = '\n'.join(
        f'      tl.fromTo("#doigt-{i} .point", {{scale: 1.6, opacity: 0}}, {{scale: 1, opacity: 1, duration: 0.3, ease: "back.out(2)"}}, {max(0, t - 0.35):.3f});\n'
        f'      tl.fromTo("#doigt-{i} .onde", {{scale: 0.4, opacity: 0.9}}, {{scale: 1.8, opacity: 0, duration: 0.7, ease: "power2.out"}}, {t:.3f});\n'
        f'      tl.to("#doigt-{i} .point", {{opacity: 0, duration: 0.3}}, {t + 0.45:.3f});'
        for i, (t, x, y) in enumerate(touchers))
    subs_js = '\n'.join(f'      tl.fromTo("#st-{i} span", {{y: 24, opacity: 0}}, {{y: 0, opacity: 1, duration: 0.25, ease: "power2.out"}}, {a:.3f});'
                        for i, (a, d, m) in enumerate(subs))
    fin = INTRO + t_ecran

    html = f'''<!doctype html>
<html lang="fr">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width={W}, height={H}" />
    <title>Tutoriel Cocuisinage — {html_esc(titre)}</title>
    <script src="media/gsap.min.js"></script>
    <style>
      @font-face {{ font-family: "Fraunces"; src: url("media/Fraunces.ttf"); font-weight: 600; }}
      @font-face {{ font-family: "Manrope"; src: url("media/Manrope.ttf"); font-weight: 800; }}
      * {{ margin: 0; padding: 0; box-sizing: border-box; }}
      html, body {{ width: {W}px; height: {H}px; overflow: hidden; background: #0F1A23; }}
      #root {{ position: relative; width: {W}px; height: {H}px; overflow: hidden; font-family: "Manrope", sans-serif; }}
      .fond {{ position: absolute; inset: 0; background: radial-gradient(circle at 50% 30%, #FFFDF2 0%, #FCF9E6 55%, #F6EBC8 100%); }}
      .rond {{ position: absolute; border-radius: 50%; }}
      #rond-a {{ width: 520px; height: 520px; left: -180px; top: 120px; background: #FFA50033; }}
      #rond-b {{ width: 420px; height: 420px; right: -150px; top: 1250px; background: #007BFF22; }}
      #entete {{ position: absolute; left: 0; right: 0; top: 70px; text-align: center; }}
      #puce {{ display: inline-block; padding: 10px 26px; border-radius: 40px; background: #007BFF; color: #fff; font-size: 30px; letter-spacing: 2px; }}
      #titre {{ display: block; margin-top: 22px; font-family: "Fraunces", serif; font-size: 76px; color: #0F1A23; }}
      #telephone {{ position: absolute; left: {TEL_X - 18}px; top: {TEL_Y - 18}px; width: {TEL_L + 36}px; height: {TEL_H + 36}px;
                   border-radius: 64px; background: #0F1A23; box-shadow: 0 40px 80px #0F1A2355; }}
      #ecran {{ position: absolute; left: 18px; top: 18px; width: {TEL_L}px; height: {TEL_H}px; border-radius: 48px; overflow: hidden; background: #fff; }}
      #ecran video {{ width: 100%; height: 100%; object-fit: cover; }}
      .doigt {{ position: absolute; width: 120px; height: 120px; }}
      .doigt i {{ position: absolute; inset: 0; border-radius: 50%; display: block; }}
      .doigt .point {{ inset: 30px; background: #FFA500CC; border: 6px solid #fff; box-shadow: 0 6px 18px #0F1A2366; }}
      .doigt .onde {{ border: 8px solid #FFA500; }}
      .st {{ position: absolute; left: 60px; right: 60px; top: 1712px; text-align: center; }}
      .st span {{ display: inline-block; padding: 14px 26px; border-radius: 22px; background: #0F1A23E6; color: #fff; font-size: 40px; line-height: 1.25; }}
      #carte {{ position: absolute; inset: 0; display: flex; flex-direction: column; align-items: center; justify-content: center; }}
      #perso {{ width: 560px; height: 560px; object-fit: contain; padding: 40px; border-radius: 50%; background: #fff; box-shadow: 0 30px 70px #FFA50055; }}
      #carte-titre {{ margin-top: 30px; font-family: "Fraunces", serif; font-size: 84px; color: #0F1A23; text-align: center; padding: 0 60px; }}
      #carte-sous {{ margin-top: 18px; font-size: 38px; color: #007BFF; }}
      #fin {{ position: absolute; inset: 0; display: flex; flex-direction: column; align-items: center; justify-content: center; }}
      #fin-perso {{ width: 460px; height: 460px; object-fit: contain; padding: 34px; border-radius: 50%; background: #fff; box-shadow: 0 30px 70px #007BFF44; }}
      #fin-texte {{ margin-top: 30px; font-family: "Fraunces", serif; font-size: 88px; color: #0F1A23; }}
      #logo {{ margin-top: 40px; width: 420px; }}
    </style>
  </head>
  <body>
    <div id="root" data-composition-id="main" data-start="0" data-duration="{total}" data-width="{W}" data-height="{H}">
      <div id="decor" class="clip" data-start="0" data-duration="{total}" data-track-index="0">
        <div class="fond"></div>
        <div id="rond-a" class="rond" data-layout-allow-overflow></div>
        <div id="rond-b" class="rond" data-layout-allow-overflow></div>
      </div>
      <div id="carte" class="clip" data-start="0" data-duration="{INTRO + 0.4}" data-track-index="1">
        <img id="perso" src="media/perso.webp" alt="" />
        <div id="carte-titre">{html_esc(titre)}</div>
        <div id="carte-sous">Tutoriel Cocuisinage</div>
      </div>
      <div id="entete" class="clip" data-start="{INTRO - 0.2}" data-duration="{t_ecran + 0.2}" data-track-index="2">
        <span id="puce">TUTORIEL</span>
        <span id="titre">{html_esc(titre)}</span>
      </div>
      <div id="telephone">
        <div id="ecran">
          <video id="video-ecran" src="media/ecran.mp4" data-start="{INTRO}" data-duration="{t_ecran}" data-track-index="4" muted playsinline></video>
        </div>
      </div>
{doigts_html}
{subs_html}
      <div id="fin" class="clip" data-start="{fin}" data-duration="{OUTRO}" data-track-index="9">
        <img id="fin-perso" src="media/perso.webp" alt="" />
        <div id="fin-texte">À vous de jouer !</div>
        <img id="logo" src="media/logo.png" alt="FoodEatUp" />
      </div>
      <audio id="voix" src="media/voix.mp3" data-start="{debut_voix}" data-duration="{d_voix}" data-track-index="10" data-volume="1"></audio>
      <audio id="musique" src="media/musique.mp3" data-start="0" data-duration="{min(total, 36)}" data-track-index="11" data-volume="0.12"></audio>
    </div>
    <script>
      window.__timelines = window.__timelines || {{}};
      const tl = gsap.timeline({{ paused: true }});
      tl.fromTo("#rond-a", {{scale: 0.8}}, {{scale: 1.1, duration: {total}, ease: "sine.inOut"}}, 0);
      tl.fromTo("#rond-b", {{scale: 1.1}}, {{scale: 0.85, duration: {total}, ease: "sine.inOut"}}, 0);
      tl.fromTo("#perso", {{scale: 0.72, rotation: -10}}, {{scale: 1, rotation: 0, duration: 0.9, ease: "elastic.out(1, 0.55)"}}, 0);
      tl.fromTo("#carte-titre", {{y: 40, scale: 0.92}}, {{y: 0, scale: 1, duration: 0.5, ease: "back.out(1.7)"}}, 0);
      tl.fromTo("#carte-sous", {{y: 30, opacity: 0}}, {{y: 0, opacity: 1, duration: 0.4, ease: "power2.out"}}, 0.7);
      tl.to("#carte", {{y: -260, opacity: 0, duration: 0.45, ease: "power2.in"}}, {INTRO - 0.4});
      tl.fromTo("#telephone", {{y: 1500, rotation: 6}}, {{y: 0, rotation: 0, duration: 0.7, ease: "back.out(1.2)"}}, {INTRO - 0.4});
      tl.fromTo("#puce", {{scale: 0, opacity: 0}}, {{scale: 1, opacity: 1, duration: 0.45, ease: "back.out(2.2)"}}, {INTRO - 0.1});
      tl.fromTo("#titre", {{y: 40, opacity: 0}}, {{y: 0, opacity: 1, duration: 0.45, ease: "power3.out"}}, {INTRO});
{doigts_js}
{subs_js}
      tl.to("#telephone", {{scale: 0.6, y: 300, opacity: 0, duration: 0.5, ease: "power2.in"}}, {fin - 0.45});
      tl.fromTo("#fin-perso", {{scale: 0.2, opacity: 0}}, {{scale: 1, opacity: 1, duration: 0.8, ease: "elastic.out(1, 0.5)"}}, {fin});
      tl.fromTo("#fin-texte", {{y: 50, opacity: 0}}, {{y: 0, opacity: 1, duration: 0.45, ease: "back.out(1.8)"}}, {fin + 0.3});
      tl.fromTo("#logo", {{y: 40, opacity: 0}}, {{y: 0, opacity: 1, duration: 0.45, ease: "power2.out"}}, {fin + 0.55});
      window.__timelines["main"] = tl;
    </script>
  </body>
</html>
'''
    (dossier / 'index.html').write_text(html)
    (dossier / 'hyperframes.json').write_text(json.dumps({'$schema': 'https://hyperframes.heygen.com/schema/hyperframes.json',
                                                          'paths': {'assets': 'media'}}, indent=2) + '\n')
    (dossier / 'package.json').write_text(json.dumps({'name': f'cocuisinage-tuto-{sujet}', 'private': True, 'type': 'module',
                                                       'scripts': {'check': 'npx --yes hyperframes@0.9.41 check',
                                                                   'render': 'npx --yes hyperframes@0.9.41 render'}}, indent=2) + '\n')
    print(f'{sujet}: voix {d_voix:.2f}s, écran {t_ecran:.2f}s (×{lent:.2f}), total {total}s, {len(touchers)} touchers, {len(subs)} sous-titres')
    return dossier


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--captures', type=Path, required=True)
    ap.add_argument('--app-assets', type=Path, default=APP_ASSETS_DEFAUT)
    ap.add_argument('sujets', nargs='*')
    a = ap.parse_args()
    for s in (a.sujets or list(SUJETS)):
        construire(s, a.captures.resolve(), a.app_assets)
