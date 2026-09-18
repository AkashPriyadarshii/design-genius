#!/usr/bin/env python3
"""
TypeSafe AI Jev Anti-Slop Design Validator for design-genius.

Model: jev-latest
Endpoint: https://api.typesafe.ai/v1/systemone
Standard library only (no pip installs).

Usage:
  python scripts/verify_design.py path/to/DESIGN.md
  python scripts/verify_design.py --audit-skill
"""

import json
import os
import re
import sys
import urllib.error
import urllib.request

API_URL = "https://api.typesafe.ai/v1/systemone"
SKILL_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def load_api_key():
    key = os.environ.get("TYPESAFE_API_KEY")
    if key:
        return key.strip()
    for cand in (".env", ".env.local"):
        p = os.path.join(SKILL_DIR, cand)
        if os.path.isfile(p):
            with open(p, "r", encoding="utf-8") as f:
                for line in f:
                    if line.strip().startswith("TYPESAFE_API_KEY="):
                        return line.strip().split("=", 1)[1].strip().strip('"\'')
    return None


def call_jev(state: str, questions: dict, timeout: float = 6.0) -> dict:
    key = load_api_key()
    if not key:
        return {"error": "TYPESAFE_API_KEY missing", "fallback": True}

    payload = {
        "model": "jev-latest",
        "state": state[:7500],
        "questions": questions,
    }

    req = urllib.request.Request(
        API_URL,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {key}",
            "Content-Type": "application/json",
            "User-Agent": "design-genius-validator/1.0",
        },
        method="POST",
    )

    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return {"success": True, "data": json.loads(resp.read().decode("utf-8"))}
    except Exception as e:
        return {"error": str(e), "fallback": True}


def mechanical_linter(text: str) -> tuple[bool, list[str]]:
    """Runs strict mechanical linter rules 9.A - 9.M."""
    issues = []

    # Strip code blocks and HTML comments for prose checks to prevent false positives
    prose_only = re.sub(r"```[\s\S]*?```", "", text)
    prose_only = re.sub(r"`[^`\n]+`", "", prose_only)
    prose_only = re.sub(r"<!--[\s\S]*?-->", "", prose_only)

    lower = text.lower()
    prose_lower = prose_only.lower()

    # 9.G: Em-dash check in prose only
    if "—" in prose_only:
        issues.append("Rule 9.G violation: Em-dash ('—') detected in spec/copy. Use hyphens, colons, or periods.")

    # 9.D: Flat cream / brass cliché triad
    has_cream = "#f5f1ea" in lower or "#f7f5f1" in lower or "#fbf8f1" in lower
    has_brass = "#b08947" in lower or "#b6553a" in lower or "#9a2436" in lower
    has_espresso = "#1a1714" in lower or "#1a1814" in lower or "#1b1814" in lower
    if has_cream and has_brass and has_espresso:
        if "causal" not in lower and "substrate" not in lower:
            issues.append("Rule 9.D violation: Banned cream/brass/espresso cliché triad detected without substrate or causal derivation.")

    # 9.A: Centered hero + 3 cards (in prose structure, ignoring negative warnings)
    if "centered hero" in prose_lower and ("3 cards" in prose_lower or "3 feature" in prose_lower or "three cards" in prose_lower):
        if not any(neg in prose_lower for neg in ("do not", "never", "no centered hero", "banned", "reject", "avoid")):
            issues.append("Rule 9.A violation: Centered hero + 3 feature cards layout archetype is banned.")

    # 9.H: Spring physics / motion check
    has_spring = any(k in lower for k in ("stiffness", "damping", "cubic-bezier", "mass", "spring"))
    if not has_spring:
        issues.append("Rule 9.H violation: Missing concrete motion curves or spring physics parameters.")

    # 9.J: Concentric radius check
    has_radius = any(k in lower for k in ("concentric", "r_inner", "radius", "r-inner", "outer - padding"))
    if not has_radius and "radius" not in lower:
        issues.append("Rule 9.J violation: Missing concentric radius calculation or radius tokens.")

    # 9.K: Zero-Simulation Linter (Blacklist + Positive Assertion Contract)
    if any(k in lower for k in ("svg map", "vector map doodle", "fake map", "mock countdown", "static weather widget", "mock weather")):
        issues.append("Rule 9.K violation: Pseudo-interactive simulation detected. Real GIS (Leaflet/MapLibre) and live APIs (Open-Meteo) required.")
    if any(k in lower for k in ("interactive map", "geographic map", "cartography", "gis map")):
        has_real_gis = any(k in lower for k in ("leaflet", "maplibre", "mapbox", "tilelayer", "tiles", "osm", "esri"))
        if not has_real_gis:
            issues.append("Rule 9.K violation: Geographic map specified without declaring real GIS engine (Leaflet/MapLibre) or tile layer provider.")
    if any(k in lower for k in ("weather widget", "live climate", "live weather", "temperature feed")):
        has_real_weather = any(k in lower for k in ("open-meteo", "api.open-meteo", "localstorage", "ttl", "fetchliveweather"))
        if not has_real_weather:
            issues.append("Rule 9.K violation: Dynamic weather feed specified without declaring live public API integration (Open-Meteo) or client-side TTL caching.")

    # 9.L: Media & Photographic Pipeline check for visual/showcase domains
    if any(k in lower for k in ("tourism", "travel", "heritage", "monument", "sanctuary", "temple", "hotel", "resort", "catalog")):
        has_photo_pipeline = any(k in lower for k in ("picture", "photo", "image", "lightbox", "aspect-", "aspect_ratio", "srcset", "webp", "dialog"))
        if not has_photo_pipeline:
            issues.append("Rule 9.L violation: Showcase or tourism domain missing photographic art direction, picture srcset, aspect-ratio containers, or lightbox inspector.")

    # 9.M: Domain Scope & Multi-Page Platform check (Regex quantifier for >=4 entities)
    multi_entity_match = re.search(r'\b([4-9]|[1-9][0-9]+)\s+(?:[a-zA-Z-]+\s+)?(shrines|temples|monuments|destinations|locations|items|products|models|entities|places|categories|routes|attractions|reserves|sanctuaries|parks|sites|regions)\b', lower)
    if multi_entity_match or any(k in lower for k in ("multi-entity", "distinct entities", "catalog of", "heritage sites")):
        has_multipage = any(k in lower for k in ("multi-page", "hub-and-spoke", "spoke", "spokes", "route hierarchy", "app router", "dynamic route", "subpage", "breadcrumbs", "dedicated page"))
        if not has_multipage and any(k in lower for k in ("single page", "1-page", "one-page", "single-page")):
            issues.append("Rule 9.M violation: Multi-entity scope (>3 entities) flattened into single-page layout. Hub-and-spoke multi-page platform required.")

    # 9.N: Interchangeable Dashboard Ban
    if any(k in lower for k in ("4 metric cards", "4 summary cards", "4 stat cards", "four metric cards")):
        has_dominant_object = any(k in lower for k in ("first-read", "dominant metric", "primary chart", "hierarchy proof", "focal object"))
        if not has_dominant_object:
            issues.append("Rule 9.N violation: Interchangeable 4-card metric dashboard detected without establishing a dominant First-Read Object or primary focal hierarchy.")

    # 9.O: 5-Second Contract & Pre-Ship Finish Gate
    if "design spec" in lower or "design.md" in lower:
        has_first_read = any(k in lower for k in ("first-read", "first read", "first_read", "primary action", "design contract", "pass or hold", "finish gate"))
        if not has_first_read:
            issues.append("Rule 9.O violation: Missing explicit 'First-Read Object' or 'Primary Action' declaration in the Design Contract.")

    # 9.P: Meaningless Empty State Ban
    if re.search(r'["\'](?:no data found|no items|no results found)["\']', lower):
        has_actionable_empty = any(k in lower for k in ("empty state", "shortcut", "create", "actionable", "guidance", "retry"))
        if not has_actionable_empty:
            issues.append("Rule 9.P violation: Meaningless empty state detected ('No data found'). Empty states must provide actionable guidance, creation shortcuts, or contextual charm.")

    return len(issues) == 0, issues


def heuristic_fallback_audit(text: str) -> dict:
    """Offline heuristic fallback if Jev is unreachable."""
    lower = text.lower()
    slop_tells = [
        "modern saas", "gradient hero", "purple/blue", "inter, roboto",
        "centered hero with 3 cards", "3 feature cards", "elevate", "cutting-edge"
    ]
    detected_slop = [tell for tell in slop_tells if tell in lower]
    has_tokens = bool(re.search(r"#[0-9a-fA-F]{3,8}|hsl\(|oklch\(", text))
    has_motion = "cubic-bezier" in lower or "stiffness" in lower or "spring" in lower

    mech_ok, mech_issues = mechanical_linter(text)
    if not mech_ok:
        detected_slop.extend(mech_issues)

    return {
        "slop_verdict": "slop" if detected_slop else "bespoke",
        "token_density": "concrete" if has_tokens else "vague",
        "motion_gate": "passed" if has_motion else "missing",
        "offline": True,
        "details": detected_slop,
    }


def audit_design_file(filepath: str) -> bool:
    if not os.path.isfile(filepath):
        print(f"[FAIL] File not found: {filepath}")
        return False

    with open(filepath, "r", encoding="utf-8", errors="replace") as f:
        content = f.read()

    print(f"\n[Jev] Auditing DESIGN.md: {filepath} ({len(content)} bytes)...")

    # Step 1: Mechanical linter pre-check
    mech_ok, mech_issues = mechanical_linter(content)
    if not mech_ok:
        print("  [WARN] Mechanical linter warnings:")
        for iss in mech_issues:
            print(f"    - {iss}")

    # Step 2: Semantic Jev System One evaluation
    questions = {
        "slop_assessment": {
            "type": "choice",
            "criteria": {
                "bespoke": "Distinctive design system with real tokens, domain-grounded palette, clear type hierarchy, and concrete motion/craft mechanics.",
                "ai_slop": "Generic AI template: centered hero + 3 cards, default purple/blue SaaS gradients, overused Inter font, or vague token hand-waving."
            }
        },
        "token_concreteness": {
            "type": "choice",
            "criteria": {
                "concrete": "Contains explicit hex/HSL/OKLCH values, exact optical radiuses, and spring physics numbers.",
                "vague_placeholders": "Contains generic placeholders, '--color: pick one', or unspecified dimensions."
            }
        },
        "craft_and_motion": {
            "type": "choice",
            "criteria": {
                "rigorous": "Includes interaction physics, reduced-motion fallbacks, focus states, and craft rules.",
                "deficient": "No motion tokens, no accessibility focus visible states, or vibes-only description."
            }
        },
        "production_standards": {
            "type": "choice",
            "criteria": {
                "production_grade": "Production-grade design specification meeting industry standards (concrete token ladders, responsive container rules, accessibility compliance, and real integrations where applicable).",
                "toy_simulation": "Relies on fake SVG map doodles instead of real GIS, un-wired static mock feeds, or single-page flattening of complex multi-entity catalogs."
            }
        }
    }

    res = call_jev(content, questions)
    if res.get("fallback"):
        print(f"  [fallback] Jev API unavailable ({res.get('error')}). Running offline heuristic scanner...")
        fb = heuristic_fallback_audit(content)
        print(f"  Slop scan:      {fb['slop_verdict'].upper()}")
        print(f"  Token density:  {fb['token_density']}")
        print(f"  Motion gate:    {fb['motion_gate']}")
        return fb["slop_verdict"] == "bespoke" and fb["token_density"] == "concrete"

    answers = res.get("data", {}).get("answers", {})
    slop = answers.get("slop_assessment", {})
    tokens = answers.get("token_concreteness", {})
    craft = answers.get("craft_and_motion", {})
    prod = answers.get("production_standards", {})

    print(f"  Aesthetic:   {slop.get('choice')} (confidence: {slop.get('confidence', 'N/A')})")
    print(f"  Tokens:      {tokens.get('choice')} (confidence: {tokens.get('confidence', 'N/A')})")
    print(f"  Craft:       {craft.get('choice')} (confidence: {craft.get('confidence', 'N/A')})")
    print(f"  Engineering: {prod.get('choice')} (confidence: {prod.get('confidence', 'N/A')})")

    passed = (
        slop.get("choice") == "bespoke"
        and tokens.get("choice") == "concrete"
        and craft.get("choice") == "rigorous"
        and prod.get("choice") != "toy_simulation"
        and mech_ok
    )

    if passed:
        print("  [OK] PASSED: Verified bespoke design system.")
        return True
    else:
        print("  [FAIL] REJECTED: Flagged slop, mechanical linter defect, or missing token rigor.")
        return False


def audit_skill_itself() -> bool:
    skill_file = os.path.join(SKILL_DIR, "SKILL.md")
    print(f"\n[Jev] Auditing SKILL.md for hardcoded paths, tone, and rigor...")
    with open(skill_file, "r", encoding="utf-8") as f:
        content = f.read()

    # Mechanical path check (rule 1 of CLAUDE.md) - Windows, Linux, macOS
    if re.search(r"[a-zA-Z]:\\Users\\|/home/[a-zA-Z0-9_-]+/|/Users/[a-zA-Z0-9_-]+/", content):
        print("  [FAIL] Machine-specific hardcoded path detected in SKILL.md!")
        return False
    else:
        print("  [ok] Machine path check passed (portable).")

    questions = {
        "instruction_rigor": {
            "type": "choice",
            "criteria": {
                "high_rigor": "Instruction set enforces concrete, mechanically verifiable rules against AI monoculture with zero corporate filler.",
                "slop": "Instructions contain vague vibes or generic advice."
            }
        }
    }

    res = call_jev(content[:6000], questions)
    if res.get("fallback"):
        print(f"  [skip] Jev offline: {res.get('error')}")
        return True

    answers = res.get("data", {}).get("answers", {})
    rigor = answers.get("instruction_rigor", {})
    print(f"  Instruction rigor: {rigor.get('choice')} (confidence: {rigor.get('confidence', 'N/A')})")
    return rigor.get("choice") == "high_rigor"


def audit_git_diff(ref: str = "HEAD~1..HEAD") -> bool:
    import subprocess
    print(f"\n[Jev] Auditing git diff ({ref}) with Jev System One...")
    try:
        diff = subprocess.check_output(["git", "diff", ref], cwd=SKILL_DIR).decode("utf-8", errors="replace")
    except Exception as e:
        print(f"  [FAIL] Failed to read git diff: {e}")
        return False

    if not diff.strip():
        try:
            diff = subprocess.check_output(["git", "diff", "HEAD"], cwd=SKILL_DIR).decode("utf-8", errors="replace")
        except Exception:
            pass
        if not diff.strip():
            print("  [info] Clean working tree, no diff to inspect.")
            return True

    # Check for hardcoded paths in diff (Windows, Linux, macOS)
    if re.search(r"[a-zA-Z]:\\Users\\|/home/[a-zA-Z0-9_-]+/|/Users/[a-zA-Z0-9_-]+/", diff):
        print("  [FAIL] Hardcoded machine path detected in git diff!")
        return False

    questions = {
        "has_hardcoded_paths": {
            "type": "choice",
            "criteria": {
                "no": "Clean portable paths with no machine-specific hardcoded directories.",
                "yes": "Contains machine-specific absolute file paths."
            }
        },
        "has_slop_or_filler": {
            "type": "choice",
            "criteria": {
                "no": "Concrete, engineering-focused design tokens and technical specifications.",
                "yes": "Contains corporate marketing buzzwords, vague filler, or hand-waving."
            }
        },
        "anti_slop_rigor": {
            "type": "choice",
            "criteria": {
                "high": "Enforces rigorous mathematical formulas, spring matrices, and anti-slop rules.",
                "low": "Weak or vague design guidance."
            }
        }
    }

    res = call_jev(diff[:7000], questions)
    if res.get("fallback"):
        print(f"  [skip] Jev offline: {res.get('error')}")
        return True

    answers = res.get("data", {}).get("answers", {})
    paths = answers.get("has_hardcoded_paths", {})
    filler = answers.get("has_slop_or_filler", {})
    rigor = answers.get("anti_slop_rigor", {})

    print(f"  Portable paths:   {paths.get('choice')} (confidence: {paths.get('confidence', 'N/A')})")
    print(f"  Zero slop/filler: {filler.get('choice')} (confidence: {filler.get('confidence', 'N/A')})")
    print(f"  Anti-slop rigor:  {rigor.get('choice')} (confidence: {rigor.get('confidence', 'N/A')})")

    passed = (
        paths.get("choice") == "no"
        and filler.get("choice") == "no"
        and rigor.get("choice") == "high"
    )
    if passed:
        print("  [OK] PASSED: Jev verified commit diff.")
        return True
    else:
        print("  [FAIL] REJECTED: Jev flagged issues in commit diff.")
        return False


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(0)

    arg = sys.argv[1]
    if arg == "--audit-skill":
        success = audit_skill_itself()
    elif arg == "--audit-diff":
        ref = sys.argv[2] if len(sys.argv) > 2 else "HEAD~1..HEAD"
        success = audit_git_diff(ref)
    else:
        success = audit_design_file(arg)

    sys.exit(0 if success else 1)

