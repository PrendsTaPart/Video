import React from 'react';
import {Easing, Img, interpolate, staticFile, useCurrentFrame} from 'remotion';
import {SceneLayout} from '../components/SceneLayout';
import {AnimatedLine} from '../components/AnimatedLines';
import {COLORS, ENTER_BEZIER} from '../theme';

// S6 · 0:55–1:05 (300f) — L'ÉCOSYSTÈME
// Le bloc FoodEatUp se dédouble en 3 satellites (vrais logos Rapido),
// puis un compteur final.

const easing = Easing.bezier(...ENTER_BEZIER);
const SATELLITES = [
	{name: 'RapidoCRM', logo: 'img/logo-rapidocrm.png'},
	{name: 'RapidoCMS', logo: 'img/logo-rapidocms.png'},
	{name: 'RapidoRH', logo: 'img/logo-rapidorh.png'},
];
const SAT_RADIUS = 260;
const SAT_NODE_SIZE = 150;
const SAT_LABEL_HEIGHT = 0;
// Le nœud du bas (angle 90°) descend de SAT_RADIUS + son propre rayon :
// le conteneur doit être assez haut pour l'inclure, sinon il chevauche
// le texte suivant (compteur final).
const DIAGRAM_HEIGHT = 2 * (SAT_RADIUS + SAT_NODE_SIZE / 2 + 10 + SAT_LABEL_HEIGHT);

const HUB_START = 0;
const SPLIT_START = 20;
const SPLIT_END = 90;
const STAT_START = 190;

export const Scene06: React.FC = () => {
	const frame = useCurrentFrame();
	const hubOpacity = interpolate(frame, [HUB_START, HUB_START + 18], [0, 1], {
		extrapolateLeft: 'clamp',
		extrapolateRight: 'clamp',
	});
	const split = interpolate(frame, [SPLIT_START, SPLIT_END], [0, 1], {
		extrapolateLeft: 'clamp',
		extrapolateRight: 'clamp',
		easing,
	});

	return (
		<SceneLayout background={COLORS.cream}>
			<div style={{display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 66}}>
				<div style={{position: 'relative', width: SAT_RADIUS * 2 + 260, height: DIAGRAM_HEIGHT}}>
					<svg
						width="100%"
						height="100%"
						style={{position: 'absolute', top: 0, left: 0, overflow: 'visible'}}
					>
						{SATELLITES.map((_, i) => {
							const angle = (i / (SATELLITES.length - 1)) * Math.PI * 0.7 + Math.PI * 0.15;
							const x = Math.cos(angle) * SAT_RADIUS * split;
							const y = Math.sin(angle) * SAT_RADIUS * split;
							return (
								<line
									key={i}
									x1="50%"
									y1="50%"
									x2={`calc(50% + ${x}px)`}
									y2={`calc(50% + ${y}px)`}
									stroke={COLORS.primary}
									strokeWidth={2}
									strokeDasharray="6 10"
									opacity={split}
								/>
							);
						})}
					</svg>
					{SATELLITES.map(({name, logo}, i) => {
						const angle = (i / (SATELLITES.length - 1)) * Math.PI * 0.7 + Math.PI * 0.15;
						const x = Math.cos(angle) * SAT_RADIUS * split;
						const y = Math.sin(angle) * SAT_RADIUS * split;
						return (
							<div
								key={name}
								style={{
									position: 'absolute',
									left: `calc(50% + ${x}px)`,
									top: `calc(50% + ${y}px)`,
									transform: 'translate(-50%, -50%)',
									opacity: split,
								}}
							>
								<div
									style={{
										width: SAT_NODE_SIZE,
										height: SAT_NODE_SIZE,
										borderRadius: '50%',
										border: `2px solid ${COLORS.primary}`,
										backgroundColor: COLORS.white,
										display: 'flex',
										alignItems: 'center',
										justifyContent: 'center',
										padding: 20,
										boxSizing: 'border-box',
									}}
								>
									<Img
										src={staticFile(logo)}
										style={{width: '100%', height: '100%', objectFit: 'contain'}}
									/>
								</div>
							</div>
						);
					})}
					<div
						style={{
							position: 'absolute',
							left: '50%',
							top: '50%',
							transform: 'translate(-50%, -50%)',
							width: 200,
							height: 200,
							borderRadius: '50%',
							backgroundColor: COLORS.white,
							border: `3px solid ${COLORS.primary}`,
							opacity: hubOpacity,
							display: 'flex',
							flexDirection: 'column',
							alignItems: 'center',
							justifyContent: 'center',
							gap: 6,
						}}
					>
						<Img src={staticFile('img/official-mark-8.png')} style={{height: 64}} />
						<span style={{color: COLORS.navy, fontSize: 22, fontWeight: 700}}>FoodEatUp</span>
					</div>
				</div>

				<AnimatedLine lineIndex={0} startFrame={STAT_START}>
					<span style={{color: COLORS.primary, fontSize: 48, fontWeight: 700}}>
						Une même famille · 4 logiciels · 1 agent
					</span>
				</AnimatedLine>
			</div>
		</SceneLayout>
	);
};
