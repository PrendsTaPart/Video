import sys, json, subprocess, numpy as np
from faster_whisper import WhisperModel
m = WhisperModel("small", compute_type="int8")
out = {}
for f in sys.argv[1:]:
    r = subprocess.run(["ffmpeg", "-v", "error", "-i", f, "-f", "s16le", "-ac", "1", "-ar", "16000", "-"], capture_output=True).stdout
    segs, _ = m.transcribe(np.frombuffer(r, np.int16).astype(np.float32) / 32768, language="fr", word_timestamps=True)
    S = [(round(s.start, 2), round(s.end, 2), s.text.strip()) for s in segs]
    out[f] = S
    print("==", f)
    for s in S: print(s)
json.dump(out, open("transcriptions.json", "w"), ensure_ascii=False, indent=1)
