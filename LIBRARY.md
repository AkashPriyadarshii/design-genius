# library — what to clone, what to skip

design-genius reads a local design library. This maps the real repos, from an
audit of the working dir: which are gold, which are dead weight. Clone what
you need; the skill adapts to whatever is present (it `ls`es before reading).

## Required (the 3 the skill reasons over)

| Repo | Why | Clone |
|------|-----|-------|
| **VoltAgent/awesome-design-md** | THE corpus. 74 real design systems with hex tokens + type scale, no code. Ground truth. | `git clone --depth 1 https://github.com/VoltAgent/awesome-design-md.git` |
| **xiaopu-ai/web-design** | The "engine room": scene-defaults, interaction-patterns, motion-library, style-seeds, 59 design-systems, DESIGN.md template. | `git clone --depth 1 https://github.com/xiaopu-ai/web-design.git` |
| **shadcn-ui/ui** | Component source for accessible, real-usage builds. | `git clone --depth 1 https://github.com/shadcn-ui/ui.git` |

## Optional patterns (add surface, not required)

| Repo | What it adds |
|------|--------------|
| open-design | 94k★ Claude Design alternative, local-first design engine (prototypes, landing pages, decks) |
| .impeccable | 65k★ AI harness design language, craft constraints & anti-slop doctrine |
| taste-skill | 84k★ Prevents LLM design convergence into generic SaaS templates |
| hallmark | 28k★ Anti-AI-slop design skill and rigorous copy discipline |
| remotion | 58k★ Programmatic video creation with React & CSS |
| hyperframes | 44k★ Agent-ready HTML/CSS-to-video rendering |
| astryx | 12k★ Facebook agent-ready open-source design system |
| coss | 10k★ Official design system of Cal.com (`coss.com/ui`) |
| assistant-ui | 12k★ TypeScript/React primitives for AI chat & agent cockpit UI |
| mapcn | 12k★ Interactive shadcn-style map components |
| liquid-glass-js | 901★ Apple-inspired glassmorphism and real-time blur shaders |
| styleseed | 943★ 23 agent skills for fixed design jobs (contrast, typography, spacing) |
| tui-studio | 1.5k★ Visual design canvas for Terminal User Interfaces (TUIs) |
| inspira-ui | Modern React components (RibbonBackground etc.) |
| animate-ui | Motion/animation component patterns |
| pixel2motion | Motion reference patterns |
| ui-skills | Skills + reference (baseline-ui, fix-accessibility, improve-ui) |
| ui-ux-pro-max-skill | Broader design skill corpus (28MB — heavy, borderline bloat) |
| diagram-design | Editorial diagram HTML+SVG patterns |
| threeui | 3D UI — only clone if 3D is in scope (146MB, 1/3 of the whole lib) |
| react-bits | Animated React components, background shaders, kinetic text |
| img2threejs | 2D image to interactive Three.js / WebGL shader pipeline |
| nothing-design-skill | Dot-matrix, NDot typeface, monochrome + hot red archetype |
| scroll-craft | WebGL canvas scroll animations and GLSL post-processing |
| pretext | Pure canvas text layout and precise multi-line typography |

See `../README.md` for the full local inventory and the 151-repo starred design catalog.

## Skip — README-only shells (audit: zero token content)

- `official-design-md` — a 3.9KB README + LICENSE + empty .git, no design systems
- `awesome-claude-design` — 16KB README link list only
- `design-resources` — single README link list, redundant with the above

These add nothing over `awesome-design-md`. Trim them if you cloned them.

## Redundancy (fine, don't delete)

`awesome-design-md/design-md/` (74 systems) overlaps
`web-design/references/design-systems/` (59) on the same names
(apple/clay/linear/stripe/vercel). Both are real and the skill reads each
per-need — web-design's have the motion/scene scaffolding around them,
awesome's is the standalone corpus.

## Layout

Your library can be any folder. Default: sibling of `design-genius`. Override:
`DESIGN_LIB=<abs path>`.

```
your-design-library/
├── awesome-design-md/   # required — the 74-system corpus
├── web-design/          # required — engine room
├── shadcn-ui/           # required — component source
└── (optional) inspira-ui animate-ui pixel2motion ui-skills diagram-design ...
```

## Growing it (the real payoff)

Add any system to `awesome-design-md/design-md/<name>/DESIGN.md` and the
skill designs in that direction. Quality bar: real hex tokens, full type
scale, ≥13KB, extracted from something that exists — never invented. License
deets in CONTRIBUTING.md.
