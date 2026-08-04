#!/usr/bin/env python3
# FoodEatUp "Saisir un mouvement de stock" tutorial.
# Same engine as the rest of the series: no avatar clip, full ElevenLabs VO,
# speed = setpts (never zoompan on real footage), xfade on every cut, forced
# back to yuv420p at the end of the chain. 48kHz stereo AAC, +faststart.
#
# This rush is the first of the series to cover TWO actions in one video:
# creating a stock movement (entrée, 3000 pièces de chocolat, motif "Réception
# commande", fournisseur Carrefour) AND correcting it afterwards through the
# row's Action menu (3000 -> 5000). Hence 12 VO lines instead of the usual 9,
# and 6 zoom-punches instead of 2.
import subprocess, os, sys
sys.path.insert(0, "/home/user/Video/videos/_shared")
from claude_prompt_sequence import (
    render_claude_stage1_png, render_claude_stage2_png, render_claude_stage3_png,
)

ROOT = "/home/user/Video/videos/foodeatup-mouvement-stock-tuto"
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

# Step banner -- built out of two drawtext layers, NOT drawbox+drawtext like
# the earlier videos of the series.
#
# Why: in this ffmpeg (6.1.1) `drawbox` does not evaluate `t` in its x/y/w/h
# expressions. A drawbox whose x depends on t is silently dropped -- no error,
# no box. `drawtext` does evaluate t per frame. So the old banner() rendered
# only its white text sliding over the screenshot: the orange filet and the
# blue plate behind it were never drawn at all. Verified on the delivered
# foodeatup-produits-tuto MP4 too -- same missing plate, which leaves white
# text on a near-white UI screenshot, barely legible.
# (`overlay` was tried first and is a dead end here: its x expression behaves
# the same way as drawbox's, and it also needs the image input looped.)
#
# The plate is drawtext's own `box`: boxborderw=16 around a 31px line gives
# exactly the 62px-high plate the workflow doc specifies. The orange filet is
# the same plate drawn once more 10px to the left in orange, so the blue one
# covers all of it but its leftmost 10px. Both layers share the same animated
# x, so filet + plate + label slide as one piece.
BANNER_Y = H - 108

def banner(text, seg_dur):
    if not text: return None
    tin, sl = 0.15, 0.32
    tout = max(tin + sl + 0.3, seg_dur - 0.55)
    a = f"min(1\\,max(0\\,(t-{tin})/{sl}))"
    b = f"min(1\\,max(0\\,(t-{tout})/{sl}))"
    x = f"-640+700*({a})-700*({b})"
    label = f" {text} "
    return (f"drawtext=fontfile={FONT}:text='{label}':fontsize=31:fontcolor=white"
            f":box=1:boxcolor={ORANGE}@0.98:boxborderw=16:x='({x})-10':y={BANNER_Y},"
            f"drawtext=fontfile={FONT}:text='{label}':fontsize=31:fontcolor=white"
            f":box=1:boxcolor={BLUE}@0.92:boxborderw=16:x='({x})':y={BANNER_Y}")

# Coordinates measured by colour-thresholding the actual frames (work/frames/),
# not eyeballed. The page scrolls by ~158px once the movements table is
# populated, so "Ajouter un mouvement" has two different y values.
# No apostrophe in any caption below (bug hit on foodeatup-ingredients-tuto --
# see FOODEATUP-TUTORIELS-WORKFLOW.md).
BTN_MVT    = (1380, 355); SZ_MVT    = (298, 56)   # "Mouvement de stock" (pilule orange)
BTN_ADD    = (1638, 344); SZ_ADD    = (316, 64)   # "+ Ajouter un mouvement" (page vide)
BTN_SUBMIT = (1211, 734); SZ_SUBMIT = (125, 65)   # "Ajouter" (submit du modal)
BTN_DOTS   = (1708, 400); SZ_DOTS   = (44, 48)    # menu Action (trois points)
BTN_EDIT   = (1545, 493); SZ_EDIT   = (260, 46)   # "Modifier" dans le menu

# (name, src_start, src_end, target_out_duration, button, btn_size, caption)
# Targets are derived from the VO durations, not the other way round: the
# sequential voice timeline (GAP 0.22) was laid out first, then each segment
# sized so the line that comments it starts on it and ends before the next cut.
# M runs slower than real time (3.95s of source over 5.90s) so the benefit
# line N8 finishes before the Claude sequence -- the content there is a static
# success toast over a settled table, so the slowdown is invisible.
segs = [
    ("A", 0.30,  4.20,  2.78, None,       None,       "1 · Gestion des stocks"),
    ("B", 4.20,  4.55,  1.00, BTN_MVT,    SZ_MVT,     None),
    ("C", 4.70,  8.00,  2.96, None,       None,       "2 · Mouvements de stock"),
    ("D", 8.00,  8.35,  1.00, BTN_ADD,    SZ_ADD,     None),
    ("E", 8.60,  16.50, 4.26, None,       None,       "3 · Produit, type et quantité"),
    ("F", 16.50, 24.00, 4.18, None,       None,       "4 · Unité, motif, fournisseur"),
    ("G", 24.00, 24.35, 1.00, BTN_SUBMIT, SZ_SUBMIT,  None),
    ("H", 24.60, 30.55, 4.21, None,       None,       "Mouvement enregistré"),
    ("I", 30.55, 31.00, 1.08, BTN_DOTS,   SZ_DOTS,    None),
    ("J", 31.05, 31.70, 1.13, BTN_EDIT,   SZ_EDIT,    None),
    ("K", 31.90, 41.55, 5.38, None,       None,       "5 · Corrigez la quantité"),
    ("L", 41.55, 41.95, 1.00, BTN_SUBMIT, SZ_SUBMIT,  None),
    ("M", 42.10, 46.05, 5.90, None,       None,       "Mouvement mis à jour"),
]
INTRO_D, OUTRO_D = 3.68, 6.20

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
# (videos/_shared/claude_prompt_sequence.py). mcp__FoodEatUp__adjust_stock
# (establishment_id, quantity, mode set|increment, motif,
# establishment_product_id | ingredient_id) is the matching tool -- schema
# checked. The video shows the "entrée" case, so the prompt is the increment
# one; the "set / inventaire" variant lives in claudePrompts[] on Lovable.
# ---------------------------------------------------------------------------
CLAUDE_PROMPT = ("Ajoute [quantité] [unité] de [produit] à mon stock, "
                 "motif [motif], pour mon établissement FoodEatUp "
                 "(ID [ID établissement]).")
CLAUDE_RESPONSE = "Bien sûr ! Je saisis ce mouvement de stock…"

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

# N9 (4.41s) has to span stages 1+2 and N10 (4.86s) has to fit inside stage 3
# alone -- hence stage 3 much longer than the shared default [2.20,1.30,2.50].
CLAUDE_STAGE_D = [3.24, 1.95, 5.64]  # reveal, copied, chatbot mockup

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
    for name, s, e, target, btn, sz, cap in segs:
        parts.append(encode_seg(name, s, e, target, btn, sz, cap))
    parts += [f"{SEG}/claude1.mp4", f"{SEG}/claude2.mp4", f"{SEG}/claude3.mp4",
              f"{SEG}/outro.mp4"]

    trans = ["fade",       # intro -> A
             "fade",       # A -> B (continuous: click on the visible page)
             "slideleft",  # B -> C (cut into the movements page)
             "fade",       # C -> D (continuous: click Ajouter un mouvement)
             "slideleft",  # D -> E (cut into the opened form)
             "slideleft",  # E -> F (cut, produit/type/quantité -> unité/motif/fournisseur)
             "fade",       # F -> G (continuous: click Ajouter)
             "fade",       # G -> H (submit -> succès/historique)
             "fade",       # H -> I (continuous: click on the Action menu)
             "fade",       # I -> J (menu open -> click Modifier)
             "slideleft",  # J -> K (cut into the prefilled form)
             "fade",       # K -> L (continuous: click Ajouter)
             "fade",       # L -> M (submit -> succès/liste à jour)
             "slideleft",  # M -> claude1
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
    "N0":  0.30,                  # intro hook
    "N1":  S["A"] + 0.25,         # "cliquez sur Mouvement de stock" -> punch B
    "N2":  S["C"] + 0.15,         # "puis sur Ajouter un mouvement" -> punch D
    "N3":  S["E"] + 0.20,         # produit / type / quantité
    "N4":  S["F"] + 0.20,         # unité / motif / fournisseur -> clic Ajouter
    "N5":  S["H"] + 0.25,         # mouvement enregistré, historique
    "N6":  S["I"] + 0.05,         # menu Action -> Modifier
    "N7":  S["K"] + 2.10,         # corrigez la quantité, validez
    "N8":  S["M"] + 0.20,         # bénéfice (StockVision AI, inventaire juste)
    "N9":  S["claude1"] + 0.20,   # explains the prompt (reveal + copied)
    "N10": S["claude3"] + 0.20,   # paste into Claude -> instant result
    "N11": OUTRO_START + 0.35,    # CTA
}
keys = [f"N{i}" for i in range(12)]
off, prev_end = {}, -GAP
for k in keys:
    o = max(anchor[k], prev_end + GAP); off[k] = o
    prev_end = o + dur(f"{ROOT}/vo/{k}.mp3")
print("offsets:", {k: round(v, 2) for k, v in off.items()}, "voice_end:", round(prev_end, 2))
drift = {k: round(off[k] - anchor[k], 2) for k in keys if off[k] - anchor[k] > 0.05}
print("drift vs anchors:", drift if drift else "none -- all lines on their anchors")
print("stage starts:", {k: round(v, 2) for k, v in S.items()})

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
FINAL = f"{ROOT}/out/foodeatup-mouvement-stock-tuto-v1.mp4"
run(["ffmpeg","-y","-v","error","-i",silent] + inputs +
    ["-filter_complex",";".join(filters),"-map","0:v","-map","[voa]",
     "-c:v","copy","-c:a","aac","-b:a","192k","-ar","48000","-ac","2",
     "-movflags","+faststart","-t",f"{total:.3f}",FINAL])
print(f"DONE: {FINAL}  {dur(FINAL):.2f}s")
