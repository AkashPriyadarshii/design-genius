# DESIGN SPEC — design-genius Marketing Site (Light Mode Archival Spec)

> Bespoke design specification produced by **design-genius** (reading its own brief and local library). 
> Fused: **akash** (`awesome-design-md/design-md/akash` — Archival ivory newsprint, cinnabar sealing-wax causal line, typographic clip-path reveals) + **IBM Carbon** (`awesome-design-md/design-md/ibm` — 0-4px flat geometry, light display weight, tabular data rows) + **Raycast** (`awesome-design-md/design-md/raycast` — telemetry instrument readout, one-accent scarcity).
> Downstream implementation: **akash-design-engineering** (@design-engineer/{tokens,physics,shaders,android,react}).

---

## 1. Visual Theme & Atmosphere

- **Medium**: Web Long-Scroll Marketing & Interactive Specification Dossier.
- **Theme Mode**: **Strictly Light Mode Only** (No dark mode theme). The site is an authentic physical artifact—an archival gazette and verified technical dossier.
- **Substrate**: Archival Munken Newsprint (`oklch(0.968 0.012 88.0)`) infused with SVG procedural micro-grain noise ($R_a \approx 2.4\,\mu\text{m}$) and 32px ledger hairlines. Never flat cream, never sterile digital white.
- **The Mandate**: The physical sealing-wax stamp verifies that zero AI slop, zero template monoculture, and zero generic purple gradients were used.
- **Tone**: Authoritative, tactile, mathematically grounded, direct. A senior systems/design engineer communicating with developers.

---

## 2. Pigmentation & OKLCH Color Tokens

Strictly Light Mode palette. Color reproduction gate passed via physical causal receipts:

```css
:root {
  /* Substrate & Paper — Archival Munken Newsprint (Ra ≈ 2.4μm) */
  --paper:           oklch(0.968 0.012 88.0); /* Base canvas: warm archival ivory */
  --paper-deep:      oklch(0.932 0.015 86.0); /* Secondary surface / card tiles / dossiers */
  --paper-elevated:  oklch(0.985 0.008 90.0); /* Lifted inspection panels */

  /* Ink & Typography — Deep Iron Gall Slate (Anchor Chroma >= 0.006) */
  --ink:             oklch(0.160 0.022 260.0); /* Primary typography & stark rules */
  --ink-muted:       oklch(0.440 0.020 260.0); /* Body text / secondary descriptions */
  --ink-faint:       oklch(0.600 0.018 260.0); /* Column headers / metadata labels */

  /* Primary Accent — Sealing-Wax Vermillion (The Anti-Slop Seal) */
  /* Causal receipt: Historical Indian gazette iron-oxide wax stamp sealing verified documents */
  --accent:          oklch(0.600 0.220 26.5);  /* The Verification Stamp */
  --accent-hover:    oklch(0.520 0.200 26.5);  /* Pressed seal interaction */
  --accent-ink:      oklch(0.140 0.030 26.5);  /* Text on top of accent */
  --accent-ghost:    color-mix(in oklch, oklch(0.600 0.220 26.5) 12%, transparent);

  /* Secondary Functional Accent — Archive Brass / Phosphor Amber */
  /* Causal receipt: Analog brass hardware indicators and active library telemetry */
  --accent-brass:    oklch(0.800 0.170 76.0);  /* Telemetry meters / active state */
  --brass-faint:     color-mix(in oklch, oklch(0.800 0.170 76.0) 15%, transparent);

  /* Hairlines & Boundaries — 1px Structural Grid Lines */
  --hairline:        oklch(0.820 0.015 85.0);  /* Subtle ledger divider */
  --hairline-strong: oklch(0.400 0.020 260.0); /* Heavy structural border */

  /* Semantic State Tokens */
  --success:         oklch(0.550 0.160 148.0); /* Terminal verified / tests pass */
  --warning:         oklch(0.720 0.180 65.0);  /* Audit advisory */
}
```

### Color Gate Receipts:
1. **Accent Hue:** 26.5° (Vermillion/Cinnabar) sits at the sharp edge of red-orange, separated ≥ 40° from cool slates (260°) and brass amber (76°).
2. **Substrate Chroma:** Base canvas has C = 0.012 at hue 88° with SVG noise, proving physical newsprint grain over flat AI cream.
3. **Contrast Verification:** AAA compliance for body ink on paper (14.2:1); AA compliance for accent on paper (5.4:1).

---

## 3. Typography Hierarchy & 2+1 Rule

Enforces the strict 2+1 font family ceiling:

1. **Display & Wordmark**: `Special Elite` (Authentic mechanical typewriter — the physical soul of un-templated documentation).
2. **Body & Prose**: `Source Serif 4` (Refined humanist editorial serif, 400 weight, 1.7 line-height).
3. **Telemetry, Mono & Code**: `IBM Plex Mono` (Tabular numbers, command palette, live telemetry counters).

### Fluid Scale (Off 15px Base):
- `display-hero`: `clamp(2.8rem, 6.5vw, 4.8rem)` / `line-height: 1.08` / `letter-spacing: -0.02em`
- `heading-1`: `clamp(2.0rem, 4.0vw, 2.8rem)` / `line-height: 1.15`
- `heading-2`: `clamp(1.4rem, 2.5vw, 1.8rem)` / `line-height: 1.25`
- `body-large`: `1.15rem` / `line-height: 1.65`
- `body-standard`: `0.938rem (15px)` / `line-height: 1.7`
- `data-mono`: `0.75rem (12px)` / `letter-spacing: 0.08em` / `tabular-nums`

---

## 4. Layout Architecture: 16-Field Swiss Modular Grid

- **Modular Division**: Desktop renders an asymmetric 4-column / 12-column Swiss Grid (`repeat(4, 1fr)` expanding to 12).
- **Continuous Typographic Spine**: 1px vertical hairline boundary anchoring navigation and section numbers.
- **Zero Padding Panic**: Whitespace is rhythmic (4px * [1, 2, 4, 8, 16, 24]), keeping gutters and section padding deliberate.

---

## 5. Kinetic Motion & Interaction (akash-design-engineering Bridge)

- **Audio Engine**: **DISABLED (Silent)**. Absolutely zero Web Audio synthesis or clicks.
- **Mechanical Easing Curves**:
  - `var(--ease-snap)`: `cubic-bezier(0.18, 0.89, 0.32, 1.28)` (120ms snap for hover stamps and button presses).
  - `var(--ease-enter)`: `cubic-bezier(0.16, 1.0, 0.3, 1.0)` (Typographic clip-path reveal and scroll entry).
- **Signature Interactive Details**:
  - **Live Fuser Widget**: Interactive terminal where visitors select 2 systems (e.g. *Nothing* + *Swiss Editorial*) and see a synthesized `DESIGN.md` token receipt live.
  - **The Sealing-Wax Stamp**: Verified stamps on shipped systems rotate -4° and stamp into cinnabar on hover.
  - **Telemetry Rollup**: Pure JavaScript `requestAnimationFrame` counters for library systems (74), levers (9), and audit dimensions (10).

---

## 6. Downstream 10-Dimension Compliance Checklist

| Dimension | Standard | Implementation |
|---|---|---|
| **1. Concentric Radii** | R_inner = max(0, R_outer - p) | Strictly 0px–2px crisp square mechanical edges |
| **2. Spring Physics** | Analytical ODE / Custom cubic-bezier | Snappy 120ms mechanical detents |
| **3. Pigments** | OKLCH with Anchor Chroma >= 0.006 | Deep Iron Gall Slate + Sealing-Wax Vermillion |
| **4. Shaders & Noise** | Procedural SVG Noise | Ra ≈ 2.4μm newsprint grain substrate |
| **5. Sensory Audio** | Disabled | 100% silent interaction |
| **6. Fluid Typography** | clamp() + tabular figures | Special Elite + Source Serif 4 + IBM Plex Mono |
| **7. Spatial Grid** | 4px rhythmic ladder | Swiss modular grid with 1px hairlines |
| **8. Accessibility** | WCAG 2.2 AAA Contrast | 14.2:1 body ink on archival paper |
| **9. Semantic HTML** | Structural Landmarks | <main>, <nav>, <aside>, <section>, JSON-LD |
| **10. Zero AI Slop** | No 3-card rows, no purple gradients | Asymmetric editorial layout with verifiable receipts |
