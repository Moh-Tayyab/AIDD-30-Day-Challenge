# EduGenius Pro

## AI Learning Platform

EduGenius Pro is an innovative AI-powered learning platform designed to transform your documents into intelligent and interactive learning materials. Upload your PDF or CSV files, and leverage the power of advanced AI models to generate concise summaries or challenging quizzes tailored to your needs.

## Features

-   **Document Upload:** Easily upload PDF and CSV files up to 200 MB.
-   **Intelligent Text Extraction:** Automatically extracts text from documents. Supports advanced Optical Character Recognition (OCR) for PDFs to accurately capture text from scanned documents or images within PDFs.
-   **AI-Powered Summarization:** Generate executive summaries of your documents to quickly grasp key concepts and main ideas.
-   **Customizable Quiz Generation:** Create engaging quizzes with adjustable difficulty levels (Easy, Medium, Hard, Expert) and specify the desired number of questions.
-   **Flexible AI Model Selection:** Choose from leading AI models such as Gemini Pro 1.5, GPT-4 Turbo, and Claude 3 Opus to power your summaries and quizzes.
-   **Creativity Control:** Adjust the "Creativity" (temperature) setting for AI model responses to fine-tune the output style.
-   **Recent Files History:** Keep track of your recently processed documents for quick access.
-   **Downloadable Output:** Download generated summaries and quizzes as Markdown files for offline review or sharing.
-   **Intuitive User Interface:** A clean, modern, and responsive interface built with Streamlit, featuring a custom design system.

## Technologies Used

-   **Streamlit:** For creating the interactive web application.
-   **OpenAI Agents SDK:** For interacting with various AI models to perform summarization and quiz generation.
-   **PyPDF:** For efficient extraction of text from PDF documents.
-   **PDF2Image:** For converting PDF pages into images, enabling OCR capabilities.
-   **PyTesseract:** A Python wrapper for Google's Tesseract-OCR Engine, used for advanced text recognition.
-   **`uv`:** A fast Python package installer and dependency resolver.

## Setup and Installation

Follow these steps to set up EduGenius Pro on your local machine.

### Prerequisites

-   Python 3.13 or newer
-   **Tesseract OCR Engine:** Required for advanced PDF OCR. Download and install it from [Tesseract Downloads](https://tesseract-ocr.github.io/tessdoc/Downloads.html).
-   **Poppler:** Required for `pdf2image` to convert PDFs to images. Download and install Poppler from [Poppler Releases](https://poppler.freedesktop.org/releases.html). Ensure `pdftocairo` and `pdfimages` are in your system's PATH.

### Installation Steps

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/EduGenius-Pro.git
    cd EduGenius-Pro
    ```
    *(Replace `https://github.com/your-username/EduGenius-Pro.git` with the actual repository URL)*

2.  **Create a virtual environment and install dependencies using `uv`:**
    ```bash
    uv venv
    source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
    uv pip install -r requirements.txt
    ```
    *(Note: If `requirements.txt` is not present, use `uv pip install openai-agents pypdf pdf2image pytesseract streamlit`)*

3.  **Set Environment Variables (for Advanced OCR):**
    If you plan to use the "Advanced OCR" feature, you must set the paths to your Tesseract executable and Poppler binaries.

    **For Windows:**
    ```bash
    $env:TESSERACT_PATH="C:\Program Files\Tesseract-OCR\tesseract.exe"
    $env:POPPLER_PATH="C:\path\to\poppler\bin"
    ```
    (Replace `C:\path\to\poppler\bin` with the actual path to your Poppler `bin` directory, e.g., `C:\Program Files\Poppler\bin`)

    **For macOS/Linux:**
    ```bash
    export TESSERACT_PATH="/usr/local/bin/tesseract" # or wherever tesseract is installed
    export POPPLER_PATH="/usr/local/bin" # or wherever poppler binaries are located
    ```

## How to Run

After setting up the environment and installing dependencies:

1.  **Activate your virtual environment:**
    ```bash
    source .venv/bin/activate # On Windows, use `.venv\Scripts\activate`
    ```

2.  **Run the Streamlit application:**
    ```bash
    uv run streamlit run app.py
    ```

    This will open the application in your web browser.

## Usage

1.  **Upload Document:** Use the "Upload Document" section to select a PDF or CSV file.
2.  **Process Document:** Click the "🚀 Process" button to extract text from your uploaded file.
3.  **Choose AI Action:** Select either "Summarise" or "Quiz" from the "AI Actions" section.
4.  **Configure AI Action:**
    *   For "Summarise," simply click "Generate."
    *   For "Quiz," choose the desired difficulty and number of questions, then click "Generate."
5.  **Review and Download:** View the generated summary or quiz in the workspace tabs and download them as Markdown files.

## Project Structure

```
.
├── agent.py            # AI agent logic (summarization, quiz generation)
├── app.py              # Main Streamlit application
├── pyproject.toml      # Project metadata and dependencies
├── uv.lock             # Lock file for uv dependency resolution
└── README.md           # This README file
```

## Contributing

Contributions are welcome! Please feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
