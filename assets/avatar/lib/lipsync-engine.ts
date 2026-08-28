/**
 * Moteur de synchro labiale — **seul point d'écriture sur les morphs de la bouche**.
 *
 * ## Pourquoi
 *
 * La bouche était pilotée par deux systèmes qui se contredisaient : TalkingHead
 * écrivait ses visèmes sur son canal interne, pendant que la boucle rAF écrivait
 * `jawOpen` sur le canal `fixed`. Or `fixed` est prioritaire sur tout le reste
 * (`fixed` > `realtime` > `system` > animation > baseline) : l'énergie RMS
 * écrasait donc les fermetures nettes que la piste de visèmes venait de poser.
 * Une bilabiale /p/ était articulée par le moteur puis immédiatement rouverte
 * par le niveau audio.
 *
 * Ici, un seul écrivain. Le moteur CDN ne touche plus à la bouche (on lui passe
 * `visemes: []`, tableau vide mais défini : il saute sa propre dérivation
 * mot → visème sans rien écrire), et tout passe par ce module.
 *
 * ## Hiérarchie
 *
 * - La **piste de visèmes** décide de la FORME de la bouche. Elle vient du
 *   graphème → phonème français, donc de l'alignement caractère exact.
 * - L'**analyse audio** ne module que l'AMPLITUDE, entre 0.6 et 1.15.
 * - Sur les visèmes de fermeture (`sil`, `PP`, `FF`, `kk`), l'amplitude est
 *   **ignorée** : la bouche se ferme franchement, quoi que dise le signal.
 *
 * L'audio ne peut donc plus contredire la forme — au pire il la rend un peu
 * plus ou un peu moins ample.
 *
 * ## Horloge
 *
 * La position dans la piste vient de `AudioContext.currentTime` et du `when`
 * réel passé à `AudioBufferSourceNode.start()`, jamais d'un compteur rAF qui
 * dériverait. On retire `baseLatency + outputLatency` pour compenser le retard
 * de sortie : ce qu'on entend à l'instant T a été poussé dans le graphe audio
 * un peu avant. Un offset de calibration reste réglable par-dessus.
 *
 * ## Testabilité
 *
 * Tout l'état vit dans une closure et l'écriture des morphs passe par une
 * interface injectée : aucun accès au DOM ni à l'audio depuis le module.
 */
import type { OculusViseme, VisemeFrame } from "@/lib/fr-phonemes";
import { DEFAULT_TUNING } from "@/lib/avatar-tuning";

/* ------------------------------------------------------------------ *
 * Interfaces injectées
 * ------------------------------------------------------------------ */

/** Écriture des morphs. Implémentée par l'adaptateur TalkingHead côté composant. */
export interface MouthWriter {
  /** Pose une valeur sur le canal prioritaire. */
  set: (morph: string, value: number) => void;
  /** Relâche le morph : le moteur reprend la main dessus. */
  clear: (morph: string) => void;
}

/** Horloge audio partagée, exprimée dans la base de temps de l'AudioContext. */
export interface SpeechClock {
  /** `AudioContext.currentTime`, en secondes. */
  audioTime: number;
  /** Instant de démarrage réel du buffer source, même base de temps. */
  startedAt: number;
  /** `baseLatency + outputLatency`, en secondes. */
  latency: number;
}

/** Indices tirés de l'analyse spectrale (voir `audio-visemes.ts`). */
export interface AudioDrive {
  /** Énergie médium 350 Hz–2 kHz : indice de voyelle ouverte, 0..1. */
  openness: number;
  /** Ratio aigu/grave : indice de fricative, 0..1. Bride l'ouverture de mâchoire. */
  fricative: number;
  /** Niveau global lissé, 0..1. */
  level: number;
}

/* ------------------------------------------------------------------ *
 * Morphs pilotés
 * ------------------------------------------------------------------ */

/** Les 15 visèmes Oculus, préfixés comme dans le GLB Ready Player Me. */
const VISEME_MORPH: Record<OculusViseme, string> = {
  sil: "viseme_sil",
  PP: "viseme_PP",
  FF: "viseme_FF",
  TH: "viseme_TH",
  DD: "viseme_DD",
  kk: "viseme_kk",
  CH: "viseme_CH",
  SS: "viseme_SS",
  nn: "viseme_nn",
  RR: "viseme_RR",
  aa: "viseme_aa",
  E: "viseme_E",
  I: "viseme_I",
  O: "viseme_O",
  U: "viseme_U",
};

/**
 * Tous les morphs que ce moteur s'autorise à écrire — et donc tous ceux qu'il
 * doit remettre à zéro en sortant. Rien d'autre ne doit toucher à cette liste.
 */
export const MOUTH_MORPHS: string[] = [...Object.values(VISEME_MORPH), "jawOpen"];

/**
 * Visèmes de fermeture. L'amplitude audio n'y est pas appliquée : une bilabiale
 * doit claquer même si le signal est fort à cet instant (le son du /p/ arrive
 * *après* la fermeture des lèvres, pas pendant).
 *
 * `sil` n'écrit aucun morph de visème : la bouche fermée, c'est l'absence de
 * forme, pas une forme de plus. On évite ainsi de dépendre de l'allure exacte
 * du morph `viseme_sil` du modèle.
 */
const CLOSURE: ReadonlySet<OculusViseme> = new Set<OculusViseme>(["sil", "PP", "FF", "kk"]);

/* ------------------------------------------------------------------ *
 * Coarticulation
 * ------------------------------------------------------------------ */

/**
 * Enveloppe par classe articulatoire. `attack` = anticipation avant le début du
 * visème, `release` = traîne après sa fin ; `sharp` donne une montée linéaire
 * (sèche), sinon on lisse en smoothstep (molle).
 *
 * Les plosives sont brèves et sèches, les voyelles longues et molles : c'est ce
 * qui distingue une bouche qui articule d'une bouche qui mâchonne.
 */
type Envelope = { attack: number; release: number; sharp: boolean };

const ENVELOPES: Record<OculusViseme, Envelope> = {
  // Plosives et fermetures : court, net.
  PP: { attack: 25, release: 35, sharp: true },
  DD: { attack: 28, release: 38, sharp: true },
  kk: { attack: 30, release: 40, sharp: true },
  // Fricatives : mise en place un peu plus progressive.
  FF: { attack: 40, release: 50, sharp: false },
  SS: { attack: 42, release: 52, sharp: false },
  CH: { attack: 42, release: 52, sharp: false },
  TH: { attack: 40, release: 50, sharp: false },
  // Nasales et liquides.
  nn: { attack: 40, release: 50, sharp: false },
  RR: { attack: 45, release: 55, sharp: false },
  // Voyelles : long, mou.
  aa: { attack: 60, release: 70, sharp: false },
  E: { attack: 58, release: 68, sharp: false },
  I: { attack: 55, release: 65, sharp: false },
  O: { attack: 60, release: 70, sharp: false },
  U: { attack: 58, release: 68, sharp: false },
  // Silence : fermeture douce.
  sil: { attack: 50, release: 50, sharp: false },
};

/** Voyelles : seules elles ouvrent la mâchoire. */
const VOWELS: ReadonlySet<OculusViseme> = new Set<OculusViseme>(["aa", "E", "I", "O", "U"]);

const clamp01 = (x: number) => (x < 0 ? 0 : x > 1 ? 1 : x);
/** Montée/descente adoucie aux deux bouts. */
const smoothstep = (x: number) => x * x * (3 - 2 * x);

/** Bornes de la fenêtre de recouvrement entre visèmes consécutifs (ms). */
export const OVERLAP_MIN_MS = 40;
export const OVERLAP_MAX_MS = 70;

/**
 * Poids d'un visème à l'instant `t`, anticipation et traîne comprises.
 *
 * Le poids monte **avant** le début du visème (anticipation) et retombe **après**
 * sa fin (traîne) : c'est la coarticulation, deux visèmes voisins se recouvrent
 * au lieu de se succéder par à-coups.
 */
function frameWeight(frame: VisemeFrame, t: number, overlapMs: number): number {
  const env = ENVELOPES[frame.viseme];
  const overlap = Math.min(Math.max(overlapMs, OVERLAP_MIN_MS), OVERLAP_MAX_MS);
  const attack = Math.min(env.attack, overlap);
  const release = Math.min(env.release, overlap);
  const shape = env.sharp ? (x: number) => x : smoothstep;

  if (t <= frame.startMs - attack) return 0;
  if (t < frame.startMs) {
    return attack <= 0 ? 1 : shape(clamp01((t - (frame.startMs - attack)) / attack));
  }
  if (t <= frame.endMs) return 1;
  if (t < frame.endMs + release) {
    return release <= 0 ? 0 : 1 - shape(clamp01((t - frame.endMs) / release));
  }
  return 0;
}

/**
 * Poids de chaque visème actif à l'instant `t`.
 *
 * Les poids sont normalisés quand leur somme dépasse 1 : pendant un
 * recouvrement, deux formes se partagent la bouche au lieu de s'additionner en
 * une grimace.
 *
 * Fonction pure — c'est elle que testent les tests de coarticulation.
 */
export function visemeWeights(
  track: readonly VisemeFrame[],
  t: number,
  overlapMs = 55,
): Map<OculusViseme, number> {
  const raw = new Map<OculusViseme, number>();
  let total = 0;

  for (const frame of track) {
    // La piste est triée : au-delà de la fenêtre de traîne, plus rien ne peut
    // contribuer — mais on ne coupe pas la boucle, une piste reste courte.
    if (t < frame.startMs - OVERLAP_MAX_MS || t > frame.endMs + OVERLAP_MAX_MS) continue;
    const w = frameWeight(frame, t, overlapMs) * frame.intensity;
    if (w <= 0) continue;
    raw.set(frame.viseme, Math.max(raw.get(frame.viseme) ?? 0, w));
  }

  for (const w of raw.values()) total += w;
  if (total > 1) {
    for (const [k, w] of raw) raw.set(k, w / total);
  }
  return raw;
}

/* ------------------------------------------------------------------ *
 * Horloge
 * ------------------------------------------------------------------ */

/**
 * Position dans la piste, en millisecondes.
 *
 * `audioTime - startedAt` donne le temps écoulé depuis le lancement du buffer.
 * On en retire la latence de sortie : le son entendu maintenant est celui qui a
 * été poussé dans le graphe il y a `latency` secondes, donc la bouche doit être
 * en avance d'autant. `calibrationMs` permet d'ajuster à la main (casque
 * Bluetooth, moniteur externe…).
 *
 * Fonction pure — testée directement.
 */
export function trackPositionMs(clock: SpeechClock, calibrationMs = 0): number {
  const elapsed = clock.audioTime - clock.startedAt;
  return elapsed * 1000 - clock.latency * 1000 + calibrationMs;
}

/* ------------------------------------------------------------------ *
 * Moteur
 * ------------------------------------------------------------------ */

export interface LipsyncEngineOptions {
  writer: MouthWriter;
  /** Décalage manuel (ms), positif = bouche en avance. Défaut 0. */
  calibrationMs?: number;
  /** Fenêtre de recouvrement entre visèmes (ms), bornée à 40–70. Défaut 55. */
  overlapMs?: number;
  /** Ouverture maximale de la mâchoire. Défaut 0.45. */
  maxJaw?: number;
  /** Amplitude appliquée aux poids de visèmes, du signal faible au signal fort. */
  amplitudeMin?: number;
  amplitudeMax?: number;
  /** Freinage de la mâchoire par l'indice de fricative, 0..1. */
  fricativeDamping?: number;
}

export interface LipsyncEngine {
  /** Arme une nouvelle piste. Ne déclenche rien tant que `update` n'est pas appelé. */
  start: (track: readonly VisemeFrame[]) => void;
  /**
   * Une image d'animation. `clock` à `null` = pas de parole en cours (la bouche
   * se referme), `drive` à `null` = pas d'analyse disponible (amplitude neutre).
   */
  update: (clock: SpeechClock | null, drive: AudioDrive | null) => void;
  /** Fondu de fermeture (défaut 180 ms) puis relâchement des morphs. */
  release: (fadeMs?: number) => void;
  /** Coupe net : tous les morphs de bouche remis à zéro puis relâchés. */
  cancel: () => void;
  /** Position courante dans la piste (ms), pour le débogage. */
  readonly positionMs: number;
  setCalibrationMs: (ms: number) => void;
}

const DEFAULT_FADE_MS = 180;

export function createLipsyncEngine(opts: LipsyncEngineOptions): LipsyncEngine {
  const {
    writer,
    maxJaw = DEFAULT_TUNING.maxJaw,
    amplitudeMin = DEFAULT_TUNING.amplitudeMin,
    amplitudeMax = DEFAULT_TUNING.amplitudeMax,
    fricativeDamping = DEFAULT_TUNING.fricativeDamping,
  } = opts;
  let calibrationMs = opts.calibrationMs ?? DEFAULT_TUNING.calibrationMs;
  const overlapMs = opts.overlapMs ?? DEFAULT_TUNING.overlapMs;

  let track: readonly VisemeFrame[] = [];
  let positionMs = 0;
  /** Dernières valeurs écrites, pour n'écrire que ce qui change. */
  const written = new Map<string, number>();
  /** Fondu de sortie : 1 = plein, 0 = fermé. `null` = pas de fondu en cours. */
  let fade: { startedAt: number; durationMs: number } | null = null;
  let fadeGain = 1;
  let dirty = false;

  /** N'écrit que si la valeur bouge : on évite de saturer le moteur à 60 Hz. */
  const put = (morph: string, value: number) => {
    const v = Math.round(clamp01(value) * 1000) / 1000;
    if (written.get(morph) === v) return;
    written.set(morph, v);
    writer.set(morph, v);
    dirty = true;
  };

  /** Remet toute la bouche à zéro, puis relâche les morphs. */
  const releaseAll = () => {
    for (const morph of MOUTH_MORPHS) {
      // On repasse par zéro avant de relâcher : sans ça, un morph pourrait
      // rester figé sur sa dernière valeur si le moteur ne réévalue pas.
      if ((written.get(morph) ?? 0) !== 0) writer.set(morph, 0);
      writer.clear(morph);
    }
    written.clear();
    dirty = false;
  };

  return {
    start(next) {
      track = next;
      positionMs = 0;
      fade = null;
      fadeGain = 1;
    },

    update(clock, drive) {
      // Fondu de sortie en cours : on éteint progressivement, base de temps audio.
      if (fade && clock) {
        // Premier passage : on ancre le fondu sur l'horloge audio.
        if (Number.isNaN(fade.startedAt)) fade.startedAt = clock.audioTime;
        const elapsed = (clock.audioTime - fade.startedAt) * 1000;
        fadeGain = 1 - clamp01(elapsed / fade.durationMs);
        if (fadeGain <= 0) {
          releaseAll();
          fade = null;
          track = [];
          return;
        }
      }

      if (!clock || track.length === 0) {
        // Rien à dire : on referme si quelque chose traîne encore.
        if (dirty) releaseAll();
        return;
      }

      positionMs = trackPositionMs(clock, calibrationMs);
      const weights = visemeWeights(track, positionMs, overlapMs);

      // Part de fermeture à cet instant : elle inhibe la mâchoire.
      let closure = 0;
      let vowel = 0;
      for (const [viseme, w] of weights) {
        if (CLOSURE.has(viseme)) closure += w;
        else if (VOWELS.has(viseme)) vowel += w;
      }
      closure = clamp01(closure);

      // Amplitude : l'audio ne décide pas de la forme, seulement de son ampleur.
      // Sans analyse, facteur neutre — la piste seule tient la bouche.
      const openness = drive ? clamp01(drive.openness) : 0.5;
      const amplitude = amplitudeMin + openness * (amplitudeMax - amplitudeMin);

      for (const viseme of Object.keys(VISEME_MORPH) as OculusViseme[]) {
        const morph = VISEME_MORPH[viseme];
        // `sil` ne s'écrit pas : la fermeture est l'absence de forme.
        if (viseme === "sil") {
          put(morph, 0);
          continue;
        }
        const w = weights.get(viseme) ?? 0;
        // Sur une fermeture, l'amplitude audio est ignorée : la bouche ferme franc.
        const gain = CLOSURE.has(viseme) ? 1 : amplitude;
        put(morph, w * gain * fadeGain);
      }

      // Mâchoire : ouverte par les voyelles, bridée par l'indice de fricative
      // (un « sss » est aigu et fort mais la mâchoire reste presque close) et
      // refermée par toute part de fermeture en cours.
      const fricative = drive ? clamp01(drive.fricative) : 0;
      const jaw = vowel * openness * (1 - fricativeDamping * fricative) * (1 - closure) * maxJaw;
      put("jawOpen", jaw * fadeGain);
    },

    release(fadeMs = DEFAULT_FADE_MS) {
      if (fadeMs <= 0) {
        releaseAll();
        track = [];
        return;
      }
      // Le fondu s'ancre sur l'horloge audio à la première `update` qui en
      // porte une (`startedAt` NaN = pas encore ancré).
      if (!fade) fade = { startedAt: Number.NaN, durationMs: fadeMs };
    },

    cancel() {
      track = [];
      fade = null;
      fadeGain = 1;
      positionMs = 0;
      releaseAll();
    },

    get positionMs() {
      return positionMs;
    },

    setCalibrationMs(ms) {
      calibrationMs = ms;
    },
  };
}
