from faster_whisper import WhisperModel
import json
m = WhisperModel("medium", device="cpu", compute_type="int8")
segs, info = m.transcribe("audio/le-clash.mp3", language="fr", word_timestamps=True,
                          vad_filter=False, beam_size=5)
out = []
for s in segs:
    out.append({"start": round(s.start,3), "end": round(s.end,3), "text": s.text.strip(),
                "words": [{"w": w.word, "s": round(w.start,3), "e": round(w.end,3)} for w in (s.words or [])]})
    print(f"[{s.start:7.2f} -> {s.end:7.2f}] {s.text.strip()}", flush=True)
json.dump(out, open("work/transcript.json","w"), ensure_ascii=False, indent=1)
print("DONE", len(out))
