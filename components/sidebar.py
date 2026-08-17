import streamlit as st
from services.storage_service import StorageService
from services.scoring_service import ScoringService
from config.settings import COLOR_PALETTES
from models.resume_model import get_demo_resume

# All 8 Canva-Inspired Rich Templates
TEMPLATE_OPTIONS = {
    "✨ Canva Modern Accent": "canva_modern",
    "🎨 Canva Split Sidebar (Two-Column)": "canva_sidebar",
    "💼 Canva Executive Banner": "canva_executive",
    "🏛️ Canva Elegant Serif": "canva_elegant",
    "🌿 Canva Minimalist Grid": "canva_minimal",
    "🎯 ATS Friendly (100% Machine Readable)": "ats_simple",
    "🔥 Canva Vibrant Highlight": "canva_vibrant",
    "📊 Canva Corporate Standard": "canva_corporate",
}

def render_sidebar(storage: StorageService):
    with st.sidebar:
        st.title("🛠️ ResumeForge")
        
        if st.button("🚀 Load Demo Data", use_container_width=True):
            st.session_state.resume = get_demo_resume()
            st.rerun()

        st.divider()

        # Score Metric
        if "resume" in st.session_state:
            score_data = ScoringService.evaluate(st.session_state.resume)
            st.metric("Quality Score", f"{score_data['score']}/100")
            with st.expander("Feedback & Suggestions"):
                for item in score_data["feedback"]:
                    st.info(f"**{item['category']}**: {item['message']}")

        st.divider()
        st.subheader("🎨 Canva Templates & Themes")

        # Template Selection Dropdown with 8 Rich Designs
        selected_template_name = st.selectbox(
            "Choose Resume Template", 
            list(TEMPLATE_OPTIONS.keys()),
            index=0
        )
        if "resume" in st.session_state:
            st.session_state.resume.style.template_id = TEMPLATE_OPTIONS[selected_template_name]

        # Color Palette Dropdown
        palette_choice = st.selectbox("Color Theme", list(COLOR_PALETTES.keys()))
        if "resume" in st.session_state:
            st.session_state.resume.style.primary_color = COLOR_PALETTES[palette_choice]["primary"]