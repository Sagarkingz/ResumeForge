"""Live A4 PDF Preview Panel with integrated Template & Color Picker."""

import streamlit as st
import pypdfium2 as pdfium
from services.pdf_generator import PDFGenerator
from services.scoring_service import ScoringService
from services.storage_service import StorageService
from config.settings import TEMPLATE_METADATA, COLOR_PALETTES, FONT_OPTIONS


def render_live_preview_panel(storage: StorageService):
    st.subheader("👁️ Live A4 Preview & Templates")
    resume = st.session_state.resume

    # Score Meter Badge
    score_data = ScoringService.evaluate(resume)
    st.progress(score_data["completeness_pct"] / 100.0)
    st.caption(f"**Quality Score:** {score_data['score']}/100 ({score_data['completeness_pct']}% Complete)")

    # 🎨 In-Line Template & Styling Switcher Panel
    with st.expander("🎨 Choose Template & Style (Live Update)", expanded=True):
        t1, t2, t3 = st.columns(3)
        
        with t1:
            template_options = {tid: meta["name"] for tid, meta in TEMPLATE_METADATA.items()}
            selected_tid = st.selectbox(
                "Template Design",
                options=list(template_options.keys()),
                format_func=lambda x: template_options[x],
                index=0
            )
            resume.style.template_id = selected_tid

        with t2:
            palette_choice = st.selectbox("Color Palette", list(COLOR_PALETTES.keys()), index=0)
            resume.style.primary_color = COLOR_PALETTES[palette_choice]["primary"]

        with t3:
            font_choice = st.selectbox("Font Style", FONT_OPTIONS, index=0)
            resume.style.font_family = font_choice

    # Zoom Controls
    if "zoom_scale" not in st.session_state:
        st.session_state["zoom_scale"] = 2.0

    z1, z2, z3 = st.columns([1, 1, 2])
    with z1:
        if st.button("🔍 Zoom In"):
            st.session_state["zoom_scale"] = min(st.session_state["zoom_scale"] + 0.5, 4.0)
            st.rerun()
    with z2:
        if st.button("🔍 Zoom Out"):
            st.session_state["zoom_scale"] = max(st.session_state["zoom_scale"] - 0.5, 1.0)
            st.rerun()

    # Generate PDF and Render Preview
    try:
        pdf_bytes = PDFGenerator.generate(resume)
        pdf_file = pdfium.PdfDocument(pdf_bytes)
        
        page = pdf_file[0]
        image = page.render(scale=st.session_state["zoom_scale"]).to_pil()
        st.image(image, use_container_width=True)

        st.download_button(
            label="📥 Download PDF Resume",
            data=pdf_bytes,
            file_name=f"{resume.personal_info.full_name or 'Resume'}.pdf",
            mime="application/pdf",
            use_container_width=True
        )

        if st.button("💾 Save Resume Locally", use_container_width=True):
            res_id = storage.save_resume(resume)
            st.success(f"Saved resume to database! (ID: {res_id})")

    except Exception as e:
        st.error(f"PDF Compilation Error: {str(e)}")