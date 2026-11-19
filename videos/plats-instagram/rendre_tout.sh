#!/bin/bash
# rend les 9 habillages, 3 à la fois
cd "$(dirname "$0")"
ls cfg/*.js | xargs -n1 basename | sed 's/\.js$//' | xargs -P3 -I{} sh -c 'node rendre.js {} && echo "{} rendu"'
