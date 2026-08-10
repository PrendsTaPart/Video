import { Config } from "@remotion/cli/config";

Config.setVideoImageFormat("png");   // png : indispensable pour l'export alpha
Config.setOverwriteOutput(true);
Config.setChromiumOpenGlRenderer("angle");

Config.setEntryPoint("src/index.ts");
