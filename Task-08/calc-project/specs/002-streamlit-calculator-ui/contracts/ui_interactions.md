# UI Interaction Contract: Streamlit Calculator

This document outlines the contract for key user interactions within the Streamlit calculator UI and their expected effects on the application state, particularly concerning the integration with the `evaluate_expression` function.

## 1. Interaction: Button Click (Number/Decimal Point)

### Description
User clicks a numerical digit (0-9) or the decimal point (.).

### Input
*   `button_value`: `str` (e.g., "7", ".")

### Expected Behavior
*   The `button_value` is appended to the `st.session_state.expression` string.
*   The UI display area is updated to reflect the new `st.session_state.expression`.
*   If `st.session_state.result` contains a previous calculation result and the `button_value` is a number, the `st.session_state.expression` should be reset to `button_value` to start a new calculation.

## 2. Interaction: Button Click (Operator)

### Description
User clicks an arithmetic operator (+, -, *, /).

### Input
*   `button_value`: `str` (e.g., "+", "-")

### Expected Behavior
*   The `button_value` is appended to the `st.session_state.expression` string.
*   The UI display area is updated.
*   Logic to prevent multiple consecutive operators (e.g., "1++2") will be handled by replacing the last operator if one exists.

## 3. Interaction: Button Click (Parentheses)

### Description
User clicks an opening or closing parenthesis.

### Input
*   `button_value`: `str` (e.g., "(", ")")

### Expected Behavior
*   The `button_value` is appended to the `st.session_state.expression` string.
*   The UI display area is updated.

## 4. Interaction: Button Click (Clear - 'C')

### Description
User clicks the 'C' button.

### Input
*   None.

### Expected Behavior
*   `st.session_state.expression` is reset to an empty string.
*   `st.session_state.result` is reset to an empty string or None.
*   The UI display area is cleared.

## 5. Interaction: Button Click (Equals - '=')

### Description
User clicks the '=' button to trigger expression evaluation.

### Input
*   The current value of `st.session_state.expression`.

### Expected Behavior
1.  **Validation**: If `st.session_state.expression` is empty, no action is taken.
2.  **Evaluation Call**: The `evaluate_expression(st.session_state.expression)` function is called.
3.  **Result Handling**:
    *   If `evaluate_expression` returns a `float` result:
        *   `st.session_state.result` is updated with the float value.
        *   `st.session_state.expression` is updated with the `str()` representation of the result to allow continued calculation.
        *   The UI display area shows the result.
    *   If `evaluate_expression` raises `ValueError` or `ZeroDivisionError`:
        *   `st.session_state.result` is updated with the error message.
        *   The UI display area shows the error message prominently (e.g., `st.error`).
        *   `st.session_state.expression` remains as the invalid expression or is cleared, based on UX decision (cleared for simplicity).

## 6. Internal Contract: `evaluate_expression` function

### Description
This refers to the pre-existing Python function responsible for parsing and computing mathematical expressions.

### Method Signature
```python
def evaluate_expression(expression: str) -> float:
```

### Parameters
*   **`expression`** (`str`): The mathematical expression string.

### Returns
*   **`float`**: The computed numerical result.

### Raises
*   **`ValueError`**: For general invalid expressions (syntax errors, invalid characters, mismatched parentheses, etc.).
*   **`ZeroDivisionError`**: For division by zero.

### Integration Note
The Streamlit UI will act as a wrapper, passing the user-built `expression` string to this function and handling its return value or exceptions.
