// Les contrôles de la série, partagés par les épisodes : format, durée, niveau sonore,
// la coupe franche, l'accent, les sous-titres, et la structure des soixante secondes.
import { existsSync } from "node:fs";
import { join } from "node:path";
import { spawnSync } from "node:child_process";

export function verifier({ EP, ROOT, OUT, FFMPEG, sonder, s2, log = console.log }) {
  const A = EP.audio, Q = EP.queue, F = EP.film;
  const { largeur: L, hauteur: H, fps: FPS } = EP.format;
  const ecarts = [];
  const dit = (ok, texte) => { log(`   ${ok ? "✅" : "❌"} ${texte}`); if (!ok) ecarts.push(texte); };

  const lufs = (f) => {
    const r = spawnSync(FFMPEG, ["-hide_banner", "-i", f, "-af", "ebur128=framelog=quiet", "-f", "null", "-"],
      { encoding: "utf8", maxBuffer: 32 * 1024 * 1024 });
    const m = /I:\s+(-?[\d.]+) LUFS/.exec(r.stderr || "");
    return m ? parseFloat(m[1]) : null;
  };
  /* Un noir encodé en yuv420p à plage réduite ne mesure pas 0 mais ~7 sur 255 : le seuil
     est là pour distinguer le noir de l'image, pas pour compter les bits. */
  const NOIR = 12;
  const luminance = (f, t) => {
    const r = spawnSync(FFMPEG, ["-hide_banner", "-loglevel", "info", "-ss", s2(t), "-i", f, "-frames:v", "1",
      "-vf", "scale=64:64,format=gray,signalstats,metadata=print:key=lavfi.signalstats.YAVG", "-f", "null", "-"],
      { encoding: "utf8", maxBuffer: 32 * 1024 * 1024 });
    const m = /lavfi\.signalstats\.YAVG=([\d.]+)/.exec(r.stderr || "");
    return m ? parseFloat(m[1]) : null;
  };
  const compterNoir = (f, t0, attendu) => {
    const mesures = [];
    for (let k = -1; k <= attendu + 2; k++) mesures.push({ k, y: luminance(f, t0 + k / FPS) });
    const noires = mesures.filter((m) => m.y !== null && m.y < NOIR).map((m) => m.k);
    const suite = noires.length && noires[noires.length - 1] - noires[0] + 1 === noires.length;
    return { noires, suite, mesures };
  };

  log("── La structure ──");
  const total = EP.format.duree_s;
  dit(F.fin_s - F.debut_s === 30, `bloc film : ${F.fin_s - F.debut_s} s (règle de la série : 30)`);
  dit(Q.blocs.transition.fin_s - Q.blocs.transition.debut_s === 3, `transition « COUPEZ » : ${Q.blocs.transition.fin_s - Q.blocs.transition.debut_s} s (3)`);
  dit(Q.blocs.methode.fin_s - Q.blocs.methode.debut_s === 20, `méthode : ${Q.blocs.methode.fin_s - Q.blocs.methode.debut_s} s (20)`);
  dit(Q.blocs.hook.fin_s - Q.blocs.hook.debut_s === 7, `hook de fin : ${Q.blocs.hook.fin_s - Q.blocs.hook.debut_s} s (7)`);
  dit(Q.fin_s === total && total === 60, `total : ${total} s (60)`);
  const trous = [];
  const bl = [Q.blocs.transition, Q.blocs.methode, Q.blocs.hook];
  for (let i = 0; i < bl.length - 1; i++) if (bl[i].fin_s !== bl[i + 1].debut_s) trous.push(i);
  dit(trous.length === 0 && F.fin_s === Q.debut_s, `les blocs s'enchaînent sans trou ni recouvrement`);

  log("\n── Les exports ──");
  for (const ex of EP.exports) {
    const f = join(OUT, ex.fichier);
    if (!existsSync(f)) { dit(false, `${ex.fichier} : absent`); continue; }
    const i = sonder(f);
    const attendue = ex.a_s - ex.de_s;
    dit(Math.abs(i.duree_s - attendue) < 0.05, `${ex.fichier} : ${i.duree_s} s (attendu ${attendue})`);
    dit(i.largeur === L && i.hauteur === H && Math.abs(i.fps - FPS) < 0.1, `${ex.fichier} : ${i.largeur}×${i.hauteur} · ${i.fps} ips`);
    const niveau = lufs(f);
    dit(niveau !== null && Math.abs(niveau - A.lufs) <= 1.5, `${ex.fichier} : ${niveau} LUFS (visé ${A.lufs} ± 1,5)`);
  }

  const complet = join(OUT, EP.exports[0].fichier);
  if (existsSync(complet)) {
    log("\n── La coupe franche à 30 s ──");
    const r = compterNoir(complet, F.fin_s, F.coupe_finale.noir_images);
    dit(r.noires.length === F.coupe_finale.noir_images && r.suite,
        `${r.noires.length} image(s) de noir plein d'affilée (attendu ${F.coupe_finale.noir_images})`);
    dit(r.mesures.find((m) => m.k === 0)?.y > 20, `image de film jusqu'à ${F.fin_s} s inclus`);

    if (F.accent) {
      log("\n── L'accent du bloc film ──");
      const a = compterNoir(complet, F.accent.t_s, F.accent.noir_images);
      dit(a.noires.length === F.accent.noir_images && a.suite,
          `${a.noires.length} image(s) de noir à ${F.accent.t_s} s (attendu ${F.accent.noir_images})`);
      dit(a.mesures.find((m) => m.k === F.accent.noir_images + 1)?.y > 20, `l'image revient juste après`);
    }
  }

  log("\n── Les sources ──");
  for (const c of F.clips) {
    const f = join(ROOT, c.fichier);
    const i = existsSync(f) ? sonder(f) : null;
    dit(!!i && Math.abs(i.duree_s - 10) < 0.1, `${c.fichier} : ${i ? i.duree_s + " s" : "absent"} (plan ${c.higgsfield.slice(0, 8)})`);
  }

  log("\n── Les sous-titres ──");
  for (const [i, st] of F.sous_titres.entries()) {
    const mots = st.lignes.map((l) => l.trim().split(/\s+/).length);
    dit(st.lignes.length <= 2 && Math.max(...mots) <= 7, `sous-titre ${i + 1} : ${st.lignes.length} ligne(s), ${mots.join("/")} mot(s)`);
  }

  log("\n── Le produit de l'annonceur ──");
  const IP = F.incrustation_produit;
  if (existsSync(join(ROOT, IP.fichier))) {
    const hors = IP.suivi.filter((p) => p.x < 0 || p.y < 0 || p.x + p.l > L || p.y + p.h > H);
    dit(hors.length === 0, `suivi dans le cadre sur les ${IP.suivi.length} points relevés`);
  } else {
    log(`   ○ aucune marque fournie : ${IP.quoi} reste vierge, rien n'est incrusté (c'est le plan de montage).`);
  }

  log(ecarts.length === 0 ? "\n✅ Aucun écart." : `\n❌ ${ecarts.length} écart(s).`);
  return ecarts;
}
