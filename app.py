"""ResumeForge Main Streamlit Application."""

import streamlit as st
from models.resume_model import get_demo_resume
from services.storage_service import StorageService
from components.navigation import render_top_navbar
from components.landing import render_landing_page, render_ai_builder_landing
from components.template_gallery import render_template_gallery
from components.wizard_sections import render_editor_sections
from components.live_preview import render_live_preview_panel
from components.job_matcher import render_job_matcher_page

st.set_page_config(page_title="ResumeForge", page_icon="📄", layout="wide")

def main():
    storage = StorageService()

    # Session State Initialization
    if "resume" not in st.session_state:
        st.session_state.resume = get_demo_resume()
    if "view_mode" not in st.session_state:
        st.session_state["view_mode"] = "landing"

    # Top Navigation Bar
    render_top_navbar()

    view = st.session_state["view_mode"]

    if view == "landing":
        render_landing_page()
    elif view == "ai_builder":
        render_ai_builder_landing()
    elif view == "templates":
        render_template_gallery()
    elif view == "job_match":
        render_job_matcher_page()
    elif view == "my_resumes":
        st.subheader("📂 My Saved Resumes")
        resumes = storage.list_resumes()
        if resumes:
            for r in resumes:
                c1, c2 = st.columns([3, 1])
                with c1:
                    st.write(f"**{r['title']}** (Updated: {r['updated_at']})")
                with c2:
                    if st.button("Load", key=f"load_res_{r['id']}"):
                        loaded = storage.get_resume(r["id"])
                        if loaded:
                            st.session_state.resume = loaded
                            st.session_state["view_mode"] = "editor"
                            st.rerun()
        else:
            st.info("No saved resumes found in database.")
    else:  # Editor View
        col_editor, col_preview = st.columns([3, 2])
        with col_editor:
            render_editor_sections()
        with col_preview:
            render_live_preview_panel(storage)

if __name__ == "__main__":
    main()