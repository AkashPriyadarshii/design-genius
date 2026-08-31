# design-genius

A Claude Code skill that writes a genuinely unique, non-slop `DESIGN.md` for
any design task. Landing page, portfolio, SaaS product page, app UI, dashboard,
site revamp. It reads a local design library, fuses two or three structurally
different real design systems, and emits one bespoke spec with real token
values, ready to hand to codegen. It never designs from the model's memory of
what "good design" looks like.

The design skill that never repeats itself.

---

## The problem it exists to kill

Every "claude design prompt" and "design skill" on the market ships the same
thing: a centered hero, three feature cards, a purple gradient, a generic
shadow, a headline that says "Modern SaaS." The reason is structural, not a
lack of effort. Those outputs come from the model's trained average of every
site it has seen, and the average of everything is nothing. It is forgettable
on arrival.

Design-genius refuses the average by refusing to work from memory at all. It
treats the model's remembered "good design" as exactly what it is: a source of
clichés. Proof lives in files, not vibes.

## How it works

A four-stage pipeline, always:

1. **Harvest intent.** One sharp question, never a form. It pulls audience,
   mood, brand voice, platform, and the single constraint that matters.
2. **Reason over the library.** It lists the design systems on disk, picks
   2-3 structurally different ones, and reads the actual token blocks. Real
   hex values, real type scales. Then it fuses two into a skeleton and texture,
   and borrows single tokens or levers from one or two more. Every borrow is
   named, so the spec carries its own receipts.
3. **Force uniqueness.** Nine levers, each one aimed at beating the AI
   default: layout archetype, color strategy, type voice, motion baseline,
   craft and micro-polish, a signature detail, copy discipline, a
   slop-rejection check, and a pre-mortem.
4. **Emit a buildable DESIGN.md.** Real token values, a full type scale,
   spacing, radius, component patterns, motion, and the signature detail. No
   `--accent: pick me`. A build tool can pick it up and ship.

A hard read-gate sits at the front: if it has not opened the actual library
files, it stops and reads. Designing without reading is vibecode, and the
skill is built to refuse it.

The pipeline ends with a cold self-audit against ten dimensions, plus, for
large or high-stakes tasks, one independent critic agent in a fresh context
whose fail list gets treated as ground truth.

## What makes it different

| Approach | What you get |
|----------|--------------|
| shadcn and UI libraries | Components, not identity |
| VoltAgent DESIGN.md systems | A static system you copy whole |
| Generic "design skills" and prompts | The average of everything, which is nothing |
| **design-genius** | A combined, bespoke design, one per request |

Where a component library gives you buttons, design-genius gives you the
identity those buttons live inside. Where a design-system corpus hands you one
person's whole look to adopt, it fuses the parts that fit your product and
cites what it took from each.

## Sounds like you

You reach for this when a phrase from the list triggers:

- "Design a landing page for X, not generic."
- "Rebuild my site. I don't want it to look like every other AI portfolio."
- "Make a unique look for Z."
- "I want a design system, not a theme."
- "No AI slop."
- "Give me a style, not a template."

It works from a text description, a PRD, a reference URL, or a screenshot. It
generalizes: it is not tuned to any one project or portfolio type, so the same
skill that ships a developer portfolio also ships a SaaS landing page or a
dashboard shell.

## The design library it reasons over

The skill reads a local design library. You control it, you grow it, and the
whole thing adapts to whatever is present. It `ls`es before it reads and
adjusts if a repo is missing.

Three repos are required:

- **VoltAgent/awesome-design-md** — 74 real design systems with hex tokens and
  type scales. The corpus and the ground truth.
- **xiaopu-ai web-design** — the engine room: scene defaults, interaction
  patterns, a motion library, style seeds, and the DESIGN.md template.
- **shadcn-ui/ui** — accessible component source for buildable output.

Optional repos add surface area: inspira-ui, animate-ui, pixel2motion,
ui-skills, diagram-design, threeui. The full clone list, the explicit skip
list, and the layout live in **[LIBRARY.md](LIBRARY.md)**. The path resolves
from the skill's own directory by default, or from `$DESIGN_LIB` when you set
it, so you can point the skill at any library folder you want.

The payoff is compounding. Drop any real design system into
`awesome-design-md/design-md/<name>/DESIGN.md` and the skill designs in that
direction too. Your taste becomes the library, and the library is what the
skill reasons over.

## Install (Claude Code)

```bash
ln -s "$PWD" ~/.claude/skills/design-genius   # macOS / Linux
# Windows (PowerShell), from this folder:
#   New-Item -ItemType Junction -Path $HOME\.claude\skills\design-genius -Target (Get-Location)
```

Clone the library, then say:

> "Use design-genius, build me a DESIGN.md for \<project\>."

It outputs the spec plus two closing lines: which systems got fused, and the
signature detail. Say "design X" for the look, "build X" once the spec is
ready. There is no menu of variants; one bespoke design per run, with variants
available as a follow-up.

## Documentation

- **[USAGE.md](USAGE.md)** — one-time setup, the two run modes, the critic,
  and how the skill gets better over time.
- **[LIBRARY.md](LIBRARY.md)** — what to clone, what to skip, and how the
  library grows.
- **[CONTRIBUTING.md](CONTRIBUTING.md)** — the corpus submission bar and the
  skill-diff rules for maintainers.
- **[CLAUDE.md](CLAUDE.md)** — agent instructions for anyone editing the
  skill itself.

## Build by

Design-genius is made by **Akash Priyadarshi**, an AI-augmented engineering
generalist who ships complete systems alone: Rust, Zig, Go, Kotlin, Dart,
TypeScript, and the agent workflows that multiply him. He builds everything he
uses and open-sources almost all of it.

More of his work: [akashpriyadarshi.vercel.app](https://akashpriyadarshi.vercel.app)
· [GitHub @AkashPriyadarshii](https://github.com/AkashPriyadarshii)

Design-genius grew out of a simple frustration: the same slop in every
"design prompt" he tried, and no way to teach a model to design instead of
average. So he built the thing that reads real design systems and fuses them,
and he open-sourced it because the more design systems people add, the better
it gets for everyone. If it saves you from one purple-gradient hero, the
hours it took were worth it.

## GitHub topics

Set these on the repository when you push (GitHub's topic limit is 20):

```
claude-code  claude-code-skill  design-system  design-tokens  ui-design
design  design-engineering  design-spec  non-slop  ai-design
design-skill  design-md  landing-page  ui-ux  brand-identity
design-engineer  claude  agent-skill  design-tools  frontend
```

## License

MIT. FOSS, on purpose. The value lives in the library-routing mechanism, so
the more design systems you or the community add, the more it compounds.
