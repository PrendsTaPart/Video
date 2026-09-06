import { copyFileSync, createWriteStream, existsSync, mkdirSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { pipeline } from 'node:stream/promises';
import { Readable } from 'node:stream';
import { racineProjet } from '../util/chemins.ts';

/**
 * Les logos officiels. Ils sont TÉLÉCHARGÉS, jamais redessinés.
 */
export const LOGOS = {
  rapidosoftware:
    'https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/bibliotheque/6ESIjTLJsdnZSZeIZqnCRCXXqaopVPwibCO4QGJr.png',
  rapidocrm:
    'https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/bibliotheque/CGuynobcv7eF4yFZLvARq1GU0KLqA5bVlcfYxJgx.png',
  rapidocms:
    'https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/bibliotheque/Xzu3D6aqmouslq55LYhOR5iAPnmKxqoQJ6UuvG0P.png',
  rapidorh:
    'https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/bibliotheque/VOlevQVkp7sfjObvcYfRtCMsqKb1oW4ujuo1vt9a.png',
} as const;

export type NomLogo = keyof typeof LOGOS;

export const cheminLogo = (nom: NomLogo): string =>
  join(racineProjet(), 'assets', 'logos', `${nom}.png`);

/** Télécharge les logos manquants. Appelé au premier lancement du pipeline. */
export const assurerLogos = async (): Promise<void> => {
  for (const [nom, url] of Object.entries(LOGOS) as [NomLogo, string][]) {
    const dest = cheminLogo(nom);
    if (existsSync(dest)) continue;
    mkdirSync(dirname(dest), { recursive: true });
    const reponse = await fetch(url);
    if (!reponse.ok || !reponse.body) {
      throw new Error(`Téléchargement du logo ${nom} impossible : HTTP ${reponse.status}`);
    }
    await pipeline(Readable.fromWeb(reponse.body as never), createWriteStream(dest));
    console.log(`  logo téléchargé : ${nom}.png`);
  }
};

/**
 * Le logo monté en fin de vidéo, copié dans `public/logos/`.
 *
 * La marque fournit `assets/logos/rapidocrm-complet.png`, mais `assets/logos/`
 * est ignoré par git : sur un clone neuf, le fichier n'existe pas et le rendu
 * échouait à la carte de fin sur un 404. Le repli est le logo officiel
 * `rapidocrm.png`, qui porte déjà le logomark et la signature — téléchargé
 * depuis la bibliothèque de la marque, jamais redessiné.
 */
export const installerLogoComplet = (racinePublic: string): void => {
  const destination = join(racinePublic, 'logos', 'rapidocrm-complet.png');
  const fourni = join(racineProjet(), 'assets', 'logos', 'rapidocrm-complet.png');
  copyFileSync(existsSync(fourni) ? fourni : cheminLogo('rapidocrm'), destination);
};
