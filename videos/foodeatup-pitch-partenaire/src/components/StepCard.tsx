import React from 'react';
import {Easing, Img, interpolate, staticFile, useCurrentFrame, useVideoConfig} from 'remotion';
import {CheckMark} from './CheckMark';
import {COLORS, ENTER_BEZIER, MS, msToFrames} from '../theme';

const easing = Easing.bezier(...ENTER_BEZIER);

/**
 * Carte d'étape qui "s'allume" au passage de son tour (bordure + fond
 * passent à l'accent bleu), puis affiche une coche. Utilisée pour la
 * chaîne séquentielle de la scène 4. Le badge affiche une image produit
 * réelle quand `imageSrc` est fourni, sinon le numéro d'étape.
 */
export const StepCard: React.FC<{
	index: number;
	label: string;
	startFrame: number;
	stepDurationMs?: number;
	imageSrc?: string;
}> = ({index, label, startFrame, stepDurationMs = MS.cardDuration, imageSrc}) => {
	const frame = useCurrentFrame();
	const {fps} = useVideoConfig();
	const stepFrames = msToFrames(stepDurationMs, fps);
	const localStart = startFrame + index * stepFrames;

	const activation = interpolate(frame, [localStart, localStart + stepFrames * 0.5], [0, 1], {
		extrapolateLeft: 'clamp',
		extrapolateRight: 'clamp',
		easing,
	});
	const checkProgress = interpolate(
		frame,
		[localStart + stepFrames * 0.5, localStart + stepFrames],
		[0, 1],
		{extrapolateLeft: 'clamp', extrapolateRight: 'clamp', easing},
	);
	const entrance = interpolate(frame, [localStart, localStart + stepFrames * 0.3], [0, 1], {
		extrapolateLeft: 'clamp',
		extrapolateRight: 'clamp',
		easing,
	});

	const background = activation > 0 ? COLORS.primary : 'transparent';

	return (
		<div
			style={{
				flex: 1,
				display: 'flex',
				flexDirection: 'column',
				alignItems: 'center',
				justifyContent: 'space-between',
				gap: 22,
				padding: '32px 22px',
				borderRadius: 24,
				border: `2px solid ${activation > 0 ? COLORS.primary : 'rgba(15,26,35,0.14)'}`,
				backgroundColor: activation > 0 ? 'rgba(0,123,255,0.10)' : COLORS.creamDeep,
				opacity: interpolate(entrance, [0, 1], [0, 1]),
				transform: `translateY(${interpolate(entrance, [0, 1], [16, 0])}px)`,
				minHeight: 340,
				boxSizing: 'border-box',
			}}
		>
			<div style={{position: 'relative', width: 108, height: 108, flexShrink: 0}}>
				{imageSrc ? (
					<div
						style={{
							width: 108,
							height: 108,
							borderRadius: 20,
							overflow: 'hidden',
							border: `2px solid ${COLORS.primary}`,
							backgroundColor: COLORS.white,
							display: 'flex',
							alignItems: 'center',
							justifyContent: 'center',
						}}
					>
						<Img src={staticFile(imageSrc)} style={{width: '100%', height: '100%', objectFit: 'cover'}} />
					</div>
				) : (
					<div
						style={{
							width: 108,
							height: 108,
							borderRadius: '50%',
							display: 'flex',
							alignItems: 'center',
							justifyContent: 'center',
							backgroundColor: background,
							border: `2px solid ${COLORS.primary}`,
						}}
					>
						<span style={{color: activation > 0 ? COLORS.white : COLORS.primary, fontSize: 40, fontWeight: 700}}>
							{index + 1}
						</span>
					</div>
				)}
				{imageSrc ? (
					<div
						style={{
							position: 'absolute',
							right: -8,
							bottom: -8,
							width: 40,
							height: 40,
							borderRadius: '50%',
							backgroundColor: background,
							border: `2px solid ${COLORS.white}`,
							display: 'flex',
							alignItems: 'center',
							justifyContent: 'center',
						}}
					>
						<span style={{color: activation > 0 ? COLORS.white : COLORS.primary, fontSize: 18, fontWeight: 700}}>
							{index + 1}
						</span>
					</div>
				) : null}
			</div>
			<div
				style={{
					color: COLORS.navy,
					fontSize: 42,
					fontWeight: 600,
					textAlign: 'center',
					lineHeight: 1.25,
				}}
			>
				{label}
			</div>
			<div style={{height: 40, display: 'flex', alignItems: 'center'}}>
				{checkProgress > 0 ? <CheckMark progress={checkProgress} size={40} color={COLORS.primary} /> : null}
			</div>
		</div>
	);
};
