import React from 'react';
import {Composition, staticFile} from 'remotion';
import {Opening} from './Opening';
import {Closing} from './Closing';
import {LogoFlash, InfinityLoop} from './Overlays';
import {OpeningV, ClosingV} from './Portrait';
import {W, H, FPS} from './brand';

// Goodly is the official face; the charter designates Poppins as the substitute
// until the .ttf is delivered, so the animations ship in Poppins.
const fontCss = `
@font-face{font-family:'Poppins';font-weight:400;src:url('${staticFile('fonts/Poppins-400.ttf')}') format('truetype');}
@font-face{font-family:'Poppins';font-weight:600;src:url('${staticFile('fonts/Poppins-600.ttf')}') format('truetype');}
@font-face{font-family:'Poppins';font-weight:700;src:url('${staticFile('fonts/Poppins-700.ttf')}') format('truetype');}
@font-face{font-family:'Poppins';font-weight:800;src:url('${staticFile('fonts/Poppins-800.ttf')}') format('truetype');}
`;

export const RemotionRoot: React.FC = () => (
  <>
    <style dangerouslySetInnerHTML={{__html: fontCss}} />
    <Composition id="Opening" component={Opening} durationInFrames={333} fps={FPS} width={W} height={H} />
    <Composition id="OpeningV" component={OpeningV} durationInFrames={333} fps={FPS} width={1080} height={1920} />
    <Composition id="ClosingV" component={ClosingV} durationInFrames={487} fps={FPS} width={1080} height={1920} />
    <Composition id="LogoFlashV" component={LogoFlash} durationInFrames={5} fps={FPS} width={1080} height={1920} />
    <Composition id="InfinityLoopV" component={InfinityLoop} durationInFrames={46} fps={FPS} width={1080} height={1920} />
    <Composition id="LogoFlash" component={LogoFlash} durationInFrames={5} fps={FPS} width={W} height={H} />
    <Composition id="InfinityLoop" component={InfinityLoop} durationInFrames={46} fps={FPS} width={W} height={H} />
    <Composition id="Closing" component={Closing} durationInFrames={487} fps={FPS} width={W} height={H} />
  </>
);
