"""ATS High-Parsability Plain Text Layout."""

from typing import List
from reportlab.platypus import Paragraph, Spacer
from templates.base_template import BaseResumeTemplate


class ATSClassicTemplate(BaseResumeTemplate):
    """Layout 4: High Parsability Single Column Plain Design."""
    def build_elements(self) -> List:
        story = []
        info = self.resume.personal_info

        story.append(Paragraph(f"<b>{info.full_name.upper()}</b>", self.styles['ResumeTitle']))
        story.append(Paragraph(f"{info.email} | {info.phone} | {info.location} | {info.linkedin}", self.styles['BodyCustom']))
        story.append(Spacer(1, 10))

        if self.resume.summary:
            story.append(Paragraph("<b>PROFESSIONAL SUMMARY</b>", self.styles['SectionHeader']))
            story.append(Paragraph(self.resume.summary, self.styles['BodyCustom']))

        if self.resume.experiences:
            story.append(Paragraph("<b>WORK EXPERIENCE</b>", self.styles['SectionHeader']))
            for exp in self.resume.experiences:
                story.append(Paragraph(f"<b>{exp.job_title}</b> - {exp.company} ({exp.start_date} - {exp.end_date})", self.styles['BodyCustom']))
                if exp.description:
                    story.append(Paragraph(exp.description, self.styles['BodyCustom']))
                for ach in exp.achievements:
                    story.append(Paragraph(f"* {ach}", self.styles['BodyCustom']))
                story.append(Spacer(1, 6))

        if self.resume.educations:
            story.append(Paragraph("<b>EDUCATION</b>", self.styles['SectionHeader']))
            for edu in self.resume.educations:
                story.append(Paragraph(f"<b>{edu.degree}</b>, {edu.institution} ({edu.start_date} - {edu.end_date})", self.styles['BodyCustom']))

        if self.resume.skill_categories:
            story.append(Paragraph("<b>TECHNICAL SKILLS</b>", self.styles['SectionHeader']))
            for cat in self.resume.skill_categories:
                story.append(Paragraph(f"<b>{cat.category_name}:</b> {', '.join(cat.skills)}", self.styles['BodyCustom']))

        return story