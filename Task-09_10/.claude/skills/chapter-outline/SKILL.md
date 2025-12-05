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