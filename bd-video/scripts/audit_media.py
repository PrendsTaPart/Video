#!/usr/bin/env python3
"""Inventaire des médias du dépôt pour « La Brigade augmentée » (étape 0).

Parcourt les fichiers suivis par Git (LFS compris), relève les métadonnées
avec ffprobe, estime la présence de voix (webrtcvad) et propose un usage.

    pip install webrtcvad-wheels
    python3 bd-video/scripts/audit_media.py   # écrit bd-video/assets/catalog.json
"""
import hashlib
import json
import os
import re
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from fractions import Fraction

ROOT = subprocess.check_output(["git", "rev-parse", "--show-toplevel"], text=True).strip()
OUT = os.path.join(ROOT, "bd-video", "assets", "catalog.json")

VIDEO = {".mp4", ".mov", ".webm", ".mkv", ".m4v", ".gif"}
AUDIO = {".mp3", ".wav", ".m4a", ".aac", ".ogg", ".flac"}
IMAGE = {".png", ".jpg", ".jpeg", ".webp", ".svg"}
FONT = {".ttf", ".otf", ".woff", ".woff2"}
SUBS = {".vtt", ".srt", ".ass"}

try:
    import webrtcvad
except ImportError:
    webrtcvad = None


def kind_of(ext):
    for k, s in (("video", VIDEO), ("audio", AUDIO), ("image", IMAGE), ("police", FONT), ("sous-titres", SUBS)):
        if ext in s:
            return k
    return None


def ffprobe(path):
    try:
        out = subprocess.run(
            ["ffprobe", "-v", "error", "-print_format", "json", "-show_format", "-show_streams", path],
            capture_output=True, text=True, timeout=60,
        )
        return json.loads(out.stdout or "{}")
    except Exception:
        return {}


def speech_ratio(path, seconds=90):
    """Part des trames de 30 ms classées « parole » sur les 90 premières secondes."""
    if webrtcvad is None:
        return None
    try:
        pcm = subprocess.run(
            ["ffmpeg", "-v", "error", "-t", str(seconds), "-i", path, "-vn", "-ac", "1", "-ar", "16000", "-f", "s16le", "-"],
            capture_output=True, timeout=120,
        ).stdout
    except Exception:
        return None
    frame = 960  # 30 ms à 16 kHz, 16 bits
    vad = webrtcvad.Vad(3)
    total = voiced = 0
    for i in range(0, len(pcm) - frame + 1, frame):
        chunk = pcm[i:i + frame]
        if max(abs(int.from_bytes(chunk[j:j + 2], "little", signed=True)) for j in range(0, frame, 64)) < 300:
            total += 1
            continue
        total += 1
        if vad.is_speech(chunk, 16000):
            voiced += 1
    return round(voiced / total, 3) if total else 0.0


def ratio_label(w, h):
    if not w or not h:
        return None
    r = w / h
    for name, val in (("9:16", 9 / 16), ("16:9", 16 / 9), ("1:1", 1), ("4:5", 4 / 5), ("4:3", 4 / 3), ("3:4", 3 / 4), ("A4 portrait", 794 / 1123)):
        if abs(r - val) < 0.02:
            return name
    return str(Fraction(w, h).limit_denominator(50)).replace("/", ":")


VO_HINT = re.compile(r"(^|/)(vo|voice|voix|voix-off|narration)(/|$)|(^|[/_-])(vo|voix|narr)[_-]", re.I)


def classify(rel, kind, meta):
    """Retourne (categorie, usage propose, recommandation)."""
    p = rel.lower()
    name = os.path.basename(p)
    in_skill = p.startswith("studio-video/.agents/")

    if kind == "police":
        return "habillage/police", "polices d'habillage", "à réutiliser" if re.search(r"bangers|comic", p) else "à ignorer"
    if kind == "sous-titres":
        return "habillage/sous-titres", "modèle de sous-titres", "à ignorer"

    if in_skill:
        if "/sfx/" in p:
            return "sfx", "bruitages Pixabay (licence libre, cf. CREDITS.md)", "à réutiliser"
        return "asset de skill", "exemple fourni avec un skill HyperFrames", "à ignorer"

    if "third-party-logos" in p or re.search(r"logo-(claude|mistral|openai)", p):
        return "logo-tiers", "logo réel d'un tiers (Claude…) — à prendre de préférence dans Figma", "à réutiliser tel quel"
    if re.search(r"product-screenshots", p):
        return "image/capture-ui", "capture d'écran du logiciel", "à réutiliser"
    if re.search(r"brand/(mascots|profile)", p):
        return "image/personnage", "mascotte FoodEatUp (hors univers BD)", "à ignorer"
    if "brand/scenes" in p and kind == "image":
        return "image diverse", "photo d'illustration (hors univers BD)", "à ignorer"
    if re.search(r"brand/(loops|scenes)", p) and kind == "video":
        return "plan-higgsfield", "boucle réaliste (cuisine, salle)", "à réutiliser (insert ponctuel)"
    if "logo-sting" in p or (re.search(r"logo", p) and kind == "video"):
        return "intro-outro-logo", "logo animé (sting)", "à réutiliser"
    if re.search(r"(^|/)(brand|logo)s?(/|$)|logo", p):
        return "intro-outro-logo", "logo / identité FoodEatUp", "à réutiliser"
    if re.search(r"outro|intro|end-?card|signature", p):
        return "intro-outro-logo", "intro / outro / carton de fin", "à réutiliser" if kind == "video" else "à ignorer"

    if kind == "audio":
        if re.search(r"music|musique|bgm|jingle", p):
            return "musique", "musique d'ambiance (placeholder ElevenLabs Music)", "à refaire"
        if re.search(r"sfx|(^|/)son-|bruit", p):
            return "sfx", "bruitage", "à réutiliser"
        if VO_HINT.search(p) or meta.get("voix") in ("oui", "probable"):
            return "voix-off", "voix off d'une autre vidéo (texte différent de la BD)", "à ignorer"
        return "audio divers", "", "à ignorer"

    if kind == "video":
        if "foodeatup-saison-2/renders/" in p and "/source/" in p:
            return "plan-seedance", "plan Seedance/Higgsfield saison 2 (Michael en live)", "à réutiliser (insert ponctuel)"
        if p.startswith("hero-video/assets/video/") or "/assets/video/hf" in p:
            return "plan-higgsfield", "plan Higgsfield réaliste (cuisine, salle, caisse)", "à réutiliser (insert ponctuel)"
        if "_captures" in p or "capture" in name or "-tuto" in p or "tutoriel" in p or "planit-tuto" in p:
            return "plan-tutoriel", "capture d'écran du logiciel (série « une case, une fonction »)", "à réutiliser"
        if "/renders/" in p or p.endswith("-final.mp4"):
            return "rendu-final", "vidéo déjà montée (référence de style)", "à ignorer"
        return "plan divers", "", "à ignorer"

    # images
    if re.search(r"portrait|avatar|personnage|character|cast", p):
        return "image/personnage", "portrait (autre univers que la BD)", "à ignorer"
    if re.search(r"screen|capture|ecran|écran|ui-", p):
        return "image/capture-ui", "capture d'écran du logiciel", "à réutiliser"
    if re.search(r"lower|third|transition|bubble|bulle|cartouche|frame", p):
        return "habillage", "élément d'habillage", "à réutiliser"
    return "image diverse", "", "à ignorer"


def probe(rel):
    path = os.path.join(ROOT, rel)
    ext = os.path.splitext(rel)[1].lower()
    kind = kind_of(ext)
    size = os.path.getsize(path) if os.path.exists(path) else 0
    rec = {"path": rel, "type": kind, "taille_octets": size}
    h = hashlib.md5()
    with open(path, "rb") as fh:
        for block in iter(lambda: fh.read(1 << 20), b""):
            h.update(block)
    rec["md5"] = h.hexdigest()

    with open(path, "rb") as fh:
        head = fh.read(200)
    if head.startswith(b"version https://git-lfs"):
        rec["lfs"] = "pointeur (contenu non téléchargé)"
        rec["categorie"], rec["usage"], rec["recommandation"] = classify(rel, kind, rec)
        return rec

    if kind in ("video", "audio", "image"):
        info = ffprobe(path)
        fmt = info.get("format", {})
        v = next((s for s in info.get("streams", []) if s.get("codec_type") == "video"), None)
        a = next((s for s in info.get("streams", []) if s.get("codec_type") == "audio"), None)
        if kind != "image":
            d = fmt.get("duration")
            rec["duree_s"] = round(float(d), 2) if d else None
            br = fmt.get("bit_rate")
            rec["debit_kbps"] = round(int(br) / 1000) if br else None
        if v and kind != "audio":
            w, h = v.get("width"), v.get("height")
            rec.update({"largeur": w, "hauteur": h, "ratio": ratio_label(w, h)})
            if kind == "video":
                fr = v.get("avg_frame_rate") or v.get("r_frame_rate")
                try:
                    rec["fps"] = round(float(Fraction(fr)), 2) if fr and fr != "0/0" else None
                except (ValueError, ZeroDivisionError):
                    rec["fps"] = None
                rec["codec_video"] = v.get("codec_name")
        if kind == "image" and ext == ".svg":
            rec["ratio"] = None
        if kind in ("video", "audio"):
            rec["codec_audio"] = a.get("codec_name") if a else None
            if not a:
                rec["voix"] = "pas d'audio"
            else:
                r = speech_ratio(path)
                rec["parole_ratio"] = r
                hint = bool(VO_HINT.search(rel.lower()))
                if hint:
                    rec["voix"] = "oui"
                elif r is None:
                    rec["voix"] = "inconnu"
                elif r >= 0.35:
                    rec["voix"] = "probable"
                elif r >= 0.12:
                    rec["voix"] = "possible"
                else:
                    rec["voix"] = "non"

    rec["categorie"], rec["usage"], rec["recommandation"] = classify(rel, kind, rec)
    return rec


def main():
    files = subprocess.check_output(["git", "ls-files", "-z"], cwd=ROOT, text=True).split("\0")
    files = [f for f in files if f and kind_of(os.path.splitext(f)[1].lower()) and not f.startswith("bd-video/")]
    files = [f for f in files if "/node_modules/" not in f]
    with ThreadPoolExecutor(max_workers=os.cpu_count() or 4) as ex:
        records = list(ex.map(probe, files))
    records.sort(key=lambda r: r["path"])
    first = {}
    for r in records:
        if r["md5"] in first:
            r["doublon_de"] = first[r["md5"]]
        else:
            first[r["md5"]] = r["path"]
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as fh:
        json.dump({"genere_par": "bd-video/scripts/audit_media.py", "total": len(records),
                   "uniques": len(first), "medias": records}, fh, ensure_ascii=False, indent=1)
    print(f"{len(records)} médias -> {os.path.relpath(OUT, ROOT)}", file=sys.stderr)


if __name__ == "__main__":
    main()
