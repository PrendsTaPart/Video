import React from 'react';
import {interpolate, useCurrentFrame, useVideoConfig} from 'remotion';
import {msToFrames} from '../theme';

/** Révèle le texte caractère par caractère à un débit fixe (ms/caractère). */
export const Typewriter: React.FC<{
	text: string;
	startFrame?: number;
	msPerChar?: number;
	style?: React.CSSProperties;
}> = ({text, startFrame = 0, msPerChar = 45, style}) => {
	const frame = useCurrentFrame();
	const {fps} = useVideoConfig();
	const framesPerChar = msToFrames(msPerChar, fps);
	const visibleChars = Math.max(
		0,
		Math.floor(interpolate(frame, [startFrame, startFrame + text.length * framesPerChar], [0, text.length], {
			extrapolateLeft: 'clamp',
			extrapolateRight: 'clamp',
		})),
	);
	return <span style={style}>{text.slice(0, visibleChars)}</span>;
};
