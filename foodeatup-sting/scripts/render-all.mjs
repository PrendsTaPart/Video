// Rend les cinq livrables du sting dans /out.
// Séquentiel : Chromium prend toute la machine, deux rendus en parallèle sont
// plus lents que l'un après l'autre.
import { execFileSync } from "node:child_process";
import { fileURLToPath } from "node:url";
import path from "node:path";

const RACINE = path.dirname(path.dirname(fileURLToPath(import.meta.url)));
const ENTREE = "src/index.ts";

const livrables = [
  { id: "sting-1080x1920", fichier: "out/sting-1080x1920.mp4", args: ["--codec=h264", "--crf=18"] },
  { id: "sting-1920x1080", fichier: "out/sting-1920x1080.mp4", args: ["--codec=h264", "--crf=18"] },
  { id: "sting-1080x1080", fichier: "out/sting-1080x1080.mp4", args: ["--codec=h264", "--crf=18"] },
  { id: "sting-loop-3s", fichier: "out/sting-loop-3s.mp4", args: ["--codec=h264", "--crf=18"] },
];

for (const l of livrables) {
  process.stdout.write(`\n=== ${l.id} -> ${l.fichier}\n`);
  execFileSync("npx", ["remotion", "render", ENTREE, l.id, l.fichier, ...l.args], {
    cwd: RACINE,
    stdio: "inherit",
    env: { ...process.env, PLAYWRIGHT_BROWSERS_PATH: "/opt/pw-browsers" },
  });
}

// L'alpha passe par une séquence PNG : le muxeur webm de Remotion écrit un
// yuv420p sans couche alpha, alors que les PNG rendus la portent bien. On
// réencode donc en VP9 avec -auto-alt-ref 0, obligatoire pour l'alpha VP9.
process.stdout.write("\n=== sting-alpha -> out/sting-alpha.webm\n");
const seq = path.join(RACINE, ".tmp-alpha");
execFileSync("rm", ["-rf", seq]);
execFileSync("npx", ["remotion", "render", ENTREE, "sting-alpha", seq, "--sequence", "--image-format=png"], {
  cwd: RACINE, stdio: "inherit",
  env: { ...process.env, PLAYWRIGHT_BROWSERS_PATH: "/opt/pw-browsers" },
});
execFileSync("ffmpeg", [
  "-v", "error",
  "-framerate", "30", "-i", path.join(seq, "element-%03d.png"),
  "-i", path.join(RACINE, "public", "sting-lit.wav"),
  "-i", path.join(RACINE, "public", "sting-vo.mp3"),
  "-filter_complex", "[1:a]volume=0.5[b];[2:a]volume=1[v];[b][v]amix=inputs=2:duration=first:normalize=0[a]",
  "-map", "0:v", "-map", "[a]", "-t", "5",
  "-c:v", "libvpx-vp9", "-pix_fmt", "yuva420p", "-auto-alt-ref", "0", "-crf", "20", "-b:v", "0",
  "-c:a", "libopus", "-b:a", "128k",
  path.join(RACINE, "out", "sting-alpha.webm"), "-y",
], { stdio: "inherit" });
execFileSync("rm", ["-rf", seq]);

console.log("\nles cinq livrables sont dans out/");
