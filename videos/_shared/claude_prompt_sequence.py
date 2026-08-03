#!/usr/bin/env python3
# Shared "Use it with Claude" 3-stage chatbot-style animation, reused as-is
# across every FoodEatUp tutorial that has a matching mcp__FoodEatUp__* tool
# (see videos/FOODEATUP-TUTORIELS-WORKFLOW.md). One visual universe for the
# whole series -- only the prompt text (and optionally the assistant's
# reply line) changes per video. First built for foodeatup-tva-tuto.
#
# Usage from a project's build.py:
#
#   import sys; sys.path.insert(0, "/home/user/Video/videos/_shared")
#   from claude_prompt_sequence import render_claude_stage1_png, \
#       render_claude_stage2_png, render_claude_stage3_png, CLAUDE_STAGE_D
#
#   PROMPT = "Crée ... [placeholder] ..."
#   render_claude_stage1_png(f"{SEG}/claude1.png", W, H, PROMPT)
#   render_claude_stage2_png(f"{SEG}/claude2.png", W, H, PROMPT)
#   render_claude_stage3_png(f"{SEG}/claude3.png", W, H, PROMPT)
#   for i, d in enumerate(CLAUDE_STAGE_D, start=1):
#       card(f"{SEG}/claude{i}.png", f"{SEG}/claude{i}.mp4", d, zoom_in=True, fade=False)
#
# card() MUST be called with fade=False for these 3 stages -- they sit mid-
# video, not at the true start/end, and stacking card()'s own fade-to-black
# on top of the xfade crossfade on both sides turns a short stage into a
# murky blur (bug hit and fixed on foodeatup-tva-tuto, see its SCRIPT.md).
# Transitions into/between/out of the 3 stages should be "slideleft" (scene
# cuts), like everywhere else a cut skips footage.
import math
from PIL import Image, ImageDraw, ImageFont, ImageFilter

FONT_BOLD = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
FONT_REG  = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"
CLAUDE_LOGO_PATH = "/home/user/Video/studio-video/assets/brand/third-party-logos/claude-logo.png"

# Claude's real brand colours, sampled directly from the official logo
# asset (clay/coral accent) -- not guessed.
CLAY      = (217, 119, 87, 255)
CLAUDE_BG = (240, 238, 230, 255)   # Claude product's own warm cream background
FEU_CREAM = (252, 249, 230, 255)   # FoodEatUp cream #FCF9E6 -- stages 1 & 2 stay on-brand FEU
NAVY      = (15, 26, 35, 255)
DARK      = (46, 42, 38, 255)
WHITE     = (255, 255, 255, 255)

TITLE = "Utilisez cette fonctionnalité avec Claude"
DEFAULT_RESPONSE = "Bien sûr ! Je m'en occupe tout de suite…"

# reveal, copied, chatbot mockup -- same pacing on every video unless a
# project has a good reason to deviate (e.g. VO line runs unusually long).
CLAUDE_STAGE_D = [2.20, 1.30, 2.50]


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


def render_claude_stage1_png(path, W, H, prompt, title=TITLE,
                              subtitle="Le prompt à copier-coller dans Claude"):
    """Big prompt reveal on the FoodEatUp cream background -- no dark box."""
    img = Image.new("RGBA", (W, H), FEU_CREAM)
    d = ImageDraw.Draw(img)
    title_f = _font(True, 46)
    _center_text(d, W/2, 96, title, title_f, NAVY)
    sub_f = _font(False, 26)
    _center_text(d, W/2, 158, subtitle, sub_f, (15, 26, 35, 190))

    prompt_f = _font(True, 40)
    card_w = 1500
    pad_x, pad_y = 56, 40
    lines = _wrap(d, prompt, prompt_f, card_w - 2*pad_x - 24)
    line_h = 56
    card_h = pad_y*2 + line_h*len(lines)
    x0 = (W - card_w)/2
    y0 = 240

    shadow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    sd = ImageDraw.Draw(shadow)
    _rrect(sd, [x0+6, y0+10, x0+card_w+6, y0+card_h+10], 26, fill=(15, 26, 35, 40))
    shadow = shadow.filter(ImageFilter.GaussianBlur(10))
    img = Image.alpha_composite(img, shadow)
    d = ImageDraw.Draw(img)
    _rrect(d, [x0, y0, x0+card_w, y0+card_h], 26, fill=WHITE, outline=(27, 109, 243, 120), width=2)
    _rrect(d, [x0, y0, x0+14, y0+card_h], 8, fill=CLAY)

    for i, line in enumerate(lines):
        d.text((x0 + pad_x + 24, y0 + pad_y + i*line_h), line, font=prompt_f, fill=NAVY)

    cap_f = _font(False, 25)
    _center_text(d, W/2, y0+card_h+34, "Remplacez les [crochets] par vos valeurs", cap_f, (15, 26, 35, 170))
    img.convert("RGB").save(path)


def render_claude_stage2_png(path, W, H, prompt, title=TITLE,
                              caption="Copié dans le presse-papiers !"):
    """Same card, brief 'copied' confirmation beat."""
    img = Image.new("RGBA", (W, H), FEU_CREAM)
    d = ImageDraw.Draw(img)
    title_f = _font(True, 46)
    _center_text(d, W/2, 96, title, title_f, NAVY)

    prompt_f = _font(True, 40)
    card_w = 1500
    pad_x, pad_y = 56, 40
    lines = _wrap(d, prompt, prompt_f, card_w - 2*pad_x - 24)
    line_h = 56
    card_h = pad_y*2 + line_h*len(lines)
    x0 = (W - card_w)/2
    y0 = 240

    _rrect(d, [x0, y0, x0+card_w, y0+card_h], 26, fill=WHITE, outline=(46, 163, 89, 220), width=4)
    _rrect(d, [x0, y0, x0+14, y0+card_h], 8, fill=(46, 163, 89, 255))
    for i, line in enumerate(lines):
        d.text((x0 + pad_x + 24, y0 + pad_y + i*line_h), line, font=prompt_f, fill=(120, 120, 120, 255))

    # green "copied" badge, checkmark drawn (not a font glyph -- avoids
    # relying on unicode coverage in Liberation Sans)
    bx, by, br = x0+card_w-6, y0-6, 34
    d.ellipse([bx-br, by-br, bx+br, by+br], fill=(46, 163, 89, 255))
    d.line([(bx-14, by), (bx-4, by+12), (bx+16, by-14)], fill=WHITE, width=6, joint="curve")

    cap_f = _font(True, 30)
    _center_text(d, W/2, y0+card_h+30, caption, cap_f, (46, 163, 89, 255))
    img.convert("RGB").save(path)


def render_claude_stage3_png(path, W, H, prompt, response=DEFAULT_RESPONSE,
                              footer="Résultat instantané, sans quitter la conversation."):
    """Claude-branded chatbot mockup: real logo, clay user bubble with the
    pasted prompt, assistant bubble starting to act on it."""
    img = Image.new("RGBA", (W, H), CLAUDE_BG)
    d = ImageDraw.Draw(img)

    _rrect(d, [0, 0, W, 96], 0, fill=WHITE)
    d.line([(0, 96), (W, 96)], fill=(0, 0, 0, 18), width=2)
    logo = Image.open(CLAUDE_LOGO_PATH).convert("RGBA")
    lh = 40
    lw = int(logo.width * lh / logo.height)
    logo = logo.resize((lw, lh))
    img.paste(logo, (56, 28), logo)
    tag_f = _font(False, 24)
    d.text((56 + lw + 20, 36), "claude.ai", font=tag_f, fill=(120, 113, 103, 255))

    body_f = _font(False, 30)
    bubble_w = 900

    lines = _wrap(d, prompt, body_f, bubble_w - 80)
    line_h = 42
    bh = 48 + line_h*len(lines)
    bx1 = W - 80
    bx0 = bx1 - bubble_w
    by0 = 150
    _rrect(d, [bx0, by0, bx1, by0+bh], 24, fill=CLAY)
    for i, line in enumerate(lines):
        d.text((bx0+40, by0+28+i*line_h), line, font=body_f, fill=WHITE)

    # assistant avatar -- clay circle with a hand-drawn asterisk (Claude's
    # mark) -- the only logo asset provided is the horizontal wordmark
    avy = by0 + bh + 70
    ar = 26
    ax = 56 + ar
    d.ellipse([ax-ar, avy-ar, ax+ar, avy+ar], fill=CLAY)
    for k in range(6):
        ang = math.pi * k / 6
        dx, dy = 16*math.cos(ang), 16*math.sin(ang)
        d.line([(ax-dx, avy-dy), (ax+dx, avy+dy)], fill=WHITE, width=4)

    rlines = _wrap(d, response, body_f, bubble_w - 80)
    rh = 48 + line_h*len(rlines) + 30
    rx0 = ax + ar + 24
    _rrect(d, [rx0, avy-ar, rx0+bubble_w, avy-ar+rh], 24, fill=WHITE, outline=(0, 0, 0, 18), width=2)
    for i, line in enumerate(rlines):
        d.text((rx0+40, avy-ar+28+i*line_h), line, font=body_f, fill=DARK)
    dy = avy-ar+28+len(rlines)*line_h+14
    for i in range(3):
        d.ellipse([rx0+40+i*26, dy, rx0+40+i*26+12, dy+12], fill=(200, 193, 183, 255))

    cap_f = _font(False, 25)
    _center_text(d, W/2, H-56, footer, cap_f, (46, 42, 38, 190))
    img.convert("RGB").save(path)
