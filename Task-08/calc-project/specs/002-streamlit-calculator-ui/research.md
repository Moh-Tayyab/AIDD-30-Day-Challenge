# Research: 002-streamlit-calculator-ui - Streamlit Best Practices and Deployment

## 1. Streamlit Deployment Constraints & Scaling

### Problem Statement

The `IMPL_PLAN` for the Streamlit UI feature indicates "NEEDS CLARIFICATION" for specific resource limits for Streamlit deployment and scaling solutions for high concurrency.

### Findings and Assumptions

*   **Deployment**: Streamlit applications are typically deployed using `streamlit run app.py` and can be hosted on various platforms:
    *   **Streamlit Community Cloud**: Free, managed hosting for public apps, with some resource limits (e.g., RAM, CPU, app size). Good for demos and small projects.
    *   **Self-hosting (e.g., AWS EC2, GCP, Azure, Heroku, Docker)**: Provides more control over resources but requires manual setup and scaling management.
*   **Resource Limits (Community Cloud as baseline)**: While specific numbers vary and evolve, free tier usage often implies modest CPU/RAM (e.g., ~1-2 vCPU, ~4-8 GB RAM). Exceeding these leads to app restarts or slowdowns.
*   **Scaling for Concurrency**: A single Streamlit application instance is single-threaded per user session. For high concurrency, multiple Streamlit instances behind a load balancer are required. Each user session consumes resources (RAM/CPU) on the server.
*   **Current Feature Scope**: The current feature is designed for single-user interaction per session, aligning with typical Streamlit usage for internal tools, dashboards, or personal projects. High concurrency is explicitly out of initial scope.

### Resolution

The "NEEDS CLARIFICATION" for Constraints and Scale/Scope are resolved by acknowledging that for a personal project or internal tool, Streamlit Community Cloud (or a similarly resourced self-host) is adequate with implicit resource constraints. For high-concurrency external use, dedicated scaling infrastructure (load balancing multiple Streamlit instances) would be required, which is out of scope.

## 2. Streamlit Development Best Practices

### Problem Statement

To ensure a robust and maintainable Streamlit calculator UI, it's important to follow best practices for Streamlit development.

### Findings and Recommendations

*   **State Management (`st.session_state`)**: For interactive applications like a calculator, `st.session_state` is crucial for persisting values across reruns (e.g., the current expression, display value). All mutable state should be stored here.
*   **Modularization**: While `app.py` can be a single file, for larger apps, consider moving complex logic (like our `evaluate_expression` function) into separate Python modules (which we already do with `src/calculator/evaluation.py`).
*   **Performance Optimization**:
    *   **`st.cache_data` and `st.cache_resource`**: Use these decorators for expensive computations or data loading that don't change frequently to prevent re-running on every interaction. (Not directly applicable to our calculator logic which is real-time input-dependent, but good general knowledge).
    *   **Avoid unnecessary reruns**: Structure code to minimize computations that trigger full app reruns.
*   **UI/UX Design**:
    *   **Clarity over Complexity**: Keep the UI clean and focused. Use Streamlit's native widgets where possible.
    *   **Custom CSS**: For professional aesthetics, `st.markdown("<style>...</style>", unsafe_allow_html=True)` can be used to inject custom CSS for buttons, fonts, layout, etc. This allows overriding Streamlit's default styles.
    *   **Layout**: `st.columns`, `st.expander`, `st.sidebar` help organize the layout effectively. For a calculator, `st.columns` is ideal for button grids.
*   **Error Handling**: Present user-friendly error messages using `st.error` or `st.warning`. Our `evaluate_expression` already raises specific exceptions, which Streamlit can catch and display.
*   **Security**: Be mindful of displaying sensitive information or allowing arbitrary code execution (not a direct concern for this calculator but good practice).
*   **Version Control**: Integrate the Streamlit app into existing Git workflow.
