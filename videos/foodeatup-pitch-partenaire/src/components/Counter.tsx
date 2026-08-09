import React from 'react';
import {Easing, interpolate, useCurrentFrame, useVideoConfig} from 'remotion';
import {ENTER_BEZIER, MS, msToFrames} from '../theme';

const easing = Easing.bezier(...ENTER_BEZIER);

/**
 * Chiffre clé : compte de 0 à la valeur cible sur 700ms puis se fige.
 * Un seul compteur à l'écran à la fois (règle de grammaire motion).
 */
export const Counter: React.FC<{
	target: number;
	startFrame?: number;
	prefix?: string;
	suffix?: string;
	style?: React.CSSProperties;
}> = ({target, startFrame = 0, prefix = '', suffix = '', style}) => {
	const frame = useCurrentFrame();
	const {fps} = useVideoConfig();
	const duration = msToFrames(MS.counterDuration, fps);
	const value = interpolate(frame, [startFrame, startFrame + duration], [0, target], {
		extrapolateLeft: 'clamp',
		extrapolateRight: 'clamp',
		easing,
	});
	const rounded = Math.round(value);
	return (
		<span style={style}>
			{prefix}
			{rounded.toLocaleString('fr-FR')}
			{suffix}
		</span>
	);
};
