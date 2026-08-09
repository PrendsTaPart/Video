import React from 'react';
import {Easing, interpolate, useCurrentFrame} from 'remotion';
import {SceneLayout} from '../components/SceneLayout';
import {AnimatedLines} from '../components/AnimatedLines';
import {ToolIcon} from '../components/ToolIcon';
import {COLORS} from '../theme';

// S3 · 0:18–0:28 (300f) — LE RENVERSEMENT
// Les icônes éparses convergent vers un point central étiqueté "MCP".

// cubic-bezier(0.16,1,0.3,1) est réservé à la grammaire des entrées de
// texte (impulsions courtes, 400ms) : appliquée à une convergence spatiale
// de 2-3s, cette courbe est trop agressive (~94% du trajet fait dans les
// 40 premiers % du temps). On utilise ici un ease-in-out classique, plus
// adapté à un mouvement continu.
const easing = Easing.inOut(Easing.cubic);
const ICON_COUNT = 8;
const RADIUS = 380;

const scattered = Array.from({length: ICON_COUNT}, (_, i) => {
	const angle = (i / ICON_COUNT) * Math.PI * 2 - Math.PI / 2;
	return {x: Math.cos(angle) * RADIUS, y: Math.sin(angle) * RADIUS};
});

const HUB_START = 0;
const CONVERGE_START = 20;
const CONVERGE_END = 120;
const TEXT_START = 150;
const HUB_SIZE = 168;

export const Scene03: React.FC = () => {
	const frame = useCurrentFrame();
	const hubOpacity = interpolate(frame, [HUB_START, HUB_START + 18], [0, 1], {
		extrapolateLeft: 'clamp',
		extrapolateRight: 'clamp',
	});
	const converge = interpolate(frame, [CONVERGE_START, CONVERGE_END], [0, 1], {
		extrapolateLeft: 'clamp',
		extrapolateRight: 'clamp',
		easing,
	});

	return (
		<SceneLayout background={COLORS.cream}>
			<div
				style={{
					display: 'flex',
					flexDirection: 'column',
					alignItems: 'center',
					gap: 90,
				}}
			>
				<div style={{position: 'relative', width: RADIUS * 2 + 56, height: RADIUS * 2 + 56}}>
					{scattered.map((p, i) => {
						const x = interpolate(converge, [0, 1], [p.x, 0]);
						const y = interpolate(converge, [0, 1], [p.y, 0]);
						// L'icône se fond dans le hub dès qu'elle atteint son
						// bord : fondu piloté par la distance réelle au centre
						// (et non par une fenêtre de temps), pour rester
						// synchronisé quelle que soit la courbe d'accélération.
						const distance = Math.hypot(x, y);
						const opacity = interpolate(
							distance,
							[HUB_SIZE / 2, HUB_SIZE / 2 + 70],
							[0, 1],
							{extrapolateLeft: 'clamp', extrapolateRight: 'clamp'},
						);
						return (
							<div
								key={i}
								style={{
									position: 'absolute',
									left: '50%',
									top: '50%',
									transform: `translate(${x - 28}px, ${y - 28}px)`,
									opacity,
								}}
							>
								<ToolIcon size={56} />
							</div>
						);
					})}
					<div
						style={{
							position: 'absolute',
							left: '50%',
							top: '50%',
							transform: 'translate(-50%, -50%)',
							width: HUB_SIZE,
							height: HUB_SIZE,
							borderRadius: '50%',
							backgroundColor: COLORS.primary,
							opacity: hubOpacity,
							display: 'flex',
							alignItems: 'center',
							justifyContent: 'center',
						}}
					>
						<span style={{color: COLORS.white, fontSize: 46, fontWeight: 700}}>MCP</span>
					</div>
				</div>

				<AnimatedLines
					lines={['L’IA ne conseille pas. Elle exécute.']}
					startFrame={TEXT_START}
					lineStyle={{
						color: COLORS.navy,
						fontSize: 66,
						fontWeight: 700,
						textAlign: 'center',
					}}
				/>
			</div>
		</SceneLayout>
	);
};
