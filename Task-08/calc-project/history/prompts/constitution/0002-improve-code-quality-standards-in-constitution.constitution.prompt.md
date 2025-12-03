---
id: 0002
title: Improve Code Quality Standards in Constitution
stage: constitution
date_iso: 2025-11-15
surface: agent
model: gemini-1.5-flash
feature: none
branch: master
user: (Your Username)
command: /sp.constitution "Update @.specify/memory/constitution.md to improve Code Quality Standards - All functions must include type hints on parameters and return types - Example: `def add(a: float, b: float) -> float:` - All functions must include docstrings explaining what they do - Example: `"""Add two numbers and return the sum."""` - Follow PEP 8 naming conventions (lowercase_with_underscores for functions) - Lines must be under 100 characters - No magic numbers; use named constants - Bad: `if x > 10:` - Good: `if x > MAX_POWER_EXPONENT:`"
labels: ["constitution", "code-quality"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files_yaml:
  - .specify/memory/constitution.md
tests_yaml: []
---

## Prompt

```text
Update @.specify/memory/constitution.md to improve Code Quality Standards

- All functions must include type hints on parameters and return types
  - Example: `def add(a: float, b: float) -> float:`
- All functions must include docstrings explaining what they do
  - Example: `"""Add two numbers and return the sum."""`
- Follow PEP 8 naming conventions (lowercase_with_underscores for functions)
- Lines must be under 100 characters
- No magic numbers; use named constants
  - Bad: `if x > 10:`
  - Good: `if x > MAX_POWER_EXPONENT:`
```

## Response

The project constitution has been updated to version 0.2.0, incorporating improved code quality standards.

**New Version**: 0.2.0
**Version Bump Rationale**: MINOR bump, due to material expansion of guidance within the "Modern Python Standards" principle.

**Files Flagged for Manual Follow-up**:
*   `.specify/templates/plan-template.md`: The "Constitution Check" section needs to be manually updated to reflect the new principles.
*   `README.md`: If this file exists, it should be reviewed for project-specific guidance that might need updating based on the new constitution.

**Suggested Commit Message**:
```
docs: amend constitution to v0.2.0 (improve code quality standards)
```
```