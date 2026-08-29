import json, re, unicodedata, difflib

def norm(s):
    s = unicodedata.normalize("NFD", s.lower())
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    s = s.replace("’","'").replace("œ","oe")
    s = re.sub(r"^(j|l|d|m|t|s|n|c|qu)'", "", s)     # élisions : j'crie → crie
    s = re.sub(r"[^a-z0-9]", "", s)
    return s

tr = json.load(open("work/transcript.json"))
W = [(norm(w["w"]), w["s"], w["e"]) for s in tr for w in s["words"] if norm(w["w"])]

lines, cur_sec = [], None
for raw in open("lyrics.txt"):
    t = raw.strip()
    if not t: continue
    if t.startswith("["):
        cur_sec = t.strip("[]"); continue
    raws = re.findall(r"[\w’'À-ÿ]+", t)
    pairs = [(norm(x), x) for x in raws]
    pairs = [p for p in pairs if p[0]]
    lines.append({"section": cur_sec, "text": t,
                  "toks": [p[0] for p in pairs], "raws": [p[1] for p in pairs]})

L = [(t, i, k) for i, ln in enumerate(lines) for k, t in enumerate(ln["toks"])]

def sim(a, b):
    if a == b: return 1.0
    r = difflib.SequenceMatcher(None, a, b).ratio()
    return r if r > 0.62 else 0.0

# Needleman-Wunsch mots-paroles × mots-transcription
n, m = len(L), len(W)
GAP = -0.45
prev = [GAP*j for j in range(m+1)]
ptr = []
for i in range(1, n+1):
    cur = [GAP*i] + [0.0]*m
    row = bytearray(m+1)
    for j in range(1, m+1):
        d = prev[j-1] + (sim(L[i-1][0], W[j-1][0])*2 - 0.5)
        u = prev[j] + GAP
        l = cur[j-1] + GAP
        if d >= u and d >= l: cur[j], row[j] = d, 1
        elif u >= l:          cur[j], row[j] = u, 2
        else:                 cur[j], row[j] = l, 3
    ptr.append(row); prev = cur

i, j = n, m
hits = {}
wordhits = {}
while i > 0 and j > 0:
    p = ptr[i-1][j]
    if p == 1:
        if sim(L[i-1][0], W[j-1][0]) > 0:
            hits.setdefault(L[i-1][1], []).append((W[j-1][1], W[j-1][2]))
            wordhits[(L[i-1][1], L[i-1][2])] = (W[j-1][1], W[j-1][2])
        i -= 1; j -= 1
    elif p == 2: i -= 1
    else: j -= 1

for idx, ln in enumerate(lines):
    h = hits.get(idx)
    ln["start"] = round(min(a for a, b in h), 3) if h else None
    ln["end"]   = round(max(b for a, b in h), 3) if h else None
    ln["n_hits"] = len(h) if h else 0

# interpolation des lignes non alignées
for idx, ln in enumerate(lines):
    if ln["start"] is None:
        p = next((lines[k]["end"] for k in range(idx-1, -1, -1) if lines[k]["end"]), 0.0)
        nx = next((lines[k]["start"] for k in range(idx+1, len(lines)) if lines[k]["start"]), p+2)
        ln["start"], ln["end"], ln["interpole"] = round(p,3), round(nx,3), True

# monotonie
for k in range(1, len(lines)):
    if lines[k]["start"] < lines[k-1]["start"]:
        lines[k]["start"] = lines[k-1]["end"]
    if lines[k]["end"] <= lines[k]["start"]:
        lines[k]["end"] = lines[k]["start"] + 1.0

for idx, ln in enumerate(lines):
    ws = []
    for k, d in enumerate(ln["raws"]):
        t = wordhits.get((idx, k))
        ws.append({"w": d, "s": t[0] if t else None, "e": t[1] if t else None})
    # interpolation linéaire des mots non alignés à l'intérieur de la ligne
    known = [(k, w["s"], w["e"]) for k, w in enumerate(ws) if w["s"] is not None]
    if known:
        for k, w in enumerate(ws):
            if w["s"] is None:
                before = [x for x in known if x[0] < k]; after = [x for x in known if x[0] > k]
                a = before[-1][2] if before else ln["start"]
                b = after[0][1] if after else ln["end"]
                gap = (k - (before[-1][0] if before else -1))
                tot = ((after[0][0] if after else len(ws)) - (before[-1][0] if before else -1))
                w["s"] = a + (b - a) * (gap - 1) / max(tot, 1)
                w["e"] = a + (b - a) * gap / max(tot, 1)
    else:
        step = (ln["end"] - ln["start"]) / max(len(ws), 1)
        for k, w in enumerate(ws):
            w["s"] = ln["start"] + k * step; w["e"] = w["s"] + step
    for w in ws:
        w["s"] = round(float(w["s"]), 3); w["e"] = round(float(max(w["e"], w["s"] + 0.08)), 3)
    ln["words"] = ws

FIX = {"Deux cuisines. Une rue.": (192.72, 195.12),
       "Demain, t'ouvres laquelle ?": (196.08, 196.78)}
for ln in lines:
    if ln["text"] in FIX:
        a, b = FIX[ln["text"]]
        ln["start"], ln["end"] = a, b
        n = len(ln["words"]); step = (b - a) / max(n, 1)
        for k, w in enumerate(ln["words"]):
            w["s"] = round(a + k*step, 3); w["e"] = round(a + (k+1)*step, 3)

json.dump(lines, open("work/lines.json","w"), ensure_ascii=False, indent=1)

sec, order = {}, []
for ln in lines:
    s = ln["section"]
    if s not in sec: sec[s] = [ln["start"], ln["end"]]; order.append(s)
    sec[s][0] = min(sec[s][0], ln["start"]); sec[s][1] = max(sec[s][1], ln["end"])
print("SECTIONS")
for s in order:
    a, b = sec[s]; print(f"  {s:<14} {a:7.2f} → {b:7.2f}  ({b-a:5.1f}s)")
print("\nLIGNES")
for ln in lines:
    flag = "~" if ln.get("interpole") else " "
    print(f"{flag}{ln['start']:7.2f}-{ln['end']:7.2f} [{ln['n_hits']:2d}/{len(ln['toks']):2d}] {ln['text'][:62]}")
