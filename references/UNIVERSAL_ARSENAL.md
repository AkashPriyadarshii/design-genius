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
5. **Absolute Ban on Em-Dashes (`—`):**
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
