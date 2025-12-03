# Data Model: 002-streamlit-calculator-ui - Calculator UI State

## 1. Entity: Calculator UI State

Represents the transient state of the calculator user interface within a Streamlit session.

### Attributes

*   **expression**: `str`
    *   **Description**: The current mathematical expression string displayed and being built by the user.
    *   **Validation**: Must be a string. Can be empty.
    *   **Managed by**: Streamlit's `st.session_state`
*   **result**: `str` or `float`
    *   **Description**: The last computed result or an error message.
    *   **Validation**: Can be a valid float number or a string representing an error.
    *   **Managed by**: Streamlit's `st.session_state`
*   **last_button**: `str` (optional)
    *   **Description**: Stores the value of the last button pressed. Useful for preventing duplicate operator entries or managing complex UI logic.
    *   **Validation**: String.
    *   **Managed by**: Streamlit's `st.session_state`

### Relationships

*   None explicitly defined beyond the internal state management within a single Streamlit session.

### Validation Rules (Implicitly handled by `evaluate_expression` and UI logic)

*   **Expression Format**: The `expression` string will be validated by the `evaluate_expression` function on '=' button press.
*   **Input Sequence**: UI logic prevents invalid input sequences (e.g., "++", "*+").

### State Transitions (Implicit)

1.  **Initial**: `expression` is an empty string, `result` is empty/null.
2.  **Button Press (Number/Operator/Parenthesis)**: `expression` is updated.
3.  **Button Press ('C')**: `expression` and `result` are cleared.
4.  **Button Press ('=')**: `expression` is passed to `evaluate_expression`. `result` is updated with numerical result or error message.
