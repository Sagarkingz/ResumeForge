"""Full Height Tinted Sidebar Templates."""

from typing import List
from reportlab.platypus import Paragraph, Spacer, Table, TableStyle, HRFlowable
from reportlab.lib import colors
from templates.base_template import BaseResumeTemplate


class CreativeSidebarTemplate(BaseResumeTemplate):
    """Layout 3: Full-Page Colored Left Sidebar with White Text."""
    def build_elements(self) -> List:
        story = []
        info = self.resume.personal_info
        p_hex = self.style_config.primary_color
        p_color = self._hex_to_color(p_hex)

        left_items = [
            Paragraph(f"<font color='white' size='+7'><b>{info.full_name}</b></font>", self.styles['BodyCustom']),
            Spacer(1, 2),
            Paragraph(f"<font color='#E5E7EB'><b>{info.professional_title}</b></font>", self.styles['BodyCustom']),
            Spacer(1, 14),
            Paragraph("<font color='white' size='+2'><b>CONTACT</b></font>", self.styles['BodyCustom']),
            HRFlowable(width="100%", thickness=1, color=colors.HexColor("#9CA3AF"), spaceAfter=8),
            Paragraph(f"<font color='white'><b>Email:</b><br/>{info.email}</font>", self.styles['BodyCustom']),
            Spacer(1, 4),
            Paragraph(f"<font color='white'><b>Phone:</b><br/>{info.phone}</font>", self.styles['BodyCustom']),
            Spacer(1, 4),
            Paragraph(f"<font color='white'><b>Location:</b><br/>{info.location}</font>", self.styles['BodyCustom']),
            Spacer(1, 14),
            Paragraph("<font color='white' size='+2'><b>SKILLS</b></font>", self.styles['BodyCustom']),
            HRFlowable(width="100%", thickness=1, color=colors.HexColor("#9CA3AF"), spaceAfter=8),
        ]

        for cat in self.resume.skill_categories:
            left_items.append(Paragraph(f"<font color='white'><b>{cat.category_name}</b></font>", self.styles['BodyCustom']))
            left_items.append(Paragraph(f"<font color='#F3F4F6'>" + ", ".join(cat.skills) + "</font>", self.styles['BodyCustom']))
            left_items.append(Spacer(1, 6))

        right_items = []
        if self.resume.summary:
            right_items.append(Paragraph(f"<font color='{p_hex}' size='+2'><b>PROFILE SUMMARY</b></font>", self.styles['SectionHeader']))
            right_items.append(Paragraph(self.resume.summary, self.styles['BodyCustom']))
            right_items.append(Spacer(1, 10))

        if self.resume.experiences:
            right_items.append(Paragraph(f"<font color='{p_hex}' size='+2'><b>EXPERIENCE</b></font>", self.styles['SectionHeader']))
            for exp in self.resume.experiences:
                right_items.append(Paragraph(f"<b>{exp.job_title}</b> @ {exp.company}", self.styles['BodyCustom']))
                right_items.append(Paragraph(f"<font color='#6B7280'>{exp.start_date} - {exp.end_date}</font>", self.styles['MetaCustom']))
                if exp.description:
                    right_items.append(Paragraph(exp.description, self.styles['BodyCustom']))
                for ach in exp.achievements:
                    right_items.append(Paragraph(f"• {ach}", self.styles['BodyCustom']))
                right_items.append(Spacer(1, 8))

        if self.resume.educations:
            right_items.append(Paragraph(f"<font color='{p_hex}' size='+2'><b>EDUCATION</b></font>", self.styles['SectionHeader']))
            for edu in self.resume.educations:
                right_items.append(Paragraph(f"<b>{edu.degree}</b> - {edu.institution}", self.styles['BodyCustom']))

        table = Table([[left_items, right_items]], colWidths=['35%', '65%'])
        table.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (0,0), p_color),
            ('VALIGN', (0,0), (-1,-1), 'TOP'),
            ('TOPPADDING', (0,0), (-1,-1), 16),
            ('BOTTOMPADDING', (0,0), (-1,-1), 20),
            ('LEFTPADDING', (0,0), (0,0), 14),
            ('RIGHTPADDING', (0,0), (0,0), 14),
            ('LEFTPADDING', (1,0), (1,0), 16),
        ]))
        story.append(table)
        return story