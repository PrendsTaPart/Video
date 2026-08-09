import React from 'react';
import {Easing, Img, interpolate, staticFile, useCurrentFrame} from 'remotion';
import {SceneLayout} from '../components/SceneLayout';
import {Typewriter} from '../components/Typewriter';
import {AnimatedLine} from '../components/AnimatedLines';
import {COLORS, ENTER_BEZIER} from '../theme';

// S1 · 0:00–0:07 (210f) — HOOK
// Photo du produit évoqué (le saumon) pour ancrer le message dans le
// concret, bulle de conversation typée caractère par caractère, puis sous
// la bulle, en bleu, la révélation.
const MESSAGE = 'On a un surplus de saumon. Écoule-le.';
const REVEAL = '4 logiciels viennent de s’exécuter.';

const IMAGE_START = 0;
const BUBBLE_START = 12;
const REVEAL_START = 120;

const easing = Easing.bezier(...ENTER_BEZIER);

export const Scene01: React.FC = () => {
	const frame = useCurrentFrame();
	const bubbleVisible = frame >= BUBBLE_START;
	const imageT = interpolate(frame, [IMAGE_START, IMAGE_START + 18], [0, 1], {
		extrapolateLeft: 'clamp',
		extrapolateRight: 'clamp',
		easing,
	});

	return (
		<SceneLayout background={COLORS.cream}>
			<div
				style={{
					display: 'flex',
					flexDirection: 'row',
					alignItems: 'center',
					gap: 90,
					width: '100%',
				}}
			>
				<div
					style={{
						opacity: imageT,
						transform: `translateX(${interpolate(imageT, [0, 1], [-24, 0])}px)`,
						width: 480,
						height: 640,
						borderRadius: 32,
						overflow: 'hidden',
						border: `2px solid ${COLORS.primary}`,
						flexShrink: 0,
						boxShadow: '0 20px 50px -20px rgba(15,26,35,0.25)',
					}}
				>
					<Img
						src={staticFile('img/saumon.jpg')}
						style={{width: '100%', height: '100%', objectFit: 'cover'}}
					/>
				</div>
				<div
					style={{
						display: 'flex',
						flexDirection: 'column',
						gap: 40,
						flex: 1,
					}}
				>
					<div
						style={{
							opacity: bubbleVisible ? 1 : 0,
							backgroundColor: COLORS.creamDeep,
							border: `2px solid rgba(15,26,35,0.16)`,
							borderRadius: 28,
							borderBottomLeftRadius: 6,
							padding: '36px 48px',
							minHeight: 96,
							display: 'flex',
							alignItems: 'center',
						}}
					>
						<Typewriter
							text={MESSAGE}
							startFrame={BUBBLE_START}
							msPerChar={55}
							style={{
								color: COLORS.navy,
								fontSize: 56,
								fontWeight: 600,
							}}
						/>
					</div>
					<AnimatedLine lineIndex={0} startFrame={REVEAL_START}>
						<span
							style={{
								color: COLORS.primary,
								fontSize: 50,
								fontWeight: 700,
							}}
						>
							{REVEAL}
						</span>
					</AnimatedLine>
				</div>
			</div>
		</SceneLayout>
	);
};
