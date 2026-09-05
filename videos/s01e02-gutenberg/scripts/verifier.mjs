#!/usr/bin/env node
// Les contrôles de la série, appliqués à cet épisode.
import { EP, ROOT, OUT, FFMPEG, sonder, s2 } from "./outils.mjs";
import { verifier } from "../../module-methode-rapidocms/scripts/verifier.mjs";

const ecarts = verifier({ EP, ROOT, OUT, FFMPEG, sonder, s2 });
if (ecarts.length) process.exitCode = 1;
