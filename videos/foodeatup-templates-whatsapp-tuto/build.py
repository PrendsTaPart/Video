#!/usr/bin/env python3
# FoodEatUp "Créer ses templates WhatsApp marketing" tutorial (Marketing,
# Fidélité & Iris module). No avatar clip: full ElevenLabs VO throughout
# (Adam Instructor FR). Speed = setpts (never zoompan on real footage). xfade
# on every cut, forced back to yuv420p at the end of the chain. 48kHz stereo
# AAC, +faststart.
#
# Rush: accueil "Campagnes & automatisations" -> clic onglet "Templates
# WhatsApp" -> page vide (bandeau Twilio simulé) -> clic "Nouveau template"
# -> modale : nom Meta "reconquete_clients" + catégorie Marketing + langue fr
# -> corps "Bonjour {{1}}, on vous attend chez {{2}} ! Profitez de {{3}} avec
# le code {{4}}." (4 variables détectées) -> libellés "prenom, restaurant,
# offre, code" -> "Enregistrer" -> toast "Template enregistré" -> carte
# Reconquete_clients (Brouillon, Modifier/Soumettre à Meta/Supprimer). Trois
# points de clic zoom-punch : onglet "Templates WhatsApp", "Nouveau
# template", "Enregistrer". Coordonnées mesurées par seuillage couleur (bleu
# FoodEatUp) sur les frames réelles, pas à l'oeil -- voir SCRIPT.md.
import subprocess, os, sys
sys.path.insert(0, "/home/user/Video/videos/_shared")
from claude_prompt_sequence import (
    render_claude_stage1_png, render_claude_stage2_png, render_claude_stage3_png,
)

ROOT = "/home/user/Video/videos/foodeatup-templates-whatsapp-tuto"
SRC  = f"{ROOT}/assets/screen.mp4"
W, H, FPS = 1920, 828, 25
SEG = f"{ROOT}/work/seg"
ORANGE = "0xF7941D"
XF = 0.28
os.makedirs(SEG, exist_ok=True)

def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        print("ERR:", " ".join(cmd)[:300]); print(r.stderr[-2000:]); raise SystemExit(1)

def dur(path):
    r = subprocess.run(["ffprobe","-v","error","-show_entries","format=duration",
                        "-of","csv=p=0",path], capture_output=True, text=True)
    return float(r.stdout.strip())

def clamp(v, lo, hi): return max(lo, min(hi, v))

ZOOM = 1.20
def crop_for(btn):
    bx, by = btn
    cw, ch = int(W/ZOOM), int(H/ZOOM); cw -= cw % 2; ch -= ch % 2
    x = int(clamp(bx - cw/2, 0, W - cw)); y = int(clamp(by - ch/2, 0, H - ch))
    return f"crop={cw}:{ch}:{x}:{y},scale={W}:{H}:flags=bicubic", (cw, ch, x, y)

def punch_highlight(btn, btn_wh, crop_box):
    cw, ch, cx, cy = crop_box
    sx, sy = W / cw, H / ch
    bw, bh = btn_wh[0] * sx, btn_wh[1] * sy
    ox, oy = (btn[0] - cx) * sx, (btn[1] - cy) * sy
    p = 14
    br = "6*sin(2*PI*t*2.2)"
    return (f"drawbox=x='{ox-bw/2-p}-{br}':y='{oy-bh/2-p}-{br}'"
            f":w='{bw+2*p}+2*({br})':h='{bh+2*p}+2*({br})'"
            f":color={ORANGE}@0.95:t=5")

# Coordonnées mesurées par seuillage couleur (bleu FoodEatUp, PIL/numpy) sur
# les frames réelles du screen recording -- voir SCRIPT.md. Pas de banner() :
# la page/modale portent déjà leurs propres libellés.
BTN_TEMPLATES_TAB    = (1099, 692);  SZ_TEMPLATES_TAB    = (400, 70)  # onglet "Templates WhatsApp"
BTN_NOUVEAU_TEMPLATE = (1671, 773);  SZ_NOUVEAU_TEMPLATE = (310, 72)  # bouton "+ Nouveau template"
BTN_ENREGISTRER      = (1025, 738);  SZ_ENREGISTRER      = (210, 68)  # bouton "Enregistrer"

# (name, src_start, src_end, target_out_duration, button_or_None, btn_size_or_None)
segs = [
    ("A", 0.30,  2.00,  2.20, None,                  None),
    ("B", 2.00,  2.35,  0.90, BTN_TEMPLATES_TAB,      SZ_TEMPLATES_TAB),      # clic onglet "Templates WhatsApp"
    ("C", 2.60,  3.80,  4.50, None,                  None),                  # page vide + bandeau Twilio
    ("D", 3.80,  4.15,  0.90, BTN_NOUVEAU_TEMPLATE,   SZ_NOUVEAU_TEMPLATE),   # clic "Nouveau template"
    ("E", 5.00,  17.50, 9.50, None,                  None),                  # nom Meta + catégorie + langue
    ("F", 18.00, 25.00, 6.00, None,                  None),                  # corps du message + variables détectées
    ("G", 25.30, 31.50, 6.50, None,                  None),                  # libellés des variables
    ("H", 31.80, 32.15, 0.90, BTN_ENREGISTRER,        SZ_ENREGISTRER),       # clic "Enregistrer"
    ("I", 33.00, 37.96, 8.00, None,                  None),                  # toast + carte template sauvegardée
]
INTRO_D, OUTRO_D = 2.60, 6.20

def encode_seg(name, s, e, target, btn, btn_sz):
    out = f"{SEG}/{name}.mp4"
    factor = (e - s) / target
    vf = f"setpts=(PTS-STARTPTS)/{factor:.6f}"
    if btn:
        crop_vf, box = crop_for(btn)
        vf += f",{crop_vf},{punch_highlight(btn, btn_sz, box)}"
    else:
        vf += f",scale={W}:{H}"
    vf += f",fps={FPS},format=yuv420p"
    run(["ffmpeg","-y","-v","error","-ss",str(s),"-to",str(e),"-i",SRC,"-an",
         "-vf",vf,"-r",str(FPS),"-c:v","libx264","-preset","medium","-crf","18",out])
    return out

# ---------------------------------------------------------------------------
# "Use it with Claude" sequence -- shared 3-stage chatbot animation. Matching
# tools: mcp__FoodEatUp__create_whatsapp_template(establishment_id, name,
# body, category, language, variables[]) crée le brouillon, puis
# mcp__FoodEatUp__submit_whatsapp_template(establishment_id, template_id,
# confirm:true) l'envoie à l'approbation Meta -- exactement le flux filmé
# (Enregistrer -> carte "Brouillon" avec bouton "Soumettre à Meta").
# ---------------------------------------------------------------------------
CLAUDE_PROMPT = ("Crée un template WhatsApp nommé [nom_meta] (catégorie "
                  "[MARKETING/UTILITY], langue [fr]) avec le message « [texte "
                  "avec {{1}}, {{2}}...] » et les variables [prenom, offre, ...], "
                  "puis soumets-le à l'approbation Meta pour mon établissement "
                  "FoodEatUp (ID [ID établissement]).")
CLAUDE_RESPONSE = "Bien sûr ! Je crée le template et je le soumets à Meta…"

def card(img, out, secs, zoom_in=True, fade=True):
    """fade=False for the claude stages: they sit mid-video and only meet the
    timeline through xfade -- adding card()'s own fade-to-black on top makes
    short stages read as a murky blur (bug hit on the tva build)."""
    z0, z1 = (1.0, 1.09) if zoom_in else (1.09, 1.0)
    frames = int(secs * FPS)
    zexpr = f"{z0}+({z1}-{z0})*on/{frames}"
    vf = (f"[0:v]scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},"
          f"boxblur=20:2,eq=brightness=-0.06[bg];"
          f"[0:v]scale={W}:{H}:force_original_aspect_ratio=decrease[fg];"
          f"[bg][fg]overlay=(W-w)/2:(H-h)/2,scale={W*2}:{H*2},"
          f"zoompan=z='{zexpr}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)'"
          f":d=1:s={W}x{H}:fps={FPS}")
    if fade:
        vf += f",fade=t=in:st=0:d=0.4,fade=t=out:st={secs-0.4:.3f}:d=0.4"
    vf += ",format=yuv420p"
    run(["ffmpeg","-y","-v","error","-loop","1","-t",str(secs),"-i",img,
         "-filter_complex",vf,"-r",str(FPS),
         "-c:v","libx264","-preset","medium","-crf","18",out])

CLAUDE_STAGE_D = [3.20, 2.60, 6.00]  # reveal, copied, chatbot mockup

def build_silent(outro_d):
    card(f"{ROOT}/assets/intro.jpg", f"{SEG}/intro.mp4", INTRO_D, zoom_in=True)
    card(f"{ROOT}/assets/outro.jpg", f"{SEG}/outro.mp4", outro_d, zoom_in=False)
    c1, c2, c3 = f"{SEG}/claude1.png", f"{SEG}/claude2.png", f"{SEG}/claude3.png"
    if not os.path.exists(c1):
        render_claude_stage1_png(c1, W, H, CLAUDE_PROMPT)
    if not os.path.exists(c2):
        render_claude_stage2_png(c2, W, H, CLAUDE_PROMPT)
    if not os.path.exists(c3):
        render_claude_stage3_png(c3, W, H, CLAUDE_PROMPT, response=CLAUDE_RESPONSE)
    for i, png in enumerate([c1, c2, c3]):
        card(png, f"{SEG}/claude{i+1}.mp4", CLAUDE_STAGE_D[i], zoom_in=True, fade=False)

    parts = [f"{SEG}/intro.mp4"]
    for name, s, e, target, btn, sz in segs:
        parts.append(encode_seg(name, s, e, target, btn, sz))
    parts.append(f"{SEG}/claude1.mp4")
    parts.append(f"{SEG}/claude2.mp4")
    parts.append(f"{SEG}/claude3.mp4")
    parts.append(f"{SEG}/outro.mp4")

    trans = ["fade",       # intro -> A
             "fade",       # A -> B (continuous: clic sur l'onglet visible)
             "slideleft",  # B -> C (cut: page Templates WhatsApp)
             "fade",       # C -> D (continuous: clic Nouveau template)
             "slideleft",  # D -> E (cut: ouverture de la modale)
             "fade",       # E -> F (continuous: nom/catégorie -> message)
             "fade",       # F -> G (continuous: message -> variables)
             "fade",       # G -> H (continuous: clic Enregistrer)
             "slideleft",  # H -> I (cut: toast + carte sauvegardée)
             "slideleft",  # I -> claude1
             "slideleft",  # claude1 -> claude2
             "slideleft",  # claude2 -> claude3
             "fade"]       # claude3 -> outro
    durs = [dur(p) for p in parts]
    starts, acc = [], 0.0
    for i, d in enumerate(durs):
        starts.append(acc); acc += d - (XF if i < len(durs) - 1 else 0)
    total = acc

    inputs, fc, cur = [], [], "[0:v]"
    for p in parts: inputs += ["-i", p]
    for k in range(len(parts) - 1):
        off = starts[k + 1]
        lbl = f"[x{k}]"
        fc.append(f"{cur}[{k+1}:v]xfade=transition={trans[k]}:duration={XF}"
                  f":offset={off:.4f}{lbl}")
        cur = lbl
    fc.append(f"{cur}format=yuv420p[vout]")
    silent = f"{ROOT}/work/video_silent.mp4"
    run(["ffmpeg","-y","-v","error"] + inputs +
        ["-filter_complex", ";".join(fc), "-map", "[vout]",
         "-r",str(FPS),"-c:v","libx264","-profile:v","high","-pix_fmt","yuv420p",
         "-preset","medium","-crf","18", silent])
    return silent, starts, total

silent, starts, total = build_silent(OUTRO_D)
print(f"SILENT TOTAL: {dur(silent):.2f}s")
labels_order = ["intro"] + [s[0] for s in segs] + ["claude1", "claude2", "claude3", "outro"]
S = dict(zip(labels_order, starts))
OUTRO_START = S["outro"]

GAP = 0.22
anchor = {
    "N0":  0.30,                 # intro hook
    "N1":  S["B"] + 0.05,        # clic onglet "Templates WhatsApp"
    "N2":  S["D"] + 0.05,        # clic "Nouveau template"
    "N3":  S["E"] + 0.15,        # nom Meta + catégorie + langue
    "N4":  S["F"] + 0.15,        # corps du message + variables
    "N5":  S["G"] + 0.15,        # libellés des variables
    "N6":  S["H"] + 0.05,        # clic "Enregistrer" -> toast
    "N7":  S["I"] + 0.15,        # carte template (bouton Soumettre à Meta)
    "N8":  S["claude1"] + 0.20,  # explique le prompt (reveal + copié)
    "N9":  S["claude3"] + 0.20,  # colle dans Claude -> résultat
    "N10": OUTRO_START + 0.35,   # CTA
}
keys = [f"N{i}" for i in range(11)]
off, prev_end = {}, -GAP
for k in keys:
    o = max(anchor[k], prev_end + GAP); off[k] = o
    prev_end = o + dur(f"{ROOT}/vo/{k}.mp3")
print("offsets:", {k: round(v, 2) for k, v in off.items()}, "voice_end:", round(prev_end, 2))
drift = {k: round(off[k] - anchor[k], 2) for k in keys if off[k] - anchor[k] > 0.05}
print("drift vs anchors:", drift if drift else "none -- all lines on their anchors")

needed = prev_end - OUTRO_START + 0.80
if needed > OUTRO_D:
    print(f"extending outro {OUTRO_D:.2f} -> {needed:.2f}")
    silent, starts, total = build_silent(needed)
    print(f"SILENT TOTAL (extended): {dur(silent):.2f}s")

total = dur(silent)
inputs, filters, labels = [], [], []
for i, k in enumerate(keys):
    inputs += ["-i", f"{ROOT}/vo/{k}.mp3"]; ms = int(off[k] * 1000)
    filters.append(f"[{i+1}:a]loudnorm=I=-16:TP=-1.5:LRA=11,adelay={ms}|{ms},apad[a{i}]")
    labels.append(f"[a{i}]")
filters.append("".join(labels) + f"amix=inputs={len(keys)}:normalize=0:duration=first[mix]")
filters.append(f"[mix]atrim=0:{total:.3f},alimiter=limit=0.6:level=disabled,"
               f"aresample=48000,aformat=sample_fmts=fltp:channel_layouts=stereo,"
               f"asetpts=N/SR/TB[voa]")
FINAL = f"{ROOT}/out/foodeatup-templates-whatsapp-tuto-v1.mp4"
run(["ffmpeg","-y","-v","error","-i",silent] + inputs +
    ["-filter_complex",";".join(filters),"-map","0:v","-map","[voa]",
     "-c:v","copy","-c:a","aac","-b:a","192k","-ar","48000","-ac","2",
     "-movflags","+faststart","-t",f"{total:.3f}",FINAL])
print(f"DONE: {FINAL}  {dur(FINAL):.2f}s")
