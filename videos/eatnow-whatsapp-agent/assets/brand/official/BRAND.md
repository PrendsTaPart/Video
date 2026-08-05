# EatNow — Brand System for AI Agents

You are designing for **EatNow**, a Hospitality OS (B2B SaaS) for restaurants, hotels, and venues. This document is the authoritative brand reference. Follow it strictly when generating landing pages, marketing sites, feature pages, decks, social posts, or any EatNow-branded surface.

---

## 1. Positioning

- **Who**: Restaurateurs, hoteliers, managers, front-of-house staff.
- **Voice**: Quiet authority. Practitioner-to-practitioner. Not marketing.
- **Tension**: Architectural rigor (Geist, grids, data) softened by editorial warmth (Fraunces italic, hospitality surfaces).
- **Tagline feel**: "The mark that maps the room." Dots = tables, guests, the service unfolding.
- **Never**: loud, corporate, abstract, exclamation-heavy, emoji-filled, or SaaS-generic.

---

## 2. Color Tokens

### Foundations (the 4 primary colors)

| Token     | Hex       | Role                                                                                               |
| --------- | --------- | -------------------------------------------------------------------------------------------------- |
| **Ink**   | `#141210` | Primary surface for hero, commercial covers, statement moments. _Warmed black, never pure `#000`._ |
| **Paper** | `#FAF8F2` | Default UI background. The working canvas. _Warmed white, never pure `#FFF`._                      |
| **Navy**  | `#10386B` | The action color — CTAs, links, selected states. **The only accent.**                              |
| **Beige** | `#DDD6C6` | Hospitality surface. Editorial covers, guest-facing pages, print.                                  |

### Warm Neutrals Scale (for text, borders, surfaces)

| Stop | Name        | Hex       | Token            | Usage                               |
| ---- | ----------- | --------- | ---------------- | ----------------------------------- |
| 00   | Paper       | `#FAF8F2` | `surface.canvas` | Default UI bg                       |
| 50   | Cream       | `#F2EDE2` | `surface.subtle` | Cards, hover, elevated surfaces     |
| 100  | Beige       | `#DDD6C6` | `surface.warm`   | Hospitality surfaces, editorial     |
| 200  | Stone Light | `#C4BFB2` | `border.default` | Default borders, dividers           |
| 300  | Stone       | `#A8A399` | `border.strong`  | Emphasized borders, disabled        |
| 400  | Stone Mid   | `#8C887C` | `text.muted`     | Helper text, captions, placeholders |
| 500  | Stone Dark  | `#5A564C` | `text.secondary` | Secondary text, labels              |
| 700  | Graphite    | `#2B2821` | `text.body`      | Body paragraphs, running text       |
| 900  | Ink         | `#141210` | `text.primary`   | Headlines, primary text             |

### Functional

| Token   | Hex       | Tint      | Usage                                   |
| ------- | --------- | --------- | --------------------------------------- |
| Success | `#3D7A58` | `#E8EFE3` | Reservation confirmed, payment captured |
| Warning | `#C68A3A` | `#F3EAD8` | Near-capacity, deposit required soon    |
| Error   | `#B84842` | `#F0DFD9` | Payment declined, no-show, destructive  |
| Info    | `#10386B` | `#DCE4EC` | Neutral context, updates (shares Navy)  |

### Proportions by Surface Type

- **Product / UI**: Paper dominant 70% · Ink for text · Navy for actions · Beige rare · white cards.
- **Commercial / Sales** (landing pages, decks): Ink dominant 60% · Fraunces on Ink for statements · Navy for CTAs · Paper for breathing room.
- **Hospitality / Guest-facing**: Beige dominant 60% · Ink for text · Navy rare · warm printed-menu feel.
- **Global baseline**: Ink 40 · Paper 35 · Beige 15 · Navy 8 · Other 2.

### Approved Color Pairings (all pass WCAG AA+)

- Ink on Paper · Paper on Ink · Ink on Beige · Paper on Navy · Beige on Ink · Navy on Beige.

### Forbidden Pairings

- Navy on Ink (fails contrast, visual noise)
- Beige on Paper (too close in value)
- Stone Mid on Beige (muddy)
- Paper on Beige (washed out)

---

## 3. Typography

### The Duet: Geist + Fraunces

**Geist is the PRIMARY voice (~90% of surfaces).** Geometric sans, all weights. Used for system/UI, product, data, architecture, and **display** (big wordmarks, hero type). EatNow is a Hospitality OS, not a magazine — rigor leads.

**Fraunces is the SECONDARY accent (~10%).** Variable serif with `opsz`, `SOFT`, `WONK` axes. Used as **italic counterpoint to Geist** — pull quotes, editorial breaks, the "beat" in a duet heading. Never the main display voice.

### Variable Font Settings

- **Geist**: weights 400 / 500 / 700. `letter-spacing: -0.04em` for display.
- **Fraunces**: `font-variation-settings: "opsz" 144, "SOFT" 100, "WONK" 1;` weight 300 italic for display. `letter-spacing: -0.03em`.

### The Duet Pattern (rhetorical "beat")

Headings are typically split: Geist bold sets the claim, Fraunces italic lands the promise. Use sparingly — one per page max.

```html
<h1>
  <span style="font-family: Geist; font-weight: 700; letter-spacing: -0.04em;"
    >Every table,</span
  >
  <span
    style="font-family: Fraunces; font-weight: 300; font-style: italic;
               font-variation-settings: 'opsz' 144, 'SOFT' 100, 'WONK' 1;
               letter-spacing: -0.03em;"
  >
    every night.</span
  >
</h1>
```

**Split examples** (Geist / _Fraunces_):

- "Four colors. / _A warmer room._"
- "Two voices. / _One architecture._"
- "Room to breathe, / _one word._"
- "Every guest, / _a new constellation._"
- "The mark that / _maps the room._"

### Type Scale (Geist, five sizes, one system)

| Role    | Size / Line-height                   | Tracking | Weight   |
| ------- | ------------------------------------ | -------- | -------- |
| Display | 96px / 96px (or up to 136px on hero) | −0.04em  | 700      |
| Title   | 48px / 52px                          | −0.025em | 500      |
| H2      | 28px / 36px                          | −0.015em | 500      |
| Body    | 16px / 24px                          | −0.005em | 400      |
| Caption | 11px / 16px                          | 0.14em   | 500 Caps |

### Rules

- Default to Geist. Reach for Fraunces only when voice matters (pull quote, section opener, chapter heading, book cover).
- Never put Fraunces in the biggest visual slot.
- Body copy is Geist 400, `text.body` color (`#2B2821`).
- No all-caps for emphasis. No italic Geist for emphasis — use weight.

---

## 4. Logo & Brandmark

### Canonical brandmark: 5×5 grid, 17 dots, 4-fold symmetric

![EatNow brandmark](./assets/brand-mark.svg)

**Pattern reference** (visible dot positions per row, 1-indexed left→right):

| Row | Positions | Dots |
| --- | --- | --- |
| 1 | 1, 2, 4, 5 | 4 |
| 2 | 1, 3, 5 | 3 |
| 3 | 2, 3, 4 | 3 |
| 4 | 1, 3, 5 | 3 |
| 5 | 1, 2, 4, 5 | 4 |

- 2-gap-2 clusters at the four corners + a diagonal X network through the center.
- The dots are tables. The X is the flow. "The mark that maps the room."

### Construction

- Dots are rounded squares: `width/height: 1 unit`, `border-radius: 12.5%` (e.g., `1px` on an 8px dot, `2px` on a 14px dot, `5px` on a 40px dot).
- Grid is uniform: dot-size × 5 with gap = dot-size between cells (so total = 9× dot-size).

### Lockups

- **Primary horizontal**: brandmark + "EatNow" wordmark, left-aligned.
- **Stacked**: brandmark above wordmark, centered.
- **Brandmark-only**: use at small sizes (below 24px height) — never attempt the horizontal lockup below that threshold.

### Clear Space & Scale

- **Exclusion zone** = 1× mark height on all four sides. No text, graphic, or edge may enter.
- **Minimum size** = 24px mark height. Below that, brandmark-only.
- **The unit** = one grid cell. All spacing derives from it (8px dot + 4px gap = 12px base cell). Clear space scales proportionally.

### Wordmark

- **Geist Bold (700)**, tracking **−0.04em**. Tight, architectural.
- Case: `EatNow` (single word, capital E and N).
- Never light, never loose.

---

## 5. Motif System — The Dot

Everything in the brand derives from one atom: the **dot**.

### Atom

- **Size**: 8 × 8 px base. Scale: 4 / 8 / 16 / 24 px.
- **Border-radius**: 12.5% of size (1px on 8px).
- **Shape**: rounded square — never a perfect circle.

### Cell & Grid

- **Cell**: 12 × 12 px (dot + 4px gap, ratio 2:1 dot:gap with 2px padding per side).
- **Rhythm**: uniform tile, all motifs align to the 4 / 8 / 16 / 24 px grid. Never off-grid, never freeform, never tilted.

### Density Spectrum

Pick one density per surface. Never stack two patterns on the same surface.

| Level         | Coverage    | Use                                                                           |
| ------------- | ----------- | ----------------------------------------------------------------------------- |
| **Whisper**   | ~8%         | Atmospheric backgrounds, hero fills, subtle surfaces                          |
| **Texture**   | ~25%        | Decorative card fills, section separators                                     |
| **Dense**     | ~60%        | Strong surfaces, full-bleed hero moments, data heatmaps                       |
| **Statement** | (logo only) | The logo's own pattern. A mark, a seal, a signature. **Never as decoration.** |

### Pattern Library (six dialects)

1. **Occupancy Heatmap** — opacity gradient on the grid reads as filled tables.
2. **Flow Lines** — connecting lines between dots = guest flow, reservations in motion.
3. **Editorial Divider** — single row of dots as rule/separator.
4. **Hero Pattern** — composed density (center-bright, edges dim) for hero backgrounds.
5. **Accent Dot** — a single dot as bullet, eyebrow, or pin.
6. **Logo Stamp** — the brandmark as seal (corner of a cover, footer).

### Rules of the Room

1. **One pattern per surface.** Never stack heatmap + flow lines. Never texture + hero. Pick the dialect, commit, strip everything else back to typography and whitespace.
2. **Density matches volume.** Whisper for backgrounds. Texture for cards. Dense for heroes. Statement = the logo, never décoration.
3. **Meaning over decoration.** Data patterns (heatmap, flow) only when they reflect real data. No decorative heatmaps, no fake flows.
4. **Respect the grid.** All motifs align to 4/8/16/24 px. Never off-grid, never freeform, never tilted. The rhythm is the signature — breaking it breaks the brand.

### When to use the Scattered pattern

When the grid feels too rigid — welcome moments, editorial covers, invitations, brand statements. Same atom, off-grid composition. An editorial exception. Keep rare.

---

## 6. Spacing & Grid

- **Base unit**: 4px. All spacing is a multiple: 4 / 8 / 12 / 16 / 24 / 32 / 48 / 64 / 80 / 96 / 128.
- **Hero padding**: 80px block / 80px inline on 1440px wide pages.
- **Inner content max-width**: 1280px.
- **Typical section gap**: 80px, reduced to 56px or 48px when content is dense.
- **Card padding**: 24px–40px depending on scale.
- **Border radius**: 4px (cards, inputs) · 10px (large surfaces like screen captures) · 12.5%-of-size (logo dots).

---

## 7. Components

### Primary CTA (Button)

- Background: Navy `#10386B`
- Text: Paper `#FAF8F2`, Geist 500, 14–15px
- Padding: 14px 24px
- Border-radius: 4px
- Arrow `→` after label, 8px gap

### Secondary action

- Underlined text link, Ink color, Geist 500. Never a ghost button.

### Card

- Background: Paper or Cream (`#F2EDE2` for subtle elevation)
- Border: 1px `#DDD6C6` (Beige) or `#C4BFB2` (Stone Light)
- Corner: 10px on large cards, 4px on inline cards
- Shadow (for floating screens only): `0 32px 64px -16px rgba(20, 18, 16, 0.18), 0 16px 32px -8px rgba(20, 18, 16, 0.08)`

### Eyebrow (section label)

- Short rule `—` (24px × 1px, Stone Light) + label in Geist 500 caps, 11–12px, tracking 0.14em, color Stone Dark `#5A564C`.

### Status Pill

- Small rounded pill, background tint of the status color (Success tint, Warning tint, etc.), text in the status color. Geist 500, 11px caps.

### Callout / Number Pin

- 24×24 Navy circle, Paper text, Geist 600, 11px. Soft shadow `0 3px 8px rgba(20,18,16,0.28)`.

---

## 8. Application Patterns

### Landing hero (commercial cover)

- **Background**: Ink `#141210` full-bleed, with a **Hero Pattern** motif (Whisper density, opacity gradient, dots in Paper at ~3–25% opacity). Pattern tends to sit off-center (top-right or left-clear) to leave room for the title.
- **Title**: The duet pattern (Geist 700 + Fraunces italic 300), 88–136px, Paper color.
- **Subtitle**: Geist 400, 16–18px, Stone Light color, max 640px width.
- **CTA row**: Primary Navy button + secondary underlined link.
- **Eyebrow**: small caps label with rule.

### Feature section (product)

- **Split**: Text left (640px) / visual right (640px). Both flush to a 1280px inner.
- **Visual right**: a real product UI (floor plan, reservation list, chat) on a Cream background with 10px corner, soft shadow, no heavy border.
- **Feature list**: 3 items, each with a small Navy accent dot bullet + Geist 500 label + Geist 400 description.

### Hero bleed (big moment)

- Full-bleed screen on the right, cropping past the right edge at ~900px, Cream background. Geist + Fraunces duet title on the left. Frame: 10px corner, 1px Stone border, long soft Ink-tinted shadow. The screen floats — never drops.

### Multi-screen (one OS, two devices)

- Desktop + phone composed in one frame. Composition Header (surfaces label) + Stage (devices with shadow + subtle dot pattern background at ~8–12% opacity) + Composition Footer (narrative copy + device labels).

### Callouts (annotating UI)

- Thin rings (1.5px, Beige color, transparent fill) around focus areas of a screenshot. Small numbered Navy pins (24px circle) at the corner of each ring. Label cards below with number + title + one-sentence explanation.

### Social (type-only)

- Cream or Ink background, duet title centered or left-aligned, minimal — no decoration beyond a corner logo stamp and a hair-line eyebrow.

### Social (imagery)

- Real hospitality photography (restaurants, plates, staff, architecture). Overlays only: Navy tint `rgba(16, 56, 107, 0.72)` for brand moments, or a bottom-up Ink scrim `linear-gradient(180deg, rgba(20,18,16,0) 0%, rgba(20,18,16,0.92) 70%, #141210 100%)` for text-over-photo posts. Logo stamp top-left or bottom-left.

---

## 9. Voice & Tone

### Four Pillars

**01 · Practitioner** (never marketer)
Talk like someone who has worked service. Call a couvert a couvert. Reference specific restaurant workflows, not generic "business outcomes."

- Yes: "We've watched this break at 19:42 on a Friday."
- No: "Unlock operational excellence."

**02 · Specific** (never abstract)
Real numbers, real names, real nights. "2,847 tables" > "thousands of tables." "Leclerc, party of 4" > "a reservation."

- Yes: "Covers down 12% on Thursdays. The deposit rule fixed it."
- No: "Drive measurable improvements across your business."

**03 · Calm** (never loud)
No exclamation marks. No CAPS for emphasis. No emoji. Short sentences. Weight carries emphasis, not volume.

- Yes: "Payment declined. The card is expired."
- No: "OOPS! Something went wrong! Please try again!!"

**04 · Human** (never corporate)
"Your kitchen" not "the stakeholder." Admit errors plainly. First person plural when we're speaking as EatNow ("we"), second person for the reader ("you, your").

- Yes: "We missed a webhook. Your 19:00 service wasn't affected."
- No: "A transient issue was experienced by the platform."

### Do / Don't — UI Writing

| Surface         | Do                                                          | Don't                                       |
| --------------- | ----------------------------------------------------------- | ------------------------------------------- |
| Empty state     | "No reservations yet. Your first Friday is tomorrow."       | "Nothing to display."                       |
| Toast (success) | "Leclerc confirmed for 19:30."                              | "Operation completed successfully!"         |
| Error           | "Card declined. Try another, or switch to cash on arrival." | "An unexpected error occurred (code 4221)." |
| Email subject   | "Tomorrow — 142 covers, 38 prepaid."                        | "Your EatNow Daily Summary"                 |

### Writing rules

- **Numbers**: always real, always specific. "2,500 restaurants" > "many restaurants."
- **Verbs**: active. "We shipped" not "was shipped."
- **Jargon**: hospitality jargon (covers, turnovers, pass, no-show, deposit) yes. Tech jargon (synergize, leverage, unlock) no.
- **Length**: short sentences. Long sentences only when one clause needs one rhythm.
- **Punctuation**: em-dashes for rhythm — like this. One per sentence max.

---

## 10. AI Agent Cheat Sheet

When designing a new EatNow surface:

1. **Identify the surface**: Product/UI? Commercial/Sales? Hospitality/Guest-facing? Pick the proportion recipe.
2. **Pick ONE motif**: Whisper bg, or Texture card, or one Hero Pattern. Never stack.
3. **Write the hero**: Geist duet title → Fraunces italic beat → Geist subtitle → Navy CTA. Max 3 levels.
4. **Choose colors by role**: Text = Ink/Graphite. Background = Paper/Ink/Beige. Actions = Navy only. Feedback = functional.
5. **Align to grid**: every element on a 4 / 8 / 16 / 24 px position. No freeform.
6. **Write with specificity**: real numbers, real workflows, practitioner voice.
7. **Check WCAG AA+** on all text pairings. If unsure, default to Ink on Paper or Paper on Ink.
8. **Refuse**: exclamation marks, emoji as icons, gradients (except the Ink scrim on photos), shadows on flat surfaces, circles (use rounded squares), cool grays, pure black, pure white.

### Quickest "good enough" template for a landing section:

```html
<section
  style="background: #141210; padding: 120px 80px; color: #FAF8F2; font-family: Geist, sans-serif;"
>
  <div style="max-width: 1280px; margin: 0 auto;">
    <div
      style="display: flex; gap: 12px; align-items: center; margin-bottom: 24px;"
    >
      <div style="width: 24px; height: 1px; background: #8C887C;"></div>
      <span
        style="font: 500 11px/16px Geist; letter-spacing: 0.14em; text-transform: uppercase; color: #8C887C;"
        >Module 01 · Reservations</span
      >
    </div>
    <h1
      style="margin: 0 0 24px; font-size: 96px; line-height: 96px; letter-spacing: -0.04em;"
    >
      <span style="font-weight: 700;">Every table,</span
      ><span
        style="font-family: Fraunces; font-weight: 300; font-style: italic; font-variation-settings: 'opsz' 144, 'SOFT' 100, 'WONK' 1; letter-spacing: -0.03em;"
      >
        every night.</span
      >
    </h1>
    <p
      style="max-width: 640px; margin: 0 0 40px; font-size: 18px; line-height: 28px; color: #C4BFB2;"
    >
      The first conversation you have with a guest. We map it — covers,
      turnovers, deposits, no-shows — so the pass never breaks at 19:42 on a
      Friday.
    </p>
    <a
      href="#"
      style="display: inline-flex; align-items: center; gap: 8px; background: #10386B; color: #FAF8F2; padding: 14px 24px; border-radius: 4px; font: 500 15px/1 Geist; text-decoration: none;"
      >See the plan →</a
    >
  </div>
</section>
```
