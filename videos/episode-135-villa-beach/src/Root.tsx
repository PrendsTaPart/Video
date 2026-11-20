import React from 'react';
import {Composition} from 'remotion';
import {Episode} from './Episode';
import {DUREE, episode} from './data/episode';

export const Root: React.FC = () => (
  <Composition id="episode-135" component={Episode} durationInFrames={DUREE * episode.fps} fps={episode.fps} width={1080} height={1920} />
);
