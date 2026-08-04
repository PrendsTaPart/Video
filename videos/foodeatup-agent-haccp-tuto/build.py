#!/usr/bin/env python3
# FoodEatUp "Agent HACCP" tutorial -- relever une temperature d'equipement
# depuis WhatsApp (agent conversationnel Predibot / StockVisionAI), avec
# preuve de synchronisation instantanee dans le module HACCP du site.
#
# Shared "use it with Claude" 3-stage sequence: add_temperature(establishment_id,
# equipment_id, temperature, measured_at) -- meme outil, meme texte de prompt
# que foodeatup-temperature-tuto (meme action, juste un autre canal de saisie).
#
# Same engine as the rest of the series: setpts for speed (never zoompan on
# real footage -- freezes the image), xfade on every cut forced back to
# yuv420p, 48kHz stereo AAC, +faststart. Rush specific: no discrete button
# clicks here (WhatsApp thread + a live page refresh), so no zoom-punch --
# banners alone carry the step-by-step narration.
import subprocess, os, sys
sys.path.insert(0, "/home/user/Video/videos/_shared")
from claude_prompt_sequence import (
    render_claude_stage1_png, render_claude_stage2_png, render_claude_stage3_png,
)

ROOT = "/home/user/Video/videos/foodeatup-agent-haccp-tuto"
SRC  = f"{ROOT}/assets/screen.mp4"
W, H, FPS = 1526, 1032, 25   # native rush resolution, no crop needed
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

BANNER_W, BANNER_H = 610, 62

def banner_png(text, path):
    """Step banner rendered once to an RGBA PNG (drawbox's x/y is evaluated
    once at init on this ffmpeg build, not per-frame -- see
    FOODEATUP-TUTORIELS-WORKFLOW.md). Slid in with overlay instead."""
    from PIL import Image, ImageDraw, ImageFont
    img = Image.new("RGBA", (BANNER_W, BANNER_H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, 9, BANNER_H - 1], fill=(247, 148, 29, 250))
    d.rectangle([10, 0, BANNER_W - 1, BANNER_H - 1], fill=(27, 109, 243, 230))
    f = ImageFont.truetype(FONT, 29)
    d.text((34, BANNER_H // 2), text, font=f, fill=(255, 255, 255, 255), anchor="lm")
    img.save(path)
    return path

def banner_overlay(seg_dur):
    tin, sl = 0.15, 0.32
    tout = max(tin + sl + 0.3, seg_dur - 0.55)
    a = f"min(1\\,max(0\\,(t-{tin})/{sl}))"
    b = f"min(1\\,max(0\\,(t-{tout})/{sl}))"
    return f"-640+700*({a})-700*({b})", H - 108

# (name, src_start, src_end, target_out_duration, caption)
segs = [
    ("A1", 0.00, 1.60, 3.60, "1 - Ecrivez votre demande sur WhatsApp"),
    ("A2", 1.60, 4.00, 5.20, "2 - L'agent demande les infos"),
    ("A3", 4.00, 6.50, 4.30, "3 - Vous repondez en une ligne"),
    ("A4", 6.50, 8.30, 3.60, "4 - Confirmation instantanee"),
    ("B",  8.50, 11.00, 4.00, "Avant : 10,0 degres C"),
    ("C",  12.60, 15.28, 4.20, "Apres : 20,0 degres C, a jour"),
]
INTRO_D, OUTRO_D = 4.60, 6.20

def encode_seg(name, s, e, target, caption):
    out = f"{SEG}/{name}.mp4"
    factor = (e - s) / target
    vf = f"setpts=(PTS-STARTPTS)/{factor:.6f},scale={W}:{H}"
    cmd = ["ffmpeg","-y","-v","error","-ss",str(s),"-to",str(e),"-i",SRC,"-an"]
    if caption:
        png = banner_png(caption, f"{SEG}/banner_{name}.png")
        bx, by = banner_overlay(target)
        cmd += ["-loop","1","-framerate",str(FPS),"-i", png,
                "-filter_complex",
                f"[0:v]{vf},fps={FPS}[base];"
                f"[base][1:v]overlay=x='{bx}':y={by}:shortest=1,format=yuv420p[v]",
                "-map","[v]"]
    else:
        cmd += ["-vf", vf + f",fps={FPS},format=yuv420p"]
    cmd += ["-r",str(FPS),"-c:v","libx264","-preset","medium","-crf","18",out]
    run(cmd)
    return out

# ---------------------------------------------------------------------------
# "Use it with Claude" sequence -- shared 3-stage chatbot animation. Matching
# tool: add_temperature(establishment_id, equipment_id, temperature,
# measured_at) -- meme prompt que foodeatup-temperature-tuto (meme action).
# ---------------------------------------------------------------------------
CLAUDE_PROMPT = ("Enregistre une température de [température] degrés pour "
                 "l'équipement [ID ou nom de l'équipement] dans mon établissement "
                 "FoodEatUp (ID [ID établissement]).")
CLAUDE_RESPONSE = "Bien sûr ! J'enregistre votre relevé de température…"

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

CLAUDE_STAGE_D = [3.00, 1.70, 5.00]

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

    trans = ["fade",       # intro -> A1
             "fade",       # A1 -> A2 (continuous WhatsApp thread)
             "fade",       # A2 -> A3
             "fade",       # A3 -> A4
             "slideleft",  # A4 -> B (cut: WhatsApp -> browser)
             "slideleft",  # B -> C (cut: avant -> apres, la preuve)
             "slideleft",  # C -> claude1
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
    "N0": 0.35,                  # hook, over the intro card (spills onto A1)
    "N1": S["A1"] + 0.20,        # "je veux modifier une temperature"
    "N2": S["A2"] + 0.20,        # bot asks equipment / temperature / notes
    "N3": S["A3"] + 0.20,        # user replies with the 3 values
    "N4": S["A4"] + 0.20,        # bot confirms
    "N5": S["B"] + 0.20,         # avant (10C) -> apres (20C) preuve live
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
    S = dict(zip(labels_order, starts))
    OUTRO_START = S["outro"]

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
FINAL = f"{ROOT}/out/foodeatup-agent-haccp-tuto-v1.mp4"
run(["ffmpeg","-y","-v","error","-i",silent] + inputs +
    ["-filter_complex",";".join(filters),"-map","0:v","-map","[voa]",
     "-c:v","copy","-c:a","aac","-b:a","192k","-ar","48000","-ac","2",
     "-movflags","+faststart","-t",f"{total:.3f}",FINAL])
print(f"DONE: {FINAL}  {dur(FINAL):.2f}s")
