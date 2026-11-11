import { existsSync, mkdirSync, readFileSync, readdirSync, writeFileSync } from 'node:fs';
import { dirname, isAbsolute, join, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

export const racineProjet = (): string =>
  resolve(dirname(fileURLToPath(import.meta.url)), '..', '..');

export const racineContenu = (): string => join(racineProjet(), 'content');

/**
 * Résout un tutoriel, soit par chemin direct, soit par (module, numéro).
 * `content/<module>/<Vxx-slug>/`
 */
export const dossierTutoriel = (chemin: string): string => {
  const abs = isAbsolute(chemin) ? chemin : resolve(process.cwd(), chemin);
  if (!existsSync(abs)) {
    throw new Error(`Dossier de tutoriel introuvable : ${abs}`);
  }
  return abs;
};

export const resoudreParModule = (module: string, numero: number): string => {
  const base = join(racineContenu(), module);
  if (!existsSync(base)) {
    throw new Error(`Module inconnu : ${module} (attendu dans ${racineContenu()})`);
  }
  const prefixe = `V${String(numero).padStart(2, '0')}`;
  const trouve = readdirSync(base).find((d) => d.startsWith(prefixe));
  if (!trouve) {
    throw new Error(`Tutoriel ${prefixe} introuvable dans le module ${module}`);
  }
  return join(base, trouve);
};

export const lireJson = <T>(chemin: string): T =>
  JSON.parse(readFileSync(chemin, 'utf8')) as T;

export const ecrireJson = (chemin: string, valeur: unknown): void => {
  mkdirSync(dirname(chemin), { recursive: true });
  writeFileSync(chemin, `${JSON.stringify(valeur, null, 2)}\n`, 'utf8');
};

export const assurerDossier = (chemin: string): string => {
  mkdirSync(chemin, { recursive: true });
  return chemin;
};

export const fichierExiste = (chemin: string): boolean => existsSync(chemin);
