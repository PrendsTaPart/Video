// Fabrique le lit sonore du sting : nappe basse, whoosh du tracé, impact de
// fermeture. Tout est synthétisé par ffmpeg — aucune banque de sons, aucun
// crédit, et le résultat est identique d'une machine à l'autre.
import { execFileSync } from "node:child_process";
import { fileURLToPath } from "node:url";
import path from "node:path";

const RACINE = path.dirname(path.dirname(fileURLToPath(import.meta.url)));
const SORTIE = path.join(RACINE, "public", "sting-lit.wav");

const DUREE = 5;
const IMPACT = 2.4;   // fermeture de la boucle
const TRACE = [0.4, 2.4];

const filtres = [
  // nappe : deux basses désaccordées, respiration lente, jamais au premier plan
  `[0:a]volume=0.42,tremolo=f=0.35:d=0.22[nappe1]`,
  `[1:a]volume=0.24[nappe2]`,
  `[nappe1][nappe2]amix=inputs=2:normalize=0[nappe]`,

  // whoosh : bruit filtré dont la bande monte pendant que le point parcourt le
  // tracé, puis retombe. Le volume suit la même courbe.
  `[2:a]highpass=f=320,lowpass=f=5200,` +
    `volume='if(between(t,${TRACE[0]},${TRACE[1]}),` +
    `0.16*sin(3.14159*(t-${TRACE[0]})/${TRACE[1] - TRACE[0]}),0)':eval=frame[whoosh]`,

  // impact : sinus grave qui claque et décroît vite, doublé d'un souffle court
  `[3:a]volume='if(between(t,${IMPACT},${IMPACT + 0.9}),0.95*exp(-7*(t-${IMPACT})),0)':eval=frame[boum]`,
  `[4:a]highpass=f=900,volume='if(between(t,${IMPACT},${IMPACT + 0.25}),0.30*exp(-16*(t-${IMPACT})),0)':eval=frame[souffle]`,

  `[nappe][whoosh][boum][souffle]amix=inputs=4:duration=first:normalize=0,` +
    `afade=t=in:st=0:d=0.25,afade=t=out:st=${DUREE - 0.35}:d=0.35,` +
    `alimiter=limit=0.89[out]`,
].join(";");

execFileSync("ffmpeg", [
  "-v", "error",
  "-f", "lavfi", "-i", `sine=frequency=55:duration=${DUREE}:sample_rate=44100`,
  "-f", "lavfi", "-i", `sine=frequency=82.5:duration=${DUREE}:sample_rate=44100`,
  "-f", "lavfi", "-i", `anoisesrc=duration=${DUREE}:color=brown:amplitude=0.6:sample_rate=44100`,
  "-f", "lavfi", "-i", `sine=frequency=58:duration=${DUREE}:sample_rate=44100`,
  "-f", "lavfi", "-i", `anoisesrc=duration=${DUREE}:color=white:amplitude=0.5:sample_rate=44100`,
  "-filter_complex", filtres,
  "-map", "[out]", "-t", String(DUREE),
  "-c:a", "pcm_s16le", "-ar", "44100", "-ac", "2",
  SORTIE, "-y",
], { stdio: "inherit" });

console.log(`lit sonore -> public/sting-lit.wav (${DUREE}s)`);
