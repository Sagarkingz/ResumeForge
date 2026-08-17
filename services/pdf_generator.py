from models.resume_model import ResumeData
from templates import get_template

class PDFGenerator:
    @staticmethod
    def generate(resume: ResumeData) -> bytes:
        template_cls = get_template(resume.style.template_id)
        renderer = template_cls(resume)
        return renderer.render_pdf()