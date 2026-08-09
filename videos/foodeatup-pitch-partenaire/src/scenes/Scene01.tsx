import React from 'react';
import {useCurrentFrame} from 'remotion';
import {SceneLayout} from '../components/SceneLayout';
import {Typewriter} from '../components/Typewriter';
import {AnimatedLine} from '../components/AnimatedLines';
import {COLORS} from '../theme';

// S1 · 0:00–0:07 (210f) — HOOK
// Bulle de conversation typée caractère par caractère, puis sous la bulle,
// en bleu, la révélation.
const MESSAGE = 'On a un surplus de saumon. Écoule-le.';
const REVEAL = '4 logiciels viennent de s’exécuter.';

const BUBBLE_START = 12;
const REVEAL_START = 120;

export const Scene01: React.FC = () => {
	const frame = useCurrentFrame();
	const bubbleVisible = frame >= BUBBLE_START;

	return (
		<SceneLayout background={COLORS.white}>
			<div
				style={{
					display: 'flex',
					flexDirection: 'column',
					alignItems: 'center',
					gap: 40,
					maxWidth: 1280,
				}}
			>
				<div
					style={{
						opacity: bubbleVisible ? 1 : 0,
						backgroundColor: COLORS.offwhite,
						border: `2px solid rgba(15,23,43,0.16)`,
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
							fontSize: 52,
							fontWeight: 600,
						}}
					/>
				</div>
				<AnimatedLine lineIndex={0} startFrame={REVEAL_START}>
					<span
						style={{
							color: COLORS.primary,
							fontSize: 42,
							fontWeight: 700,
						}}
					>
						{REVEAL}
					</span>
				</AnimatedLine>
			</div>
		</SceneLayout>
	);
};
