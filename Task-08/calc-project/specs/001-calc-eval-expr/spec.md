# Feature Specification: 001-calc-eval-expr - Evaluate Arithmetic Expressions

## 1. Introduction

This document specifies the requirements for the "Evaluate Arithmetic Expressions" feature within the calculator project. The primary goal is to provide functionality to parse and compute the result of mathematical expressions given as a string.

## 2. Goals

*   To enable the calculator to evaluate valid arithmetic expressions.
*   To support basic arithmetic operations.
*   To adhere to standard mathematical order of operations (PEMDAS/BODMAS).
*   To handle invalid expressions gracefully.

## 3. Scope

### In Scope

*   **Supported Operations**: Addition (+), Subtraction (-), Multiplication (*), Division (/).
*   **Numbers**: Non-negative integers and floating-point numbers.
*   **Parentheses**: Support for nested parentheses to control order of operations.
*   **Whitespace**: Expressions should be able to contain arbitrary whitespace.
*   **Error Handling**: Detection and reporting of invalid expressions (e.g., syntax errors, division by zero).

### Out of Scope

*   Advanced mathematical functions (e.g., trigonometry, logarithms, powers, square roots).
*   Variables or symbolic computation.
*   Expression assignment.
*   Negative numbers as direct input (e.g., `-5` as a literal, but `2-5` is in scope).
*   Unary minus/plus.

## 4. Functional Requirements

### FR1: Evaluate Valid Arithmetic Expression

The system shall take a string representing an arithmetic expression and return its computed numerical result.

*   **Input**: A string containing an arithmetic expression.
*   **Output**: A floating-point number representing the result of the evaluation.
*   **Examples**:
    *   "1 + 2" -> 3.0
    *   "3 * (4 + 5)" -> 27.0
    *   "10 / 2 - 1" -> 4.0
    *   "(1 + 2) * (3 - 1)" -> 6.0
    *   "2.5 * 2 + 1" -> 6.0

### FR2: Handle Order of Operations

The system shall correctly apply the standard mathematical order of operations (Parentheses, Exponents (not applicable here), Multiplication and Division (left to right), Addition and Subtraction (left to right)).

### FR3: Detect Invalid Expressions

The system shall detect and report errors for malformed or invalid expressions.

*   **Input**: An invalid string expression.
*   **Output**: An error message indicating the nature of the invalidity.
*   **Examples**:
    *   "1 + (2" -> "Mismatched parentheses" or "Invalid expression"
    *   "1 + / 2" -> "Syntax error"
    *   "10 / 0" -> "Division by zero"
    *   "abc + 1" -> "Invalid character"

## 5. Non-Functional Requirements

### NFR1: Accuracy

The evaluation should provide accurate results for floating-point arithmetic up to a reasonable precision (e.g., standard double-precision floating-point).

### NFR2: Performance

Expressions of moderate length (e.g., up to 100 characters with standard operations) should be evaluated within milliseconds.

### NFR3: Robustness

The system should not crash or enter an unrecoverable state due to invalid input.

## 6. Open Questions / Clarifications

*   What is the maximum expected length of an expression?
*   Should scientific notation be supported for input/output?
*   What specific error messages are expected for each type of invalid expression? (e.g., precise error codes or human-readable messages).
