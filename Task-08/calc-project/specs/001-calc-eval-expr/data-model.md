# Data Model: 001-calc-eval-expr - Expression Evaluation

## 1. Entity: Expression

Represents a mathematical expression to be evaluated.

### Attributes

*   **expression_string**: `str`
    *   **Description**: The raw input string representing the arithmetic expression.
    *   **Validation**: Must be a non-empty string.
*   **result**: `float` (after successful evaluation)
    *   **Description**: The computed numerical result of the expression.
    *   **Validation**: Must be a valid floating-point number.
*   **error_message**: `str` (in case of evaluation failure)
    *   **Description**: A human-readable message indicating the reason for an invalid expression or evaluation error.
    *   **Validation**: Non-empty string if an error occurred.

### Relationships

*   None explicitly defined for a single expression evaluation. The evaluation process is largely self-contained per expression.

### Validation Rules (from Feature Spec)

*   **Syntax**: Expression must adhere to valid arithmetic syntax (numbers, +, -, *, /, parentheses).
*   **Operations**: Only +, -, *, / are supported.
*   **Numbers**: Non-negative integers and floating-point numbers.
*   **Parentheses**: Must be balanced and correctly nested.
*   **Division by Zero**: Expressions resulting in division by zero are invalid.
*   **Invalid Characters**: Expression must not contain characters outside of supported numbers, operators, and parentheses.

### State Transitions (Implicit)

1.  **Initial**: `Expression` object created with `expression_string`. `result` and `error_message` are null/undefined.
2.  **Evaluating**: Internal parsing and computation occur.
3.  **Evaluated (Success)**: `result` is populated with the computed float value. `error_message` remains null/undefined.
4.  **Evaluated (Failure)**: `error_message` is populated with a description of the error. `result` remains null/undefined.
