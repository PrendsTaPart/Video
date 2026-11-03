#!/usr/bin/env python3
# FoodEatUp "Traçabilité complète — synchroniser avec vos produits" tutorial.
# Same pipeline as foodeatup-tva-tuto / foodeatup-fournisseurs-tuto: no avatar
# clip, full ElevenLabs VO throughout, speed via setpts (never zoompan on real
# footage), xfade on every cut, forced back to yuv420p at the end of the
# chain, 48kHz stereo AAC. Click coordinates measured by colour-thresholding
# the actual extracted frames (see scratchpad), not eyeballed.
import subprocess, os, sys
sys.path.insert(0, "/home/user/Video/videos/_shared")
from claude_prompt_sequence import (
    render_claude_stage1_png, render_claude_stage2_png, render_claude_stage3_png,
)

ROOT = "/home/user/Video/videos/foodeatup-tracabilite-complete-tuto"
SRC  = f"{ROOT}/assets/screen.mp4"
W, H, FPS = 1920, 828, 25
SEG = f"{ROOT}/work/seg"
FONT = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
BLUE, ORANGE = "0x1B6DF3", "0xF7941D"
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

def banner(text, seg_dur):
    if not text: return None
    tin, sl = 0.15, 0.32
    tout = max(tin + sl + 0.3, seg_dur - 0.55)
    a = f"min(1\\,max(0\\,(t-{tin})/{sl}))"
    b = f"min(1\\,max(0\\,(t-{tout})/{sl}))"
    x = f"-640+700*({a})-700*({b})"
    y = H - 108
    return (f"drawbox=x='{x}':y={y}:w=10:h=62:color={ORANGE}@0.98:t=fill,"
            f"drawbox=x='({x})+10':y={y}:w=560:h=62:color={BLUE}@0.90:t=fill,"
            f"drawtext=fontfile={FONT}:text='{text}':fontsize=31:fontcolor=white"
            f":x='({x})+34':y={y+16}")

# Coordinates measured by colour-thresholding the actual frames (orange
# 0xF7941D, blue 0x0C7EF8, red badge ~0xCE2347). NOTE: the page is auto-
# scrolled a few px between t=0 and t=4, so the card arrow's on-screen
# position at click time (~4.75s) is (1702,384), not where it sits at t=0
# (a first pass wrongly reused a stale y-coordinate and punched blank space
# -- verified by sampling frames every 0.3s from 4.0 to 4.9s and re-running
# the colour search with a wider vertical box each time).
BTN_CARD_ARROW   = (1702, 384); SZ_CARD_ARROW   = (56, 56)   # "Traçabilité complète" card arrow
BTN_ADD_PRODUCT  = (1703, 650); SZ_ADD_PRODUCT  = (40, 40)   # "+" on Abricot row
BTN_VALIDER_SEL  = (1735, 193); SZ_VALIDER_SEL  = (110, 46)  # "Valider" (product selection)
BTN_NON_COMPLETE = (1552, 496); SZ_NON_COMPLETE = (170, 54)  # "non complété" badge
BTN_VALIDER_TRAC = (1032, 694); SZ_VALIDER_TRAC = (200, 55)  # "Valider la traçabilité"
BTN_ENREGISTRER  = (1673, 606); SZ_ENREGISTRER  = (140, 50)  # "Enregistrer"
BTN_DATE_VALIDER = (1273, 577); SZ_DATE_VALIDER = (150, 66)  # "Valider" (date modal)

# Click timings below were re-verified a second time (sampling every 0.2-
# 0.3s around each transition, colour-thresholding the real button pixels --
# see scratchpad/frames3..8): several were off by seconds in the first pass
# (which trusted a coarse 2s-step scan), most notably "+" Abricot (really
# ~8.15s, not 9.9s), "non complété" (really ~12.8s, not 15.9s) and "Valider
# la traçabilité" (really ~34.3s, not 38.2s). The 46-52s window (a stray
# trip to the Accueil dashboard, not part of the traçabilité flow) is cut.
# (name, src_start, src_end, target_out_duration, click_time_or_None, button, btn_size, caption)
segs = [
    ("A", 0.20,  4.60,  2.30, None, None,             None,               "1 · Traçabilité"),
    ("B", 4.65,  4.90,  0.90, 4.75, BTN_CARD_ARROW,    SZ_CARD_ARROW,      None),
    ("C", 4.95,  8.00,  4.40, None, None,             None,               "2 · Ajoutez vos produits"),
    ("D", 8.05,  8.30,  0.90, 8.15, BTN_ADD_PRODUCT,   SZ_ADD_PRODUCT,     None),
    ("E", 8.35, 11.10,  2.40, None, None,             None,               None),
    ("F", 11.15, 11.35, 0.85, 11.20, BTN_VALIDER_SEL,  SZ_VALIDER_SEL,     None),
    ("G", 11.40, 12.65, 2.60, None, None,             None,               "3 · Fiche produit"),
    ("H", 12.70, 12.90, 0.85, 12.80, BTN_NON_COMPLETE, SZ_NON_COMPLETE,    None),
    ("I", 12.95, 22.00, 5.40, None, None,             None,               "4 · Photo de la DLC"),
    ("J", 22.10, 34.15, 6.10, None, None,             None,               "5 · Quantité, DLC, lot"),
    ("K", 34.20, 34.45, 0.90, 34.30, BTN_VALIDER_TRAC, SZ_VALIDER_TRAC,    None),
    ("L", 34.50, 39.50, 1.80, None, None,             None,               None),
    ("M", 39.55, 40.95, 1.80, None, None,             None,               "6 · Statut Complété"),
    ("N", 41.00, 41.20, 0.85, 41.10, BTN_ENREGISTRER,  SZ_ENREGISTRER,     None),
    ("O", 41.25, 43.45, 1.40, None, None,             None,               None),
    ("P", 43.50, 43.75, 0.85, 43.60, BTN_DATE_VALIDER, SZ_DATE_VALIDER,    None),
    ("Q", 52.00, 55.68, 1.80, None, None,             None,               "Terminé !"),
]
INTRO_D, OUTRO_D = 4.60, 6.20

def encode_seg(name, s, e, target, btn, btn_sz, caption):
    out = f"{SEG}/{name}.mp4"
    factor = (e - s) / target
    vf = f"setpts=(PTS-STARTPTS)/{factor:.6f}"
    if btn:
        crop_vf, box = crop_for(btn)
        vf += f",{crop_vf},{punch_highlight(btn, btn_sz, box)}"
    else:
        vf += f",scale={W}:{H}"
    b = banner(caption, target)
    if b: vf += f",{b}"
    vf += f",fps={FPS},format=yuv420p"
    run(["ffmpeg","-y","-v","error","-ss",str(s),"-to",str(e),"-i",SRC,"-an",
         "-vf",vf,"-r",str(FPS),"-c:v","libx264","-preset","medium","-crf","18",out])
    return out

# ---------------------------------------------------------------------------
# "Use it with Claude" sequence -- shared 3-stage chatbot animation
# (videos/_shared/claude_prompt_sequence.py). mcp__FoodEatUp__
# create_haccp_tracabilite(establishment_id, type="complete",
# reference_type="product", quantite, dlc, lot, remarques) is the matching
# tool -- fields checked against the tool schema before writing the prompt
# below, they line up with what the rush actually shows on screen (photo
# DLC, quantité, DLC, numéro de lot, remarques).
# ---------------------------------------------------------------------------
CLAUDE_PROMPT = ("Crée une fiche de traçabilité complète pour [nom du produit] : "
                  "lot [numéro de lot], DLC [jj/mm/aaaa], quantité [quantité], "
                  "dans mon établissement FoodEatUp (ID [ID établissement]).")
CLAUDE_RESPONSE = "Bien sûr ! J'enregistre cette fiche de traçabilité pour votre établissement…"

def card(img, out, secs, zoom_in=True, fade=True):
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

CLAUDE_STAGE_D = [3.00, 2.30, 5.30]  # reveal, copied, chatbot mockup

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
    for name, s, e, target, ck, btn, sz, cap in segs:
        parts.append(encode_seg(name, s, e, target, btn, sz, cap))
    parts.append(f"{SEG}/claude1.mp4")
    parts.append(f"{SEG}/claude2.mp4")
    parts.append(f"{SEG}/claude3.mp4")
    parts.append(f"{SEG}/outro.mp4")

    trans = ["fade",       # intro -> A
             "fade",       # A -> B (continuous: click on the visible card)
             "slideleft",  # B -> C (cut: empty state -> product list)
             "fade",       # C -> D (continuous: click + on Abricot)
             "fade",       # D -> E (continuous: row now checked)
             "fade",       # E -> F (continuous: click Valider)
             "slideleft",  # F -> G (cut: back to Traçabilité complète)
             "fade",       # G -> H (continuous: click non complété)
             "slideleft",  # H -> I (cut: modal opens, photo DLC)
             "slideleft",  # I -> J (cut: quantité/DLC/lot fields)
             "fade",       # J -> K (continuous: click Valider la traçabilité)
             "fade",       # K -> L (validating spinner)
             "slideleft",  # L -> M (cut: statut Complété)
             "fade",       # M -> N (continuous: click Enregistrer)
             "slideleft",  # N -> O (cut: modal date/heure)
             "fade",       # O -> P (continuous: click Valider)
             "slideleft",  # P -> Q (cut: retour liste, Complété)
             "slideleft",  # Q -> claude1
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
    "N0": 0.30,                  # intro hook
    "N1": S["B"] + 0.10,         # "ouvrez la Traçabilité complète" on the click
    "N2": S["D"] + 0.10,         # "ajoutez vos produits en un clic"
    "N3": S["I"] + 0.20,         # "photo de la DLC"
    "N4": S["J"] + 0.20,         # "quantité, date, numéro de lot"
    "N5": S["K"] + 0.10,         # "validez" -> statut Complété
    "N6": S["claude1"] + 0.20,   # explains the prompt (reveal + copied)
    "N7": S["claude3"] + 0.20,   # paste into Claude -> instant result
    "N8": OUTRO_START + 0.35,    # CTA
}
keys = [f"N{i}" for i in range(9)]
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
FINAL = f"{ROOT}/out/foodeatup-tracabilite-complete-tuto-v1.mp4"
run(["ffmpeg","-y","-v","error","-i",silent] + inputs +
    ["-filter_complex",";".join(filters),"-map","0:v","-map","[voa]",
     "-c:v","copy","-c:a","aac","-b:a","192k","-ar","48000","-ac","2",
     "-movflags","+faststart","-t",f"{total:.3f}",FINAL])
print(f"DONE: {FINAL}  {dur(FINAL):.2f}s")
