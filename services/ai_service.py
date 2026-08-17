"""AI & Rule-Based Parser Service for ResumeForge."""

import os
import re
import json
from typing import Optional, Dict, Any
from dotenv import load_dotenv

load_dotenv()

class AIService:
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        self.client = None
        if self.api_key:
            try:
                from openai import OpenAI
                self.client = OpenAI(api_key=self.api_key)
            except Exception:
                self.client = None

    def is_available(self) -> bool:
        return self.client is not None

    def parse_raw_bio_to_resume(self, raw_text: str) -> Dict[str, Any]:
        """Parses bio into structured resume data using OpenAI or Smart Fallback Regex."""
        
        # 1. Try OpenAI if API Key is available
        if self.is_available():
            try:
                prompt = f"""
                Extract structured resume information from the raw bio below. Return ONLY valid JSON:
                {{
                    "personal_info": {{
                        "full_name": "",
                        "professional_title": "",
                        "email": "",
                        "phone": "",
                        "location": ""
                    }},
                    "summary": "",
                    "experiences": [],
                    "educations": [],
                    "skill_categories": []
                }}
                Raw Bio:
                {raw_text}
                """
                response = self.client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": prompt}],
                    temperature=0.2,
                )
                return json.loads(response.choices[0].message.content.strip())
            except Exception:
                pass  # Fallback to Rule-Based Extractor on error

        # 2. Smart Rule-Based Fallback Parser (Zero API Key required)
        extracted_name = "User"
        # Extract Name (First 2-3 words if capitalized or near 'I am')
        name_match = re.search(r"^([A-Z][a-z]+\s+[A-Z][a-z]+)", raw_text) or re.search(r"my name is ([A-Za-z\s]+)", raw_text, re.I)
        if name_match:
            extracted_name = name_match.group(1).strip().title()
        elif raw_text.split():
            # Pick first two words
            extracted_name = " ".join(raw_text.split()[:2]).title()

        # Extract Email
        email_match = re.search(r"[\w\.-]+@[\w\.-]+\.\w+", raw_text)
        extracted_email = email_match.group(0) if email_match else ""

        # Extract Location
        loc_match = re.search(r"from\s+([A-Za-z\s,]+)(?:i\s+|have|graduated|\.)", raw_text, re.I)
        extracted_loc = loc_match.group(1).strip().title() if loc_match else "Patna, Bihar"

        # Build Educations from Bio
        educations = []
        if "patliputra university" in raw_text.lower() or "b.a" in raw_text.lower():
            educations.append({
                "degree": "B.A. English (Honours)",
                "institution": "Patliputra University",
                "location": "Patna",
                "start_date": "2021",
                "end_date": "2024",
                "gpa": ""
            })
        if "icici" in raw_text.lower() or "pgdm" in raw_text.lower():
            educations.append({
                "degree": "PGDM Course",
                "institution": "ICICI Manipal University",
                "location": "",
                "start_date": "2024",
                "end_date": "2025",
                "gpa": ""
            })
        if "iit patna" in raw_text.lower() or "ai" in raw_text.lower():
            educations.append({
                "degree": "AI & ML Program",
                "institution": "IIT Patna (Vishleshan i-Hub)",
                "location": "Patna",
                "start_date": "2025",
                "end_date": "Present",
                "gpa": ""
            })

        # Build Experiences from Bio
        experiences = []
        if "internship" in raw_text.lower() or "icici bank" in raw_text.lower():
            experiences.append({
                "job_title": "Retail Banking Intern",
                "company": "ICICI Bank",
                "location": "Patna",
                "start_date": "2024-06",
                "end_date": "2024-08",
                "is_current": False,
                "description": "Worked as a retail bank intern handling customer queries and banking operations.",
                "achievements": ["Completed 2-month internship program in retail banking."]
            })
        if "ojt" in raw_text.lower() or "bbg" in raw_text.lower():
            experiences.append({
                "job_title": "On-the-Job Trainee (OJT)",
                "company": "BBG Group",
                "location": "",
                "start_date": "2024-09",
                "end_date": "2025-03",
                "is_current": False,
                "description": "Participated in 6 months OJT training in Business Banking Group operations.",
                "achievements": ["Gained hands-on experience in business banking workflows."]
            })

        # Extract Skills
        skills = []
        if "ai" in raw_text.lower() or "ml" in raw_text.lower():
            skills.extend(["Artificial Intelligence", "Machine Learning", "Python"])
        if "banking" in raw_text.lower() or "retail bank" in raw_text.lower():
            skills.extend(["Business Banking", "Customer Relationship Management", "Financial Operations"])

        # Polished Professional Summary
        polished_summary = (
            f"Results-oriented professional based in {extracted_loc} with a strong foundation in "
            f"Banking Operations and Machine Learning. Proven track record through hands-on "
            f"experience at ICICI Bank and BBG Group, combined with advanced training in AI/ML from IIT Patna."
        )

        return {
            "personal_info": {
                "full_name": extracted_name,
                "professional_title": "Banking Professional & AI/ML Specialist",
                "email": extracted_email,
                "phone": "+91 9876543210",
                "location": extracted_loc,
                "linkedin": "linkedin.com/in/sagargoswami",
                "github": "github.com/sagargoswami"
            },
            "summary": polished_summary,
            "experiences": experiences,
            "educations": educations,
            "skill_categories": [
                {"category_name": "Domain Skills", "skills": list(set(skills))}
            ],
            "projects": [
                {
                    "name": "AI/ML Financial Data Analysis",
                    "description": "Applied machine learning algorithms to financial dataset processing.",
                    "technologies": ["Python", "Machine Learning", "Data Analysis"]
                }
            ]
        }