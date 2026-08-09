// Charte graphique OFFICIELLE FoodEatUp (PDF de marque de Michael), confirmée
// à l'identique par deux sources indépendantes : le repo de doc produit
// (foodeatup-guide-star, src/styles.css + README) et studio-video/CLAUDE.md.
// Fond crème (sable) par défaut, texte marine, bleu en accent primaire,
// orange en accent secondaire (CTA, badges, surlignages).
export const COLORS = {
	cream: '#FCF9E6',
	creamDeep: '#F5F0D4',
	navy: '#0F1A23',
	primary: '#007BFF',
	orange: '#FFA500',
	white: '#FFFFFF',
	// Couleurs d'accent tertiaires, utilisées uniquement pour des petits
	// éléments ponctuels (badges d'intégration) — jamais comme fond ni
	// comme couleur de texte principale.
	whatsappGreen: '#25D366',
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
