# CRITIQUE.md — design-genius REVISE mode (audit / review / critique / redesign)

Entered via SKILL.md Stage 0 when an existing design artifact is present in
the project. You are the auditor, not the original designer. Same doctrine as
NEW mode, different input (existing code) and output (a diff, not a blank
spec).

## 1. Read the real artifact (evidence, never memory)

List the project's styling surface and read the actual files:

```
index.html    → extract :root tokens, fonts, layout structure
*.css/*.scss  → hex values → HSL, type scale, spacing grid, shadows
DESIGN.md      → the stated intent (if present)
styles/ , app/ components → for larger codebases
```

Extract and print the ACTUAL palette as hex→HSL. Do not guess from a
screenshot or the repo's README. If a DESIGN.md exists, it is the product's
declared intent; the code is the reality. Score reality.

## 2. Classify: SLOP or DISTINCT

SLOP = any of the AI-default family:
- bg warm-cream (`#f1ede4`–`#fbfaf7`) or near-black (`#0a0a0a`–`#0d0b08`)
- accent Hue in **15°–45°** (orange-amber: `#FF4500`, `#E65100`, `#FE860F`,
  `#ff5c1f`, `#e8582c`, `#b3402a`, `#ffb454`, terracotta, amber)
- centered hero + 3 feature cards + footer
- Inter / Roboto / Space Grotesk / Plus Jakarta as the only faces
- purple or blue-purple gradient hero
- em-dashes as the default connector in prose

DISTINCT = palette/intent already off that family (accent hue outside 15–45°
on a non-warm bg, or a deliberate single accent that isn't orange-on-cream).
DISTINCT → say so, mark "no change needed," and stop. Do not force-color a
site that already cleared the band.

## 3. The scored rubric — all ten dimensions, pass/fail

Score each 1–10 and list every fail as a named action. Reuse the Stage 5 audit
dimensions: (1) color, (2) type, (3) spacing/rhythm, (4) component
consistency, (5) responsive below 768px, (6) dark/light both promised,
(7) motion baseline, (8) a11y gate, (9) density, (10) polish/craft. Plus the
four judgment checks: generic-at-a-glance, human copy, on-product or costume,
holds at the real payload. Hard fails are mechanical tells from the nine
levers: accent in band, em-dash spray, eyebrow overuse, CTA dead text
("Learn more"), serif-for-taste, drop-shadow-everything, centered-3-cards.

## 4. Emit the diff-DESIGN.md (what to change, exactly)

For every fail, output a change an agent can apply blind:

```
## Re-tint
--canvas: ...   (old #... → new #...)
--accent: ...   (old #... → new #..., Hue N° — proven outside 15–45°)

## Type swap
Inter → <distinctive face>  (why this pairing)

## Layout
centered-hero-3-cards → <archetype change>  (tokens are not a design; the
structure must change, not just the paint)

## Copy fix
"Learn more" → "Read the field log"  (verb/name the exact string)

## Hue proof
final accent {hex} = {HSL}: Hue {N}° → clears the band (outside 15–45° on a
non-warm bg). If it lands back in band, re-pick from another family.
```

Accent scarcity: one chromatic moment per viewport. Kill to one accent-bearing
element, white/neutral between color moments. Ink never pure `#000`.

## 5. Verify

After the fix map is applied, re-run step 2. It must now read DISTINCT. That
re-run is the verification; a redesign that still trips a mechanical tell is
not done. Report: per-fail pass/fail toggled, the hue proof number, one line
what the site became.

## 6. REDESIGN variant — full unique re-look, matched to product DNA

Use when intent is "redesign / rebuild / make it new," not "just fix the
slop." REVISE (above) surgically diffs the fails; REDESIGN rebuilds the whole
look from scratch — yet must stay THIS product's, never a costume and never
generic.

1. **Pull the product DNA from the real artifacts, not the brief.** Read the
   actual files (voice in the copy, the domain, the feature set, the real
   content). Name in one list: what the product IS, who it's for, the one
   emotion, what makes it different from a template. This is the debt you
   cannot break in the redesign.
2. **Redesign, don't retint.** Pick a structurally NEW archetype (Stage 4
   layout list), fresh accent from the domain router (Stage 4.5 — must clear
   15°–45°), new type pairing, new motion. It is not the old site with a new
   brush.
3. **The matched test (both directions, enforced):**
   - Not generic: a stranger sees no warm-cream/orange-amber default, no
     centered-3-cards, no Inter — the nine levers all pass.
   - Not a costume: a stranger says "that's clearly X's product," not "that
     looks like some other brand" and not "generic template." The DNA from
     step 1 must be visible: the content, voice, and domain read through the
     new look.
4. **Hue proof still required.** State the accent hex + Hue number; outside
   15°–45° on a non-warm bg. If it lands back in band, re-pick a different
   family.
5. **Verify:** re-run classify (step 2) on the redesign. Must read DISTINCT
   AND on-product. A redesign that is unique but off-brand is a fail; one
   that is on-brand but slop is also a fail. Both gates pass or it isn't
   done.

## Rules

- Audit is cold: read as a stranger, no loyalty to the existing design.
- One report, not a menu. If the user wants options, that's follow-up.
- Never redesign into a fallback AI-default to "fix" another ban (e.g. don't
  trade orange-on-cream for purple gradient, that's still in the family of
  slop). The re-pick must be structurally different, per Stage 4.5.
- Terse. Report + the diff map + the hue proof. No preamble.

## Reference

The nine levers, seed router, hue re-pick gate, and typecraft/motion/copy
mechanics all live in SKILL.md Stages 4–5. Reuse those rules verbatim; this
file only changes the input target and the output shape.
