/**
 * Charte RapidoSoftware — source unique des couleurs, de la typo et des règles
 * de contraste. Rien n'est codé en dur ailleurs.
 */

export const BRAND = {
  colors: {
    grisPrimaire: '#383838', // texte, titres, usage général — R56 V56 B56
    vert: '#4CAF50', // RapidoCRM — couleur dominante — R76 V175 B80
    violet: '#7E57C2', // RapidoRH — contrepoint — R126 V87 B194
    bleu: '#03A9F5', // RapidoCMS — accent tertiaire — R3 V169 B245
    fondClair: '#F2F4F7',
    blanc: '#FFFFFF',
  },
  font: 'Arial, Helvetica, sans-serif', // police unique de la charte, aucune autre
  radius: 24,
} as const;

export type BrandColor = (typeof BRAND.colors)[keyof typeof BRAND.colors];

/** Les seuls fonds sur lesquels un élément de marque peut être posé. */
export const FONDS_AUTORISES: string[] = [
  BRAND.colors.blanc,
  BRAND.colors.fondClair,
  BRAND.colors.vert,
  BRAND.colors.violet,
  BRAND.colors.bleu,
  BRAND.colors.grisPrimaire,
];

export const PALETTE: string[] = Object.values(BRAND.colors);

const normalise = (hex: string): string => {
  const h = hex.trim().toUpperCase();
  if (/^#[0-9A-F]{3}$/.test(h)) {
    return `#${h[1]}${h[1]}${h[2]}${h[2]}${h[3]}${h[3]}`;
  }
  return h;
};

export const estCouleurDeCharte = (hex: string): boolean =>
  PALETTE.map(normalise).includes(normalise(hex));

const LUMINANCES: Record<string, number> = {
  '#383838': 0.045,
  '#4CAF50': 0.34,
  '#7E57C2': 0.15,
  '#03A9F5': 0.34,
  '#F2F4F7': 0.9,
  '#FFFFFF': 1,
};

/**
 * Règle de contraste de la charte : sur un aplat, le texte est UNIQUEMENT blanc
 * ou #383838. Jamais de texte coloré sur fond coloré.
 * Utilisée partout — ne jamais écrire une couleur de texte à la main.
 */
export const textOn = (bg: string): string => {
  const cle = normalise(bg);
  const l = LUMINANCES[cle];
  if (l === undefined) {
    throw new Error(
      `textOn: « ${bg} » n'est pas une couleur de la charte RapidoSoftware. ` +
        `Fonds autorisés : ${PALETTE.join(', ')}`,
    );
  }
  return l > 0.5 ? BRAND.colors.grisPrimaire : BRAND.colors.blanc;
};

/** Couleur associée à un module du catalogue (pastilles, badges). */
export const couleurModule = (module: string): string => {
  const m = module.toLowerCase();
  if (m.includes('rh') || m.includes('ressources')) return BRAND.colors.violet;
  if (m.includes('cms') || m.includes('site') || m.includes('marketing')) {
    return BRAND.colors.bleu;
  }
  return BRAND.colors.vert; // RapidoCRM par défaut
};
