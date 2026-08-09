import React from 'react';
import {Easing, OffthreadVideo, interpolate, useCurrentFrame} from 'remotion';
import {COLORS, ENTER_BEZIER} from '../theme';

const easing = Easing.bezier(...ENTER_BEZIER);

/**
 * Bulle vidéo circulaire (façon avatar/webcam) pour l'intro présentée par
 * l'avatar HeyGen. Pop-in scale+fade à l'entrée, puis fondu de sortie avant
 * la coupe vers la scène suivante — pas de queue de bulle BD (l'avatar
 * parle lui-même, ce n'est pas une bulle de texte).
 */
export const AvatarBubble: React.FC<{
	src: string;
	size?: number;
	startFrame?: number;
	popDuration?: number;
	fadeOutStart?: number;
	fadeOutDuration?: number;
}> = ({src, size = 620, startFrame = 0, popDuration = 16, fadeOutStart, fadeOutDuration = 24}) => {
	const frame = useCurrentFrame();
	const popT = interpolate(frame, [startFrame, startFrame + popDuration], [0, 1], {
		extrapolateLeft: 'clamp',
		extrapolateRight: 'clamp',
		easing,
	});
	const fadeT =
		fadeOutStart === undefined
			? 1
			: interpolate(frame, [fadeOutStart, fadeOutStart + fadeOutDuration], [1, 0], {
					extrapolateLeft: 'clamp',
					extrapolateRight: 'clamp',
					easing,
				});
	const scale = interpolate(popT, [0, 1], [0.72, 1]);

	return (
		<div
			style={{
				position: 'relative',
				width: size,
				height: size,
				opacity: popT * fadeT,
				transform: `scale(${scale})`,
			}}
		>
			<div
				style={{
					width: '100%',
					height: '100%',
					borderRadius: '50%',
					overflow: 'hidden',
					border: `6px solid ${COLORS.primary}`,
					boxShadow: '0 24px 60px -20px rgba(15,26,35,0.35)',
					backgroundColor: COLORS.white,
				}}
			>
				<OffthreadVideo
					src={src}
					style={{
						width: '100%',
						height: '100%',
						objectFit: 'cover',
						objectPosition: '50% 20%',
					}}
				/>
			</div>
		</div>
	);
};
