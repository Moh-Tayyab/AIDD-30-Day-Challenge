# Quickstart: 002-streamlit-calculator-ui - Professional Streamlit Calculator UI

This guide provides a quick overview of how to run and interact with the Streamlit-based calculator UI.

## 1. Installation

Ensure you have `uv` installed and activated your project environment.
Then install Streamlit:

```bash
uv pip install streamlit
```

## 2. Running the Application

From the project root directory, run the Streamlit application using:

```bash
uv run streamlit run app.py
```

This will open the calculator UI in your web browser, typically at `http://localhost:8501`.

## 3. Usage

Interact with the calculator by clicking the buttons for numbers, operators, and parentheses.

*   **Building Expressions**: Click numbers, operators (+, -, \*, /), and parentheses to form an expression.
*   **Clear Display**: Click the 'C' button to clear the current expression and result.
*   **Evaluate Expression**: Click the '=' button to calculate the result of the current expression.
*   **Error Handling**: Invalid expressions or division by zero will display an error message on the calculator screen.

## 4. Example Interaction

1.  Open the Streamlit app in your browser.
2.  Click `5`, then `\*`, then `(`, then `1`, then `+`, then `2`, then `)`, then `=`.
3.  The display should show `15.0`.
4.  Click `C`.
5.  Click `1`, then `/`, then `0`, then `=`.
6.  The display should show an error message like "Error: Division by zero error."
```