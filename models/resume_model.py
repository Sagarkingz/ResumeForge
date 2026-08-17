"""Data models for ResumeForge."""

from dataclasses import dataclass, field, asdict
from typing import List, Optional, Dict, Any
import json

@dataclass
class PersonalInfo:
    full_name: str = ""
    professional_title: str = ""
    email: str = ""
    phone: str = ""
    location: str = ""
    linkedin: str = ""
    github: str = ""
    portfolio: str = ""
    website: str = ""
    photo_b64: Optional[str] = None
    date_of_birth: str = ""
    nationality: str = ""
    career_level: str = "Mid-Level"  # Fresher, Entry, Mid-Level, Senior, Executive
    open_to_relocation: bool = False

@dataclass
class Experience:
    job_title: str = ""
    company: str = ""
    location: str = ""
    start_date: str = ""
    end_date: str = ""
    is_current: bool = False
    description: str = ""
    achievements: List[str] = field(default_factory=list)

@dataclass
class Education:
    degree: str = ""
    institution: str = ""
    location: str = ""
    start_date: str = ""
    end_date: str = ""
    gpa: str = ""
    description: str = ""

@dataclass
class SkillCategory:
    category_name: str = "Technical Skills"
    skills: List[str] = field(default_factory=list)

@dataclass
class Project:
    name: str = ""
    description: str = ""
    technologies: List[str] = field(default_factory=list)
    project_url: str = ""
    github_url: str = ""

@dataclass
class Certification:
    name: str = ""
    issuing_organization: str = ""
    date: str = ""
    credential_url: str = ""

@dataclass
class Language:
    language: str = ""
    proficiency: str = "Professional"  # Native, Professional, Intermediate, Basic

@dataclass
class StyleConfig:
    template_id: str = "modern_accent"
    primary_color: str = "#1E3A8A"
    secondary_color: str = "#3B82F6"
    text_color: str = "#1F2937"
    font_family: str = "Helvetica"
    font_size: int = 10
    margin_mm: int = 12
    show_photo: bool = False
    length_option: str = "1 Page"  # 1 Page, 2 Pages, Auto

@dataclass
class ResumeData:
    id: Optional[int] = None
    title: str = "My Resume"
    personal_info: PersonalInfo = field(default_factory=PersonalInfo)
    summary: str = ""
    experiences: List[Experience] = field(default_factory=list)
    educations: List[Education] = field(default_factory=list)
    skill_categories: List[SkillCategory] = field(default_factory=list)
    projects: List[Project] = field(default_factory=list)
    certifications: List[Certification] = field(default_factory=list)
    languages: List[Language] = field(default_factory=list)
    achievements: List[str] = field(default_factory=list)
    volunteer_experience: List[str] = field(default_factory=list)
    interests: List[str] = field(default_factory=list)
    target_job_description: str = ""
    style: StyleConfig = field(default_factory=StyleConfig)

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), indent=2)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "ResumeData":
        personal_info = PersonalInfo(**data.get("personal_info", {}))
        style = StyleConfig(**data.get("style", {}))
        
        experiences = [Experience(**e) for e in data.get("experiences", [])]
        educations = [Education(**ed) for ed in data.get("educations", [])]
        skill_cats = [SkillCategory(**sc) for sc in data.get("skill_categories", [])]
        projects = [Project(**p) for p in data.get("projects", [])]
        certs = [Certification(**c) for c in data.get("certifications", [])]
        langs = [Language(**l) for l in data.get("languages", [])]

        return cls(
            id=data.get("id"),
            title=data.get("title", "My Resume"),
            personal_info=personal_info,
            summary=data.get("summary", ""),
            experiences=experiences,
            educations=educations,
            skill_categories=skill_cats,
            projects=projects,
            certifications=certs,
            languages=langs,
            achievements=data.get("achievements", []),
            volunteer_experience=data.get("volunteer_experience", []),
            interests=data.get("interests", []),
            target_job_description=data.get("target_job_description", ""),
            style=style,
        )

def get_demo_resume() -> ResumeData:
    """Generates a complete, realistic demo resume."""
    return ResumeData(
        title="Software Developer - Full Demo",
        personal_info=PersonalInfo(
            full_name="Alex Morgan",
            professional_title="Senior Full-Stack Engineer",
            email="alex.morgan@example.com",
            phone="+1 (555) 019-2834",
            location="San Francisco, CA",
            linkedin="linkedin.com/in/alexmorgan-demo",
            github="github.com/alexmorgan-demo",
            portfolio="alexmorgan.dev",
            website="https://alexmorgan.dev",
            career_level="Senior",
            open_to_relocation=True
        ),
        summary=(
            "Accomplished Senior Full-Stack Engineer with 6+ years of experience "
            "architecting high-performance web applications and cloud services. "
            "Expert in Python, TypeScript, and microservices architecture with a track record "
            "of optimizing pipeline throughput and leading agile development teams."
        ),
        experiences=[
            Experience(
                job_title="Senior Software Engineer",
                company="TechCorp Solutions",
                location="San Francisco, CA",
                start_date="2022-03",
                end_date="Present",
                is_current=True,
                description="Lead engineer for high-throughput streaming and transaction APIs.",
                achievements=[
                    "Spearheaded migration to microservices, reducing API endpoint latency by 38%.",
                    "Mentored a team of 6 junior developers on modern clean code standards.",
                    "Automated CI/CD deployment pipelines cutting deployment windows from 2 hrs to 15 mins."
                ]
            ),
            Experience(
                job_title="Full Stack Developer",
                company="DataStream Tech",
                location="Austin, TX",
                start_date="2019-06",
                end_date="2022-02",
                is_current=False,
                description="Engineered real-time analytics web dashboards for enterprise clients.",
                achievements=[
                    "Developed client-facing streaming interface using React, WebSockets, and FastAPI.",
                    "Optimized database indexing and queries, decreasing server CPU load by 45%."
                ]
            )
        ],
        educations=[
            Education(
                degree="B.S. in Computer Science",
                institution="UC Berkeley",
                location="Berkeley, CA",
                start_date="2015-08",
                end_date="2019-05",
                gpa="3.85 / 4.0",
                description="Graduated with High Honors. Teaching Assistant for Data Structures."
            )
        ],
        skill_categories=[
            SkillCategory("Languages", ["Python", "TypeScript", "SQL", "Go", "HTML/CSS"]),
            SkillCategory("Frameworks & Tools", ["FastAPI", "React", "Docker", "Kubernetes", "PostgreSQL", "Redis"]),
            SkillCategory("Leadership & Methodology", ["System Architecture", "Agile/Scrum", "CI/CD", "Code Review"])
        ],
        projects=[
            Project(
                name="ResumeForge",
                description="Open-source AI-assisted resume creation platform built with Python & Streamlit.",
                technologies=["Python", "Streamlit", "ReportLab", "SQLite"],
                project_url="https://resumeforge.demo",
                github_url="github.com/alexmorgan-demo/resumeforge"
            )
        ],
        certifications=[
            Certification("AWS Certified Solutions Architect", "Amazon Web Services", "2023-05", "https://aws.amazon.com/verify")
        ],
        languages=[
            Language("English", "Native"),
            Language("Spanish", "Intermediate")
        ],
        achievements=[
            "Winner of TechCrunch Disrupt Hackathon 2021",
            "Published research paper on distributed caching in IEEE Software"
        ],
        style=StyleConfig(template_id="modern_accent", primary_color="#1E3A8A")
    )