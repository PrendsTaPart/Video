#!/usr/bin/env python3
# FoodEatUp "Relever une température d'équipement" tutorial (HACCP).
#
# Shared "use it with Claude" 3-stage sequence: add_temperature(establishment_id,
# equipment_id, temperature, measured_at) matches exactly what the rush shows --
# pick an equipment, set the measured value, save it into the HACCP log.
#
# Same engine as the rest of the series: setpts for speed (never zoompan on real
# footage -- freezes the image), fixed crop+scale zoom-punch on clicks, xfade on
# every cut forced back to yuv420p, 48kHz stereo AAC, +faststart.
#
# Rush specific: this screen recording is 1920x1020 and still carries the browser
# chrome (tab strip + URL bar + bookmarks bar). Content starts at y=191 exactly,
# so a flat crop=1920:828:0:192 lands on the series' native 1920x828 canvas with
# no scaling and no lost UI -- measured, not guessed (see SCRIPT.md).
import subprocess, os, sys
sys.path.insert(0, "/home/user/Video/videos/_shared")
from claude_prompt_sequence import (
    render_claude_stage1_png, render_claude_stage2_png, render_claude_stage3_png,
)

ROOT = "/home/user/Video/videos/foodeatup-temperature-tuto"
SRC  = f"{ROOT}/assets/screen.mp4"
W, H, FPS = 1920, 828, 25
CHROME_CROP = f"crop={W}:{H}:0:192"   # strips the browser chrome, keeps 1:1 pixels
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

BANNER_W, BANNER_H = 610, 62   # 10px orange rule + 600px blue panel

def banner_png(text, path):
    """The step banner, drawn once into an RGBA PNG instead of with drawbox.

    ffmpeg 6.1.1 evaluates drawbox's x/y/w/h expressions ONCE, at init (t=0),
    while drawtext re-evaluates them every frame. With the slide-in expression
    below, t=0 puts the box at x=-640 -- fully off-canvas -- so the panel never
    appeared and only the white text rendered, floating on the page background.
    overlay does re-evaluate x per frame (eval=frame is its default), so the
    banner is baked into a PNG here and slid in with overlay instead. Same look
    as the rest of the series, animation included.
    """
    from PIL import Image, ImageDraw, ImageFont
    img = Image.new("RGBA", (BANNER_W, BANNER_H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, 9, BANNER_H - 1], fill=(247, 148, 29, 250))          # ORANGE @0.98
    d.rectangle([10, 0, BANNER_W - 1, BANNER_H - 1], fill=(27, 109, 243, 230))  # BLUE @0.90
    f = ImageFont.truetype(FONT, 31)
    d.text((34, BANNER_H // 2), text, font=f, fill=(255, 255, 255, 255), anchor="lm")
    img.save(path)
    return path

def banner_overlay(seg_dur):
    """x expression for the overlay: slide in, hold, slide out."""
    tin, sl = 0.15, 0.32
    tout = max(tin + sl + 0.3, seg_dur - 0.55)
    a = f"min(1\\,max(0\\,(t-{tin})/{sl}))"
    b = f"min(1\\,max(0\\,(t-{tout})/{sl}))"
    return f"-640+700*({a})-700*({b})", H - 108

# Coordinates measured by colour-thresholding the actual frames, then shifted
# into the cropped 1920x828 space (source y minus the 192px of browser chrome).
BTN_SAVE    = (1570, 754); SZ_SAVE    = (572, 72)   # green "Enregistrer les relevés de température"
BTN_CONFIRM = (871, 607);  SZ_CONFIRM = (241, 68)   # blue "Oui, enregistrer!" in the confirm modal

# (name, src_start, src_end, target_out_duration, click_time_or_None, button, btn_size, caption)
segs = [
    ("A",  0.30,  3.20,  2.40, None,  None,        None,        "1 · Vos équipements et leur plage cible"),
    ("B",  3.20,  6.60,  5.55, None,  None,        None,        None),
    ("C",  6.60, 10.45,  3.60, None,  None,        None,        "2 · Ajustez la température relevée"),
    ("D", 10.60, 10.95,  1.10, 10.90, BTN_SAVE,    SZ_SAVE,     None),
    ("E", 11.05, 12.30,  3.00, None,  None,        None,        "3 · Confirmez le relevé"),
    ("E2",12.30, 12.50,  0.90, 12.45, BTN_CONFIRM, SZ_CONFIRM,  None),
    ("F", 13.35, 15.25,  3.20, None,  None,        None,        None),
    ("G", 15.40, 20.60,  6.80, None,  None,        None,        "Relevé enregistré et daté"),
]
INTRO_D, OUTRO_D = 3.40, 6.20

def encode_seg(name, s, e, target, btn, btn_sz, caption):
    out = f"{SEG}/{name}.mp4"
    factor = (e - s) / target
    vf = f"{CHROME_CROP},setpts=(PTS-STARTPTS)/{factor:.6f}"
    if btn:
        crop_vf, box = crop_for(btn)
        vf += f",{crop_vf},{punch_highlight(btn, btn_sz, box)}"
    else:
        vf += f",scale={W}:{H}"

    cmd = ["ffmpeg","-y","-v","error","-ss",str(s),"-to",str(e),"-i",SRC,"-an"]
    if caption:
        png = banner_png(caption, f"{SEG}/banner_{name}.png")
        bx, by = banner_overlay(target)
        # fps=FPS MUST come before overlay. The rush is variable-frame-rate, and
        # overlay's framesync drops the trailing frames of a VFR main input --
        # segment E came out 2.32s instead of 3.20s until the stream was made
        # CFR first. The banner PNG is looped indefinitely and shortest=1 lets
        # the (now CFR) footage decide the segment length, exactly as the plain
        # -vf path does.
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
# measured_at), which is exactly the action the rush performs.
# ---------------------------------------------------------------------------
CLAUDE_PROMPT = ("Enregistre une température de [température] degrés pour "
                 "l'équipement [nom de l'équipement] dans mon établissement "
                 "FoodEatUp (ID [ID établissement]).")
CLAUDE_RESPONSE = "Bien sûr ! J'enregistre votre relevé de température…"

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

# Slightly longer than the module default: N6 has to carry stages 1+2 and N7 the
# whole chatbot stage (measured line durations, see SCRIPT.md).
CLAUDE_STAGE_D = [3.00, 1.70, 4.20]

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
             "fade",       # A -> B (continuous: same list view)
             "fade",       # B -> C (continuous: stepper adjustments)
             "fade",       # C -> D (continuous: click Enregistrer)
             "fade",       # D -> E (submit -> confirm modal)
             "fade",       # E -> E2 (continuous: click Oui, enregistrer)
             "slideleft",  # E2 -> F (cut past the save round-trip)
             "fade",       # F -> G (OK -> refreshed counters)
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
    "N0": 0.35,                  # hook, over the intro card (spills onto A)
    "N1": S["B"] + 0.25,         # equipment list + target range
    "N2": S["C"] + 0.25,         # +/- steppers
    "N3": S["D"] + 0.10,         # click "Enregistrer les relevés de température"
    "N4": S["E"] + 0.25,         # confirm modal
    "N5": S["G"] + 0.30,         # saved, dated, flagged non conforme
    "N6": S["claude1"] + 0.25,   # explains the prompt (reveal + copied)
    "N7": S["claude3"] + 0.25,   # paste into Claude -> instant result
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
FINAL = f"{ROOT}/out/foodeatup-temperature-tuto-v1.mp4"
run(["ffmpeg","-y","-v","error","-i",silent] + inputs +
    ["-filter_complex",";".join(filters),"-map","0:v","-map","[voa]",
     "-c:v","copy","-c:a","aac","-b:a","192k","-ar","48000","-ac","2",
     "-movflags","+faststart","-t",f"{total:.3f}",FINAL])
print(f"DONE: {FINAL}  {dur(FINAL):.2f}s")
