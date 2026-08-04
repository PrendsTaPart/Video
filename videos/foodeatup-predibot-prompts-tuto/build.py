#!/usr/bin/env python3
# FoodEatUp "Parler a PrediBot avec nos prompts" tutorial (module predibot, 3/3).
# Unlike the other -tuto videos, the rush is a WhatsApp chat scroll with the
# StockVisionAI agent ("PredBot") -- no UI clicks to zoom-punch on, just
# screen segments cut/reordered to match the VO. Full ElevenLabs VO
# throughout (native audio in the rush is app/keyboard noise, not narration).
# Speed = setpts (never zoompan on real footage). xfade on every cut, forced
# back to yuv420p at the end of the chain. 48kHz stereo AAC, +faststart.
#
# Rush: "Liste mes stocks" -> stock list w/ CRITIQUE alerts -> "Liste mes
# recettes" -> recipe list -> "verifie le fournisseur louay" -> supplier
# card -> "Cree une commande fournisseur" -> agent asks for fields -> user
# fills them in -> order confirmed (ref CMD-...) -> cut to the real
# FoodEatUp app (Gestion des Livraisons) as proof it's not simulated ->
# "Genere le dashboard stock" -> Dashboard Stock FoodEatUp (KPIs + table).
# Matches mcp__Foodeatup__create_supplier_order exactly (order-creation step).
import subprocess, os, sys
sys.path.insert(0, "/home/user/Video/videos/_shared")
from claude_prompt_sequence import (
    render_claude_stage1_png, render_claude_stage2_png, render_claude_stage3_png,
)

ROOT = "/home/user/Video/videos/foodeatup-predibot-prompts-tuto"
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

def banner(text, seg_dur):
    # Static position (this ffmpeg 6.1.1 build evaluates drawbox x/y/w/h once
    # at t=0 -- a t-based slide expression renders frozen off-screen for the
    # whole clip, see FOODEATUP-TUTORIELS-WORKFLOW.md). No apostrophe in any
    # text below (same bug class as the `%`/apostrophe drawtext trap).
    if not text: return None
    x, y = 40, H - 108
    return (f"drawbox=x={x}:y={y}:w=10:h=62:color={ORANGE}@0.98:t=fill,"
            f"drawbox=x={x+10}:y={y}:w=620:h=62:color={BLUE}@0.90:t=fill,"
            f"drawtext=fontfile={FONT}:text='{text}':fontsize=31:fontcolor=white"
            f":x={x+34}:y={y+16}")

# Source timestamps measured on the actual frames (ffmpeg -ss t -frames:v 1
# sampled at 1-2s steps), not eyeballed. Reordered vs raw rush: the source
# shows the app cut-in (Gestion des Livraisons) BEFORE the order fields are
# typed; here the order is: ask -> fields+confirmation -> proof in the real
# app, which reads better as a demo. 0-4.5s (leftover unrelated HR/staff
# scroll before the rush's first message) is cut.
# (name, src_start, src_end, target_out_duration, caption)
segs = [
    ("A",  4.50, 14.00, 13.50, "Liste mes stocks"),
    ("B", 14.00, 21.00,  6.00, "Liste mes recettes"),
    ("C", 21.00, 27.00,  6.00, "Verifiez un fournisseur"),
    ("D", 27.00, 31.00,  4.00, "Creez une commande fournisseur"),
    ("F", 36.50, 40.00,  5.00, "Commande confirmee"),
    ("E", 31.00, 36.50,  4.50, "Suivi cote application FoodEatUp"),
    ("G", 48.00, 62.00, 10.00, "Dashboard stock genere"),
]
INTRO_D, OUTRO_D = 2.60, 6.20

def encode_seg(name, s, e, target, caption):
    out = f"{SEG}/{name}.mp4"
    factor = (e - s) / target
    vf = f"setpts=(PTS-STARTPTS)/{factor:.6f},scale={W}:{H}"
    b = banner(caption, target)
    if b: vf += f",{b}"
    vf += f",fps={FPS},format=yuv420p"
    run(["ffmpeg","-y","-v","error","-ss",str(s),"-to",str(e),"-i",SRC,"-an",
         "-vf",vf,"-r",str(FPS),"-c:v","libx264","-preset","medium","-crf","18",out])
    return out

# ---------------------------------------------------------------------------
# "Use it with Claude" sequence -- shared 3-stage chatbot animation.
# mcp__Foodeatup__create_supplier_order matches exactly the order-creation
# step shown in the rush (fournisseur + produit + quantite + date).
# ---------------------------------------------------------------------------
CLAUDE_PROMPT = ("Crée une commande fournisseur pour mon établissement FoodEatUp "
                  "(ID [ID établissement]) auprès du fournisseur [ID fournisseur] : "
                  "[quantité] [unité] de [ingrédient], livraison prévue le [date prévue].")
CLAUDE_RESPONSE = "C'est fait ! Votre commande fournisseur a été créée…"

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

CLAUDE_STAGE_D = [2.20, 1.30, 2.50]

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
    for name, s, e, target, cap in segs:
        parts.append(encode_seg(name, s, e, target, cap))
    parts.append(f"{SEG}/claude1.mp4")
    parts.append(f"{SEG}/claude2.mp4")
    parts.append(f"{SEG}/claude3.mp4")
    parts.append(f"{SEG}/outro.mp4")

    trans = ["fade",       # intro -> A
             "fade",       # A -> B (continuous: another question typed)
             "fade",       # B -> C
             "fade",       # C -> D
             "slideleft",  # D -> F (cut: fields filled elsewhere in the chat)
             "slideleft",  # F -> E (cut: switch to the real app)
             "slideleft",  # E -> G (cut: back to chat -> dashboard)
             "slideleft",  # G -> claude1
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
    "N1": S["A"] + 0.20,         # "Liste mes stocks" reveal
    "N2": S["B"] + 0.20,         # "Liste mes recettes"
    "N3": S["C"] + 0.20,         # "verifie le fournisseur"
    "N4": S["D"] + 0.10,         # order form -> fields -> confirmation
    "N5": S["G"] + 0.20,         # dashboard reveal (benefit)
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
FINAL = f"{ROOT}/out/foodeatup-predibot-prompts-tuto-v1.mp4"
run(["ffmpeg","-y","-v","error","-i",silent] + inputs +
    ["-filter_complex",";".join(filters),"-map","0:v","-map","[voa]",
     "-c:v","copy","-c:a","aac","-b:a","192k","-ar","48000","-ac","2",
     "-movflags","+faststart","-t",f"{total:.3f}",FINAL])
print(f"DONE: {FINAL}  {dur(FINAL):.2f}s")
