import React from "react";
import { Composition } from "remotion";
import { Sting, defauts, StingProps } from "./Sting";

const FPS = 30;
const DUREE = 5 * FPS;

/**
 * Une composition par livrable. Les props sont les mêmes partout : c'est ce qui
 * permet de rejouer le sting pour une autre marque Rapido en changeant la
 * baseline, la couleur d'accent et le logo, sans toucher au code.
 */
export const RemotionRoot: React.FC = () => (
  <>
    <Composition
      id="sting-1080x1920"
      component={Sting}
      durationInFrames={DUREE}
      fps={FPS}
      width={1080}
      height={1920}
      defaultProps={defauts}
    />
    <Composition
      id="sting-1920x1080"
      component={Sting}
      durationInFrames={DUREE}
      fps={FPS}
      width={1920}
      height={1080}
      defaultProps={defauts}
    />
    <Composition
      id="sting-1080x1080"
      component={Sting}
      durationInFrames={DUREE}
      fps={FPS}
      width={1080}
      height={1080}
      defaultProps={defauts}
    />
    {/* fond transparent : pour incruster le sting sur une vidéo existante */}
    <Composition
      id="sting-alpha"
      component={Sting}
      durationInFrames={DUREE}
      fps={FPS}
      width={1080}
      height={1920}
      defaultProps={{ ...defauts, transparent: true } as StingProps}
    />
    {/* les 3 premières secondes seules : la boucle du logo, sans l'outro.
        Bouclable — l'animation part du noir et y revient. */}
    <Composition
      id="sting-loop-3s"
      component={Sting}
      durationInFrames={3 * FPS}
      fps={FPS}
      width={1080}
      height={1920}
      defaultProps={{ ...defauts, avecVo: false, boucle: true } as StingProps}
    />
  </>
);
