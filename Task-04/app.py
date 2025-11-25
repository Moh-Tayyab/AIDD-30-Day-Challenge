import tempfile
import os
import io
import asyncio
import streamlit as st
from pypdf import PdfReader
from agent import summarize_document, generate_quiz

# --- UI Configuration & Design System ---
def setup_page_config():
    st.set_page_config(
        page_title="AI EduTools - Study Smarter",
        page_icon="📚",
        layout="wide",
        initial_sidebar_state="collapsed"
    )

def load_custom_css():
    st.markdown("""
    <style>
        /* --- Design System Variables --- */
        :root {
            --primary-gradient: linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%);
            --bg-gradient: linear-gradient(135deg, #f8fafc 0%, #eef2ff 100%);
            --glass-bg: rgba(255, 255, 255, 0.7);
            --glass-border: 1px solid rgba(255, 255, 255, 0.5);
            --glass-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
            --text-primary: #1e293b;
            --text-secondary: #64748b;
            --accent-color: #6366f1;
            --success-color: #10b981;
            --warning-color: #f59e0b;
            --error-color: #ef4444;
            --radius-lg: 16px;
            --radius-md: 12px;
            --radius-sm: 8px;
        }

        /* --- Global Reset & Typography --- */
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
        
        html, body, [class*="st-"] {
            font-family: 'Inter', sans-serif;
            color: var(--text-primary);
        }

        .stApp {
            background: var(--bg-gradient);
            background-attachment: fixed;
        }

        /* --- Layout & Spacing --- */
        .block-container {
            padding-top: 2rem;
            padding-bottom: 4rem;
            max-width: 1000px;
        }

        /* --- Component: Header --- */
        .header-container {
            text-align: center;
            margin-bottom: 3rem;
            padding: 2rem;
            background: var(--glass-bg);
            backdrop-filter: blur(12px);
            border-radius: var(--radius-lg);
            border: var(--glass-border);
            box-shadow: var(--glass-shadow);
        }
        .header-title {
            font-size: 2.5rem;
            font-weight: 800;
            background: var(--primary-gradient);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 0.5rem;
            letter-spacing: -0.02em;
        }
        .header-subtitle {
            font-size: 1.1rem;
            color: var(--text-secondary);
            font-weight: 400;
        }

        /* --- Component: Cards --- */
        .ui-card {
            background: white;
            padding: 2rem;
            border-radius: var(--radius-lg);
            border: 1px solid #e2e8f0;
            box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.05);
            margin-bottom: 2rem;
            transition: transform 0.2s ease, box-shadow 0.2s ease;
        }
        .ui-card:hover {
            transform: translateY(-2px);
            box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.05);
        }
        .card-header {
            display: flex;
            align-items: center;
            gap: 1rem;
            margin-bottom: 1.5rem;
        }
        .step-badge {
            background: #e0e7ff;
            color: var(--accent-color);
            padding: 0.25rem 0.75rem;
            border-radius: 999px;
            font-size: 0.75rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.05em;
        }
        .card-title {
            font-size: 1.25rem;
            font-weight: 600;
            color: var(--text-primary);
            margin: 0;
        }

        /* --- Component: File Uploader --- */
        [data-testid="stFileUploader"] {
            padding: 2rem;
            border: 2px dashed #cbd5e1;
            border-radius: var(--radius-md);
            background: #f8fafc;
            transition: border-color 0.2s;
        }
        [data-testid="stFileUploader"]:hover {
            border-color: var(--accent-color);
            background: #f1f5f9;
        }
        [data-testid="stFileUploader"] section {
             padding: 0;
        }
        
        /* --- Component: Buttons --- */
        .stButton > button {
            width: 100%;
            border-radius: var(--radius-md);
            font-weight: 600;
            padding: 0.75rem 1.5rem;
            border: none;
            transition: all 0.2s;
        }
        /* Primary Button Style (default streamlit button) */
        .stButton > button {
            background: var(--primary-gradient);
            color: white;
            box-shadow: 0 4px 6px -1px rgba(99, 102, 241, 0.3);
        }
        .stButton > button:hover {
            opacity: 0.9;
            transform: translateY(-1px);
            box-shadow: 0 6px 8px -1px rgba(99, 102, 241, 0.4);
        }
        
        /* --- Component: Inputs & Selects --- */
        .stTextInput > div > div, .stSelectbox > div > div {
            border-radius: var(--radius-md);
            border-color: #e2e8f0;
        }
        .stTextInput > div > div:focus-within, .stSelectbox > div > div:focus-within {
            border-color: var(--accent-color);
            box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.1);
        }

        /* --- Component: Metrics --- */
        [data-testid="stMetric"] {
            background: #f8fafc;
            padding: 1rem;
            border-radius: var(--radius-md);
            border: 1px solid #e2e8f0;
        }
        [data-testid="stMetricLabel"] {
            font-size: 0.875rem;
            color: var(--text-secondary);
        }
        [data-testid="stMetricValue"] {
            font-size: 1.5rem;
            font-weight: 700;
            color: var(--text-primary);
        }

        /* --- Component: Status Messages --- */
        .stSuccess, .stInfo, .stWarning, .stError {
            border-radius: var(--radius-md);
            border: none;
            padding: 1rem;
        }
        .stSuccess { background: #ecfdf5; color: #065f46; }
        .stInfo { background: #eff6ff; color: #1e40af; }
        .stWarning { background: #fffbeb; color: #92400e; }
        .stError { background: #fef2f2; color: #991b1b; }

        /* --- Utilities --- */
        .text-sm { font-size: 0.875rem; color: var(--text-secondary); }
        .mb-4 { margin-bottom: 1rem; }
        .mt-2 { margin-top: 0.5rem; }
        
        /* Hide default elements */
        #MainMenu, header, footer { visibility: hidden; }
        
    </style>
    """, unsafe_allow_html=True)

# --- Helper Functions ---
def format_file_size(size_bytes):
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size_bytes < 1024.0:
            return f"{size_bytes:.2f} {unit}"
        size_bytes /= 1024.0
    return f"{size_bytes:.2f} TB"

def ui_card_start(step, title):
    st.markdown(f"""
    <div class="ui-card">
        <div class="card-header">
            <span class="step-badge">{step}</span>
            <h3 class="card-title">{title}</h3>
        </div>
    """, unsafe_allow_html=True)

def ui_card_end():
    st.markdown("</div>", unsafe_allow_html=True)

# --- Application Sections ---

def render_header():
    st.markdown("""
    <div class="header-container">
        <h1 class="header-title">AI EduTools</h1>
        <p class="header-subtitle">Transform your study materials into intelligent summaries and quizzes.</p>
    </div>
    """, unsafe_allow_html=True)

def render_footer():
    st.markdown("""
    <div style="text-align: center; margin-top: 4rem; padding-top: 2rem; border-top: 1px solid #e2e8f0;">
        <p class="text-sm">© 2024 AI EduTools • Built for Students</p>
    </div>
    """, unsafe_allow_html=True)

def render_file_upload():
    ui_card_start("Step 1", "Upload Document")
    
    st.markdown('<p class="text-sm mb-4">Upload your study material (PDF or CSV) to get started. Max size: 200MB.</p>', unsafe_allow_html=True)
    
    uploaded_file = st.file_uploader(
        "Upload file",
        type=["pdf", "csv"],
        label_visibility="collapsed"
    )

    if uploaded_file:
        file_size = len(uploaded_file.getvalue())
        max_size = 200 * 1024 * 1024

        st.markdown('<div class="mt-2"></div>', unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            st.metric("File Name", uploaded_file.name)
        with col2:
            st.metric("File Size", format_file_size(file_size))

        if file_size > max_size:
            st.error(f"File size ({format_file_size(file_size)}) exceeds 200MB limit.")
            st.session_state.text = ""
            ui_card_end()
            return None
            
    ui_card_end()
    return uploaded_file

def process_and_preview(uploaded_file):
    # Only process if it's a new file
    if st.session_state.last_uploaded_file_id != uploaded_file.file_id:
        with st.spinner("Processing document..."):
            text = ""
            file_ext = os.path.splitext(uploaded_file.name)[1].lower()
            
            try:
                if file_ext == ".pdf":
                    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
                        tmp.write(uploaded_file.getvalue())
                        tmp_path = tmp.name
                    
                    reader = PdfReader(tmp_path)
                    for page in reader.pages:
                        extracted = page.extract_text()
                        if extracted: text += extracted
                    
                    os.unlink(tmp_path)
                    
                elif file_ext == ".csv":
                    text = uploaded_file.getvalue().decode("utf-8")
                
                st.session_state.text = text
                st.session_state.last_uploaded_file_id = uploaded_file.file_id
                st.session_state.summary = ""
                st.session_state.quiz = ""
                
            except Exception as e:
                st.error(f"Error processing file: {str(e)}")
                st.session_state.text = ""

    # Preview Section
    if st.session_state.text:
        ui_card_start("Step 2", "Content Preview")
        
        chars = len(st.session_state.text)
        words = len(st.session_state.text.split())
        
        st.markdown(f"""
        <div style="display: flex; gap: 2rem; margin-bottom: 1rem; padding: 1rem; background: #f8fafc; border-radius: 8px;">
            <div>
                <span class="text-sm">Characters</span>
                <div style="font-weight: 600; font-size: 1.1rem;">{chars:,}</div>
            </div>
            <div>
                <span class="text-sm">Words</span>
                <div style="font-weight: 600; font-size: 1.1rem;">{words:,}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.text_area(
            "Preview",
            st.session_state.text[:1000] + "..." if len(st.session_state.text) > 1000 else st.session_state.text,
            height=150,
            label_visibility="collapsed"
        )
        ui_card_end()
        return True
    return False

def render_actions():
    ui_card_start("Step 3", "Choose Action")
    
    tab1, tab2 = st.tabs(["📋 Generate Summary", "❓ Generate Quiz"])
    
    with tab1:
        st.markdown('<div class="mt-2"></div>', unsafe_allow_html=True)
        st.markdown('<p class="text-sm">Create a concise summary of the key points from your document.</p>', unsafe_allow_html=True)
        if st.button("Generate Summary", key="btn_summary"):
            with st.spinner("Analyzing content..."):
                try:
                    res = asyncio.run(summarize_document(st.session_state.text))
                    st.session_state.summary = res
                    st.session_state.quiz = ""
                    st.rerun()
                except Exception as e:
                    st.error(f"Error: {e}")

    with tab2:
        st.markdown('<div class="mt-2"></div>', unsafe_allow_html=True)
        col1, col2 = st.columns([2, 1])
        with col1:
            st.markdown('<p class="text-sm" style="margin-top: 0.5rem;">Create a quiz to test your knowledge.</p>', unsafe_allow_html=True)
        with col2:
            difficulty = st.selectbox("Difficulty", ["medium", "hard", "phd-level"], label_visibility="collapsed")
            
        if st.button("Generate Quiz", key="btn_quiz"):
            with st.spinner("Generating questions..."):
                try:
                    res = asyncio.run(generate_quiz(st.session_state.text, difficulty, 5))
                    st.session_state.quiz = res
                    st.session_state.summary = ""
                    st.rerun()
                except Exception as e:
                    st.error(f"Error: {e}")
                    
    ui_card_end()

def render_results():
    if st.session_state.summary:
        st.markdown("""
        <div class="ui-card" style="border-left: 4px solid var(--accent-color);">
            <h3 class="card-title" style="margin-bottom: 1rem;">✨ Summary</h3>
        """, unsafe_allow_html=True)
        st.markdown(st.session_state.summary)
        st.markdown("</div>", unsafe_allow_html=True)

    if st.session_state.quiz:
        st.markdown("""
        <div class="ui-card" style="border-left: 4px solid var(--accent-color);">
            <h3 class="card-title" style="margin-bottom: 1rem;">🧠 Quiz</h3>
        """, unsafe_allow_html=True)
        st.markdown(st.session_state.quiz)
        st.markdown("</div>", unsafe_allow_html=True)

# --- Main Application ---
def main():
    setup_page_config()
    load_custom_css()
    
    # State Initialization
    if "text" not in st.session_state: st.session_state.text = ""
    if "summary" not in st.session_state: st.session_state.summary = ""
    if "quiz" not in st.session_state: st.session_state.quiz = ""
    if "last_uploaded_file_id" not in st.session_state: st.session_state.last_uploaded_file_id = None

    render_header()
    
    # Main Layout
    uploaded_file = render_file_upload()
    
    if uploaded_file:
        has_content = process_and_preview(uploaded_file)
        if has_content:
            render_actions()
            render_results()
            
    render_footer()

if __name__ == "__main__":
    main()