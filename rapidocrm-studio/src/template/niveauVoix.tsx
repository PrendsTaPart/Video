import React from 'react';
import { useAudioData, visualizeAudio } from '@remotion/media-utils';
import { staticFile, useCurrentFrame, useVideoConfig } from 'remotion';

/**
 * Niveau sonore de la voix off à la frame courante, entre 0 et 1.
 *
 * Il pilote la bulle du présentateur — anneau, halo, barres. Le hook exige une
 * piste : `NiveauVoix` ci-dessous fait le branchement pour les appelants qui
 * n'en ont pas toujours une, un hook ne pouvant pas être conditionnel.
 */
export const useNiveauVoix = (audioSrc: string): number => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const donnees = useAudioData(staticFile(audioSrc));

  if (!donnees) return 0;

  const bandes = visualizeAudio({
    fps,
    frame,
    audioData: donnees,
    numberOfSamples: 16,
  });
  // Moyenne des basses et médiums : la voix y vit, les aigus font du bruit.
  const utiles = bandes.slice(1, 9);
  const moyenne = utiles.reduce((s, v) => s + v, 0) / utiles.length;
  return Math.min(1, moyenne * 5);
};

/**
 * Rend ses enfants avec le niveau de la voix, ou zéro s'il n'y a pas de piste.
 */
export const NiveauVoix: React.FC<{
  audioSrc: string | null;
  children: (niveau: number) => React.ReactNode;
}> = ({ audioSrc, children }) =>
  audioSrc ? (
    <AvecPiste audioSrc={audioSrc}>{children}</AvecPiste>
  ) : (
    <>{children(0)}</>
  );

const AvecPiste: React.FC<{
  audioSrc: string;
  children: (niveau: number) => React.ReactNode;
}> = ({ audioSrc, children }) => <>{children(useNiveauVoix(audioSrc))}</>;
