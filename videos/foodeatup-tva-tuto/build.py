#!/usr/bin/env python3
# FoodEatUp "Paramétrer sa TVA" tutorial.
# No avatar clip: full ElevenLabs VO throughout. Speed = setpts (never zoompan
# on real footage). xfade on every cut, forced back to yuv420p at the end of
# the chain. 48kHz stereo AAC, +faststart. Segment targets set close to each
# VO line's measured duration (see vo/*.mp3) before building, not after.
import subprocess, os

ROOT = "/home/user/Video/videos/foodeatup-tva-tuto"
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

BTN_ADD_TVA  = (1708, 351); SZ_ADD_TVA  = (170, 46)   # "Ajouter TVA" (header)
BTN_ADD_SAVE = (1204, 602); SZ_ADD_SAVE = (136, 56)   # "Ajouter" (modal submit)
BTN_EDIT     = (1489, 537); SZ_EDIT     = (24, 24)    # pencil icon on the row
BTN_SAVE     = (1172, 602); SZ_SAVE     = (204, 56)   # "Sauvegarder" (modal submit)

# (name, src_start, src_end, target_out_duration, click_time_or_None, button, btn_size, caption)
segs = [
    ("A", 0.20, 1.40, 2.00, None, None,        None,        "1 · Ajouter une TVA"),
    ("B", 1.40, 1.55, 0.90, 1.40, BTN_ADD_TVA,  SZ_ADD_TVA,  None),
    ("C", 2.00, 5.90, 2.50, None, None,        None,        "2 · Nom et pourcentage"),
    ("D", 6.30, 6.55, 0.90, 6.40, BTN_ADD_SAVE, SZ_ADD_SAVE, None),
    ("E", 7.00, 9.00, 2.70, None, None,        None,        "Taux ajouté"),
    ("F", 9.30, 9.55, 0.90, 9.40, BTN_EDIT,     SZ_EDIT,     "3 · Modifier une TVA"),
    ("G", 10.00, 14.90, 2.90, None, None,      None,        None),
    ("H", 15.20, 15.55, 0.90, 15.30, BTN_SAVE, SZ_SAVE,     None),
    ("I", 16.00, 18.20, 2.10, None, None,      None,        "Taux mis à jour"),
]
INTRO_D, OUTRO_D = 2.60, 6.20

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
# "Use it with Claude" sequence -- 3-stage chatbot-style animation, PIL
# rendered (not ffmpeg drawtext/lavfi -- gives full control over rounded
# chat bubbles, real logo compositing and text wrapping, and sidesteps the
# drawtext '%'-expansion bug entirely since PIL just draws literal glyphs).
# Each stage is a flat PNG fed through the existing card() -- same proven
# image->video colour path used for intro/outro, no lavfi colour source.
# Reusable template: any future video with a matching FoodEatUp MCP tool
# gets this same 3-stage sequence (see FOODEATUP-TUTORIELS-WORKFLOW.md).
# ---------------------------------------------------------------------------
from PIL import Image, ImageDraw, ImageFont

FONT_BOLD = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
FONT_REG  = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"
CLAUDE_LOGO_PATH = "/home/user/Video/studio-video/assets/brand/third-party-logos/claude-logo.png"

# Claude's real brand colours, sampled from the official logo asset itself
# (clay/coral accent) -- not guessed.
CLAY   = (217, 119, 87, 255)
CLAUDE_BG = (240, 238, 230, 255)   # Claude product's own warm cream background
FEU_CREAM = (252, 249, 230, 255)  # FoodEatUp cream #FCF9E6
NAVY   = (15, 26, 35, 255)
DARK   = (46, 42, 38, 255)
WHITE  = (255, 255, 255, 255)

CLAUDE_PROMPT = ("Crée un taux de TVA nommé [nom du taux] à [pourcentage]% "
                  "pour mon établissement FoodEatUp (ID [ID établissement]).")

def _font(bold, size):
    return ImageFont.truetype(FONT_BOLD if bold else FONT_REG, size)

def _wrap(draw, text, font, max_w):
    words, lines, cur = text.split(" "), [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=font) <= max_w:
            cur = trial
        else:
            if cur: lines.append(cur)
            cur = w
    if cur: lines.append(cur)
    return lines

def _rrect(draw, box, radius, fill=None, outline=None, width=1):
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)

def _center_text(draw, cx, y, text, font, fill):
    w = draw.textlength(text, font=font)
    draw.text((cx - w / 2, y), text, font=font, fill=fill)

def render_claude_stage1_png(path):
    """Big prompt reveal on the FoodEatUp cream background -- no dark box."""
    img = Image.new("RGBA", (W, H), FEU_CREAM)
    d = ImageDraw.Draw(img)
    title_f = _font(True, 46)
    _center_text(d, W/2, 96, "Utilisez cette fonctionnalité avec Claude", title_f, NAVY)
    sub_f = _font(False, 26)
    _center_text(d, W/2, 158, "Le prompt à copier-coller dans Claude", sub_f, (15,26,35,190))

    prompt_f = _font(True, 40)
    card_w = 1500
    pad_x, pad_y = 56, 40
    lines = _wrap(d, CLAUDE_PROMPT, prompt_f, card_w - 2*pad_x - 24)
    line_h = 56
    card_h = pad_y*2 + line_h*len(lines)
    x0 = (W - card_w)/2
    y0 = 240

    # soft shadow, then white card, then clay accent bar on the left
    shadow = Image.new("RGBA", (W, H), (0,0,0,0))
    sd = ImageDraw.Draw(shadow)
    _rrect(sd, [x0+6, y0+10, x0+card_w+6, y0+card_h+10], 26, fill=(15,26,35,40))
    shadow = shadow.filter(__import__("PIL.ImageFilter", fromlist=["ImageFilter"]).GaussianBlur(10))
    img = Image.alpha_composite(img, shadow)
    d = ImageDraw.Draw(img)
    _rrect(d, [x0, y0, x0+card_w, y0+card_h], 26, fill=WHITE, outline=(27,109,243,120), width=2)
    _rrect(d, [x0, y0, x0+14, y0+card_h], 8, fill=CLAY)

    for i, line in enumerate(lines):
        d.text((x0 + pad_x + 24, y0 + pad_y + i*line_h), line, font=prompt_f, fill=NAVY)

    cap_f = _font(False, 25)
    _center_text(d, W/2, y0+card_h+34, "Remplacez les [crochets] par vos valeurs", cap_f, (15,26,35,170))
    img.convert("RGB").save(path)

def render_claude_stage2_png(path):
    """Same card, brief 'copied' confirmation beat."""
    img = Image.new("RGBA", (W, H), FEU_CREAM)
    d = ImageDraw.Draw(img)
    title_f = _font(True, 46)
    _center_text(d, W/2, 96, "Utilisez cette fonctionnalité avec Claude", title_f, NAVY)

    prompt_f = _font(True, 40)
    card_w = 1500
    pad_x, pad_y = 56, 40
    lines = _wrap(d, CLAUDE_PROMPT, prompt_f, card_w - 2*pad_x - 24)
    line_h = 56
    card_h = pad_y*2 + line_h*len(lines)
    x0 = (W - card_w)/2
    y0 = 240

    _rrect(d, [x0, y0, x0+card_w, y0+card_h], 26, fill=WHITE, outline=(46,163,89,220), width=4)
    _rrect(d, [x0, y0, x0+14, y0+card_h], 8, fill=(46,163,89,255))
    for i, line in enumerate(lines):
        d.text((x0 + pad_x + 24, y0 + pad_y + i*line_h), line, font=prompt_f, fill=(120,120,120,255))

    # green "copied" badge, top-right of the card, checkmark drawn (not a
    # font glyph -- avoids relying on unicode coverage in Liberation Sans)
    bx, by, br = x0+card_w-6, y0-6, 34
    d.ellipse([bx-br, by-br, bx+br, by+br], fill=(46,163,89,255))
    d.line([(bx-14, by), (bx-4, by+12), (bx+16, by-14)], fill=WHITE, width=6, joint="curve")

    cap_f = _font(True, 30)
    _center_text(d, W/2, y0+card_h+30, "Copié dans le presse-papiers !", cap_f, (46,163,89,255))
    img.convert("RGB").save(path)

def render_claude_stage3_png(path):
    """Claude-branded chatbot mockup: real logo, clay user bubble with the
    pasted prompt, assistant bubble starting to act on it."""
    img = Image.new("RGBA", (W, H), CLAUDE_BG)
    d = ImageDraw.Draw(img)

    # top bar
    _rrect(d, [0, 0, W, 96], 0, fill=WHITE)
    d.line([(0, 96), (W, 96)], fill=(0,0,0,18), width=2)
    logo = Image.open(CLAUDE_LOGO_PATH).convert("RGBA")
    lh = 40
    lw = int(logo.width * lh / logo.height)
    logo = logo.resize((lw, lh))
    img.paste(logo, (56, 28), logo)
    tag_f = _font(False, 24)
    d.text((56 + lw + 20, 36), "claude.ai", font=tag_f, fill=(120,113,103,255))

    body_f = _font(False, 30)
    bubble_w = 900

    # user bubble (right), clay fill, white text -- the pasted prompt
    lines = _wrap(d, CLAUDE_PROMPT, body_f, bubble_w - 80)
    line_h = 42
    bh = 48 + line_h*len(lines)
    bx1 = W - 80
    bx0 = bx1 - bubble_w
    by0 = 150
    _rrect(d, [bx0, by0, bx1, by0+bh], 24, fill=CLAY)
    for i, line in enumerate(lines):
        d.text((bx0+40, by0+28+i*line_h), line, font=body_f, fill=WHITE)

    # assistant avatar -- clay circle with a hand-drawn asterisk (Claude's
    # mark), since the only logo asset provided is the horizontal wordmark
    avy = by0 + bh + 70
    ar = 26
    ax = 56 + ar
    d.ellipse([ax-ar, avy-ar, ax+ar, avy+ar], fill=CLAY)
    import math
    for k in range(6):
        ang = math.pi * k / 6
        dx, dy = 16*math.cos(ang), 16*math.sin(ang)
        d.line([(ax-dx, avy-dy), (ax+dx, avy+dy)], fill=WHITE, width=4)

    # assistant response bubble (left), white card, dark text + typing dots
    resp = "Bien sûr ! Je crée ce taux de TVA pour votre établissement…"
    rlines = _wrap(d, resp, body_f, bubble_w - 80)
    rh = 48 + line_h*len(rlines) + 30
    rx0 = ax + ar + 24
    _rrect(d, [rx0, avy-ar, rx0+bubble_w, avy-ar+rh], 24, fill=WHITE, outline=(0,0,0,18), width=2)
    for i, line in enumerate(rlines):
        d.text((rx0+40, avy-ar+28+i*line_h), line, font=body_f, fill=DARK)
    dy = avy-ar+28+len(rlines)*line_h+14
    for i in range(3):
        d.ellipse([rx0+40+i*26, dy, rx0+40+i*26+12, dy+12], fill=(200,193,183,255))

    cap_f = _font(False, 25)
    _center_text(d, W/2, H-56, "Résultat instantané, sans quitter la conversation.", cap_f, (46,42,38,190))
    img.convert("RGB").save(path)

def card(img, out, secs, zoom_in=True, fade=True):
    """fade=False for cards that sit mid-video and only ever meet the rest
    of the timeline through an xfade crossfade (e.g. the claude1/2/3 chatbot
    stages) -- baking in card()'s own 0.4s fade-to-black on top of a short
    clip's crossfades on both sides stacks two darkenings and makes brief
    cards (~1s) read as a murky blur instead of a clean beat. Regular
    intro/outro (true start/end of the video) keep fade=True."""
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

CLAUDE_STAGE_D = [2.20, 1.30, 2.50]  # reveal, copied, chatbot mockup

def build_silent(outro_d):
    card(f"{ROOT}/assets/intro.jpg", f"{SEG}/intro.mp4", INTRO_D, zoom_in=True)
    card(f"{ROOT}/assets/outro.jpg", f"{SEG}/outro.mp4", outro_d, zoom_in=False)
    stage_pngs = [f"{SEG}/claude1.png", f"{SEG}/claude2.png", f"{SEG}/claude3.png"]
    stage_renderers = [render_claude_stage1_png, render_claude_stage2_png, render_claude_stage3_png]
    for png, renderer in zip(stage_pngs, stage_renderers):
        if not os.path.exists(png):
            renderer(png)
    for i, png in enumerate(stage_pngs):
        card(png, f"{SEG}/claude{i+1}.mp4", CLAUDE_STAGE_D[i], zoom_in=True, fade=False)
    parts = [f"{SEG}/intro.mp4"]
    for name, s, e, target, ck, btn, sz, cap in segs:
        parts.append(encode_seg(name, s, e, target, btn, sz, cap))
    parts.append(f"{SEG}/claude1.mp4")
    parts.append(f"{SEG}/claude2.mp4")
    parts.append(f"{SEG}/claude3.mp4")
    parts.append(f"{SEG}/outro.mp4")

    # slideleft between the 3 claude stages (distinct scenes/cuts, same
    # convention as skipped-footage cuts elsewhere) and into/out of outro;
    # fade everywhere else (continuous screen-recording action).
    trans = ["fade"] * (len(parts) - 1)
    trans[-4] = "slideleft"  # last real seg -> claude1
    trans[-3] = "slideleft"  # claude1 -> claude2
    trans[-2] = "slideleft"  # claude2 -> claude3
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
    "N0": 0.30,
    "N1": S["A"] + 0.20,
    "N2": S["C"] + 0.20,
    "N3": S["E"] + 0.20,
    "N4": S["F"] + 0.20,
    "N5": S["H"] + 0.20,
    "N6": S["claude1"] + 0.20,
    "N7": OUTRO_START + 0.35,
}
keys = [f"N{i}" for i in range(8)]
off, prev_end = {}, -GAP
for k in keys:
    o = max(anchor[k], prev_end + GAP); off[k] = o
    prev_end = o + dur(f"{ROOT}/vo/{k}.mp3")
print("offsets:", {k: round(v, 2) for k, v in off.items()}, "voice_end:", round(prev_end, 2))

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
FINAL = f"{ROOT}/out/foodeatup-tva-tuto-v1.mp4"
run(["ffmpeg","-y","-v","error","-i",silent] + inputs +
    ["-filter_complex",";".join(filters),"-map","0:v","-map","[voa]",
     "-c:v","copy","-c:a","aac","-b:a","192k","-ar","48000","-ac","2",
     "-movflags","+faststart","-t",f"{total:.3f}",FINAL])
print(f"DONE: {FINAL}  {dur(FINAL):.2f}s")
