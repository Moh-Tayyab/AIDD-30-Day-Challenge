---
name: "research-factcheck"
description: "Perform quick research checks and suggest reliable sources or note if claim is uncertain."
version: "1.0.0"
---

# Research & Fact-Check Skill

## When to use
- User asks "Is this fact true?" or "Give me sources for X".

## How this skill works
1. Identify factual claim(s).
2. If claim seems verifiable, return: short verdict (True/False/Unclear), confidence, suggested sources to check.
3. If web lookup required, recommend search queries or ask to permit web fetch tools.

## Output Format
- Claim
- Verdict + confidence
- Quick notes (1-2 lines)
- Suggested search queries / sources