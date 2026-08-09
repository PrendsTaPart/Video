import React from 'react';
import {Easing, interpolate, useCurrentFrame} from 'remotion';
import {SceneLayout} from '../components/SceneLayout';
import {AnimatedLine} from '../components/AnimatedLines';
import {Pill} from '../components/Pill';
import {useEnterStyle} from '../components/enter';
import {COLORS, ENTER_BEZIER} from '../theme';

// S7 · 1:05–1:16 (330f) — LA CONFIANCE
// Gauche : bandeau "Confirmer ?" avec un curseur qui valide.
// Droite : quatre badges de conformité.

const easing = Easing.bezier(...ENTER_BEZIER);
const BADGES = ['NF525', 'TVA', 'DSN', 'HACCP'];

const TITLE_START = 0;
const SLIDER_START = 40;
const SLIDER_END = 90;
const BADGES_START = 70;

const ConfirmSlider: React.FC = () => {
	const frame = useCurrentFrame();
	const t = interpolate(frame, [SLIDER_START, SLIDER_END], [0, 1], {
		extrapolateLeft: 'clamp',
		extrapolateRight: 'clamp',
		easing,
	});
	const trackWidth = 200;
	const thumbSize = 64;
	const thumbX = interpolate(t, [0, 1], [4, trackWidth - thumbSize - 4]);
	return (
		<div
			style={{
				position: 'relative',
				width: trackWidth,
				height: thumbSize + 8,
				borderRadius: 999,
				border: `2px solid ${COLORS.primary}`,
				backgroundColor: t > 0.05 ? 'rgba(0,123,255,0.14)' : COLORS.creamDeep,
			}}
		>
			<div
				style={{
					position: 'absolute',
					left: thumbX,
					top: 4,
					width: thumbSize,
					height: thumbSize,
					borderRadius: '50%',
					backgroundColor: COLORS.primary,
				}}
			/>
		</div>
	);
};

const Badge: React.FC<{label: string; index: number}> = ({label, index}) => {
	const enter = useEnterStyle(index, BADGES_START);
	return (
		<div style={{opacity: enter.opacity, transform: enter.transform}}>
			<Pill label={label} active style={{fontSize: 36}} />
		</div>
	);
};

export const Scene07: React.FC = () => {
	return (
		<SceneLayout background={COLORS.cream}>
			<div
				style={{
					display: 'flex',
					flexDirection: 'row',
					width: '100%',
					alignItems: 'center',
					justifyContent: 'space-between',
				}}
			>
				<div
					style={{
						flex: 1,
						display: 'flex',
						flexDirection: 'column',
						alignItems: 'flex-start',
						gap: 44,
					}}
				>
					<AnimatedLine lineIndex={0} startFrame={TITLE_START}>
						<span style={{color: COLORS.navy, fontSize: 66, fontWeight: 700}}>Confirmer ?</span>
					</AnimatedLine>
					<ConfirmSlider />
				</div>
				<div
					style={{
						flex: 1,
						display: 'flex',
						flexDirection: 'column',
						alignItems: 'flex-end',
						gap: 24,
					}}
				>
					{BADGES.map((b, i) => (
						<Badge key={b} label={b} index={i} />
					))}
				</div>
			</div>
		</SceneLayout>
	);
};
