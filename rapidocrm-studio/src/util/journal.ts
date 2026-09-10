import { appendFileSync } from 'node:fs';
import { join } from 'node:path';

const couleurs = {
  gris: '\x1b[90m',
  vert: '\x1b[32m',
  jaune: '\x1b[33m',
  rouge: '\x1b[31m',
  reset: '\x1b[0m',
};

export const info = (msg: string): void => console.log(msg);
export const etape = (msg: string): void =>
  console.log(`${couleurs.vert}▸${couleurs.reset} ${msg}`);
export const avertir = (msg: string): void =>
  console.log(`${couleurs.jaune}⚠ ${msg}${couleurs.reset}`);
export const erreur = (msg: string): void =>
  console.error(`${couleurs.rouge}✖ ${msg}${couleurs.reset}`);
export const discret = (msg: string): void =>
  console.log(`${couleurs.gris}${msg}${couleurs.reset}`);

/** Journal persistant : content/<module>/<Vxx>/pipeline.log */
export const consigner = (dossier: string, ligne: string): void => {
  const horodatage = new Date().toISOString();
  appendFileSync(join(dossier, 'pipeline.log'), `${horodatage}  ${ligne}\n`, 'utf8');
};

export const chronometrer = async <T>(
  dossier: string,
  nom: string,
  action: () => Promise<T>,
): Promise<T> => {
  const debut = Date.now();
  etape(nom);
  try {
    const resultat = await action();
    const duree = ((Date.now() - debut) / 1000).toFixed(1);
    consigner(dossier, `${nom} — OK en ${duree}s`);
    discret(`   ${nom} terminé en ${duree}s`);
    return resultat;
  } catch (e) {
    const duree = ((Date.now() - debut) / 1000).toFixed(1);
    consigner(dossier, `${nom} — ÉCHEC après ${duree}s : ${(e as Error).message}`);
    throw e;
  }
};
