import tempfile

import streamlit as st
import google.generativeai as genai
from PyPDF2 import PdfReader

# Initialize the agent
#
genai.configure(api_key="YOUR_API_KEY")
model = genai.GenerativeModel("gemini-1.5-flash")


def get_gemini_response(instruction, text):
    """
    This function will take an instruction and text as input and return the response from the gemini model.
    """
    prompt = f"{instruction}\n\n{text}"
    response = llm.generate_content(prompt)
    return response.text


def main():
    st.title("PDF Summarizer and Quiz Generator")

    # Get API key from user
    api_key = st.text_input("Enter your Gemini API Key:", type="password")

    if api_key:
        llm.api_key = api_key

        uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

        if uploaded_file is not None:
            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
                tmp_file.write(uploaded_file.getvalue())
                pdf_path = tmp_file.name

            pdf_reader = PdfReader(pdf_path)
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text()

            st.subheader("PDF Content")
            st.text_area("Full Text", text, height=300)

            if st.button("Generate Summary"):
                instruction = "Summarize the following text:"
                summary = get_gemini_response(instruction, text)
                st.subheader("Summary")
                st.write(summary)

            if st.button("Create Quiz"):
                instruction = "Generate a multiple choice quiz from the following text:"
                quiz = get_gemini_response(instruction, text)
                st.subheader("Quiz")
                st.write(quiz)


if __name__ == "__main__":
    main()


