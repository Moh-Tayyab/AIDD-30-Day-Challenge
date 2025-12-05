---
phr_id: "0004"
phr_title: "Implement Claude Skills Content"
phr_stage: "general"
phr_date: "2025-12-05"
phr_model: "gemini-1.5-pro"
phr_feature: "none"
phr_branch: "main"
phr_user: "user"
phr_command: "implement the skill content in Task-09_10"
phr_labels: ["claude-skills", "content"]
phr_links:
  spec: "null"
  ticket: "null"
  adr: "null"
  pr: "null"
phr_files_yaml:
  - "Task-09_10/.claude/skills/chapter-outline/SKILL.md"
  - "Task-09_10/.claude/skills/character-dev/SKILL.md"
  - "Task-09_10/.claude/skills/plot-checker/SKILL.md"
  - "Task-09_10/.claude/skills/research-factcheck/SKILL.md"
phr_tests_yaml: []
---

## Prompt Text

```
.claude/skills/chapter-outline/SKILL.md
---
name: "chapter-outline"
description: "Generate chapter-by-chapter outlines for a book. Use when user asks to create a book outline or chapters."
version: "1.0.0"
---

# Chapter Outline Skill

## When to use
- User asks: "Make a chapter outline for a [genre] book" or "Plan a book with N chapters".

## How this skill works
1. Ask for book genre, target audience, desired length (# chapters).
2. Create a high-level 8-12 chapter outline (title + 1-line summary each).
3. For each chapter, produce 3 key bullet points (main beats).
4. Optionally produce estimated word count per chapter.

## Output Format
- Title
- Target audience
- Chapters: numbered list with title + 1-line summary
- For each chapter: 3 bullet beats

## Example
**Input**: "Plan a 10-chapter sci-fi novel for teenagers about time travel"  
**Output**: (structured outline...)

.claude/skills/character-dev/SKILL.md

---
name: "character-development"
description: "Help design characters: backstory, motivation, arcs, and relationships."
version: "1.0.0"
---

# Character Development Skill

## When to use
- User asks to "create a protagonist" or "develop character arcs".

## How this skill works
1. Ask for role (protagonist/antagonist/support).
2. Produce: name, age, one-line hook, 3 backstory bullets, main motive, emotional arc, flaws, growth moments.
3. Suggest 3 scenes that reveal character.

## Output Format
- Name | Age | Hook
- Backstory (3 bullets)
- Motivation
- Arc (start → change → end)
- Scene suggestions (3)


.claude/skills/plot-checker/SKILL.md

---
name: "plot-consistency"
description: "Check a plot/outline for contradictions, timeline issues, and character motivation problems."
version: "1.0.0"
---

# Plot Consistency Skill

## When to use
- User pastes an outline or chapter drafts and asks "Check my plot" or "Find contradictions".

## How this skill works
1. Scan outline/draft.
2. Validate timeline (dates/ages/events).
3. Flag contradictions (character does X then later acts like X never happened).
4. Suggest fixes and short rewrites for confusing sections.

## Output Format
- Summary of issues (numbered)
- Each issue: location, why it's a problem, suggested fix

.claude/skills/research-factcheck/SKILL.md

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


please implement it in Task-09_10
```

## Response Text

All `SKILL.md` files have been updated with the provided content. The requested content for the skills has been successfully implemented in `Task-09_10`.
