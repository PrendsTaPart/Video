// Construit le tracé de l'infini FoodEatUp en UN path SVG continu.
//
// Mesuré sur foodeatup-infinity.png : 73 x 146, trait de 11 px, deux lobes de
// même diamètre centrés en y = 40 et y = 108, qui se croisent à mi-hauteur.
//
// Deux cercles parcourus d'un seul trait, en partant du croisement : boucle du
// haut, retour au croisement, boucle du bas, retour au point de départ. Un seul
// M, quatre arcs, aucune levée de plume — c'est ce qui rend getTotalLength()
// continu et donc stroke-dashoffset exploitable.
//
// Une lemniscate de Gerono a été essayée d'abord : ses lobes sont pincés en
// sablier, là où le sigle a deux anneaux ronds. Écartée.
import { writeFileSync } from "node:fs";

const CX = 36.5, CY = 73, R = 31;
const HAUT = CY - 2 * R;   // sommet du lobe supérieur
const BAS = CY + 2 * R;    // pointe du lobe inférieur

// sweep 1 puis 0 : les deux boucles tournent en sens inverse, ce qui produit le
// croisement en huit au lieu de deux cercles empilés.
const d = [
  `M${CX},${CY}`,
  `A${R},${R} 0 1 1 ${CX},${HAUT}`,
  `A${R},${R} 0 1 1 ${CX},${CY}`,
  `A${R},${R} 0 1 0 ${CX},${BAS}`,
  `A${R},${R} 0 1 0 ${CX},${CY}`,
  "Z",
].join(" ");

writeFileSync(new URL("../src/infinity-path.ts", import.meta.url),
  `// Généré par scripts/gen-lemniscate.mjs — ne pas éditer à la main.\n` +
  `export const INFINITY_PATH =\n  "${d}";\n` +
  `export const INFINITY_VIEWBOX = "0 0 73 146";\n` +
  `export const INFINITY_STROKE = 11;\n` +
  `export const INFINITY_CROISEMENT = { x: ${CX}, y: ${CY} };\n`);

writeFileSync(new URL("../out/lemniscate-apercu.svg", import.meta.url),
  `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 73 146" width="146" height="292">` +
  `<path d="${d}" fill="none" stroke="#0070E8" stroke-width="11" stroke-linecap="round"/></svg>`);

console.log(`path : ${d}`);
