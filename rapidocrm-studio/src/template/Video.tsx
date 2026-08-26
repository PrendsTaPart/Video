import React from 'react';
import { AbsoluteFill, Audio, Sequence, staticFile } from 'remotion';
import { BRAND } from '../brand/tokens.ts';
import type { PropsVideo } from '../schema/index.ts';
import { calculerMinutage } from './minutage.ts';
import { Demo } from './sequences/Demo.tsx';
import { Ouverture } from './sequences/Ouverture.tsx';
import { Hook } from './sequences/Hook.tsx';
import { Punchline } from './sequences/Punchline.tsx';
import { SegmentClaude } from './sequences/SegmentClaude.tsx';
import { TitreSeq } from './sequences/TitreSeq.tsx';

/**
 * Le montage complet. Aucun texte en dur : tout vient de script.json.
 */
export const Video: React.FC<PropsVideo & { vertical?: boolean }> = ({
  script,
  alignement,
  demoSegments,
  demoSrc,
  vignetteSrc,
  audioSrc,
  vertical = false,
}) => {
  const minutage = calculerMinutage(script, alignement);

  return (
    <AbsoluteFill style={{ backgroundColor: BRAND.colors.fondClair }}>
      {/* La voix off démarre au hook : l'ouverture est muette. */}
      {audioSrc && (
        <Sequence from={minutage.hook.debut}>
          <Audio src={staticFile(audioSrc)} />
        </Sequence>
      )}

      <Sequence from={minutage.ouverture.debut} durationInFrames={minutage.ouverture.duree}>
        <Ouverture script={script} vignetteSrc={vignetteSrc} />
      </Sequence>

      <Sequence from={minutage.hook.debut} durationInFrames={minutage.hook.duree}>
        <Hook script={script} vertical={vertical} />
      </Sequence>

      <Sequence from={minutage.titre.debut} durationInFrames={minutage.titre.duree}>
        <TitreSeq script={script} vertical={vertical} />
      </Sequence>

      <Sequence from={minutage.demo.debut} durationInFrames={minutage.demo.duree}>
        <Demo
          script={script}
          alignement={alignement}
          minutage={minutage}
          demoSegments={demoSegments}
          demoSrc={demoSrc}
          vertical={vertical}
        />
      </Sequence>

      <Sequence from={minutage.claude.debut} durationInFrames={minutage.claude.duree}>
        <SegmentClaude script={script} vertical={vertical} />
      </Sequence>

      <Sequence from={minutage.punchline.debut} durationInFrames={minutage.punchline.duree}>
        <Punchline script={script} vertical={vertical} />
      </Sequence>
    </AbsoluteFill>
  );
};
