import React from 'react';
import { Composition, Still } from 'remotion';
import { PropsVideoSchema, type PropsVideo } from '../schema/index.ts';
import { FPS, calculerMinutage } from './minutage.ts';
import { SCRIPT_FACTICE } from './donnees-factices.ts';
import { Video } from './Video.tsx';
import { Vignette } from './Vignette.tsx';

const defauts: PropsVideo = {
  script: SCRIPT_FACTICE,
  alignement: null,
  demoSegments: [],
  demoSrc: null,
  vignetteSrc: null,
  avatarSrc: null,
  audioSrc: null,
};

const duree = (props: PropsVideo): number => calculerMinutage(props.script, props.alignement).total;

export const RemotionRoot: React.FC = () => (
  <>
    <Composition
      id="Tutoriel16x9"
      component={Video}
      width={1920}
      height={1080}
      fps={FPS}
      schema={PropsVideoSchema}
      defaultProps={defauts}
      durationInFrames={duree(defauts)}
      calculateMetadata={({ props }) => ({ durationInFrames: duree(props as PropsVideo) })}
    />

    <Composition
      id="Tutoriel9x16"
      component={Video}
      width={1080}
      height={1920}
      fps={FPS}
      schema={PropsVideoSchema}
      defaultProps={{ ...defauts, vertical: true } as PropsVideo}
      durationInFrames={duree(defauts)}
      calculateMetadata={({ props }) => ({ durationInFrames: duree(props as PropsVideo) })}
    />

    {/* Prévisualisation du template : séquences 1, 2, 4 et 5, sans vidéo source. */}
    {/* Prévisualisation du template : un écran RapidoCRM réel tient lieu de
        plan de démonstration, pour juger le cadre, le zoom et les annotations. */}
    <Composition
      id="Preview"
      component={Video}
      width={1920}
      height={1080}
      fps={FPS}
      defaultProps={{ ...defauts, demoSrc: 'ecrans/liste-commerciaux.webp' }}
      durationInFrames={duree(defauts)}
    />

    <Still
      id="Vignette16x9"
      component={Vignette as unknown as React.FC<Record<string, unknown>>}
      width={1280}
      height={720}
      defaultProps={{ script: SCRIPT_FACTICE, captureSrc: null, vertical: false }}
    />
    <Still
      id="Vignette9x16"
      component={Vignette as unknown as React.FC<Record<string, unknown>>}
      width={1080}
      height={1920}
      defaultProps={{ script: SCRIPT_FACTICE, captureSrc: null, vertical: true }}
    />
  </>
);
