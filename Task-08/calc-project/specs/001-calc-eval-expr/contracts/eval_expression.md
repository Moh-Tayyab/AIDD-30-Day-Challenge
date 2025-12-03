# API Contract: Evaluate Expression Function

## Function: `evaluate_expression`

Provides functionality to parse and compute the result of mathematical expressions.

### Method Signature

```python
def evaluate_expression(expression: str) -> float:
```

### Parameters

*   **`expression`** (`str`):
    *   **Description**: The mathematical expression string to be evaluated.
    *   **Constraints**:
        *   Must be a non-empty string.
        *   Must contain only supported characters (digits, '.', '+', '-', '*', '/', '(', ')', whitespace).
        *   Must adhere to valid arithmetic syntax.
        *   Parentheses must be balanced.
        *   Length up to 100 characters (P0 assumption from research).

### Returns

*   **`float`**:
    *   **Description**: The computed numerical result of the expression.
    *   **Conditions**: Returned if the `expression` is valid and successfully evaluated.

### Raises

*   **`ValueError`**:
    *   **Description**: Raised for general invalid expressions or syntax errors.
    *   **Conditions**:
        *   Malformed syntax (e.g., `1 + (2`).
        *   Unsupported characters (e.g., `1 $ 2`).
        *   Mismatched parentheses.
        *   Empty input string.
    *   **Error Message Examples**:
        *   "Invalid expression: Mismatched parentheses."
        *   "Invalid expression: Syntax error near ')'."
        *   "Invalid expression: Unsupported character '$'."
*   **`ZeroDivisionError`**:
    *   **Description**: Raised when an attempt to divide by zero is detected.
    *   **Conditions**: Any division operation where the denominator evaluates to zero.
    *   **Error Message Example**:
        *   "Division by zero error."

### Behavior

*   Adheres to standard mathematical order of operations (PEMDAS/BODMAS).
*   Handles non-negative integers and floating-point numbers.
*   Ignores arbitrary whitespace in the expression string.
*   Provides clear, descriptive error messages upon failure.

### Example Usage

```python
from calculator.evaluation import evaluate_expression

# Successful evaluation
result = evaluate_expression("1 + 2 * (3 - 1)") # Expected: 5.0

# Error handling: Syntax error
try:
    evaluate_expression("1 + / 2")
except ValueError as e:
    print(e) # Expected: "Invalid expression: Syntax error near '/'."

# Error handling: Division by zero
try:
    evaluate_expression("10 / (5 - 5)")
except ZeroDivisionError as e:
    print(e) # Expected: "Division by zero error."
```
