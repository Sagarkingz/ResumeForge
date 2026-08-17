"""5 Distinct Core PDF Layout Engines for ResumeForge."""

from typing import List
from reportlab.platypus import Paragraph, Spacer, Table, TableStyle, HRFlowable
from reportlab.lib import colors
from templates.base_template import BaseResumeTemplate


# 1. Corporate Executive Banner
class BannerExecutiveTemplate(BaseResumeTemplate):
    def build_elements(self) -> List:
        story = []
        info = self.resume.personal_info
        p_hex = self.style_config.primary_color
        p_color = self._hex_to_color(p_hex)

        banner = [
            [Paragraph(f"<font color='white' size='+10'><b>{(info.full_name or 'YOUR NAME').upper()}</b></font>", self.styles['BodyCustom'])],
            [Paragraph(f"<font color='#E5E7EB' size='+2'>{info.professional_title or ''}</font>", self.styles['BodyCustom'])],
            [Spacer(1, 4)],
            [Paragraph(f"<font color='white'>{' • '.join([c for c in [info.email, info.phone, info.location, info.linkedin] if c])}</font>", self.styles['BodyCustom'])]
        ]
        t = Table(banner, colWidths=['100%'])
        t.setStyle(TableStyle([('BACKGROUND', (0,0), (-1,-1), p_color), ('TOPPADDING', (0,0), (-1,-1), 18), ('BOTTOMPADDING', (0,0), (-1,-1), 18), ('LEFTPADDING', (0,0), (-1,-1), 18)]))
        story.append(t)
        story.append(Spacer(1, 12))

        left, right = [], []
        if self.resume.summary:
            left.append(Paragraph(f"<font color='{p_hex}' size='+2'><b>PROFILE</b></font>", self.styles['SectionHeader']))
            left.append(HRFlowable(width="100%", thickness=1.5, color=p_color, spaceAfter=6))
            left.append(Paragraph(self.resume.summary, self.styles['BodyCustom']))
            left.append(Spacer(1, 10))

        if self.resume.skill_categories:
            left.append(Paragraph(f"<font color='{p_hex}' size='+2'><b>SKILLS</b></font>", self.styles['SectionHeader']))
            left.append(HRFlowable(width="100%", thickness=1.5, color=p_color, spaceAfter=6))
            for cat in self.resume.skill_categories:
                left.append(Paragraph(f"<b>{cat.category_name}</b>", self.styles['BodyCustom']))
                left.append(Paragraph(", ".join(cat.skills), self.styles['BodyCustom']))
                left.append(Spacer(1, 4))

        if self.resume.experiences:
            right.append(Paragraph(f"<font color='{p_hex}' size='+2'><b>EXPERIENCE</b></font>", self.styles['SectionHeader']))
            right.append(HRFlowable(width="100%", thickness=1.5, color=p_color, spaceAfter=6))
            for exp in self.resume.experiences:
                right.append(Paragraph(f"<b>{exp.job_title}</b> — {exp.company}", self.styles['BodyCustom']))
                right.append(Paragraph(f"<font color='#6B7280'>{exp.start_date} - {exp.end_date}</font>", self.styles['MetaCustom']))
                if exp.description:
                    right.append(Paragraph(exp.description, self.styles['BodyCustom']))
                right.append(Spacer(1, 8))

        if self.resume.educations:
            right.append(Paragraph(f"<font color='{p_hex}' size='+2'><b>EDUCATION</b></font>", self.styles['SectionHeader']))
            right.append(HRFlowable(width="100%", thickness=1.5, color=p_color, spaceAfter=6))
            for edu in self.resume.educations:
                right.append(Paragraph(f"<b>{edu.degree}</b>, {edu.institution}", self.styles['BodyCustom']))

        grid = Table([[left, right]], colWidths=['35%', '65%'])
        grid.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('RIGHTPADDING', (0,0), (0,0), 12), ('LEFTPADDING', (1,0), (1,0), 12)]))
        story.append(grid)
        return story


# 2. Tinted Left Sidebar
class LeftSidebarTemplate(BaseResumeTemplate):
    def build_elements(self) -> List:
        story = []
        info = self.resume.personal_info
        p_hex = self.style_config.primary_color
        p_color = self._hex_to_color(p_hex)

        left = [
            Paragraph(f"<font color='white' size='+7'><b>{info.full_name}</b></font>", self.styles['BodyCustom']),
            Spacer(1, 2),
            Paragraph(f"<font color='#E5E7EB'><b>{info.professional_title}</b></font>", self.styles['BodyCustom']),
            Spacer(1, 14),
            Paragraph("<font color='white' size='+2'><b>CONTACT</b></font>", self.styles['BodyCustom']),
            HRFlowable(width="100%", thickness=1, color=colors.HexColor("#9CA3AF"), spaceAfter=8),
            Paragraph(f"<font color='white'>{info.email}<br/>{info.phone}<br/>{info.location}</font>", self.styles['BodyCustom']),
            Spacer(1, 14),
            Paragraph("<font color='white' size='+2'><b>SKILLS</b></font>", self.styles['BodyCustom']),
            HRFlowable(width="100%", thickness=1, color=colors.HexColor("#9CA3AF"), spaceAfter=8),
        ]

        for cat in self.resume.skill_categories:
            left.append(Paragraph(f"<font color='white'><b>{cat.category_name}</b></font>", self.styles['BodyCustom']))
            left.append(Paragraph(f"<font color='#F3F4F6'>" + ", ".join(cat.skills) + "</font>", self.styles['BodyCustom']))
            left.append(Spacer(1, 6))

        right = []
        if self.resume.summary:
            right.append(Paragraph(f"<font color='{p_hex}' size='+2'><b>SUMMARY</b></font>", self.styles['SectionHeader']))
            right.append(Paragraph(self.resume.summary, self.styles['BodyCustom']))
            right.append(Spacer(1, 10))

        if self.resume.experiences:
            right.append(Paragraph(f"<font color='{p_hex}' size='+2'><b>EXPERIENCE</b></font>", self.styles['SectionHeader']))
            for exp in self.resume.experiences:
                right.append(Paragraph(f"<b>{exp.job_title}</b> @ {exp.company}", self.styles['BodyCustom']))
                right.append(Paragraph(f"<font color='#6B7280'>{exp.start_date} - {exp.end_date}</font>", self.styles['MetaCustom']))
                if exp.description:
                    right.append(Paragraph(exp.description, self.styles['BodyCustom']))
                right.append(Spacer(1, 8))

        if self.resume.educations:
            right.append(Paragraph(f"<font color='{p_hex}' size='+2'><b>EDUCATION</b></font>", self.styles['SectionHeader']))
            for edu in self.resume.educations:
                right.append(Paragraph(f"<b>{edu.degree}</b> - {edu.institution}", self.styles['BodyCustom']))

        t = Table([[left, right]], colWidths=['35%', '65%'])
        t.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (0,0), p_color),
            ('VALIGN', (0,0), (-1,-1), 'TOP'),
            ('TOPPADDING', (0,0), (-1,-1), 16),
            ('BOTTOMPADDING', (0,0), (-1,-1), 20),
            ('LEFTPADDING', (0,0), (0,0), 14),
            ('RIGHTPADDING', (0,0), (0,0), 14),
            ('LEFTPADDING', (1,0), (1,0), 16),
        ]))
        story.append(t)
        return story


# 3. Centered Luxury Serif
class CenteredSerifTemplate(BaseResumeTemplate):
    def build_elements(self) -> List:
        story = []
        info = self.resume.personal_info
        p_hex = self.style_config.primary_color

        story.append(Paragraph(f"<font size='+11'><b>{info.full_name}</b></font>", self.styles['ResumeTitle']))
        story.append(Paragraph(f"<font color='{p_hex}' size='+2'><i>{info.professional_title}</i></font>", self.styles['BodyCustom']))
        story.append(Spacer(1, 4))
        story.append(HRFlowable(width="100%", thickness=1, color=colors.black, spaceAfter=6))
        
        contacts = [c for c in [info.email, info.phone, info.location, info.linkedin] if c]
        if contacts:
            story.append(Paragraph(" • ".join(contacts), self.styles['BodyCustom']))
            story.append(Spacer(1, 10))

        if self.resume.summary:
            story.append(Paragraph("<b>PROFESSIONAL STATEMENT</b>", self.styles['SectionHeader']))
            story.append(Paragraph(self.resume.summary, self.styles['BodyCustom']))
            story.append(Spacer(1, 8))

        if self.resume.experiences:
            story.append(Paragraph("<b>EXPERIENCE</b>", self.styles['SectionHeader']))
            for exp in self.resume.experiences:
                story.append(Paragraph(f"<b>{exp.job_title}</b> | {exp.company} <font color='#6B7280'>({exp.start_date} - {exp.end_date})</font>", self.styles['BodyCustom']))
                if exp.description:
                    story.append(Paragraph(exp.description, self.styles['BodyCustom']))
                story.append(Spacer(1, 6))

        if self.resume.educations:
            story.append(Paragraph("<b>EDUCATION</b>", self.styles['SectionHeader']))
            for edu in self.resume.educations:
                story.append(Paragraph(f"<b>{edu.degree}</b>, {edu.institution}", self.styles['BodyCustom']))

        return story


# 4. ATS Plain Machine-Readable
class ATSPlainTemplate(BaseResumeTemplate):
    def build_elements(self) -> List:
        story = []
        info = self.resume.personal_info

        story.append(Paragraph(f"<b>{(info.full_name or '').upper()}</b>", self.styles['ResumeTitle']))
        story.append(Paragraph(f"{info.email} | {info.phone} | {info.location} | {info.linkedin}", self.styles['BodyCustom']))
        story.append(Spacer(1, 8))

        if self.resume.summary:
            story.append(Paragraph("<b>PROFESSIONAL SUMMARY</b>", self.styles['SectionHeader']))
            story.append(Paragraph(self.resume.summary, self.styles['BodyCustom']))

        if self.resume.experiences:
            story.append(Paragraph("<b>WORK EXPERIENCE</b>", self.styles['SectionHeader']))
            for exp in self.resume.experiences:
                story.append(Paragraph(f"<b>{exp.job_title}</b> - {exp.company} ({exp.start_date} - {exp.end_date})", self.styles['BodyCustom']))
                if exp.description:
                    story.append(Paragraph(exp.description, self.styles['BodyCustom']))
                story.append(Spacer(1, 6))

        if self.resume.educations:
            story.append(Paragraph("<b>EDUCATION</b>", self.styles['SectionHeader']))
            for edu in self.resume.educations:
                story.append(Paragraph(f"<b>{edu.degree}</b>, {edu.institution} ({edu.start_date} - {edu.end_date})", self.styles['BodyCustom']))

        return story


# 5. Right Sidebar Metadata Panel
class RightSidebarTemplate(BaseResumeTemplate):
    def build_elements(self) -> List:
        story = []
        info = self.resume.personal_info
        p_hex = self.style_config.primary_color

        story.append(Paragraph(f"<font color='{p_hex}' size='+10'><b>{info.full_name}</b></font>", self.styles['ResumeTitle']))
        story.append(Paragraph(f"<b>{info.professional_title}</b>", self.styles['BodyCustom']))
        story.append(HRFlowable(width="100%", thickness=1.5, color=self._hex_to_color(p_hex), spaceAfter=10))

        main_left = []
        if self.resume.summary:
            main_left.append(Paragraph(f"<font color='{p_hex}'><b>SUMMARY</b></font>", self.styles['SectionHeader']))
            main_left.append(Paragraph(self.resume.summary, self.styles['BodyCustom']))
            main_left.append(Spacer(1, 8))

        if self.resume.experiences:
            main_left.append(Paragraph(f"<font color='{p_hex}'><b>EXPERIENCE</b></font>", self.styles['SectionHeader']))
            for exp in self.resume.experiences:
                main_left.append(Paragraph(f"<b>{exp.job_title}</b> — {exp.company}", self.styles['BodyCustom']))
                main_left.append(Paragraph(f"<font color='#6B7280'>{exp.start_date} - {exp.end_date}</font>", self.styles['MetaCustom']))
                if exp.description:
                    main_left.append(Paragraph(exp.description, self.styles['BodyCustom']))
                main_left.append(Spacer(1, 6))

        side_right = [
            Paragraph(f"<font color='{p_hex}'><b>CONTACT</b></font>", self.styles['SectionHeader']),
            Paragraph(f"{info.email}<br/>{info.phone}<br/>{info.location}", self.styles['BodyCustom']),
            Spacer(1, 10),
            Paragraph(f"<font color='{p_hex}'><b>EDUCATION</b></font>", self.styles['SectionHeader']),
        ]
        for edu in self.resume.educations:
            side_right.append(Paragraph(f"<b>{edu.degree}</b><br/>{edu.institution}", self.styles['BodyCustom']))
            side_right.append(Spacer(1, 4))

        t = Table([[main_left, side_right]], colWidths=['65%', '35%'])
        t.setStyle(TableStyle([
            ('VALIGN', (0,0), (-1,-1), 'TOP'),
            ('RIGHTPADDING', (0,0), (0,0), 12),
            ('BACKGROUND', (1,0), (1,0), colors.HexColor("#F3F4F6")),
            ('LEFTPADDING', (1,0), (1,0), 10),
            ('TOPPADDING', (1,0), (1,0), 10),
            ('BOTTOMPADDING', (1,0), (1,0), 10),
        ]))
        story.append(t)
        return story