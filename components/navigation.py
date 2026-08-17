"""Top navigation bar for ResumeForge."""

import streamlit as st

def render_top_navbar():
    col_logo, col_nav = st.columns([2, 5])
    
    with col_logo:
        st.markdown("### 🛠️ **ResumeForge**")

    with col_nav:
        n1, n2, n3, n4, n5 = st.columns(5)
        with n1:
            if st.button("🏠 Home"):
                st.session_state["view_mode"] = "landing"
                st.rerun()
        with n2:
            if st.button("📝 Editor"):
                st.session_state["view_mode"] = "editor"
                st.rerun()
        with n3:
            if st.button("🎨 Templates"):
                st.session_state["view_mode"] = "templates"
                st.rerun()
        with n4:
            if st.button("🎯 Job Match"):
                st.session_state["view_mode"] = "job_match"
                st.rerun()
        with n5:
            if st.button("📂 My Resumes"):
                st.session_state["view_mode"] = "my_resumes"
                st.rerun()

    st.divider()