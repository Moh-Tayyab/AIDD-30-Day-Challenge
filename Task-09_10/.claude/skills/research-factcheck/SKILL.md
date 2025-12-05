---
name: "research-factcheck"
description: "Specialized skill for performing rapid research checks, validating factual claims, and suggesting reliable sources. It can identify uncertainty in information."
version: "1.0.0"
---

# Research & Fact-Check Skill: Precision Information Validation

## Overview
The Research & Fact-Check Skill serves as an essential tool for verifying factual accuracy and sourcing information efficiently. It helps authors, researchers, and content creators ensure their work is grounded in verifiable data and provides confidence levels regarding the reliability of claims.

## When to Employ This Skill
This skill is critical in situations where:
*   User asks: "Is this fact true?" or "Verify the accuracy of this statement."
*   User requests: "Provide reliable sources for [specific information or claim]."
*   There is a need to establish the certainty of a factual assertion within a narrative or argument.

## How This Skill Operates
The fact-checking process is executed with a focus on speed and accuracy:

1.  **Claim Identification**: The skill first isolates and identifies specific factual claim(s) embedded within the user's query.
2.  **Verification & Verdict**: If the identified claim appears verifiable through existing knowledge or internal databases, it delivers:
    *   A concise verdict (True, False, or Unclear).
    *   A confidence level (High, Medium, Low) regarding the verdict's certainty.
    *   Suggestions for additional sources where the user can cross-reference the information.
3.  **External Lookup Recommendation**: If the claim necessitates an external web search for verification, the skill will:
    *   Recommend precise search queries to guide the user's own research.
    *   Alternatively, it may prompt the user for permission to utilize web fetch tools for direct online verification (if available and authorized).

## Output Format
The results are presented in a structured and easily interpretable format:

*   **Claim**: [The factual statement being verified]
*   **Verdict**: [True/False/Unclear]
*   **Confidence**: [High/Medium/Low]
*   **Quick Notes**: [1-2 concise lines providing context or brief explanation of the verdict]
*   **Suggested Search Queries / Sources**: [List of recommended search terms or direct source references for further investigation]

## Example Interaction
**User Input**: "Is it true that penguins can fly, and where can I find information about that?"  
**Expected Output**:
*   **Claim**: Penguins can fly.
*   **Verdict**: False
*   **Confidence**: High
*   **Quick Notes**: Penguins are flightless birds adapted for swimming.
*   **Suggested Search Queries / Sources**: "penguin flight capabilities", "evolution of penguins", "flightless birds"
