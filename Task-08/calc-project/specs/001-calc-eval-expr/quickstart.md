# Quickstart: 001-calc-eval-expr - Evaluate Arithmetic Expressions

This guide provides a quick overview of how to use the `evaluate_expression` function for evaluating arithmetic expressions.

## Installation (Conceptual)

Assuming the `calculator` library is installed:

```bash
# This is a conceptual installation, actual command may vary
# pip install calculator
```

## Usage

The `evaluate_expression` function is available under the `calculator.evaluation` module.

### Basic Evaluation

To evaluate a simple arithmetic expression:

```python
from calculator.evaluation import evaluate_expression

expression = "5 * (10 - 2) + 3"
result = evaluate_expression(expression)
print(f"The result of '{expression}' is: {result}")
# Expected output: The result of '5 * (10 - 2) + 3' is: 43.0
```

### Handling Errors

The function raises specific exceptions for invalid expressions or conditions like division by zero. It's important to handle these in your code.

```python
from calculator.evaluation import evaluate_expression

# Example 1: Invalid syntax
invalid_expression_1 = "1 + (2"
try:
    evaluate_expression(invalid_expression_1)
except ValueError as e:
    print(f"Error evaluating '{invalid_expression_1}': {e}")
# Expected output: Error evaluating '1 + (2': Invalid expression: Mismatched parentheses.

# Example 2: Division by zero
invalid_expression_2 = "10 / (2 - 2)"
try:
    evaluate_expression(invalid_expression_2)
except ZeroDivisionError as e:
    print(f"Error evaluating '{invalid_expression_2}': {e}")
# Expected output: Error evaluating '10 / (2 - 2)': Division by zero error.
```

## Supported Features

*   Basic arithmetic operations: `+`, `-`, `*`, `/`.
*   Standard order of operations (PEMDAS/BODMAS).
*   Parentheses for grouping.
*   Non-negative integers and floating-point numbers.
*   Graceful error handling for invalid input.
