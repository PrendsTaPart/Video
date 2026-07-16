#!/usr/bin/env python3
"""
Générateur d'avatars parlants HeyGen — API REST v3 (api.heygen.com/v3, header x-api-key).
Débloque la génération d'avatars RÉELS (Avatar IV) côté CLI : les outils MCP compose/render_video
sont désactivés pour ce type de client, mais l'API REST v3 fonctionne dès qu'une clé est fournie.

Clé : HEYGEN_API_KEY dans studio-video/.env  (ou variable d'environnement).

Pipelines :
  1) TEXTE   : POST /v3/videos (avatar_id + script + voice_id, Avatar IV) -> mp4 (voix HeyGen)
  2) LIPSYNC : /v3/videos (base) puis /v3/lipsyncs sur notre audio ElevenLabs -> mp4 (NOTRE voix)

Usage :
  python3 heygen_avatar.py check                         # vérifie la clé + crédits + liste voix FR
  python3 heygen_avatar.py upload <fichier>              # upload un asset -> asset_id
  python3 heygen_avatar.py video  <avatar_id> <voice_id> "<script>" [out.mp4] [16:9|9:16]
  python3 heygen_avatar.py lipsync <video_url_or_asset> <audio_mp3> [out.mp4]   # relip sur NOTRE VO
"""
import os, sys, json, time, urllib.request, urllib.error, mimetypes, uuid

BASE = "https://api.heygen.com/v3"

def key():
    k = os.environ.get("HEYGEN_API_KEY")
    if not k:
        env = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env")
        if os.path.exists(env):
            for ln in open(env):
                if ln.strip().startswith("HEYGEN_API_KEY="):
                    k = ln.strip().split("=", 1)[1].strip().strip('"')
    if not k:
        sys.exit("HEYGEN_API_KEY manquante (studio-video/.env ou variable d'environnement).")
    return k

def req(method, path, body=None, headers=None):
    url = path if path.startswith("http") else BASE + path
    h = {"x-api-key": key(), "Accept": "application/json"}
    data = None
    if body is not None:
        data = json.dumps(body).encode(); h["Content-Type"] = "application/json"
    if headers: h.update(headers)
    r = urllib.request.Request(url, data=data, headers=h, method=method)
    try:
        with urllib.request.urlopen(r, timeout=120) as resp:
            return json.loads(resp.read().decode())
    except urllib.error.HTTPError as e:
        sys.exit(f"HTTP {e.code} {method} {url}\n{e.read().decode()[:800]}")

def upload(path):
    """POST /v3/assets — multipart. Retourne (asset_id, url)."""
    boundary = "----hg" + uuid.uuid4().hex
    fn = os.path.basename(path); ct = mimetypes.guess_type(path)[0] or "application/octet-stream"
    body = b"".join([
        f"--{boundary}\r\n".encode(),
        f'Content-Disposition: form-data; name="file"; filename="{fn}"\r\n'.encode(),
        f"Content-Type: {ct}\r\n\r\n".encode(),
        open(path, "rb").read(), b"\r\n",
        f"--{boundary}--\r\n".encode(),
    ])
    r = urllib.request.Request(BASE + "/assets", data=body, method="POST",
        headers={"x-api-key": key(), "Content-Type": f"multipart/form-data; boundary={boundary}"})
    with urllib.request.urlopen(r, timeout=300) as resp:
        d = json.loads(resp.read().decode())["data"]
    return d["asset_id"], d.get("url")

def poll(getter, id_, label, done=("completed",), fail=("failed",), every=6, tries=200):
    for _ in range(tries):
        d = getter(id_).get("data", {})
        st = d.get("status")
        print(f"  {label} {id_} -> {st}")
        if st in done: return d
        if st in fail: sys.exit(f"{label} échoué: {json.dumps(d)[:400]}")
        time.sleep(every)
    sys.exit(f"{label} timeout")

def create_video(avatar_id, voice_id, script, aspect="16:9", resolution="720p", engine="avatar_iii"):
    # avatar_iii/720p = économe (tient dans les petits budgets de crédits API) ; avatar_iv/1080p = premium, coûteux
    d = req("POST", "/videos", {
        "type": "avatar", "avatar_id": avatar_id, "script": script, "voice_id": voice_id,
        "resolution": resolution, "aspect_ratio": aspect, "engine": {"type": engine},
    })
    return d["data"]["video_id"] if "data" in d else d.get("video_id")

def get_video(vid): return req("GET", f"/videos/{vid}")

def create_lipsync(video_ref, audio_ref, mode="precision"):
    def ref(x):
        return {"type": "asset_id", "asset_id": x} if x.startswith(("ast", "asset")) else {"type": "url", "url": x}
    d = req("POST", "/lipsyncs", {"video": ref(video_ref), "audio": ref(audio_ref), "mode": mode, "title": "predibot"})
    return d["data"]["lipsync_id"] if "data" in d else d.get("lipsync_id")

def get_lipsync(lid): return req("GET", f"/lipsyncs/{lid}")

def download(url, out):
    urllib.request.urlretrieve(url, out); print("  -> saved", out)

def cmd_check():
    q = req("GET", "https://api.heygen.com/v2/user/remaining_quota").get("data", {})
    det = q.get("details", {})
    print(f"Crédits — API : {det.get('api','?')}  |  plan (app web) : {det.get('plan_credit','?')}")
    print("  ⚠️ La génération API consomme les crédits 'api' (pas les crédits 'plan').")
    v = req("GET", "https://api.heygen.com/v2/voices", None)
    voices = v.get("data", {}).get("voices", [])
    fr = [x for x in voices if "french" in str(x.get("language", "")).lower()][:8]
    print("Voix FR (échantillon) :")
    for x in fr: print("  ", x.get("voice_id"), "-", x.get("name"), x.get("gender"))
    print("Astuce : GET /v3/avatars/looks -> un look_id sert d'avatar_id pour /v3/videos.")

def main():
    a = sys.argv[1:]
    if not a or a[0] == "check": return cmd_check()
    if a[0] == "upload":
        aid, url = upload(a[1]); print("asset_id:", aid, "\nurl:", url); return
    if a[0] == "video":
        avatar_id, voice_id, script = a[1], a[2], a[3]
        out = a[4] if len(a) > 4 else "heygen_out.mp4"; aspect = a[5] if len(a) > 5 else "16:9"
        vid = create_video(avatar_id, voice_id, script, aspect); print("video_id:", vid)
        d = poll(get_video, vid, "video"); download(d["video_url"], out); return
    if a[0] == "lipsync":
        video_ref, audio = a[1], a[2]; out = a[3] if len(a) > 3 else "heygen_lipsync.mp4"
        # audio local -> upload d'abord
        if os.path.exists(audio): audio, _ = upload(audio)
        lid = create_lipsync(video_ref, audio); print("lipsync_id:", lid)
        d = poll(get_lipsync, lid, "lipsync"); download(d.get("video_url") or d.get("url"), out); return
    sys.exit(__doc__)

if __name__ == "__main__":
    main()
