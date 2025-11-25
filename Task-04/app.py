import streamlit as st
import os
import asyncio
import tempfile
from pypdf import PdfReader
from pdf2image import convert_from_path
import pytesseract
from agent import summarize_document, generate_quiz

# ------------------------------------------------------------------
#  DESIGN SYSTEM – production palette, 8-pt grid, Inter
# ------------------------------------------------------------------
DS = {
    # colour
    "primary": "#2563eb",
    "primary-dark": "#1d4ed8",
    "surface": "#ffffff",
    "bg": "#f1f5f9",
    "border": "#e2e8f0",
    "text": "#1e293b",
    "text2": "#64748b",
    # type
    "font": "'Inter',-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif",
    # radius
    "r-sm": "6px",
    "r-md": "10px",
    "r-lg": "14px",
    "r-xl": "20px",
    # shadow
    "sh-sm": "0 1px 3px 0 rgba(0,0,0,.08),0 1px 2px 0 rgba(0,0,0,.06)",
    "sh-md": "0 4px 6px -1px rgba(0,0,0,.1),0 2px 4px -1px rgba(0,0,0,.06)",
    "sh-lg": "0 10px 15px -3px rgba(0,0,0,.1),0 4px 6px -2px rgba(0,0,0,.05)",
}


# ------------------------------------------------------------------
#  GLOBAL CSS – injected once
# ------------------------------------------------------------------
def _inject_css():
    st.markdown(
        f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    *{{box-sizing:border-box;-webkit-font-smoothing:antialiased}}
    .stApp{{font-family:{DS['font']};background:{DS['bg']};color:{DS['text']}}}
    h1,h2,h3{{font-weight:600;letter-spacing:-.02em;margin:0 0 .75rem 0}}
    h1{{font-size:2.25rem}}
    h2{{font-size:1.5rem}}
    h3{{font-size:1.25rem}}
    .block-container{{padding-top:2rem;padding-bottom:3rem}}
    /* buttons */
    .stButton>button{{
        border:none;border-radius:{DS['r-md']};font-weight:600;
        padding:.6rem 1.4rem;box-shadow:{DS['sh-sm']};
        background:linear-gradient(135deg,{DS['primary']} 0%,{DS['primary-dark']} 100%);
        color:#fff;transition:all .2s ease;
    }}
    .stButton>button:hover{{transform:translateY(-1px);box-shadow:{DS['sh-md']}}}
    /* inputs */
    .stTextInput>div>div,.stSelectbox>div>div{{
        border-radius:{DS['r-md']};border:1px solid {DS['border']};
        transition:border-color .2s,box-shadow .2s;
    }}
    .stTextInput>div>div:focus-within,.stSelectbox>div>div:focus-within{{
        border-color:{DS['primary']};box-shadow:0 0 0 3px {DS['primary']}20;
    }}
    /* cards */
    .card{{
        background:{DS['surface']};border:1px solid {DS['border']};
        border-radius:{DS['r-lg']};padding:1.5rem;box-shadow:{DS['sh-sm']};
        margin-bottom:1.5rem;
    }}
    /* uploader */
    .stFileUploader>section{{
        border:2px dashed {DS['border']};border-radius:{DS['r-lg']};
        background:#fff;transition:border-color .2s;
    }}
    .stFileUploader>section:hover{{border-color:{DS['primary']}}}
    /* Force dark text in uploader */
    [data-testid="stFileUploader"] {{color: {DS['text']} !important;}}
    [data-testid="stFileUploader"] small {{color: {DS['text2']} !important;}}
    [data-testid="stFileUploader"] span {{color: {DS['text']} !important;}}
    
    /* metrics */
    [data-testid="stMetricLabel"] {{color: {DS['text2']} !important;}}
    [data-testid="stMetricValue"] {{color: {DS['text']} !important;}}
    
    /* radio buttons */
    [data-testid="stRadio"] label {{color: {DS['text']} !important;}}
    [data-testid="stRadio"] div[role="radiogroup"] > label {{color: {DS['text']} !important;}}
    [data-testid="stRadio"] p {{color: {DS['text']} !important;}}
    
    /* tabs */
    .stTabs [data-baseweb="tab-list"]{{gap:1rem;border-bottom:1px solid {DS['border']}}}
    .stTabs [data-baseweb="tab"]{{
        height:3rem;font-weight:500;color:{DS['text2']};
        border-radius:{DS['r-md']} {DS['r-md']} 0 0;
    }}
    .stTabs [aria-selected="true"]{{
        color:{DS['primary']};border-bottom:2px solid {DS['primary']};
    }}
    /* hide menu/footer */
    #MainMenu,footer,header{{visibility:hidden}}
    </style>
    """,
        unsafe_allow_html=True,
    )


# ------------------------------------------------------------------
#  BUSINESS LOGIC
# ------------------------------------------------------------------
class DocProcessor:
    @staticmethod
    def fmt_size(b: int) -> str:
        for u in ["B", "KB", "MB", "GB"]:
            if b < 1024:
                return f"{b:.1f} {u}"
            b /= 1024
        return f"{b:.1f} TB"

    @staticmethod
    def extract(uploaded_file) -> tuple[str, str | None]:
        text, err = "", None
        ext = os.path.splitext(uploaded_file.name)[1].lower()

        # Configure Tesseract and Poppler paths if environment variables are set
        if "TESSERACT_PATH" in os.environ:
            pytesseract.pytesseract.tesseract_cmd = os.environ["TESSERACT_PATH"]
        if "POPPLER_PATH" in os.environ:
            os.environ["PATH"] += os.pathsep + os.environ["POPPLER_PATH"]

        try:
            if ext == ".pdf":
                with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
                    tmp.write(uploaded_file.getvalue())
                    tmp_path = tmp.name
                reader = PdfReader(tmp_path)
                for i, p in enumerate(reader.pages):
                    t = p.extract_text()
                    if t:
                        text += t
                    elif st.session_state.get("adv_ocr", False):  # OCR fallback only if adv_ocr is enabled
                        # Check if Tesseract and Poppler are configured for OCR
                        if "TESSERACT_PATH" not in os.environ:
                            err = "OCR is enabled but TESSERACT_PATH environment variable is not set."
                            break
                        if "POPPLER_PATH" not in os.environ:
                            err = "OCR is enabled but POPPLER_PATH environment variable is not set."
                            break
                        try:
                            imgs = convert_from_path(tmp_path, first_page=i + 1, last_page=i + 1)
                            if imgs:
                                text += pytesseract.image_to_string(imgs[0])
                        except Exception as ocr_e:
                            err = f"OCR failed on page {i+1}: {ocr_e}"
                            break
                os.unlink(tmp_path)
            elif ext == ".csv":
                text = uploaded_file.getvalue().decode("utf-8")
        except Exception as e:
            err = str(e)
        return text, err


# ------------------------------------------------------------------
#  UI COMPONENTS
# ------------------------------------------------------------------
def sidebar():
    with st.sidebar:
        st.markdown("### 🧠 EduGenius Pro")
        st.markdown("AI Learning Platform")
        st.markdown("---")
        model = st.selectbox("Model", ["Gemini Pro 1.5", "GPT-4 Turbo", "Claude 3 Opus"])
        temp = st.slider("Creativity", 0.0, 1.0, 0.7, 0.1)
        st.toggle("Advanced OCR", True, key="adv_ocr")
        st.markdown("---")
        st.markdown("### 📄 Recent")
        if "hist" not in st.session_state:
            st.session_state.hist = []
        if not st.session_state.hist:
            st.caption("No files yet")
        else:
            for f in st.session_state.hist[-5:]:
                st.button(f"📄 {f}", use_container_width=True, key=f"rec_{f}")


def upload_card() -> None:
    st.markdown("### 📤 Upload Document")
    st.caption("PDF or CSV  •  max 200 MB")
    file = st.file_uploader("Choose file", type=["pdf", "csv"], label_visibility="collapsed")
    if not file:
        st.session_state.text = None
        return

    b = len(file.getvalue())
    if b > 200 * 1024 * 1024:
        st.error("File > 200 MB"); return

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Name", file.name)
    with col2:
        st.metric("Size", DocProcessor.fmt_size(b))
    with col3:
        st.metric("Type", file.type.split("/")[-1].upper())

    if st.button("🚀 Process", type="primary", use_container_width=True):
        with st.spinner("Analysing…"):
            text, err = DocProcessor.extract(file)
            if text:
                st.session_state.text = text
                st.session_state.fname = file.name
                if "hist" not in st.session_state:
                    st.session_state.hist = []
                if file.name not in st.session_state.hist:
                    st.session_state.hist.append(file.name)
                st.success("✅ Document ready")
                st.rerun()
            else:
                st.error(f"Processing failed: {err}")


def actions_card():
    if not st.session_state.get("text"):
        st.info("Upload a document first"); return

    st.markdown("### ⚡ AI Actions")
    action = st.radio("Choose", ["Summarise", "Quiz"], horizontal=True, label_visibility="collapsed")
    st.markdown("---")

    if action == "Summarise":
        st.markdown("**Executive Summary**")
        st.caption("Concise overview of key points")
        if st.button("Generate", key="sum_btn", use_container_width=True):
            with st.spinner("Creating summary…"):
                try:
                    st.session_state.summary = asyncio.run(summarize_document(st.session_state.text))
                    st.session_state.quiz = None; st.rerun()
                except Exception as e:
                    st.error(str(e))
    else:
        c1, c2 = st.columns(2)
        with c1:
            diff = st.selectbox("Difficulty", ["Easy", "Medium", "Hard", "Expert"])
        with c2:
            n = st.number_input("Questions", 3, 20, 5)
        if st.button("Generate", key="quiz_btn", use_container_width=True):
            with st.spinner("Crafting quiz…"):
                try:
                    st.session_state.quiz = asyncio.run(generate_quiz(st.session_state.text, diff.lower(), n))
                    st.session_state.summary = None; st.rerun()
                except Exception as e:
                    st.error(str(e))


def workspace():
    if not st.session_state.get("text"):
        st.markdown(
            '<div style="text-align:center;padding:4rem 0;color:#94a3b8;">'
            "👋 Upload a document to begin</div>",
            unsafe_allow_html=True,
        ); return

    t1, t2, t3 = st.tabs(["📄 Preview", "📊 Summary", "🎯 Quiz"])
    with t1:
        st.caption(st.session_state.fname)
        st.text_area("Content", st.session_state.text, height=400, label_visibility="collapsed")
    with t2:
        if st.session_state.get("summary"):
            st.markdown(st.session_state.summary)
            st.download_button(
                "📥 Download", st.session_state.summary,
                file_name=f"{st.session_state.fname}_summary.md",
                use_container_width=True
            )
        else:
            st.info("Generate a summary first")
    with t3:
        if st.session_state.get("quiz"):
            st.markdown(st.session_state.quiz)
            st.download_button(
                "📥 Download", st.session_state.quiz,
                file_name=f"{st.session_state.fname}_quiz.md",
                use_container_width=True
            )
        else:
            st.info("Generate a quiz first")


# ------------------------------------------------------------------
#  MAIN
# ------------------------------------------------------------------
def main():
    st.set_page_config(
        page_title="EduGenius Pro | AI Learning Assistant",
        page_icon="🧠",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    _inject_css()
    # state
    for k in ("text", "fname", "summary", "quiz"):
        if k not in st.session_state:
            st.session_state[k] = None

    # layout
    sidebar()
    col1, col2 = st.columns([1, 2], gap="large")
    with col1:
        st.markdown("# 🎓 EduGenius Pro")
        st.markdown("Transform documents into intelligent learning materials")
        upload_card()
        with st.container():
            actions_card()
    with col2:
        workspace()


if __name__ == "__main__":
    main()