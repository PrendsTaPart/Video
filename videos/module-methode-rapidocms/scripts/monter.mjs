// Le montage, partagé par les épisodes de la série : bloc film (30 s) + queue animée (30 s),
// audio mixé, exports et vignette. Ne génère aucune vidéo — les plans viennent de source/.
import { existsSync, writeFileSync, readFileSync, rmSync, mkdirSync } from "node:fs";
import { join } from "node:path";
import { spawnSync } from "node:child_process";

export const MODULE = join(import.meta.dirname, "..");

/* L'accroche et les sous-titres sont fixes pendant leur créneau : une image PNG chacun,
   posée par ffmpeg au bon moment, plutôt que neuf cents images de plus à rendre. */
async function incrustations({ EP, ROOT, work, chromium, chrome, y }) {
  const F = EP.film;
  const dir = join(work, "incrustations");
  rmSync(dir, { recursive: true, force: true });
  mkdirSync(dir, { recursive: true });

  const page_html = join(work, "incrustations.html");
  writeFileSync(page_html, readFileSync(join(MODULE, "incrustations.html"), "utf8"));
  const nav = await chromium.launch({ executablePath: chrome, args: ["--no-sandbox", "--force-device-scale-factor=1"] });
  const page = await nav.newPage({ viewport: { width: EP.format.largeur, height: EP.format.hauteur }, deviceScaleFactor: 1 });
  await page.goto("file://" + page_html);
  await page.evaluate(() => document.fonts.ready);

  const faites = [];
  await page.evaluate((a) => window.montrer(a), { type: "accroche", ...F.accroche, y: y.accroche });
  const fa = join(dir, "accroche.png");
  await page.screenshot({ path: fa, omitBackground: true });
  faites.push({ fichier: fa, debut_s: F.accroche.debut_s, fin_s: F.accroche.fin_s });

  for (const [i, st] of F.sous_titres.entries()) {
    if (st.lignes.length > 2) throw new Error(`sous-titre ${i + 1} : ${st.lignes.length} lignes, deux au maximum.`);
    for (const ligne of st.lignes) {
      const mots = ligne.trim().split(/\s+/).length;
      if (mots > 7) throw new Error(`sous-titre ${i + 1} : « ${ligne} » fait ${mots} mots, sept au maximum.`);
    }
    await page.evaluate((s) => window.montrer(s), { type: "soustitre", lignes: st.lignes, y: y.soustitre });
    const f = join(dir, `st${i + 1}.png`);
    await page.screenshot({ path: f, omitBackground: true });
    faites.push({ fichier: f, debut_s: st.debut_s, fin_s: st.fin_s });
  }
  await nav.close();
  return faites;
}

export async function monter({ EP, ROOT, WORK, OUT, chromium, chrome, ff, sonder, s2, y, FFMPEG, log = console.log }) {
  const F = EP.film, Q = EP.queue, A = EP.audio;
  const { largeur: L, hauteur: H, fps: FPS } = EP.format;
  const QUEUE_MUETTE = join(WORK, "queue-muette.mp4");
  const VO = join(ROOT, "audio", "vo-queue.wav");
  const NAPPE = join(ROOT, A.nappe);

  for (const [quoi, c] of [["la queue animée", QUEUE_MUETTE], ["la voix off de la queue", VO], ["la nappe", NAPPE]]) {
    if (!existsSync(c)) throw new Error(`manque ${quoi} : ${c} — lancer npm run queue d'abord.`);
  }
  mkdirSync(OUT, { recursive: true });

  /* Le niveau : on mesure, on corrige, on vérifie. loudnorm — même en deux passes — rate
     sa cible de plusieurs décibels sur ces extraits. Une mesure EBU R128 suivie d'un gain
     fixe est exacte, et le limiteur garde le vrai crête sous −1,5 dBTP. */
  const mesurerLufs = (fichier) => {
    const r = spawnSync(FFMPEG, ["-hide_banner", "-i", fichier, "-af", "ebur128=framelog=quiet", "-f", "null", "-"],
      { encoding: "utf8", maxBuffer: 32 * 1024 * 1024 });
    const m = /I:\s+(-?[\d.]+) LUFS/.exec(r.stderr || "");
    if (!m) throw new Error(`impossible de mesurer le niveau de ${fichier}.`);
    return parseFloat(m[1]);
  };

  /* Les deux blocs ne sortent pas du tout au même niveau : le film vient de Higgsfield,
     très bas, la queue est mixée ici. Les caler chacun sur la cible AVANT de les coller
     est la seule façon d'avoir un film entier au bon niveau — normaliser l'assemblage
     ne ferait que déshabiller l'un pour habiller l'autre. */
  const caler = (fichier, quoi) => {
    const mesure = mesurerLufs(fichier);
    const gain = A.lufs - mesure;
    const cale = fichier.replace(/\.mp4$/, "-cale.mp4");
    ff(["-i", fichier, "-af", `volume=${gain.toFixed(2)}dB,alimiter=limit=0.841:level=disabled`,
        "-c:v", "copy", "-c:a", "aac", "-b:a", "256k", "-ar", "48000", cale]);
    log(`   ${quoi} : ${mesure.toFixed(1)} → ${mesurerLufs(cale).toFixed(1)} LUFS (${gain >= 0 ? "+" : ""}${gain.toFixed(1)} dB)`);
    return cale;
  };

  const incrusts = await incrustations({ EP, ROOT, work: WORK, chromium, chrome, y });

  /* ── le produit de l'annonceur ── */
  const IP = F.incrustation_produit;
  const produit = existsSync(join(ROOT, IP.fichier)) ? join(ROOT, IP.fichier) : null;
  if (!produit) log(`   ${IP.quoi} : aucune marque fournie, rien n'est incrusté.`);

  /* ── le bloc film ── */
  const chaine = [];
  F.clips.forEach((_, i) => {
    chaine.push(`[${i}:v]scale=${L}:${H}:flags=lanczos,fps=${FPS},setsar=1,format=yuv420p[c${i}]`);
  });
  chaine.push(`${F.clips.map((_, i) => `[c${i}][${i}:a]`).join("")}concat=n=${F.clips.length}:v=1:a=1[fv][fa]`);

  let courant = "fv";
  incrusts.forEach((inc, k) => {
    const src = F.clips.length + k;
    chaine.push(`[${courant}][${src}:v]overlay=0:0:enable='between(t,${s2(inc.debut_s)},${s2(inc.fin_s)})':format=auto[o${k}]`);
    courant = `o${k}`;
  });

  if (produit) {
    const src = F.clips.length + incrusts.length;
    const p = IP.suivi;
    const interp = (champ) => {
      const bouts = [];
      for (let i = 0; i < p.length - 1; i++) {
        const [a, b] = [p[i], p[i + 1]];
        const pente = (b[champ] - a[champ]) / (b.t_s - a.t_s);
        bouts.push(`if(lt(t,${s2(b.t_s)}), ${a[champ]}+(t-${s2(a.t_s)})*${pente.toFixed(4)}`);
      }
      return bouts.join(", ") + `, ${p[p.length - 1][champ]}` + ")".repeat(p.length - 1);
    };
    const fenetre = `enable='between(t,${s2(IP.debut_s)},${s2(IP.fin_s)})'`;
    if (IP.relief) {
      /* « pressé dans la cire, pas posé dessus » : une copie sombre et floue décalée de
         quelques pixels fait le creux, et l'emblème lui-même passe à l'opacité réduite pour
         que la matière du support continue de se lire à travers. */
      const D = 5;
      chaine.push(`[${src}:v]scale=${p[0].l}:${p[0].h},split=2[pr1][pr2]`);
      chaine.push(`[pr1]format=rgba,colorchannelmixer=rr=0:gg=0:bb=0:aa=0.55,gblur=sigma=3[ombre]`);
      chaine.push(`[pr2]format=rgba,colorchannelmixer=aa=0.82[embleme]`);
      chaine.push(`[${courant}][ombre]overlay=x='(${interp("x")})+${D}':y='(${interp("y")})+${D}':${fenetre}[oomb]`);
      chaine.push(`[oomb][embleme]overlay=x='${interp("x")}':y='${interp("y")}':${fenetre}[oprod]`);
    } else {
      chaine.push(`[${src}:v]scale=${p[0].l}:${p[0].h}[prod]`);
      chaine.push(`[${courant}][prod]overlay=x='${interp("x")}':y='${interp("y")}':${fenetre}[oprod]`);
    }
    courant = "oprod";
  }

  /* L'accent, quand l'épisode en a un : quelques images de noir sur un point du son.
     Le son n'est pas touché — c'est tout l'effet, l'image saute et le son continue. */
  if (F.accent) {
    const fin = F.accent.t_s + F.accent.noir_images / FPS - 1 / (FPS * 2);
    chaine.push(`[${courant}]drawbox=x=0:y=0:w=${L}:h=${H}:color=black@1:t=fill:enable='between(t,${s2(F.accent.t_s)},${s2(fin)})'[vfilm]`);
  } else {
    chaine.push(`[${courant}]null[vfilm]`);
  }

  const FILM = join(WORK, "film.mp4");
  ff([...F.clips.flatMap((c) => ["-i", join(ROOT, c.fichier)]),
      ...incrusts.flatMap((i) => ["-loop", "1", "-i", i.fichier]),
      ...(produit ? ["-loop", "1", "-i", produit] : []),
      "-filter_complex", chaine.join(";"),
      "-map", "[vfilm]", "-map", "[fa]", "-t", s2(F.fin_s - F.debut_s),
      "-c:v", "libx264", "-preset", "slow", "-crf", "17", "-pix_fmt", "yuv420p",
      "-c:a", "aac", "-b:a", "256k", "-ar", "48000", FILM]);
  log(`✅ bloc film — ${sonder(FILM).duree_s} s`);
  const FILM_CALE = caler(FILM, "niveau du film");

  /* ── la queue : le rendu muet + voix + nappe + les SFX du clap ── */
  const noir_s = F.coupe_finale.noir_images / FPS;
  const dureeQueue = Q.fin_s - Q.debut_s;
  const nappeDecalage = A.nappe_queue_debut_s - Q.debut_s;
  const clapT = Q.blocs.transition.clap_s - Q.debut_s;

  const QUEUE = join(WORK, "queue.mp4");
  ff(["-i", QUEUE_MUETTE, "-i", VO, "-i", NAPPE,
      "-i", join(MODULE, "sfx", "whoosh.mp3"), "-i", join(MODULE, "sfx", "clap.mp3"),
      "-filter_complex", [
        `[0:v]drawbox=x=0:y=0:w=${L}:h=${H}:color=black@1:t=fill:enable='lt(t,${s2(noir_s)})'[qv]`,
        // l'ardoise qui monte, puis le claquement
        `[3:a]adelay=${Math.round(0.10 * 1000)}:all=1,volume=0.5[wh]`,
        `[4:a]adelay=${Math.round(clapT * 1000)}:all=1,volume=0.9[cl]`,
        // la nappe démarre après la transition, sous la voix
        `[2:a]atrim=0:${s2(dureeQueue - nappeDecalage)},asetpts=PTS-STARTPTS,` +
          `adelay=${Math.round(nappeDecalage * 1000)}:all=1,volume=0.22,` +
          `afade=t=in:st=${s2(nappeDecalage)}:d=0.4[nappe]`,
        `[nappe][1:a]sidechaincompress=threshold=0.03:ratio=6:attack=12:release=280:makeup=1[duck]`,
        `[duck][1:a][wh][cl]amix=inputs=4:normalize=0:dropout_transition=0[qa]`,
      ].join(";"),
      "-map", "[qv]", "-map", "[qa]", "-t", s2(dureeQueue),
      "-c:v", "libx264", "-preset", "slow", "-crf", "17", "-pix_fmt", "yuv420p",
      "-c:a", "aac", "-b:a", "256k", "-ar", "48000", QUEUE]);
  log(`✅ queue animée — ${sonder(QUEUE).duree_s} s`);
  const QUEUE_CALE = caler(QUEUE, "niveau de la queue");

  /* ── les exports ── */
  const liste = join(WORK, "blocs.txt");
  writeFileSync(liste, [FILM_CALE, QUEUE_CALE].map((f) => `file '${f}'`).join("\n") + "\n");
  const COMPLET = join(WORK, "complet.mp4");
  ff(["-f", "concat", "-safe", "0", "-i", liste, "-c", "copy", COMPLET]);

  for (const ex of EP.exports) {
    const duree = ex.a_s - ex.de_s;
    const sortie = join(OUT, ex.fichier);
    const fondu = A.fondu_sortie_s;
    ff(["-ss", s2(ex.de_s), "-i", COMPLET, "-t", s2(duree),
        "-af", `afade=t=out:st=${s2(duree - fondu)}:d=${fondu}`,
        "-c:v", "libx264", "-preset", "slow", "-crf", "18", "-pix_fmt", "yuv420p",
        "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-movflags", "+faststart", sortie]);
    const i = sonder(sortie);
    log(`✅ ${ex.fichier} — ${i.duree_s} s · ${i.largeur}×${i.hauteur} · ${i.fps} ips · ${mesurerLufs(sortie).toFixed(1)} LUFS`);
  }

  const vignette = join(OUT, EP.vignette.fichier);
  ff(["-ss", s2(EP.vignette.t_s), "-i", COMPLET, "-frames:v", "1", "-q:v", "2", vignette]);
  log(`✅ ${EP.vignette.fichier} — image à ${EP.vignette.t_s} s`);
  return COMPLET;
}
