#!/usr/bin/env python3
"""Regroupe les répliques en lots ElevenLabs, puis redécoupe les lots en fichiers par réplique.

    python3 bd-video/scripts/vo_batches.py plan            # écrit audio/vo_batches.json
    python3 bd-video/scripts/vo_batches.py split           # audio/vo_raw/<lot>.mp3 → audio/vo/<id>.mp3

Pourquoi des lots : chaque fichier généré n'est téléchargeable que par une URL signée ; un lot par
voix et par partie (≈ 60 au lieu de 236) garde le téléchargement praticable. Les répliques d'un lot
sont séparées par une longue pause ([long pause]) ; le découpage cherche les N-1 plus longs silences.
"""
import json
import os
import re
import subprocess
import sys

ROOT = os.path.join(subprocess.check_output(["git", "rev-parse", "--show-toplevel"], text=True).strip(), "bd-video")
MAX_CHARS = 2400
SEP = " [long pause] "


def plan():
    manifest = json.load(open(os.path.join(ROOT, "audio", "vo_manifest.json")))
    parts = {s["id"]: s["part"] for s in json.load(open(os.path.join(ROOT, "storyboard.json")))}
    batches = {}
    order = []
    for m in manifest:
        key = (parts[m["id"]], m["cast"])
        if key not in batches:
            batches[key] = [[]]
            order.append(key)
        cur = batches[key][-1]
        if cur and sum(len(x["tts_text"]) + len(SEP) for x in cur) + len(m["tts_text"]) > MAX_CHARS:
            batches[key].append([])
            cur = batches[key][-1]
        cur.append(m)
    out = []
    for key in order:
        for k, lines in enumerate(batches[key]):
            part, cast = key
            pnum = re.match(r"(Partie \d|Prologue|Épilogue)", part)
            tag = (pnum.group(1) if pnum else part).lower().replace("partie ", "p").replace("é", "e")
            bid = f"{tag}-{cast}-{k+1}"
            out.append({"batch": bid, "voice_id": lines[0]["voice_id"], "cast": cast, "model_id": lines[0]["model_id"],
                        "ids": [x["id"] for x in lines], "prompt": SEP.join(x["tts_text"] for x in lines)})
    json.dump(out, open(os.path.join(ROOT, "audio", "vo_batches.json"), "w"), ensure_ascii=False, indent=1)
    print(f"{len(out)} lots · {sum(len(b['prompt']) for b in out)} caractères")


def norm(t):
    t = re.sub(r"\[[^\]]*\]", " ", t.lower())
    return re.sub(r"[^a-z0-9àâäçéèêëîïôöùûüœ]+", "", t)


_model = None


def words(raw):
    """Mots horodatés (faster-whisper, local) ; mis en cache à côté du lot."""
    global _model
    cache = raw.replace(".mp3", ".words.json")
    if os.path.exists(cache):
        return json.load(open(cache))
    if _model is None:
        from faster_whisper import WhisperModel
        _model = WhisperModel("small", device="cpu", compute_type="int8")
    segs, _ = _model.transcribe(raw, language="fr", word_timestamps=True)
    out = [[w.start, w.end, w.word] for s in segs for w in s.words]
    json.dump(out, open(cache, "w"), ensure_ascii=False)
    return out


def duration(path):
    return float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", path],
                                capture_output=True, text=True).stdout)


def cut_points(raw, texts):
    """Instant de coupure entre chaque réplique : alignement texte attendu ↔ transcription (difflib)."""
    from difflib import SequenceMatcher
    ws = words(raw)
    tr, owner = "", []
    for i, (_, _, w) in enumerate(ws):
        n = norm(w)
        tr += n
        owner += [i] * len(n)
    exp, bounds = "", []
    for t in texts:
        exp += norm(t)
        bounds.append(len(exp))
    sm = SequenceMatcher(None, exp, tr, autojunk=False)
    mapping = {}
    for a, b, size in sm.get_matching_blocks():
        for k in range(size):
            mapping[a + k] = b + k
    cuts = []
    for bnd in bounds[:-1]:
        # dernier caractère de la réplique k retrouvé dans la transcription
        j = next((mapping[c] for c in range(bnd - 1, -1, -1) if c in mapping), None)
        if j is None:
            return None
        wi = owner[j]
        nxt = wi + 1
        while nxt < len(ws) and not norm(ws[nxt][2]):
            nxt += 1
        end_prev = ws[wi][1]
        start_next = ws[nxt][0] if nxt < len(ws) else end_prev + 0.3
        cuts.append((end_prev + start_next) / 2 if start_next > end_prev else end_prev)
    return cuts


def split():
    batches = json.load(open(os.path.join(ROOT, "audio", "vo_batches.json")))
    texts = {m["id"]: m["text"] for m in json.load(open(os.path.join(ROOT, "audio", "vo_manifest.json")))}
    os.makedirs(os.path.join(ROOT, "audio", "vo"), exist_ok=True)
    report = []
    only = set(sys.argv[2:])
    for b in batches:
        raw = os.path.join(ROOT, "audio", "vo_raw", f"{b['batch']}.mp3")
        if not os.path.exists(raw) or (only and b["batch"] not in only):
            continue
        total = duration(raw)
        cuts = cut_points(raw, [texts[i] for i in b["ids"]]) if len(b["ids"]) > 1 else []
        if cuts is None:
            report.append(f"⚠ {b['batch']} : alignement impossible")
            continue
        bounds = [0.0] + cuts + [total]
        for i, sid in enumerate(b["ids"]):
            a, c = bounds[i], bounds[i + 1]
            out = os.path.join(ROOT, "audio", "vo", f"{sid}.mp3")
            subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", f"{a:.3f}", "-to", f"{c:.3f}", "-i", raw,
                            "-af", "silenceremove=start_periods=1:start_threshold=-50dB,areverse,"
                                   "silenceremove=start_periods=1:start_threshold=-50dB,areverse,"
                                   "afade=t=in:d=0.02,apad=pad_dur=0.08", "-c:a", "libmp3lame", "-b:a", "160k", out], check=True)
            d = duration(out)
            rate = len(texts[sid]) / max(d, 0.1)
            flag = " ⚠ débit anormal" if rate < 7 or rate > 24 else ""
            report.append(f"{sid}\t{d:5.2f}s\t{rate:4.1f} car/s{flag}\t{b['batch']}")
    path = os.path.join(ROOT, "audio", "vo_split_report.txt")
    old = open(path).read().splitlines() if os.path.exists(path) and only else []
    keep = [l for l in old if l.split("\t")[-1] not in only]
    open(path, "w").write("\n".join(keep + report) + "\n")
    print("\n".join(r for r in report if "⚠" in r) or "découpage sans alerte")
    print(f"{len(os.listdir(os.path.join(ROOT, 'audio', 'vo')))} fichiers dans audio/vo/")


if __name__ == "__main__":
    {"plan": plan, "split": split}[sys.argv[1]]()
