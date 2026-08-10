import React from 'react';
import {Audio, Series, staticFile} from 'remotion';
import {Scene00} from './scenes/Scene00';
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

// Découpage du storyboard, 30fps. S0 = intro avatar HeyGen (audio inclus
// dans le clip, pas de piste séparée). S1-S12 portent chacune une piste VO
// ElevenLabs (public/audio/vo-sXX.mp3) ; leur durée en frames a été recalée
// sur la durée réelle de la voix générée (+buffer) plutôt que sur l'estimation
// au mot approximative utilisée pour les sous-titres — certaines scènes
// (S3, S8 notamment) avaient largement sous-estimé le temps de lecture réel.
export const SCENES = [
	{name: 'S0 Intro avatar', frames: 300, Component: Scene00, audio: null},
	{name: 'S1 Hook', frames: 210, Component: Scene01, audio: 'audio/vo-s01.mp3'},
	{name: 'S2 Le problème', frames: 355, Component: Scene02, audio: 'audio/vo-s02.mp3'},
	{name: 'S3 Le renversement', frames: 454, Component: Scene03, audio: 'audio/vo-s03.mp3'},
	{name: 'S4 Cas d’usage signature', frames: 420, Component: Scene04, audio: 'audio/vo-s04.mp3'},
	{name: 'S5 La plateforme', frames: 390, Component: Scene05, audio: 'audio/vo-s05.mp3'},
	{name: 'S6 L’écosystème', frames: 339, Component: Scene06, audio: 'audio/vo-s06.mp3'},
	{name: 'S7 La confiance', frames: 376, Component: Scene07, audio: 'audio/vo-s07.mp3'},
	{name: 'S8 La preuve', frames: 558, Component: Scene08, audio: 'audio/vo-s08.mp3'},
	{name: 'S9 Les 3 portes d’entrée', frames: 420, Component: Scene09, audio: 'audio/vo-s09.mp3'},
	{name: 'S10 L’économie du partenariat', frames: 373, Component: Scene10, audio: 'audio/vo-s10.mp3'},
	{name: 'S11 Pourquoi maintenant', frames: 210, Component: Scene11, audio: 'audio/vo-s11.mp3'},
	{name: 'S12 Clôture', frames: 90, Component: Scene12, audio: 'audio/vo-s12.mp3'},
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
				{SCENES.map(({name, frames, Component, audio}) => (
					<Series.Sequence key={name} durationInFrames={frames} layout="none">
						<Component />
						{audio ? <Audio src={staticFile(audio)} /> : null}
					</Series.Sequence>
				))}
			</Series>
		</>
	);
};
