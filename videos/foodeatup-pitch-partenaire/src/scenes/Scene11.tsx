import React from 'react';
import {Easing, interpolate, useCurrentFrame} from 'remotion';
import {SceneLayout} from '../components/SceneLayout';
import {AnimatedLines} from '../components/AnimatedLines';
import {COLORS, ENTER_BEZIER} from '../theme';

// S11 · 1:50–1:57 (210f) — POURQUOI MAINTENANT
// Une fenêtre lumineuse qui s'ouvre sur fond clair, puis trois lignes courtes.

const easing = Easing.bezier(...ENTER_BEZIER);
const WINDOW_OPEN_START = 0;
const WINDOW_OPEN_END = 36;
const TEXT_START = 46;

export const Scene11: React.FC = () => {
	const frame = useCurrentFrame();
	const openT = interpolate(frame, [WINDOW_OPEN_START, WINDOW_OPEN_END], [0, 1], {
		extrapolateLeft: 'clamp',
		extrapolateRight: 'clamp',
		easing,
	});

	return (
		<SceneLayout background={COLORS.cream}>
			<div
				style={{
					position: 'relative',
					width: 1400,
					padding: '80px 90px',
					borderRadius: 28,
					border: `2px solid ${COLORS.primary}`,
					backgroundColor: COLORS.creamDeep,
					boxShadow: `0 0 ${interpolate(openT, [0, 1], [0, 90])}px rgba(0,123,255,${interpolate(openT, [0, 1], [0, 0.35])})`,
					transform: `scaleX(${openT})`,
					transformOrigin: 'center',
					boxSizing: 'border-box',
				}}
			>
				<AnimatedLines
					lines={[
						'2026 : la bascule agentique',
						'Aucun leader sur l’agent vocal',
						'Les géants US absents en France et au Maghreb',
					]}
					startFrame={TEXT_START}
					gap={26}
					lineStyle={{
						color: COLORS.navy,
						fontSize: 42,
						fontWeight: 600,
					}}
				/>
			</div>
		</SceneLayout>
	);
};
