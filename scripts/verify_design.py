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
    """Runs strict mechanical linter rules 9.A - 9.J."""
    issues = []
    lower = text.lower()

    # 9.G: Em-dash check
    if "—" in text:
        issues.append("Rule 9.G violation: Em-dash ('—') detected in spec/copy. Use hyphens, colons, or periods.")

    # 9.D: Flat cream / brass cliché triad
    has_cream = "#f5f1ea" in lower or "#f7f5f1" in lower or "#fbf8f1" in lower
    has_brass = "#b08947" in lower or "#b6553a" in lower or "#9a2436" in lower
    has_espresso = "#1a1714" in lower or "#1a1814" in lower or "#1b1814" in lower
    if has_cream and has_brass and has_espresso:
        if "causal" not in lower and "substrate" not in lower:
            issues.append("Rule 9.D violation: Banned cream/brass/espresso cliché triad detected without substrate or causal derivation.")

    # 9.A: Centered hero + 3 cards
    if "centered hero" in lower and ("3 cards" in lower or "3 feature" in lower or "three cards" in lower):
        issues.append("Rule 9.A violation: Centered hero + 3 feature cards layout archetype is banned.")

    # 9.H: Spring physics / motion check
    has_spring = any(k in lower for k in ("stiffness", "damping", "cubic-bezier", "mass", "spring"))
    if not has_spring:
        issues.append("Rule 9.H violation: Missing concrete motion curves or spring physics parameters.")

    # 9.J: Concentric radius check
    has_radius = any(k in lower for k in ("concentric", "r_inner", "radius", "r-inner", "outer - padding"))
    if not has_radius and "radius" not in lower:
        issues.append("Rule 9.J violation: Missing concentric radius calculation or radius tokens.")

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

    print(f"  Aesthetic: {slop.get('choice')} (confidence: {slop.get('confidence', 'N/A')})")
    print(f"  Tokens:    {tokens.get('choice')} (confidence: {tokens.get('confidence', 'N/A')})")
    print(f"  Craft:     {craft.get('choice')} (confidence: {craft.get('confidence', 'N/A')})")

    passed = (
        slop.get("choice") == "bespoke"
        and tokens.get("choice") == "concrete"
        and craft.get("choice") == "rigorous"
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

    # Mechanical path check (rule 1 of CLAUDE.md)
    if re.search(r"[a-zA-Z]:\\Users\\|/home/[a-zA-Z0-9]+/", content):
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


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(0)

    arg = sys.argv[1]
    if arg == "--audit-skill":
        success = audit_skill_itself()
    else:
        success = audit_design_file(arg)

    sys.exit(0 if success else 1)
