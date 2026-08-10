#!/usr/bin/env python3
"""Génère la console de production : une page par épisode, filtrable par saison.

Tout ce qu'il faut pour produire un épisode sur un seul écran : le script HeyGen
à copier, le lien du chapitre Drive à filmer, le prompt Higgsfield du hook.
"""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
eps = json.loads((ROOT / "content" / "episodes.json").read_text(encoding="utf-8"))
hf = json.loads((ROOT / "content" / "prompts-higgsfield.json").read_text(encoding="utf-8"))
dm = json.loads((ROOT / "content" / "drive-map.json").read_text(encoding="utf-8"))
hooks = json.loads((ROOT / "content" / "hooks-higgsfield.json").read_text(encoding="utf-8"))

data = []
for e in eps["episodes"]:
    eid = f"EP{e['n']:03d}"
    d = dm.get(eid, {})
    data.append({
        "id": eid,
        "n": e["n"],
        "s": (e["n"] - 1) // 30 + 1,
        "t": e["t"],
        "mod": e["mod"],
        "ch": d.get("chapitre_drive") or e["ch"],
        "sur": d.get("chapitre_drive") is not None,
        "url": d.get("url", ""),
        "hook": e["hook"],
        "punch": e["punch"],
        "heygen": e["heygen"],
        "hf": hf.get(eid, ""),
        "rendu": eid in hooks,
    })

PAGE = """<title>FoodEatUp — console de production des 150 épisodes</title>
<style>
:root{
  --ground:#F7F3E4; --surface:#FFFDF7; --raised:#FBF7EA;
  --ink:#14202B; --ink-2:#3E5060; --muted:#6B7C89;
  --line:#E2DAC2; --line-2:#EFE8D4;
  --accent:#0A5FD0; --accent-soft:#E4EDFB;
  --flag:#B45905; --flag-soft:#FBEEDC;
  --ok:#1F7A4C; --ok-soft:#E3F1E9;
  --shadow:0 1px 2px rgba(20,32,43,.06),0 8px 24px -16px rgba(20,32,43,.28);
}
@media (prefers-color-scheme:dark){
  :root:not([data-theme="light"]){
    --ground:#0F1820; --surface:#16222C; --raised:#1B2933;
    --ink:#E9EEF2; --ink-2:#B3C1CC; --muted:#8296A4;
    --line:#26363F; --line-2:#1F2E37;
    --accent:#5AA2FF; --accent-soft:#12304F;
    --flag:#F0A24A; --flag-soft:#3A2A15;
    --ok:#5FCB93; --ok-soft:#14332A;
    --shadow:0 1px 2px rgba(0,0,0,.4),0 10px 28px -18px rgba(0,0,0,.7);
  }
}
:root[data-theme="dark"]{
  --ground:#0F1820; --surface:#16222C; --raised:#1B2933;
  --ink:#E9EEF2; --ink-2:#B3C1CC; --muted:#8296A4;
  --line:#26363F; --line-2:#1F2E37;
  --accent:#5AA2FF; --accent-soft:#12304F;
  --flag:#F0A24A; --flag-soft:#3A2A15;
  --ok:#5FCB93; --ok-soft:#14332A;
  --shadow:0 1px 2px rgba(0,0,0,.4),0 10px 28px -18px rgba(0,0,0,.7);
}
*{box-sizing:border-box}
body{
  margin:0; background:var(--ground); color:var(--ink);
  font-family:ui-sans-serif,system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;
  font-size:15px; line-height:1.55; -webkit-font-smoothing:antialiased;
}
.wrap{max-width:1180px;margin:0 auto;padding:32px 20px 96px}
header{margin-bottom:26px}
h1{font-size:26px;line-height:1.2;margin:0 0 6px;letter-spacing:-.02em;text-wrap:balance;font-weight:650}
.sub{color:var(--muted);font-size:14px;margin:0;max-width:64ch}
.stats{display:flex;flex-wrap:wrap;gap:8px;margin-top:16px}
.stat{background:var(--surface);border:1px solid var(--line);border-radius:8px;
  padding:7px 12px;font-size:12.5px;color:var(--ink-2);font-variant-numeric:tabular-nums}
.stat b{color:var(--ink);font-weight:640}

.controls{position:sticky;top:0;z-index:5;background:var(--ground);
  padding:12px 0;margin-bottom:14px;border-bottom:1px solid var(--line);
  display:flex;gap:10px;flex-wrap:wrap;align-items:center}
.seg{display:flex;gap:2px;background:var(--raised);border:1px solid var(--line);
  border-radius:9px;padding:3px}
.seg button{appearance:none;border:0;background:transparent;color:var(--ink-2);
  font:inherit;font-size:13px;padding:6px 13px;border-radius:6px;cursor:pointer}
.seg button:hover{color:var(--ink)}
.seg button[aria-pressed="true"]{background:var(--accent);color:#fff;font-weight:600}
.seg button:focus-visible,input:focus-visible,.copy:focus-visible,
.drive:focus-visible,summary:focus-visible{outline:2px solid var(--accent);outline-offset:2px}
input[type="search"]{flex:1;min-width:200px;background:var(--surface);color:var(--ink);
  border:1px solid var(--line);border-radius:9px;padding:9px 13px;font:inherit;font-size:14px}
input[type="search"]::placeholder{color:var(--muted)}

.list{display:flex;flex-direction:column;gap:12px}
.ep{background:var(--surface);border:1px solid var(--line);border-radius:12px;
  padding:18px 20px;box-shadow:var(--shadow);border-left:3px solid transparent;
  transition:border-color .18s,background .18s}
.ep.done{border-left-color:var(--ok);background:var(--ok-soft)}
.ep.done .ttl{color:var(--ok)}
.ep.done .script,.ep.done pre{background:var(--surface)}
.tick{display:flex;align-items:center;gap:8px;cursor:pointer;user-select:none;
  font-size:12px;letter-spacing:.04em;text-transform:uppercase;color:var(--muted);
  font-weight:640;white-space:nowrap}
.tick input{appearance:none;width:19px;height:19px;margin:0;flex:none;cursor:pointer;
  border:1.5px solid var(--line);border-radius:5px;background:var(--raised);
  display:grid;place-content:center}
.tick input:checked{background:var(--ok);border-color:var(--ok)}
.tick input:checked::after{content:"";width:5px;height:9px;border:solid #fff;
  border-width:0 2px 2px 0;transform:rotate(45deg) translate(-1px,-1px)}
.tick input:focus-visible{outline:2px solid var(--accent);outline-offset:2px}
.ep.done .tick{color:var(--ok)}
.bar{height:5px;border-radius:3px;background:var(--line-2);overflow:hidden;
  margin-top:12px;max-width:420px}
.bar i{display:block;height:100%;background:var(--ok);border-radius:3px;
  transition:width .3s}
.ep-head{display:flex;gap:12px;align-items:baseline;flex-wrap:wrap;margin-bottom:4px}
.num{font-variant-numeric:tabular-nums;font-weight:680;font-size:13px;color:var(--accent);
  background:var(--accent-soft);border-radius:6px;padding:3px 8px;letter-spacing:.01em}
.ttl{font-size:17px;font-weight:620;letter-spacing:-.01em;margin:0}
.chips{display:flex;gap:6px;flex-wrap:wrap;margin-left:auto}
.chip{font-size:11.5px;letter-spacing:.03em;text-transform:uppercase;
  color:var(--muted);border:1px solid var(--line);border-radius:20px;padding:3px 9px}
.chip.ok{color:var(--ok);border-color:var(--ok);background:var(--ok-soft)}
.chip.flag{color:var(--flag);border-color:var(--flag);background:var(--flag-soft);text-transform:none}

.path{font-size:13px;color:var(--muted);margin:2px 0 14px}
.path b{color:var(--ink-2);font-weight:560}

.block{margin-top:12px}
.lab{display:flex;align-items:center;gap:8px;margin-bottom:6px}
.lab span{font-size:11px;letter-spacing:.09em;text-transform:uppercase;color:var(--muted);font-weight:640}
.copy{margin-left:auto;appearance:none;font:inherit;font-size:12px;cursor:pointer;
  background:var(--raised);color:var(--ink-2);border:1px solid var(--line);
  border-radius:7px;padding:4px 11px}
.copy:hover{color:var(--ink);border-color:var(--accent)}
.copy[data-done="1"]{color:var(--ok);border-color:var(--ok);background:var(--ok-soft)}
.script{background:var(--raised);border:1px solid var(--line-2);border-left:3px solid var(--accent);
  border-radius:0 8px 8px 0;padding:12px 15px;font-size:15px;line-height:1.6}
.mini{display:flex;gap:22px;flex-wrap:wrap;margin-top:12px}
.mini div{min-width:180px;flex:1}
.mini p{margin:0;font-size:14px;color:var(--ink-2)}
.drive{display:inline-flex;align-items:center;gap:7px;text-decoration:none;
  background:var(--accent);color:#fff;font-size:13.5px;font-weight:560;
  border-radius:8px;padding:8px 14px;margin-top:4px}
.drive:hover{filter:brightness(1.08)}
.drive.pale{background:var(--flag-soft);color:var(--flag);border:1px solid var(--flag)}
details{margin-top:12px;border-top:1px solid var(--line-2);padding-top:10px}
summary{cursor:pointer;font-size:12.5px;color:var(--muted);list-style:none;
  display:flex;align-items:center;gap:7px}
summary::-webkit-details-marker{display:none}
summary::before{content:"›";display:inline-block;transition:transform .15s}
details[open] summary::before{transform:rotate(90deg)}
summary:hover{color:var(--ink-2)}
pre{margin:10px 0 0;background:var(--raised);border:1px solid var(--line-2);border-radius:8px;
  padding:13px 15px;overflow-x:auto;font-family:ui-monospace,SFMono-Regular,Menlo,monospace;
  font-size:12.5px;line-height:1.65;color:var(--ink-2);white-space:pre-wrap;word-break:break-word}
.empty{text-align:center;color:var(--muted);padding:64px 0;font-size:15px}
@media (prefers-reduced-motion:reduce){*{transition:none!important}}
@media (max-width:640px){
  .wrap{padding:22px 14px 72px} h1{font-size:22px}
  .chips{margin-left:0;width:100%} .ep{padding:15px 16px}
}
</style>

<div class="wrap">
<header>
  <h1>Console de production — 150 épisodes FoodEatUp</h1>
  <p class="sub">Pour chaque épisode : le script que dit l'avatar, le chapitre Drive à
  filmer, et le prompt du hook. Tout est copiable d'un clic.</p>
  <div class="stats" id="stats"></div>
</header>

<div class="controls">
  <div class="seg" id="seasons" role="group" aria-label="Filtrer par saison"></div>
  <input type="search" id="q" placeholder="Chercher un titre, un module, un mot du script…"
         aria-label="Rechercher un épisode">
  <div class="seg"><button type="button" id="restants" aria-pressed="false">Reste à faire</button></div>
</div>

<div class="list" id="list"></div>
<p class="empty" id="empty" hidden>Aucun épisode ne correspond.</p>
</div>

<script type="application/json" id="data">__DATA__</script>
<script>
const EPS = JSON.parse(document.getElementById('data').textContent);
const list = document.getElementById('list');
const empty = document.getElementById('empty');
let saison = 0, q = '', restants = false;

// L'avancement vit dans le navigateur : rien à sauvegarder, rien à synchroniser.
const CLE = 'foodeatup-episodes-montes';
let done = new Set();
try { done = new Set(JSON.parse(localStorage.getItem(CLE) || '[]')); } catch {}
const sauver = () => {
  try { localStorage.setItem(CLE, JSON.stringify([...done])); } catch {}
};

const esc = s => s.replace(/[&<>"]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));

function stats() {
  const n = done.size, pct = Math.round(n / EPS.length * 100);
  document.getElementById('stats').innerHTML = [
    [`${n} / ${EPS.length}`, 'épisodes montés'],
    [EPS.filter(e => e.sur).length, 'chapitres Drive résolus'],
    [EPS.filter(e => e.rendu).length, 'hooks déjà générés']
  ].map(([v, l]) => `<div class="stat"><b>${v}</b> ${l}</div>`).join('')
   + `<div class="bar" role="img" aria-label="${pct}% des épisodes montés"><i style="width:${pct}%"></i></div>`;
}
stats();

const seg = document.getElementById('seasons');
seg.innerHTML = ['Toutes', 1, 2, 3, 4, 5].map((l, i) =>
  `<button type="button" data-s="${i}" aria-pressed="${i === 0}">${i ? 'Saison ' + l : l}</button>`
).join('');
seg.addEventListener('click', e => {
  const b = e.target.closest('button'); if (!b) return;
  saison = +b.dataset.s;
  [...seg.children].forEach(x => x.setAttribute('aria-pressed', x === b));
  render();
});
document.getElementById('q').addEventListener('input', e => {
  q = e.target.value.toLowerCase().trim(); render();
});
document.getElementById('restants').addEventListener('click', e => {
  restants = !restants;
  e.target.setAttribute('aria-pressed', restants);
  render();
});

// Cocher n'entraîne pas de re-rendu : la carte se colore sur place, sinon on
// perdrait le prompt qu'on vient d'ouvrir juste au-dessus.
document.addEventListener('change', e => {
  const c = e.target.closest('input[data-done]'); if (!c) return;
  const id = c.dataset.done;
  c.checked ? done.add(id) : done.delete(id);
  sauver();
  document.querySelector(`[data-ep="${id}"]`).classList.toggle('done', c.checked);
  stats();
});

function card(e) {
  const drive = e.url
    ? `<a class="drive ${e.sur ? '' : 'pale'}" href="${e.url}" target="_blank" rel="noopener">
         ${e.sur ? 'Ouvrir le chapitre Drive' : 'Ouvrir le module (chapitre à confirmer)'}</a>`
    : '';
  return `<article class="ep ${done.has(e.id) ? 'done' : ''}" data-ep="${e.id}">
    <div class="ep-head">
      <span class="num">${e.id}</span>
      <h2 class="ttl">${esc(e.t)}</h2>
      <div class="chips">
        <label class="tick" title="Marquer l'épisode comme monté">
          <input type="checkbox" data-done="${e.id}" ${done.has(e.id) ? 'checked' : ''}>
          Monté</label>
        <span class="chip">Saison ${e.s}</span>
        ${e.rendu ? '<span class="chip ok">hook généré</span>' : ''}
        ${e.sur ? '' : '<span class="chip flag">chapitre à confirmer</span>'}
      </div>
    </div>
    <p class="path"><b>${esc(e.mod)}</b> › ${esc(e.ch)}</p>

    <div class="block">
      <div class="lab"><span>Script de la voix HeyGen</span>
        <button class="copy" type="button" data-copy="hg-${e.id}">Copier</button></div>
      <div class="script" id="hg-${e.id}">${esc(e.heygen)}</div>
    </div>

    <div class="mini">
      <div><div class="lab"><span>Hook incrusté · 0,8 → 3,5 s</span></div>
        <p>${esc(e.hook)}</p></div>
      <div><div class="lab"><span>Punchline VO · 5,0 s</span></div>
        <p>${esc(e.punch)}</p></div>
    </div>

    <div class="block">${drive}</div>

    <details>
      <summary>Prompt Higgsfield du hook</summary>
      <div class="lab" style="margin-top:10px">
        <span>À générer depuis l'interface Higgsfield</span>
        <button class="copy" type="button" data-copy="hf-${e.id}">Copier</button></div>
      <pre id="hf-${e.id}">${esc(e.hf)}</pre>
    </details>
  </article>`;
}

function render() {
  const vis = EPS.filter(e =>
    (!saison || e.s === saison) &&
    (!restants || !done.has(e.id)) &&
    (!q || (e.t + ' ' + e.mod + ' ' + e.ch + ' ' + e.heygen + ' ' + e.hook + ' ' +
            e.punch + ' ' + e.id).toLowerCase().includes(q)));
  list.innerHTML = vis.map(card).join('');
  empty.hidden = vis.length > 0;
}

document.addEventListener('click', async e => {
  const b = e.target.closest('.copy'); if (!b) return;
  const src = document.getElementById(b.dataset.copy);
  try {
    await navigator.clipboard.writeText(src.textContent);
    b.textContent = 'Copié'; b.dataset.done = '1';
    setTimeout(() => { b.textContent = 'Copier'; delete b.dataset.done; }, 1600);
  } catch { b.textContent = 'Sélectionne et copie'; }
});

render();
</script>
"""

out = ROOT / "console.html"
out.write_text(PAGE.replace("__DATA__", json.dumps(data, ensure_ascii=False)), encoding="utf-8")
print(f"{out.name} — {out.stat().st_size // 1024} Ko, {len(data)} épisodes")
