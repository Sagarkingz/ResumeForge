"""Granular scoring engine with actionable suggestions and progress tracking."""

from typing import Dict, List, Any
from models.resume_model import ResumeData

class ScoringService:
    @staticmethod
    def evaluate(resume: ResumeData) -> Dict[str, Any]:
        score = 0
        total_items = 8
        completed_items = 0
        checks: List[Dict[str, Any]] = []

        # 1. Contact Completeness
        info = resume.personal_info
        contact_complete = bool(info.full_name and info.email and info.phone and info.location)
        if contact_complete:
            score += 15
            completed_items += 1
            checks.append({"status": "pass", "label": "Contact Information Complete"})
        else:
            checks.append({"status": "warn", "label": "Missing Contact Info (Email/Phone/Location)"})

        # 2. LinkedIn / Links
        if info.linkedin or info.github or info.portfolio:
            score += 10
            completed_items += 1
            checks.append({"status": "pass", "label": "Online Portfolio / LinkedIn Added"})
        else:
            checks.append({"status": "warn", "label": "Add LinkedIn or Portfolio Link"})

        # 3. Professional Summary
        words = len(resume.summary.split())
        if 25 <= words <= 90:
            score += 15
            completed_items += 1
            checks.append({"status": "pass", "label": "Strong Professional Summary"})
        elif words > 0:
            score += 8
            checks.append({"status": "info", "label": "Expand Summary to 30-60 words"})
        else:
            checks.append({"status": "fail", "label": "Missing Professional Summary"})

        # 4. Work Experience
        if len(resume.experiences) > 0:
            score += 20
            completed_items += 1
            checks.append({"status": "pass", "label": f"{len(resume.experiences)} Work Experience Entry(ies)"})
        else:
            checks.append({"status": "fail", "label": "No Work Experience Entries"})

        # 5. Education
        if len(resume.educations) > 0:
            score += 15
            completed_items += 1
            checks.append({"status": "pass", "label": "Education Listed"})
        else:
            checks.append({"status": "fail", "label": "Missing Education"})

        # 6. Skills
        total_skills = sum(len(cat.skills) for cat in resume.skill_categories)
        if total_skills >= 5:
            score += 10
            completed_items += 1
            checks.append({"status": "pass", "label": f"{total_skills} Skills Categorized"})
        else:
            checks.append({"status": "warn", "label": "Add at least 5 key skills"})

        # 7. Projects
        if len(resume.projects) > 0:
            score += 10
            completed_items += 1
            checks.append({"status": "pass", "label": f"{len(resume.projects)} Project(s) Featured"})
        else:
            checks.append({"status": "info", "label": "Add Projects to strengthen resume"})

        # 8. Certifications / Languages
        if len(resume.certifications) > 0 or len(resume.languages) > 0:
            score += 5
            completed_items += 1
            checks.append({"status": "pass", "label": "Certifications / Languages Included"})
        else:
            checks.append({"status": "info", "label": "Add Certifications or Languages"})

        completeness_pct = int((completed_items / total_items) * 100)

        return {
            "score": min(score, 100),
            "completeness_pct": completeness_pct,
            "checks": checks
        }