<!--
Sync Impact Report:
Version Change: 0.1.0 -> 0.2.0 (MINOR: Expanded Code Quality Standards)
Modified Principles:
  - I. Test-First Development (no change)
  - II. Modern Python Standards (expanded with code quality rules)
  - III. Architectural Decision Records (ADRs) (no change)
  - IV. Object-Oriented Principles (no change)
  - V. Code Quality & Coverage (no change)
Added Sections:
  - Technical Stack & Version Control (no change)
  - Assumptions (implicitly added by filling content) (no change)
Removed Sections:
  - PRINCIPLE_6_NAME and PRINCIPLE_6_DESCRIPTION (empty in template) (no change)
  - SECTION_3_NAME and SECTION_3_CONTENT (empty in template) (no change)
Templates Requiring Updates:
  - .specify/templates/plan-template.md: ⚠ pending (The "Constitution Check" section needs to be updated to reflect the new principles. This will require a manual update or a future agent task.)
  - .specify/templates/spec-template.md: ✅ updated
  - .specify/templates/tasks-template.md: ✅ updated
  - .specify/templates/commands/*.md: ✅ updated (Directory not found, so no files to update.)
  - README.md: ⚠ pending (File not found, but if it existed, it would need review for project-specific guidance.)
Follow-up TODOs:
  - TODO(PROJECT_NAME): Confirm official project name.
-->
# Calculator Library Constitution

## Core Principles

### I. Test-First Development
All development MUST follow a Test-Driven Development (TDD) approach. Tests MUST be written and approved before implementation begins. The Red-Green-Refactor cycle MUST be strictly enforced.

### II. Modern Python Standards
All code MUST use Python 3.12+. All functions MUST include type hints on parameters and return types (e.g., `def add(a: float, b: float) -> float:`). All functions MUST include docstrings explaining their purpose (e.g., `"""Add two numbers and return the sum."""`). Code MUST follow PEP 8 naming conventions (e.g., `lowercase_with_underscores` for functions). Lines MUST be under 100 characters. Magic numbers are forbidden; named constants MUST be used instead (e.g., `if x > MAX_POWER_EXPONENT:` instead of `if x > 10:`). Code MUST be clean, readable, and adhere to Python's idiomatic practices.

### III. Architectural Decision Records (ADRs)
All significant architectural decisions MUST be documented using Architectural Decision Records (ADRs) to capture context, options, and rationale.

### IV. Object-Oriented Principles
All object-oriented code MUST adhere to essential OOP principles, including SOLID, DRY (Don't Repeat Yourself), and KISS (Keep It Simple, Stupid).

### V. Code Quality & Coverage
All tests MUST pass. The codebase MUST maintain at least 80% code coverage. `dataclasses` MUST be used for data structures where appropriate.

## Technical Stack & Version Control

The project MUST use Python 3.12+ with UV as the package manager. `pytest` MUST be used for all testing. All project files MUST be managed under Git version control.

## Governance

This Constitution supersedes all other project practices. Amendments require a documented proposal, team approval, and a migration plan for existing codebases. All pull requests and code reviews MUST verify compliance with these principles.

**Version**: 0.2.0 | **Ratified**: 2025-11-15 | **Last Amended**: 2025-11-15
