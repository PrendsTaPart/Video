import {Easing, interpolate, useCurrentFrame, useVideoConfig} from 'remotion';
import {ENTER_BEZIER, MS, msToFrames} from '../theme';

const easing = Easing.bezier(...ENTER_BEZIER);

/**
 * Grammaire d'entrée commune : translation verticale 24px + opacité,
 * cubic-bezier(0.16, 1, 0.3, 1), 400ms, décalage de 80ms entre lignes.
 * `lineIndex` = position de l'élément dans la séquence d'apparition (0, 1, 2...).
 * `startFrame` = frame locale à la scène où l'entrée commence.
 */
export const useEnterStyle = (
	lineIndex: number,
	startFrame = 0,
): {opacity: number; transform: string} => {
	const frame = useCurrentFrame();
	const {fps} = useVideoConfig();
	const duration = msToFrames(MS.textEnterDuration, fps);
	const stagger = msToFrames(MS.textEnterStagger, fps);
	const localStart = startFrame + lineIndex * stagger;
	const t = interpolate(frame, [localStart, localStart + duration], [0, 1], {
		extrapolateLeft: 'clamp',
		extrapolateRight: 'clamp',
		easing,
	});
	const translateY = interpolate(t, [0, 1], [24, 0]);
	return {
		opacity: t,
		transform: `translateY(${translateY}px)`,
	};
};

/** Même grammaire, mais pilotée directement en frames absolues (utile hors texte). */
export const enterProgress = (
	frame: number,
	fps: number,
	startFrame: number,
	lineIndex = 0,
): number => {
	const duration = msToFrames(MS.textEnterDuration, fps);
	const stagger = msToFrames(MS.textEnterStagger, fps);
	const localStart = startFrame + lineIndex * stagger;
	return interpolate(frame, [localStart, localStart + duration], [0, 1], {
		extrapolateLeft: 'clamp',
		extrapolateRight: 'clamp',
		easing,
	});
};
