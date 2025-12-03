# Research: 001-calc-eval-expr - Expression Parsing and Evaluation

## 1. Primary Dependencies: Expression Parsing and Evaluation

### Problem Statement

The "Evaluate Arithmetic Expressions" feature requires robust parsing and evaluation of mathematical expressions. The primary decision is whether to use existing Python libraries or implement a custom solution.

### Options Considered

#### Option A: Custom Implementation (Shunting-yard algorithm, Recursive Descent Parser)

*   **Description**: Implement a parser (e.g., using the Shunting-yard algorithm to convert infix to postfix notation, then evaluate postfix, or a Recursive Descent Parser to build an AST) and an evaluator from scratch.
*   **Pros**:
    *   Full control over logic and error messages.
    *   No external dependencies, potentially smaller footprint.
    *   Can be optimized for specific use cases.
*   **Cons**:
    *   Significant development effort and time.
    *   Higher risk of bugs (parsing can be complex).
    *   Reinventing the wheel; existing battle-tested solutions are available.
*   **Trade-offs**: High development cost vs. high control.

#### Option B: Using Python's `eval()`

*   **Description**: Directly use Python's built-in `eval()` function to evaluate the expression string.
*   **Pros**:
    *   Extremely simple and fast to implement.
    *   Handles full Python expression syntax out-of-the-box.
*   **Cons**:
    *   **Major Security Risk**: `eval()` can execute arbitrary Python code, making it highly dangerous for untrusted input. This is a critical security vulnerability for any public-facing application.
    *   Lack of fine-grained control over supported operations or error messages.
*   **Trade-offs**: Extreme ease of use vs. critical security vulnerability. **Not suitable for untrusted input.**

#### Option C: Using a Third-Party Parsing/Evaluation Library (e.g., `numexpr`, `ast` module, `pyparsing`, `simpleeval`)

*   **Description**: Leverage existing Python libraries designed for safe expression parsing and evaluation.
*   **Pros**:
    *   Reduced development time and effort.
    *   More robust and battle-tested than custom implementations.
    *   Often safer than `eval()` (e.g., `simpleeval` allows whitelisting operations).
    *   Provides more control than raw `eval()` (e.g., building ASTs with `ast` module).
*   **Cons**:
    *   Adds external dependencies.
    *   May introduce performance overhead if the library is overly general.
    *   Learning curve for the chosen library.
*   **Trade-offs**: Balance of development time, robustness, and control.

### Decision and Rationale

**Decision**: Implement a custom parser and evaluator, or use a well-vetted, secure third-party library like `simpleeval` or `pyparsing` if the project size and complexity justify the dependency.

**Rationale**: Option B (`eval()`) is explicitly rejected due to severe security risks when dealing with untrusted user input, which is a common scenario for calculator-like functionality. A custom implementation (Option A) provides maximum control but incurs significant development cost and risk. Using a robust third-party library (Option C) offers a good balance. For a calculator, a custom implementation of a parsing algorithm (like Shunting-yard) and an evaluator is a common educational exercise and can be efficient for basic arithmetic. If the expression complexity grows, a library would be preferred.

For the initial scope of basic arithmetic, a custom implementation or `simpleeval` would be suitable. Given the emphasis on "Modern Python Standards" and control over error messages, a **custom implementation** is tentatively preferred for its learning value and control, especially if the feature remains within the "in scope" boundaries. If "out of scope" features become necessary later, re-evaluating for a more comprehensive library will be required.

## 2. Constraints and Scale/Scope Assumptions

### Problem Statement

The `FEATURE_SPEC` defines performance goals ("Expressions of moderate length (e.g., up to 100 characters with standard operations) should be evaluated within milliseconds"). However, specific constraints (p95 latency, memory usage) and scale/scope (concurrent evaluations, max expression complexity) are "NEEDS CLARIFICATION". For planning, reasonable assumptions must be made.

### Assumptions and Rationale

*   **Constraint: p95 Latency**: Assume P95 latency for expression evaluation should be less than 50ms. This is well within the "milliseconds" goal for a user-facing interaction.
*   **Constraint: Memory Usage**: Assume memory usage per evaluation should be minimal, ideally under 5MB per expression. This is a conservative estimate for simple expressions.
*   **Scale/Scope: Concurrent Evaluations**: Assume the system will primarily handle single, sequential evaluations. If this feature were to be exposed via an API, we would assume low concurrency, e.g., < 10 concurrent evaluations per second. High concurrency is currently out of scope.
*   **Scale/Scope: Max Expression Complexity**: The `FEATURE_SPEC` mentions "up to 100 characters." We will assume this implies a maximum depth of nested parentheses of around 5-10 levels and approximately 20-30 operations.

### Rationale for Assumptions

These assumptions provide concrete targets for development and testing. They are derived from the "milliseconds" performance goal and typical usage patterns for a basic calculator. These need to be validated with the product owner/stakeholders as these are critical non-functional requirements.

### Resolution

The "NEEDS CLARIFICATION" for Constraints and Scale/Scope are resolved by proposing these assumptions for initial planning. These will require explicit validation.
