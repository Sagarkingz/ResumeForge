"""Base template engine supporting dynamic layout geometry and visual badges."""

from abc import ABC, abstractmethod
import io
from typing import List, Any
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from models.resume_model import ResumeData

class BaseResumeTemplate(ABC):
    def __init__(self, resume: ResumeData):
        self.resume = resume
        self.style_config = resume.style
        self.styles = getSampleStyleSheet()
        self._setup_custom_styles()

    def _hex_to_color(self, hex_code: str) -> colors.Color:
        try:
            return colors.HexColor(hex_code)
        except Exception:
            return colors.HexColor("#1E3A8A")

    def _setup_custom_styles(self):
        primary = self._hex_to_color(self.style_config.primary_color)
        font = self.style_config.font_family

        self.styles.add(ParagraphStyle(
            'ResumeTitle',
            fontName=f"{font}-Bold",
            fontSize=22,
            leading=26,
            textColor=primary,
            spaceAfter=4
        ))

        self.styles.add(ParagraphStyle(
            'ResumeSubtitle',
            fontName=f"{font}-Bold",
            fontSize=12,
            leading=16,
            textColor=colors.HexColor("#4B5563"),
            spaceAfter=8
        ))

        self.styles.add(ParagraphStyle(
            'SectionHeader',
            fontName=f"{font}-Bold",
            fontSize=13,
            leading=17,
            textColor=primary,
            spaceBefore=10,
            spaceAfter=6,
            keepWithNext=True
        ))

        self.styles.add(ParagraphStyle(
            'BodyCustom',
            fontName=font,
            fontSize=9.5,
            leading=13.5,
            textColor=colors.HexColor("#1F2937"),
            spaceAfter=4
        ))

        self.styles.add(ParagraphStyle(
            'MetaCustom',
            fontName=f"{font}-Oblique",
            fontSize=8.5,
            leading=11.5,
            textColor=colors.HexColor("#6B7280")
        ))

    @abstractmethod
    def build_elements(self) -> List[Any]:
        pass

    def render_pdf(self) -> bytes:
        buffer = io.BytesIO()
        margin = self.style_config.margin_mm * 2.83465  # mm to points
        doc = SimpleDocTemplate(
            buffer,
            pagesize=letter,
            leftMargin=margin,
            rightMargin=margin,
            topMargin=margin,
            bottomMargin=margin
        )
        elements = self.build_elements()
        doc.build(elements)
        buffer.seek(0)
        return buffer.getvalue()