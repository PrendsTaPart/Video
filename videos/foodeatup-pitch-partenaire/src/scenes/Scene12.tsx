import React from 'react';
import {Img, staticFile} from 'remotion';
import {SceneLayout} from '../components/SceneLayout';
import {AnimatedLine} from '../components/AnimatedLines';
import {COLORS} from '../theme';

// S12 · 1:57–2:00 (90f) — CLÔTURE (fond blanc cassé)
// Logo FoodEatUp (asset officiel de marque), slogan, URL. Rien d'autre.
export const Scene12: React.FC = () => {
	return (
		<SceneLayout background={COLORS.offwhite}>
			<div style={{display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 44}}>
				<AnimatedLine lineIndex={0} startFrame={0}>
					<Img src={staticFile('img/official-logo-horizontal.png')} style={{height: 96}} />
				</AnimatedLine>
				<AnimatedLine lineIndex={1} startFrame={0}>
					<span
						style={{
							color: COLORS.navy,
							fontSize: 38,
							fontWeight: 600,
							textAlign: 'center',
						}}
					>
						Une infinité de solutions pour gérer votre restaurant.
					</span>
				</AnimatedLine>
				<AnimatedLine lineIndex={2} startFrame={0}>
					<span style={{color: COLORS.primary, fontSize: 30, fontWeight: 600}}>
						site.foodeatup.com
					</span>
				</AnimatedLine>
			</div>
		</SceneLayout>
	);
};
