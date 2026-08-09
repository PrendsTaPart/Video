import React from 'react';
import {interpolate, useCurrentFrame} from 'remotion';
import {SceneLayout} from '../components/SceneLayout';
import {AnimatedLine} from '../components/AnimatedLines';
import {Counter} from '../components/Counter';
import {ToolIcon} from '../components/ToolIcon';
import {COLORS} from '../theme';

// S2 · 0:07–0:18 (330f) — LE PROBLÈME
// 10 icônes dispersées, reliées par des traits en pointillés qui se
// rompent un à un ; trois chiffres apparaissent ensuite en séquence.

const ICON_COLS = 5;
const ROW_GAP = 190;
const COL_GAP = 190;

const positions = Array.from({length: 10}, (_, i) => {
	const row = Math.floor(i / ICON_COLS);
	const col = i % ICON_COLS;
	return {x: col * COL_GAP, y: row * ROW_GAP};
});

// 8 liens : 4 par rangée (snake gauche→droite).
const LINKS = [
	[0, 1],
	[1, 2],
	[2, 3],
	[3, 4],
	[5, 6],
	[6, 7],
	[7, 8],
	[8, 9],
] as const;

const BREAK_START = 6;
const BREAK_STEP = 16;

const STATS = [
	{kind: 'counter' as const, prefix: '', suffix: ' outils', target: 10, start: 40},
	{kind: 'text' as const, label: '1 à 2 h perdues par jour', start: 160},
	{kind: 'text' as const, label: 'Des appels manqués', start: 250},
];

const activeStatIndex = (frame: number): number => {
	let active = 0;
	STATS.forEach((s, i) => {
		if (frame >= s.start) active = i;
	});
	return active;
};

export const Scene02: React.FC = () => {
	const frame = useCurrentFrame();
	const width = (ICON_COLS - 1) * COL_GAP;
	const height = ROW_GAP;
	const active = activeStatIndex(frame);
	const activeStat = STATS[active];

	return (
		<SceneLayout background={COLORS.white}>
			<div style={{display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 90}}>
				<div style={{position: 'relative', width, height}}>
					<svg
						width={width}
						height={height}
						style={{position: 'absolute', top: 0, left: 0, overflow: 'visible'}}
					>
						{LINKS.map(([a, b], i) => {
							const pa = positions[a];
							const pb = positions[b];
							const breakFrame = BREAK_START + i * BREAK_STEP;
							const broken = interpolate(frame, [breakFrame, breakFrame + 10], [0, 1], {
								extrapolateLeft: 'clamp',
								extrapolateRight: 'clamp',
							});
							return (
								<line
									key={`${a}-${b}`}
									x1={pa.x}
									y1={pa.y}
									x2={pb.x}
									y2={pb.y}
									stroke={COLORS.navy}
									strokeWidth={2}
									strokeDasharray="6 10"
									opacity={interpolate(broken, [0, 1], [0.45, 0])}
								/>
							);
						})}
					</svg>
					{positions.map((p, i) => (
						<div
							key={i}
							style={{
								position: 'absolute',
								left: p.x - 28,
								top: p.y - 28,
							}}
						>
							<ToolIcon size={56} opacity={0.9} />
						</div>
					))}
				</div>

				<div style={{height: 90, display: 'flex', alignItems: 'center', justifyContent: 'center'}}>
					<AnimatedLine lineIndex={0} startFrame={activeStat.start}>
						{activeStat.kind === 'counter' ? (
							<span style={{color: COLORS.primary, fontSize: 76, fontWeight: 700}}>
								<Counter
									target={activeStat.target}
									startFrame={activeStat.start}
									suffix={activeStat.suffix}
								/>
							</span>
						) : (
							<span style={{color: COLORS.primary, fontSize: 56, fontWeight: 700}}>
								{activeStat.label}
							</span>
						)}
					</AnimatedLine>
				</div>
			</div>
		</SceneLayout>
	);
};
