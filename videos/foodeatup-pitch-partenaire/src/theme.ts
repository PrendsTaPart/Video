// Charte FoodEatUp — alignée sur les couleurs réelles de site.foodeatup.com
// (extraites de assets/styles-*.css — tokens --surface, --surface-alt,
// --surface-dark, --brand, --ink). Le site est à dominante CLAIRE : fond
// blanc/blanc cassé, texte foncé, bleu en accent. Le navy ne sert plus de
// fond de scène par défaut — seulement de couleur de texte / accent foncé
// ponctuel, comme sur le site.
export const COLORS = {
	primary: '#147AFF',
	white: '#FFFFFF',
	offwhite: '#F2F7FF',
	navy: '#0F172B',
	// Couleurs d'accent secondaires, utilisées uniquement pour des petits
	// éléments ponctuels (badges d'intégration, cf. site) — jamais comme
	// fond ni comme couleur de texte principale.
	whatsappGreen: '#25D366',
	successGreen: '#1EB857',
} as const;

export const FONT_FAMILY = '"Trebuchet MS", sans-serif';

// Échelle typographique agrandie par rapport au premier jet (lisibilité
// écran + impact pitch partenaire).
export const TYPE = {
	display: 96,
	h1: 64,
	h2: 48,
	body: 34,
	label: 26,
} as const;

// Grille 12 colonnes, marge 120 px (sur une composition 1920x1080).
export const GRID = {
	width: 1920,
	height: 1080,
	margin: 120,
	columns: 12,
} as const;

export const CONTENT_WIDTH = GRID.width - GRID.margin * 2;

// Easing des entrées de texte : cubic-bezier(0.16, 1, 0.3, 1).
export const ENTER_BEZIER: [number, number, number, number] = [0.16, 1, 0.3, 1];

// Durées de la grammaire motion, en millisecondes.
export const MS = {
	textEnterDuration: 400,
	textEnterStagger: 80,
	counterDuration: 700,
	cardDuration: 500,
} as const;

export const msToFrames = (ms: number, fps: number): number => (ms / 1000) * fps;
