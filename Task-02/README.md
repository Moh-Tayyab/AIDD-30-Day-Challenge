# 30-Day Challenge: Task 2

## Part A: Core Concepts

### Nine Pillars Understanding

**Why is using AI Development Agents (like Gemini CLI) for repetitive setup tasks better for your growth as a system architect?**

A) Using AI Development Agents for repetitive setup tasks is better for your growth as a system architect because becoming an architect involves more than just writing code. It's about designing, integrating, and scaling AI systems. Automating repetitive tasks frees you to focus on these higher-level architectural concerns.

**Explain how the Nine Pillars of AIDD help a developer grow into an M-Shaped Developer?**

A) The Nine Pillars of AIDD enable a developer to combine practical, hands-on skills with strategic thinking. This dual capability allows them to solve complex problems holistically, making them proficient across multiple related domains, which is the essence of an M-Shaped Developer.

### Vibe Coding vs. Specification-Driven Development

**Why does Vibe Coding usually create problems after one week?**

A) Vibe Coding often leads to problems within a week because it is inherently unplanned and lacks a clear, predefined structure. This leads to code that is difficult to maintain, scale, and debug.

**How would Specification-Driven Development prevent those problems?**

A) Specification-Driven Development (SDD) prevents these issues by establishing clear specifications and requirements *before* any code is implemented. This ensures the developer knows exactly what to build and how to build it, resulting in a more robust and maintainable system.

### Architecture Thinking

**How does architecture-first thinking change the role of a developer in AIDD?**

A) In AI-Driven Development, an architecture-first approach elevates the developer's role from a simple coder to a strategic thinker. The focus shifts from just writing code to considering the system's long-term scalability, maintainability, and overall design.

**Explain why developers must think in layers and systems instead of raw code?**

A) Developers must think in layers and systems because modern software is incredibly complex. If everything were handled as raw, monolithic code, it would be nearly impossible to understand, debug, or update. A layered, systemic approach allows for modularity, separation of concerns, and easier management of complexity.

---

## PART B: Prompt Engineering

### PROMPT

Generate a 1-paragraph specification for an email validation function detailing its purpose, input/output parameters, and validation criteria for local-part (character rules, length, special character positioning) and domain.

### PARAGRAPH

> The email validation function shall accept a single string input representing a candidate email address and return a structured output containing a boolean validity status along with descriptive error messages. Its purpose is to ensure that the email adheres to standard formatting rules by validating both the local-part and domain components. For the local-part, the function must allow only permitted characters (letters, digits, and special characters such as `.!#$%&'*+/=?^_{|}~-`), enforce a maximum length of 64 characters, prevent consecutive or trailing dots, and ensure special characters do not appear at the beginning or end. For the domain, it must verify proper label formatting separated by dots, enforce alphanumeric-plus-hyphen rules, and validate the top-level domain (TLD). Clear and precise error messages should be returned for all violations, helping users understand exactly why an email is invalid.

---

## PART C: Multiple Choice Questions

**1. What is the main purpose of Spec-Driven Development?**
   A. Make coding faster
   B. Clear requirements before coding begins ✅
   C. Remove developers
   D. Avoid documentation

**2. What is the biggest mindset shift in AI-Driven Development?**
   A. Writing more code manually
   B. Thinking in systems and clear instructions ✅
   C. Memorizing more syntax
   D. Working without any tools

**3. Biggest failure of Vibe Coding?**
   A. AI stops responding
   B. Architecture becomes hard to extend ✅
   C. Code runs slow
   D. Fewer comments written

**4. Main advantage of using AI CLI agents (like Gemini CLI)?**
   A. They replace the developer completely
   B. Handle repetitive tasks so dev focuses on design & problem-solving ✅
   C. Make coding faster but less reliable
   D. Make coding optional

**5. What defines an M-Shaped Developer?**
   A. Knows little about everything
   B. Deep in only one field
   C. Deep skills in multiple related domains ✅
   D. Works without AI tools
