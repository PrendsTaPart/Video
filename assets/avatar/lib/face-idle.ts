/**
 * Expressivité faciale hors synchro labiale — respiration, clignements, regard,
 * sourcils et humeur.
 *
 * ## Périmètre
 *
 * Ce module ne touche **jamais** aux morphs de la bouche pilotés par
 * `lipsync-engine` (les 15 `viseme_*` et `jawOpen`). La frontière est vérifiée
 * à l'exécution : toute tentative d'écriture sur un morph de la bouche est
 * ignorée et signalée. Les deux modules cohabitent sur le même visage sans se
 * disputer un seul morph — c'était précisément le défaut de la boucle rAF
 * précédente, où tout était mélangé dans un même `useEffect`.
 *
 * `mouthSmileLeft/Right` n'appartiennent pas au lipsync : c'est un sourire
 * résiduel du haut du visage, il reste donc ici.
 *
 * ## Une seule horloge
 *
 * Aucun `setTimeout`, aucun `requestAnimationFrame` interne. Tout est piloté
 * par `update({ nowMs, … })` appelé depuis la boucle unique du composant :
 * clignements, saccades et rampes d'humeur sont des machines à états lues à
 * chaque image. C'est ce qui rend le module testable et évite les minuteries
 * orphelines au démontage.
 *
 * ## `prefers-reduced-motion`
 *
 * Rien n'est supprimé en silence. Le comportement dégradé est explicite :
 *
 * | Élément              | Normal                              | Réduit                            |
 * | -------------------- | ----------------------------------- | --------------------------------- |
 * | Respiration          | ±100 % d'amplitude, buste + tête    | **conservée à 40 %**, buste seul  |
 * | Regard               | 3 états + micro-saccades            | **conservé**, sans micro-saccades |
 * | Clignements simples  | log-normale ~4 s                    | **conservés**, cadence identique  |
 * | Clignements doubles  | ~20 % des cas                       | **supprimés**                     |
 * | Micro-saccades       | toutes les 250–600 ms               | **supprimées**                    |
 * | Balayage réflexif    | départ franc en haut à gauche       | **amplitude divisée par 2**       |
 * | Sourcils / sourire   | suivis d'intonation et d'humeur     | **conservés**, rampes ralenties   |
 *
 * Autrement dit : le visage reste vivant et lisible, mais plus rien ne bouge
 * de façon saccadée ou imprévisible.
 */
import { MOUTH_MORPHS } from "@/lib/lipsync-engine";
import { DEFAULT_TUNING } from "@/lib/avatar-tuning";

/* ------------------------------------------------------------------ *
 * Interfaces injectées
 * ------------------------------------------------------------------ */

/** Sorties du moteur d'avatar utilisées par le visage. */
export interface FaceWriter {
  /** Morph sur le canal `system` (prioritaire sur les animations du moteur). */
  setValue: (morph: string, value: number, ms?: number | null) => void;
  /** Regard vers un point de la fenêtre. */
  lookAt: (x: number, y: number, ms?: number) => void;
  /** Retour du regard vers la caméra. */
  lookAtCamera: (ms?: number) => void;
  /** Humeur du moteur (pose, respiration de fond, paramètres de voix). */
  setMood: (mood: string) => void;
  /** Rectangle du canvas dans la fenêtre, pour viser le regard. */
  getRect: () => { left: number; top: number; width: number; height: number } | null;
}

/** État du monde à une image donnée. */
export interface FaceIdleInput {
  /** Horloge monotone en ms (`performance.now()`). */
  nowMs: number;
  /** Le chef est-il en train de parler ? */
  speaking: boolean;
  /** Niveau d'enveloppe vocale 0..1 — sert à l'intonation des sourcils. */
  level: number;
  /** Pointeur dans le panneau du Chef Bot, en coordonnées fenêtre. `null` si absent. */
  pointer: { x: number; y: number } | null;
  /** Humeur visée. */
  mood: string;
  /**
   * Image trop longue : on saute les morphs secondaires (sourcils, sourire,
   * respiration). Les machines à états continuent d'avancer, seules les
   * écritures coûteuses sont omises.
   */
  degraded?: boolean;
  /**
   * Accompagnement silencieux : le chef regarde quelque chose avec le visiteur
   * (une vidéo en lecture) sans parler. Ajoute des hochements de tête lents et
   * espacés à la micro-vie habituelle. La bouche n'est jamais concernée.
   */
  accompanying?: boolean;
  /**
   * Maintient le contact caméra même après un long silence. Sans lui, le regard
   * part en balayage réflexif au bout de {@link REFLECTIVE_AFTER_MS} — ce qu'on
   * ne veut pas quand le chef est en attente devant le visiteur (vidéo en pause).
   */
  contact?: boolean;
}

export interface FaceIdleOptions {
  writer: FaceWriter;
  /** `prefers-reduced-motion` : voir le tableau en tête de fichier. */
  reducedMotion?: boolean;
  /** Source d'aléa injectable (tests déterministes). */
  random?: () => number;
  /**
   * Intensité de la micro-vie (respiration, balancement, saccades). 1 = nominal.
   * Se cumule avec `reducedMotion`, qui reste prioritaire pour l'accessibilité.
   */
  vitality?: number;
}

export interface FaceIdle {
  update: (input: FaceIdleInput) => void;
  /**
   * Fin de réplique. Déclenche un clignement dans les 300 ms et, si la réplique
   * était longue, deux cycles de respiration ample.
   */
  notifyUtteranceEnd: (durationMs: number) => void;
  /** Pic d'attention : aucun clignement pendant 400 ms (le regard ne « décroche » pas). */
  notifyAttentionPeak: () => void;
  /** Remet le visage au neutre et relâche les morphs écrits. */
  reset: () => void;
}

/* ------------------------------------------------------------------ *
 * Constantes
 * ------------------------------------------------------------------ */

/** Fréquence respiratoire au repos : ~13 cycles/minute. */
const BREATH_HZ = 0.22;
const BREATH_PERIOD_MS = 1000 / BREATH_HZ;
/** Variation aléatoire d'amplitude d'un cycle à l'autre. */
const BREATH_JITTER = 0.15;
/** Une réplique au-delà de cette durée « essouffle » : respiration ample ensuite. */
const LONG_UTTERANCE_MS = 6000;
/** Durée du surcroît d'amplitude après une réplique longue : deux cycles. */
const BREATH_BOOST_MS = 2 * BREATH_PERIOD_MS;

/** Médiane de l'intervalle entre clignements. */
const BLINK_MEDIAN_MS = 4000;
/** Dispersion de la log-normale (en log). */
const BLINK_SIGMA = 0.42;
const BLINK_MIN_MS = 900;
const BLINK_MAX_MS = 11000;
/** Fermeture puis ouverture de la paupière. */
const BLINK_CLOSE_MS = 90;
const BLINK_OPEN_MS = 110;
/** Probabilité d'un clignement double. */
const DOUBLE_BLINK_P = 0.2;
const DOUBLE_BLINK_GAP_MS = 200;
/** Clignement systématique après une fin de phrase. */
const END_OF_PHRASE_BLINK_MS = 300;
/** Fenêtre pendant laquelle un pic d'attention interdit les clignements. */
const ATTENTION_HOLD_MS = 400;

/** Silence au-delà duquel le regard part en balayage réflexif. */
export const REFLECTIVE_AFTER_MS = 2600;

/**
 * Hochement d'accompagnement — « je suis là, je regarde avec vous ».
 *
 * Un aller-retour du menton, lent, sur le morph signé `headRotateX` (positif =
 * menton qui descend). L'amplitude est volontairement dix fois inférieure à un
 * acquiescement de conversation : à côté d'une vidéo, un vrai hochement
 * capterait le regard alors que le contenu est ailleurs.
 */
const NOD_DURATION_MS = 950;
const NOD_AMPLITUDE = 0.055;
/** Espacement entre deux hochements, tiré uniformément. */
const NOD_MIN_MS = 5000;
const NOD_MAX_MS = 11000;
/** Mouvement réduit : hochements deux fois plus discrets et deux fois plus rares. */
const NOD_REDUCED_AMPLITUDE = 0.45;
const NOD_REDUCED_SPACING = 1.8;
/** Cadence des micro-saccades. */
const SACCADE_MIN_MS = 250;
const SACCADE_MAX_MS = 600;

/** Durée de l'interpolation entre deux humeurs. */
const MOOD_BLEND_MS = 1200;
/** Retour au neutre après une réplique. */
const MOOD_RELEASE_MS = 1800;

/** Seuil d'écriture : en deçà, la valeur est considérée inchangée. */
const EPSILON = 0.008;

const clamp = (x: number, lo: number, hi: number) => (x < lo ? lo : x > hi ? hi : x);
const clamp01 = (x: number) => clamp(x, 0, 1);
/** Interpolation adoucie aux deux bouts — jamais de rampe linéaire visible. */
const ease = (x: number) => x * x * (3 - 2 * x);

/* ------------------------------------------------------------------ *
 * Expressions par humeur
 * ------------------------------------------------------------------ */

/**
 * Haut du visage par humeur. Le moteur applique déjà ses propres baselines,
 * mais elles basculent d'un coup sur `setMood`. On réécrit donc ces quelques
 * morphs sur le canal `system` (prioritaire sur la baseline) pour maîtriser la
 * transition — c'est ce qui remplace le `setMood` sec.
 */
export type FaceExpression = {
  browInnerUp: number;
  browDown: number;
  eyeSquint: number;
  mouthSmile: number;
};

const NEUTRAL: FaceExpression = { browInnerUp: 0, browDown: 0, eyeSquint: 0, mouthSmile: 0 };

const MOOD_EXPRESSION: Record<string, FaceExpression> = {
  neutral: NEUTRAL,
  happy: { browInnerUp: 0.08, browDown: 0, eyeSquint: 0.18, mouthSmile: 0.32 },
  love: { browInnerUp: 0.22, browDown: 0, eyeSquint: 0.24, mouthSmile: 0.38 },
  // Humeurs « sérieuses » : le front descend au lieu de monter.
  sad: { browInnerUp: 0.35, browDown: 0.12, eyeSquint: 0.05, mouthSmile: 0 },
  angry: { browInnerUp: 0, browDown: 0.55, eyeSquint: 0.3, mouthSmile: 0 },
  disgust: { browInnerUp: 0, browDown: 0.4, eyeSquint: 0.25, mouthSmile: 0 },
  fear: { browInnerUp: 0.5, browDown: 0, eyeSquint: 0, mouthSmile: 0 },
  sleep: { browInnerUp: 0, browDown: 0.1, eyeSquint: 0, mouthSmile: 0.05 },
};

const expressionFor = (mood: string): FaceExpression => MOOD_EXPRESSION[mood] ?? NEUTRAL;

const blendExpression = (a: FaceExpression, b: FaceExpression, t: number): FaceExpression => ({
  browInnerUp: a.browInnerUp + (b.browInnerUp - a.browInnerUp) * t,
  browDown: a.browDown + (b.browDown - a.browDown) * t,
  eyeSquint: a.eyeSquint + (b.eyeSquint - a.eyeSquint) * t,
  mouthSmile: a.mouthSmile + (b.mouthSmile - a.mouthSmile) * t,
});

/* ------------------------------------------------------------------ *
 * Lois de tirage
 * ------------------------------------------------------------------ */

/** Normale centrée réduite par Box-Muller, à partir d'un uniforme injecté. */
function gaussian(random: () => number): number {
  // `1 - random()` écarte 0, dont le logarithme diverge.
  const u = 1 - random();
  const v = random();
  return Math.sqrt(-2 * Math.log(u)) * Math.cos(2 * Math.PI * v);
}

/**
 * Intervalle entre deux clignements, en loi log-normale.
 *
 * L'intervalle uniforme précédent produisait une cadence de métronome. Une
 * log-normale donne beaucoup d'intervalles proches de la médiane et une longue
 * traîne de pauses plus rares — la forme effectivement mesurée sur l'humain.
 */
export function nextBlinkIntervalMs(random: () => number): number {
  const raw = Math.exp(Math.log(BLINK_MEDIAN_MS) + BLINK_SIGMA * gaussian(random));
  return clamp(raw, BLINK_MIN_MS, BLINK_MAX_MS);
}

/* ------------------------------------------------------------------ *
 * Machine
 * ------------------------------------------------------------------ */

/** État du regard. */
export type GazeState = "contact" | "reflective" | "pointer";

const MOUTH_OWNED = new Set(MOUTH_MORPHS);

/**
 * Morphs signés du moteur : contrairement aux blendshapes (0..1), les rotations
 * de buste et de tête vont de −1 à 1 et ont **0 pour neutre**. Les écrire comme
 * un blendshape (0.5 au repos) inclinerait l'avatar en permanence.
 */
const SIGNED_MORPHS: ReadonlySet<string> = new Set([
  "bodyRotateX",
  "bodyRotateY",
  "bodyRotateZ",
  "headRotateX",
  "headRotateY",
  "headRotateZ",
]);

export function createFaceIdle(opts: FaceIdleOptions): FaceIdle {
  const {
    writer,
    reducedMotion = false,
    random = Math.random,
    vitality = DEFAULT_TUNING.vitality,
  } = opts;

  /* --- écriture --- */
  const written = new Map<string, number>();
  let mouthViolation = false;

  const put = (morph: string, value: number, ms: number | null = null) => {
    /*
     * Garde-fou : `lipsync-engine` est le seul propriétaire de la bouche. Si ce
     * module tentait d'y écrire, les deux se contrediraient exactement comme
     * avant le découpage — on refuse plutôt que de laisser passer.
     */
    if (MOUTH_OWNED.has(morph)) {
      if (!mouthViolation) {
        mouthViolation = true;
        console.warn(`[face-idle] écriture refusée sur un morph de la bouche : ${morph}`);
      }
      return;
    }
    const v = SIGNED_MORPHS.has(morph) ? clamp(value, -1, 1) : clamp01(value);
    const prev = written.get(morph);
    if (prev !== undefined && Math.abs(prev - v) < EPSILON) return;
    written.set(morph, v);
    writer.setValue(morph, v, ms);
  };

  /** Écrit une paire gauche/droite (sourcils, yeux, sourire). */
  const putPair = (base: string, value: number, ms: number | null = null) => {
    put(`${base}Left`, value, ms);
    put(`${base}Right`, value, ms);
  };

  /* --- respiration --- */
  let breathPhase = random() * Math.PI * 2;
  let breathAmp = 1;
  let boostUntil = 0;
  let lastNow = 0;

  /* --- clignements --- */
  let blinkAt = 0;
  /** Clignement en cours : instant de départ, ou `null`. */
  let blinkStart: number | null = null;
  let blinkQueued = 0;
  /**
   * Le clignement en cours est-il le second d'une paire ? Sans ce drapeau, un
   * doublon peut à son tour tirer un doublon et la paupière part en rafale.
   */
  let blinkIsDouble = false;
  let attentionUntil = 0;
  let lidValue = 0;

  /* --- hochements d'accompagnement --- */
  let nodAt = 0;
  /** Hochement en cours : instant de départ, ou `null`. */
  let nodStart: number | null = null;

  /* --- regard --- */
  let gaze: GazeState = "contact";
  let silentSince = 0;
  let saccadeAt = 0;
  /** Suivi des transitions de parole : reprendre le contact visuel en début de réplique. */
  let wasSpeaking = false;

  /* --- humeur --- */
  let currentMood = "neutral";
  let fromExpr: FaceExpression = NEUTRAL;
  let toExpr: FaceExpression = NEUTRAL;
  let blendStart = 0;
  let blendDuration = MOOD_BLEND_MS;

  /* --- intonation --- */
  let lastLevel = 0;
  let browIntonation = 0;

  const scheduleBlink = (now: number) => {
    blinkAt = now + nextBlinkIntervalMs(random);
  };

  return {
    update(input) {
      const {
        nowMs: now,
        speaking,
        level,
        pointer,
        mood,
        degraded = false,
        accompanying = false,
        contact = false,
      } = input;
      const dt = lastNow === 0 ? 16 : clamp(now - lastNow, 0, 100);
      lastNow = now;
      if (blinkAt === 0) scheduleBlink(now);
      if (saccadeAt === 0) saccadeAt = now + 900;

      /* ---------- humeur : rampe au lieu d'une bascule ---------- */
      if (mood !== currentMood) {
        // Le moteur bascule ses poses et sa respiration de fond tout de suite ;
        // le haut du visage, lui, est interpolé par nos soins sur `MOOD_BLEND_MS`.
        const t = blendDuration > 0 ? clamp01((now - blendStart) / blendDuration) : 1;
        fromExpr = blendExpression(fromExpr, toExpr, ease(t));
        toExpr = expressionFor(mood);
        blendStart = now;
        blendDuration = MOOD_BLEND_MS;
        currentMood = mood;
        try {
          writer.setMood(mood);
        } catch {
          /* humeur inconnue du moteur : la rampe visuelle s'applique quand même */
        }
      }
      const blendT = blendDuration > 0 ? clamp01((now - blendStart) / blendDuration) : 1;
      const expr = blendExpression(fromExpr, toExpr, ease(blendT));

      /* ---------- respiration ---------- */
      const prevPhase = breathPhase;
      breathPhase += (dt / BREATH_PERIOD_MS) * Math.PI * 2;
      if (Math.floor(prevPhase / (Math.PI * 2)) !== Math.floor(breathPhase / (Math.PI * 2))) {
        // Nouveau cycle : on retire une amplitude légèrement différente.
        breathAmp = 1 + (random() * 2 - 1) * BREATH_JITTER;
      }
      const boosted = now < boostUntil ? 2 : 1;
      // Réduit : on garde la respiration, à 40 % d'amplitude et sans la tête.
      const breathScale = (reducedMotion ? 0.4 : 1) * breathAmp * boosted * vitality;
      const breath = 0.5 + 0.5 * Math.sin(breathPhase);

      /* ---------- hochements d'accompagnement ---------- */
      const nodSpacing = () => {
        const span = NOD_MIN_MS + random() * (NOD_MAX_MS - NOD_MIN_MS);
        return span * (reducedMotion ? NOD_REDUCED_SPACING : 1);
      };
      let nod = 0;
      if (accompanying) {
        if (nodAt === 0) nodAt = now + nodSpacing();
        // On ne hoche pas par-dessus une réplique : le geste appartient au silence.
        if (nodStart === null && !speaking && now >= nodAt) nodStart = now;
        if (nodStart !== null) {
          const t = (now - nodStart) / NOD_DURATION_MS;
          if (t >= 1) {
            nodStart = null;
            nodAt = now + nodSpacing();
          } else {
            // Une demi-sinusoïde : descente puis remontée, sans à-coup aux bouts.
            nod =
              Math.sin(t * Math.PI) *
              NOD_AMPLITUDE *
              (reducedMotion ? NOD_REDUCED_AMPLITUDE : 1) *
              vitality;
          }
        }
      } else {
        nodStart = null;
        nodAt = 0;
      }

      // Très léger balancement, en quadrature avec le souffle. Morphs
      // signés : 0 = neutre, l'amplitude reste sous 2 % de la course.
      const sway = Math.sin(breathPhase - Math.PI / 2);
      const swayX = reducedMotion ? 0 : sway * 0.018 * boosted * vitality;
      if (!degraded) {
        put("chestInhale", clamp01(breath * 0.45 * breathScale), 120);
        if (!reducedMotion) put("bodyRotateZ", sway * 0.012 * boosted * vitality, 160);
      }
      /*
       * Le hochement passe même en mode dégradé, et même en mouvement réduit
       * (à amplitude divisée) : c'est le seul mouvement qu'on regarde en
       * présence silencieuse, et il ne coûte qu'une écriture. Hors hochement,
       * la règle d'origine s'applique — pas de balancement de tête si l'image
       * est trop longue ou si le visiteur a demandé moins de mouvement.
       */
      if (nod !== 0 || (!degraded && !reducedMotion)) put("headRotateX", swayX + nod, 140);

      /* ---------- clignements ---------- */
      if (now >= attentionUntil) {
        if (blinkStart === null && (now >= blinkAt || blinkQueued > 0)) {
          blinkStart = now;
          if (blinkQueued > 0) {
            blinkQueued--;
            blinkIsDouble = true;
            scheduleBlink(now);
          } else {
            blinkIsDouble = false;
            scheduleBlink(now);
          }
        }
      } else if (blinkStart === null) {
        // Pic d'attention : on repousse sans jamais « sauter » un clignement.
        blinkAt = Math.max(blinkAt, attentionUntil);
      }

      if (blinkStart !== null) {
        const elapsed = now - blinkStart;
        if (elapsed <= BLINK_CLOSE_MS) {
          lidValue = ease(clamp01(elapsed / BLINK_CLOSE_MS));
        } else if (elapsed <= BLINK_CLOSE_MS + BLINK_OPEN_MS) {
          lidValue = 1 - ease(clamp01((elapsed - BLINK_CLOSE_MS) / BLINK_OPEN_MS));
        } else {
          lidValue = 0;
          blinkStart = null;
          /*
           * Doublon occasionnel — jamais en chaîne : un clignement déjà second
           * d'une paire n'en déclenche pas un troisième. Supprimé en mouvement
           * réduit (voir le tableau de dégradation en tête de fichier).
           */
          if (!reducedMotion && !blinkIsDouble && blinkQueued === 0 && random() < DOUBLE_BLINK_P) {
            blinkQueued = 1;
          }
          blinkIsDouble = false;
        }
        putPair("eyeBlink", lidValue, 0);
      } else if (lidValue !== 0) {
        lidValue = 0;
        putPair("eyeBlink", 0, 60);
      }

      /* ---------- regard ---------- */
      if (speaking) silentSince = now;
      const silentFor = now - silentSince;

      const nextGaze: GazeState = pointer
        ? "pointer"
        : contact || speaking || silentFor < REFLECTIVE_AFTER_MS
          ? "contact"
          : "reflective";

      const rect = writer.getRect();
      /*
       * Une prise de parole réaffirme le contact visuel même si l'état de regard
       * n'a pas changé : on est déjà en `contact` au repos, mais le chef doit
       * « revenir » à la caméra au moment où il commence à parler.
       */
      const startedSpeaking = speaking && !wasSpeaking;
      wasSpeaking = speaking;
      const changed = nextGaze !== gaze || (startedSpeaking && nextGaze === "contact");
      if (changed) gaze = nextGaze;

      if (gaze === "pointer" && pointer) {
        // Suivi du curseur, avec un léger retard : le regard n'est pas collé.
        writer.lookAt(pointer.x, pointer.y, changed ? 420 : 260);
        saccadeAt = now + SACCADE_MIN_MS;
      } else if (gaze === "contact") {
        if (changed) writer.lookAtCamera(speaking ? 320 : 600);
        // Micro-saccades autour de la caméra : le regard n'est jamais fixe.
        if (!reducedMotion && rect && now >= saccadeAt) {
          const jitterX = (random() * 2 - 1) * rect.width * 0.05;
          const jitterY = (random() * 2 - 1) * rect.height * 0.04;
          writer.lookAt(
            rect.left + rect.width / 2 + jitterX,
            rect.top + rect.height * 0.42 + jitterY,
            180,
          );
          saccadeAt = now + SACCADE_MIN_MS + random() * (SACCADE_MAX_MS - SACCADE_MIN_MS);
        }
      } else if (rect) {
        // Balayage réflexif : le regard part en haut à gauche, « je cherche ».
        // En mouvement réduit, on divise l'écart par deux.
        const reach = reducedMotion ? 0.5 : 1;
        if (changed || now >= saccadeAt) {
          const x = rect.left + rect.width * (0.5 - 0.34 * reach + (random() * 0.08 - 0.04));
          const y = rect.top + rect.height * (0.42 - 0.3 * reach + (random() * 0.06 - 0.03));
          writer.lookAt(x, y, changed ? 520 : 300);
          saccadeAt = now + (reducedMotion ? 1400 : 700 + random() * 900);
        }
      }

      /* ---------- sourcils, yeux, sourire ---------- */
      if (!degraded) {
        /*
         * Intonation : on suit la **dérivée** de l'enveloppe, pas un seuil brut.
         * Un seuil fait monter les sourcils sur tout passage fort et les y
         * laisse ; la dérivée ne réagit qu'aux montées — c'est ce qui marque
         * une question ou une insistance.
         */
        const slope = (level - lastLevel) / (dt / 1000);
        lastLevel = level;
        const impulse = speaking ? clamp01(slope * 0.35) : 0;
        // Montée vive, retombée lente.
        browIntonation +=
          (impulse - browIntonation) *
          (impulse > browIntonation ? 0.35 : 0.06 * (reducedMotion ? 0.6 : 1));

        const ms = reducedMotion ? 260 : 140;
        put("browInnerUp", clamp01(expr.browInnerUp + browIntonation * 0.45), ms);
        putPair("browDown", expr.browDown, ms);
        putPair("eyeSquint", expr.eyeSquint, reducedMotion ? 400 : 240);
        /*
         * Sourire résiduel : il ne retombe pas à zéro entre deux phrases, il
         * reste dans les yeux et aux commissures. Atténué pendant la parole
         * pour ne pas lutter visuellement avec les visèmes.
         */
        putPair("mouthSmile", expr.mouthSmile * (speaking ? 0.45 : 1), reducedMotion ? 420 : 280);
      }
    },

    notifyUtteranceEnd(durationMs) {
      const now = lastNow;
      // Clignement systématique dans les 300 ms qui suivent la fin de phrase.
      blinkAt = Math.min(blinkAt, now + END_OF_PHRASE_BLINK_MS * random());
      // Réplique longue : deux cycles de respiration plus ample.
      if (durationMs >= LONG_UTTERANCE_MS) boostUntil = now + BREATH_BOOST_MS;
      // Retour au neutre en rampe, plus lent que la prise d'humeur.
      fromExpr = blendExpression(
        fromExpr,
        toExpr,
        ease(clamp01((now - blendStart) / blendDuration)),
      );
      toExpr = NEUTRAL;
      blendStart = now;
      blendDuration = MOOD_RELEASE_MS;
      currentMood = "neutral";
    },

    notifyAttentionPeak() {
      attentionUntil = lastNow + ATTENTION_HOLD_MS;
    },

    reset() {
      for (const morph of written.keys()) writer.setValue(morph, 0, 200);
      written.clear();
      blinkStart = null;
      blinkQueued = 0;
      lidValue = 0;
      browIntonation = 0;
      fromExpr = NEUTRAL;
      toExpr = NEUTRAL;
      currentMood = "neutral";
    },
  };
}
