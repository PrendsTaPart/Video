// Suit un objet de couleur franche dans le bas de l'image, pour y coller l'incrustation
// de l'annonceur. Sert à tous les épisodes dont le produit porte un repère colorimétrique
// net — la bouteille de sauce, le sceau de cire. Sur un objet sombre et mat, il n'y a rien
// à suivre : le relevé se fait alors à l'œil et s'écrit à la main dans episode.json.
import { readFileSync, rmSync, mkdirSync, existsSync } from "node:fs";
import { join } from "node:path";

/* Un percentile plutôt qu'un extremum : une main, un reflet ou un bout de tissu de la même
   teinte ne doivent pas étirer la boîte jusqu'au bord du cadre. */
const q = (arr, p) => { const a = [...arr].sort((u, v) => u - v); return a[Math.floor((a.length - 1) * p)]; };

export async function suivreCouleur({
  clip, instants, decalage_s = 0, work, L, H,
  bande = [0.55, 1.0],           // la portion verticale où chercher
  teinte = "rouge",              // rouge | orange
  min_pixels = 2500,
  tolerance_taille = 1.6,   // au-delà, la boîte a avalé autre chose que l'objet
  chromium, chrome, ff, sonder, s2,
}) {
  const dir = join(work, "suivi");
  rmSync(dir, { recursive: true, force: true });
  mkdirSync(dir, { recursive: true });

  const infos = sonder(clip);
  const derniere = infos.duree_s - 2 / (infos.fps || 30);

  const nav = await chromium.launch({ executablePath: chrome, args: ["--no-sandbox"] });
  const page = await nav.newPage({ viewport: { width: 400, height: 300 } });
  const releves = [];
  let reference = null;

  for (const t of instants) {
    const dans = Math.min(t - decalage_s, derniere);
    const f = join(dir, `t${String(t).replace(".", "_")}.png`);
    ff(["-ss", s2(dans), "-i", clip, "-frames:v", "1", "-vf", `scale=${L}:${H}:flags=lanczos`, f]);
    if (!existsSync(f)) throw new Error(`aucune image extraite à ${dans.toFixed(3)} s de ${clip}.`);

    const boite = await page.evaluate(async ({ uri, L, H, bande, teinte }) => {
      const img = new Image(); img.src = uri; await img.decode();
      const c = document.createElement("canvas"); c.width = L; c.height = H;
      const ctx = c.getContext("2d", { willReadFrequently: true });
      ctx.drawImage(img, 0, 0);
      const y0 = Math.round(H * bande[0]), y1 = Math.round(H * bande[1]);
      const d = ctx.getImageData(0, y0, L, y1 - y0).data;
      const xs = [], ys = [];
      for (let i = 0; i < d.length; i += 4) {
        const r = d[i], g = d[i + 1], b = d[i + 2];
        const mx = Math.max(r, g, b), mn = Math.min(r, g, b);
        const sat = mx === 0 ? 0 : (mx - mn) / mx;
        const rouge = r > 95 && r > g * 1.9 && r > b * 1.9 && sat > 0.5;
        const orange = r > 105 && r > g * 1.55 && r > b * 1.55 && sat > 0.45;
        if (teinte === "rouge" ? rouge : orange) {
          const p = i / 4; xs.push(p % L); ys.push(y0 + Math.floor(p / L));
        }
      }
      return { n: xs.length, xs, ys };
    }, { uri: "data:image/png;base64," + readFileSync(f).toString("base64"), L, H, bande, teinte });

    if (boite.n < min_pixels) { releves.push({ t_s: t, trouve: false, motif: "trop peu de pixels", pixels: boite.n }); continue; }
    const xmin = q(boite.xs, 0.02), xmax = q(boite.xs, 0.98);
    const ymin = q(boite.ys, 0.02), ymax = q(boite.ys, 0.98);
    const l = xmax - xmin, h = ymax - ymin;

    /* Le décor peut porter la même teinte que l'objet — ici la braise du brasero, qui
       finit par occuper tout l'établi. Une boîte qui enfle brusquement n'est plus l'objet :
       la première détection valable donne la taille de référence, les suivantes doivent
       s'y tenir. Mieux vaut un relevé plus court qu'un suivi qui part dans le décor. */
    /* On juge sur la largeur seule : c'est elle qui trahit l'emballement. La hauteur, elle,
       grandit légitimement quand la lumière chaude descend le long de l'objet. */
    if (reference === null) reference = { l, h };
    const derive = l / reference.l;
    if (derive > tolerance_taille) {
      releves.push({ t_s: t, trouve: false, motif: `boîte ${l}×${h}, ${derive.toFixed(1)}× la taille de référence`, pixels: boite.n });
      continue;
    }
    releves.push({ t_s: t, trouve: true, pixels: boite.n, x: xmin, y: ymin, l, h });
  }
  await nav.close();
  return releves;
}
