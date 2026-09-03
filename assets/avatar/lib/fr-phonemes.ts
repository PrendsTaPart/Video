/**
 * Graphème → phonème français → visème Oculus, déterministe et sans dépendance.
 *
 * Pourquoi ce module : ElevenLabs renvoie un alignement **caractère par
 * caractère**. Jusqu'ici on l'agrégeait en timings de mots, puis on redécoupait
 * ces mots en tranches de lettres par heuristique — on reconstruisait
 * approximativement une donnée qu'on avait exacte. Ici, chaque phonème connaît
 * les lettres qui l'ont produit : son timing est **lu** dans l'alignement, jamais
 * réparti au prorata.
 *
 * Deuxième raison : TalkingHead 1.7 n'embarque de moteur de lipsync que pour
 * `fi`, `en` et `lt`. Son sélecteur est `this.lipsync[lang] || Object.values(this.lipsync)[0]`,
 * donc `lipsyncLang: "fr"` retombe silencieusement sur le **premier module chargé,
 * le finnois**. Fournir une piste de visèmes explicite court-circuite ce moteur.
 *
 * ## Table phonème → visème Oculus
 *
 * Les 15 visèmes Oculus sont plus grossiers que l'inventaire phonémique français
 * (~36 phonèmes) : plusieurs phonèmes partagent donc une même position de bouche.
 *
 * | Visème | Phonèmes (API)        | Exemples                          |
 * | ------ | --------------------- | --------------------------------- |
 * | `aa`   | a, ɑ̃                  | p**a**s, restaur**an**t           |
 * | `E`    | e, ɛ, ɛ̃, ə            | ét**é**, m**è**re, p**ain**, l**e** |
 * | `I`    | i, j                  | l**i**t, pa**y**s                 |
 * | `O`    | o, ɔ, ɔ̃, ø, œ, œ̃      | m**o**t, b**on**, p**eu**, br**un** |
 * | `U`    | u, y, w, ɥ            | f**ou**, t**u**, **oi**, l**ui**  |
 * | `PP`   | p, b, m               | **p**ain, **b**on, **m**ain       |
 * | `FF`   | f, v                  | **f**eu, **v**ous                 |
 * | `TH`   | θ, ð                  | (emprunts : *th*riller)           |
 * | `DD`   | t, d, l               | **t**u, **d**e, **l**a            |
 * | `kk`   | k, g                  | **c**ou, **g**are                 |
 * | `CH`   | ʃ, ʒ                  | **ch**at, **j**our                |
 * | `SS`   | s, z                  | **s**el, ro**s**e                 |
 * | `nn`   | n, ɲ                  | **n**on, a**gn**eau               |
 * | `RR`   | ʁ                     | **r**ue                           |
 * | `sil`  | —                     | silences et pauses                |
 *
 * Note : `intensity` décrit l'ouverture attendue de la bouche (0–1). TalkingHead
 * 1.7 ne la lit pas sur le chemin `visemes` — il applique 0.9 aux bilabiales /
 * labiodentales et 0.6 ailleurs. On s'en sert donc en amont, pour écarter les
 * articulations trop faibles (e muet) qui feraient « mâchonner » l'avatar.
 */

/** Les 15 visèmes Oculus, tels que TalkingHead les préfixe en `viseme_<id>`. */
export type OculusViseme =
  | "sil"
  | "PP"
  | "FF"
  | "TH"
  | "DD"
  | "kk"
  | "CH"
  | "SS"
  | "nn"
  | "RR"
  | "aa"
  | "E"
  | "I"
  | "O"
  | "U";

/** Un caractère horodaté issu de l'alignement ElevenLabs. */
export type TimedChar = { c: string; startMs: number; endMs: number };

/** Un visème horodaté, prêt pour TalkingHead. */
export type VisemeFrame = {
  viseme: OculusViseme;
  startMs: number;
  endMs: number;
  /** Ouverture attendue de la bouche, 0–1. */
  intensity: number;
};

/** Un phonème et l'empan de lettres qui l'a produit (demi-ouvert : [from, to[). */
export type Phoneme = { p: string; from: number; to: number };

/* ------------------------------------------------------------------ *
 * Tables
 * ------------------------------------------------------------------ */

const PHONEME_TO_VISEME: Record<string, OculusViseme> = {
  // Voyelles orales
  a: "aa",
  e: "E",
  ɛ: "E",
  ə: "E",
  i: "I",
  o: "O",
  ɔ: "O",
  ø: "O",
  œ: "O",
  u: "U",
  y: "U",
  // Voyelles nasales
  ɑ̃: "aa",
  ɛ̃: "E",
  ɔ̃: "O",
  œ̃: "O",
  // Semi-voyelles
  j: "I",
  w: "U",
  ɥ: "U",
  // Consonnes
  p: "PP",
  b: "PP",
  m: "PP",
  f: "FF",
  v: "FF",
  t: "DD",
  d: "DD",
  l: "DD",
  k: "kk",
  g: "kk",
  s: "SS",
  z: "SS",
  ʃ: "CH",
  ʒ: "CH",
  n: "nn",
  ɲ: "nn",
  ʁ: "RR",
  θ: "TH",
  ð: "TH",
};

/** Ouverture de bouche par phonème (0–1). Les voyelles ouvrent, le schwa presque pas. */
const PHONEME_INTENSITY: Record<string, number> = {
  a: 1,
  ɑ̃: 1,
  ɛ: 0.85,
  ɛ̃: 0.85,
  e: 0.8,
  ɔ: 0.85,
  ɔ̃: 0.85,
  o: 0.8,
  œ: 0.8,
  œ̃: 0.8,
  ø: 0.75,
  u: 0.7,
  y: 0.7,
  i: 0.7,
  ə: 0.35,
  j: 0.55,
  w: 0.6,
  ɥ: 0.6,
  p: 0.9,
  b: 0.9,
  m: 0.9,
  f: 0.9,
  v: 0.9,
};
const DEFAULT_CONSONANT_INTENSITY = 0.6;

const VOWEL_LETTERS = "aeiouyàâäéèêëîïôöùûüœæ";
const isVowelLetter = (c: string | undefined) => !!c && VOWEL_LETTERS.includes(c);

/**
 * Exceptions : mots dont la graphie ment sur la prononciation. Le G2P régulier
 * les traiterait mal quelles que soient les règles, c'est le propre d'une
 * exception — on les liste plutôt que de tordre les règles autour d'elles.
 */
const LEXICON: Record<string, string[]> = {
  femme: ["f", "a", "m"],
  oignon: ["ɔ", "ɲ", "ɔ̃"],
  monsieur: ["m", "ə", "s", "j", "ø"],
  messieurs: ["m", "e", "s", "j", "ø"],
  automne: ["o", "t", "ɔ", "n"],
  paon: ["p", "ɑ̃"],
  aout: ["u"],
  août: ["u"],
  eu: ["y"],
  eux: ["ø"],
  est: ["ɛ"],
  es: ["ɛ"],
  et: ["e"],
  les: ["l", "e"],
  des: ["d", "e"],
  mes: ["m", "e"],
  tes: ["t", "e"],
  ses: ["s", "e"],
  ces: ["s", "e"],
  qui: ["k", "i"],
  que: ["k", "ə"],
  quest: ["k", "ɛ"], // « qu'est » après retrait de l'apostrophe
  ce: ["s", "ə"],
  fils: ["f", "i", "s"],
  tous: ["t", "u", "s"],
  plus: ["p", "l", "y", "s"],
  sept: ["s", "ɛ", "t"],
  huit: ["ɥ", "i", "t"],
  neuf: ["n", "œ", "f"],
  dix: ["d", "i", "s"],
  six: ["s", "i", "s"],
};

/* ------------------------------------------------------------------ *
 * Règles graphème → phonème
 * ------------------------------------------------------------------ */

type Rule = {
  /** Graphie reconnue à la position courante. */
  g: string;
  /** Phonèmes produits (vide = lettre muette). */
  p: string[];
  /** Condition contextuelle éventuelle. */
  when?: (w: string, i: number, end: number) => boolean;
};

/** Une voyelle nasale ne l'est que si la nasale n'est pas « rouverte » par une voyelle ou une nasale suivante. */
const nasal = (w: string, i: number, len: number) => {
  const next = w[i + len];
  return !isVowelLetter(next) && next !== "n" && next !== "m";
};

/** Position finale du mot (ou suivie uniquement de lettres muettes finales). */
const atEnd = (w: string, i: number, len: number) => i + len >= w.length;

/**
 * Le « e » est-il en syllabe fermée ? Vrai s'il est suivi d'au moins deux
 * consonnes (« res-taurant », « cher-cher ») ou d'une unique consonne finale
 * (« mer », « sel »). Dans ce cas il s'ouvre en /ɛ/ ; ailleurs il se réduit en /ə/.
 */
function closedSyllable(w: string, i: number, end: number): boolean {
  let consonants = 0;
  let k = i + 1;
  while (k < end && !isVowelLetter(w[k])) {
    consonants++;
    k++;
  }
  if (consonants >= 2) return true;
  return consonants === 1 && k >= end;
}

/**
 * Règles essayées dans l'ordre à chaque position : la première qui matche gagne.
 * Les graphies longues précèdent les courtes (« eau » avant « eu » avant « e »).
 */
const RULES: Rule[] = [
  /* --- voyelles nasales (avant les voyelles orales) --- */
  { g: "aient", p: ["ɛ"], when: atEnd },
  { g: "ain", p: ["ɛ̃"], when: (w, i) => nasal(w, i, 3) },
  { g: "aim", p: ["ɛ̃"], when: (w, i) => nasal(w, i, 3) },
  { g: "ein", p: ["ɛ̃"], when: (w, i) => nasal(w, i, 3) },
  { g: "eim", p: ["ɛ̃"], when: (w, i) => nasal(w, i, 3) },
  { g: "oin", p: ["w", "ɛ̃"], when: (w, i) => nasal(w, i, 3) },
  { g: "ien", p: ["j", "ɛ̃"], when: (w, i) => nasal(w, i, 3) },
  { g: "yen", p: ["j", "ɛ̃"], when: (w, i) => nasal(w, i, 3) },
  { g: "oen", p: ["w", "ɛ̃"], when: (w, i) => nasal(w, i, 3) },
  { g: "an", p: ["ɑ̃"], when: (w, i) => nasal(w, i, 2) },
  { g: "am", p: ["ɑ̃"], when: (w, i) => nasal(w, i, 2) },
  { g: "en", p: ["ɑ̃"], when: (w, i) => nasal(w, i, 2) },
  { g: "em", p: ["ɑ̃"], when: (w, i) => nasal(w, i, 2) },
  { g: "in", p: ["ɛ̃"], when: (w, i) => nasal(w, i, 2) },
  { g: "im", p: ["ɛ̃"], when: (w, i) => nasal(w, i, 2) },
  { g: "yn", p: ["ɛ̃"], when: (w, i) => nasal(w, i, 2) },
  { g: "ym", p: ["ɛ̃"], when: (w, i) => nasal(w, i, 2) },
  { g: "on", p: ["ɔ̃"], when: (w, i) => nasal(w, i, 2) },
  { g: "om", p: ["ɔ̃"], when: (w, i) => nasal(w, i, 2) },
  { g: "un", p: ["œ̃"], when: (w, i) => nasal(w, i, 2) },
  { g: "um", p: ["œ̃"], when: (w, i) => nasal(w, i, 2) },

  /* --- voyelles composées --- */
  { g: "eau", p: ["o"] },
  { g: "œu", p: ["ø"] },
  { g: "oeu", p: ["ø"] },
  { g: "eu", p: ["ø"] },
  { g: "au", p: ["o"] },
  { g: "ou", p: ["u"] },
  { g: "oi", p: ["w", "a"] },
  { g: "oy", p: ["w", "a", "j"] },
  { g: "ai", p: ["ɛ"] },
  { g: "ei", p: ["ɛ"] },
  { g: "ay", p: ["ɛ", "j"] },
  { g: "ey", p: ["ɛ", "j"] },
  // « ui » ne vaut /ɥi/ qu'après consonne : « lui » oui, mais pas dans « oui ».
  { g: "ui", p: ["ɥ", "i"], when: (w, i) => i > 0 && !isVowelLetter(w[i - 1]) },

  /* --- consonnes composées --- */
  { g: "ch", p: ["ʃ"] },
  { g: "ck", p: ["k"] },
  { g: "gn", p: ["ɲ"] },
  { g: "ph", p: ["f"] },
  { g: "th", p: ["t"] },
  // « qu » = /k/ ; « gu » = /g/ devant e/i/y (le u y est un simple diacritique).
  { g: "qu", p: ["k"] },
  { g: "gu", p: ["g"], when: (w, i) => "eiyéèê".includes(w[i + 2] ?? "") },
  { g: "cc", p: ["k", "s"], when: (w, i) => "eiyéèê".includes(w[i + 2] ?? "") },
  { g: "sc", p: ["s"], when: (w, i) => "eiyéèê".includes(w[i + 2] ?? "") },
  { g: "ill", p: ["j"], when: (w, i) => i > 0 && isVowelLetter(w[i - 1]) },

  /* --- consonnes doubles : une seule articulation --- */
  ...["bb", "cc", "dd", "ff", "gg", "ll", "mm", "nn", "pp", "rr", "tt", "zz"].map((g) => ({
    g,
    p: [
      {
        bb: "b",
        cc: "k",
        dd: "d",
        ff: "f",
        gg: "g",
        ll: "l",
        mm: "m",
        nn: "n",
        pp: "p",
        rr: "ʁ",
        tt: "t",
        zz: "z",
      }[g] as string,
    ],
  })),
  { g: "ss", p: ["s"] },

  /* --- consonnes simples à contexte --- */
  { g: "c", p: ["s"], when: (w, i) => "eiyéèê".includes(w[i + 1] ?? "") },
  { g: "c", p: ["k"] },
  { g: "ç", p: ["s"] },
  { g: "g", p: ["ʒ"], when: (w, i) => "eiyéèê".includes(w[i + 1] ?? "") },
  { g: "g", p: ["g"] },
  // « s » intervocalique se sonorise : ro*s*e /ʁoz/.
  {
    g: "s",
    p: ["z"],
    when: (w, i) => i > 0 && isVowelLetter(w[i - 1]) && isVowelLetter(w[i + 1]),
  },
  { g: "x", p: ["k", "s"] },
  { g: "h", p: [] }, // toujours muet en français

  /* --- voyelles simples --- */
  { g: "é", p: ["e"] },
  { g: "è", p: ["ɛ"] },
  { g: "ê", p: ["ɛ"] },
  { g: "ë", p: ["ɛ"] },
  { g: "à", p: ["a"] },
  { g: "â", p: ["a"] },
  { g: "ä", p: ["a"] },
  { g: "î", p: ["i"] },
  { g: "ï", p: ["i"] },
  { g: "ô", p: ["o"] },
  { g: "ö", p: ["ɔ"] },
  { g: "û", p: ["y"] },
  { g: "ù", p: ["y"] },
  { g: "ü", p: ["y"] },
  { g: "a", p: ["a"] },
  { g: "i", p: ["i"] },
  { g: "o", p: ["ɔ"] },
  { g: "u", p: ["y"] },
  // « -er » / « -ez » finaux d'un mot d'au moins deux syllabes valent /e/, le
  // « r » restant muet : « chercher » /ʃɛʁʃe/. Les monosyllabes gardent /ɛʁ/
  // (« mer », « cher »), d'où le garde-fou sur la position.
  { g: "er", p: ["e"], when: (w, i, end) => i + 2 >= end && i > 2 },
  { g: "ez", p: ["e"], when: (w, i, end) => i + 2 >= end && i > 1 },
  // « e » nu : /ɛ/ en syllabe fermée (suivi d'au moins deux consonnes, ou d'une
  // consonne finale), /ə/ sinon. « restaurant » /ʁɛs…/ vs « petit » /pəti/.
  { g: "e", p: ["ɛ"], when: (w, i, end) => closedSyllable(w, i, end) },
  { g: "e", p: ["ə"] },
  // « y » entre voyelles vaut /j/ ; ailleurs /i/.
  { g: "y", p: ["j"], when: (w, i) => i > 0 && isVowelLetter(w[i - 1]) && isVowelLetter(w[i + 1]) },
  { g: "y", p: ["i"] },

  /* --- consonnes simples --- */
  { g: "b", p: ["b"] },
  { g: "d", p: ["d"] },
  { g: "f", p: ["f"] },
  { g: "j", p: ["ʒ"] },
  { g: "k", p: ["k"] },
  { g: "l", p: ["l"] },
  { g: "m", p: ["m"] },
  { g: "n", p: ["n"] },
  { g: "p", p: ["p"] },
  { g: "q", p: ["k"] },
  { g: "r", p: ["ʁ"] },
  { g: "s", p: ["s"] },
  { g: "t", p: ["t"] },
  { g: "v", p: ["v"] },
  { g: "w", p: ["w"] },
  { g: "z", p: ["z"] },
];

/** Consonnes finales muettes en français (hors mots outils listés au lexique). */
const SILENT_FINAL = new Set(["s", "t", "d", "x", "z", "p", "g", "e"]);

/**
 * Détermine la longueur de la queue muette d'un mot : le « e » final et les
 * consonnes finales non prononcées. « restaurant » → 1 (t), « parcours » → 1 (s),
 * « température » → 1 (e). Le « r » de « jour » ou le « l » de « seul » restent.
 */
function silentTailLength(w: string): number {
  if (w.length < 2) return 0;
  // Pluriel « -es » : les deux lettres se taisent, mais la consonne qui précède
  // reste prononcée et sonorisée (« roses » /ʁoz/).
  if (w.length > 2 && w.endsWith("es")) return 2;
  // « e » final muet : il ne masque JAMAIS la consonne qui le précède —
  // « rose » /ʁoz/, « température » /tɑ̃peʁatyʁ/.
  if (w.endsWith("e")) return 1;
  // Consonne finale muette isolée : « restauran(t) », « parcour(s) ».
  const last = w[w.length - 1];
  if (last && last !== "e" && SILENT_FINAL.has(last)) return 1;
  return 0;
}

/**
 * Convertit un mot (déjà minusculé, sans ponctuation) en phonèmes, chacun
 * rattaché aux lettres qui l'ont produit.
 */
export function frenchPhonemes(word: string): Phoneme[] {
  const w = word.toLowerCase();
  if (!w) return [];

  // Exceptions : on rattache tous les phonèmes à l'empan complet du mot.
  const lex = LEXICON[w];
  if (lex) return lex.map((p) => ({ p, from: 0, to: w.length }));

  const tail = silentTailLength(w);
  const end = w.length - tail;
  const out: Phoneme[] = [];

  let i = 0;
  while (i < end) {
    let matched = false;
    for (const rule of RULES) {
      const len = rule.g.length;
      if (i + len > end) continue;
      if (w.slice(i, i + len) !== rule.g) continue;
      if (rule.when && !rule.when(w, i, end)) continue;
      for (const p of rule.p) out.push({ p, from: i, to: i + len });
      i += len;
      matched = true;
      break;
    }
    if (!matched) {
      // Lettre inconnue (chiffre, symbole) : ignorée, mais on avance toujours.
      i++;
    }
  }

  // « e » final muet : articulation résiduelle très faible, utile pour relâcher
  // la bouche plutôt que de la laisser figée sur la consonne précédente.
  if (tail > 0 && w.endsWith("e") && out.length > 0) {
    out.push({ p: "ə", from: w.length - 1, to: w.length });
  } else if (tail > 0 && out.length > 0) {
    // Consonne finale muette : on étire le dernier phonème sur ses lettres.
    const last = out[out.length - 1];
    if (last) last.to = w.length;
  }

  return out;
}

/* ------------------------------------------------------------------ *
 * Découpage en mots horodatés
 * ------------------------------------------------------------------ */

type TimedWord = { letters: TimedChar[]; text: string };

/** Sépare l'apostrophe et le trait d'union : « qu'est-ce » → qu / est / ce. */
const WORD_SEPARATOR = /[\s'’\-–—.,;:!?…«»()"]/u;

function splitWords(chars: TimedChar[]): TimedWord[] {
  const words: TimedWord[] = [];
  let cur: TimedChar[] = [];
  const flush = () => {
    if (cur.length === 0) return;
    words.push({ letters: cur, text: cur.map((t) => t.c).join("") });
    cur = [];
  };
  for (const t of chars) {
    if (WORD_SEPARATOR.test(t.c)) flush();
    else cur.push(t);
  }
  flush();
  return words;
}

/* ------------------------------------------------------------------ *
 * Liaisons
 * ------------------------------------------------------------------ */

/**
 * Mots outils déclenchant une liaison obligatoire devant voyelle. On s'en tient
 * à ce sous-ensemble sûr : les liaisons facultatives varient avec le registre et
 * une liaison fautive s'entend plus qu'une liaison omise.
 */
const LIAISON_WORDS = new Set([
  "les",
  "des",
  "mes",
  "tes",
  "ses",
  "ces",
  "nos",
  "vos",
  "leurs",
  "un",
  "deux",
  "trois",
  "six",
  "dix",
  "aux",
  "aux",
  "nous",
  "vous",
  "ils",
  "elles",
  "on",
  "en",
  "est",
  "sont",
  "ont",
  "sans",
  "dans",
  "chez",
  "très",
  "plus",
  "moins",
  "grand",
  "petit",
  "bien",
  "tout",
  "tous",
  "quand",
]);

/** Consonne de liaison produite par la lettre finale. */
const LIAISON_SOUND: Record<string, string> = {
  s: "z",
  x: "z",
  z: "z",
  t: "t",
  d: "t",
  n: "n",
  p: "p",
  r: "ʁ",
};

/* ------------------------------------------------------------------ *
 * Piste de visèmes
 * ------------------------------------------------------------------ */

export type VisemeOptions = {
  /** Appliquer les liaisons obligatoires (défaut : true). */
  liaisons?: boolean;
  /** Silence (ms) à partir duquel on insère un visème `sil` (défaut : 120). */
  minSilenceMs?: number;
  /** Intensité en deçà de laquelle le visème est écarté (défaut : 0 = tout garder). */
  minIntensity?: number;
};

const visemeOf = (p: string): OculusViseme => PHONEME_TO_VISEME[p] ?? "sil";
const intensityOf = (p: string): number => PHONEME_INTENSITY[p] ?? DEFAULT_CONSONANT_INTENSITY;

/**
 * Transforme un alignement caractère en piste de visèmes horodatés.
 *
 * Le timing n'est jamais estimé : chaque phonème hérite du début de sa première
 * lettre et de la fin de sa dernière. Les phonèmes multiples issus d'une même
 * graphie (« oi » → /w/ + /a/) se partagent l'empan à parts égales.
 */
export function charsToVisemes(chars: TimedChar[], opt: VisemeOptions = {}): VisemeFrame[] {
  const { liaisons = true, minSilenceMs = 120, minIntensity = 0 } = opt;
  const words = splitWords(chars);
  const frames: VisemeFrame[] = [];

  words.forEach((word, wi) => {
    const phonemes = frenchPhonemes(word.text);
    if (phonemes.length === 0) return;

    // Liaison : la consonne finale muette se rattache au mot suivant s'il
    // commence par une voyelle. Elle est prononcée à la place du silence.
    const next = words[wi + 1];
    let liaisonPhoneme: string | undefined;
    if (liaisons && next) {
      const lower = word.text.toLowerCase();
      const last = lower[lower.length - 1];
      const nextFirst = next.text.toLowerCase()[0];
      if (
        last &&
        LIAISON_WORDS.has(lower) &&
        LIAISON_SOUND[last] &&
        (isVowelLetter(nextFirst) || nextFirst === "h")
      ) {
        liaisonPhoneme = LIAISON_SOUND[last];
      }
    }

    // Regroupe les phonèmes partageant le même empan de lettres pour se
    // partager sa durée (« oi » → /w/ puis /a/ sur la même paire de lettres).
    let k = 0;
    while (k < phonemes.length) {
      const span = phonemes[k];
      if (!span) break;
      let j = k;
      while (j + 1 < phonemes.length && phonemes[j + 1]?.from === span.from) j++;
      const group = phonemes.slice(k, j + 1);

      const first = word.letters[span.from];
      const lastLetter = word.letters[Math.min(span.to, word.letters.length) - 1];
      const startMs = first?.startMs ?? 0;
      const endMs = lastLetter?.endMs ?? startMs;
      const step = (endMs - startMs) / group.length;

      group.forEach((ph, gi) => {
        const s = startMs + step * gi;
        const e = gi === group.length - 1 ? endMs : startMs + step * (gi + 1);
        const intensity = intensityOf(ph.p);
        if (intensity < minIntensity) return;
        frames.push({
          viseme: visemeOf(ph.p),
          startMs: Math.round(s),
          endMs: Math.round(e),
          intensity,
        });
      });

      k = j + 1;
    }

    // La liaison occupe le tout début du silence inter-mots.
    if (liaisonPhoneme && next) {
      const wordEnd = word.letters[word.letters.length - 1]?.endMs ?? 0;
      const nextStart = next.letters[0]?.startMs ?? wordEnd;
      if (nextStart > wordEnd) {
        frames.push({
          viseme: visemeOf(liaisonPhoneme),
          startMs: Math.round(wordEnd),
          endMs: Math.round(Math.min(nextStart, wordEnd + 60)),
          intensity: intensityOf(liaisonPhoneme),
        });
      }
    }

    // Silence explicite : referme la bouche entre deux groupes de souffle.
    if (next) {
      const wordEnd = word.letters[word.letters.length - 1]?.endMs ?? 0;
      const nextStart = next.letters[0]?.startMs ?? wordEnd;
      const gap = nextStart - wordEnd;
      if (gap >= minSilenceMs) {
        frames.push({
          viseme: "sil",
          startMs: Math.round(wordEnd + (liaisonPhoneme ? 60 : 0)),
          endMs: Math.round(nextStart),
          intensity: 0,
        });
      }
    }
  });

  return mergeAdjacent(frames);
}

/** Fusionne les visèmes identiques qui se suivent : la bouche ne « rebondit » pas. */
function mergeAdjacent(frames: VisemeFrame[]): VisemeFrame[] {
  const out: VisemeFrame[] = [];
  for (const f of frames) {
    if (f.endMs <= f.startMs) continue;
    const prev = out[out.length - 1];
    if (prev && prev.viseme === f.viseme && f.startMs - prev.endMs <= 1) {
      prev.endMs = f.endMs;
      prev.intensity = Math.max(prev.intensity, f.intensity);
      continue;
    }
    out.push({ ...f });
  }
  return out;
}

/* ------------------------------------------------------------------ *
 * Format TalkingHead
 * ------------------------------------------------------------------ */

export type TalkingHeadVisemes = {
  visemes: OculusViseme[];
  vtimes: number[];
  vdurations: number[];
};

/** Met la piste au format attendu par `speakAudio` (`visemes` / `vtimes` / `vdurations`). */
export function toTalkingHead(frames: VisemeFrame[]): TalkingHeadVisemes {
  return {
    visemes: frames.map((f) => f.viseme),
    vtimes: frames.map((f) => f.startMs),
    vdurations: frames.map((f) => Math.max(1, f.endMs - f.startMs)),
  };
}

/* ------------------------------------------------------------------ *
 * Décodage du champ `chars` généré
 * ------------------------------------------------------------------ */

/** Alignement caractère compact, tel que stocké dans `voice-lines.generated.ts`. */
export type PackedChars = { c: string; s: number[]; e: number[] };

/** Déplie l'alignement compact en caractères horodatés. */
export function unpackChars(packed: PackedChars): TimedChar[] {
  // `Array.from` respecte les paires de substitution, contrairement à `split("")`.
  const letters = Array.from(packed.c);
  return letters.map((c, i) => ({
    c,
    startMs: packed.s[i] ?? 0,
    endMs: packed.e[i] ?? packed.s[i] ?? 0,
  }));
}
