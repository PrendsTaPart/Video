import json, random
random.seed(11)
lines = json.load(open("work/lines.json"))
SL = json.load(open("shotlist.json"))
PONT_A, PONT_B = 126.0, SL["sections"]["COUPLET 3"][0]      # aucun texte sur le pont
CREME, MARINE, BLEU = "&H00E6F9FC", "&H00231A0F", "&H00FF7B00"

def esc(s): return s.replace("{","(").replace("}",")")
def tc(t):
    t = max(t, 0); h = int(t//3600); m = int(t%3600//60); s = t%60
    return f"{h}:{m:02d}:{s:05.2f}"

CH_SECTIONS = {"COUPLET 1"}                                  # côté « subit » : légèrement tremblant
cards = []
for ln in lines:
    if ln["section"] in ("INTRO",): continue
    ws = [w for w in ln["words"] if w["e"] > w["s"]]
    if not ws: continue
    if PONT_A <= ws[0]["s"] < PONT_B: continue
    buf = []
    for i, w in enumerate(ws):
        buf.append(w)
        gap = (ws[i+1]["s"] - w["e"]) if i+1 < len(ws) else 9
        n = sum(len(x["w"]) for x in buf) + len(buf)
        if len(buf) >= 4 or n >= 20 or gap > 0.34 or i == len(ws)-1:
            cards.append((ln, buf)); buf = []

ev = []
for ln, card in cards:
    tremble = ln["section"] in CH_SECTIONS
    for k, w in enumerate(card):
        parts = []
        for j, x in enumerate(card):
            t = esc(x["w"].upper())
            parts.append(f"{{\\c{BLEU}}}{t}{{\\c{CREME}}}" if j == k else t)
        txt = " ".join(parts)
        x0, y0 = 540, 1330
        if tremble:
            x0 += random.randint(-5, 5); y0 += random.randint(-4, 4)
        start = w["s"] if k else card[0]["s"]
        end   = card[k+1]["s"] if k+1 < len(card) else card[-1]["e"] + 0.12
        if end <= start: end = start + 0.1
        ev.append((start, end, f"{{\\an5\\pos({x0},{y0})}}{txt}"))

ev.sort()
head = f"""[Script Info]
ScriptType: v4.00+
PlayResX: 1080
PlayResY: 1920
WrapStyle: 2
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: K,Poppins ExtraBold,84,{CREME},{CREME},{MARINE},{MARINE},0,0,0,0,100,100,1,0,1,7,5,5,60,60,60,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
with open("work/subs.ass","w") as f:
    f.write(head)
    for a,b,t in ev:
        f.write(f"Dialogue: 0,{tc(a)},{tc(b)},K,,0,0,0,,{t}\n")
print(f"{len(cards)} cartons, {len(ev)} états karaoké")
print(f"pont sans texte : {PONT_A:.2f} → {PONT_B:.2f}")
