import React from 'react';
import {staticFile} from 'remotion';
import {SceneLayout} from '../components/SceneLayout';
import {AvatarBubble} from '../components/AvatarBubble';
import {AnimatedLine} from '../components/AnimatedLines';
import {COLORS} from '../theme';

// S0 · 0:00–0:10 (300f) — INTRO AVATAR
// Bulle vidéo circulaire (avatar HeyGen réel, fourni par l'utilisateur) qui
// présente la vidéo avant que le pitch (ex-S1) ne démarre. Durée calée sur
// le clip source (9,24 s) + pop-in et fondu de sortie.
const BUBBLE_START = 6;
const LABEL_START = 0;
const TAGLINE_START = 40;

export const Scene00: React.FC = () => {
	return (
		<SceneLayout background={COLORS.cream}>
			<div style={{display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 36}}>
				<AnimatedLine lineIndex={0} startFrame={LABEL_START}>
					<span
						style={{
							color: COLORS.primary,
							fontSize: 34,
							fontWeight: 700,
							letterSpacing: 2,
							textTransform: 'uppercase',
						}}
					>
						FoodEatUp
					</span>
				</AnimatedLine>

				<AvatarBubble src={staticFile('video/avatar-intro.mp4')} size={620} startFrame={BUBBLE_START} />

				<AnimatedLine lineIndex={0} startFrame={TAGLINE_START}>
					<span style={{color: COLORS.navy, fontSize: 46, fontWeight: 600, textAlign: 'center'}}>
						On vous explique tout, en direct.
					</span>
				</AnimatedLine>
			</div>
		</SceneLayout>
	);
};
