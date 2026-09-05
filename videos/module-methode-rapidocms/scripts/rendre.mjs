// Rend la queue animée d'un épisode : transition « COUPEZ », méthode, hook de fin.
// Appelé par le script de chaque épisode, qui lui passe son contexte.
//
// Les visuels de la méthode et de l'orchestration sont les mêmes d'un épisode à l'autre ;
// seuls le numéro de séquence, le titre sur l'ardoise et la punchline de fin changent.
// C'est pour ces trois-là qu'on rend la queue par épisode plutôt qu'une fois pour toutes.
import { readFileSync, writeFileSync, rmSync, mkdirSync } from "node:fs";
import { join } from "node:path";

export const MODULE = join(import.meta.dirname, "..");

/* Simple Icons livre des tracés monochromes sans couleur : on pose celle de la marque
   sur le SVG plutôt que de le redessiner. */
const teinter = (source, couleur) => source.replace("<svg ", `<svg fill="${couleur}" `);

export function donneesAnimation({ EP, logosDir, charte }) {
  const b64 = (rel, mime) => `data:${mime};base64,${readFileSync(join(logosDir, rel)).toString("base64")}`;
  const svg = (rel) => readFileSync(join(logosDir, rel), "utf8");
  const svgUri = (rel, couleur) =>
    "data:image/svg+xml;base64," + Buffer.from(teinter(svg(rel), couleur)).toString("base64");

  const Q = EP.queue;
  const t0 = Q.debut_s;
  const rel = (s) => +(s - t0).toFixed(4);            // temps absolu → temps local au module

  const creneaux = Q.lignes.filter((l) => l.ecran === "etape")
    .map((l) => ({ debut_s: rel(l.debut_s), fin_s: rel(l.fin_s) }));
  if (creneaux.length !== Q.etapes.length) {
    throw new Error(`${creneaux.length} créneaux de voix off pour ${Q.etapes.length} cartes d'étape.`);
  }
  const ouverture = Q.lignes.find((l) => l.ecran === "ouverture");
  if (!ouverture) throw new Error("aucune ligne d'ouverture dans queue.lignes.");

  return {
    fps: EP.format.fps,
    frames: Math.round((Q.fin_s - Q.debut_s) * EP.format.fps),
    duree_s: Q.fin_s - Q.debut_s,
    blocs: {
      transition: [rel(Q.blocs.transition.debut_s), rel(Q.blocs.transition.fin_s)],
      methode: [rel(Q.blocs.methode.debut_s), rel(Q.blocs.methode.fin_s)],
      hook: [rel(Q.blocs.hook.debut_s), rel(Q.blocs.hook.fin_s)],
    },
    sequence: Q.blocs.transition.sequence,
    titre_episode: EP.titre.toUpperCase(),
    ouverture: { debut_s: rel(ouverture.debut_s), fin_s: rel(ouverture.fin_s) },
    etapes: Q.etapes,
    creneaux,
    orchestration: {
      ...Q.orchestration,
      debut_s: rel(Q.orchestration.debut_s),
      reseaux_debut_s: rel(Q.orchestration.reseaux_debut_s),
    },
    hook: Q.blocs.hook,
    logos: {
      rapidocms: b64("rapidocms.png", "image/png"),
      higgsfield: b64("higgsfield.png", "image/png"),
      heygen: b64("heygen.png", "image/png"),
      claude: svgUri("claude.svg", "#D97757"),
      elevenlabs: svgUri("elevenlabs.svg", "#000000"),
    },
    reseaux_svg: Object.fromEntries(Q.orchestration.reseaux.map((n) => [n, svg(`${n}.svg`)])),
    couleurs_reseaux: charte.reseaux,
  };
}

export async function rendre({ donnees, work, sortie, chromium, chrome, ff, apercus = null }) {
  const images = join(work, "queue-images");
  const page_html = join(work, "queue.html");
  mkdirSync(work, { recursive: true });
  writeFileSync(page_html, readFileSync(join(MODULE, "animation.html"), "utf8")
    .replace("__DATA__", JSON.stringify(donnees)));

  const navigateur = await chromium.launch({ executablePath: chrome, args: ["--no-sandbox", "--force-device-scale-factor=1"] });
  const page = await navigateur.newPage({ viewport: { width: 1080, height: 1920 }, deviceScaleFactor: 1 });
  const erreurs = [];
  page.on("pageerror", (e) => erreurs.push(String(e)));
  await page.goto("file://" + page_html);
  await page.evaluate(() => document.fonts.ready);
  if (erreurs.length) throw new Error(`la page de la queue lève une erreur : ${erreurs.join(" | ")}`);

  if (apercus) {
    const faits = [];
    for (const t of apercus) {
      await page.evaluate((i) => window.seek(i), Math.round(t * donnees.fps));
      const f = join(work, `apercu-${String(t).replace(".", "s")}.png`);
      await page.screenshot({ path: f });
      faits.push(f);
    }
    await navigateur.close();
    return faits;
  }

  rmSync(images, { recursive: true, force: true });
  mkdirSync(images, { recursive: true });
  for (let f = 0; f < donnees.frames; f++) {
    await page.evaluate((i) => window.seek(i), f);
    await page.screenshot({ path: join(images, `f${String(f).padStart(4, "0")}.png`) });
    if (f % 120 === 0) process.stdout.write(`   ${f}/${donnees.frames}\n`);
  }
  if (erreurs.length) throw new Error(`la page de la queue a levé une erreur pendant le rendu : ${erreurs.join(" | ")}`);
  await navigateur.close();

  ff(["-framerate", String(donnees.fps), "-i", join(images, "f%04d.png"),
      "-c:v", "libx264", "-preset", "slow", "-crf", "16", "-pix_fmt", "yuv420p", sortie]);
  return sortie;
}
