import sys, json
from faster_whisper import WhisperModel
m = WhisperModel("small", device="cpu", compute_type="int8")
for f in sys.argv[1:]:
    import subprocess, numpy as np
    a=np.frombuffer(subprocess.run(["ffmpeg","-v","error","-i",f,"-ac","1","-ar","16000","-f","s16le","-"],capture_output=True).stdout,np.int16).astype(np.float32)/32768
    segs, _ = m.transcribe(a, language="fr", word_timestamps=True)
    words=[]
    for s in segs:
        for w in s.words: words.append([round(w.start,2), round(w.end,2), w.word.strip()])
    json.dump(words, open(f.replace('.mp3','.words.json'),'w'), ensure_ascii=False)
    print(f, len(words)); print(' '.join(f"{w[2]}@{w[0]}" for w in words))
