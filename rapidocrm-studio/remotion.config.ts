import { Config } from '@remotion/cli/config';

Config.setVideoImageFormat('jpeg');
Config.setCodec('h264');
Config.setCrf(18);
Config.setConcurrency(4);
Config.setChromiumOpenGlRenderer('angle');
Config.setEntryPoint('src/template/index.ts');
