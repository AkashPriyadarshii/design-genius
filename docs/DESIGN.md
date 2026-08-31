# DESIGN.md — design-genius marketing landing page

Unique look built by design-genius (self-applied). **Fusion:** Warp (warm-dark terminal canvas, editorial restraint) × The Verge (acid highlight, mono metadata). This is the design-genius thesis applied to its own page: prompt-driven, one amber accent, projects/list as terminal output lines, real links.

**Signature:** the page IS a terminal session. `$` prompts, a live-type headline, list rows as `ls`/`cat` output, one amber highlight, real links everywhere, block cursor blink as the only ambient motion.

## One-line pitch
"A developer's terminal rendered as a product page — warm dark, one amber highlight, the skill's own pipeline as terminal output, every claim a real link."

## Tokens
```
--canvas:     #0b0a09   (warm charcoal, not pure #000)
--canvas-2:   #12100e   (secondary surface — code/panel rows)
--canvas-3:   #1a1713   (hover surface)
--hairline:   #262119   (1px borders, flat depth)
--ink:        #e8e3d8   (primary text, warm parchment)
--body:       #a89f8e   (secondary text)
--mute:       #6e675a   (metadata)
--accent:     #ffb454   (warm amber — command prompts, highlights, CTA)
--accent-2:   #4a3a1e   (dark amber for tags/chips)
--ansi-green: #7bd88f   (real links — the shell's hyperlink color)
--ansi-red:   #ff6b6b   (errors/danger, sparing)
```
Typography:
- Display: **Instrument Serif** 400 italic for the headline — real serif, anti-slop type voice (not Inter).
- Body/code: **JetBrains Mono** (terminal face), used for everything mono (prompts, labels, metadata).
- Two faces only. Third face = dead weight, rejected.

## Layout (single scroll page)
- **Sticky window titlebar**: traffic dots + `design-genius@akashpriyadarshi ~/skill`. Blur on scroll.
- **Hero (prompt):** `$ npx design-genius "build me a look that isn't slop"` then result echo: serif headline "The design skill that never repeats itself." + block cursor. Sub: one line what it does.
- **`cat ./pipeline`** — the 4-stage pipeline as terminal output lines (harvest → read-gate → fuse → emit), each with a mono tag `#stage`.
- **`diff generic vs design-genius`** — the difference as a comparison block (shadcn / VoltAgent-who/copy / generic-slop / design-genius).
- **`ls ./examples`** — trigger-phrase list as terminal rows ("design a landing page for X", "rebuild my site not generic"...).
- **`cat ./install.sh`** — the install block as a copyable terminal code block (clone + junction/symlink + run). Real copy button optional; block must be correct.
- **Author/footer:** `$ whoami` → "Built by Akash Priyadarshi" + links (site, GitHub, resume) as real hrefs. `$ exit` + cursor.

## Motion (L2)
- Scroll-reveal + stagger (IntersectionObserver), rows lighten + amber left bar on hover, focus-within states, sticky titlebar blur.
- `prefers-reduced-motion` fallback kills all animation.
- Block cursor blink = the one ambient motion.

## A11y (gate)
- Contrast ≥4.5:1 body / 3:1 UI on every token pair. Keyboard-reachable with visible focus. No hover-only interactivity. Links describe destination. Mono labels aren't the only signal (color + text).

## Slop-rejection (checked)
- ✗ centered hero + 3 cards → prompt-driven terminal, rows not cards
- ✗ purple/blue gradient → flat warm charcoal, one amber accent
- ✗ generic shadows → 1px hairlines, flat depth
- ✗ Inter everywhere → Instrument Serif + JetBrains Mono (2 faces)
- ✗ dead links/placeholder copy → real hrefs (repo, site, GitHub, resume), real skill output
- ✗ no-motion / hover-only → keyboard focus + reduced-motion both present
- ✗ "Marketed" slop copy → one-line thesis + facts, no "Unlock the power"
