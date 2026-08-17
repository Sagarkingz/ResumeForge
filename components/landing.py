"""Start Here landing page for ResumeForge."""

import streamlit as st
from models.resume_model import get_demo_resume, ResumeData
from services.ai_service import AIService

def render_landing_page():
    st.markdown("<h1 style='text-align: center;'>📄 ResumeForge</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: #6B7280;'>Build beautiful, ATS-friendly resumes in minutes.</h3>", unsafe_allow_html=True)
    st.write("")
    st.write("")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.info("### ✨ Build with AI")
        st.write("Type or paste your unstructured bio, experience, and education details. AI will organize everything into a formatted resume.")
        if st.button("Start AI Builder", use_container_width=True):
            st.session_state["view_mode"] = "ai_builder"
            st.rerun()

    with col2:
        st.success("### 📝 Build Manually")
        st.write("Fill in your personal information, work history, education, skills, and projects step-by-step using our editor.")
        if st.button("Start Manual Editor", use_container_width=True):
            st.session_state.resume = ResumeData()
            st.session_state["view_mode"] = "editor"
            st.rerun()

    with col3:
        st.warning("### 📄 Use Demo Resume")
        st.write("Explore ResumeForge with a fully populated sample resume to preview templates, colors, and scoring tools immediately.")
        if st.button("Load Sample Resume", use_container_width=True):
            st.session_state.resume = get_demo_resume()
            st.session_state["view_mode"] = "editor"
            st.rerun()

def render_ai_builder_landing():
    st.subheader("✨ Build Resume with AI")
    st.write("Tell us about yourself—your degree, job history, skills, and accomplishments. Don't worry about formatting; AI will structure it for you.")

    raw_bio = st.text_area(
        "Paste or type your details here:",
        height=200,
        placeholder="e.g. Sagar Goswami I am from patna bihar I have graduated in 2024 from patliputra university in B.A english honours..."
    )

    col1, col2 = st.columns([1, 4])
    with col1:
        if st.button("✨ Build My Resume", use_container_width=True):
            if raw_bio.strip():
                ai_service = AIService()
                with st.spinner("Parsing details and structuring your resume..."):
                    parsed_data = ai_service.parse_raw_bio_to_resume(raw_bio)
                    st.session_state.resume = ResumeData.from_dict(parsed_data)
                    st.session_state["view_mode"] = "editor"
                    st.rerun()
            else:
                st.error("Please enter your details before proceeding.")
    with col2:
        if st.button("Back to Home"):
            st.session_state["view_mode"] = "landing"
            st.rerun()