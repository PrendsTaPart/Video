import React from 'react';
import {Series} from 'remotion';
import {Scene01} from './scenes/Scene01';
import {Scene02} from './scenes/Scene02';
import {Scene03} from './scenes/Scene03';
import {Scene04} from './scenes/Scene04';
import {Scene05} from './scenes/Scene05';
import {Scene06} from './scenes/Scene06';
import {Scene07} from './scenes/Scene07';
import {Scene08} from './scenes/Scene08';
import {Scene09} from './scenes/Scene09';
import {Scene10} from './scenes/Scene10';
import {Scene11} from './scenes/Scene11';
import {Scene12} from './scenes/Scene12';

// Découpage exact du storyboard, 30fps — total 3600 frames (2:00).
export const SCENES = [
	{name: 'S1 Hook', frames: 210, Component: Scene01},
	{name: 'S2 Le problème', frames: 330, Component: Scene02},
	{name: 'S3 Le renversement', frames: 300, Component: Scene03},
	{name: 'S4 Cas d’usage signature', frames: 420, Component: Scene04},
	{name: 'S5 La plateforme', frames: 390, Component: Scene05},
	{name: 'S6 L’écosystème', frames: 300, Component: Scene06},
	{name: 'S7 La confiance', frames: 330, Component: Scene07},
	{name: 'S8 La preuve', frames: 300, Component: Scene08},
	{name: 'S9 Les 3 portes d’entrée', frames: 420, Component: Scene09},
	{name: 'S10 L’économie du partenariat', frames: 300, Component: Scene10},
	{name: 'S11 Pourquoi maintenant', frames: 210, Component: Scene11},
	{name: 'S12 Clôture', frames: 90, Component: Scene12},
] as const;

export const Main: React.FC = () => {
	return (
		<>
			{/*
			 * public/music.mp3 est volontairement vide (piste non sourcée
			 * interdite). Une fois le fichier fourni, décommenter :
			 * <Audio src={staticFile('music.mp3')} volume={0.5} />
			 */}
			<Series>
				{SCENES.map(({name, frames, Component}) => (
					<Series.Sequence key={name} durationInFrames={frames} layout="none">
						<Component />
					</Series.Sequence>
				))}
			</Series>
		</>
	);
};
