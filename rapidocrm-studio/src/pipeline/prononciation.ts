/**
 * Pré-traitement du texte avant envoi à ElevenLabs. La forme chiffrée reste
 * affichée à l'écran ; seule la voix reçoit la version développée.
 */

const SIGLES: Record<string, string> = {
  CRM: 'C.R.M.',
  CMS: 'C.M.S.',
  TVA: 'T.V.A.',
  PDF: 'P.D.F.',
  IA: 'I.A.',
  MCP: 'M.C.P.',
  RH: 'R.H.',
  API: 'A.P.I.',
  URL: 'U.R.L.',
  SMS: 'S.M.S.',
  KPI: 'K.P.I.',
  HT: 'hors taxes',
  TTC: 'toutes taxes comprises',
  // SIRET, SIREN, IBAN se prononcent tels quels — volontairement absents.
};

const UNITES = [
  'zéro', 'un', 'deux', 'trois', 'quatre', 'cinq', 'six', 'sept', 'huit', 'neuf',
  'dix', 'onze', 'douze', 'treize', 'quatorze', 'quinze', 'seize', 'dix-sept',
  'dix-huit', 'dix-neuf',
];
const DIZAINES = [
  '', '', 'vingt', 'trente', 'quarante', 'cinquante', 'soixante', 'soixante',
  'quatre-vingt', 'quatre-vingt',
];

/** Un entier en toutes lettres, jusqu'au million. */
export const enLettres = (n: number): string => {
  if (n < 0) return `moins ${enLettres(-n)}`;
  if (n < 20) return UNITES[n] as string;
  if (n < 100) {
    const d = Math.floor(n / 10);
    const u = n % 10;
    if (d === 7 || d === 9) {
      return `${DIZAINES[d]}-${UNITES[10 + u]}`;
    }
    if (u === 0) return `${DIZAINES[d]}${d === 8 ? 's' : ''}`;
    if (u === 1 && d !== 8) return `${DIZAINES[d]} et un`;
    return `${DIZAINES[d]}-${UNITES[u]}`;
  }
  if (n < 1000) {
    const c = Math.floor(n / 100);
    const reste = n % 100;
    const tete = c === 1 ? 'cent' : `${UNITES[c]} cent${reste === 0 ? 's' : ''}`;
    return reste === 0 ? tete : `${tete} ${enLettres(reste)}`;
  }
  if (n < 1_000_000) {
    const m = Math.floor(n / 1000);
    const reste = n % 1000;
    const tete = m === 1 ? 'mille' : `${enLettres(m)} mille`;
    return reste === 0 ? tete : `${tete} ${enLettres(reste)}`;
  }
  const m = Math.floor(n / 1_000_000);
  const reste = n % 1_000_000;
  const tete = m === 1 ? 'un million' : `${enLettres(m)} millions`;
  return reste === 0 ? tete : `${tete} ${enLettres(reste)}`;
};

/** « 1 240 € » → « mille deux cent quarante euros ». */
export const montantsEnLettres = (texte: string): string =>
  texte.replace(
    /(\d[\d  ]*)(?:,(\d{1,2}))?\s*(€|euros?)/gi,
    (_tout, entier: string, centimes: string | undefined) => {
      const n = Number(entier.replace(/[\s ]/g, ''));
      const base = `${enLettres(n)} euro${n > 1 ? 's' : ''}`;
      if (!centimes) return base;
      const c = Number(centimes.padEnd(2, '0'));
      return c === 0 ? base : `${base} ${enLettres(c)}`;
    },
  );

export const developperSigles = (texte: string): string =>
  texte.replace(/\b[A-Z]{2,5}\b/g, (sigle) => SIGLES[sigle] ?? sigle);

/**
 * Texte prêt pour la synthèse : sigles développés, montants en lettres,
 * pauses entre les phrases longues.
 */
export const pourLaVoix = (texte: string, pauseFinale = true): string => {
  let sortie = developperSigles(montantsEnLettres(texte.trim()));
  sortie = sortie.replace(/\s{2,}/g, ' ');
  // Un sigle développé en fin de phrase laisse un point en trop : « C.R.M.. »
  sortie = sortie.replace(/\.\.(?=\s|$)/g, '.');
  return pauseFinale ? `${sortie} <break time="0.4s" />` : sortie;
};
