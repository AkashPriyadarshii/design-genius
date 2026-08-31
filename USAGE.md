# usage

## One-time setup

1. Install the skill (see README — symlink/junction into `~/.claude/skills/`).
2. Clone the library it reads. See **LIBRARY.md** for what to clone and what
   to skip — or just:
   ```bash
   mkdir -p design && cd design
   git clone --depth 1 https://github.com/VoltAgent/awesome-design-md.git
   git clone --depth 1 https://github.com/xiaopu-ai/web-design.git
   git clone --depth 1 https://github.com/shadcn-ui/ui.git
   ```
3. Make sure the skill can find the library:
   - Default: the library lives *beside* `design-genius` (same parent dir), or
   - Override: `export DESIGN_LIB=/abs/path/to/your/design/library`

## Two ways to run

**Manual (default).** Trigger by saying the trigger phrase:
`"design a landing page for X"`, `"rebuild my site, not generic"`,
`"make a unique look for Z"`, `"no AI slop"`. The skill runs its pipeline
in your context and emits `DESIGN.md` + the two closing lines (fused systems,
signature detail).

**Auto-fusion (recommended for a deliberate task).** In a fresh Claude Code
session pointing at the target project, say:
`"use design-genius, build me a DESIGN.md for <project>"`. Name WHICH two
systems you want fused if you have a hunch — otherwise the skill picks
structurally-different ones itself.

## The critic (unbiased check)

The skill audits its own output. For a big/high-stakes task it spawns ONE
independent critic agent (fresh context) that scores the DESIGN.md against a
harsh rubric and returns fails to fix. This is built into the pipeline — you
don't run it yourself.

## Making the skill better over time (the real payoff)

Drop any real design system into `awesome-design-md/design-md/<name>/DESIGN.md`
— real hex tokens, full type scale, ≥13KB. The skill then designs in that
direction too. See CONTRIBUTING.md.

## What it does NOT do

- No codegen. It emits the *spec* (DESIGN.md), then hands off to `web-design`
  / shadcn to build. Say "design X" for the look; say "build X" when the
  DESIGN.md is ready.
- No menu of options. One design per run. Want variants? Ask as a follow-up.
