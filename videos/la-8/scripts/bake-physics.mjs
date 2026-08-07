// Bakes a REAL physics simulation of the break + a shot-by-shot clearance of the table
// (12 numbered balls potted one at a time, the 8 never touched) using Matter.js.
// Output: compositions/data/physics-data.js — a plain JS file (window.__PHYSICS__ = {...})
// so the HyperFrames compositions can <script src> it with no network fetch, and read
// deterministic per-frame positions instead of hand-scripted GSAP tweens.
//
// Run: node scripts/bake-physics.mjs
import Matter from "matter-js";
import { writeFileSync } from "node:fs";

const { Engine, Bodies, Composite, Body, Vector, Events } = Matter;

const FPS = 30;
const DT_MS = 1000 / 120; // physics substep
const RECORD_EVERY = 4; // 120/4 = 30 recorded samples/sec
const BALL_R = 44;
const CUE_R = 39;

// Table geometry — matches the felt/rail box already used in the compositions
// (left 120 top 90 right 120 bottom 90 on a 1920x1080 canvas, 14px border).
// Rail line sits at x=160/1760, y=140/940; pockets are gaps IN that rail, not
// points behind a solid wall — the wall segments below stop short around each
// pocket so a ball can actually roll through and get captured.
const RAIL = { left: 160, right: 1760, top: 140, bottom: 940 };
const POCKETS = {
  TL: { x: 160, y: 140 },
  TC: { x: 960, y: 140 },
  TR: { x: 1760, y: 140 },
  BL: { x: 160, y: 940 },
  BC: { x: 960, y: 940 },
  BR: { x: 1760, y: 940 },
};
const POCKET_LIST = Object.entries(POCKETS).map(([k, v]) => ({ id: k, ...v }));
const POCKET_CAPTURE_R = 58;
const GAP = 88; // half-width of the pocket opening cut into each rail segment
const BOUNDS = { minX: RAIL.left, maxX: RAIL.right, minY: RAIL.top, maxY: RAIL.bottom };

// ── Rack layout — identical numbering/colors used by the compositions.
// Apex (ball 1) faces the cue (top), the sparse row holding the 3 ghost gaps
// is at the back (bottom) — least disturbed by the break, which is the point.
const CX = 960;
const ROWS_Y = [300, 378, 456, 534, 612];
function rowX(row, col) {
  const count = row + 1;
  const start = CX - ((count - 1) * 88) / 2;
  return start + col * 88;
}
const RACK = [
  { row: 0, col: 0, id: "1", cat: "Caisse & encaissement", c: "#F2C94C" },
  { row: 1, col: 0, id: "2", cat: "Réservation & salle", c: "#2D9CDB" },
  { row: 1, col: 1, id: "3", cat: "Agent vocal téléphonique", c: "#EB5757" },
  { row: 2, col: 0, id: "4", cat: "Food cost & stock", c: "#9B51E0" },
  { row: 2, col: 1, id: "8", cat: "FoodEatUp", c: "#15181d", eight: true },
  { row: 2, col: 2, id: "5", cat: "HACCP", c: "#F2994A" },
  { row: 3, col: 0, id: "6", cat: "Planning & RH", c: "#27AE60" },
  { row: 3, col: 1, id: "7", cat: "Fidélité & animation", c: "#8A3B4E" },
  { row: 3, col: 2, id: "9", cat: "Avis & e-réputation", c: "#F2C94C", stripe: true },
  { row: 3, col: 3, id: "10", cat: "Site & commande en ligne", c: "#2D9CDB", stripe: true },
  { row: 4, col: 0, id: "11", cat: "Messages sortants", c: "#EB5757", stripe: true },
  { row: 4, col: 1, id: "12", cat: "BI, compta & pilotage", c: "#9B51E0", stripe: true },
  // row: 4, col: 2/3/4 — the 3 ghosts. Never physical bodies: they don't even
  // get hit by the break because they were never on the table.
];
RACK.forEach((b) => {
  b.x = rowX(b.row, b.col);
  b.y = ROWS_Y[b.row];
});

const engine = Engine.create({ gravity: { x: 0, y: 0 } });
const world = engine.world;

let watchId = null;
Events.on(engine, "collisionStart", (evt) => {
  if (!watchId || !process.env.DEBUG_COLLIDE) return;
  for (const pair of evt.pairs) {
    const a = pair.bodyA,
      b = pair.bodyB;
    const me = a.__id === watchId ? a : b.__id === watchId ? b : null;
    if (me) {
      const other = me === a ? b : a;
      console.error(
        `    collide ${watchId} x ${other.__id || other.label} — ${watchId}@(${me.position.x.toFixed(0)},${me.position.y.toFixed(0)}) v=(${me.velocity.x.toFixed(1)},${me.velocity.y.toFixed(1)})`
      );
    }
  }
});

const wallOpts = { isStatic: true, restitution: 0.55, friction: 0 };
const wallThickness = 40;

function hSegment(xFrom, xTo, y) {
  const cx = (xFrom + xTo) / 2;
  const w = xTo - xFrom;
  return Bodies.rectangle(cx, y, w, wallThickness, wallOpts);
}
function vSegment(yFrom, yTo, x) {
  const cy = (yFrom + yTo) / 2;
  const h = yTo - yFrom;
  return Bodies.rectangle(x, cy, wallThickness, h, wallOpts);
}

// 6 rail segments, each stopping short GAP px before every pocket so a ball
// can actually roll through the opening instead of bouncing off a solid wall.
Composite.add(world, [
  hSegment(RAIL.left + GAP, POCKETS.TC.x - GAP, RAIL.top),
  hSegment(POCKETS.TC.x + GAP, RAIL.right - GAP, RAIL.top),
  hSegment(RAIL.left + GAP, POCKETS.BC.x - GAP, RAIL.bottom),
  hSegment(POCKETS.BC.x + GAP, RAIL.right - GAP, RAIL.bottom),
  vSegment(RAIL.top + GAP, RAIL.bottom - GAP, RAIL.left),
  vSegment(RAIL.top + GAP, RAIL.bottom - GAP, RAIL.right),
]);

const ballOpts = { restitution: 0.93, friction: 0, frictionAir: 0.015, label: "ball" };
const bodies = {}; // id -> Matter body
RACK.forEach((b) => {
  const body = Bodies.circle(b.x, b.y, BALL_R, { ...ballOpts });
  body.__id = b.id;
  bodies[b.id] = body;
  Composite.add(world, body);
});

// Cue ball starts above the rack, breaks downward into the apex — well clear
// of the TC pocket's capture radius (58px) even though it shares its x.
const cue = Bodies.circle(960, 250, CUE_R, { ...ballOpts, frictionAir: 0.02, label: "cue" });
cue.__id = "cue";
Composite.add(world, cue);
Body.setVelocity(cue, { x: 1.0, y: 17 });

const potted = new Set();
const events = []; // { id, frame }
const frames = []; // per recorded sample: { [id]: {x,y} | null, cue: {x,y}|null }

let sample = 0;
let step = 0;
let settleStreak = 0;
const BREAK_MAX_STEPS = Math.round((5.0 * 1000) / DT_MS);

function maxSpeed(excludeEight) {
  let m = 0;
  for (const id of Object.keys(bodies)) {
    if (potted.has(id)) continue;
    if (excludeEight && id === "8") continue;
    const s = Vector.magnitude(bodies[id].velocity);
    if (s > m) m = s;
  }
  const cs = potted.has("cue") ? 0 : Vector.magnitude(cue.velocity);
  if (cs > m) m = cs;
  return m;
}

function recordSample() {
  const f = { t: sample / FPS };
  for (const b of RACK) {
    if (potted.has(b.id)) {
      f[b.id] = null;
    } else {
      const body = bodies[b.id];
      f[b.id] = { x: Math.round(body.position.x * 10) / 10, y: Math.round(body.position.y * 10) / 10 };
    }
  }
  f.cue = potted.has("cue") ? null : { x: Math.round(cue.position.x * 10) / 10, y: Math.round(cue.position.y * 10) / 10 };
  frames.push(f);
  sample++;
}

function nearestPocket(p) {
  let best = POCKET_LIST[0];
  let bd = Infinity;
  for (const pk of POCKET_LIST) {
    const d = Vector.magnitude(Vector.sub(p, pk));
    if (d < bd) {
      bd = d;
      best = pk;
    }
  }
  return best;
}

function checkPockets() {
  for (const id of Object.keys(bodies)) {
    if (potted.has(id) || id === "8") continue;
    const p = bodies[id].position;
    let caught = false;
    for (const pk of POCKET_LIST) {
      if (Vector.magnitude(Vector.sub(p, pk)) < POCKET_CAPTURE_R) {
        caught = true;
        events.push({ id, frame: frames.length, pocket: pk.id });
        break;
      }
    }
    // safety net: a ball that squeezed through a pocket gap without tripping
    // the radius check (grazing shot) but is now off the playing surface —
    // still a real physical outcome (it went in), just credit the nearest pocket.
    if (!caught && (p.x < RAIL.left - 70 || p.x > RAIL.right + 70 || p.y < RAIL.top - 70 || p.y > RAIL.bottom + 70)) {
      caught = true;
      events.push({ id, frame: frames.length, pocket: nearestPocket(p).id });
    }
    if (caught) {
      potted.add(id);
      Composite.remove(world, bodies[id]);
    }
  }
  if (!potted.has("cue")) {
    const p = cue.position;
    for (const pk of POCKET_LIST) {
      if (Vector.magnitude(Vector.sub(p, pk)) < POCKET_CAPTURE_R) {
        // scratch — respot the cue ball rather than losing it for the rest of the "game"
        Body.setPosition(cue, { x: 960, y: 820 });
        Body.setVelocity(cue, { x: 0, y: 0 });
        break;
      }
    }
  }
}

// ── Phase 1: the break. Step until it settles (or hit the time cap).
while (step < BREAK_MAX_STEPS) {
  Engine.update(engine, DT_MS);
  step++;
  checkPockets();
  if (step % RECORD_EVERY === 0) {
    recordSample();
    const ms = maxSpeed(true);
    settleStreak = ms < 0.06 ? settleStreak + 1 : 0;
    if (settleStreak > 20) break; // ~0.66s of calm
  }
}
const breakEndFrame = frames.length;

// ── Phase 2: clear the table, one ball at a time.
//
// Modeling a full cue-ball flight for every shot (spawn it somewhere clear,
// aim it down a ghost-ball line, hope nothing else on a crowded table gets in
// the way) turned out to be exactly the kind of "solver" that's fragile in
// practice — most attempts sailed past the target or clipped a neighbour and
// caromed off God knows where. What's actually real about a potted ball is
// what happens to IT: a rigid body, with mass, friction and restitution,
// crossing the felt and colliding with whatever real obstacles are actually
// in front of it. So each "shot" here is a direct impulse on the object ball
// itself (the invisible cue that struck it isn't the interesting part) — real
// collisions with every other ball still on the table, real rail bounces,
// real friction decay, aimed at the nearest pocket and retried from wherever
// it actually ends up if the first line doesn't get there.
// Greedy, round by round: always take the shot that's actually easiest right
// now (closest ball to any pocket), not a fixed 1-2-3 script. A miss moves
// the ball and reshuffles what "easiest" means for the next round — which is
// exactly how clearing a real table goes, and it clears the crowd fastest
// instead of grinding fixed-order shots through the most cluttered moment
// (right after the break) first.
const remaining = new Set(RACK.filter((b) => !b.eight).map((b) => b.id));
const SHOT_MAX_STEPS = Math.round((1.4 * 1000) / DT_MS);
const attemptsUsed = {};
let round = 0;
const MAX_ROUNDS = remaining.size * 9;
while (remaining.size > 0 && round < MAX_ROUNDS) {
  round++;
  let bestId = null;
  let bestPocket = null;
  let bestDist = Infinity;
  for (const id of remaining) {
    const pos = bodies[id].position;
    for (const pk of POCKET_LIST) {
      const d = Vector.magnitude(Vector.sub(pos, pk));
      if (d < bestDist) {
        bestDist = d;
        bestId = id;
        bestPocket = pk;
      }
    }
  }
  const id = bestId;
  watchId = id;
  const n = (attemptsUsed[id] = (attemptsUsed[id] || 0) + 1);
  const pos = { x: bodies[id].position.x, y: bodies[id].position.y };
  // after a couple of failed rounds on the same ball, try a different pocket
  // and nudge the angle rather than repeat the exact line that just failed
  let pocketChoice = bestPocket;
  if (n > 2) {
    const byDist = POCKET_LIST.map((pk) => ({ pk, d: Vector.magnitude(Vector.sub(pos, pk)) })).sort((a, b) => a.d - b.d);
    pocketChoice = byDist[Math.min(n - 1, byDist.length - 1)].pk;
  }
  const jitterDeg = n <= 1 ? 0 : (((n % 2 === 0 ? 1 : -1) * (5 + n * 3) * Math.PI) / 180);
  const rawDir = Vector.normalise(Vector.sub(pocketChoice, pos));
  const cosT = Math.cos(jitterDeg);
  const sinT = Math.sin(jitterDeg);
  const dir = { x: rawDir.x * cosT - rawDir.y * sinT, y: rawDir.x * sinT + rawDir.y * cosT };
  const nd = Vector.magnitude(Vector.sub(pocketChoice, pos));
  const speed = Math.min(14, nd * 0.013 + 7 + n * 0.8);
  Body.setVelocity(bodies[id], Vector.mult(dir, speed));
  if (process.env.DEBUG_SHOTS) {
    console.error(`round ${round}: ball ${id} (try ${n}) from=(${pos.x.toFixed(0)},${pos.y.toFixed(0)}) -> ${pocketChoice.id} speed=${speed.toFixed(1)}`);
  }

  let shotSteps = 0;
  let shotSettle = 0;
  while (shotSteps < SHOT_MAX_STEPS) {
    Engine.update(engine, DT_MS);
    shotSteps++;
    checkPockets();
    if (shotSteps % RECORD_EVERY === 0) {
      recordSample();
      if (potted.has(id)) {
        remaining.delete(id);
        for (let i = 0; i < 5; i++) recordSample(); // a short beat before cutting to the next shot
        break;
      }
      const ms = maxSpeed(true);
      shotSettle = ms < 0.04 ? shotSettle + 1 : 0;
      if (shotSettle > 9) break; // settled without dropping — reassess next round
    }
  }
}
if (process.env.DEBUG_SHOTS && remaining.size) {
  console.error(`  never dropped after ${MAX_ROUNDS} rounds: ${[...remaining].join(", ")}`);
}

const eightBody = bodies["8"];
const eightRest = { x: Math.round(eightBody.position.x * 10) / 10, y: Math.round(eightBody.position.y * 10) / 10 };

// ── Time-remap for pacing: the physics is real, but a 60-second ad can't sit
// through however long the actual clearance takes. The early flurry (most
// balls drop within a handful of seconds of the break, one after another) is
// exactly the pace we want on screen — keep it real-time. Whatever's left
// (a couple of balls that took several retries) gets compressed so the whole
// clearance still lands in a fixed screen budget, without cutting any of it.
const FLURRY_POTS = Math.min(7, events.length);
const flurryEndFrame = events.length ? events[FLURRY_POTS - 1].frame : breakEndFrame;
const TARGET_PHASE2_SECONDS = 12.0;
const flurrySeconds = (flurryEndFrame - breakEndFrame) / FPS;
const tailFrames = frames.slice(flurryEndFrame);
const tailSecondsOriginal = tailFrames.length / FPS;
const tailBudget = Math.max(1.5, TARGET_PHASE2_SECONDS - flurrySeconds);
const tailStep = Math.max(1, Math.round(tailFrames.length / Math.max(1, tailBudget * FPS)));

const keptFrames = frames.slice(0, flurryEndFrame);
for (let i = 0; i < tailFrames.length; i += tailStep) {
  keptFrames.push(tailFrames[i]);
}
// always keep the very last frame so nothing snaps at the end
if ((tailFrames.length - 1) % tailStep !== 0 && tailFrames.length > 0) {
  keptFrames.push(tailFrames[tailFrames.length - 1]);
}
// frame index i < flurryEndFrame maps 1:1; beyond that, the tail is
// compressed by tailStep — same formula used to build keptFrames above.
function remapFrameIndex(f) {
  if (f < flurryEndFrame) return f;
  return flurryEndFrame + Math.round((f - flurryEndFrame) / tailStep);
}
const remappedEvents = events.map((e) => ({
  id: e.id,
  pocket: e.pocket,
  frame: Math.min(keptFrames.length - 1, remapFrameIndex(e.frame)),
}));
// re-timestamp the kept frames to a clean 0-based sequence
keptFrames.forEach((f, i) => (f.t = i / FPS));

if (process.env.DEBUG_SHOTS) {
  console.log(
    `Remap: flurry ${FLURRY_POTS} pots in ${flurrySeconds.toFixed(2)}s (kept), tail ${tailSecondsOriginal.toFixed(2)}s -> ~${(keptFrames.length / FPS - flurrySeconds - breakEndFrame / FPS).toFixed(2)}s (step ${tailStep})`
  );
}

const data = {
  fps: FPS,
  totalFrames: keptFrames.length,
  breakEndFrame,
  ballRadius: BALL_R,
  cueRadius: CUE_R,
  pockets: POCKETS,
  balls: RACK.map((b) => ({ id: b.id, cat: b.cat, c: b.c, stripe: !!b.stripe, eight: !!b.eight })),
  events: remappedEvents,
  eightRestPosition: eightRest,
  frames: keptFrames,
};

writeFileSync(
  new URL("../compositions/data/physics-data.js", import.meta.url),
  "window.__PHYSICS__ = " + JSON.stringify(data) + ";\n"
);

console.log("Raw simulated frames:", frames.length, "=", (frames.length / FPS).toFixed(2) + "s");
console.log("Break ends at frame", breakEndFrame, "=", (breakEndFrame / FPS).toFixed(2) + "s");
console.log("Output (remapped) duration:", (keptFrames.length / FPS).toFixed(2) + "s,", keptFrames.length, "frames");
console.log("8-ball rest position:", eightRest);
console.log(
  "Pot order (remapped):",
  remappedEvents.map((e) => `${e.id}@${(e.frame / FPS).toFixed(2)}s(${e.pocket})`).join(", ")
);
console.log("Potted count:", potted.size - (potted.has("cue") ? 1 : 0), "/", RACK.filter((b) => !b.eight).length);
