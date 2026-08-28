/**
 * Analyse spectrale de la voix en cours de lecture.
 *
 * Le moteur d'avatar expose un `AnalyserNode` branché sur la voix. On y lit
 * l'énergie image par image, puis on la lisse (attaque rapide, relâchement plus
 * lent) pour éviter le tremblement.
 *
 * ## Pourquoi trois bandes plutôt qu'un RMS
 *
 * Un RMS large bande mesure un **volume**, pas une **articulation** : un « sss »
 * et un « aaa » de même intensité donnent le même chiffre, donc la même
 * ouverture de mâchoire — alors que l'un se prononce dents presque serrées et
 * l'autre bouche grande ouverte.
 *
 * On sépare donc le spectre en trois :
 *
 * | Bande  | Plage        | Ce qu'elle indique                                  |
 * | ------ | ------------ | --------------------------------------------------- |
 * | grave  | 80–350 Hz    | voisement (vibration des cordes vocales), F0         |
 * | médium | 350 Hz–2 kHz | formants F1/F2 : **indice de voyelle ouverte**       |
 * | aigu   | 2–6 kHz      | bruit de friction (s, ch, f)                         |
 *
 * Le ratio aigu/grave donne un **indice de fricative** : élevé sur un « sss »
 * (beaucoup d'aigu, peu de voisement), bas sur une voyelle. Il sert à brider
 * l'ouverture de mâchoire. L'énergie médium sert d'indice de voyelle ouverte et
 * pilote l'amplitude.
 *
 * La FFT passe à 512 points : à 48 kHz, 93,75 Hz par bin au lieu de 187,5 —
 * indispensable pour isoler proprement une bande qui démarre à 80 Hz.
 */

/** Taille de FFT attendue sur l'analyseur (résolution ~94 Hz à 48 kHz). */
export const FFT_SIZE = 512;

/** Bornes des trois bandes, en hertz. */
const BANDS = {
  low: [80, 350],
  mid: [350, 2000],
  high: [2000, 6000],
} as const;

/** Lissage : montée rapide, descente plus douce. */
const ATTACK = 0.55;
const RELEASE = 0.16;

/** En dessous de ce niveau, on considère qu'il n'y a pas de voix. */
export const SILENCE_LEVEL = 0.06;

/** Indices spectraux d'une image d'analyse. */
export interface VoiceBands {
  /** Énergie 80–350 Hz, 0..1. */
  low: number;
  /** Énergie 350 Hz–2 kHz, 0..1 — indice de voyelle ouverte. */
  mid: number;
  /** Énergie 2–6 kHz, 0..1. */
  high: number;
  /** Niveau global lissé, 0..1. */
  level: number;
  /** Ratio aigu/grave normalisé, 0..1 — indice de fricative. */
  fricative: number;
  /** Ouverture attendue de la bouche, 0..1 — dérivée du médium. */
  openness: number;
}

export interface VoiceEnvelope {
  /** Met à jour l'enveloppe depuis l'analyseur et renvoie les indices lissés. */
  read: (analyser: AnalyserNode | null | undefined) => VoiceBands;
  /** Derniers indices, sans relecture de l'analyseur. */
  readonly bands: VoiceBands;
  /** Dernier niveau global lissé. */
  readonly level: number;
  /** Vrai sur une attaque marquée (accentuation de la voix). */
  readonly accent: boolean;
  /** Retour progressif à zéro (fin de réplique, coupure). */
  decay: () => VoiceBands;
  reset: () => void;
}

const clamp01 = (x: number) => (x < 0 ? 0 : x > 1 ? 1 : x);

/** Énergie moyenne d'une plage de fréquences, 0..1. */
function bandEnergy(data: Uint8Array, from: number, to: number, hzPerBin: number): number {
  const start = Math.max(0, Math.floor(from / hzPerBin));
  const end = Math.min(data.length - 1, Math.ceil(to / hzPerBin));
  let sum = 0;
  let n = 0;
  for (let i = start; i <= end; i++) {
    const v = (data[i] ?? 0) / 255;
    sum += v * v;
    n++;
  }
  return n > 0 ? Math.sqrt(sum / n) : 0;
}

const EMPTY: VoiceBands = {
  low: 0,
  mid: 0,
  high: 0,
  level: 0,
  fricative: 0,
  openness: 0,
};

export function createVoiceEnvelope(): VoiceEnvelope {
  let low = 0;
  let mid = 0;
  let high = 0;
  let level = 0;
  let accent = false;
  let data: Uint8Array | null = null;

  /** Lissage asymétrique : la voix monte vite et retombe doucement. */
  const smooth = (current: number, target: number) =>
    current + (target - current) * (target > current ? ATTACK : RELEASE);

  const snapshot = (): VoiceBands => {
    // Fricative : beaucoup d'aigu pour peu de voisement. Le +0.05 évite une
    // division explosive quand tout est proche de zéro.
    const fricative = clamp01(high / (low + high + 0.05) - 0.25) / 0.75;
    // Ouverture : portée par le médium, un peu soutenue par le grave.
    const openness = clamp01(mid * 1.25 + low * 0.35);
    return { low, mid, high, level, fricative: clamp01(fricative), openness };
  };

  return {
    read(analyser) {
      if (!analyser) return this.decay();
      // La FFT du moteur CDN est réglée sur 256 : on l'élargit une fois.
      if (analyser.fftSize !== FFT_SIZE) {
        try {
          analyser.fftSize = FFT_SIZE;
        } catch {
          /* certains navigateurs refusent après démarrage : on garde la valeur en place */
        }
      }
      if (!data || data.length !== analyser.frequencyBinCount) {
        data = new Uint8Array(analyser.frequencyBinCount);
      }
      // @ts-expect-error -- signatures ArrayBuffer/ArrayBufferLike divergentes selon la lib DOM.
      analyser.getByteFrequencyData(data);

      const sampleRate = analyser.context?.sampleRate ?? 48000;
      const hzPerBin = sampleRate / (analyser.frequencyBinCount * 2);

      low = smooth(low, bandEnergy(data, BANDS.low[0], BANDS.low[1], hzPerBin));
      mid = smooth(mid, bandEnergy(data, BANDS.mid[0], BANDS.mid[1], hzPerBin));
      high = smooth(high, bandEnergy(data, BANDS.high[0], BANDS.high[1], hzPerBin));

      // Niveau global : dominé par le médium, là où porte la voix.
      const raw = clamp01(Math.max(low * 0.8, mid, high * 0.7));
      const shaped = clamp01((raw - 0.05) / 0.55) ** 0.8;
      accent = shaped - level > 0.12;
      level = smooth(level, shaped);

      return snapshot();
    },

    get bands() {
      return snapshot();
    },
    get level() {
      return level;
    },
    get accent() {
      return accent;
    },

    decay() {
      accent = false;
      low *= 0.82;
      mid *= 0.82;
      high *= 0.82;
      level *= 0.82;
      if (level < 0.005) {
        low = mid = high = level = 0;
        return EMPTY;
      }
      return snapshot();
    },

    reset() {
      low = mid = high = level = 0;
      accent = false;
    },
  };
}

/** Prochain intervalle (ms) entre deux clignements naturels. */
export function nextBlinkDelay(): number {
  return 2200 + Math.random() * 3800;
}
