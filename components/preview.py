import streamlit as st
import pypdfium2 as pdfium
from services.pdf_generator import PDFGenerator
from services.storage_service import StorageService

def render_preview(storage: StorageService):
    st.subheader("👁️ Live Preview")
    resume = st.session_state.resume
    try:
        pdf_bytes = PDFGenerator.generate(resume)
        pdf_file = pdfium.PdfDocument(pdf_bytes)
        image = pdf_file[0].render(scale=2).to_pil()
        st.image(image, use_container_width=True)

        st.download_button(
            label="📥 Download Resume PDF",
            data=pdf_bytes,
            file_name=f"{resume.personal_info.full_name or 'Resume'}.pdf",
            mime="application/pdf",
            use_container_width=True
        )
        if st.button("💾 Save Resume", use_container_width=True):
            res_id = storage.save_resume(resume)
            st.success(f"Saved to database (ID: {res_id})")
    except Exception as e:
        st.error(f"Compilation error: {e}")