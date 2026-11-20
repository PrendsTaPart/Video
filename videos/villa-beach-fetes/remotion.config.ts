import {Config} from '@remotion/cli/config';

// Les images, le logo et les musiques sont lus dans assets/ (staticFile).
Config.setPublicDir('assets');
Config.setVideoImageFormat('jpeg');
Config.setJpegQuality(92);
Config.setCodec('h264');
Config.setCrf(18);
