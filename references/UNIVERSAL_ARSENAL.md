# UNIVERSAL DESIGN ARSENAL
## Synthesized Intelligence from the 60 Subdirectories of the Design Ecosystem

This document is the unified, production-grade intelligence extract harvested across all 60 specialized design repositories, skills, and token libraries in the `$DESIGN_LIB` ecosystem. It provides mathematical formulas, token recipes, interaction physics, copywriting doctrines, and medium archetypes for `design-genius`.

---

## 1. Directory Matrix & Provenance Map

| Category | Repositories & Toolkits | Extracted Intelligence & Primitives |
|---|---|---|
| **Anti-Slop & Taste** | `taste-skill`, `impeccable`, `hallmark`, `stop-slop`, `no-ai-slop`, `pencilplaybook` | Strict font bans, OKLCH reproduction gates, verb-driven CTAs, silent success, 10-dimension audit rubric, 40% disabled opacity. |
| **Complete Design Systems** | `awesome-design-md`, `design-md`, `coss`, `astryx`, `shadcn-ui`, `nothing-design-skill`, `official-design-md` | 74+ real-world product DESIGN.md specs (Linear, Stripe, Apple, SpaceX, PostHog, etc.), Cal.com enterprise scheduling, Radix accessible components. |
| **Motion & Kinetic Physics** | `pixel2motion`, `lenis`, `transitions.dev`, `animate-ui`, `react-bits`, `inspira-ui`, `driver.js` | ODE RK4 kinetic springs, `cubic-bezier(0.16, 1, 0.3, 1)`, view transitions, smooth inertia scrolling, interactive spotlight cards, guided walkthrough masks. |
| **Substrates, Shaders & 3D** | `liquid-glass-js`, `scroll-craft`, `scroll-world`, `shadergradient`, `threeui`, `img2threejs`, `liquid-logo` | Real-time WebGL refraction/chromatic aberration, GLSL shaders, camera lerp, turbulent noise fields, Three.js spatial lighting. |
| **Specialized Mediums** | `tui-studio`, `pretext`, `assistant-ui`, `mapcn`, `diagram-design`, `tegaki`, `hyperframes`, `frontend-slides`, `skills-slides` | 80x24 ANSI terminal matrices, canvas multiline text rasterization, AI agent conversational cockpits, dark MapLibre cartography, technical exploded diagrams, HTML/CSS video rendering. |
| **A11y, Iconography & Assets** | `axe-core`, `styleseed`, `ui-ux-pro-max-skill`, `ux-skill`, `simple-icons`, `nerd-fonts`, `pic-smaller`, `beautify-github-readme` | WCAG 2.1 AA/AAA contrast ratios (4.5:1 / 3:1), 23 styleseed agent skills, monospace/brand glyphs, lossless image optimization. |

---

## 2. Mathematical Laws & Geometry Formulations

### A. Concentric Radii Law (`impeccable` + `taste-skill`)
Arbitrary border-radii within nested layouts create optical dissonance. Inner elements must mathematically derive their radius from the parent container:
$$R_{\text{inner}} = \max(0, R_{\text{outer}} - \text{Padding})$$
*Example:* If outer card has $R = 12\text{px}$ and `padding: 8px`, the inner image or badge **must** have $R = 4\text{px}$ (never 12px pill or 8px).

### B. Typecraft Leading & Tracking Asymptote (`taste-skill` + `impeccable`)
- **Negative Letter-Spacing Curve:** Scales inversely with font size and asymptotes to `0` at body size:
  - Display (>80px): `letter-spacing: -0.035em` (~-1.4px to -2.8px)
  - Subhead (32px–48px): `letter-spacing: -0.015em` (~-0.5px to -0.7px)
  - Body (14px–18px): `letter-spacing: 0` (strict neutral tracking)
  - Micro/Mono (10px–12px): `letter-spacing: +0.06em` to `+0.14em` (loose tracking for legibility)
- **Leading Ratio Ceiling:**
  - Headlines/Display: `line-height: 0.85` to `1.15` (tightened spine)
  - Longform Body: `line-height: 1.60` to `1.85` (relaxed reading comfort)
- **Weight Contrast Law:** Minimum $\Delta \ge 300$ font-weight units between heading and adjacent body copy (e.g., 700 bold over 400 normal, or 600 semibold over 300 light).

### C. Color Separation & Pigment Formulation (`taste-skill` + `awesome-design-md`)
- **Mathematical Hue Separation:** Base substrate and primary accent hues must maintain an arc distance of at least $40^\circ$:
  $$|\text{Hue}_{\text{accent}} - \text{Hue}_{\text{substrate}}| \ge 40^\circ$$
- **Chroma Anchoring in Neutrals:** Every grey or neutral token must carry a trace chroma ($\text{chroma} \ge 0.006$) tinted toward the primary accent hue to eliminate sterile dead greys.
- **Lightness Bands in OKLCH:**
  - Light-mode Substrate: $L \in [0.96, 0.985]$, $C \in [0.005, 0.02]$
  - Light-mode Ink: $L \in [0.15, 0.22]$, $C \in [0.01, 0.03]$
  - Dark-mode Substrate: $L \in [0.11, 0.16]$, $C \in [0.008, 0.025]$
  - Dark-mode Ink: $L \in [0.92, 0.97]$, $C \in [0.005, 0.015]$
  - Accent Pigments: $C \in [0.12, 0.24]$ (vibrant, saturated focal interrupt)
- **Dark Mode Elevation:** Surface elevation is expressed through **lightness increments (+3% to +5% L per level)**, never colored drop-shadow glows.

---

## 3. Kinetic Interaction & Motion Physics (`pixel2motion` + `lenis`)

### A. Kinetic Duration Budget
- **Micro-interactions (detents, toggles, icon clicks):** $80\text{ms}\text{--}140\text{ms}$
- **Surface transitions (dialogs, dropdowns, accordions):** $180\text{ms}\text{--}240\text{ms}$
- **Layout & Page morphs (shared element transitions):** $300\text{ms}\text{--}380\text{ms}$

### B. Standard Bezier Curves
- **Primary Deceleration (Snappy Action):** `cubic-bezier(0.16, 1, 0.3, 1)` (Apple/Linear rapid ease-out)
- **Mechanical Snap (Hardware Detent):** `cubic-bezier(0.2, 0.8, 0.2, 1)`
- **Inertial Glide (Smooth Scroll):** `cubic-bezier(0.25, 1, 0.5, 1)`

### C. Analytical Spring Formulation (ODE RK4)
For physical spring simulations (framer-motion, canvas, or WebGL):
$$F = -k(x - x_0) - c v$$
- **Stiffness ($k$):** $180\text{--}300$
- **Damping ($c$):** $24\text{--}36$ (critically damped or slight single under-damped bounce)
- **Mass ($m$):** $1.0$

---

## 4. Medium & Substrate Matrix

### 1. Liquid Glass Substrate (`liquid-glass-js`)
- **Shader:** WebGL fragment shader with dynamic normal map refraction, specular highlight reflection, and chromatic dispersion ($R/G/B$ offset).
- **CSS Fallback:**
  ```css
  background: rgba(255, 255, 255, 0.65);
  backdrop-filter: blur(16px) saturate(180%);
  -webkit-backdrop-filter: blur(16px) saturate(180%);
  border: 1px solid rgba(255, 255, 255, 0.35);
  box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.08);
  ```

### 2. Terminal ANSI / Curses Substrate (`tui-studio`)
- **Grid:** Strict 80-column / 24-row fixed-pitch character cell grid.
- **Borders:** Unicode box-drawing characters (`┌─┐│└─┘` or double `╔═╗║╚═╝`).
- **Typography:** Fixed-width tabular monospace (`IBM Plex Mono`, `JetBrains Mono`). Zero proportional fonts.
- **Palette:** 16-color ANSI or 256-color terminal palette with strict high contrast.

### 3. Canvas High-Density Text Substrate (`pretext`)
- Direct canvas text measurement and multiline layout without triggering DOM layout thrashing.
- Exact subpixel glyph positioning for financial charts, real-time ledgers, and telemetry streams.

### 4. Conversational AI Agent Cockpit (`assistant-ui`)
- Multi-turn message streams with explicit distinction between user input, assistant thought traces, tool execution cards, and final outputs.
- Collapsible streaming reasoning panels with status badge indicators (`running`, `complete`, `error`).

### 5. Hardware / Industrial Blueprint Substrate (`nothing-design-skill` + `diagram-design`)
- Stark monochrome void (`#0f0f0f` or `#fafafa`) with hairline borders (`1px solid var(--hairline)`).
- NDOT 57 dot-matrix typography for model numbers, leader lines ($P\text{-}01, P\text{-}02$), torque callouts, and isometric exploded assemblies.

---

## 5. Copywriting Anti-Slop Discipline (`hallmark` + `stop-slop`)

1. **Buttons Must Name the Verb:**
   - ❌ Banned: "Submit", "Click Here", "Get Started", "Learn More", "Continue"
   - ✅ Allowed: "Deploy Cluster", "Generate Token", "Export CSV", "Download Spec", "Create Account"
2. **The 3-Part Error Formula:**
   $$\text{Error} = [\text{What Happened}] \longrightarrow [\text{Why It Happened}] \longrightarrow [\text{Concrete Imperative Action}]$$
   *Example:* "Database connection dropped (read timeout). Verify your VPC tunnel and retry."
3. **Silent Success:**
   - Zero toast notifications or congratulatory banners for normal, expected operations (e.g. saving an auto-saved draft).
   - Only surface confirmation alerts on irreversible destruction or critical state transitions.
4. **Anatomy Over Abstraction:**
   - Always display exact numbers and concrete units: "3 of 14 files indexed" rather than "Processing files...".
5. **Absolute Ban on Em-Dashes (` - `):**
   - Em-dashes in UI and spec copy are banned. Replace with hyphens (`-`), colons (`:`), commas, or separate sentences.

---

## 6. Strict Ban & Anti-Convergence Registry

| Category | Banned Clichés (Instant Reject) | Mandatory Alternative |
|---|---|---|
| **Layout** | Centered hero + 3 equal cards | Asymmetric golden ratio grid, editorial broadsheet column, or hardware TUI split |
| **Gradients** | Purple-to-blue linear gradients on white | Single bespoke pigment derived from physical product DNA |
| **Fonts** | Inter, Roboto, Space Grotesk, Plus Jakarta, Geist, Satoshi, Sora, Cabinet Grotesk | Bespoke pairings: Serif/Mono or Display Sans/Geometric Mono with weight contrast |
| **Serifs** | Fraunces or Instrument Serif by default | Earned serif choices (Source Serif 4, EB Garamond, Charter) justified by editorial context |
| **Surfaces** | Generic drop shadows (`box-shadow: 0 10px 25px rgba(0,0,0,0.1)`) | Solid 1px hairlines, surface lightness ladder, or real physical liquid glass |
| **Palette** | Tailwind `blue-500` / `indigo-600` / `#000000` / `#ffffff` | Micro-grain OKLCH pigments with anchor-tinted neutrals ($\text{chroma} \ge 0.006$) |

---

## 7. High-Craft Specialized Doctrines & Micro-Systems

### A. Emil Kowalski Interaction Laws (`emil-skills` / Linear & Vercel)
1. **Directional Easing Asymmetry:**
   - **Enter Animations:** MUST strictly use `ease-out` (rapid deceleration). The user initiated an action; the result must appear immediately. Never `ease-in` on enter.
   - **Exit Animations:** MUST strictly use `ease-in` (rapid acceleration out of frame). Once dismissed, elements should exit fast without lagging.
2. **GPU Compositing Rule (Zero Layout Thrashing):**
   - Strictly animate **`transform`** and **`opacity`** only.
   - Never animate `width`, `height`, `top`, `left`, `margin`, or `padding` (causes layout recalculation and dropped frames).
3. **Distance-Scaled Duration:**
   - Animation duration must scale dynamically with distance traveled ($d$). A 20px nudge takes ~100ms; a full-screen drawer take ~300ms. Fixed arbitrary durations feel sluggish or abrupt.
4. **Origin-Aware Spatial Anchoring:**
   - Set `transform-origin` to match the exact trigger source (e.g. dropdowns scale out directly from the button click coordinate, dialogs expand from the trigger pill).

### B. Geometry-Matched Skeletons (`boneyard`)
- Generic animated gray boxes are banned.
- Skeleton loading screens must mirror the exact layout geometry, aspect ratio, and typography heights of the resolved UI children to prevent layout shifts (CLS = 0).

### C. Curated Flow Calibration (`refero-skill`)
- Base complex workflows (onboarding funnels, multi-tier checkout, audit logs, command palettes) on empirically proven patterns from top production products rather than speculative wireframes.

### D. Mathematical Stroke Drawing (`tegaki`)
- For handwriting, sketch vectors, and signature line reveals, compute exact path lengths:
  $$\text{stroke-dasharray} = L, \quad \text{stroke-dashoffset}: L \longrightarrow 0$$
  where $L = \text{path.getTotalLength()}$, easing with `cubic-bezier(0.16, 1, 0.3, 1)`.

### E. Viscosity & Fluid Velocity Fields (`liquid-logo`)
- Fluid warping effects apply a Navier-Stokes grid approximation to SVG paths, maintaining volume conservation ($div(\mathbf{u}) = 0$) during distortion.

---

## 8. Calibrated Spring Physics Matrix & Interaction Tiers

Replace arbitrary `transition: all 0.3s ease` with standardized 4-tier spring physics:

| Interaction Tier | Stiffness ($k$) | Damping ($c$) | Mass ($m$) | Perceptual Feel | Real-World Application |
| :--- | :---: | :---: | :---: | :--- | :--- |
| **Tier 1: Snappy Inputs** | `400–500` | `30–35` | `0.8` | Instant, tactile press (<140ms) | Button press (`scale(0.97)`), switches, toggles |
| **Tier 2: Spatial Sheets** | `220–300` | `24–28` | `1.0` | Natural settle with 10% micro-bounce | Modals, bottom sheets, command palette drawer |
| **Tier 3: Fluid Trackers** | `120–180` | `12–16` | `1.0` | Organic glide with fluid inertia | Tab indicator pills, dynamic island, fluid cursor |
| **Tier 4: Hotkey Actions** |  -  |  -  |  -  | **Strict `0ms` (Instant)** | Actions triggered via Cmd+K, Esc, or arrow keys |

### Kinetic Interaction Rules
1. **Never Animate from `scale(0)`:** Enter from `scale(0.95)` + `opacity: 0`. Physical elements expand from a rest volume, never an infinitesimal singularity.
2. **Asymmetric Tooltip Delay:** Hover delay = `800–1000ms` (prevents flicker on casual cursor sweeps); Focus delay = `0ms` (keyboard users arrive with deliberate intent).
3. **Tabular Numerals Everywhere:** Every counter, timer, currency, and numerical column must enforce `font-variant-numeric: tabular-nums` (or OpenType `tnum` 1) to eliminate jitter.
4. **Optical Centering Shims:** Add `-1px` to `-2px` vertical compensation on uppercase icon/button labels to neutralize baseline descender pull.
5. **Text Balance & Pretty:** Enforce `text-wrap: balance` on headings (under 4 lines) and `text-wrap: pretty` on body copy to ban single-word dangling orphans.

---

## 9. Tested Substrates & Material Elevations (`AkashDesigns` & `awesome-design-md`)

### A. Substrate Pigment Library
- **Void Obsidian (`#08090a` / `#000000`):** Pure absence substrate (`oklch(0.12 0.005 260)`), hairline border `rgba(255, 255, 255, 0.08)`, card surface `#0e1219`.
- **Munken Parchment (`#fdfbf7`):** Warm tactile ground (`oklch(0.98 0.008 85)`), raw ink `#2c2825`, divider `#e8e4dc`.
- **Newsprint Rag (`#f4f1ea`):** Dense editorial paper (`oklch(0.95 0.012 88)`), muted charcoal `#59534a`, hairline rule `#d5cfc2`.
- **Bone Ceramic (`#f9f6f0`):** Polished mineral base (`oklch(0.97 0.008 90)`), elevated `#ffffff`, recessed wells `#ede7db`.

### B. Dark Mode Elevation (Banning Diffuse Black Drop-Shadows)
Dark mode surfaces cannot cast black shadows on dark backgrounds. Elevation is constructed through stepped lightness + inner specular bevels:
- **Base Canvas:** `#08090a` (0% lift)
- **Card Layer 1:** `#0e1219` + `border: 1px solid rgba(255, 255, 255, 0.06)` + `box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.08)`
- **Elevated Overlay / Modal:** `#161c26` + `border: 1px solid rgba(255, 255, 255, 0.12)` + `box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.15), 0 20px 40px rgba(0, 0, 0, 0.5)`

### C. Fast OKLCH Contrast Delta Pre-Check
If $|L_{\text{text}} - L_{\text{background}}| < 0.50$ (50% lightness delta in OKLCH), the pair is mathematically guaranteed to fail WCAG 4.5:1. Recalibrate immediately.

---

## 10. W3C DTCG Token Specification Standard

Emit tokens using the W3C Design Tokens Community Group standard (`$` prefix) for universal pipeline compilation (Tokens Studio, Style Dictionary, Figma):

```json
{
  "color": {
    "surface": {
      "base": { "$value": "#08090a", "$type": "color" },
      "card": { "$value": "#0e1219", "$type": "color" }
    },
    "accent": {
      "primary": { "$value": "#00f090", "$type": "color" }
    }
  },
  "motion": {
    "spring": {
      "snappy": {
        "$type": "cubicBezier",
        "$value": [0.16, 1, 0.3, 1]
      }
    }
  }
}
```

---

## 11. Apple Liquid Glass Optical Refraction & WebGL Zero-Jank Standards

### A. Liquid Glass SVG Displacement Refraction
True optical refraction displaces background geometry via SVG turbulence rather than flat blur:

```html
<svg width="0" height="0" class="absolute pointer-events-none" aria-hidden="true">
  <filter id="liquid-refract" x="-20%" y="-20%" width="140%" height="140%">
    <feTurbulence type="fractalNoise" baseFrequency="0.04" numOctaves="2" result="noise" />
    <feDisplacementMap in="SourceGraphic" in2="noise" scale="22" xChannelSelector="R" yChannelSelector="G" />
  </filter>
</svg>
```
```css
.liquid-glass-lens {
  backdrop-filter: url(#liquid-refract) blur(4px) saturate(1.25);
  -webkit-backdrop-filter: url(#liquid-refract) blur(4px) saturate(1.25);
  background: rgba(255, 255, 255, 0.03); /* Max 5% opacity to avoid milky haze */
  box-shadow: inset 0 1px 1px rgba(255, 255, 255, 0.25), 0 12px 32px rgba(0, 0, 0, 0.2);
}
```
**Chromium Invariants:** Ancestors must NOT have `isolation: isolate` or `opacity < 1`. Lens element must never have an explicit `z-index`.

### B. WebGL Zero-Jank Contract
1. **DPR Clamping:** Clamped to $\min(\text{window.devicePixelRatio}, 1.5)$ (max $2.0$). Uncapped 3x retina kills mobile battery and triggers frame drops.
2. **Visibility Culling:** Disconnect `requestAnimationFrame` when scrolled out of viewport via `IntersectionObserver`.
3. **1D Palette Textures (LUT):** Replace runtime `pow()` and trigonometric noise branches in fragment shaders with 256×1 precomputed 1D LUT textures.

---

## 12. Broadsheet & Retro-Computing Archetypes

### A. Multi-Column Broadsheet Editorial
- **Grid:** 4-to-6 column asymmetric newspaper grid (`grid-template-columns: repeat(4, minmax(0, 1fr))`) with 1px vertical hairline column dividers.
- **Hierarchy:** Kicker eyebrow + multi-column wrapped display headline + dateline string (`CITY, Country  -  Date`) + bold drop cap (`font-size: 3.5rem; float: left; line-height: 0.8; margin-right: 0.5rem`).

### B. Retro 1996 Computing Hardware
- **Surfaces:** Classic 3D beveled surfaces (Border-Top/Left: `2px solid #ffffff`, Border-Bottom/Right: `2px solid #808080`, Background: `#c0c0c0`).
- **Typography:** Tabular fixed-pitch bitmap or monospaced font with zero anti-aliasing.
- **Palettes:** Warm pastel ribbon tints (`#ffffe0` lemon chiffon, `#e0f0ff` ice blue) against industrial battleship gray.


