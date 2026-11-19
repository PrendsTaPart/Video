import React from 'react';
import {Composition} from 'remotion';
import {MenuVideo} from './components/MenuVideo';
import {Teaser} from './components/Teaser';
import {durees, tempo} from './data/fetes';

const fps = tempo.fps;

// Six compositions : deux menus (9:16), deux teasers (9:16), deux menus en post Instagram (4:5).
export const Root: React.FC = () => (
  <>
    <Composition id="noel-menu-9x16" component={MenuVideo} durationInFrames={durees.menu * fps} fps={fps} width={1080} height={1920} defaultProps={{fete: 'noel' as const}} />
    <Composition id="nouvel-an-menu-9x16" component={MenuVideo} durationInFrames={durees.menu * fps} fps={fps} width={1080} height={1920} defaultProps={{fete: 'nye' as const}} />
    <Composition id="noel-teaser-9x16" component={Teaser} durationInFrames={durees.teaser * fps} fps={fps} width={1080} height={1920} defaultProps={{fete: 'noel' as const}} />
    <Composition id="nouvel-an-teaser-9x16" component={Teaser} durationInFrames={durees.teaser * fps} fps={fps} width={1080} height={1920} defaultProps={{fete: 'nye' as const}} />
    <Composition id="noel-menu-4x5" component={MenuVideo} durationInFrames={durees.menu * fps} fps={fps} width={1080} height={1350} defaultProps={{fete: 'noel' as const}} />
    <Composition id="nouvel-an-menu-4x5" component={MenuVideo} durationInFrames={durees.menu * fps} fps={fps} width={1080} height={1350} defaultProps={{fete: 'nye' as const}} />
  </>
);
