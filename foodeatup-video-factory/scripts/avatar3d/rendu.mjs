import { chromium } from "playwright-core";
import fs from "node:fs";
const piste = JSON.parse(fs.readFileSync("visemes-EP001.json", "utf8"));
fs.mkdirSync("images", { recursive: true });
const nav = await chromium.launch({executablePath:"/opt/pw-browsers/chromium-1194/chrome-linux/chrome",
  args:["--use-gl=swiftshader","--enable-unsafe-swiftshader","--no-sandbox"]});
const page = await nav.newPage({viewport:{width:1080,height:1920}});
await page.goto("http://127.0.0.1:8811/scene.html?fond=../../assets/fond-cuisine.jpg");
  await page.waitForTimeout(1500);
await page.waitForFunction("window.pret === true",{timeout:90000});
const t0 = Date.now();
for (let i = 0; i < piste.images.length; i++) {
  const f = piste.images[i];
  await page.evaluate(`poser(${JSON.stringify(f.m)}, ${JSON.stringify(f.os)})`);
  await page.screenshot({ path: `images/f${String(i).padStart(4,"0")}.png` });
  if (i % 40 === 0) console.log(`  ${i}/${piste.images.length}  ${((Date.now()-t0)/1000).toFixed(0)}s`);
}
await nav.close();
console.log(`${piste.images.length} images en ${((Date.now()-t0)/1000).toFixed(0)}s`);
