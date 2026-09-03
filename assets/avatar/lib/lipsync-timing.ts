/**
 * Affinage des timings de synchro labiale.
 *
 * ElevenLabs nous donne un timing par mot. TalkingHead répartit alors les
 * visèmes sur toute la durée du mot, ce qui donne une bouche « molle » sur les
 * mots longs et aucune fermeture nette sur la ponctuation.
 *
 * On raffine donc la piste :
 *  - les mots longs sont découpés en segments syllabiques (timings répartis au
 *    prorata du nombre de lettres) ;
 *  - la ponctuation devient un segment vide, ce qui referme la bouche et crée
 *    une micro-pause naturelle ;
 *  - les silences supérieurs à 120 ms sont matérialisés par un segment vide.
 */

export interface LipsyncTrack {
  words: string[];
  wtimes: number[];
  wdurations: number[];
}

/** Durée (ms) au-delà de laquelle un mot est découpé. */
const MAX_SEGMENT_MS = 140;
/** Durée (ms) maximale d'un segment syllabique avant nouveau découpage. */
const MAX_SYLLABLE_MS = 180;
/** Fermeture (ms) insérée avant une bilabiale (b, p, m). */
const BILABIAL_MS = 45;
/** Silence (ms) à partir duquel on insère une fermeture de bouche. */
const SILENCE_MS = 90;

const VOWELS = "aeiouyàâäéèêëîïôöùûüœ";

/** Découpe grossière d'un mot en syllabes (voyelle = noyau). */
function splitSyllables(word: string): string[] {
  const out: string[] = [];
  let current = "";
  let hasVowel = false;

  for (const ch of word) {
    const isVowel = VOWELS.includes(ch.toLowerCase());
    if (isVowel) {
      // Nouvelle syllabe si la précédente contenait déjà voyelle + consonne.
      if (hasVowel && !VOWELS.includes(current[current.length - 1]?.toLowerCase() ?? "")) {
        out.push(current);
        current = "";
        hasVowel = false;
      }
      hasVowel = true;
    }
    current += ch;
  }
  if (current) out.push(current);
  return out.length > 0 ? out : [word];
}

/** Sépare la ponctuation finale du mot ("bonjour," -> ["bonjour", ","]). */
function stripPunctuation(word: string): { core: string; punct: string } {
  const match = /^(.*?)([.,;:!?…»)]*)$/su.exec(word);
  return { core: match?.[1] ?? word, punct: match?.[2] ?? "" };
}

/** Découpe un segment trop long en tranches régulières (bouche plus vivante). */
function splitLong(part: string, ms: number): string[] {
  const slices = Math.ceil(ms / MAX_SYLLABLE_MS);
  if (slices <= 1 || part.length < 2) return [part];
  const size = Math.ceil(part.length / slices);
  const out: string[] = [];
  for (let i = 0; i < part.length; i += size) out.push(part.slice(i, i + size));
  return out;
}

export function refineLipsync(track: LipsyncTrack): LipsyncTrack {
  const words: string[] = [];
  const wtimes: number[] = [];
  const wdurations: number[] = [];

  const push = (w: string, t: number, d: number) => {
    if (d <= 0) return;
    words.push(w);
    wtimes.push(Math.round(t));
    wdurations.push(Math.round(d));
  };

  for (let i = 0; i < track.words.length; i++) {
    const raw = track.words[i] ?? "";
    const start = track.wtimes[i] ?? 0;
    const duration = track.wdurations[i] ?? 0;
    if (!raw.trim() || duration <= 0) continue;

    const { core, punct } = stripPunctuation(raw);
    // La ponctuation occupe la fin du mot : on lui laisse une petite fenêtre.
    const punctMs = punct ? Math.min(90, duration * 0.2) : 0;
    const coreMs = duration - punctMs;

    if (core) {
      if (coreMs > MAX_SEGMENT_MS) {
        const parts = splitSyllables(core);
        const letters = parts.reduce((n, p) => n + Math.max(1, p.length), 0);
        let cursor = start;
        for (const part of parts) {
          const share = (Math.max(1, part.length) / letters) * coreMs;
          const slices = splitLong(part, share);
          const sliceMs = share / slices.length;
          for (const slice of slices) {
            // Bilabiale : micro-fermeture juste avant, la bouche « claque ».
            if (/^[bpm]/i.test(slice) && sliceMs > BILABIAL_MS * 2) {
              push("", cursor, BILABIAL_MS);
              push(slice, cursor + BILABIAL_MS, sliceMs - BILABIAL_MS);
            } else {
              push(slice, cursor, sliceMs);
            }
            cursor += sliceMs;
          }
        }
      } else {
        push(core, start, coreMs);
      }
    }

    // Fermeture de bouche sur la ponctuation.
    if (punct) push("", start + coreMs, punctMs);

    // Silence explicite avant le mot suivant.
    const nextStart = track.wtimes[i + 1];
    if (typeof nextStart === "number") {
      const gap = nextStart - (start + duration);
      if (gap >= SILENCE_MS) push("", start + duration, gap);
    }
  }

  return { words, wtimes, wdurations };
}
