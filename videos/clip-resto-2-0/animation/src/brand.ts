// FoodEatUp brand constants — rapido-kb/charte-graphique.md (Brandbook, mai 2025).
// No colour outside this palette may appear in the animations.
export const C = {
  marine: '#0F1A23',   // fond principal, imposé par la charte
  bleu:   '#007BFF',   // primaire : logo, CTA, motif toque
  creme:  '#FCF9E6',   // fonds clairs, texte sur marine
  orange: '#FFA500',   // accent : validation, liseré
  noir:   '#231F20',   // texte sur fond coloré (règle d'accessibilité)
  bleuClair: '#A6D0FF',
};

// Goodly is the official face but is not in this repo; the charter itself
// designates Poppins as the substitute until the .ttf is delivered.
export const FONT = 'Poppins, system-ui, sans-serif';

export const FPS = 30;
export const W = 1920;
export const H = 1080;

// Logo protection zone: half the logo height (the charter also asks for 10 % of
// its width — keep the larger of the two).
export const protection = (logoH: number, logoW: number) =>
  Math.max(logoH / 2, logoW * 0.1);

export const easeOutCubic = (t: number) => 1 - Math.pow(1 - t, 3);
export const easeInOutCubic = (t: number) =>
  t < 0.5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2;
