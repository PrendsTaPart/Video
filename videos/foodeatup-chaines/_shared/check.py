#!/usr/bin/env python3
"""
Contrôle automatique de index.html — critères d'acceptation C0 + contrat HyperFrames.

    python3 check.py          # index.html du dossier courant

Sort en code 1 si un seul critère échoue.
"""

import pathlib
import re
import sys

PALETTE = {"#fcf9e6", "#0f1a23", "#007bff", "#147aff", "#ffa500", "#fff", "#ffffff"}

ok, bad = [], []


def chk(cond, msg):
    (ok if cond else bad).append(msg)


def main(path: pathlib.Path) -> int:
    h = path.read_text(encoding="utf-8")

    # durée et nombre de scènes sont LUS dans le fichier, pas supposés : le même
    # contrôle sert aux variantes de 55 s et au bloc de fin, plus court.
    m = re.search(r'id="main"[^>]*data-duration="([\d.]+)"', h)
    root_duration = float(m.group(1)) if m else -1.0
    n_scenes = len(re.findall(r'class="scene clip"', h))

    # --- contrat d'import ---
    chk(bool(re.search(r'id="main"[^>]*data-composition-id="main"', h)),
        'racine live data-composition-id="main"')
    chk("<template" not in h, "aucun <template> (la racine doit être dans le DOM live)")
    for attr in ('data-width="1920"', 'data-height="1080"', 'data-start="0"'):
        chk(attr in h, f"racine {attr}")
    chk(root_duration > 0, f"racine data-duration numérique ({root_duration}s)")
    chk('window.__timelines["main"] = tl;' in h, 'timeline sur __timelines["main"]')
    chk("gsap.timeline({ paused: true })" in h, "timeline paused")
    chk("window.__resources" not in h, "pas de manifeste splash-loader")

    # --- scènes jointives ---
    scenes = re.findall(
        r'id="(s\d+)"[^>]*data-start="([\d.]+)"[^>]*data-duration="([\d.]+)"', h)
    chk(len(scenes) == n_scenes, f"{n_scenes} scènes déclarées et tuilées")
    t = 0.0
    for sid, s, d in scenes:
        s, d = float(s), float(d)
        chk(abs(s - t) < 1e-6, f"{sid} jointive à {t}s")
        t = s + d
    chk(abs(t - root_duration) < 1e-6, f"somme des scènes = {t}s == data-duration")

    # --- empilement explicite (sinon la scène sortante transparaît) ---
    for i in range(1, n_scenes + 1):
        chk(re.search(rf"#s{i} \{{ z-index: {i}; \}}", h) is not None,
            f"#s{i} a un z-index explicite")

    # --- déterminisme ---
    for pat, label in [(r"Date\.now", "Date.now"), (r"Math\.random", "Math.random"),
                       (r"setInterval", "setInterval"), (r"setTimeout", "setTimeout"),
                       (r"requestAnimationFrame", "requestAnimationFrame"),
                       (r"repeat:\s*-1", "repeat:-1"),
                       (r'from:\s*"random"', "stagger random"),
                       (r"\.play\(\)", "media .play()")]:
        chk(not re.search(pat, h), f"aucun {label}")

    # --- assets auto-portés ---
    chk("fonts.googleapis.com" not in h and "fonts.gstatic.com" not in h,
        "aucun lien Google Fonts")
    non_data = [u for u in re.findall(r"url\(([^)]+)\)", h) if not u.startswith("data:")]
    chk(not non_data, f"toutes les url() en data: URI ({non_data[:2]})")
    chk(h.count("@font-face") == 2, "2 @font-face inlinés (Fredoka + Baloo 2)")
    chk("s3://" not in h and "amazonaws.com" not in h, "aucune URL expirante/privée")
    chk("placehold" not in h, "aucun asset placeholder")
    chk(h.count("cdn.jsdelivr.net") >= 2, "runtime/GSAP depuis le CDN (non inlinés)")

    # --- shader (optionnel : un bloc en coupes franches n'en a pas) ---
    if "HyperShader.init" in h:
        sc = re.search(r"scenes:\s*\[([^\]]+)\]", h)
        n_tr = len(re.findall(r"\{ time:", h))
        n_sc = len(sc.group(1).split(",")) if sc else 0
        chk(n_sc == n_tr + 1, f"scenes({n_sc}) == transitions({n_tr})+1")
        dm = re.search(r'shader:\s*"[^"]+",\s*duration:\s*([\d.]+)', h)
        chk(dm and float(dm.group(1)) >= 0.3, "durée shader >= 0.3s")
    else:
        ok.append("aucun shader (coupes franches) — contrôle sans objet")

    # --- charte C0 ---
    off = {x.lower() for x in re.findall(r"#[0-9a-fA-F]{3,6}\b", h)} - PALETTE
    chk(not off, f"aucune couleur hors palette ({sorted(off)})")

    # --- aucun chiffre non sourcé à l'écran ---
    # On ne garde que le TEXTE rendu : on retire script/style, puis toutes les
    # balises AVEC leurs attributs. Sans ça, un style="width:62%" (largeur de
    # barre, invisible pour le spectateur) ferait échouer le critère à tort.
    visible = re.sub(r"<script.*?</script>|<style.*?</style>", "", h, flags=re.S)
    visible = re.sub(r"<[^>]+>", " ", visible)
    chk("%" not in visible, "aucun pourcentage affiché")
    chk("€" not in visible, "aucun montant affiché")
    chk(not re.search(r"\d[\d\s.,]*\s*(g|kg|€|%)\b", visible), "aucune quantité chiffrée affichée")

    print("\n".join("  OK   " + x for x in ok))
    if bad:
        print()
        print("\n".join("  ÉCHEC " + x for x in bad))
        print(f"\n{len(bad)} échec(s) sur {len(ok) + len(bad)} critères.")
        return 1
    print(f"\n{len(ok)}/{len(ok)} critères OK.")
    return 0


if __name__ == "__main__":
    target = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "index.html")
    sys.exit(main(target))
