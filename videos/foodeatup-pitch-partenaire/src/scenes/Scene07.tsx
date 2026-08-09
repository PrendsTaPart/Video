import React from 'react';
import {Easing, Img, interpolate, staticFile, useCurrentFrame} from 'remotion';
import {SceneLayout} from '../components/SceneLayout';
import {AnimatedLine} from '../components/AnimatedLines';
import {Pill} from '../components/Pill';
import {useEnterStyle} from '../components/enter';
import {COLORS, ENTER_BEZIER} from '../theme';

// S7 · 1:05–1:16 (330f) — LA CONFIANCE
// Gauche : bandeau "Confirmer ?" avec un curseur qui valide.
// Droite : quatre badges de conformité. Bas : aperçu réel du module HACCP.

const easing = Easing.bezier(...ENTER_BEZIER);
// 4 points vérifiés dans /conformite du dépôt du site — le module de
// caisse (NF525) est explicitement "en développement, pas encore
// commercialisé" et n'est donc PAS un badge de conformité acquis :
// on affiche à la place les 4 garanties déjà en place aujourd'hui.
const BADGES = ['RGPD', 'HACCP', 'Sécurité', 'Réversibilité'];

const TITLE_START = 0;
const SLIDER_START = 40;
const SLIDER_END = 90;
const BADGES_START = 70;
const SCREENSHOT_START = 150;

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
			<Pill label={label} active style={{fontSize: 42}} />
		</div>
	);
};

const ScreenshotInset: React.FC = () => {
	const enter = useEnterStyle(0, SCREENSHOT_START);
	return (
		<div
			style={{
				opacity: enter.opacity,
				transform: enter.transform,
				width: 520,
				borderRadius: 16,
				overflow: 'hidden',
				border: `2px solid ${COLORS.primary}`,
				boxShadow: '0 20px 50px -20px rgba(15,26,35,0.3)',
				backgroundColor: COLORS.white,
			}}
		>
			<div
				style={{
					display: 'flex',
					alignItems: 'center',
					gap: 8,
					padding: '10px 14px',
					backgroundColor: COLORS.creamDeep,
				}}
			>
				{[COLORS.primary, COLORS.navy, COLORS.primary].map((c, i) => (
					<div
						key={i}
						style={{width: 10, height: 10, borderRadius: '50%', backgroundColor: c, opacity: 0.5}}
					/>
				))}
			</div>
			<Img
				src={staticFile('img/screenshot-haccp-modules.png')}
				style={{width: '100%', display: 'block'}}
			/>
		</div>
	);
};

export const Scene07: React.FC = () => {
	return (
		<SceneLayout background={COLORS.cream}>
			<div style={{display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 40, width: '100%'}}>
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
							<span style={{color: COLORS.navy, fontSize: 78, fontWeight: 700}}>Confirmer ?</span>
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
				<ScreenshotInset />
			</div>
		</SceneLayout>
	);
};
