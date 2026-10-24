#!/usr/bin/env python3
"""
Générateur des vidéos verticales « pages de l'Académie » (1080×1920).

Une vidéo = une voix off ElevenLabs (Adam) + sa transcription mot à mot
(ElevenLabs Scribe, words.json) + une musique + une liste de scènes. Chaque
scène et chaque élément apparaît sur un mot de la voix (« cue »), retrouvé dans
la transcription : rien n'est calé à l'œil.

Usage :
    python3 tools/gen_page_video.py <id> [<id> ...]   (ids de page_videos.py)

Le script écrit videos/foodeatup-<slug>/ : index.html, SCRIPT.md, meta.json,
hyperframes.json, assets (vendor, brand, audio normalisé à -16 LUFS).
"""
import html
import json
import re
import shutil
import subprocess
import sys
import unicodedata
from pathlib import Path

HERE = Path(__file__).resolve().parent
STUDIO = HERE.parent
VIDEOS = STUDIO / "videos"
TEMPLATE_ASSETS = VIDEOS / "foodeatup-recrutement-partenaires" / "assets"

sys.path.insert(0, str(HERE))
from page_videos import VIDEOS_SPEC  # noqa: E402
import os  # noqa: E402

# Dossier des voix (NN.mp3 + NN.words.json) et musiques téléchargées depuis le flow ElevenLabs.
AUDIO_DIR = Path(os.environ.get("PAGE_VIDEO_AUDIO", HERE / "_audio"))

# ── Icônes (traits, viewBox 24) ────────────────────────────────────────────
ICONS = {
    "robot": '<rect x="4" y="8" width="16" height="11" rx="3"/><path d="M12 4v4M9 13h.01M15 13h.01M9 16h6"/>',
    "book": '<path d="M4 5a2 2 0 0 1 2-2h14v16H6a2 2 0 0 0-2 2z"/><path d="M4 19V5M9 7h7"/>',
    "check": '<circle cx="12" cy="12" r="9"/><path d="M8 12l3 3 5-6"/>',
    "cross": '<circle cx="12" cy="12" r="9"/><path d="M9 9l6 6M15 9l-6 6"/>',
    "lock": '<rect x="5" y="10" width="14" height="10" rx="2"/><path d="M8 10V7a4 4 0 0 1 8 0v3"/>',
    "key": '<circle cx="8" cy="12" r="4"/><path d="M12 12h9M18 12v3M21 12v2"/>',
    "settings": '<circle cx="12" cy="12" r="3"/><path d="M12 2v3M12 19v3M2 12h3M19 12h3M5 5l2 2M17 17l2 2M5 19l2-2M17 7l2-2"/>',
    "link": '<path d="M10 14a4 4 0 0 0 6 0l3-3a4 4 0 0 0-6-6l-1 1"/><path d="M14 10a4 4 0 0 0-6 0l-3 3a4 4 0 0 0 6 6l1-1"/>',
    "plus": '<circle cx="12" cy="12" r="9"/><path d="M12 8v8M8 12h8"/>',
    "chat": '<path d="M4 5h16v11H9l-5 4z"/>',
    "play": '<rect x="3" y="5" width="18" height="14" rx="3"/><path d="M10 9l5 3-5 3z"/>',
    "bolt": '<path d="M13 2L4 14h7l-1 8 9-12h-7z"/>',
    "phone": '<rect x="7" y="2" width="10" height="20" rx="2"/><path d="M11 18h2"/>',
    "box": '<path d="M3 8l9-5 9 5v8l-9 5-9-5z"/><path d="M3 8l9 5 9-5M12 13v8"/>',
    "thermo": '<path d="M10 13V5a2 2 0 0 1 4 0v8a4 4 0 1 1-4 0z"/>',
    "team": '<circle cx="9" cy="8" r="3"/><circle cx="17" cy="9" r="2.5"/><path d="M3 20c0-4 3-6 6-6s6 2 6 6M15 14c3 0 6 2 6 6"/>',
    "truck": '<path d="M2 6h11v10H2zM13 10h5l3 3v3h-8"/><circle cx="6" cy="18" r="2"/><circle cx="17" cy="18" r="2"/>',
    "chef": '<path d="M7 14a4 4 0 1 1 2-7 4 4 0 0 1 6 0 4 4 0 1 1 2 7v5H7z"/><path d="M7 17h10"/>',
    "calc": '<rect x="5" y="2" width="14" height="20" rx="2"/><path d="M8 6h8M8 11h2M14 11h2M8 15h2M14 15h2M8 19h8"/>',
    "shop": '<path d="M3 9l2-5h14l2 5M4 9v11h16V9M3 9h18"/><path d="M10 20v-5h4v5"/>',
    "cart": '<path d="M3 4h3l2 11h11l2-8H7"/><circle cx="10" cy="19" r="1.5"/><circle cx="17" cy="19" r="1.5"/>',
    "qr": '<rect x="3" y="3" width="7" height="7"/><rect x="14" y="3" width="7" height="7"/><rect x="3" y="14" width="7" height="7"/><path d="M14 14h3v3M21 14v7h-4M14 18v3"/>',
    "card": '<rect x="2" y="5" width="20" height="14" rx="2"/><path d="M2 10h20M6 15h4"/>',
    "calendar": '<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/>',
    "star": '<path d="M12 3l2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1L3.2 9.5l6.1-.9z"/>',
    "gift": '<rect x="3" y="9" width="18" height="12" rx="1"/><path d="M3 13h18M12 9v12M12 9c-2-4-6-4-6-1s6 1 6 1 6 2 6-1-4-3-6 1"/>',
    "megaphone": '<path d="M3 10v4l13 5V5zM16 9a4 4 0 0 1 0 6M6 14l1 5h3l-1-4"/>',
    "loop": '<path d="M4 12a8 8 0 0 1 14-5l2-2v6h-6l2-2a5 5 0 0 0-9 3"/><path d="M20 12a8 8 0 0 1-14 5l-2 2v-6h6l-2 2a5 5 0 0 0 9-3"/>',
    "euro": '<path d="M17 6a7 7 0 1 0 0 12M4 10h9M4 14h9"/>',
    "rocket": '<path d="M12 2c4 3 5 8 4 13H8C7 10 8 5 12 2z"/><path d="M8 15l-3 4h4M16 15l3 4h-4"/><circle cx="12" cy="9" r="2"/>',
    "school": '<path d="M2 9l10-5 10 5-10 5z"/><path d="M6 11v5c3 3 9 3 12 0v-5M22 9v6"/>',
    "handshake": '<path d="M2 12l4-4 4 2 4-3 4 3 4 2-4 5-4 2-4-1-4-2z"/><path d="M10 10l3 3M13 9l3 3"/>',
    "bug": '<rect x="7" y="7" width="10" height="13" rx="5"/><path d="M12 7V4M9 4l1 3M15 4l-1 3M3 11h4M17 11h4M3 17h4M17 17h4"/>',
    "globe": '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3a14 14 0 0 1 0 18M12 3a14 14 0 0 0 0 18"/>',
    "heart": '<path d="M12 20s-7-4.5-7-10a4 4 0 0 1 7-2.5A4 4 0 0 1 19 10c0 5.5-7 10-7 10z"/>',
    "receipt": '<path d="M6 2h12v20l-3-2-3 2-3-2-3 2z"/><path d="M9 7h6M9 11h6M9 15h4"/>',
    "map": '<path d="M12 21s-7-6-7-11a7 7 0 0 1 14 0c0 5-7 11-7 11z"/><circle cx="12" cy="10" r="2.5"/>',
    "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
    "chart": '<rect x="3" y="4" width="18" height="16" rx="2"/><path d="M7 16v-4M12 16V8M17 16v-6"/>',
    "door": '<path d="M5 21V4a1 1 0 0 1 1-1h12a1 1 0 0 1 1 1v17M3 21h18"/><circle cx="15" cy="12" r="1"/>',
    "code": '<path d="M8 7l-5 5 5 5M16 7l5 5-5 5M14 4l-4 16"/>',
    "search": '<circle cx="11" cy="11" r="7"/><path d="M16 16l5 5"/>',
}


def icon(name, color="#007bff", size=64):
    if not name:
        return ""
    return (
        f'<svg class="ico" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" '
        f'stroke="{color}" stroke-width="2.1" stroke-linecap="round" stroke-linejoin="round">'
        f"{ICONS[name]}</svg>"
    )


# ── Transcription : retrouver les mots ─────────────────────────────────────
def norm(t):
    t = unicodedata.normalize("NFD", t.lower())
    t = "".join(c for c in t if unicodedata.category(c) != "Mn")
    return re.sub(r"[^a-z0-9']+", "", t.replace("’", "'"))


class Words:
    def __init__(self, path):
        raw = json.loads(Path(path).read_text())["words"]
        self.words = []
        for w in raw:
            if w["type"] != "word":
                continue
            if not norm(w["text"]) and self.words:  # « ? », « : » : collés au mot précédent
                self.words[-1] = dict(self.words[-1], text=self.words[-1]["text"] + " " + w["text"].strip())
                continue
            self.words.append(dict(w))
        self.cursor = 0
        self.end = self.words[-1]["end"]

    def find(self, phrase, from_start=False, advance=True):
        """Début du premier passage de `phrase` à partir du curseur, puis avance."""
        toks = [norm(t) for t in phrase.split()]
        toks = [t for t in toks if t]
        start = 0 if from_start else self.cursor
        for i in range(start, len(self.words) - len(toks) + 1):
            if all(norm(self.words[i + k]["text"]) == toks[k] for k in range(len(toks))):
                self.cursor = i + 1 if advance else i
                return round(self.words[i]["start"], 3)
        raise SystemExit(f"Cue introuvable : « {phrase} » (après le mot {start})")


# ── Sous-titres : blocs de 2 à 5 mots, coupés là où la phrase respire ──────
def build_subs(words, replacements):
    toks = [{"t": w["text"], "s": w["start"], "e": w["end"]} for w in words.words]
    # Remplacements d'affichage (« tutoriel point foodeatup point com » → URL…)
    out = []
    i = 0
    reps = [([norm(x) for x in src.split()], dst) for src, dst in replacements]
    while i < len(toks):
        for src, dst in reps:
            n = len(src)
            if [norm(t["t"]) for t in toks[i : i + n]] == src:
                last = toks[i + n - 1]["t"]
                punct = re.search(r"[.,?:;!]+$", last)
                out.append({"t": dst + (punct.group(0) if punct else ""), "s": toks[i]["s"], "e": toks[i + n - 1]["e"]})
                i += n
                break
        else:
            out.append(toks[i])
            i += 1
    for t in out:
        if norm(t["t"]) == "foodeatup":
            t["t"] = re.sub(r"(?i)foodeatup", "FoodEatUp", t["t"])
    chunks, cur = [], []
    for k, t in enumerate(out):
        cur.append(t)
        end_sentence = re.search(r"[.?!]$", t["t"]) is not None
        brk = re.search(r"[,:;]$", t["t"]) is not None
        nxt_gap = out[k + 1]["s"] - t["e"] if k + 1 < len(out) else 1
        nxt_len = len(" ".join(x["t"] for x in cur)) + (len(out[k + 1]["t"]) + 1 if k + 1 < len(out) else 0)
        if (nxt_len > 30 and len(cur) >= 2) or (k + 1 < len(out) and "." in out[k + 1]["t"][:-1] and "/" in out[k + 1]["t"]):
            chunks.append(cur)
            cur = []
            continue
        if end_sentence or (brk and len(cur) >= 2) or len(cur) >= 5 or (nxt_gap > 0.35 and len(cur) >= 2):
            chunks.append(cur)
            cur = []
    if cur:
        chunks.append(cur)
    # Un bloc d'un seul mot rejoint son voisin (le précédent si la phrase continue).
    k = 0
    while k < len(chunks):
        if len(chunks[k]) == 1 and len(chunks) > 1:
            prev_open = k > 0 and not re.search(r"[.?!]$", chunks[k - 1][-1]["t"])
            L = lambda c: len(" ".join(x["t"] for x in c))
            if prev_open and len(chunks[k - 1]) < 6 and L(chunks[k - 1] + chunks[k]) <= 42:
                chunks[k - 1].extend(chunks.pop(k))
                continue
            if k + 1 < len(chunks) and not re.search(r"[.?!]$", chunks[k][-1]["t"]) and L(chunks[k] + chunks[k + 1]) <= 42:
                chunks[k + 1] = chunks[k] + chunks[k + 1]
                chunks.pop(k)
                continue
        k += 1
    subs = []
    for c in chunks:
        text = " ".join(t["t"] for t in c)
        text = re.sub(r"\s+([?:;!])", r" \1", text)
        text = re.sub(r"[.,;:]+$", "", text).strip()
        size = min(60, int(1010 / (0.56 * max(len(text), 1))))
        subs.append([round(c[0]["s"], 3), round(c[-1]["e"] + 0.25, 3), text, size])
    for a, b in zip(subs, subs[1:]):
        a[1] = min(a[1], b[0])
    return subs


# ── Rendu HTML ─────────────────────────────────────────────────────────────
def esc(t):
    return html.escape(t, quote=True)


def render_item(it, idx):
    kind = it["kind"]
    iid = f'i{idx}'
    col = it.get("color", "#007bff")
    ic = icon(it.get("icon"), col, it.get("isize", 64))
    text = esc(it.get("text", ""))
    sub = f'<span class="sub-t">{esc(it["sub"])}</span>' if it.get("sub") else ""
    if kind == "big":
        return f'<div class="big" id="{iid}">{icon(it.get("icon"), col, 220)}<div class="big-t">{text}</div>{sub}</div>'
    if kind == "stat":
        return f'<div class="stat" id="{iid}"><div class="stat-n">{text}</div>{sub}</div>'
    if kind == "pill":
        return f'<div class="pill" id="{iid}">{ic}<span>{text}</span></div>'
    if kind == "row":
        num = f'<span class="num" style="background:{col}">{esc(str(it["num"]))}</span>' if "num" in it else ic
        return f'<div class="row card" id="{iid}">{num}<div><div class="row-t">{text}</div>{sub}</div></div>'
    if kind == "tile":
        num = f'<span class="tnum" style="color:{col}">{esc(str(it["num"]))}</span>' if "num" in it else ic
        return f'<div class="tile card" id="{iid}">{num}<div class="tile-t">{text}</div>{sub}</div>'
    if kind == "price":
        hl = " hl" if it.get("highlight") else ""
        return (f'<div class="price card{hl}" id="{iid}"><div class="p-name">{text}</div>'
                f'<div class="p-amt">{esc(it["amount"])}</div>{sub}</div>')
    if kind == "bubble":
        who = it.get("who", "me")
        return f'<div class="bubble {who}" id="{iid}">{text}</div>'
    if kind == "url":
        fs = min(50, int(820 / (0.56 * len(it["text"]))))
        return f'<div class="url" id="{iid}" style="font-size:{fs}px">{ic}<span>{text}</span></div>'
    if kind == "badge":
        return f'<div class="badge" id="{iid}" style="background:{it.get("bg", "#c88100")}">{icon(it.get("icon"), "#fff", 48)}<span>{text}</span></div>'
    if kind == "img":
        return f'<img class="{it.get("cls", "")}" id="{iid}" src="{it["src"]}" alt="" />'
    if kind == "note":
        return f'<div class="note" id="{iid}">{text}</div>'
    raise SystemExit(f"type inconnu {kind}")


ANIM = {
    "big": 'tl.from("#{id}", {{ scale: 0.5, opacity: 0, duration: 0.6, ease: "back.out(2)" }}, {t});\n'
           '      tl.from("#{id} .ico", {{ rotation: -15, y: 40, duration: 0.7, ease: "elastic.out(1, 0.5)" }}, {t});',
    "stat": 'tl.from("#{id}", {{ scale: 0.3, opacity: 0, duration: 0.6, ease: "elastic.out(1, 0.55)" }}, {t});',
    "pill": 'tl.from("#{id}", {{ y: 40, scale: 0.6, opacity: 0, duration: 0.45, ease: "back.out(2.5)" }}, {t});',
    "row": 'tl.from("#{id}", {{ x: -500, opacity: 0, duration: 0.5, ease: "back.out(1.5)" }}, {t});',
    "tile": 'tl.from("#{id}", {{ scale: 0.4, opacity: 0, duration: 0.45, ease: "back.out(2.5)" }}, {t});',
    "price": 'tl.from("#{id}", {{ y: 160, opacity: 0, duration: 0.55, ease: "back.out(1.6)" }}, {t});',
    "bubble": 'tl.from("#{id}", {{ scale: 0.5, opacity: 0, transformOrigin: "{origin}", duration: 0.45, ease: "back.out(2.2)" }}, {t});',
    "url": 'tl.from("#{id}", {{ scale: 0.6, opacity: 0, duration: 0.6, ease: "elastic.out(1, 0.6)" }}, {t});',
    "badge": 'tl.from("#{id}", {{ scale: 0, rotation: -6, duration: 0.55, ease: "elastic.out(1, 0.5)" }}, {t});',
    "img": 'tl.from("#{id}", {{ y: 80, scale: 0.8, opacity: 0, duration: 0.6, ease: "back.out(2)" }}, {t});',
    "note": 'tl.from("#{id}", {{ opacity: 0, y: 20, duration: 0.4 }}, {t});',
}


def build(spec):
    slug = spec["slug"]
    out = VIDEOS / f"foodeatup-{slug}"
    words = Words(AUDIO_DIR / f'{spec["vo"]}.words.json')
    vo_end = words.end
    total = round(vo_end + spec.get("tail", 2.6), 2)

    # Scènes : chaque scène commence sur son cue, finit au début de la suivante.
    scenes = []
    for sc in spec["scenes"]:
        t0 = 0.0 if sc["cue"] is None else words.find(sc["cue"], advance=False)
        if sc["cue"] is not None:
            t0 = max(0.0, round(t0 - 0.15, 3))
        items = []
        for it in sc.get("items", []):
            cue = it.get("cue")
            if cue is None:
                ti = t0 + 0.25
            elif cue.startswith("+"):
                ti = t0 + float(cue[1:])
            else:
                ti = max(t0 + 0.1, words.find(cue) - 0.1)
            items.append(dict(it, t=round(ti, 3)))
        scenes.append(dict(sc, t0=t0, items=items))
    cta_t = scenes[-1]["t0"]
    for a, b in zip(scenes, scenes[1:]):
        a["t1"] = b["t0"]
    scenes[-1]["t1"] = total
    subs = build_subs(words, spec.get("replace", []))

    # HTML des scènes
    n = 0
    sec_html, js = [], []
    for k, sc in enumerate(scenes):
        sid = f"s{k + 1}"
        dur = round(sc["t1"] - sc["t0"], 3)
        layout = sc.get("layout", "stack")
        kicker = f'<h2 class="kicker">{sc["kicker"]}</h2>' if sc.get("kicker") else ""
        body = []
        for it in sc["items"]:
            n += 1
            it["id"] = f"i{n}"
            body.append(render_item(it, n))
        cls = "scene clip" + (" final" if sc.get("final") else "")
        sec_html.append(
            f'      <section id="{sid}" class="{cls}" data-start="{sc["t0"]}" data-duration="{dur}" data-track-index="2">\n'
            f'        {kicker}\n        <div class="body {layout}">\n          ' + "\n          ".join(body) +
            "\n        </div>\n      </section>"
        )
        js.append(f"      // {sid} · {sc.get('note', sc.get('kicker', '') or '')}")
        if sc.get("kicker"):
            js.append(f'      tl.from("#{sid} .kicker", {{ y: -50, opacity: 0, duration: 0.45, ease: "back.out(2)" }}, {round(sc["t0"] + 0.05, 3)});')
        for it in sc["items"]:
            origin = "100% 100%" if it.get("who", "me") == "me" else "0% 100%"
            js.append("      " + ANIM[it["kind"]].format(id=it["id"], t=it["t"], origin=origin))
            if it.get("pulse"):
                pt = words.find(it["pulse"], from_start=True) if not str(it["pulse"]).startswith("+") else it["t"] + float(it["pulse"][1:])
                js.append(f'      tl.to("#{it["id"]}", {{ scale: 1.06, duration: 0.22, yoyo: true, repeat: 1, ease: "sine.inOut" }}, {round(pt, 3)});')
        if k + 1 < len(scenes):
            js.append(f'      tl.to("#{sid}", {{ opacity: 0, y: -60, duration: 0.3, ease: "power2.in" }}, {round(sc["t1"] - 0.3, 3)});')
    logo_end = cta_t if scenes[-1].get("final") else total

    page = TEMPLATE.format(
        title=esc(spec["title"]),
        comment=spec["comment"],
        total=total,
        vo_dur=round(min(vo_end + 0.4, total), 2),
        music_vol=spec.get("music_vol", 0.14),
        logo_end=round(logo_end, 3),
        sections="\n\n".join(sec_html),
        subs=json.dumps(subs, ensure_ascii=False),
        subs_end=round(min(vo_end + 0.4, total), 2),
        js="\n".join(js),
    )

    # Fichiers
    out.mkdir(parents=True, exist_ok=True)
    (out / "renders").mkdir(exist_ok=True)
    for sub in ("vendor", "brand"):
        dst = out / "assets" / sub
        if not dst.exists():
            shutil.copytree(TEMPLATE_ASSETS / sub, dst)
    (out / "assets" / "audio").mkdir(parents=True, exist_ok=True)
    for src, dst in ((AUDIO_DIR / f'{spec["vo"]}.mp3', "voix-adam.mp3"), (AUDIO_DIR / f'{spec["music"]}.mp3', "musique.mp3")):
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(src), "-af", "loudnorm=I=-16:TP=-1.5:LRA=11",
                        "-ar", "44100", "-b:a", "192k", str(out / "assets" / "audio" / dst)], check=True)
    shutil.copy(VIDEOS / "foodeatup-recrutement-partenaires" / "hyperframes.json", out / "hyperframes.json")
    (out / "meta.json").write_text(json.dumps({"id": f"foodeatup-{slug}", "name": f"foodeatup-{slug}",
                                               "createdAt": "2026-10-23T11:30:00.000Z"}, indent=2) + "\n")
    shutil.copy(AUDIO_DIR / f'{spec["vo"]}.words.json', out / "assets" / "audio" / "voix-adam.words.json")
    (out / "index.html").write_text(page)
    (out / "SCRIPT.md").write_text(script_md(spec, scenes, total))
    print(f"{slug}: {total}s, {len(scenes)} scènes, {len(subs)} sous-titres")


def script_md(spec, scenes, total):
    lines = [f'# {spec["title"]} — {total:.0f} s, vertical 1080×1920', "",
             spec["about"], "", f'**Source du contenu :** {spec["source"]}', "",
             "- Voix : **Adam - Instructor** (`TGAegA0zNRi8I6nUdq3i`), `eleven_multilingual_v2`, prise 1 sur 2.",
             f'- Musique : ElevenLabs Music v2.5 (`{spec["music"]}`), instrumentale, sous la voix.',
             "- Audio normalisé à −16 LUFS ; scènes, éléments et sous-titres calés sur la transcription "
             "mot à mot ElevenLabs Scribe.",
             "- Flow ElevenLabs : `XBWW3jSkIoTotuA5WrkJ`. Montage généré par `tools/gen_page_video.py`.", "",
             "## Voix off", "", spec["vo_text"], "", "## Scènes", "", "| Début | Scène | Éléments |", "|---|---|---|"]
    for sc in scenes:
        els = " · ".join(re.sub(r"<[^>]+>", "", it.get("text", "")) for it in sc["items"])
        name = re.sub(r"<[^>]+>", "", sc.get("kicker") or sc.get("note", ""))
        lines.append(f'| {sc["t0"]:.2f} s | {name} | {els} |')
    lines += ["", f'Rendu : `renders/foodeatup-{spec["slug"]}-v1.mp4`.', "",
              "## Publication", "Archivée dans la bibliothèque RapidoCMS. **Aucune publication sur les réseaux "
              "sans validation humaine de la pièce.**", ""]
    return "\n".join(lines)


TEMPLATE = """<!doctype html>
<html lang="fr">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=1080, height=1920" />
    <!--
      {title} — vertical 1080×1920, {total} s.
      {comment}
      Généré par studio-video/tools/gen_page_video.py : chaque scène et chaque
      élément démarrent sur un mot de la voix off (transcription ElevenLabs Scribe).
    -->
    <script src="assets/vendor/gsap.min.js"></script>
    <style>
      @font-face {{
        font-family: "Goodly";
        src: url("assets/vendor/fonts/Fredoka-Variable.woff2") format("woff2-variations");
        font-weight: 300 700;
      }}
      * {{ margin: 0; padding: 0; box-sizing: border-box; }}
      html, body {{ width: 1080px; height: 1920px; overflow: hidden; background: #fcf9e6; }}
      body {{ font-family: "Goodly", sans-serif; color: #0f1a23;
        --ink: #0f1a23; --ink-soft: #55616b; --blue: #007bff; --blue-deep: #0057b8;
        --orange: #ffa500; --orange-text: #c88100; --bg-deep: #f5efcf; }}
      #root {{ position: relative; width: 1080px; height: 1920px; overflow: hidden; background: #fcf9e6; }}
      .halo {{ position: absolute; border-radius: 50%; }}
      #halo-blue {{ width: 900px; height: 900px; left: -320px; top: -260px;
        background: radial-gradient(circle, rgba(0,123,255,.15), transparent 65%); }}
      #halo-orange {{ width: 820px; height: 820px; right: -300px; bottom: -220px;
        background: radial-gradient(circle, rgba(255,165,0,.2), transparent 65%); }}
      #logo-top {{ position: absolute; top: 90px; left: 50%; transform: translateX(-50%); width: 380px; height: auto; }}

      .scene {{ position: absolute; inset: 0; display: flex; flex-direction: column; align-items: center;
        justify-content: flex-start; padding: 290px 80px 0; text-align: center; }}
      .kicker {{ font-size: 78px; font-weight: 700; line-height: 1.06; letter-spacing: -0.5px; margin-bottom: 56px; }}
      .kicker b {{ color: var(--blue); font-weight: 700; }}
      .kicker em {{ font-style: normal; color: #a86a00; }}
      .body {{ width: 100%; display: flex; flex-direction: column; align-items: center; gap: 28px; }}
      .body.center {{ flex: 1; justify-content: center; margin-top: -260px; gap: 44px; }}
      .body.grid2 {{ display: grid; grid-template-columns: 1fr 1fr; gap: 26px; }}
      .body.wrap {{ flex-direction: row; flex-wrap: wrap; justify-content: center; gap: 22px; }}
      .card {{ background: #fff; border: 4px solid var(--ink); border-radius: 36px; box-shadow: 0 11px 0 var(--ink); }}

      .big {{ display: flex; flex-direction: column; align-items: center; gap: 30px; }}
      .big .ico {{ width: 220px; height: 220px; }}
      .big-t {{ font-size: 104px; font-weight: 700; line-height: 1.02; letter-spacing: -1px; }}
      .big .sub-t {{ font-size: 54px; color: var(--ink-soft); font-weight: 600; }}
      .stat-n {{ font-size: 230px; font-weight: 700; line-height: 1; color: var(--blue); }}
      .stat .sub-t {{ font-size: 50px; font-weight: 600; color: var(--ink-soft); display: block; margin-top: 8px; }}
      .pill {{ display: inline-flex; align-items: center; gap: 16px; font-size: 46px; font-weight: 600;
        padding: 18px 36px; border-radius: 999px; background: #fff; border: 4px solid var(--ink); box-shadow: 0 8px 0 var(--ink); }}
      .pill .ico {{ width: 52px; height: 52px; }}
      .row {{ width: 100%; display: flex; align-items: center; gap: 30px; text-align: left; padding: 26px 34px; border-radius: 32px; }}
      .row .ico {{ width: 70px; height: 70px; flex: none; }}
      .row .num {{ flex: none; width: 88px; height: 88px; border-radius: 26px; color: #fff; font-size: 52px; font-weight: 700;
        display: flex; align-items: center; justify-content: center; }}
      .row-t {{ font-size: 48px; font-weight: 700; line-height: 1.1; }}
      .row .sub-t, .tile .sub-t, .price .sub-t {{ display: block; font-size: 32px; font-weight: 500; color: var(--ink-soft); margin-top: 6px; line-height: 1.25; }}
      .tile {{ display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 12px; padding: 30px 22px; min-height: 230px; }}
      .tile .ico {{ width: 76px; height: 76px; }}
      .tnum {{ font-size: 64px; font-weight: 700; line-height: 1; }}
      .tile-t {{ font-size: 42px; font-weight: 700; line-height: 1.1; }}
      .price {{ width: 100%; padding: 32px 40px; text-align: left; }}
      .price.hl {{ border-color: var(--blue); box-shadow: 0 11px 0 var(--blue-deep); }}
      .p-name {{ font-size: 44px; font-weight: 700; }}
      .p-amt {{ font-size: 76px; font-weight: 700; color: var(--blue); line-height: 1.1; margin-top: 4px; }}
      .bubble {{ max-width: 860px; font-size: 44px; font-weight: 600; line-height: 1.25; padding: 28px 36px; border-radius: 40px; text-align: left; }}
      .bubble.me {{ align-self: flex-end; background: var(--blue); color: #fff; border-bottom-right-radius: 10px; }}
      .bubble.bot {{ align-self: flex-start; background: #fff; border: 4px solid var(--ink); border-bottom-left-radius: 10px; }}
      .bubble.wa {{ align-self: flex-start; background: #e7f6ee; border: 4px solid #0e7a4f; border-bottom-left-radius: 10px; }}
      .url {{ white-space: nowrap; display: inline-flex; align-items: center; gap: 16px; font-size: 50px; font-weight: 700; color: #fff; background: var(--blue);
        padding: 26px 46px; border-radius: 999px; box-shadow: 0 12px 0 var(--blue-deep); }}
      .url .ico {{ width: 56px; height: 56px; }}
      .badge {{ display: inline-flex; align-items: center; gap: 16px; font-size: 42px; font-weight: 700; color: #fff;
        padding: 18px 34px; border-radius: 999px; }}
      .badge .ico {{ width: 48px; height: 48px; }}
      .note {{ font-size: 34px; font-weight: 500; color: var(--ink-soft); }}
      .final .body {{ flex: 1; justify-content: center; margin-top: -200px; gap: 50px; }}
      .final .logo-end {{ width: 620px; height: auto; }}
      .final .chef-end {{ width: 220px; height: auto; }}

      #subs {{ position: absolute; left: 0; right: 0; bottom: 120px; height: 100px; }}
      .sub {{ position: absolute; left: 30px; right: 30px; text-align: center; font-size: 60px; font-weight: 700;
        color: #fff; -webkit-text-stroke: 8px #0f1a23; paint-order: stroke fill; letter-spacing: 1px; opacity: 0; white-space: nowrap; }}
    </style>
  </head>
  <body>
    <div id="root" data-composition-id="main" data-start="0" data-duration="{total}" data-width="1080" data-height="1920">
      <audio id="voix" class="clip" src="assets/audio/voix-adam.mp3" data-start="0" data-duration="{vo_dur}" data-track-index="10" data-volume="1"></audio>
      <audio id="musique" class="clip" src="assets/audio/musique.mp3" data-start="0" data-duration="{total}" data-track-index="11"
        data-volume="{music_vol}" data-fade-in="0.6" data-fade-out="2.2"></audio>
      <div id="halo-blue" class="halo clip" data-start="0" data-duration="{total}" data-track-index="0"></div>
      <div id="halo-orange" class="halo clip" data-start="0" data-duration="{total}" data-track-index="0"></div>
      <img id="logo-top" class="clip" data-start="0" data-duration="{logo_end}" data-track-index="1"
        src="assets/brand/foodeatup-logo-horizontal-mascot.png" alt="FoodEatUp" />

{sections}

      <div id="subs" class="clip" data-start="0" data-duration="{total}" data-track-index="5"></div>
    </div>

    <script>
      window.__timelines = window.__timelines || {{}};
      const tl = gsap.timeline({{ paused: true }});

      // Sous-titres : [début, fin, texte] tirés de la transcription mot à mot.
      const SUBS = {subs};
      const subsBox = document.getElementById("subs");
      SUBS.forEach(([t0, t1, text, size]) => {{
        const el = document.createElement("div");
        el.className = "sub";
        el.style.fontSize = size + "px";
        el.textContent = text;
        subsBox.appendChild(el);
        tl.set(el, {{ opacity: 1 }}, t0);
        tl.set(el, {{ opacity: 0 }}, Math.min(t1, {subs_end}));
      }});

      tl.to("#halo-blue", {{ x: 140, y: 120, duration: {total}, ease: "sine.inOut" }}, 0);
      tl.to("#halo-orange", {{ x: -120, y: -160, duration: {total}, ease: "sine.inOut" }}, 0);
      tl.to("#logo-top", {{ opacity: 0, duration: 0.3 }}, Math.max(0, {logo_end} - 0.3));

{js}

      window.__timelines["main"] = tl;
    </script>
  </body>
</html>
"""

if __name__ == "__main__":
    ids = sys.argv[1:] or list(VIDEOS_SPEC)
    for vid in ids:
        build(VIDEOS_SPEC[vid])
