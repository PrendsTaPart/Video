/**
 * Charte Claude (Anthropic), utilisée UNIQUEMENT par la carte prompt de la
 * séquence 4.
 *
 * C'est une exception assumée à la règle « Arial et la palette RapidoSoftware
 * partout » : cette carte représente Claude, pas RapidoCRM. Elle porte donc les
 * couleurs et la typographie d'Anthropic, comme une capture d'écran porterait
 * celles du logiciel qu'elle montre. Le reste de la frame reste à la charte
 * RapidoSoftware.
 */
export const CLAUDE = {
  colors: {
    sombre: '#141413', // texte principal
    clair: '#faf9f5', // fond de la carte
    grisMoyen: '#b0aea5',
    grisClair: '#e8e6dc',
    orange: '#d97757', // accent principal
    bleu: '#6a9bcc',
    vert: '#788c5d',
  },
  /** Titres : Poppins, Arial en repli. */
  policeTitre: 'Poppins, Arial, Helvetica, sans-serif',
  /** Corps : Lora, Georgia en repli. */
  policeCorps: 'Lora, Georgia, serif',
  radius: 20,
} as const;

/** Chemin staticFile du logo Claude. */
export const LOGO_CLAUDE = 'ia/claude.png';
