"""High-Impact Canva-Inspired Templates for ResumeForge."""

from typing import List
from reportlab.platypus import Paragraph, Spacer, Table, TableStyle, HRFlowable
from reportlab.lib import colors
from templates.base_template import BaseResumeTemplate


class CreativeSidebarTemplate(BaseResumeTemplate):
    """Canva Split Two-Column: Full Colored Left Sidebar + Clean Right Main Body."""
    def build_elements(self) -> List:
        story = []
        info = self.resume.personal_info
        p_hex = self.style_config.primary_color
        p_color = self._hex_to_color(p_hex)

        # Left Column: Profile, Contacts, Skills, Education
        left_items = [
            Paragraph(f"<font color='white' size='+6'><b>{info.full_name}</b></font>", self.styles['BodyCustom']),
            Spacer(1, 4),
            Paragraph(f"<font color='#E5E7EB' size='+1'><b>{info.professional_title}</b></font>", self.styles['BodyCustom']),
            Spacer(1, 16),
            Paragraph("<font color='white' size='+2'><b>CONTACT</b></font>", self.styles['BodyCustom']),
            HRFlowable(width="100%", thickness=1, color=colors.HexColor("#9CA3AF"), spaceAfter=10),
            Paragraph(f"<font color='white'><b>Email:</b><br/>{info.email}</font>", self.styles['BodyCustom']),
            Spacer(1, 6),
            Paragraph(f"<font color='white'><b>Phone:</b><br/>{info.phone}</font>", self.styles['BodyCustom']),
            Spacer(1, 6),
            Paragraph(f"<font color='white'><b>Location:</b><br/>{info.location}</font>", self.styles['BodyCustom']),
            Spacer(1, 6),
            Paragraph(f"<font color='white'><b>LinkedIn:</b><br/>{info.linkedin}</font>", self.styles['BodyCustom']),
            Spacer(1, 20),
            Paragraph("<font color='white' size='+2'><b>CORE SKILLS</b></font>", self.styles['BodyCustom']),
            HRFlowable(width="100%", thickness=1, color=colors.HexColor("#9CA3AF"), spaceAfter=10),
        ]

        for cat in self.resume.skill_categories:
            left_items.append(Paragraph(f"<font color='white'><b>{cat.category_name}</b></font>", self.styles['BodyCustom']))
            left_items.append(Paragraph(f"<font color='#F3F4F6'>" + ", ".join(cat.skills) + "</font>", self.styles['BodyCustom']))
            left_items.append(Spacer(1, 8))

        if self.resume.educations:
            left_items.append(Spacer(1, 10))
            left_items.append(Paragraph("<font color='white' size='+2'><b>EDUCATION</b></font>", self.styles['BodyCustom']))
            left_items.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#9CA3AF"), spaceAfter=10))
            for edu in self.resume.educations:
                left_items.append(Paragraph(f"<font color='white'><b>{edu.degree}</b></font>", self.styles['BodyCustom']))
                left_items.append(Paragraph(f"<font color='#E5E7EB'>{edu.institution}</font>", self.styles['MetaCustom']))
                left_items.append(Spacer(1, 6))

        # Right Column: Profile Summary & Work Experience
        right_items = []
        if self.resume.summary:
            right_items.append(Paragraph(f"<font color='{p_hex}' size='+3'><b>PROFILE SUMMARY</b></font>", self.styles['SectionHeader']))
            right_items.append(Paragraph(self.resume.summary, self.styles['BodyCustom']))
            right_items.append(Spacer(1, 14))

        if self.resume.experiences:
            right_items.append(Paragraph(f"<font color='{p_hex}' size='+3'><b>WORK EXPERIENCE</b></font>", self.styles['SectionHeader']))
            for exp in self.resume.experiences:
                right_items.append(Paragraph(f"<font size='+2'><b>{exp.job_title}</b></font>", self.styles['BodyCustom']))
                right_items.append(Paragraph(f"<font color='#4B5563'><b>{exp.company}</b> | {exp.start_date} - {'Present' if exp.is_current else exp.end_date}</font>", self.styles['MetaCustom']))
                right_items.append(Spacer(1, 4))
                if exp.description:
                    right_items.append(Paragraph(exp.description, self.styles['BodyCustom']))
                for ach in exp.achievements:
                    right_items.append(Paragraph(f"• {ach}", self.styles['BodyCustom']))
                right_items.append(Spacer(1, 12))

        # Side-by-side Table layout
        table = Table([[left_items, right_items]], colWidths=['35%', '65%'])
        table.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (0,0), p_color),
            ('VALIGN', (0,0), (-1,-1), 'TOP'),
            ('TOPPADDING', (0,0), (0,0), 20),
            ('BOTTOMPADDING', (0,0), (0,0), 40),
            ('LEFTPADDING', (0,0), (0,0), 16),
            ('RIGHTPADDING', (0,0), (0,0), 16),
            ('TOPPADDING', (1,0), (1,0), 20),
            ('LEFTPADDING', (1,0), (1,0), 20),
            ('RIGHTPADDING', (1,0), (1,0), 12),
        ]))
        story.append(table)
        return story


class ExecutiveBannerTemplate(BaseResumeTemplate):
    """Canva Executive: Dark Top Header Banner + Card Sections."""
    def build_elements(self) -> List:
        story = []
        info = self.resume.personal_info
        p_hex = self.style_config.primary_color
        p_color = self._hex_to_color(p_hex)

        banner = [
            [Paragraph(f"<font color='white' size='+10'><b>{info.full_name.upper()}</b></font>", self.styles['BodyCustom'])],
            [Paragraph(f"<font color='#E5E7EB' size='+2'>{info.professional_title}</font>", self.styles['BodyCustom'])],
            [Spacer(1, 8)],
            [Paragraph(f"<font color='white'>{'  •  '.join([c for c in [info.email, info.phone, info.location, info.linkedin] if c])}</font>", self.styles['BodyCustom'])]
        ]
        t_banner = Table(banner, colWidths=['100%'])
        t_banner.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,-1), p_color),
            ('TOPPADDING', (0,0), (-1,-1), 22),
            ('BOTTOMPADDING', (0,0), (-1,-1), 22),
            ('LEFTPADDING', (0,0), (-1,-1), 20),
        ]))
        story.append(t_banner)
        story.append(Spacer(1, 16))

        if self.resume.summary:
            story.append(Paragraph(f"<font color='{p_hex}' size='+2'><b>EXECUTIVE PROFILE</b></font>", self.styles['SectionHeader']))
            story.append(HRFlowable(width="100%", thickness=1.5, color=p_color, spaceAfter=8))
            story.append(Paragraph(self.resume.summary, self.styles['BodyCustom']))
            story.append(Spacer(1, 14))

        if self.resume.experiences:
            story.append(Paragraph(f"<font color='{p_hex}' size='+2'><b>CAREER HISTORY</b></font>", self.styles['SectionHeader']))
            story.append(HRFlowable(width="100%", thickness=1.5, color=p_color, spaceAfter=8))
            for exp in self.resume.experiences:
                story.append(Paragraph(f"<font size='+2'><b>{exp.job_title}</b></font> — <font color='#374151'><b>{exp.company}</b></font> <font color='#6B7280'>({exp.start_date} - {'Present' if exp.is_current else exp.end_date})</font>", self.styles['BodyCustom']))
                if exp.description:
                    story.append(Paragraph(exp.description, self.styles['BodyCustom']))
                for ach in exp.achievements:
                    story.append(Paragraph(f"• {ach}", self.styles['BodyCustom']))
                story.append(Spacer(1, 10))

        if self.resume.skill_categories:
            story.append(Paragraph(f"<font color='{p_hex}' size='+2'><b>TECHNICAL SKILLS</b></font>", self.styles['SectionHeader']))
            story.append(HRFlowable(width="100%", thickness=1.5, color=p_color, spaceAfter=8))
            for cat in self.resume.skill_categories:
                story.append(Paragraph(f"<b>{cat.category_name}:</b> {', '.join(cat.skills)}", self.styles['BodyCustom']))

        return story


class ModernTemplate(BaseResumeTemplate):
    """Canva Modern: Bold Side Accents and Clean Spacing."""
    def build_elements(self) -> List:
        story = []
        info = self.resume.personal_info
        p_hex = self.style_config.primary_color
        p_color = self._hex_to_color(p_hex)

        story.append(Paragraph(f"<font color='{p_hex}' size='+11'><b>{info.full_name}</b></font>", self.styles['ResumeTitle']))
        story.append(Paragraph(f"<font color='#4B5563' size='+2'><b>{info.professional_title}</b></font>", self.styles['BodyCustom']))
        story.append(Spacer(1, 6))

        contacts = [c for c in [info.email, info.phone, info.location, info.linkedin] if c]
        if contacts:
            story.append(Paragraph(" <font color='#9CA3AF'>|</font> ".join(contacts), self.styles['BodyCustom']))
            story.append(Spacer(1, 8))

        story.append(HRFlowable(width="100%", thickness=2.5, color=p_color, spaceAfter=16))

        if self.resume.summary:
            story.append(Paragraph(f"<font color='{p_hex}' size='+2'><b>ABOUT ME</b></font>", self.styles['SectionHeader']))
            story.append(Paragraph(self.resume.summary, self.styles['BodyCustom']))
            story.append(Spacer(1, 12))

        if self.resume.experiences:
            story.append(Paragraph(f"<font color='{p_hex}' size='+2'><b>EXPERIENCE</b></font>", self.styles['SectionHeader']))
            for exp in self.resume.experiences:
                t_data = [
                    [Paragraph(f"<font size='+1'><b>{exp.job_title}</b></font> <font color='#4B5563'>| {exp.company}</font>", self.styles['BodyCustom']),
                     Paragraph(f"<font color='#6B7280'><b>{exp.start_date} - {'Present' if exp.is_current else exp.end_date}</b></font>", self.styles['BodyCustom'])]
                ]
                t = Table(t_data, colWidths=['70%', '30%'])
                t.setStyle(TableStyle([('ALIGN', (1,0), (1,0), 'RIGHT'), ('LEFTPADDING', (0,0), (-1,-1), 0)]))
                story.append(t)
                if exp.description:
                    story.append(Paragraph(exp.description, self.styles['BodyCustom']))
                for ach in exp.achievements:
                    story.append(Paragraph(f"• {ach}", self.styles['BodyCustom']))
                story.append(Spacer(1, 10))

        if self.resume.skill_categories:
            story.append(Paragraph(f"<font color='{p_hex}' size='+2'><b>SKILLS & EXPERTISE</b></font>", self.styles['SectionHeader']))
            for cat in self.resume.skill_categories:
                story.append(Paragraph(f"<b>{cat.category_name}:</b> " + ", ".join(cat.skills), self.styles['BodyCustom']))

        return story


class ElegantSerifTemplate(BaseResumeTemplate):
    """Canva Elegant: Centered Luxury Layout."""
    def build_elements(self) -> List:
        story = []
        info = self.resume.personal_info
        p_hex = self.style_config.primary_color

        story.append(Paragraph(f"<font size='+11'><b>{info.full_name}</b></font>", self.styles['ResumeTitle']))
        story.append(Paragraph(f"<font color='{p_hex}' size='+2'><i>{info.professional_title}</i></font>", self.styles['BodyCustom']))
        story.append(Spacer(1, 6))
        story.append(HRFlowable(width="100%", thickness=1, color=colors.black, spaceAfter=8))

        contacts = [c for c in [info.email, info.phone, info.location, info.linkedin] if c]
        if contacts:
            story.append(Paragraph(" • ".join(contacts), self.styles['BodyCustom']))
            story.append(Spacer(1, 14))

        if self.resume.summary:
            story.append(Paragraph("<b>PROFESSIONAL STATEMENT</b>", self.styles['SectionHeader']))
            story.append(Paragraph(self.resume.summary, self.styles['BodyCustom']))
            story.append(Spacer(1, 12))

        if self.resume.experiences:
            story.append(Paragraph("<b>PROFESSIONAL EXPERIENCE</b>", self.styles['SectionHeader']))
            for exp in self.resume.experiences:
                story.append(Paragraph(f"<b>{exp.job_title}</b> | {exp.company} <font color='#6B7280'>({exp.start_date} - {exp.end_date})</font>", self.styles['BodyCustom']))
                if exp.description:
                    story.append(Paragraph(exp.description, self.styles['BodyCustom']))
                for ach in exp.achievements:
                    story.append(Paragraph(f"• {ach}", self.styles['BodyCustom']))
                story.append(Spacer(1, 10))

        return story


class MinimalistGridTemplate(ModernTemplate):
    pass

class ATSSimpleTemplate(ModernTemplate):
    pass

class VibrantAccentTemplate(ExecutiveBannerTemplate):
    pass

class ClassicCorporateTemplate(ModernTemplate):
    pass