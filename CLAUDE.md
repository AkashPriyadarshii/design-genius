# CLAUDE.md

Agent instructions for this repository. Read this before editing design-genius.

## What this repo is

Design-genius. A Claude Code skill that emits a unique, non-slop `DESIGN.md`
spec by reading a local design library and fusing 2-3 structurally different
systems. It never designs from the model's memory of "good design."

## Layout

```
CLAUDE.md        these notes
README.md        headline + install + SEO/marketing surface
USAGE.md         how a user runs it
LIBRARY.md       what to clone, what to skip, how the library grows
CONTRIBUTING.md  corpus submission bar + skill-diff rules
SKILL.md         the skill itself (the only file that runs)
```

## Editing SKILL.md — the ground rules

1. **Never hardcode a machine path.** The library path resolves from the
   skill's own directory, or `$DESIGN_LIB`. A literal `C:\Users\...` or
   macOS home path in SKILL.md is a bug. Grep for it before committing.
2. **The read-gate is sacred.** Design-genius only works if it reads real
   files. Do not soften Stage 3's "STOP and read if you have not read" rule.
3. **Every lever earns its place.** Stage 4 lists nine. Adding one is
   justified only by a real, observed failure mode, not speculation. When you
   add a rule, cite the source system or failure it fixes.
4. **Keep the no-slop bar concrete.** Taste rules belong in the skill as
   mechanically checkable tells (banned palettes, capped eyebrows, CTA
   line-wrap), never as "make it look good" vibes.
5. **Audit your change like the skill audits output.** Cold read. Does this
   make the skill more likely to ship a bespoke design, or just longer?

## Testing

No test suite. The verification contract: change must not break the read-gate
or the output contract (DESIGN.md + fused-systems line + signature line). Run
the skill on one task after a substantive edit and confirm it still reads the
library and cites a real token.

## Releasing

- Bump material behavior changes in the frontmatter `description` so the
  skill trigger surface stays accurate.
- Keep README, USAGE, LIBRARY in sync when the pipeline changes. README says
  "nine levers," Stage 4 does not say "eight."
- LICENSE is MIT. External corpus files are not vendored; the library is
  cloned separately (see LIBRARY.md), so no third-party license obligations
  land in this repo.

## Non-goals

- No codegen. This skill emits the spec; web-design/shadcn build it. Do not
  add a build step here.
- No menu of designs. One bespoke spec per run. Variants are a stage-5
  follow-up, never the default.
- No image generation, no component source. The library supplies both.
