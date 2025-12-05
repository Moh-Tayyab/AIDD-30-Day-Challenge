---
name: "chapter-outline"
description: "Specialized skill for generating structured, chapter-by-chapter outlines for book projects. Ideal for initial book planning and content structuring."
version: "1.0.0"
---

# Chapter Outline Skill: Strategic Book Structuring

## Overview
The Chapter Outline Skill is designed to assist authors and content creators in establishing a robust structural foundation for their books. It systematically generates detailed chapter outlines, providing a clear roadmap for the writing process.

## When to Employ This Skill
This skill is activated under the following circumstances:
*   User requests to "Create a chapter outline for a [genre] book."
*   User asks to "Plan a book with [N] chapters."
*   When a structured content plan is required before drafting commences.

## How This Skill Operates
The process for generating a chapter outline is highly interactive and structured:

1.  **Initial Query**: The skill will prompt the user for critical information:
    *   Desired book genre (e.g., Fantasy, Sci-Fi, Romance, Non-fiction).
    *   Target audience demographics or preferences.
    *   Preferred total number of chapters.
2.  **High-Level Outline Generation**: A comprehensive outline consisting of 8-12 chapters will be developed. Each chapter will feature:
    *   A concise, compelling title.
    *   A single-sentence summary capturing the essence of the chapter's content.
3.  **Detailed Chapter Beats**: For every chapter in the outline, three crucial bullet points will be provided, detailing the main narrative beats or thematic elements.
4.  **Optional Word Count Estimation**: Upon request, the skill can furnish an estimated word count for each chapter, aiding in project planning and scope management.

## Output Format
The generated outline will be presented in a clear, hierarchical Markdown format:

*   **Book Title**: [Proposed Title]
*   **Target Audience**: [Description of Target Audience]
*   **Chapters**:
    *   **Chapter 1: [Chapter Title]**
        *   *[One-line Summary of Chapter 1]*
        *   Main Beat 1: [Key event or topic]
        *   Main Beat 2: [Key event or topic]
        *   Main Beat 3: [Key event or topic]
        *   *(Optional: Estimated Word Count: [X words])
    *   **Chapter 2: [Chapter Title]**
        *   *[One-line Summary of Chapter 2]*
        *   Main Beat 1: [Key event or topic]
        *   Main Beat 2: [Key event or topic]
        *   Main Beat 3: [Key event or topic]
        *   *(Optional: Estimated Word Count: [X words])
    *   ... (Continues for all chapters)

## Example Interaction
**User Input**: "Plan a 10-chapter sci-fi novel for teenagers about time travel."  
**Expected Output**: A structured outline detailing ten chapters, each with a title, one-line summary, three key beats, and potentially estimated word counts, tailored for a teenage sci-fi audience.
