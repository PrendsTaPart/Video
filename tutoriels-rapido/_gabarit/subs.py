"""Sous-titres à partir du SCRIPT (texte exact) calé sur les temps de la transcription Whisper.
Avantage : aucune faute de transcription à l'écran (IMAP, devis, noms propres…).
build_subs(cfg, words, offset) -> [[début, fin, texte], ...]
Règles : une ligne, 2 à 6 mots (7 si cela évite un mot orphelin), coupure à la ponctuation, jamais de point final."""
import difflib
import re
import unicodedata

NUM = {'un': '1', 'une': '1', 'deux': '2', 'trois': '3', 'quatre': '4', 'cinq': '5', 'six': '6', 'sept': '7', 'huit': '8',
       'neuf': '9', 'dix': '10', 'douze': '12', 'quinze': '15', 'vingt': '20', 'trente': '30'}


def _norm(s):
    s = unicodedata.normalize('NFKD', s.lower())
    s = ''.join(c for c in s if not unicodedata.combining(c))
    s = re.sub(r'[^a-z0-9]', '', s)
    return NUM.get(s, s)


def build_subs(cfg, words, offset):
    # mots du script (avec ponctuation) et jetons normalisés
    sw = []                                   # (mot affiché, [jetons])
    for p in cfg['paragraphs']:
        for w in p['text'].split():
            toks = [t for t in (_norm(x) for x in re.split(r"['’\-]", w)) if t]
            if not toks and sw:                   # « : », « ; », « ? »… : rattaché au mot précédent
                sw[-1] = (sw[-1][0] + ' ' + w, sw[-1][1]); continue
            sw.append((w, toks))
    st, sidx = [], []
    for i, (_, toks) in enumerate(sw):
        for t in toks:
            st.append(t); sidx.append(i)
    tt, tidx = [], []
    for j, w in enumerate(words):
        for t in [x for x in (_norm(y) for y in re.split(r"[\s'’\-]+", w['text'])) if x]:
            tt.append(t); tidx.append(j)
    m = {}
    for a, b, n in difflib.SequenceMatcher(a=st, b=tt, autojunk=False).get_matching_blocks():
        for k in range(n):
            m.setdefault(sidx[a + k], tidx[b + k])
    # temps de chaque mot du script (interpolés entre deux mots retrouvés)
    times = [None] * len(sw)
    for i in range(len(sw)):
        if i in m:
            times[i] = (words[m[i]]['start'], words[m[i]]['end'])
    known = [i for i, t in enumerate(times) if t]
    for i in range(len(sw)):
        if times[i]:
            continue
        prev = max([k for k in known if k < i], default=None)
        nxt = min([k for k in known if k > i], default=None)
        a = times[prev][1] if prev is not None else 0.0
        b = times[nxt][0] if nxt is not None else words[-1]['end']
        span = (nxt if nxt is not None else len(sw)) - (prev if prev is not None else -1)
        pos = i - (prev if prev is not None else -1)
        s = a + (b - a) * (pos - 0.5) / span
        times[i] = (s, s + max(0.12, (b - a) / span))
    # découpage
    chunks, cur = [], []
    for i, (w, _) in enumerate(sw):
        nxt = sw[i + 1][0] if i + 1 < len(sw) else None
        sentence_end = re.search(r'[.!?…]$', w)
        if sentence_end and not cur and chunks and len(chunks[-1]) < 7:
            chunks[-1].append(i); continue
        cur.append(i)
        gap = (times[i + 1][0] - times[i][1]) if nxt else 9
        nxt_closes = nxt is not None and re.search(r'[.!?…,]$', nxt)
        full = len(cur) >= 6 and not (len(cur) < 7 and nxt_closes)
        if full or (len(cur) >= 2 and (re.search(r'[.!?…:;,]$', w) or gap > 0.35)) or nxt is None:
            chunks.append(cur); cur = []
    if cur:
        chunks.append(cur)
    subs = []
    for c in chunks:
        text = ' '.join(sw[i][0] for i in c)
        text = re.sub(r'\s+([:;!?»])', ' \\1', text)            # espaces insécables françaises
        text = re.sub(r'[.!?…]+$', '', text).rstrip(' ,:; ').strip()
        subs.append([offset + times[c[0]][0], offset + times[c[-1]][1] + 0.12, text])
    for i in range(len(subs) - 1):
        subs[i][1] = min(subs[i][1], subs[i + 1][0] - 0.02)
    return subs
