"""Job Description Matcher component."""

import streamlit as st
from services.ai_service import AIService

def render_job_matcher_page():
    st.subheader("🎯 Job Description Keyword Matcher")
    st.write("Paste a target job posting below. ResumeForge will analyze your resume against the description and highlight missing keywords.")

    resume = st.session_state.resume
    resume.target_job_description = st.text_area(
        "Target Job Description:",
        value=resume.target_job_description,
        height=180,
        placeholder="Paste job requirements here..."
    )

    if st.button("✨ Match Resume against Job Description", use_container_width=True):
        if resume.target_job_description.strip():
            ai_service = AIService()
            resume_content = f"{resume.summary} " + " ".join([s for cat in resume.skill_categories for s in cat.skills])
            with st.spinner("Analyzing keyword density and requirements..."):
                result = ai_service.match_job_description(resume_content, resume.target_job_description)
                
                st.markdown("---")
                st.metric("Job Compatibility Match Score", f"{result.get('match_score', 75)}%")
                
                st.subheader("⚠️ Missing Keywords")
                for kw in result.get("missing_keywords", []):
                    st.warning(f"• **{kw}**")

                st.subheader("💡 Recommendations")
                for rec in result.get("recommendations", []):
                    st.info(f"• {rec}")
        else:
            st.error("Please paste a job description first.")