#!/usr/bin/env python3
# Shared "Jarvis voice agent" 2-stage explainer animation, for tutorials about
# FoodEatUp's Jarvis voice assistant (seats, tokens, role-based voice access).
# Same engine/spirit as claude_prompt_sequence.py: PNG rendered via PIL (full
# control over text/shapes, no drawtext/%/emoji-glyph pitfalls), then passed
# into a project's card() with fade=False (mid-video stage, meets the timeline
# only through xfade -- see FOODEATUP-TUTORIELS-WORKFLOW.md). No dedicated
# MCP tool backs this feature (QR/phone pairing is physical, not automatable),
# so this replaces the "use it with Claude" slot rather than sitting beside it.
#
# Usage from a project's build.py:
#
#   import sys; sys.path.insert(0, "/home/user/Video/videos/_shared")
#   from jarvis_voice_sequence import render_jarvis_stage1_png, render_jarvis_stage2_png
#   render_jarvis_stage1_png(f"{SEG}/jarvis1.png", W, H)
#   render_jarvis_stage2_png(f"{SEG}/jarvis2.png", W, H)
#   for i, png in enumerate([f"{SEG}/jarvis1.png", f"{SEG}/jarvis2.png"], start=1):
#       card(png, f"{SEG}/jarvis{i}.mp4", 3.00, zoom_in=True, fade=False)
import math
from PIL import Image, ImageDraw, ImageFont

FONT_BOLD = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
FONT_REG  = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"

FEU_CREAM = (252, 249, 230, 255)   # FoodEatUp cream #FCF9E6
NAVY      = (15, 26, 35, 255)
BLUE      = (27, 109, 243, 255)
PURPLE    = (124, 92, 240, 255)    # matches the real Jarvis mic gradient (blue->purple)
GREEN     = (46, 163, 89, 255)
ORANGE    = (247, 148, 29, 255)
WHITE     = (255, 255, 255, 255)
GREY      = (120, 120, 120, 255)

ROLE_COLORS = {
    "MANAGER": (27, 109, 243, 255),
    "ADMIN":   (124, 92, 240, 255),
}
ROLE_TAGS = {
    "MANAGER": ["Stock", "Courses", "Finances"],
    "ADMIN":   ["Équipe", "Comptabilité", "Config"],
}


def _font(bold, size):
    return ImageFont.truetype(FONT_BOLD if bold else FONT_REG, size)


def _center_text(draw, cx, y, text, font, fill):
    w = draw.textlength(text, font=font)
    draw.text((cx - w / 2, y), text, font=font, fill=fill)


def _rrect(draw, box, radius, fill=None, outline=None, width=1):
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def _tint(color, bg, frac):
    """Pre-blended opaque tint. Drawing straight onto a flat RGB base with an
    RGBA fill does NOT alpha-composite (PIL just writes the RGBA tuple's RGB
    verbatim, alpha gets discarded on convert('RGB')) -- bug hit while
    building this module: 'light tinted' avatar circles and tag pills came
    out fully solid, making same-hue text drawn on top invisible. Blend the
    colour against the background ourselves and always fill with a plain
    opaque RGB tuple."""
    return tuple(int(bg[c] + (color[c] - bg[c]) * frac) for c in range(3))


def _draw_mic(draw, cx, cy, r, color=WHITE):
    """Hand-drawn mic glyph (capsule body + stand), no font/emoji glyph."""
    bw, bh = r * 0.62, r * 1.15
    _rrect(draw, [cx - bw / 2, cy - bh / 2, cx + bw / 2, cy + bh / 2], bw / 2, fill=color)
    draw.arc([cx - r * 0.95, cy - r * 0.55, cx + r * 0.95, cy + r * 0.95],
              start=15, end=165, fill=color, width=max(3, int(r * 0.09)))
    draw.line([(cx, cy + r * 0.95), (cx, cy + r * 1.35)], fill=color, width=max(3, int(r * 0.09)))
    draw.line([(cx - r * 0.4, cy + r * 1.35), (cx + r * 0.4, cy + r * 1.35)],
              fill=color, width=max(3, int(r * 0.09)))


def _draw_robot_badge(draw, cx, cy, r, color):
    """Small hand-drawn robot head, echoing the in-app Jarvis badge icon."""
    _rrect(draw, [cx - r, cy - r * 0.8, cx + r, cy + r * 0.9], r * 0.35, fill=color)
    eye_r = r * 0.14
    draw.ellipse([cx - r * 0.45 - eye_r, cy - eye_r, cx - r * 0.45 + eye_r, cy + eye_r], fill=WHITE)
    draw.ellipse([cx + r * 0.45 - eye_r, cy - eye_r, cx + r * 0.45 + eye_r, cy + eye_r], fill=WHITE)
    draw.line([(cx, cy - r), (cx, cy - r * 1.35)], fill=color, width=max(2, int(r * 0.08)))
    draw.ellipse([cx - r * 0.1, cy - r * 1.5, cx + r * 0.1, cy - r * 1.3], fill=color)


def render_jarvis_stage1_png(path, W, H,
                              title="Un siège Jarvis par employé",
                              subtitle="Jarvis s'adapte au rôle et aux permissions de chacun"):
    """3 employee seats fanned out under Jarvis, each with its own role tags --
    visual explanation of role/permission-scoped voice access (no MCP tool
    backs this, so it's a generated explainer, not a screen capture)."""
    img = Image.new("RGBA", (W, H), FEU_CREAM)
    d = ImageDraw.Draw(img)

    title_f = _font(True, 46)
    _center_text(d, W / 2, 74, title, title_f, NAVY)
    sub_f = _font(False, 25)
    _center_text(d, W / 2, 134, subtitle, sub_f, (15, 26, 35, 190))

    # Central Jarvis hub.
    hub_cx, hub_cy, hub_r = W / 2, 300, 76
    for ring_r, frac in [(hub_r + 34, 0.25), (hub_r + 18, 0.45)]:
        d.ellipse([hub_cx - ring_r, hub_cy - ring_r, hub_cx + ring_r, hub_cy + ring_r],
                   outline=_tint(PURPLE, FEU_CREAM, frac), width=4)
    d.ellipse([hub_cx - hub_r, hub_cy - hub_r, hub_cx + hub_r, hub_cy + hub_r], fill=PURPLE)
    _draw_mic(d, hub_cx, hub_cy - 6, hub_r * 0.5, color=WHITE)
    label_f = _font(True, 24)
    _center_text(d, hub_cx, hub_cy + hub_r + 16, "JARVIS", label_f, PURPLE)

    seats = [
        ("AC", "Alice", "MANAGER"),
        ("JD", "Jean", "ADMIN"),
        ("SA", "Soulayma", "MANAGER"),
    ]
    seat_y = 520
    xs = [W * 0.20, W * 0.5, W * 0.80]
    name_f = _font(True, 28)
    role_f = _font(False, 20)
    tag_f = _font(True, 19)

    for (initials, name, role), sx in zip(seats, xs):
        color = ROLE_COLORS[role]
        line_col = _tint(color, FEU_CREAM, 0.65)
        # dashed connector from hub down to this seat
        steps = 22
        for i in range(steps):
            tt0, tt1 = i / steps, (i + 0.5) / steps
            if i % 2:
                continue
            x0 = hub_cx + (sx - hub_cx) * tt0
            y0 = hub_cy + hub_r + 10 + (seat_y - 60 - (hub_cy + hub_r + 10)) * tt0
            x1 = hub_cx + (sx - hub_cx) * tt1
            y1 = hub_cy + hub_r + 10 + (seat_y - 60 - (hub_cy + hub_r + 10)) * tt1
            d.line([(x0, y0), (x1, y1)], fill=line_col, width=3)

        av_r = 46
        d.ellipse([sx - av_r, seat_y - av_r, sx + av_r, seat_y + av_r],
                   fill=_tint(color, FEU_CREAM, 0.16), outline=color, width=3)
        _center_text(d, sx, seat_y - 16, initials, _font(True, 30), color)
        _center_text(d, sx, seat_y + av_r + 14, name, name_f, NAVY)
        _center_text(d, sx, seat_y + av_r + 48, role, role_f, GREY)

        tags = ROLE_TAGS[role]
        tw = [d.textlength(t, font=tag_f) + 28 for t in tags]
        total_w = sum(tw) + 10 * (len(tags) - 1)
        tx = sx - total_w / 2
        ty = seat_y + av_r + 78
        tag_bg = _tint(color, FEU_CREAM, 0.14)
        for t, w in zip(tags, tw):
            _rrect(d, [tx, ty, tx + w, ty + 32], 16, fill=tag_bg)
            _center_text(d, tx + w / 2, ty + 6, t, tag_f, color)
            tx += w + 10

    img.convert("RGB").save(path)


def render_jarvis_stage2_png(path, W, H,
                              title="Contrôlez FoodEatUp à la voix",
                              subtitle="Dites simplement ce que vous voulez faire"):
    """Big pulsing-mic hero: concentric sound-wave rings baked into the still
    (card()'s Ken Burns zoom animates the rest, same trick as every other
    generated card in the series -- no per-frame procedural animation)."""
    bg = (240, 238, 230)
    img = Image.new("RGBA", (W, H), (*bg, 255))
    d = ImageDraw.Draw(img)

    cx, cy = W / 2, H / 2 + 20
    for i, (rr, frac) in enumerate([(260, 0.10), (200, 0.16), (145, 0.24)]):
        d.ellipse([cx - rr, cy - rr, cx + rr, cy + rr], outline=_tint(PURPLE, bg, frac),
                   width=10 - i * 2)

    core_r = 100
    steps = 40
    for i in range(steps):
        t = i / steps
        r = core_r * (1 - 0.12 * t)
        col = tuple(int(BLUE[c] + (PURPLE[c] - BLUE[c]) * t) for c in range(3))
        d.ellipse([cx - r, cy - r * (1 - t * 0.02), cx + r, cy + r], fill=(*col, 255))
    _draw_mic(d, cx, cy - 8, core_r * 0.55, color=WHITE)

    title_f = _font(True, 48)
    _center_text(d, W / 2, cy - 260 - 60, title, title_f, NAVY)
    sub_f = _font(False, 27)
    _center_text(d, W / 2, cy + 260 + 30, subtitle, sub_f, (15, 26, 35, 190))

    img.convert("RGB").save(path)
