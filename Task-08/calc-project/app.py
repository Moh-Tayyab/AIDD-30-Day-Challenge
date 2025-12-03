import streamlit as st
from src.calculator.evaluation import evaluate_expression

# ==========================================
# 🎨 THEME & DESIGN SYSTEM
# ==========================================

class Theme:
    """
    Defines the visual style of the application using CSS.
    """
    
    # Modern Dark/Light Theme Palette
    COLORS = {
        "bg": "#f8fafc",             # Slate 50
        "surface": "#ffffff",        # White
        "primary": "#6366f1",        # Indigo 500
        "primary_hover": "#4f46e5",  # Indigo 600
        "secondary": "#e2e8f0",      # Slate 200
        "text_main": "#1e293b",      # Slate 800
        "text_muted": "#64748b",     # Slate 500
        "accent": "#f43f5e",         # Rose 500 (for clear/delete)
        "success": "#10b981",        # Emerald 500 (for equals)
        "font": "'Inter', -apple-system, BlinkMacSystemFont, sans-serif"
    }

    @staticmethod
    def inject_css():
        st.markdown(f"""
        <style>
            /* Import Font */
            @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

            /* Global Reset */
            .stApp {{
                background-color: {Theme.COLORS['bg']};
                font-family: {Theme.COLORS['font']};
            }}
            
            /* Hide Streamlit Elements */
            #MainMenu {{visibility: hidden;}}
            footer {{visibility: hidden;}}
            header {{visibility: hidden;}}

            /* Calculator Container */
            .calc-container {{
                max-width: 400px;
                margin: 0 auto;
                padding: 2rem;
                background: {Theme.COLORS['surface']};
                border-radius: 24px;
                box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
                border: 1px solid {Theme.COLORS['secondary']};
            }}

            /* Display Screen */
            .calc-display {{
                background: {Theme.COLORS['bg']};
                border-radius: 16px;
                padding: 1.5rem;
                margin-bottom: 1.5rem;
                text-align: right;
                box-shadow: inset 0 2px 4px 0 rgba(0, 0, 0, 0.06);
            }}
            
            .calc-display-value {{
                font-size: 2.5rem;
                font-weight: 700;
                color: {Theme.COLORS['text_main']};
                word-wrap: break-word;
                line-height: 1.2;
            }}
            
            .calc-display-history {{
                font-size: 1rem;
                color: {Theme.COLORS['text_muted']};
                min-height: 1.5rem;
                margin-bottom: 0.5rem;
            }}

            /* Buttons */
            .stButton button {{
                width: 100%;
                height: 64px;
                border-radius: 16px;
                border: none;
                font-size: 1.25rem;
                font-weight: 600;
                background-color: {Theme.COLORS['surface']};
                color: {Theme.COLORS['text_main']};
                box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
                transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
                border: 1px solid {Theme.COLORS['secondary']};
            }}

            .stButton button:hover {{
                transform: translateY(-2px);
                box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
                background-color: {Theme.COLORS['bg']};
            }}

            .stButton button:active {{
                transform: translateY(0);
                box-shadow: inset 0 2px 4px 0 rgba(0, 0, 0, 0.06);
            }}

            /* Operator Buttons */
            div[data-testid="column"] > div > div > div > button.operator-btn {{
                background-color: {Theme.COLORS['primary']};
                color: white;
            }}

            /* Special Buttons */
            .btn-primary button {{
                background-color: {Theme.COLORS['primary']} !important;
                color: white !important;
            }}
            .btn-primary button:hover {{
                background-color: {Theme.COLORS['primary_hover']} !important;
            }}
            
            .btn-accent button {{
                background-color: {Theme.COLORS['accent']} !important;
                color: white !important;
            }}
            
            .btn-success button {{
                background-color: {Theme.COLORS['success']} !important;
                color: white !important;
            }}

        </style>
        """, unsafe_allow_html=True)

# ==========================================
# 🧠 LOGIC & STATE
# ==========================================

class Calculator:
    """
    Handles the state and logic of the calculator.
    """
    def __init__(self):
        if "expression" not in st.session_state:
            st.session_state.expression = ""
        if "result" not in st.session_state:
            st.session_state.result = None
        if "history" not in st.session_state:
            st.session_state.history = ""

    def append(self, value: str):
        operators = ['+', '-', '*', '/']
        current_exp = st.session_state.expression

        # Reset if we have a result and user types a number (start new)
        if st.session_state.result is not None:
            if value in operators:
                # Continue calculation with previous result
                st.session_state.expression = str(st.session_state.result) + str(value)
            else:
                # Start fresh
                st.session_state.expression = str(value)
            st.session_state.result = None
            st.session_state.history = ""
        else:
            # Prevent duplicate operators
            if value in operators and current_exp and current_exp[-1] in operators:
                st.session_state.expression = current_exp[:-1] + str(value)
            else:
                st.session_state.expression += str(value)

    def clear(self):
        st.session_state.expression = ""
        st.session_state.result = None
        st.session_state.history = ""

    def backspace(self):
        if st.session_state.result is None:
            st.session_state.expression = st.session_state.expression[:-1]

    def calculate(self):
        if not st.session_state.expression:
            return

        try:
            # Store expression in history before calculating
            st.session_state.history = st.session_state.expression + " ="
            
            result = evaluate_expression(st.session_state.expression)
            
            # Format result to avoid unnecessary decimals
            if isinstance(result, float) and result.is_integer():
                result = int(result)
                
            st.session_state.result = result
            st.session_state.expression = str(result)
        except Exception as e:
            st.session_state.result = "Error"
            st.session_state.expression = ""

# ==========================================
# 🖥️ UI COMPONENTS
# ==========================================

def render_display():
    """Renders the calculator display screen."""
    history = st.session_state.get("history", "")
    current = st.session_state.get("expression", "0")
    if not current: current = "0"
    
    st.markdown(f"""
    <div class="calc-display">
        <div class="calc-display-history">{history}</div>
        <div class="calc-display-value">{current}</div>
    </div>
    """, unsafe_allow_html=True)

def render_keypad(calc):
    """Renders the calculator buttons grid."""
    
    # Row 1: Clear, Backspace, %, /
    c1, c2, c3, c4 = st.columns(4)
    with c1: 
        st.markdown('<div class="btn-accent">', unsafe_allow_html=True)
        st.button("AC", on_click=calc.clear, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    with c2: st.button("⌫", on_click=calc.backspace, use_container_width=True)
    with c3: st.button("(", on_click=calc.append, args=("(",), use_container_width=True)
    with c4: st.button(")", on_click=calc.append, args=(")",), use_container_width=True)

    # Row 2: 7, 8, 9, /
    c1, c2, c3, c4 = st.columns(4)
    with c1: st.button("7", on_click=calc.append, args=("7",), use_container_width=True)
    with c2: st.button("8", on_click=calc.append, args=("8",), use_container_width=True)
    with c3: st.button("9", on_click=calc.append, args=("9",), use_container_width=True)
    with c4: 
        st.markdown('<div class="btn-primary">', unsafe_allow_html=True)
        st.button("÷", on_click=calc.append, args=("/",), use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # Row 3: 4, 5, 6, *
    c1, c2, c3, c4 = st.columns(4)
    with c1: st.button("4", on_click=calc.append, args=("4",), use_container_width=True)
    with c2: st.button("5", on_click=calc.append, args=("5",), use_container_width=True)
    with c3: st.button("6", on_click=calc.append, args=("6",), use_container_width=True)
    with c4: 
        st.markdown('<div class="btn-primary">', unsafe_allow_html=True)
        st.button("×", on_click=calc.append, args=("*",), use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # Row 4: 1, 2, 3, -
    c1, c2, c3, c4 = st.columns(4)
    with c1: st.button("1", on_click=calc.append, args=("1",), use_container_width=True)
    with c2: st.button("2", on_click=calc.append, args=("2",), use_container_width=True)
    with c3: st.button("3", on_click=calc.append, args=("3",), use_container_width=True)
    with c4: 
        st.markdown('<div class="btn-primary">', unsafe_allow_html=True)
        st.button("−", on_click=calc.append, args=("-",), use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # Row 5: 0, ., =, +
    c1, c2, c3, c4 = st.columns(4)
    with c1: st.button("0", on_click=calc.append, args=("0",), use_container_width=True)
    with c2: st.button(".", on_click=calc.append, args=(".",), use_container_width=True)
    with c3: 
        st.markdown('<div class="btn-success">', unsafe_allow_html=True)
        st.button("=", on_click=calc.calculate, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    with c4: 
        st.markdown('<div class="btn-primary">', unsafe_allow_html=True)
        st.button("+", on_click=calc.append, args=("+",), use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# 🚀 MAIN APPLICATION
# ==========================================

def main():
    st.set_page_config(
        page_title="Calculator Pro",
        page_icon="🧮",
        layout="centered",
        initial_sidebar_state="collapsed"
    )
    
    Theme.inject_css()
    calc = Calculator()
    
    # Main Container
    st.markdown('<div class="calc-container">', unsafe_allow_html=True)
    
    st.markdown("### 🧮 Calculator Pro")
    render_display()
    render_keypad(calc)
    
    st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
