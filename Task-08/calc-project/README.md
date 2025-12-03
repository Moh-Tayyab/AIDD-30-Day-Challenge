# Calculator Project (Task-08)

This project implements a versatile calculator, featuring both a command-line interface (CLI) for expression evaluation and a modern, interactive web-based graphical user interface (GUI) built with Streamlit. Developed as part of Task-08, it demonstrates robust arithmetic evaluation capabilities and a modular architecture designed for easy extension.

## Features

-   **Expression Evaluation:** Capable of parsing and evaluating standard mathematical expressions.
-   **Basic Arithmetic Operations:** Supports addition (+), subtraction (-), multiplication (*), and division (/).
-   **Interactive CLI:** Evaluate expressions directly from your terminal.
-   **Streamlit GUI:** A user-friendly web interface with a digital calculator keypad, real-time expression display, and calculation history.
-   **Modular Design:** A clear separation of concerns between evaluation logic, operations, and user interfaces allows for easy maintenance and future enhancements.

## Project Structure

```
.
├───app.py                        # Streamlit web application for the GUI calculator
├───main.py                       # Basic demonstration of core arithmetic operations
├───run_eval.py                   # Command-line interface for interactive expression evaluation
├───src/                          # Core source code for the calculator logic
│   └───calculator/
│       ├───__init__.py
│       ├───evaluation.py         # Handles expression parsing and evaluation
│       ├───operations.py         # Defines basic arithmetic operations
│       └───utils.py              # Utility functions
├───tests/                        # Unit and integration tests
│   ├───integration/
│   └───unit/
│       ├───test_evaluation.py    # Tests for the expression evaluation logic
│       └───test_operations.py    # Tests for basic arithmetic operations
└───pyproject.toml                # Project metadata and dependencies
└───uv.lock                       # Lock file for `uv` dependency manager
```

## Setup & Installation

To get this project up and running on your local machine, follow these steps:

### Prerequisites

-   **Python 3.13+**: The project is developed and tested with Python 3.13 and newer.
-   **`uv` (recommended)** or `pip`: For efficient dependency management.

### Steps

1.  **Clone the repository:**
    Start by cloning the entire `AIDD-30-Day-Challenge` repository, which contains `Task-08`:
    ```bash
    git clone https://github.com/Moh-Tayyab/AIDD-30-Day-Challenge.git
    cd AIDD-30-Day-Challenge/Task-08/calc-project
    ```

2.  **Install dependencies:**
    It is highly recommended to use `uv` for installing dependencies due to its speed and reliability.
    ```bash
    uv sync
    ```
    If you prefer to use `pip`, you can install in editable mode:
    ```bash
    # pip install -e .
    ```

## Usage

### Command-Line Interface (CLI)

Run `run_eval.py` for an interactive CLI experience where you can input expressions directly:

```bash
python run_eval.py
```

Follow the prompts to enter expressions. Type `quit` to exit.

### Streamlit Graphical User Interface (GUI)

To launch the web-based calculator GUI:

```bash
streamlit run app.py
```

This will open the calculator interface in your web browser.

### Running Tests

To ensure everything is working correctly, you can run the provided tests:

```bash
pytest
```

## Contributing

Contributions are welcome! Please ensure that any new features or bug fixes include corresponding tests and adhere to the project's coding standards.

## License

This project is licensed under the [MIT License](LICENSE.md) - see the `LICENSE.md` file for details.
